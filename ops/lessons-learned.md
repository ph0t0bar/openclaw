---

## 2026-03-16 (22:28 UTC) — LearningBot: Voice Research Gaps & Onboarding Patterns

### Lesson: Voice Research Has Fresher Content in Older Vault Entries

**What happened:**
Researcher 21:53 UTC searched Hub drops for Joey's latest thinking but found mostly BHA user sessions (205/263 drops this week). Query 1 "idea feature want" → old email forwards. Query 2 "build product AI" → Jan 2026 session checkpoints. Query 3 "future vision next" → DCS hydration notes from earlier. Key insight: Most recent drops are BHA activity, not Joey's personal ideation.

**Why it matters:**
Agent trying to find "latest thinking" looked in recent drops, but Joey's strategic thinking appears in older vault entries (Jan-Feb 2026), not current BHA sessions. Looking in wrong temporal direction.

**How to prevent:**
- For Joey's strategic thinking: search older vault (Jan-Feb 2026) not recent drops
- For product signals: mine BHA user patterns, not Joey's explicit statements  
- For feature ideas: check session checkpoints and DCS context, not email forwards
- Document content freshness map: what's in recent vs older vault

---

### Lesson: 97% Activation Rate with 3 Persistent Zero-Drop Users

**What happened:**
OnboardBot 22:22 UTC confirmed: 101 total users, 98/101 have 1+ drops (97% activation rate). But same 3 users remain at 0 drops across multiple checks: hamer.daniel@gmail.com (Danny), steventazic@gmail.com, mitch.p.hamer@gmail.com.

**Why it matters:**
Near-perfect activation rate validates funnel, but persistent 3% never-activated cohort suggests systemic barrier, not random drop-off. Danny is family member — personal outreach needed, not automated nurture.

**Pattern:**
Zero-drop users fall into two buckets:
1. **Family/friends** — need personal onboarding, not email sequences
2. **Test signups** — may have different intent (curiosity vs usage)

**How to address:**
- Segment zero-drop users by relationship (family vs stranger)
- Family: personal text/call from Joey
- Others: re-engagement flow with friction-reduction focus
- Track time-to-first-drop: if >7 days, high probability of permanent zero-drop

---

### Lesson: BHA Drives 100% of Recent Acquisition

**What happened:**
OnboardBot confirmed 22/22 active users in last 72h came from BHA. Zero direct/DropAnywhere signups in recent period. BHA = exclusive acquisition channel for active users.

**Why it matters:**
Single-channel dependency. If BHA has outage, conversion drops to zero. No organic/direct acquisition happening despite SEO/content efforts.

**How to mitigate:**
- Diversify acquisition: SEO (currently invisible), content marketing, founder brand
- Launch week (Mar 24-30) should test organic channels
- Monitor BHA → DA funnel health as critical metric
- Consider what happens if Poe/BHA has outage

---

### Lesson: Silent Cron Jobs Need Visibility

**What happened:**
Pattern 110 detected earlier: MetricsSnapshotBot and DropMiningBot scheduled but not logging. 22:28 UTC check: still no output from these scheduled jobs in recent memory log.

**Why it matters:**
Scheduled jobs may be running silently, failing silently, or not running at all. No visibility = no ability to debug or verify.

**Root cause:**
Cron jobs may be running in isolated sessions that don't log to main memory file, or failing before log write, or never triggered.

**How to fix:**
- Add explicit log entry at job START and COMPLETION
- Write to dedicated cron-status.json file with timestamps
- Add heartbeat: last run timestamp visible to other agents
- Consider moving scheduled work to agent-based triggering (Chief of Staff triggers rather than pure cron)

---

*End of LearningBot cycle 22:28 UTC*
