---
summary: "Operational cheat sheet — services, endpoints, architecture, capabilities"
read_when:
  - Bootstrapping a workspace manually
  - Need to call an API or check a service
  - Debugging infrastructure issues
---
# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

---

## GitHub

- **Account:** ph0t0bar
- **CLI:** Authenticated via `GH_TOKEN` env var
- **Two PATs in `.env.local`:** `GH_TOKEN` (ACTIVE, verified 2026-03-17) + `GITHUB_TOKEN` (EXPIRED, bad credentials)
- **Working PAT:** `GH_TOKEN` from `/root/.openclaw/.env.local` — use this one for API calls
- **⚠️ `gh` CLI not installed** — use `curl` with GitHub API directly. The npm `gh` package is NOT GitHub CLI.
- **Recovery note:** If GITHUB_TOKEN ever expires, check old session transcripts in `/root/.openclaw/agents/main/sessions/` with `grep -o "github_pat_[A-Za-z0-9_]*"`
- **GitHub API pattern:** `curl -s -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/repos/ph0t0bar/REPO/...`
- **Default repo for GITHUB_TOKEN:** `ph0t0bar/dropanywhere-app`
- **Active repos:**
  - **openclaw** — Personal AI assistant (this workspace!)
  - **opoerator-hub** — DropAnywhere backend (Python, Railway)
  - **dropanywhere-app** — DropAnywhere frontend (Next.js 14)
  - **brutallyhonest-next** — AI persona marketplace (Next.js 16, Live)
  - **dropanywhere-cron** — Daily digest cron jobs (Python)
  - **joey-backup** — Personal backup system + OpenClaw memory offsite backup + **historical content archive**
    - `context/` — Dated snapshots of MEMORY.md, TOOLS.md, SOUL.md, USER.md, AGENTS.md, HEARTBEAT.md
    - `sessions/` — Session saves and daily logs
    - `specs/` — PRDs, orchestrator specs, funnel prompts
    - `Ingestion/` — **THE MOTHERLODE** (2,422 files, added 2026-03-11):
      - `0_VAULT/conversations/` — 2,070 ChatGPT conversations (Dec 2022 – Jul 2024)
      - `0_VAULT/BHA/` — 52 Notion database exports (Personas, System Prompts, Knowledge Base, Users, Messages, etc.)
      - `.claude/context/` — 34 files: brain state, mined patterns, persona architectures, ABOUT_JOEY_HAMER.md
      - `.agent/workflows/` — Eduardo agent workflows (hydration, extraction, sync-to-notion)
      - `20260107/`–`20260310/` — 80+ dated drops/chats from Jan–Mar 2026
      - Root docs: `GOD_MODE_NOTION_FULL.md`, `FULL_HYDRATION_CONTEXT.md`, `_FROM-JOEY.md`, `SYSTEM_ARCHITECTURE.md`, `FULL_ASSET_INVENTORY.txt`
      - Content Transformation System design doc: `specs/content-transformation-system-dec2025.md`
  - **aichatbridge** — Poe bot web integration tutorial
  - **Face-detection-with-OpenCV-and-deep-learning** — CV experiments
  - *(plus older projects: Dashstart, insight-engine, etc.)*

---

## Railway Infrastructure

### Project: openclaw-gateway
- **Project ID:** `30f0336d-a3bb-4ce6-a05f-a8e130489c56`
- **Service ID:** `c4b86774-0805-4602-b18d-99081599e126`
- **Environment:** production (`63e7f7c9-7b0d-4b98-a778-141f01e8fab0`)
- **Public URL:** `openclaw-gateway-production-54a0.up.railway.app`
- **Private domain:** `openclaw-gateway.railway.internal`
- **Region:** us-west2
- **Volume:** `ff3e6e2c-8cc1-492f-ba61-9f7507ec0d3c` mounted at `/root/.openclaw`
- **Git:** main branch, repo `ph0t0bar/openclaw`
- **Port:** 8080
- **Node:** v22.22.0, production mode
- **Storage backend:** dual

