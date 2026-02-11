/**
 * OpenClaw Hydration Plugin
 *
 * Invisible context hydration - users drop data, everything else happens automatically.
 * Fetches drops from oPOErator Hub API and injects context before every prompt.
 * Registers hub_api tool for full agent access to all Hub endpoints.
 */

import type { OpenClawPluginApi } from "openclaw/plugin-sdk";
import { Type } from "@sinclair/typebox";
import { readdir, readFile, stat } from "node:fs/promises";
import { homedir } from "node:os";
import { join } from "node:path";
import { hydrationConfigSchema, type HydrationConfig } from "./config.js";

// ============================================================================
// Types
// ============================================================================

type Drop = {
  id: string;
  source: string;
  content: string;
  timestamp: string;
  tags?: string[];
};

type HydrationContext = {
  drops: Drop[];
  sessions: any[];
  digests: any[];
  timestamp: number;
};

// ============================================================================
// oPOErator Hub Client
// ============================================================================

type HydrationResponse = {
  status: string;
  user_id: string | null;
  matched?: boolean;
  drops: Drop[];
  sessions: any[];
  digests: any[];
};

class HubClient {
  constructor(
    private baseUrl: string,
    private apiKey: string,
    private fallbackUserId: string,
    private logger: { info: (msg: string) => void; warn: (msg: string) => void },
  ) {}

  /**
   * Fetch hydration context by user_id (fallback/default mode).
   */
  async getHydrationContext(
    dropsLimit: number = 15,
    sessionsLimit: number = 5,
    digestsLimit: number = 3,
  ): Promise<HydrationResponse | null> {
    if (!this.fallbackUserId) return null;

    try {
      const url = `${this.baseUrl}/api/hydrate/${encodeURIComponent(this.fallbackUserId)}?drops_limit=${dropsLimit}&sessions_limit=${sessionsLimit}&digests_limit=${digestsLimit}`;
      const response = await fetch(url, {
        headers: {
          "Content-Type": "application/json",
          ...(this.apiKey && { "X-API-Key": this.apiKey }),
        },
      });

      if (!response.ok) {
        this.logger.warn(`hydration: API ${response.status} for /api/hydrate`);
        return null;
      }

      return response.json();
    } catch (err) {
      this.logger.warn(`hydration: API error for /api/hydrate: ${err}`);
      return null;
    }
  }

  /**
   * Verify a CONNECT code and link phone to user account.
   * Called when user texts "CONNECT ABC123" to the channel.
   */
  async verifyCode(params: {
    code: string;
    phone: string;
    channel: string;
  }): Promise<{ status: string; user_id?: string; message?: string } | null> {
    try {
      const url = `${this.baseUrl}/api/channels/verify-code`;
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...(this.apiKey && { "X-API-Key": this.apiKey }),
        },
        body: JSON.stringify({
          code: params.code,
          phone: params.phone,
          channel: params.channel,
        }),
      });

      return response.json();
    } catch (err) {
      this.logger.warn(`hydration: verifyCode API error: ${err}`);
      return null;
    }
  }

  /**
   * Check if this is a first-time sender (no user_id found for identity).
   */
  async isFirstTimeSender(
    identityType: "phone" | "email",
    identityValue: string,
  ): Promise<boolean> {
    const response = await this.getHydrationByIdentity(identityType, identityValue, 1, 0, 0);
    return !response || !response.matched || !response.user_id;
  }

  /**
   * Ingest a drop to Hub (zero AI tokens).
   * Used by message_received hook to capture incoming messages.
   */
  async ingestDrop(params: {
    identityType: "phone" | "email";
    identityValue: string;
    content: string;
    source: string;
    metadata?: Record<string, unknown>;
  }): Promise<{ status: string; vault_id?: number } | null> {
    try {
      const url = `${this.baseUrl}/api/ingest`;
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...(this.apiKey && { "X-API-Key": this.apiKey }),
        },
        body: JSON.stringify({
          source: params.source,
          content: params.content,
          identity_type: params.identityType,
          identity_value: params.identityValue,
          metadata: params.metadata,
        }),
      });

      if (!response.ok) {
        this.logger.warn(`hydration: ingest API ${response.status}`);
        return null;
      }

      return response.json();
    } catch (err) {
      this.logger.warn(`hydration: ingest API error: ${err}`);
      return null;
    }
  }

  /**
   * Fetch hydration context by identity (phone or email).
   * This powers multi-user hydration - each sender gets their own context.
   */
  async getHydrationByIdentity(
    identityType: "phone" | "email",
    identityValue: string,
    dropsLimit: number = 15,
    sessionsLimit: number = 5,
    digestsLimit: number = 3,
  ): Promise<HydrationResponse | null> {
    try {
      const params = new URLSearchParams({
        identity_type: identityType,
        identity_value: identityValue,
        drops_limit: String(dropsLimit),
        sessions_limit: String(sessionsLimit),
        digests_limit: String(digestsLimit),
      });
      const url = `${this.baseUrl}/api/hydrate/by-identity?${params}`;
      const response = await fetch(url, {
        headers: {
          "Content-Type": "application/json",
          ...(this.apiKey && { "X-API-Key": this.apiKey }),
        },
      });

      if (!response.ok) {
        this.logger.warn(`hydration: API ${response.status} for /api/hydrate/by-identity`);
        return null;
      }

      return response.json();
    } catch (err) {
      this.logger.warn(`hydration: API error for /api/hydrate/by-identity: ${err}`);
      return null;
    }
  }
}

