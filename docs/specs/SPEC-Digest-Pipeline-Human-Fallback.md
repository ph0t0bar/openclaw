# SPEC-Digest-Pipeline-Human-Fallback.md

## Status: SKELETON — Draft for Review

**Created:** 2026-03-18 03:42 UTC  
**Source:** Agent Board Strategic Notes (20:33, 20:49, 01:07, 02:48 UTC)  
**Priority:** P0 — Core Product Failure  
**Owner:** TBD

---

## Problem Statement

The digest pipeline has **zero redundancy**. When Dropper-Code's Claude Code hits usage limits, 105+ users receive no digests. Current state: **2/107 digests sent in 24h** (PRD Section 8).

**The Danny Advisory Model Insight:** Danny gets reliable emails because Joey (human) is in the loop. When automation fails, there's a human fallback. The DA digest pipeline has no such fallback — it just fails silently.

---

## Goals

1. **Zero Silent Failures:** Detect digest pipeline stalls within 2 hours
2. **Human Fallback:** Alert Joey via WhatsApp with one-click approval to send degraded-mode digests
3. **Trust Preservation:** No user goes >24h without a digest without explicit acknowledgment

---

## Non-Goals

- Full automation replacement (human-in-loop is the feature, not a bug)
- Complex retry logic (focus on detection + human escalation)
- New digest template design (use existing Brooke template)

---

## Success Metrics

| Metric | Current | Target |
|--------|---------|--------|
| Digests sent / eligible users | 2% | 95% |
| Time to detect stall | Unknown | <2 hours |
| User complaints about missed digests | ? | Zero |

---

## Proposed Architecture

### 1. Digest Monitoring Endpoint

```python
# GET /api/admin/digest-status
{
  "users_eligible": 108,
  "digests_sent_24h": 2,
  "stall_detected": true,
  "stalled_users": ["user_id_1", "user_id_2", ...],
  "last_successful_batch": "2026-03-17T03:00:00Z",
  "dropper_code_status": "claude_limit_exhausted",
  "recommended_action": "human_fallback"
}
```

### 2. Human Fallback Alert

When `digest_sender.py` fails for >2 hours:

```python
# POST to OpenClaw webhook
{
  "alert_type": "DIGEST_STALL",
  "severity": "critical",
  "message": "DIGEST STALLED: 105 users waiting. Last batch: 21h ago.",
  "action_url": "https://hub.../admin/digest-fallback",
  "approve_text": "Send degraded digests now",
  "stall_reason": "Claude Code usage limits (resets Mar 20 3am UTC)"
}
```

### 3. Degraded Mode Digest

Simpler template that doesn't require Claude:
- Static template (Brooke-themed)
- No AI-generated insights
- Basic "Your drops from the last 24h" list
- One-click approval from Joey

---

## Open Questions

1. Should degraded digests include AI insights or just raw drops?
2. What's the SLA for Joey response? (Auto-send after X hours?)
3. Should this integrate with existing alert monitors or be standalone?
4. How to handle partial failures (some users get digests, others don't)?

---

## Related

- PRD Section 8 (Metrics showing 2/107 digests sent)
- SPEC-Morning-Brief-Template-Redesign.md (Brooke template ready)
- Agent Board notes: 20:33, 20:49, 01:07, 02:48 UTC

---

## Next Steps

1. [ ] Review with Joey — is human-in-loop the right approach?
2. [ ] Design degraded-mode digest template
3. [ ] Implement `/api/admin/digest-status` endpoint
4. [ ] Wire up OpenClaw WhatsApp alerts
5. [ ] Test with Joey-only send before rolling to all users

---

*The board has spoken: 40+ strategic notes converged on this one truth — the digest pipeline needs redundancy. This spec is the skeleton. Flesh it out or discard it, but don't debate it for another 20 hours.* 🦜
