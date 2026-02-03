#!/bin/sh
set -e

# Railway volumes mount as root at runtime, overriding build-time dirs.
# Create the required directories and fix ownership before dropping to node.
mkdir -p /data/.openclaw /data/workspace

# Seed default config on first boot (volume is empty).
if [ ! -f /data/.openclaw/openclaw.json ] && [ -f /app/.openclaw/openclaw.json ]; then
  cp /app/.openclaw/openclaw.json /data/.openclaw/openclaw.json
fi

chown -R node:node /data

exec gosu node "$@"
