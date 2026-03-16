#!/bin/bash
# Send a Brooke-themed, threaded email via Resend
# Usage: send-threaded-email.sh <thread> <subject> <html_file>
# Threads: morning-brief, creative-review, ops-tasks, claw-convo, weekly-report

THREAD="${1:-claw-convo}"
SUBJECT="${2:-💬 Claw}"
HTML_FILE="${3:-/tmp/email-body.html}"

THREAD_ID="<${THREAD}@drop-anywhere.com>"

python3 << PYEOF
import json

with open("${HTML_FILE}") as f:
    html = f.read()

payload = {
    "from": "DropAnywhere <hello@drop-anywhere.com>",
    "to": "joeyhamer@gmail.com",
    "subject": """${SUBJECT}""",
    "headers": {
        "In-Reply-To": "${THREAD_ID}",
        "References": "${THREAD_ID}"
    },
    "html": html
}

with open("/tmp/threaded-email.json", "w") as f:
    json.dump(payload, f)
PYEOF

curl -s -X POST 'https://api.resend.com/emails' \
  -H "Authorization: Bearer $RESEND_API_KEY" \
  -H 'Content-Type: application/json' \
  -d @/tmp/threaded-email.json | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('id','FAILED'))"
