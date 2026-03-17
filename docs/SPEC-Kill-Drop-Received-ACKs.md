# SPEC-Kill-Drop-Received-ACKs — Product Spec

**Status:** Draft  
**Created:** 2026-03-17  
**Source:** Joey Drop #7 + Agent-Board Decision  
**Priority:** 🚨 HIGH (Product Decision Made)

---

## Problem

Current "Drop received" acknowledgment emails are bare, transactional, and create friction:
- Subject: "Drop received"
- Body: Minimal confirmation with no value-add
- Feel: Robotic, system-generated noise
- Result: Users learn to ignore DropAnywhere emails

## Solution

**Replace bare ACKs with Brooke-themed threaded replies** that:
1. Confirm receipt (still)
2. Add lightweight value (context, insight, or warmth)
3. Use Brooke persona voice (warm, helpful, human)
4. Thread properly so inbox stays organized

---

## Current State

```
Subject: Drop received

Your drop has been received and will be processed.

— DropAnywhere
```

## Target State

```
Subject: Re: [Original Drop Subject]

Got it 🦜

[Contextual response based on drop content]
— Brooke
```

---

## Implementation Checklist

- [ ] Design new email template in Brooke voice
- [ ] Implement threading (In-Reply-To headers)
- [ ] Add content-aware snippet generation
- [ ] A/B test vs current bare ACK
- [ ] Monitor reply rates and sentiment

## Open Questions

1. Should we include a "processing ETA" indicator?
2. How much context should the threaded reply include?
3. Do we still send ACK for drops that trigger immediate processing?

---

## References

- Source Drop: #1773719385661621
- Agent-Board Decision: PRODUCT-KILL-ACK-EMAILS
- Voice Reference: weekly-catch-STYLE-GUIDE.md
