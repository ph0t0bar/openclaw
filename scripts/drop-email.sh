#!/bin/bash
# Send a Drop conversational email to Joey
# Usage: bash scripts/claw-email.sh "Subject" "Body text"

SUBJECT="${1:-💬 Drop}"
BODY="${2:-Message from Drop}"

# Create JSON payload
python3 << PYEOF
import json
import os

html = f"""<html><body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; max-width: 700px; margin: 0 auto; color: #333; line-height: 1.6; background: #FDFBF7; padding: 40px 20px;">
<div style="border-left: 4px solid #C17F59; padding-left: 20px; margin-bottom: 30px;">
<h2 style="color: #C17F59; margin: 0;">{os.environ.get('SUBJECT', '💬 Drop')}</h2>
</div>
<div style="background: white; padding: 30px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
<p>{os.environ.get('BODY', '').replace(chr(10), '<br>')}</p>
</div>
<p style="color: #999; font-size: 12px; margin-top: 30px; text-align: center;">
Reply to this email to continue the conversation<br>
🦜 Drop — DropAnywhere
</p>
</body></html>"""

payload = {
    "from": "DropAnywhere <hello@drop-anywhere.com>",
    "to": "joeyhamer@gmail.com",
    "subject": os.environ.get('SUBJECT'),
    "html": html
}

with open('/tmp/claw-message.json', 'w') as f:
    json.dump(payload, f)
PYEOF

# Send via Resend
curl -s -X POST 'https://api.resend.com/emails' \
  -H "Authorization: Bearer $RESEND_API_KEY" \
  -H 'Content-Type: application/json' \
  -d @/tmp/claw-message.json | python3 -c "import json,sys;d=json.load(sys.stdin);print('Sent:', d.get('id'))"
