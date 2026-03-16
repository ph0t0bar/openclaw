#!/bin/bash
# Append to daily decision log
LOG_FILE="/root/.openclaw/workspace/ops/decisions.log"
DATE=$(date -u +%Y-%m-%d)

# Create file with header if it doesn't exist
if [ ! -f "$LOG_FILE" ]; then
    echo "# DecisionBot Log — Started $DATE" > "$LOG_FILE"
    echo "" >> "$LOG_FILE"
fi

# Append the content passed via stdin or arguments
cat >> "$LOG_FILE"
echo "" >> "$LOG_FILE"
