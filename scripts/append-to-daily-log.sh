#!/bin/bash
# Append content to today's daily log file
TODAY=$(date -u +%Y-%m-%d)
LOG_FILE="/root/.openclaw/workspace/memory/${TODAY}.md"

# Create the file if it doesn't exist
if [ ! -f "$LOG_FILE" ]; then
    echo "# Daily Log - $TODAY" > "$LOG_FILE"
    echo "" >> "$LOG_FILE"
fi

# Append the input (from stdin or arguments) to the log file
if [ $# -eq 0 ]; then
    # Read from stdin
    cat >> "$LOG_FILE"
else
    # Use arguments
    echo "$*" >> "$LOG_FILE"
fi

echo "" >> "$LOG_FILE"