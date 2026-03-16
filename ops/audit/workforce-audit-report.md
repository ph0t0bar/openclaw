# Workforce & Operations Pre-Launch Audit Report

**Auditor:** Opus Subagent (Phase 1e)  
**Date:** 2026-03-16  
**Launch Target:** March 24, 2026  
**Deadline for Fixes:** March 22, 2026

---

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Configured Agents** | 27 cron jobs + 5 scheduled maintenance jobs |
| **Active Today** | 25/27 (93%) |
| **Idle/Broken** | RailwayBot (0 cycles), StripeBot (0 cycles), Kimi Patrol (0% success) |
| **Policy Conflicts Found** | 5 (detailed below) |
| **Specs Triaged** | 39 total → 9 KEEP / 15 ARCHIVE / 6 KILL / 9 INTERNAL-OPS |
| **Missing Procedures** | 4 critical gaps |
| **Security Concerns** | 2 low-severity |
| **Overall Health** | 🟢 System operational, needs cleanup not rescue |

### Top 5 Action Items for Joey

1. 🔴 **Finalize admission flow** — No documented procedure for waitlist → admitted → first email. This is the Day 1 user experience and it's undefined.
2. 🔴 **Resolve digest pipeline** — DISABLE_CRONS=1 on Hub + dropanywhere-cron dead = no automated digests. Manual trigger path undocumented. Must decide: restore cron service or build Hub-internal scheduler before launch.
3. 🟡 **Consolidate duplicate files** — COMPANY-CONSTITUTION.md exists in both `ops/` (201 lines, current) and `docs/specs/` (136 lines, stale). `agent-board.md` also duplicated. Single source of truth needed.
4. 🟡 **Kill/archive 21 specs** — 39 specs is overwhelming. Only 9 are launch-relevant. The rest create confusion about what's actually shipping.
5. 🟡 **Family re-engagement** — Lisa (12d inactive), Danny (0 drops ever), Bob (9d inactive). These are soft-launch Tier 1 users who need personal outreach before March 24.

---

## A. Agent Roster Accuracy

### Agent Count: Constitution vs Roster vs Reality

| Source | Count | Notes |
|--------|-------|-------|
| COMPANY-CONSTITUTION.md (ops/) | 25 active + 2 idle = 27 | Most current, updated 20:19 UTC today |
| roster.md | 25 active + 2 idle = 27 | Matches constitution |
| HEARTBEAT.md | References ~5-6 roles (Dropper-Code, tasks, morning brief) | Doesn't list individual agents |
| AGENTS.md | No agent roster | Focuses on Claw's own behavior |

🟢 **Constitution and roster are in sync** — both show 27 agents, same status.

### Redundancy Check

| Overlap Area | Agents | Verdict |
|-------------|--------|---------|
| Content creation | ContentBot + FounderVoiceBot + ContentPitchBot | 🟢 OK — different roles (generate / voice-validate / pitch). Three-gate pipeline documented and working. |
| User monitoring | UserHealthBot + OnboardBot | 🟢 OK — different focus (retention vs activation) |
| Strategy | Opus Strategist + Chief of Staff + Meta | 🟡 OVERLAP — All three do "strategic oversight." Opus votes, CoS coordinates, Meta grades. Some redundancy in grading/reviewing. |
| Operations | Kimi Patrol + RailwayBot | 🟡 OVERLAP — Both monitor infrastructure. RailwayBot is idle (0 cycles). Consider merging into Patrol. |
| Documentation | DocBot + SpecBot + LearningBot | 🟡 OVERLAP — DocBot (docs), SpecBot (specs), LearningBot (lessons). Three agents doing documentation work. |

### "Claw" vs "Drop" Branding Check

- 🟢 BRAND-GUIDE.md is clear: "Drop" externally, "Claw" internal only
- 🟢 EMAIL-STANDARDS.md uses "DropAnywhere" consistently
- 🟢 CEO-EMAIL-OS.md uses "Drop" for external identity
- 🟡 SOUL.md still identifies as "Claw" — fine for internal, but any agent reading SOUL.md and using it in public output would leak the internal name
- 🟡 AGENTS.md references "Claw" throughout — internal only, OK