// ============================================================================
// Hydration Engine
// ============================================================================

class HydrationEngine {
  private cache: HydrationContext | null = null;
  private cacheTime = 0;
  private hubClient: HubClient | null = null;
  // Per-identity cache: identity -> { context, timestamp }
  private identityCache = new Map<string, { context: HydrationContext; timestamp: number }>();

  constructor(
    private config: HydrationConfig,
    private logger: { info: (msg: string) => void; warn: (msg: string) => void },
  ) {
    // Initialize Hub client if configured (userId is now optional fallback)
    if (config.hubUrl && config.apiKey) {
      this.hubClient = new HubClient(config.hubUrl, config.apiKey, config.userId || "", logger);
    }
  }

  /**
   * Check if message is a CONNECT command (e.g., "CONNECT ABC123").
   * Returns the code if found, null otherwise.
   */
  parseConnectCommand(content: string): string | null {
    const match = content
      .trim()
      .toUpperCase()
      .match(/^CONNECT\s+([A-Z0-9]{6})$/);
    return match ? match[1] : null;
  }

  /**
   * Handle CONNECT command - verify code and link phone to account.
   */
  async handleConnectCommand(params: {
    code: string;
    from: string;
    channel: string;
  }): Promise<{ success: boolean; message: string }> {
    if (!this.hubClient) {
      return { success: false, message: "Service unavailable" };
    }

    const identity = this.extractIdentityFromSessionKey(params.from);
    if (!identity || identity.type !== "phone") {
      return { success: false, message: "Could not identify your phone number" };
    }

    const result = await this.hubClient.verifyCode({
      code: params.code,
      phone: identity.value,
      channel: params.channel,
    });

    if (result && result.status === "ok") {
      this.logger.info(`hydration: connected phone ${identity.value} to user ${result.user_id}`);
      return {
        success: true,
        message:
          "Phone connected successfully! Your messages will now be saved as drops and included in your daily digest.",
      };
    }

    return {
      success: false,
      message:
        result?.message ||
        "Invalid or expired code. Please generate a new one from the DropAnywhere dashboard.",
    };
  }

  /**
   * Check if this is a first-time sender.
   */
  async isFirstTimeSender(from: string): Promise<boolean> {
    if (!this.hubClient) return true;

    const identity = this.extractIdentityFromSessionKey(from);
    if (!identity) return true;

    return this.hubClient.isFirstTimeSender(identity.type, identity.value);
  }

  /**
   * Get welcome message for first-time senders.
   */
  getWelcomeMessage(): string {
    return `Welcome to DropAnywhere!

I'm your personal drop capture system. Any message you send here will be saved to your vault and included in your daily digest email.

To link this number to your existing DropAnywhere account:
1. Go to drop-anywhere.com/dashboard
2. Click "Connect Channels"
3. Follow the instructions to get a CONNECT code
4. Text "CONNECT [YOUR-CODE]" back here

Or just start dropping! Your messages will be saved and you can claim them later.`;
  }

