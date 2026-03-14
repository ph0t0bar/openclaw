#!/bin/sh
set -e

CONFIG="/root/.openclaw/openclaw.json"

# Wait for Railway volume mount (mounts after container start)
echo "Waiting for volume at /root/.openclaw..."
for i in 1 2 3 4 5 6 7 8 9 10; do
  if [ -d "/root/.openclaw" ]; then
    echo "Volume mounted."
    break
  fi
  sleep 1
done

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
  echo "No config found, creating at $CONFIG..."
  mkdir -p /root/.openclaw
  echo '{"gateway":{"controlUi":{"dangerouslyAllowHostHeaderOriginFallback":true}}}' > "$CONFIG"
  echo "Created config with controlUi fallback enabled"
fi

exec "$@"
