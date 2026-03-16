# Email Threading System

## How It Works
Resend supports `headers` with `In-Reply-To` and `References` to chain emails into Gmail threads.
Each stream gets a persistent thread ID based on a stable Message-ID.

## Thread IDs (stable, never change)

| Stream | Thread Message-ID | Subject Prefix |
|--------|-------------------|----------------|
| Morning Brief | `<morning-brief@drop-anywhere.com>` | ☀️ Morning Brief |
| Creative Review | `<creative-review@drop-anywhere.com>` | 🦜 Creative Review |
| Ops & Tasks | `<ops-tasks@drop-anywhere.com>` | ⚙️ Ops |
| Drop Conversation | `<drop-convo@drop-anywhere.com>` | 💬 Drop |
| Weekly Report | `<weekly-report@drop-anywhere.com>` | 📊 Week in Review |

## Implementation
Every email-sending agent MUST include headers in Resend payload:

```json
{
  "from": "DropAnywhere <hello@drop-anywhere.com>",
  "to": "joeyhamer@gmail.com",
  "subject": "☀️ Morning Brief — Mar 17",
  "headers": {
    "In-Reply-To": "<morning-brief@drop-anywhere.com>",
    "References": "<morning-brief@drop-anywhere.com>"
  },
  "html": "..."
}
```

## Rules
- SAME subject prefix per thread (Gmail uses subject for grouping too)
- First email in a thread sets the Message-ID; all subsequent use In-Reply-To
- Never mix streams in one thread
- Joey's replies automatically chain because Gmail threads by References header