  /**
   * Capture an incoming message as a drop (zero AI tokens).
   * Called by message_received hook.
   */
  async captureMessage(params: {
    from: string;
    content: string;
    channel: string;
    metadata?: Record<string, unknown>;
  }): Promise<boolean> {
    if (!this.hubClient) {
      this.logger.warn("hydration: capture skipped - no Hub client configured");
      return false;
    }

    // Extract identity from 'from' field
    const identity = this.extractIdentityFromSessionKey(params.from);
    if (!identity) {
      this.logger.warn(`hydration: capture skipped - no identity in: ${params.from}`);
      return false;
    }

    // Ingest to Hub (zero AI tokens)
    const result = await this.hubClient.ingestDrop({
      identityType: identity.type,
      identityValue: identity.value,
      content: params.content,
      source: params.channel,
      metadata: params.metadata,
    });

    if (result && result.status === "ok") {
      this.logger.info(
        `hydration: captured drop for ${identity.type}:${identity.value} (vault_id: ${result.vault_id})`,
      );
      return true;
    }

    return false;
  }

  /**
   * Extract identity from sessionKey.
   * Session keys look like: "agent:default:+15551234567" or just "+15551234567"
   * Returns { type: "phone"|"email", value: string } or null if not extractable.
   */
  extractIdentityFromSessionKey(
    sessionKey?: string,
  ): { type: "phone" | "email"; value: string } | null {
    if (!sessionKey) return null;

    // Try to extract phone number (E.164 format or with common prefixes)
    const phoneMatch = sessionKey.match(/(\+?\d{10,15})/);
    if (phoneMatch) {
      let phone = phoneMatch[1];
      // Normalize to E.164 if it looks like a US number without +
      if (!phone.startsWith("+") && phone.length === 10) {
        phone = `+1${phone}`;
      } else if (!phone.startsWith("+") && phone.length === 11 && phone.startsWith("1")) {
        phone = `+${phone}`;
      }
      return { type: "phone", value: phone };
    }

    // Try to extract email
    const emailMatch = sessionKey.match(/([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})/);
    if (emailMatch) {
      return { type: "email", value: emailMatch[1].toLowerCase() };
    }

    return null;
  }

  /**
   * Hydrate context for a specific identity.
   * This is used for multi-user mode where each sender gets their own context.
   */
  async hydrateForIdentity(identity: {
    type: "phone" | "email";
    value: string;
  }): Promise<HydrationContext> {
    const now = Date.now();
    const cacheTtl = (this.config.cacheTtl ?? 60) * 1000;
    const cacheKey = `${identity.type}:${identity.value}`;

    // Check identity-specific cache
    const cached = this.identityCache.get(cacheKey);
    if (cached && now - cached.timestamp < cacheTtl) {
      return cached.context;
    }

    let drops: Drop[] = [];
    let sessions: any[] = [];
    let digests: any[] = [];

    // Fetch from Hub by identity
    if (this.hubClient) {
      const hubContext = await this.hubClient.getHydrationByIdentity(
        identity.type,
        identity.value,
        this.config.maxDrops ?? 15,
        5,
        3,
      );
      if (hubContext && hubContext.matched) {
        drops = hubContext.drops || [];
        sessions = hubContext.sessions || [];
        digests = hubContext.digests || [];
        this.logger.info(
          `hydration: found user ${hubContext.user_id} for ${identity.type}:${identity.value}`,
        );
      }
    }

    const context: HydrationContext = { drops, sessions, digests, timestamp: now };
    this.identityCache.set(cacheKey, { context, timestamp: now });

    return context;
  }

  private resolvePath(path: string): string {
    if (path.startsWith("~")) {
      return join(homedir(), path.slice(1));
    }
    return path;
  }

