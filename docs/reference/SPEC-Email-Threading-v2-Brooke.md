# SPEC-Email-Threading-v2-Brooke — Kill Bare ACKs, Enable Threaded Replies

**Status:** DRAFT  
**Priority:** P0 (from agent-board Drop #7)  
**Created:** 2026-03-17  
**Owner:** Product/Email System  

---

## Problem Statement

Current "Drop received" ACK emails are friction-heavy:
- Bare confirmation emails create inbox noise
- No context about what was captured
- Missed opportunity for immediate value-add (threaded reply with insights)
- Violates the "Your Second Brain Has No Inbox" philosophy

**Decision logged:** Kill bare ACK emails entirely. Replace with optional, value-add threaded replies.

---

## Goals

| Goal | Metric |
|------|--------|
| Eliminate inbox noise from bare ACKs | 0 bare "Drop received" emails |
| Increase perceived value per drop | Threaded reply open rate > 40% |
| Maintain capture confirmation | Alternative confirmation path (in-app, digest) |
| Brooke-themed voice consistency | All threaded replies use Brooke persona |

---

## Non-Goals

- Real-time processing (digest pipeline timing is acceptable)
- SMS ACKs (SMS channel stays silent, as designed)
- Voice ACKs (voice channel stays silent)

---

## User Flow

### Current State (TO BE KILLED)
```
User sends drop → Immediate email: "Drop received. We'll process this in your next digest."
```

### Future State
```
User sends drop → Silent confirmation (in-app badge, next digest) 
                 → IF drop contains questions/urgent markers:
                   → Threaded reply within 15 min with Brooke voice + initial insights
                 → ELSE:
                   → No immediate email (wait for digest)
```

---

## Brooke Voice Guidelines for Threaded Replies

From the Brooke Theme:
- **Palette:** Warm cream, sage, caramel
- **Typography:** Newsreader (elegant, editorial)
- **Tone:** Thoughtful, warm, slightly witty, never corporate
- **Structure:** 
  1. Acknowledge the specific content (not generic)
  2. Add one insight, connection, or question
  3. Sign off with personality

### Example Threaded Reply

**Subject:** Re: Your drop about the Rancho Mirage patio design

> Hey Joey,
> 
> Got it — the travertine vs. limestone debate with the heated pool factor. Smart to think about thermal mass before the summer hits.
> 
> This connects to something you mentioned back in January about wanting the space to feel "lived-in but intentional." The lighter stone might actually serve that better — shows the patina of use without looking neglected.
> 
> I'll surface this in your digest tomorrow with those material samples you linked. No need to hold it in your head.
> 
> — Brooke

---

## Technical Implementation

### Database Changes

```sql
-- Add threaded reply tracking
ALTER TABLE drops ADD COLUMN threaded_reply_sent BOOLEAN DEFAULT FALSE;
ALTER TABLE drops ADD COLUMN threaded_reply_content TEXT;
ALTER TABLE drops ADD COLUMN threaded_reply_sent_at TIMESTAMP;

-- Add user preference for threaded replies
ALTER TABLE users ADD COLUMN enable_threaded_replies BOOLEAN DEFAULT TRUE;
```

### Email Service Changes

**File:** `hub/email_service.py` (or equivalent)

**Current logic to disable:**
```python
# REMOVE this block
if drop.source in ['email', 'sms', 'voice']:
    send_ack_email(user.email, drop.id)
```

**New logic to add:**
```python
def should_send_threaded_reply(drop: Drop) -> bool:
    """Determine if drop warrants immediate threaded reply."""
    if not user.enable_threaded_replies:
        return False
    
    # Check for urgency markers
    urgency_keywords = ['urgent', 'asap', 'deadline', 'tomorrow', 'today', '?']
    content_lower = drop.content.lower()
    
    has_urgency = any(kw in content_lower for kw in urgency_keywords)
    has_question = '?' in drop.content
    
    return has_urgency or has_question

def generate_threaded_reply(drop: Drop) -> str:
    """Generate Brooke-voiced threaded reply."""
    # Call LLM with Brooke system prompt
    # Return formatted email body
    pass
```

### Brooke System Prompt

```
You are Brooke, a warm, thoughtful AI assistant with editorial taste. 
You write email replies that feel personal and insightful, never robotic.

Guidelines:
- Reference specific details from the user's drop
- Make one unexpected connection to their past drops (if relevant)
- Keep it under 150 words
- Sign off as "— Brooke" (em-dash, not hyphen)
- Never use "I hope this email finds you well" or other corporate filler
- Never use emojis (Brooke doesn't need them)

The user just dropped this content: {drop_content}
Generate a threaded reply that adds immediate value.
```

---

## Compliance Requirements

From agent-board Drop #5: All emails must include:
- [ ] Unsubscribe link
- [ ] Privacy policy link
- [ ] Physical address (if required by CAN-SPAM)

**Footer template for threaded replies:**
```
---
You're receiving this because you sent a drop to DropAnywhere.
Threaded replies can be disabled in your settings: <link>
Privacy Policy: <link> | Unsubscribe: <link>
DropAnywhere, LLC | Chicago, IL
```

---

## Rollout Plan

| Phase | Date | Action |
|-------|------|--------|
| 1 | Day 1 | Disable bare ACK emails (immediate) |
| 2 | Day 2-3 | Implement threaded reply logic |
| 3 | Day 4-5 | Brooke voice tuning with Joey feedback |
| 4 | Day 6 | Beta test with Joey's drops only |
| 5 | Day 7 | Roll out to all users with preference toggle |

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Bare ACK emails sent | 0 | Email log audit |
| Threaded reply open rate | > 40% | Resend/Mailgun tracking |
| Threaded reply reply rate | > 5% | Reply-to tracking |
| User complaints about missing ACKs | 0 | Support tickets |
| Unsubscribe rate from threaded replies | < 0.5% | Resend tracking |

---

## Open Questions

1. Should threaded replies be immediate (within 15 min) or batched (hourly)?
2. Do we need a daily cap on threaded replies per user?
3. How do we handle threaded replies for drops that trigger automation (e.g., COMPASS onboarding)?
4. Should we A/B test Brooke voice vs. current neutral voice?

---

## Related

- Agent Board Drop #7: "Kill 'Drop received' ACK emails" (2026-03-17)
- Agent Board Drop #5: Unsubscribe/privacy compliance requirement
- Brooke Theme documentation: `docs/reference/templates/`
- PRD Section 5.x: Email system improvements

---

*Last updated: 2026-03-17 by SpecBot*