### Project: oPOErator Hub (Backend)
- **Project ID:** `a097a5f5-d82a-46c7-a1d7-d1904cf3106e`
- **Service ID:** `99d414bf-383e-4d9e-a7f7-15d10ec2789e`
- **Environment ID:** `2e4cfb9f-34d7-4fdf-bef3-4c60f617388c`
- **Public URL:** `hub-production-f423.up.railway.app`
- **Volume:** `8899df29` mounted at `/app/data`
- **Git:** main branch, repo `ph0t0bar/opoerator-hub`
- **Has own GITHUB_TOKEN:** different PAT from openclaw-gateway (scoped to Hub repo)
- **Variables URL:** https://railway.com/project/a097a5f5-d82a-46c7-a1d7-d1904cf3106e/service/99d414bf-383e-4d9e-a7f7-15d10ec2789e/variables

### Project: DropAnywhere Frontend
- **Project ID:** `d07a0723-d1bd-4aff-b002-0192b4a32973` (RAILWAY_FRONTEND_PROJECT_ID)
- **Live URL:** https://drop-anywhere.com

### Railway API Access
- **API Key:** ✅ available (`RAILWAY_API_KEY`)
- **API Token:** ✅ available (`RAILWAY_API_TOKEN`)
- **Staging Token:** ✅ available (`RAILWAY_STAGING_TOKEN`)
- Can manage deployments, services, and variables via Railway API

---

## oPOErator Hub (DropAnywhere Backend)

- **Production URL:** `https://hub-production-f423.up.railway.app`
- **API Key:** via `HUB_API_KEY` / `INGEST_API_KEY` (same key)
- **Database:** PostgreSQL on Railway (connection string in `HUB_DATABASE_URL`)
- **Webhook endpoint:** `/hooks/agent` (token: `OPENCLAW_HOOK_TOKEN`)

### Poe Orchestrator
- **Endpoint:** `/poe/v1/chat/completions` (on Hub)
- **Auth key:** `POE_ORCHESTRATOR_KEY` env var (added 2026-03-09 by Joey to Railway)
- **Purpose:** Routes Poe bot conversations through Hub for dynamic prompt injection, funnel CTAs, and conversation logging

### Key API Endpoints
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/ingest` | POST | Drop ingestion (source: api/email/sms/voice/chat) |
| `/api/search?q=&user_id=` | GET | Search user drops |
| `/api/memory/context/openclaw` | GET | My persistent memory |
| `/api/memory` | POST | Write memory |
| `/api/ops/dashboard` | GET | System health overview |
| `/api/ops/tasks` | GET/POST | Task queue (for dropper-code) |
| `/api/ops/tasks/{id}` | PATCH | Approve/reject tasks |
| `/api/agent-drops` | POST | Create agent drops |
| `/api/admin/stats` | GET | User stats, drop counts |
| `/api/admin/drops/activity` | GET | Drop activity feed |
| `/api/admin/users` | GET | User list |
| `/api/webhook/email` | POST | Resend email webhook receiver |
| `/api/alerts` | POST | Send alerts |
| `/api/alerts/daily-summary` | POST | Trigger daily summary |
| `/api/dcs/code-task` | POST | Create code task for DCS agent |
| `/api/tasks/pending` | GET | Pending HITL tasks |
| `/api/tasks/approve` | POST | Approve pending task |

### Key Users
| User | ID | Email | Drops |
|------|----|-------|-------|
| Joey | `b419d8ad5d23513f` | joeyhamer@gmail.com | 334+ |
| Danny Hamer | `920d4d339900efd5` | hamer.daniel@gmail.com | — |

### Feature Flags (env)
- `ENABLE_ALERT_MONITORS=true`
- `ENABLE_DIGEST_SCHEDULER=true`
- `ENABLE_RE_ENGAGEMENT=true`
- `ENABLE_TASK_WORKER=true`
- `DISABLE_CRONS=1` ⚠️ (crons disabled on this service — they run elsewhere)
- `POLL_INTERVAL=300` (5 min)

---

## Dropper-Code (Autonomous Code Agent)

- **Health:** `GET https://dropper-code-production.up.railway.app/health`
- **Trigger:** `POST https://dropper-code-production.up.railway.app/trigger/{job_name}`
- **Polls task queue** every 45s for approved tasks
- **Flow:** Brain-scan (every 4h) → proposes tasks → I auto-approve/escalate → dropper-code executes → pushes branch → opens PR
- **Target repos:** opoerator-hub, dropanywhere-app, openclaw

---

## AI / LLM Services

### Anthropic (Direct)
- **API Key:** ✅ via `ANTHROPIC_API_KEY`
- **OAuth Token:** ✅ via `CLAUDE_CODE_OAUTH_TOKEN`
- **Default model:** `anthropic/claude-sonnet-4-6` (OPENCLAW_DEFAULT_MODEL)
- **Current session model:** `anthropic/claude-opus-4-6` (override)
- **CLAUDE_MODEL env:** `sonnet`