  private async scanLocalDrops(): Promise<Drop[]> {
    const drops: Drop[] = [];
    const maxAge = (this.config.maxDropAge ?? 24) * 60 * 60 * 1000;
    const now = Date.now();

    for (const dropPath of this.config.dropPaths ?? []) {
      const resolvedPath = this.resolvePath(dropPath);

      try {
        const files = await readdir(resolvedPath);

        for (const file of files) {
          if (file.startsWith(".") || file.startsWith("_")) continue;

          const filePath = join(resolvedPath, file);
          const fileStat = await stat(filePath).catch(() => null);

          if (!fileStat || !fileStat.isFile()) continue;

          const age = now - fileStat.mtimeMs;
          if (age > maxAge) continue;

          const ext = file.split(".").pop()?.toLowerCase() ?? "";
          let content = "";

          if (["txt", "md", "json"].includes(ext)) {
            try {
              content = await readFile(filePath, "utf-8");
              if (content.length > 2000) {
                content = content.slice(0, 2000) + "...[truncated]";
              }
            } catch {
              content = `[Error reading file]`;
            }
          } else if (["m4a", "mp3", "wav"].includes(ext)) {
            content = `[Voice: ${file}]`;
          } else if (["jpg", "jpeg", "png", "gif"].includes(ext)) {
            content = `[Image: ${file}]`;
          }

          drops.push({
            id: file,
            source: "local",
            content,
            timestamp: new Date(fileStat.mtimeMs).toISOString(),
          });
        }
      } catch (err) {
        this.logger.warn(`hydration: failed to scan ${dropPath}: ${err}`);
      }
    }

    drops.sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime());
    return drops.slice(0, this.config.maxDrops ?? 10);
  }

  private async loadCheckpoint(): Promise<string | null> {
    if (!this.config.checkpointPath) return null;

    const resolvedPath = this.resolvePath(this.config.checkpointPath);

    try {
      const files = await readdir(resolvedPath);
      const checkpoints = files
        .filter((f) => f.includes("CHECKPOINT") && f.endsWith(".md"))
        .sort()
        .reverse();

      if (checkpoints.length === 0) return null;

      const content = await readFile(join(resolvedPath, checkpoints[0]), "utf-8");
      return content.length > 4000 ? content.slice(0, 4000) + "\n...[truncated]" : content;
    } catch (err) {
      this.logger.warn(`hydration: failed to load checkpoint: ${err}`);
      return null;
    }
  }

  async hydrate(): Promise<HydrationContext> {
    const now = Date.now();
    const cacheTtl = (this.config.cacheTtl ?? 60) * 1000;

    if (this.cache && now - this.cacheTime < cacheTtl) {
      return this.cache;
    }

    let drops: Drop[] = [];
    let sessions: any[] = [];
    let digests: any[] = [];

    // Fetch from Hub if configured (single optimized call)
    if (this.hubClient) {
      const hubContext = await this.hubClient.getHydrationContext(this.config.maxDrops ?? 15, 5, 3);
      if (hubContext) {
        drops = hubContext.drops || [];
        sessions = hubContext.sessions || [];
        digests = hubContext.digests || [];
      }
    }

    // Also scan local paths if configured
    if (this.config.dropPaths && this.config.dropPaths.length > 0) {
      const localDrops = await this.scanLocalDrops();
      drops = [...drops, ...localDrops].slice(0, this.config.maxDrops ?? 10);
    }

    this.cache = { drops, sessions, digests, timestamp: now };
    this.cacheTime = now;

    return this.cache;
  }

  buildContext(ctx: HydrationContext): string {
    const parts: string[] = [];

    // Recent drops
    if (ctx.drops.length > 0) {
      const dropSummary = ctx.drops
        .slice(0, 10)
        .map((d) => {
          const preview = d.content.slice(0, 200).replace(/\n/g, " ");
          return `- [${d.source}] ${preview}`;
        })
        .join("\n");

      parts.push(`<recent-drops count="${ctx.drops.length}">\n${dropSummary}\n</recent-drops>`);
    }

    // Recent sessions (titles only)
    if (ctx.sessions.length > 0) {
      const sessionList = ctx.sessions
        .slice(0, 5)
        .map((s) => `- ${s.name || s.id}`)
        .join("\n");

      parts.push(`<recent-sessions>\n${sessionList}\n</recent-sessions>`);
    }

    // Latest digest summary
    if (ctx.digests.length > 0) {
      const latest = ctx.digests[0];
      parts.push(
        `<latest-digest date="${latest.date}">\n${latest.summary || "No summary"}\n</latest-digest>`,
      );
    }

    return parts.join("\n\n");
  }
}

// ============================================================================
// Hub API Response Formatter
// ============================================================================

/**
 * Format Hub API JSON responses into clean, model-friendly text.
 * Known endpoints get structured summaries; unknown endpoints get pretty JSON.
 */
