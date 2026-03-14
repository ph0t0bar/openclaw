#!/bin/sh
set -e

# Find the openclaw config wherever it lives (volume, home dir, etc.)
CONFIG=""
for candidate in \
  "$HOME/.openclaw/openclaw.json" \
  "$OPENCLAW_STATE_DIR/openclaw.json" \
  "$OPENCLAW_CONFIG_PATH" \
  ; do
  if [ -n "$candidate" ] && [ -f "$candidate" ]; then
    CONFIG="$candidate"
    break
  fi
done

# Also check common Railway volume mount points
if [ -z "$CONFIG" ]; then
  CONFIG=$(find /var/lib/containers /data /mnt 2>/dev/null -name "openclaw.json" -type f | head -1)
fi

if [ -n "$CONFIG" ]; then
  echo "Found config at: $CONFIG"

  # Auto-fix stale config keys
  echo "Running openclaw doctor --fix..."
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
  echo "No openclaw.json found, creating default config..."
  mkdir -p "$HOME/.openclaw"
  echo '{"gateway":{"controlUi":{"dangerouslyAllowHostHeaderOriginFallback":true}}}' > "$HOME/.openclaw/openclaw.json"
  echo "Created config with controlUi fallback enabled"
fi

exec "$@"