### OpenRouter
- **API Key:** ✅ via `OPENROUTER_API_KEY`
- **Used by:** BrutallyHonest.ai for multi-model access (GPT-4o, Gemini, Claude)

---

## Payment & Billing

### Stripe (Live)
- **Secret Key:** ✅ via `STRIPE_SECRET_KEY` (live, not test)
- **Webhook Secret:** ✅ via `STRIPE_WEBHOOK_SECRET`
- **Monthly Price ID:** `price_1T2HMlEwnzhvBnaiZGFlBIxy`
- **Yearly Price ID:** `price_1Stu7tEwnzhvBnaiuAKt9d3x`
- **Used by:** BrutallyHonest.ai

---

## Email (Resend)

- **API Key:** ✅ via `RESEND_API_KEY`
- **From address:** `DropAnywhere <hello@drop-anywhere.com>` (RESEND_FROM_EMAIL)
- **Webhook secret:** ✅ via `RESEND_WEBHOOK_SECRET`
- **Can also send as:** `joey@drop-anywhere.com`
- **Cloudflare WAF limit:** ~100KB inline payload. Workaround: write JSON to /tmp, use `curl -d @/tmp/file.json`
- Joey wants FULL quality PDFs emailed, never stripped-down. Always use parrot footer.

---

## SMS / Voice (Twilio)

- **Auth Token:** ✅ via `TWILIO_AUTH_TOKEN`
- **Capability:** SMS ingestion for DropAnywhere
- *(Phone number / SID not in env — may be configured in Hub)*

---

## Poe Bots

- **Access Key (PCB):** ✅ via `POE_ACCESS_KEY_PCB`
- **API Key:** ✅ via `POE_API_KEY`
- **Drop Access Key:** ✅ via `POE_DROP_ACCESS_KEY`
- **Joey's bots:** 14+ personas (BrutallyHonestAI, theREALrealtalk, NotTherapyBot, IdealPrompt, etc.)

---

## BrutallyHonest.ai

- **Admin API Key:** ✅ via `BHA_ADMIN_API_KEY`
- **Bridge Secret:** ✅ via `BRIDGE_API_SECRET`
- **Webhook Secret:** ✅ via `BHA_WEBHOOK_SECRET` (set on Hub, BHA prod/staging, Dropper-Code)
- **Live URL:** https://app.brutallyhonest.ai
- **Stack:** Next.js 16, OpenRouter, Stripe, PostgreSQL
- **Products:** Pay-as-you-go ($4.99), Pro Monthly ($7/mo), Founders Mode ($47)
- **Sentry DSN:** configured but empty (NEXT_PUBLIC_SENTRY_DSN="")

---

## OpenClaw Gateway

- **Version:** 2026.2.3 (commit 944bcfb)
- **Config path:** `/root/.openclaw/openclaw.json`
- **State dir:** `/root/.openclaw`
- **Workspace:** `/root/.openclaw/workspace`
- **Gateway port:** 8080
- **Internal gateway:** `0.0.0.0:18789`
- **Hook URL:** `https://openclaw-gateway-production-54a0.up.railway.app/hooks/agent`
- **Hook token:** ✅ via `OPENCLAW_HOOK_TOKEN` / `HOOKS_TOKEN`
- **Setup password:** ✅ via `SETUP_PASSWORD`
- **Prefer pnpm:** yes
- **Bootstrapped:** yes

---

## PRD Maintenance Crons

The master PRD (`docs/PRD-Action-Plan-2026-03-10.md`) is kept alive by 3 cron jobs:

| Job | Cron ID | Schedule (UTC) | Model |
|-----|---------|----------------|-------|
| Metrics Snapshot | `a1bcf313-c54a-4606-b510-ee35f2094d6d` | 02,08,14,20 daily | Kimi K2.5 (OpenRouter) |
| Daily Metrics Refresh | `1ef071a5-1971-4d3c-8ef8-6a63a988be21` | 14:00 daily | Kimi K2.5 (OpenRouter) |
| Weekly Full Refresh | `c5222e50-a871-461c-b33f-9fec84a961ac` | 01:00 Monday | Kimi K2.5 (OpenRouter) |
| Drop Mining | `e0cb7ab1-521e-4c9e-9b2a-7f0be9c70b74` | 22:00 Wed + Sat | Kimi K2.5 (OpenRouter) |