function formatHubResponse(path: string, json: any): string {
  // Tasks endpoint
  if (path.match(/\/api\/ops\/tasks/) && json.tasks) {
    const tasks = json.tasks as any[];
    if (tasks.length === 0) return "No tasks found.";

    const lines = [`${tasks.length} task(s):\n`];
    for (const t of tasks) {
      lines.push(`- [${t.priority || "normal"}] ${t.status || "?"}: ${t.title || "untitled"}`);
      lines.push(
        `  assignee: ${t.assignee || "?"} | repo: ${t.target_repo || "?"} | created_by: ${t.created_by || "?"}`,
      );
      if (t.description) {
        lines.push(`  desc: ${t.description.slice(0, 150)}`);
      }
      if (t.result) {
        lines.push(`  result: ${t.result.slice(0, 150)}`);
      }
      lines.push(`  id: ${t.id || "?"} | ts: ${t.ts || "?"}`);
    }
    return lines.join("\n");
  }

  // Messages endpoint
  if (path.match(/\/api\/ops\/messages/) && json.messages) {
    const msgs = json.messages as any[];
    if (msgs.length === 0) return "No messages found.";

    const lines = [`${msgs.length} message(s):\n`];
    for (const m of msgs) {
      lines.push(`- [${m.priority || "normal"}] from=${m.from || "?"} (${m.ts || "?"})`);
      lines.push(`  ${(m.message || "").slice(0, 300)}`);
    }
    return lines.join("\n");
  }

  // Agent drops endpoint
  if (path.match(/\/api\/agent-drops/) && json.drops) {
    const drops = json.drops as any[];
    if (drops.length === 0) return "No agent drops found.";

    const lines = [`${drops.length} drop(s):\n`];
    for (const d of drops) {
      lines.push(
        `- [${d.type || "?"}] from=${d.from || d.from_agent || "?"} (${d.timestamp || d.ts || "?"})`,
      );
      lines.push(`  ${(d.content || d.title || "").slice(0, 200)}`);
    }
    return lines.join("\n");
  }

  // Health / status / dashboard — return pretty JSON
  if (path.match(/\/api\/ops\/dashboard|\/api\/admin\/stats|\/health/)) {
    return JSON.stringify(json, null, 2);
  }

  // Default: pretty-print JSON (compact for small, indented for readable)
  const compact = JSON.stringify(json);
  if (compact.length < 2000) {
    return JSON.stringify(json, null, 2);
  }
  return compact;
}

// ============================================================================
// Plugin Definition
// ============================================================================

