#!/bin/sh
set -e

# Railway volume mounts at /root/.openclaw — ensure workspace subdir exists.
mkdir -p /root/.openclaw/workspace

# Seed default config on first boot (volume is empty).
if [ ! -f /root/.openclaw/openclaw.json ] && [ -f /app/.openclaw/openclaw.json ]; then
  cp /app/.openclaw/openclaw.json /root/.openclaw/openclaw.json
fi

# Seed workspace templates if missing.
if [ -d /app/docs/reference/templates ]; then
  for tpl in /app/docs/reference/templates/*.md; do
    dest="/root/.openclaw/workspace/$(basename "$tpl")"
    [ -f "$dest" ] || cp "$tpl" "$dest"
  done
fi

exec "$@"