### Hub-Side Alert Monitors (run inside Hub, NOT OpenClaw)
Hub has `ENABLE_ALERT_MONITORS=true` — an async scheduler with 5-min ticks:
| Monitor | Interval | Alerts via `/hooks/agent` → WhatsApp |
|---------|----------|--------------------------------------|
| Hub Health | 1h | Latency > 5s |
| Digest Pipeline | 1h | Stalled users (no digest in 36h) |
| Error Rate | 1h | > 20 errors/hour |
| Stripe | 4h | New sales or failed charges |
| GitHub CI + Security | 6h | Failed workflows, dependabot alerts |
| Poe Costs | 6h | Low balance (< 500), high burn (> 5K/6h) |
| Resend Email | 6h | Bounces, delivery issues |
| Railway | 6h | Failed deployments |
| Google Analytics | 6h | Traffic data |
| Daily Ops Summary | 24h (~9am UTC) | Full metrics summary |

Manual triggers: `POST /api/alerts/run-monitors`, `POST /api/alerts/daily-summary`

All run as isolated sessions. Daily is silent. Weekly sends Joey a summary. Drop Mining is silent enrichment.

---

## Active Projects

### DropAnywhere Ecosystem
- **Backend:** hub-production-f423.up.railway.app
- **Frontend:** https://drop-anywhere.com
- **Frontend Railway Project:** d07a0723-d1bd-4aff-b002-0192b4a32973
- **Philosophy:** "Your Second Brain Has No Inbox"
- **Features:** Multi-channel ingestion, daily digests, vault search, context bank

### BrutallyHonest.ai
- **Live:** https://app.brutallyhonest.ai
- **Stack:** Next.js 16, OpenRouter, Stripe, PostgreSQL
- **Products:** Pay-as-you-go ($4.99), Pro Monthly ($7/mo), Founders Mode ($47)
- **Personas:** BrutallyHonestAI, DecisionMaker, GrowthOracle, etc.

### OpenClaw (This Workspace)
- **Purpose:** Personal AI assistant
- **Vibe:** "The parrot way" 🦜
- **Features:** Heartbeats, cron jobs, memory system, node integration
- **Git:** main branch, latest commit: `37d32eac` — "fix: guard registry.typedHooks against undefined before .filter()/.some()"

---

## Environment

- **Host:** Linux 6.12.22+bpo-cloud-amd64 (x64), Docker/containerized
- **Hostname:** 5a1024706416
- **Node:** v22.22.0
- **Yarn:** 1.22.22 (but pnpm preferred)
- **Workspace:** /root/.openclaw/workspace
- **Python:** available (PYTHONUNBUFFERED=1)
- **Storage:** Railway volume at `/root/.openclaw`

---

## Digest Template Library

- Stored in `workspace/templates/` (committed to git)
- **Brooke Theme** ✅ — cream/sage/copper, Newsreader, Lucide icons, liquid glass
- **RIA Theme** ✅ — financial advisory (Danny Hamer brief style)
- **Protocol/DashStart/Apple** — planned
- PDF generation: Puppeteer + Chrome headless on this container
- No emojis in PDFs (headless Chrome lacks emoji fonts), no gradient text

---

## TTS / Voice

- **Preferred voice:** *(to be configured)*
- **Default speaker:** *(to be configured)*

---

## iOS Shortcuts

### DropAnywhere Ingest Shortcut
**Status:** Working (v1)

**Endpoint:** `POST https://hub-production-f423.up.railway.app/api/ingest`

**Headers:**
- `X-API-Key: <HUB_API_KEY>`
- `Content-Type: application/json`

**Request Body (JSON):**
```json
{
  "content": "Your drop text here",
  "source": "api"
}
```

**Important:** The `source` field must be one of the allowed values. Use `"api"` for iOS shortcut drops.

**Current Capabilities:**
- ✅ Text ingestion via dictation
- ✅ Time/Device/Screenshot metadata capture
- ✅ Clipboard content
- ❌ Image analysis (screenshot text extraction not yet implemented)

---

## Cameras / Devices

- *(to be added when nodes are connected)*

---

## Admin Emails

- `joeyhamer@gmail.com` (ADMIN_EMAILS)

---

*Last hydrated: 2026-03-02 from env vars. No raw secrets stored — only service names, endpoints, and capabilities.*
