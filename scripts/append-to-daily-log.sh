#!/bin/bash
# Append to daily log script
DAILY_LOG="/root/.openclaw/workspace/memory/$(date -u +%Y-%m-%d).md"
mkdir -p "$(dirname "$DAILY_LOG")"
echo "" >> "$DAILY_LOG"
echo "$1" >> "$DAILY_LOG"