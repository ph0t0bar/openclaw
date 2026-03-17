# SPEC-Unsubscribe-Privacy-Compliance-Audit

> **Status:** SKELETON — Drafted by SpecBot  
> **Source:** agent-board.md High-Priority Task #2 (Drop 1773719120783927)  
> **Priority:** 🚨 HIGH — Legal exposure  

---

## Problem Statement

All outbound emails from DropAnywhere/BHA ecosystem must include:
1. **Unsubscribe link** — One-click functional
2. **Physical address** — CAN-SPAM compliance
3. **Privacy policy link** — GDPR/CCPA
4. **Clear sender identification** — No spoofing

**Current Gap:** Enforcement inconsistency — some emails lack compliance elements.

---

## Scope

### Systems to Audit
- [ ] **DropAnywhere Hub** — Daily digests, weekly catch, onboarding
- [ ] **BrutallyHonest.ai** — Welcome emails, notifications
- [ ] **OpenClaw** — Agent-generated emails (EMAIL-LOG.md)
- [ ] **Poe Bots** — System messages (if any email flow)
- [ ] **Resend Dashboard** — Centralized audit trail

### Email Templates to Verify
| Template | Unsubscribe | Address | Privacy | Last Checked |
|----------|-------------|---------|---------|--------------|
| Daily Digest | ⬜ | ⬜ | ⬜ | — |
| Weekly Catch | ⬜ | ⬜ | ⬜ | — |
| Welcome Email | ⬜ | ⬜ | ⬜ | — |
| Password Reset | ⬜ | ⬜ | ⬜ | — |
| Billing/Receipts | ⬜ | ⬜ | ⬜ | — |
| Agent Notifications | ⬜ | ⬜ | ⬜ | — |

---

## Compliance Requirements

### CAN-SPAM (US)
- ✅ Accurate header information
- ✅ Non-deceptive subject lines
- ✅ Clear ad identification (if promotional)
- ✅ Physical postal address
- ✅ One-click unsubscribe (valid for 30 days)
- ✅ Honor unsubscribe within 10 business days

### GDPR (EU)
- ✅ Lawful basis for processing (consent or legitimate interest)
- ✅ Right to erasure honored
- ✅ Data processing disclosure
- ✅ Clear opt-out mechanism

### CCPA (California)
- ✅ "Do Not Sell My Info" (if applicable)
- ✅ Privacy policy link
- ✅ Opt-out mechanism

---

## Implementation Plan

### Phase 1: Audit (1 day)
- [ ] Inventory all email templates in Hub
- [ ] Inventory all email templates in BHA
- [ ] Check Resend dashboard for bounce/complaint rates
- [ ] Document current compliance gaps

### Phase 2: Fix Templates (1 day)
- [ ] Update Hub email templates with footer
- [ ] Update BHA email templates with footer
- [ ] Standardize unsubscribe endpoint: `POST /api/unsubscribe`
- [ ] Test all unsubscribe flows

### Phase 3: Process Enforcement (ongoing)
- [ ] Add compliance check to EMAIL-LOG.md workflow
- [ ] Create pre-send validation in Hub
- [ ] Monthly Resend audit (bounce rates > 5% = flag)

---

## Footer Template

```html
<!-- Standard Footer -->
<div style="margin-top: 40px; padding-top: 20px; border-top: 1px solid #e0e0e0; font-size: 12px; color: #666;">
  <p>
    DropAnywhere, Inc.<br>
    123 Main St<br>
    Chicago, IL 60601
  </p>
  <p>
    <a href="{{unsubscribe_url}}">Unsubscribe</a> | 
    <a href="https://drop-anywhere.com/privacy">Privacy Policy</a> | 
    <a href="https://drop-anywhere.com/terms">Terms</a>
  </p>
</div>
```

---

## Related

- `SPEC-Kill-Drop-ACK-Emails.md` — Replacing bare ACKs with threaded replies
- `EMAIL-STANDARDS-2026-03-16.md` — Email composition standards
- `DIGEST-POLICY-2026-03-16.md` — Digest generation policy
- `ops/agent-board.md` — Source task

---

## Success Criteria

- [ ] 100% of outbound emails include unsubscribe link
- [ ] 100% of outbound emails include physical address
- [ ] 100% of outbound emails include privacy policy link
- [ ] Unsubscribe requests honored within 24 hours (SLA: 10 business days)
- [ ] Bounce rate < 2% on Resend
- [ ] Complaint rate < 0.1% on Resend

---

*Skeleton created by SpecBot — flesh out before execution.*
