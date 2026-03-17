---

## 2026-03-17 (06:23 UTC) — LearningBot: Secret Exposure & Crisis Overstatement

### Lesson: Exposed Secrets in Git History — Critical Security Escalation

**What happened:**
05:29 UTC: Sentry secret scan flagged 🔴 CRITICAL — "Exposed API keys in git history (Anthropic, Stripe, GitHub)." Escalated to ops/escalations.md.

**The gap:**
Regular HEAD~3 scans were clean (🟢), but historical git history contained exposed credentials. Sentry only scans recent commits, not full history. Old commits with keys remained undetected.

**Why it matters:**
Git history is forever. Even if current code is clean, old commits with keys can be mined by attackers. This is a common attack vector.

**Fix:**
- Full git history audit (not just HEAD~3)
- GitHub secret scanning enabled on repo
- Key rotation for any exposed credentials
- Pre-commit hooks to prevent future exposure
- Consider git-filter-repo to purge history if needed

---

### Lesson: Poe Crisis Overstated — Balance Topped Up Without Emergency

**What happened:**
05:30 UTC: Ops Monitor showed Poe balance at 283,939 (healthy). 05:33 UTC: DocBot confirmed "Poe balance topped up 12,522💀→283,939✅ (crisis resolved)."

**The contradiction:**
System spent 3+ hours in "CRITICAL" mode with "~35min runway" alerts. Actual balance never hit zero and was topped up normally. The crisis was significantly overstated.

**Root cause:**
- Burn rate calculated from 6h window included Joey's historical usage spikes
- Agents calculated independently without validating against actual balance deltas
- "CRITICAL" threshold triggered too early (at ~12K balance vs actual ~6h runway)

**The cost:**
- 3+ hours of elevated alert fatigue
- Potential over-reaction (pausing agents unnecessarily)
- Distrust in monitoring when "crisis" resolves without incident

**Fix:**
- Validate burn projection: compare projected vs actual balance change over 1h
- If projected vs actual diverges > 2x → flag calculation as suspect
- Use smoothed 12h burn rate, not volatile 6h window
- "CRITICAL" threshold = 2h actual runway (validated), not projected

---

### Lesson: Digest Policy Misdiagnosis — Intentional Off-State Treated as Bug

**What happened:**
05:35 UTC: Heartbeat noted "Digest stall is FALSE ALARM — digests intentionally off (waitlist admission, see ops/DIGEST-POLICY.md)."

Earlier, multiple agents had:
- Created wrong tasks to "fix" digest stall (task_1773671381_109, task_1773685322_843 — both cancelled)
- Flagged digest stall as launch blocker
- Escalated to critical status

**The gap:**
DIGEST-POLICY.md existed but wasn't propagated to agent context. Agents assumed "3 digests sent = broken" rather than "3 digests = intentional (only Joey receives them)."

**Root cause:**
- Policy docs exist but aren't in agent working memory
- No explicit "digest policy: INTENTIONALLY OFF" in heartbeat state
- Agents pattern-matched to "low digest count = bug" without checking policy

**Fix:**
- Add explicit `digest_policy: "INTENTIONALLY_OFF"` to heartbeat-state.json
- Heartbeat check reads policy before flagging stall
- Policy changes require config update, not just doc update
- Morning brief includes current policy state block

---

### Lesson: Spec Sync from Remote — 4 Missing Specs Discovered

**What happened (SUCCESS):**
05:23 UTC: SpecBot compared remote joey-backup/specs vs local docs/specs. Found 4 specs missing locally:
- STRATEGIC-POLL-Email-Only-2026-03-16.md
- STRATEGIC-ANSWERS-Email-Only-2026-03-16.md  
- data-dump-content-creation-workflow.md
- escalations.md

All 4 synced from remote to local.

**The win:**
Cross-repo comparison found drift. Specs created in other contexts (or older backups) were missing from workspace.

**The gap:**
No automated spec sync. Relies on SpecBot manual comparison. Drift accumulates silently.

**Fix:**
- SpecBot runs bidirectional sync every 6h
- Specs are single-source (joey-backup) with local cache
- Git pre-commit hook warns if specs not synced
- Spec changelog tracked (not just file existence)

---

### Lesson: Constitution Self-Correction — 93% Operational Rate Achieved

**What happened (SUCCESS):**
05:21 UTC: Governance updated constitution — roster corrected from "4/25 agents active" (outdated crisis narrative) to "25/27 agents (93% operational)."

**The pattern:**
System recovered from timeout crisis (80% failure → 93% operational in ~18 hours). Constitution now reflects reality.

**Key insight:**
Crisis-to-perfection arc validated again. Constraint (300s timeout) forced architectural simplification (25 agents → core 5 + message bottles).

**Remaining gap:**
- 2 idle agents (StripeBot, RailwayBot)
- 3 agents with timeout errors (DocBot, PatternBot, SpecBot)
- WhatsApp delivery errors blocking 3 scheduled jobs

**Fix:**
- Weekly constitution audit (not just during crisis)
- Idle agent → auto-disable after 7 days
- Error-prone agent → prompt review required

---

### Lesson: Heartbeat Policy Verification — Check Before Escalating

**What happened:**
Earlier heartbeats escalated digest stall to Joey. 05:35 UTC heartbeat correctly identified "FALSE ALARM" after reading DIGEST-POLICY.md.

**The fix:**
Heartbeat now reads policy before escalating:
- Digest stall detected → check `digest_policy` state
- If INTENTIONALLY_OFF → log only, no escalation
- If ENABLED → escalate normally

**Generalization:**
All heartbeat checks should verify policy state before escalating:
- Digest stall → check digest_policy
- Poe balance → check auto_topup_enabled
- Task failures → check retry_policy
- Family retention → check outreach_policy

**Implementation:**
Add `policy_verification` layer to heartbeat system. Escalation = anomaly + policy allows escalation.

---

*End of LearningBot cycle 06:23 UTC*

