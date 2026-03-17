#!/bin/bash
# Append to daily log script
LOG_FILE="/root/.openclaw/workspace/memory/$(date -u +%Y-%m-%d).md"
mkdir -p "$(dirname "$LOG_FILE")"
echo "" >> "$LOG_FILE"
echo "$1" >> "$LOG_FILE"
