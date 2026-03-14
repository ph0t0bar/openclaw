#!/bin/sh
set -e

# Auto-fix stale config keys on boot (safe no-op if config is already clean)
if [ -f "$HOME/.openclaw/openclaw.json" ]; then
  echo "Running openclaw doctor --fix to repair config..."
  node /app/openclaw.mjs doctor --fix || echo "Warning: doctor --fix failed, continuing anyway"
fi

exec "$@"
