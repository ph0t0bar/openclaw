#!/bin/sh
set -e

# Railway volumes mount as root at runtime, overriding build-time dirs.
# Create the required directories and fix ownership before dropping to node.
mkdir -p /data/.openclaw /data/workspace
chown -R node:node /data

exec gosu node "$@"