const hydrationPlugin = {
  id: "hydration",
  name: "Context Hydration",
  description: "Invisible context hydration from oPOErator Hub and local drops",
  kind: "hydration" as const,
  configSchema: hydrationConfigSchema,

  register(api: OpenClawPluginApi) {
    const rawConfig = api.pluginConfig ?? {};
    const cfg: HydrationConfig = {
      enabled: rawConfig.enabled ?? true,
      hubUrl: rawConfig.hubUrl || "https://hub-production-f423.up.railway.app",
      apiKey: rawConfig.apiKey,
      userId: rawConfig.userId,
      dropPaths: rawConfig.dropPaths ?? [],
      checkpointPath: rawConfig.checkpointPath,
      maxDropAge: rawConfig.maxDropAge ?? 24,
      maxDrops: rawConfig.maxDrops ?? 10,
      cacheTtl: rawConfig.cacheTtl ?? 60,
      captureEnabled: rawConfig.captureEnabled ?? false,
      captureChannels: rawConfig.captureChannels ?? [],
    };

    if (!cfg.enabled) {
      api.logger.info("hydration: plugin disabled");
      return;
    }

    const engine = new HydrationEngine(cfg, api.logger);

    const sourceDesc = cfg.hubUrl
      ? `hub: ${cfg.hubUrl}`
      : `local: ${cfg.dropPaths?.length ?? 0} paths`;
    api.logger.info(`hydration: plugin registered (${sourceDesc}, cache: ${cfg.cacheTtl}s)`);

    // ========================================================================
    // Lifecycle Hooks
    // ========================================================================

    api.on("before_agent_start", async (event, agentCtx) => {
      if (!event.prompt || event.prompt.length < 3) return;

      // IMPORTANT: prependContext gets prepended directly to the user's prompt text.
      // Injecting large context here causes small models (Haiku) to echo it back
      // instead of responding. Keep this minimal — the agent has hub_api tool
      // to fetch full context (memory, drops, dashboard) when it needs it.
    });

    // ========================================================================
    // Hub API Tool — gives agent full access to all Hub endpoints
    // ========================================================================

    if (cfg.hubUrl && cfg.apiKey) {
      const hubBaseUrl = cfg.hubUrl.replace(/\/+$/, "");

      api.registerTool(
        {
          name: "hub_api",
          description: `Make authenticated API calls to the oPOErator Hub (${hubBaseUrl}).

Key endpoints:
- GET /api/memory/context/openclaw — your persistent memory (condensed markdown)
- GET /api/memory?agent=openclaw&search=keyword — search memories
- POST /api/memory — write memory: {agent, namespace, key, content, tags[]}
- DELETE /api/memory/{id} — delete a memory
- GET /api/ops/dashboard — system health, digest pipeline, error rates
- GET /api/ops/tasks?assignee=openclaw&status=pending — your pending tasks
- POST /api/ops/propose — propose an action for approval: {title, description, action_type}
- POST /api/ops/messages — post status update: {content, from_agent}
- GET /api/ops/proposals?status=pending — pending proposals
- POST /api/agent-drops — create drop: {from_agent, drop_type, title, content, tags[]}
- GET /api/agent-drops?from_agent=openclaw — list drops
- POST /api/alerts — send alert: {project, type, message, severity}
- POST /api/alerts/daily-summary — trigger daily summary
- GET /api/admin/stats — user stats, drop counts, digest stats
- POST /api/ingest — ingest a drop for a user
- GET /api/search?q=keyword&user_id=X — search user drops
- POST /api/dcs/code-task — create code task for DCS agent
- GET /api/tasks/pending — pending HITL tasks
- POST /api/tasks/approve — approve a pending task

Auth is handled automatically via X-API-Key header.`,
          parameters: Type.Object({
            method: Type.Unsafe<"GET" | "POST" | "PATCH" | "PUT" | "DELETE">({
              type: "string",
              enum: ["GET", "POST", "PATCH", "PUT", "DELETE"],
              description: "HTTP method",
            }),
            path: Type.String({
              description: "API path starting with /api/ (e.g. /api/memory/context/openclaw)",
            }),
            body: Type.Optional(
              Type.String({
                description: "JSON request body (for POST/PATCH/PUT). Must be valid JSON string.",
              }),
            ),
            query: Type.Optional(
              Type.String({
                description:
                  'Query parameters as JSON object (e.g. {"agent": "openclaw", "limit": "10"}). Values are stringified automatically.',
              }),
            ),
          }),
          async execute(_id: string, params: Record<string, unknown>) {
            const method = (
              typeof params.method === "string" ? params.method : "GET"
            ).toUpperCase();
            const path = typeof params.path === "string" ? params.path : "";

            if (!path.startsWith("/api/")) {
              return { result: JSON.stringify({ error: "Path must start with /api/" }) };
            }

            // Build URL with optional query params
            let url = `${hubBaseUrl}${path}`;
            if (typeof params.query === "string" && params.query.trim()) {
              try {
                const qp = JSON.parse(params.query);
                const qs = new URLSearchParams();
                for (const [k, v] of Object.entries(qp)) {
                  qs.append(k, String(v));
                }
                const qsStr = qs.toString();
                if (qsStr) {
                  url += (url.includes("?") ? "&" : "?") + qsStr;
                }
              } catch {
                return { result: JSON.stringify({ error: "Invalid query JSON" }) };
              }
            }

            // Build request options
            const opts: RequestInit = {
              method,
              headers: {
                "Content-Type": "application/json",
                Accept: "application/json",
                "X-API-Key": cfg.apiKey!,
              },
            };

            if (typeof params.body === "string" && params.body.trim() && method !== "GET") {
              opts.body = params.body;
            }

            try {
              const response = await fetch(url, opts);
              const text = await response.text();

              if (!response.ok) {
                return {
                  result: `ERROR: HTTP ${response.status} for ${method} ${path}\n${text.slice(0, 500)}`,
                };
              }

              // Try to parse as JSON and format for readability
              try {
                const json = JSON.parse(text);
                const formatted = formatHubResponse(path, json);
                if (formatted.length > 8000) {
                  return { result: formatted.slice(0, 8000) + "\n...[truncated]" };
                }
                return { result: formatted };
              } catch {
                // Not JSON — return raw text truncated
                const truncated =
                  text.length > 8000
                    ? text.slice(0, 8000) + "\n...[truncated, " + text.length + " bytes total]"
                    : text;
                return { result: truncated };
              }
            } catch (err) {
              return {
                result: `ERROR: Request failed: ${err instanceof Error ? err.message : String(err)}`,
              };
            }
          },
        } as any,
        { name: "hub_api" },
      );

      api.logger.info(`hydration: registered hub_api tool → ${hubBaseUrl}`);
    }

    // ========================================================================
    // Message Capture Hook (Zero AI Tokens)
    // ========================================================================

    if (cfg.captureEnabled) {
      api.logger.info(
        `hydration: capture enabled for channels: ${cfg.captureChannels?.length ? cfg.captureChannels.join(", ") : "all"}`,
      );

      // Track first-time senders to avoid repeated welcome messages
      const welcomedSenders = new Set<string>();

      api.on("message_received", async (event) => {
        try {
          // Filter by channel if configured
          const channel = (event.metadata?.channel as string) || "unknown";
          if (cfg.captureChannels && cfg.captureChannels.length > 0) {
            if (!cfg.captureChannels.includes(channel)) {
              return; // Skip channels not in allowlist
            }
          }

          // Skip empty or very short messages
          if (!event.content || event.content.length < 2) {
            return;
          }

          // 1. Check for CONNECT command (e.g., "CONNECT ABC123")
          const connectCode = engine.parseConnectCommand(event.content);
          if (connectCode) {
            const result = await engine.handleConnectCommand({
              code: connectCode,
              from: event.from,
              channel,
            });

            // Return response to user (this triggers auto-reply)
            return {
              reply: result.message,
              skipAgent: true, // Don't invoke AI for CONNECT commands
            };
          }

          // 2. Check if first-time sender (show welcome message)
          const senderKey = event.from;
          if (!welcomedSenders.has(senderKey)) {
            const isFirstTime = await engine.isFirstTimeSender(event.from);
            welcomedSenders.add(senderKey); // Mark as welcomed (even if not first time)

            if (isFirstTime) {
              api.logger.info(`hydration: first-time sender ${event.from}`);
              // Still capture the message as a drop
              await engine.captureMessage({
                from: event.from,
                content: event.content,
                channel,
                metadata: event.metadata,
              });

              // Return welcome message
              return {
                reply: engine.getWelcomeMessage(),
                skipAgent: false, // Allow AI to also respond if configured
              };
            }
          }

          // 3. Normal capture - save as drop (zero AI tokens)
          await engine.captureMessage({
            from: event.from,
            content: event.content,
            channel,
            metadata: event.metadata,
          });
        } catch (err) {
          api.logger.warn(`hydration: capture error: ${err}`);
        }
      });
    }

    // ========================================================================
    // CLI Commands
    // ========================================================================

    api.registerCli(
      ({ program }) => {
        const hydrate = program.command("hydrate").description("Context hydration commands");

        hydrate
          .command("status")
          .description("Show hydration status")
          .action(async () => {
            const ctx = await engine.hydrate();
            console.log(`Drops: ${ctx.drops.length}`);
            console.log(`Sessions: ${ctx.sessions.length}`);
            console.log(`Digests: ${ctx.digests.length}`);
            console.log(`Last updated: ${new Date(ctx.timestamp).toISOString()}`);
          });

        hydrate
          .command("drops")
          .description("List recent drops")
          .action(async () => {
            const ctx = await engine.hydrate();
            for (const drop of ctx.drops) {
              console.log(`[${drop.source}] ${drop.content.slice(0, 80)}...`);
            }
          });

        hydrate
          .command("preview")
          .description("Preview hydration context")
          .action(async () => {
            const ctx = await engine.hydrate();
            const context = engine.buildContext(ctx);
            console.log(context || "(no context to inject)");
          });
      },
      { commands: ["hydrate"] },
    );

    // ========================================================================
    // Service
    // ========================================================================

    api.registerService({
      id: "hydration",
      start: () => {
        api.logger.info("hydration: service started");
      },
      stop: () => {
        api.logger.info("hydration: service stopped");
      },
    });
  },
};

export default hydrationPlugin;
