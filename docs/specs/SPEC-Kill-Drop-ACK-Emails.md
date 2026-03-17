# SPEC-Kill-Drop-ACK-Emails

> **Status:** Skeleton — Draft  
> **Created:** 2026-03-17 by SpecBot  
> **Source:** agent-board.md Drop #7, 1773719385661621  
> **Priority:** 🚨 HIGH — Product decision made, execution pending

---

## 1. Problem Statement

Bare "Drop received" ACK emails create friction and inbox clutter. They feel transactional, not helpful. They violate the "Your Second Brain Has No Inbox" philosophy by creating email noise for every drop.

### Current Behavior
- User sends drop → receives standalone email: "Drop received. Processing..."
- Separate thread for every drop creates inbox pollution
- No value-add — just confirmation of receipt

### Desired Behavior  
- User sends drop → silent processing or threaded Brooke-themed contextual reply
- No standalone ACK unless specifically requested
- Threaded replies add value (summary, insight, next step) not just confirmation

---

## 2. Success Criteria

| Metric | Target |
|--------|--------|
| ACK emails eliminated | 100% of drops (unless user opts in) |
| Threaded reply coverage | 100% of drops that generate insights |
| User inbox volume | -50% emails per active dropper |
| Reply engagement rate | >30% click-through on threaded replies |

---

## 3. Technical Approach

### 3.1 Email Threading Strategy

**For drops via email:**
- Set `In-Reply-To` header referencing original drop's `Message-ID`
- Set `References` header with thread chain
- Use same `Subject` prefix ("Re: Drop — [topic]")

**For drops via other channels (SMS, API, voice):**
- Generate synthetic `Message-ID` if not provided
- Include original drop content in reply body for context
- Subject: "Your drop about [extracted topic]"

### 3.2 Brooke-Themed Reply Templates

**Template 1: Simple Summary (for drops with clear topic)**
```
Subject: Re: Drop — [topic]

Hey [name],

Got it — [one-line summary of drop]. 

[Optional: One insight or follow-up question if obvious]

🦜 Brooke
```

**Template 2: Context + Next Step (for drops requiring action)**
```
Subject: Re: Drop — [topic]

Hey [name],

Captured: [summary]. 

I'll [action item or reminder context].

[Optional: Related memory link if relevant]

🦜 Brooke
```

**Template 3: Threaded Insight (for drops that triggered analysis)**
```
Subject: Re: Drop — [topic]

Hey [name],

You mentioned [topic] — this connects to [related previous drop/memory].

[Insight or pattern observation]

Want me to [offer: expand, remind, connect to digest]?

🦜 Brooke
```

### 3.3 Opt-In ACK for Users Who Want It

Some users may prefer confirmation. Add user preference:
- `email_ack_mode: "silent" | "threaded" | "confirm_only"`
- Default: "silent" (no ACK, threaded replies only when valuable)
- Migration: existing users keep current behavior unless they opt into "silent"

---

## 4. Implementation Notes

### Backend Changes
- [ ] Modify `send_drop_ack()` in Hub to check user preference
- [ ] Create `send_threaded_reply()` function with threading headers
- [ ] Update email template system to support Brooke voice
- [ ] Add `message_thread_id` tracking to drops table

### Frontend/API Changes  
- [ ] Add `email_ack_mode` to user preferences
- [ ] Expose in settings UI (mobile + web)

### Migration
- [ ] Backfill `message_thread_id` for recent drops
- [ ] Send communication about change to active email droppers

---

## 5. Dependencies

- **Blocked by:** None — product decision made
- **Blocks:** EMAIL-LOG.md audit (need to verify threaded replies are logged)
- **Related:** DIGEST-POLICY-2026-03-16.md, EMAIL-STANDARDS-2026-03-16.md

---

## 6. Open Questions

1. Should we A/B test threaded vs. silent for a subset of users?
2. What happens to drops that don't generate insights? (silent vs. minimal ACK)
3. How do we handle threading for forwarded drops or email chains?
4. Emoji policy in Brooke replies? (🦜 parrot brand yes/no?)

---

## 7. References

- Source drop: #1773719385661621 (Joey: "Kill 'Drop received' ACK emails")
- Related PRD: EMAIL-STANDARDS-2026-03-16.md
- Design system: Brooke Theme (cream/sage/copper, Newsreader)

---

*Skeleton created by SpecBot — flesh out sections as implementation approaches.*
