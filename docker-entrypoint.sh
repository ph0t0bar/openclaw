#!/bin/sh
set -e

# Railway volume mounts at /root/.openclaw — ensure workspace subdir exists.
mkdir -p /root/.openclaw/workspace

# Always copy bundled config (overwrite volume's stale config on each deploy).
# Config contains env var placeholders (${POE_API_KEY}, ${HOOKS_TOKEN}) that OpenClaw resolves at runtime.
if [ -f /app/.openclaw/openclaw.json ]; then
  cp /app/.openclaw/openclaw.json /root/.openclaw/openclaw.json
fi

# Apply deployment overrides from environment variables.
# This ensures the git-tracked config can stay in sync with upstream
# while Railway env vars control deployment-specific settings.
node -e "
const fs = require('fs');
const configPath = '/root/.openclaw/openclaw.json';
if (!fs.existsSync(configPath)) process.exit(0);

const cfg = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
const env = process.env;
let changed = false;

// Override primary model (e.g. OPENCLAW_PRIMARY_MODEL=poe/claude-haiku-4.5)
if (env.OPENCLAW_PRIMARY_MODEL) {
  cfg.agents = cfg.agents || {};
  cfg.agents.defaults = cfg.agents.defaults || {};
  cfg.agents.defaults.model = cfg.agents.defaults.model || {};
  cfg.agents.defaults.model.primary = env.OPENCLAW_PRIMARY_MODEL;
  changed = true;
}

// Override workspace path (e.g. OPENCLAW_WORKSPACE=/root/.openclaw/workspace)
if (env.OPENCLAW_WORKSPACE) {
  cfg.agents = cfg.agents || {};
  cfg.agents.defaults = cfg.agents.defaults || {};
  cfg.agents.defaults.workspace = env.OPENCLAW_WORKSPACE;
  changed = true;
}

// Force API key and hooks token to use env var placeholders (never hardcoded).
// OpenClaw's config loader resolves \${VAR} from process.env at runtime.
if (cfg.models && cfg.models.providers && cfg.models.providers.poe) {
  if (cfg.models.providers.poe.apiKey !== '\${POE_API_KEY}') {
    cfg.models.providers.poe.apiKey = '\${POE_API_KEY}';
    changed = true;
  }
}
if (cfg.hooks && cfg.hooks.token !== '\${HOOKS_TOKEN}') {
  cfg.hooks.token = '\${HOOKS_TOKEN}';
  changed = true;
}

// Apply full JSON overlay if provided (escape hatch for any other settings)
if (env.OPENCLAW_CONFIG_OVERLAY) {
  try {
    const overlay = JSON.parse(env.OPENCLAW_CONFIG_OVERLAY);
    function merge(target, source) {
      for (const key of Object.keys(source)) {
        if (source[key] && typeof source[key] === 'object' && !Array.isArray(source[key])
            && target[key] && typeof target[key] === 'object' && !Array.isArray(target[key])) {
          merge(target[key], source[key]);
        } else {
          target[key] = source[key];
        }
      }
    }
    merge(cfg, overlay);
    changed = true;
  } catch (e) {
    console.error('OPENCLAW_CONFIG_OVERLAY parse error:', e.message);
  }
}

if (changed) {
  fs.writeFileSync(configPath, JSON.stringify(cfg, null, 2) + '\n');
  console.log('[entrypoint] Applied deployment config overrides');
}
"

# Copy cron jobs — prefer deploy-specific file over git-tracked version.
# OPENCLAW_CRON_JOBS env var takes highest priority (JSON string).
if [ -n "$OPENCLAW_CRON_JOBS" ]; then
  mkdir -p /root/.openclaw/cron
  printf '%s\n' "$OPENCLAW_CRON_JOBS" > /root/.openclaw/cron/jobs.json
  echo "[entrypoint] Wrote cron jobs from OPENCLAW_CRON_JOBS env var"
elif [ -f /app/.openclaw/cron/jobs.json ]; then
  mkdir -p /root/.openclaw/cron
  cp /app/.openclaw/cron/jobs.json /root/.openclaw/cron/jobs.json
fi

# Seed workspace templates if missing.
if [ -d /app/docs/reference/templates ]; then
  for tpl in /app/docs/reference/templates/*.md; do
    dest="/root/.openclaw/workspace/$(basename "$tpl")"
    [ -f "$dest" ] || cp "$tpl" "$dest"
  done
fi

# Sync agent drops (Claude Code → OpenClaw).
# Fresh drops overwrite on each deploy; OpenClaw's outbound drops persist on volume.
mkdir -p /root/.openclaw/workspace/drops/from-claude-code \
         /root/.openclaw/workspace/drops/from-openclaw
if [ -d /app/drops/from-claude-code ]; then
  cp /app/drops/from-claude-code/*.md /root/.openclaw/workspace/drops/from-claude-code/ 2>/dev/null || true
fi

exec "$@"
