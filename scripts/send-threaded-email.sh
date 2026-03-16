#!/bin/bash
# Send a Brooke-themed, threaded, deliverability-compliant email via Resend
# Usage: send-threaded-email.sh <thread> <subject> <body_html_file> [preheader]
# Threads: morning-brief, creative-review, ops-tasks, drop-convo, weekly-report

THREAD="${1:-drop-convo}"
SUBJECT="${2:-💬 Drop}"
BODY_FILE="${3:-/tmp/email-body.html}"
PREHEADER="${4:-}"

THREAD_ID="<${THREAD}@drop-anywhere.com>"

python3 << PYEOF
import json

with open("${BODY_FILE}") as f:
    body = f.read()

preheader = """${PREHEADER}"""

html = f"""<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
</head>
<body style="margin:0; padding:0; background:#FDFBF7; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;">

<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;">{preheader}</div>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#FDFBF7;">
<tr><td align="center" style="padding:40px 20px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0">

{body}

<tr><td style="padding:25px 0 0 0; border-top:1px solid #E8E0D8; text-align:center;">
<p style="margin:0; color:#999; font-size:12px; line-height:1.8;">
Reply to this email &mdash; Drop reads every reply. &#x1F99C;<br>
<a href="mailto:hello@drop-anywhere.com" style="color:#C17F59; text-decoration:none;">hello@drop-anywhere.com</a><br><br>
DropAnywhere &middot; Chicago, IL &middot; USA<br>
<a href="mailto:unsubscribe@drop-anywhere.com?subject=unsubscribe" style="color:#999; text-decoration:underline;">Unsubscribe</a> &middot;
<a href="https://drop-anywhere.com/privacy" style="color:#999; text-decoration:underline;">Privacy</a>
</p>
</td></tr>

</table>
</td></tr>
</table>
</body>
</html>"""

payload = {
    "from": "DropAnywhere <hello@drop-anywhere.com>",
    "to": "joeyhamer@gmail.com",
    "subject": """${SUBJECT}""",
    "headers": {
        "In-Reply-To": "${THREAD_ID}",
        "References": "${THREAD_ID}",
        "List-Unsubscribe": "<mailto:unsubscribe@drop-anywhere.com>",
        "List-Unsubscribe-Post": "List-Unsubscribe=One-Click"
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
