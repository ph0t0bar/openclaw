#!/bin/bash
# Simple script to append content to daily log
# Usage: echo "content" | bash append-to-daily-log.sh

DAILY_LOG="/root/.openclaw/workspace/memory/$(date -u +%Y-%m-%d).md"

# Read from stdin and append to daily log
while IFS= read -r line; do
    echo "$line" >> "$DAILY_LOG"
done