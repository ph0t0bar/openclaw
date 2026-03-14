#!/bin/sh
set -e

# Railway volume mounts config at /root/.openclaw but container runs as USER node
CONFIG="/root/.openclaw/openclaw.json"

if [ -f "$CONFIG" ]; then
  echo "Found config at: $CONFIG"

  # Auto-fix stale config keys
  node /app/openclaw.mjs doctor --fix || echo "Warning: doctor --fix failed"

  # Patch controlUi for non-loopback Railway deploy
  node -e "
    const fs = require('fs');
    const cfg = JSON.parse(fs.readFileSync(process.argv[1], 'utf8'));
    if (!cfg.gateway) cfg.gateway = {};
    if (!cfg.gateway.controlUi) cfg.gateway.controlUi = {};
    cfg.gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback = true;
    fs.writeFileSync(process.argv[1], JSON.stringify(cfg, null, 2));
    console.log('Patched controlUi.dangerouslyAllowHostHeaderOriginFallback = true');
  " "$CONFIG" || echo "Warning: config patch failed"
else
  echo "No config at $CONFIG, creating..."
  mkdir -p /root/.openclaw
  echo '{"gateway":{"controlUi":{"dangerouslyAllowHostHeaderOriginFallback":true}}}' > "$CONFIG"
  echo "Created config with controlUi fallback enabled"
fi

# Point openclaw to the volume-mounted config
export OPENCLAW_CONFIG_PATH="$CONFIG"

exec "$@"
