#!/bin/bash
# Atomic append to daily log — prevents race conditions from multiple agents
# Usage: echo "### HH:MM UTC — AgentName\n- finding" | bash append-to-daily-log.sh

LOGDIR="/root/.openclaw/workspace/memory"
TODAY=$(date -u +%Y-%m-%d)
LOGFILE="$LOGDIR/$TODAY.md"
LOCKFILE="/tmp/daily-log-$TODAY.lock"

# Create log file with header if missing
if [ ! -f "$LOGFILE" ]; then
  echo "# Daily Log — $TODAY" > "$LOGFILE"
  echo "" >> "$LOGFILE"
fi

# Read from stdin
CONTENT=$(cat)

if [ -z "$CONTENT" ]; then
  exit 0
fi

# Use flock for atomic append
(
  flock -w 10 200 || exit 1
  echo "" >> "$LOGFILE"
  echo "$CONTENT" >> "$LOGFILE"
) 200>"$LOCKFILE"
