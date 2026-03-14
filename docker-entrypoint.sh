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

# Ensure config exists and has required Railway settings
node -e "
  const fs = require('fs');
  const path = process.argv[1];
  let cfg = {};
  try { cfg = JSON.parse(fs.readFileSync(path, 'utf8')); } catch {}
  if (!cfg.gateway) cfg.gateway = {};
  if (!cfg.gateway.controlUi) cfg.gateway.controlUi = {};
  cfg.gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback = true;
  cfg.gateway.controlUi.dangerouslyDisableDeviceAuth = true;

  // Remove stale keys that cause validation errors
  if (cfg.commands) delete cfg.commands.ownerDisplay;
  if (cfg.channels && cfg.channels.whatsapp) delete cfg.channels.whatsapp.enabled;

  fs.mkdirSync(require('path').dirname(path), { recursive: true });
  fs.writeFileSync(path, JSON.stringify(cfg, null, 2));
  console.log('Config ready at ' + path);
" "$CONFIG" || echo "Warning: config setup failed"

exec "$@"
