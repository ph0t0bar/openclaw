#!/bin/bash
# Append to daily log file
LOG_FILE="/root/.openclaw/workspace/memory/$(date -u +%Y-%m-%d).md"
mkdir -p "$(dirname "$LOG_FILE")"
cat >> "$LOG_FILE"
