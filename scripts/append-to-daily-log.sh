#!/bin/bash
# Append text to daily log with timestamp

DATE=$(date -u +%Y-%m-%d)
LOG_FILE="/root/.openclaw/workspace/memory/$DATE.md"

# Ensure the directory exists
mkdir -p "/root/.openclaw/workspace/memory"

# Read from stdin and append to log
cat >> "$LOG_FILE"