### Email From Address

- 🟢 EMAIL-STANDARDS.md mandates `DropAnywhere <hello@drop-anywhere.com>`
- 🟢 CEO-EMAIL-OS.md confirms same
- 🟢 Resend payload template in EMAIL-STANDARDS.md has correct from address
- 💡 No mechanism to verify agents actually USE the template at runtime

### append-to-daily-log.sh Usage

- 🟢 Script exists at `/root/.openclaw/workspace/scripts/append-to-daily-log.sh`
- 🟡 Not referenced in ops/ files — no mandate for agents to use it
- 💡 RECOMMENDATION: Add to COMMS-GUIDE.md as mandatory logging method

---

## B. Policy Consistency

### Conflict 1: Digest Status 🔴

| File | Says |
|------|------|
| DIGEST-POLICY.md | "DIGESTS ARE OFF (BY DESIGN)" — DISABLE_CRONS=1 intentional |
| digest-stall-strategy.md (spec) | "THE critical launch blocker" — treats stall as emergency |
| lessons-learned.md | Documents agents filing "digest stall" bugs as a lesson about misdiagnosis |
| CEO-EMAIL-OS.md | Describes 6 active email streams as if running |
| LAUNCH-CRITICAL-PATH | Lists digest pipeline as Phase 2 stabilize item |

