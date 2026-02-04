#!/bin/sh
set -e

# Railway volume mounts at /root/.openclaw — ensure workspace subdir exists.
mkdir -p /root/.openclaw/workspace

# Always copy bundled config (overwrite volume's stale config on each deploy).
# Config contains env var placeholders (${POE_API_KEY}, ${HOOKS_TOKEN}) that Railway resolves.
if [ -f /app/.openclaw/openclaw.json ]; then
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
