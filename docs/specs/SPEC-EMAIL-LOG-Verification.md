# SPEC-EMAIL-LOG-Verification-Protocol

**Status:** Skeleton  
**Created:** 2026-03-17  
**Source:** FeedbackBot Task Queue (Drop 1773719281471780)  
**Priority:** MEDIUM  

---

## Problem Statement

Agent-generated emails may not be consistently logged to EMAIL-LOG.md. This creates a compliance and audit gap where outbound communications cannot be traced back to their originating agent, task, or timestamp.

---

## Goals

1. **Audit Coverage** — Verify all agent-generated emails are being logged
2. **Standardization** — Ensure consistent EMAIL-LOG.md format across all agents
3. **Gap Detection** — Identify any unlogged emails from recent agent runs
4. **Process Enforcement** — Document requirements for future agent email generation

---

## Background

From ops/agent-board.md:
> "Maintain EMAIL-LOG.md for all agent-generated emails (Joey's request)"

This was logged as a process requirement during FeedbackBot processing of Drop 6 (03:48 UTC).

---

## Scope

### In Scope
- All agent-generated emails from OpenClaw agents (DecisionBot, FeedbackBot, DigestBot, etc.)
- Emails sent via Resend API through Hub
- Emails triggered by cron jobs
- Emails triggered by heartbeat actions

### Out of Scope
- User-initiated emails (manual sends)
- System notification emails (infrastructure alerts)
- Third-party service emails (Stripe, Railway, etc.)

---

## Audit Checklist (Draft)

### Phase 1: Discovery
- [ ] Identify all email-sending code paths in OpenClaw agents
- [ ] List all Resend API calls in the codebase
- [ ] Review recent Hub webhook logs for email events
- [ ] Check EMAIL-LOG.md exists and is in correct location

### Phase 2: Gap Analysis
- [ ] Cross-reference sent emails (Resend dashboard) vs logged emails
- [ ] Identify any unlogged email sends in last 30 days
- [ ] Check for partial logs (email sent but missing metadata)

### Phase 3: Standardization
- [ ] Define required EMAIL-LOG.md format
- [ ] Document mandatory fields for each log entry
- [ ] Create helper function/template for consistent logging

### Phase 4: Remediation
- [ ] Backfill any missing log entries (if possible)
- [ ] Update all email-sending agents to use standardized logging
- [ ] Add EMAIL-LOG verification to agent post-flight checklist

---

## Proposed Log Format

```markdown
## YYYY-MM-DD HH:MM UTC — [AgentName]

**To:** recipient@example.com  
**Subject:** Email subject line  
**Source:** [cron/heartbeat/manual/agent-task]  
**Task:** Link to originating task/issue  
**Resend ID:** [resend message ID for traceability]

**Content Summary:**
Brief description of email purpose (not full body for privacy)

**Status:** ✅ Sent / ❌ Failed / ⏭️ Queued
```

---

## Email-Sending Agents to Audit

| Agent | Email Types | Logging Status | Notes |
|-------|-------------|----------------|-------|
| DecisionBot | Approval notifications, task completions | ? | |
| FeedbackBot | Drop routing confirmations | ? | |
| DigestBot | Daily digests, weekly catches | ? | |
| SpecBot | Spec creation confirmations | ? | |
| ? | ? | ? | |

---

## Open Questions

1. Where should EMAIL-LOG.md live? (`docs/`? `ops/`? `memory/`?)
2. Should we log full email bodies or just metadata?
3. How far back should the backfill go?
4. Should unlogged emails trigger alerts?
5. Integration with Hub's email webhook for automatic logging?

---

## Success Criteria

- [ ] 100% of agent-generated emails logged within 24 hours of send
- [ ] All email log entries follow standardized format
- [ ] Gap analysis report delivered to Joey
- [ ] Process documented for future agent development

---

## Dependencies

- Access to Resend dashboard/API for email history
- Hub webhook logs for email events
- Agent code review to identify all send paths

---

## Related

- ops/agent-board.md — FeedbackBot task queue
- SPEC-Kill-Drop-ACK-Emails.md — Email product changes
- SPEC-Unsubscribe-Privacy-Compliance-Audit.md — Email compliance

---

*Skeleton created by SpecBot — 2026-03-17 20:03 UTC*