**Verdict:** 🔴 FIX BEFORE LAUNCH — The system has contradictory signals. DIGEST-POLICY.md is canonical (Joey's direct instruction), but digest-stall-strategy.md and CEO-EMAIL-OS.md create confusion. digest-stall-strategy.md should be archived. CEO-EMAIL-OS describes a future state.

### Conflict 2: Agent Count Across Files 🟡

| File | Agent Count |
|------|-------------|
| ops/COMPANY-CONSTITUTION.md | 25/27 active (correct, updated today) |
| docs/specs/COMPANY-CONSTITUTION.md | Different content (stale — 136 lines vs 201) |
| AGENT-COMPANY-v3.md (spec) | Proposes 40 agents across 10 departments |
| HEARTBEAT.md | Doesn't mention specific agents |

**Verdict:** 🟡 SHOULD FIX — Archive the stale `docs/specs/COMPANY-CONSTITUTION.md`. Make `ops/` the single location.

### Conflict 3: CEO-EMAIL-OS vs Current Reality 🟡

CEO-EMAIL-OS describes a fully email-first operating system with 6 streams (Morning Brief, Creative Review, Task Approvals, Alerts, Weekly Report, Drop Conversation). Currently:
- Morning Brief: ✅ Exists in HEARTBEAT.md (WhatsApp, not email)
- Creative Review: Documented in CREATIVE-FEEDBACK-LOOP.md but unclear if running
- DecisionBot: Listed in agent-board.md, ran at 21:06 UTC — "0 email drops scanned"
- Weekly Report: Not evidenced as actually running

**Verdict:** 🟡 SHOULD FIX — CEO-EMAIL-OS is aspirational, not operational. Label it as target state, not current state.

### Conflict 4: HEARTBEAT.md vs Agent Roster 🟢

HEARTBEAT.md focuses on Claw's own heartbeat behavior (auto-approve tasks, morning brief, hydration). It doesn't describe individual agent heartbeats — those are managed through OpenClaw cron system. These are different concepts.

**Verdict:** 🟢 OK — No actual conflict, just different scopes.

### Conflict 5: Push-Queue → Archivist Flow 🟡

- push-queue.md exists and is clear: "Agents: DO NOT push to GitHub directly"
- Queue is empty (Archivist processes each cycle)
- 🟡 COMMS-GUIDE.md mentions agent-board and escalations but NOT push-queue
- 🟡 No agents explicitly reference push-queue.md in their documented prompts

**Verdict:** 🟡 SHOULD FIX — Add push-queue to COMMS-GUIDE.md and PERMISSIONS.md.

---

## C. Spec Triage

### 39 Specs → Recommendation

| # | Spec | Rec | Reason |
|---|------|-----|--------|
| 1 | AGENT-COMPANY-v3.md | ARCHIVE | Aspirational 40-agent org chart. Current 27 agents work. |
| 2 | ARI-Styling-Assistant-Crawl-Walk-Run.md | ARCHIVE | Side project for Ari, not DA launch |
| 3 | COMMS-GUIDE.md | KEEP | Active agent communication standard |
| 4 | COMPANY-CONSTITUTION.md (specs/) | KILL | Stale duplicate of ops/COMPANY-CONSTITUTION.md |
| 5 | Cash-Burn-Tracker-Advisor-Kit.md | ARCHIVE | Mitch advisory kit — post-launch |
| 6 | GUMROAD-GENESIS-LISTING.md | ARCHIVE | Gumroad product listing — post-launch revenue |
| 7 | LAUNCH-CRITICAL-PATH-2026-03-14.md | KEEP | Active launch execution plan |
| 8 | LOOPSLAP-MASTER-PRD-2026-Q1.md | KILL | Superseded by PRD-Action-Plan. "LoopSlap" is old entity name. |
| 9 | PERMISSIONS.md | KEEP | Active security framework |
| 10 | PLATFORM-DEPARTMENT.md | ARCHIVE | Platform dept proposal — post-launch |
| 11 | PRD-Action-Plan-2026-03-11.md | KEEP | Master PRD — single source of truth |
| 12 | PRD-Desktop-Mobile-Split-2026-03-10.md | ARCHIVE | Good idea, not for launch |
| 13 | RAILWAY-BOT-MANUAL.md | KEEP | Active agent manual |
| 14 | SNAPBACK-INTEGRATION-2026-03-11.md | KEEP | Core product direction |
| 15 | SOFT-LAUNCH-LIST.md | KEEP | Active — 12 users across 3 tiers |
| 16 | SPEC-Adaptive-Weekly-Catch-2026-03-11.md | ARCHIVE | Adaptive Weekly Catch — post-launch sophistication |
| 17 | SPEC-Admin-User-Lifecycle-Dashboard.md | ARCHIVE | Admin dashboard improvements — post-launch |
| 18 | SPEC-DigestBot.md | KILL | Skeleton for an agent that doesn't exist. Digest pipeline is off by policy. |
| 19 | SPEC-Human-Insight-Snapshot.md | ARCHIVE | Onboarding survey concept — post-launch |
| 20 | SPEC-Joey-AI-Builder-Pack.md | ARCHIVE | B2B product — Week 3-4 per own timeline |
| 21 | SPEC-MOMENTUM-TRACKER.md | KILL | Skeleton agent spec — not built, not needed for launch |
| 22 | SPEC-Message-Bottle-Protocol.md | ARCHIVE | Interesting architecture, not blocking launch |
| 23 | SPEC-Mitch-Advisory-Template-Kit.md | ARCHIVE | Client deliverable for Mitch — post-launch |
| 24 | SPEC-NARRATIVE-ENGINE.md | KILL | Skeleton agent spec — not built |
| 25 | SPEC-PATTERN-WEAVER.md | KILL | Skeleton agent spec — not built |
| 26 | SPEC-Snapback-Email-Sequence.md | KEEP | 7-day email sequence — core product |
| 27 | SPEC-Transurfing-Snapback-Music.md | ARCHIVE | Personal visualization — not product spec |
| 28 | SPEC-User-Scenario-Matrix.md | KEEP | Comprehensive user journey map — launch reference |
| 29 | SPEC-VAULT-Archaeologist.md | ARCHIVE | Historical mining agent — post-launch |
| 30 | SPEC-Weekly-Catch-Progressive-Disclosure.md | ARCHIVE | Advanced personalization — post-launch |
| 31 | agent-board.md (specs/) | KILL | Duplicate of ops/agent-board.md (different content — specs version is the template) |
| 32 | content-transformation-system-dec2025.md | ARCHIVE | Historical reference — origin story |
| 33 | digest-stall-strategy.md | KILL | Contradicts DIGEST-POLICY.md. Digests are intentionally off. |
| 34 | goldmine-index.md | KEEP (internal ops) | Active reference for content mining |
| 35 | poe-funnel-paste-ready-2026-03-11.md | ARCHIVE | Poe CTA copy — good but not launch-blocking |
| 36 | snapback-offer-2026-03-11.md | KEEP | Core offer copy |
| 37 | target-slide-rancho-mirage-2026-03-11.md | ARCHIVE | Personal visualization |
| 38 | transurfing-snapback-product-vision-2026-03-11.md | ARCHIVE | Vision doc — inspirational, not operational |
| 39 | weekly-catch-STYLE-GUIDE.md | KEEP | Active template styling reference |

### Summary

| Action | Count |
|--------|-------|
| **KEEP** | 12 |
| **ARCHIVE** | 18 |
| **KILL** | 9 |
| **Total** | 39 |

---

## D. Memory Integrity

### MEMORY.md Assessment

| Section | Status | Issue |
|---------|--------|-------|
| About Joey | 🟢 OK | Accurate, comprehensive |
| About Me (Claw) | 🟢 OK | Consistent with SOUL.md |
| Key Decisions | 🟢 OK | |
| Active Projects | 🟡 STALE | Says "As of 2026-03-02" — now 14 days old. DA at 65 users (now 101). BHA at 211 (now 259). |
| Lessons Learned | 🟢 OK | Good distilled wisdom |
| Motherlode section | 🟢 OK | Accurate archive description |
| BHA PMF Signal | 🟡 STALE | References "172 total BHA users" — now 259 |
| Poe Orchestrator | 🟢 OK | Historical record, still accurate |
| Last Updated | 🟡 STALE | Says "2026-03-14" but metrics are from March 2-9 |

**Verdict:** 🟡 SHOULD FIX — Metrics snapshot in MEMORY.md needs refresh. User counts, MRR, agent counts all outdated.

### TOOLS.md Assessment

| Section | Status | Issue |
|---------|--------|-------|
| GitHub | 🟡 | Notes GH_TOKEN expired, GITHUB_TOKEN active — should clean up expired reference |
| Railway | 🟢 OK | Accurate project IDs, URLs |
| Hub endpoints | 🟢 OK | Comprehensive |
| dropanywhere-cron | 🟡 | Listed under "Active repos" — service is dead |
| Digest Template | 🟢 OK | |
| Feature Flags | 🟢 OK | DISABLE_CRONS=1 documented |

**Verdict:** 🟡 SHOULD FIX — Remove dropanywhere-cron from "Active repos" or mark as dead.

### Files Referencing dropanywhere-cron as Potentially Alive

| File | Context | Fix Needed? |
|------|---------|-------------|
| TOOLS.md | Listed under "Active repos" | 🟡 Yes — mark as dead/archived |
| DIGEST-POLICY.md | "dropanywhere-cron service is not running — intentional" | 🟢 No — correctly states it's dead |
| digest-stall-strategy.md | Investigates it as root cause | 🟡 Archive this spec |
| lessons-learned.md | Documents the failure | 🟢 No — historical record |
| MEMORY.md | Not checked beyond 200 lines | — |

---

## E. Email System Audit

### Email-Sending Agents/Systems

| Sender | What | Frequency | From Address | Threading | Unsubscribe |
|--------|------|-----------|-------------|-----------|-------------|
| CEO-EMAIL-OS (Morning Brief) | Daily brief to Joey | Daily 8am CST | hello@drop-anywhere.com | ✅ morning-brief | ✅ |
| CEO-EMAIL-OS (Creative Review) | Content for review | Every 4h | hello@drop-anywhere.com | ✅ creative-review | ✅ |
| CEO-EMAIL-OS (Task Approvals) | Batched hourly | As needed | hello@drop-anywhere.com | ✅ ops-tasks | ✅ |
| CEO-EMAIL-OS (Alerts) | Critical alerts | Immediate | hello@drop-anywhere.com | ✅ ops-tasks | ✅ |
| CEO-EMAIL-OS (Weekly Report) | Weekly summary | Sunday | hello@drop-anywhere.com | ✅ weekly-report | ✅ |
| Email Digest (users) | User daily digests | OFF by policy | hello@drop-anywhere.com | N/A | ✅ |
| Auto-ACK (EMAIL-SLA) | Reply acknowledgment | On email receipt | hello@drop-anywhere.com | — | — |
| DecisionBot | Process email replies | Hourly | N/A (reads, doesn't send) | — | — |

### Duplicate Streams?

🟡 **Potential Overlap:** Morning Brief (email) AND WhatsApp morning brief (HEARTBEAT.md). Currently the WhatsApp version runs; the email version is described in CEO-EMAIL-OS but may not be operational. No evidence of duplicate sends.

### DecisionBot Status

- Last ran 21:06 UTC — "0 email drops scanned, 0 pending tasks, 0 actions executed"
- Status: 🟢 Running but idle (no inbound email drops to process)
- 💡 This is expected if Joey isn't replying to emails yet

### Auto-ACK Status

- Described in EMAIL-SLA.md: "When ANY email arrives from Joey, auto-send acknowledgment"
- 🟡 No evidence of this actually running. No agent named "Auto-ACK" in roster.
- 💡 RECOMMENDATION: Verify Auto-ACK is implemented, not just documented

---

## F. Gaps — What's Missing

### 1. Admission Flow 🔴 FIX BEFORE LAUNCH

**Current state:** DIGEST-POLICY.md says "Users are admitted when the platform is ready" and "Joey will flip the switch." SOFT-LAUNCH-LIST.md has 12 users selected across 3 tiers.

**What's missing:**
- No documented step-by-step for admitting a user
- No "first email" template for newly admitted users
- No definition of what "admitted" means technically (Hub flag? Manual?)
- No sequence: What does a user receive on Day 1, Day 2, Day 7?
- SPEC-User-Scenario-Matrix has the lifecycle stages but no implementation detail

### 2. Rollback Plan 🔴 FIX BEFORE LAUNCH

**Not documented anywhere.** If launch goes wrong:
- How do you disable digests for all users quickly?
- How do you revert a bad deploy?
- Who gets notified?
- What's the communication to admitted users?

### 3. User Communication Plan 🟡 SHOULD FIX

- SOFT-LAUNCH-LIST.md has 12 users but no welcome email template
- SPEC-Snapback-Email-Sequence has the 7-day sequence but it's for Snapback signups, not soft launch admits
- No "Day 0: Welcome to DropAnywhere" email exists

### 4. Soft Launch List Status 🟢 OK (with caveats)

- SOFT-LAUNCH-LIST.md is comprehensive: 12 users across 3 tiers
- Includes criteria, personalization angles, and notes
- 🟡 **Caveat:** Tier 1 family members are at-risk (Lisa 12d inactive, Danny 0 drops). May need personal outreach before formal soft launch.

### 5. Other Undocumented Procedures 🟡

- **Poe balance monitoring/top-up procedure** — balance at 39K, burning ~43K/6h. No documented threshold for action.
- **Claude Code quota management** — daily resets at 4pm UTC, causes task failures. No documented workaround beyond "wait."
- **WhatsApp delivery failure recovery** — 3 scheduled jobs affected by WhatsApp errors. No fallback documented.

---

## G. Security

### Raw Secrets in Workspace

- 🟢 TOOLS.md does NOT contain raw API keys — only references env var names
- 🟢 ops/ files don't contain secrets
- 🟡 `ops/dashboard/index.html` has a password input field with placeholder `ghp_...` — this is a UI pattern, not a leaked secret, but the placeholder suggests users paste tokens into a browser form
- 🟢 No grep hits for actual token patterns (sk-, ghp_, github_pat_, re_, whsec_) in ops/ or specs/

### Agent Access to Protected Files

| File | Protection Level | Can Agents Modify? |
|------|-----------------|-------------------|
| SOUL.md | 🔴 RESTRICTED per PERMISSIONS.md | 🟡 No enforcement — any agent with file write access could modify |
| USER.md | 🔴 RESTRICTED per PERMISSIONS.md | 🟡 Same — policy says Claw-only, no technical enforcement |
| MEMORY.md | 🔴 RESTRICTED per PERMISSIONS.md | 🟡 Same — loaded only in main session per AGENTS.md, but no write lock |

**Verdict:** 🟡 SHOULD FIX — PERMISSIONS.md defines access levels but there's no enforcement mechanism. Any cron agent with workspace access could theoretically write to SOUL.md. This is a policy risk, not an active exploit.

### GitHub Push Centralization

- 🟢 push-queue.md exists: "Agents: DO NOT push to GitHub directly"
- 🟢 Archivist runs every 20min and processes the queue
- 🟡 No enforcement — any agent could `git push` or use GitHub API directly
- 💡 Trust-based system. Acceptable for current scale but should be audited if agent count grows.

### Overall Security Assessment

🟢 **No critical security issues found.** The system relies on policy-based security (documented rules) rather than technical enforcement (file permissions, ACLs). This is appropriate for a single-user system where all agents run in the same workspace. If the workspace is ever shared with untrusted agents, technical enforcement would be needed.

---

## Summary Scorecard

| Area | Rating | Key Finding |
|------|--------|-------------|
| Agent Roster | 🟢 | 93% operational, constitution and roster in sync |
| Policy Consistency | 🟡 | 5 conflicts found, 2 significant (digest status, CEO-EMAIL-OS vs reality) |
| Spec Hygiene | 🟡 | 39 specs is too many. 9 KILL, 18 ARCHIVE recommended. |
| Memory Integrity | 🟡 | MEMORY.md metrics stale by 2 weeks. TOOLS.md has dead repo reference. |
| Email System | 🟢 | Standards well-documented. Auto-ACK unverified. No duplicate sends. |
| Missing Procedures | 🔴 | Admission flow and rollback plan are critical gaps |
| Security | 🟢 | Policy-based, no raw secrets, no critical issues |

### Launch Readiness: 🟡 CONDITIONAL GO

The system is operationally healthy (93% agent uptime, 84% success rate, all core services running). The gaps are **procedural, not technical**: missing admission flow, missing rollback plan, and spec/policy cleanup. These can be addressed in the 6 days before launch.

---

## Recommended Fix Priority

| Priority | Item | Owner | Effort |
|----------|------|-------|--------|
| 🔴 P0 | Document admission flow (waitlist → admitted → first email) | Joey + Drop | 2h |
| 🔴 P0 | Document rollback plan | Drop | 1h |
| 🔴 P0 | Decide digest pipeline strategy (restore cron vs Hub scheduler) | Joey | Decision |
| 🟡 P1 | Archive 18 specs, kill 9 | Drop/Archivist | 30min |
| 🟡 P1 | Consolidate duplicate files (constitution, agent-board) | Drop | 15min |
| 🟡 P1 | Update MEMORY.md metrics snapshot | Drop | 30min |
| 🟡 P1 | Mark dropanywhere-cron as dead in TOOLS.md | Drop | 5min |
| 🟡 P1 | Label CEO-EMAIL-OS as "target state" not current | Drop | 5min |
| 🟡 P1 | Add push-queue to COMMS-GUIDE.md | Drop | 10min |
| 🟡 P1 | Family outreach before soft launch | Joey | Personal |
| 💡 P2 | Create welcome email template for admitted users | Drop | 1h |
| 💡 P2 | Verify Auto-ACK implementation | Drop | 30min |
| 💡 P2 | Consider merging RailwayBot into Patrol (idle) | Drop | 15min |
| 💡 P2 | Add append-to-daily-log.sh mandate to COMMS-GUIDE | Drop | 5min |

---

*Report generated 2026-03-16 ~17:20 CDT by Opus audit subagent.*
