#!/bin/sh
set -e

CONFIG="$HOME/.openclaw/openclaw.json"

# Auto-fix stale config keys on boot
if [ -f "$CONFIG" ]; then
  echo "Running openclaw doctor --fix to repair config..."
  node /app/openclaw.mjs doctor --fix || echo "Warning: doctor --fix failed, continuing anyway"
fi

# Ensure controlUi allows host-header origin fallback for Railway (non-loopback)
if [ -f "$CONFIG" ]; then
  node -e "
    const fs = require('fs');
    const cfg = JSON.parse(fs.readFileSync('$CONFIG', 'utf8'));
    if (!cfg.gateway) cfg.gateway = {};
    if (!cfg.gateway.controlUi) cfg.gateway.controlUi = {};
    cfg.gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback = true;
    fs.writeFileSync('$CONFIG', JSON.stringify(cfg, null, 2));
    console.log('Patched controlUi.dangerouslyAllowHostHeaderOriginFallback = true');
  " || echo "Warning: config patch failed, continuing anyway"
fi

exec "$@"
