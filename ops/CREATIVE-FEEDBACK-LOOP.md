# Creative Feedback Loop

## How It Works

1. **Creative Review Email** (every 4h) scans `social/`, `docs/specs/`, and `ops/` for new/modified files
2. Emails Joey a formatted digest with all new content
3. Joey replies inline — "this one's good", "cut paragraph 2", "too corporate", etc.
4. Reply hits Resend webhook → Hub drop (source: email, tagged as feedback)
5. **FeedbackBot** (every 1h) checks Hub for feedback drops, routes them to:
   - `ops/feedback/YYYY-MM-DD.md` (raw log)
   - Updates the relevant file's companion `review-*.md` with Joey's notes
   - Posts to agent-board so ContentBot/FounderVoiceBot see the feedback

## Reply Address
- From: `DropAnywhere <hello@drop-anywhere.com>`
- Joey replies to this address → webhook catches it

## Rules
- Only email NEW or MODIFIED content (not stuff already reviewed)
- Track what's been sent in `ops/creative-review-state.json`
- Keep emails scannable — 30 seconds to skim
- Include "Approve ✅ / Needs Work 🔄 / Kill ❌" prompts per item
