# Email Standards — ALL AGENTS MUST FOLLOW

## Single Sender Identity

**ALL emails use:**
- From: `DropAnywhere <hello@drop-anywhere.com>`
- Reply-To: `hello@drop-anywhere.com`

**NEVER use:** noreply@, joey@, OpenClaw, or any other from address.

---

## Deliverability Requirements (MANDATORY in every email)

### 1. List-Unsubscribe Header
Every email MUST include in the Resend payload:
```json
"headers": {
  "List-Unsubscribe": "<mailto:unsubscribe@drop-anywhere.com>",
  "List-Unsubscribe-Post": "List-Unsubscribe=One-Click"
}
```

### 2. Physical Address (CAN-SPAM)
Every email footer MUST include:
```
DropAnywhere · Chicago, IL · USA
```

### 3. Unsubscribe Link in Footer
Every email footer MUST include:
```html
<a href="mailto:unsubscribe@drop-anywhere.com?subject=unsubscribe" style="color:#999;">Unsubscribe</a>
```

### 4. Preheader Text
Every email SHOULD include a preheader (the preview text in Gmail):
```html
<div style="display:none;max-height:0;overflow:hidden;">Preview text here</div>
```

---

## Threading Headers (MANDATORY)

Every email MUST include thread headers per EMAIL-THREADING.md:
```json
"headers": {
  "In-Reply-To": "<thread-id@drop-anywhere.com>",
  "References": "<thread-id@drop-anywhere.com>",
  "List-Unsubscribe": "<mailto:unsubscribe@drop-anywhere.com>",
  "List-Unsubscribe-Post": "List-Unsubscribe=One-Click"
}
```

Thread IDs: morning-brief, creative-review, ops-tasks, claw-convo, weekly-report

---

## Subject Line Prefixes (mandatory)

| Stream | Prefix | Thread ID |
|--------|--------|-----------|
| Morning Brief | ☀️ | morning-brief |
| Creative Review | 🦜 | creative-review |
| Ops & Tasks | ⚙️ | ops-tasks |
| Alerts | 🚨 | ops-tasks |
| Weekly Report | 📊 | weekly-report |
| Claw Conversation | 💬 | claw-convo |
| Documents/PDFs | 📄 | claw-convo |

---

## Brooke Theme HTML Template

EVERY email body MUST follow this structure:

```html
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
</head>
<body style="margin:0; padding:0; background:#FDFBF7; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;">

<!-- Preheader (hidden preview text) -->
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;">
  PREHEADER TEXT HERE
</div>

<!-- Container -->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#FDFBF7;">
<tr><td align="center" style="padding:40px 20px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0">

  <!-- Header -->
  <tr><td style="padding:0 0 20px 0; border-bottom:3px solid #C17F59;">
    <h1 style="margin:0; color:#C17F59; font-size:24px; font-weight:600;">
      SUBJECT/TITLE HERE
    </h1>
    <p style="margin:5px 0 0 0; color:#888; font-size:14px;">SUBTITLE/DATE</p>
  </td></tr>

  <!-- Body -->
  <tr><td style="padding:25px 0;">
    <!-- Content sections go here -->
    <!-- Use these styles: -->
    <!-- Section card: background:white; padding:20px; border-radius:12px; box-shadow:0 2px 8px rgba(0,0,0,0.05); margin-bottom:16px; -->
    <!-- Heading: color:#5B7B6A; font-size:16px; font-weight:600; -->
    <!-- Body text: color:#333; font-size:15px; line-height:1.6; -->
    <!-- Accent text: color:#C17F59; -->
    <!-- Alert/urgent: background:#FFF3F3; border-left:4px solid #E53E3E; -->
    <!-- Success: background:#F0FFF4; border-left:4px solid #5B7B6A; -->
  </td></tr>

  <!-- Footer (MANDATORY — deliverability) -->
  <tr><td style="padding:25px 0 0 0; border-top:1px solid #E8E0D8; text-align:center;">
    <p style="margin:0; color:#999; font-size:12px; line-height:1.8;">
      Reply to this email — Claw reads every reply. 🦜<br>
      <a href="mailto:hello@drop-anywhere.com" style="color:#C17F59; text-decoration:none;">hello@drop-anywhere.com</a><br><br>
      DropAnywhere · Chicago, IL · USA<br>
      <a href="mailto:unsubscribe@drop-anywhere.com?subject=unsubscribe" style="color:#999; text-decoration:underline;">Unsubscribe</a> · 
      <a href="https://drop-anywhere.com/privacy" style="color:#999; text-decoration:underline;">Privacy</a>
    </p>
  </td></tr>

</table>
</td></tr>
</table>
</body>
</html>
```

---

## Color Reference

| Name | Hex | Use |
|------|-----|-----|
| Cream | #FDFBF7 | Background |
| Copper | #C17F59 | Primary accent, headers, links |
| Sage | #5B7B6A | Section headers, success states |
| Dark text | #333333 | Body copy |
| Light text | #888888 | Subtitles, metadata |
| Muted | #999999 | Footer, timestamps |
| Card bg | #FFFFFF | Content cards |
| Border | #E8E0D8 | Dividers |
| Alert red | #E53E3E | Urgent items |
| Alert bg | #FFF3F3 | Urgent background |
| Success bg | #F0FFF4 | Success background |

---

## Anti-Spam Checklist

Before sending ANY email, verify:
- [ ] From: `DropAnywhere <hello@drop-anywhere.com>`
- [ ] List-Unsubscribe header present
- [ ] Physical address in footer
- [ ] Unsubscribe link in footer
- [ ] Text-to-image ratio > 80% text (no image-heavy emails)
- [ ] No ALL CAPS subjects
- [ ] No excessive punctuation (!!!)
- [ ] Preheader text set (not empty)
- [ ] Threading headers (In-Reply-To + References)
- [ ] HTML uses table-based layout (not divs — better email client compat)
- [ ] Content is relevant (no empty/no-action emails)

---

## Resend Payload Template

Complete copy-paste template for agents:

```python
import json

payload = {
    "from": "DropAnywhere <hello@drop-anywhere.com>",
    "to": "joeyhamer@gmail.com",
    "subject": "PREFIX Subject Here",
    "headers": {
        "In-Reply-To": "<THREAD-ID@drop-anywhere.com>",
        "References": "<THREAD-ID@drop-anywhere.com>",
        "List-Unsubscribe": "<mailto:unsubscribe@drop-anywhere.com>",
        "List-Unsubscribe-Post": "List-Unsubscribe=One-Click"
    },
    "html": html_content
}

with open("/tmp/email.json", "w") as f:
    json.dump(payload, f)
```

Then: `curl -s -X POST 'https://api.resend.com/emails' -H "Authorization: Bearer $RESEND_API_KEY" -H 'Content-Type: application/json' -d @/tmp/email.json`
