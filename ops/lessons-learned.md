# Lessons Learned Log

Operational lessons, failures, and improvements captured by LearningBot.

---

### 22:50 UTC — LearningBot (2026-03-17)

**LESSON: GitHub Token as Recurring Single Point of Failure**
- **What happened:** SpecBot and SkillMiner both failed GitHub API authentication (bad credentials) during the same 30-min window
- **Why:** `GITHUB_TOKEN` expired (confirmed in TOOLS.md as "EXPIRED, bad credentials"), forcing agents to pivot to degraded workflows
- **Impact:** 2 agent workflows blocked, specs couldn't sync from joey-backup, GitHub mining skipped
- **How to prevent:** 
  - Refresh GH_TOKEN before expiration (TOOLS.md shows working PAT is `GH_TOKEN`, not `GITHUB_TOKEN`)
  - Add token health check to Sentry's secret scan routine
  - Document token refresh date in TOOLS.md with 90-day reminder
- **Replicate when:** Any GitHub-dependent skill needs to verify token health first

**LESSON: Digest Pipeline Regression = Launch Risk**
- **What happened:** Only 2/108 users received digests in 24h — a 98% failure rate persisting 6+ hours
- **Why:** Dropper-Code stalled due to Claude usage exhaustion (resets Mar 20), blocking digest generation
- **Impact:** Core value proposition compromised during launch week; family members at risk flagged repeatedly
- **How to prevent:**
  - Implement LLM fallback when Claude quota exhausted (Gemini, GPT-4o via OpenRouter)
  - Add digest pipeline monitoring with 2h failure threshold alert
  - Pre-generate digest templates before quota windows
- **Pattern reference:** Pattern 234 (persistent), Pattern 253 (6hr+), Pattern 260 (launch readiness paradox)

**LESSON: Visual Crisis Response Speed > Infrastructure Crisis Response**
- **What happened:** Morning Brief template crisis ("not good looking" feedback) achieved 25-minute unanimous consensus across agents
- **Why:** User-facing visual issues trigger faster response than backend failures
- **Impact:** Strategic sequencing agreed (fix pipeline → redesign → resume) but not yet implemented
- **How to replicate:** 
  - Frame infrastructure issues as "user-facing" to accelerate response
  - Use visual mockups/prototypes for technical issues (makes them concrete)
- **Pattern reference:** Pattern 251, Meta-Pattern: Crisis type determines response speed

**LESSON: Content Pipeline Velocity Success vs Digest Pipeline Failure**
- **What happened:** 7 LinkedIn posts created, polished, and delivered in 1 hour while digest pipeline remained stalled for 6+ hours
- **Why:** Content pipeline has clear owner (ContentBot), review process (FounderVoice), and no external dependencies; digests depend on Dropper-Code + Claude quota
- **Impact:** Launch week content ready, but core product value (daily digests) unavailable
- **How to replicate:**
  - Remove external dependencies from critical paths
  - Give digest pipeline same ownership clarity as content pipeline
- **Pattern reference:** Pattern 258

**LESSON: Agent Grade Inflation Without Execution**
- **What happened:** Meta scorecard improved from 75% → 83% → 92% value production while 4 critical operational gaps persisted
- **Why:** Grading based on activity volume, not outcome delivery; "A" grades for research/patterns even when core systems broken
- **Impact:** False confidence in system health; Launch Coordinator showed GREEN while digest pipeline RED
- **How to prevent:**
  - Weight grades by customer impact (digest failure = auto C regardless of other activity)
  - Require "fixed" confirmation before upgrading failed system grades
- **Pattern reference:** Pattern 259, Pattern 260 (launch readiness paradox)

**LESSON: Family Retention Risk as System Health Canary**
- **What happened:** 3 family members flagged as at-risk (lhamer228, rhamersunsetpartners, hamer.daniel) — zero drops, empty vaults, 10-13 days inactive
- **Why:** If personal stakes don't trigger execution, nothing will; indicates systemic engagement failure
- **Impact:** Emotional + business cost; family should be easiest cohort to retain
- **How to prevent:**
  - Family members get priority digest queue (guaranteed delivery even during outages)
  - Personal onboarding call for family vault emptiness
  - Auto-escalate family inactivity to Claw immediate notification
- **Pattern reference:** Pattern 264

**LESSON: Poe Balance as Hidden Launch Risk**
- **What happened:** Poe balance burned 37K→46K→64K→remaining (erratic reporting), ~12h runway at peak burn
- **Why:** BHA depends on Poe for organic traffic; Kimi-K2.5 model burning 22K/6h
- **Impact:** If Poe depleted, BHA loses primary acquisition channel during launch week
- **How to prevent:**
  - Poe balance check in Unified Ops Monitor with 48h runway alert
  - Implement PoeBalanceGuardian skill (SPEC created 22:19 UTC)
  - Auto-switch to lower-cost models when balance < 100K
- **Pattern reference:** Pattern 254 (Claude quota SPOF applies to Poe too)

**LESSON: Skill Mining Works — Implementation Doesn't**
- **What happened:** SkillMiner identified 10 skill ideas, 5 gaps, Tier 1 priority for PoeBalanceGuardian — but no implementation triggered
- **Why:** Mining is automated, implementation requires manual decision/approval
- **Impact:** Knowledge without action; same patterns identified repeatedly (PatternBot, LearningBot both captured same insights)
- **How to replicate:**
  - Auto-create GitHub issues for Tier 1 skill gaps
  - Add "implement highest priority skill" as mandatory agent action
- **Pattern reference:** Pattern 262 (strategic consensus without implementation)
