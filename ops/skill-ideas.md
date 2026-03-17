# Skill Ideas — Mined from Sessions & Patterns

## Status: ACTIVE IDEAS

### 1. agent-orchestrator
**Trigger:** When user says "run the agents" or "start the agency cycle"
**Problem:** Joey manually triggers agent cycles; this could be automated
**Evidence:** 
- Daily agent cycles run at specific times (16:00 UTC, 18:00 UTC, 20:00 UTC)
- 25+ agents performing coordinated tasks
- Pattern of Meta scorecard reporting
**Code Pattern:** Cron-like scheduling with agent dispatch
**Votes:** 0 | **Status:** Draft

---

### 2. pattern-weaver
**Trigger:** When multiple agents report similar findings
**Problem:** Cross-agent pattern recognition is manual
**Evidence:**
- PatternBot catalogs patterns (Pattern 251-150 observed)
- Pattern 251: Visual design crisis = User churn trigger
- Pattern 252: Template crisis reveals design system gap
- Pattern 253: Digest pipeline regression persists
**Code Pattern:** Pattern extraction from agent logs
**Votes:** 0 | **Status:** Draft

---

### 3. heartbeat-monitor
**Trigger:** Every 30min or when system health degrades
**Problem:** Hub/Dropper-Code health checks are scattered
**Evidence:**
- Chief of Staff runs health checks repeatedly
- Patrol checks: Hub, BHA, Poe, Stripe, Dropper-Code
- Same checks: 100 users, 20 drops/24h, 3 digests, Poe balance
**Code Pattern:** Unified health dashboard aggregation
**Votes:** 0 | **Status:** Draft

---

### 4. goldmine-miner
**Trigger:** When researching Joey's historical content
**Problem:** joey-backup/Ingestion/ has 2,422 files but access is manual
**Evidence:**
- Deep Researcher "GOLDMINE" findings: 2,070 ChatGPT conversations
- Opus mined theProtocol, SYSTEM_ARCHITECTURE.md
- Pattern: "One wisdom file > 25 task agents"
**Code Pattern:** GitHub API content search + indexing
**Votes:** 0 | **Status:** Draft

---

### 5. content-pitcher
**Trigger:** When new drops arrive with content potential
**Problem:** Converting drops to content angles is manual
**Evidence:**
- ContentPitch generates 3 angles per drop
- LinkedIn, Twitter, Blog angles from single drop
- "SURPIPHANY" concept → 3 content pieces
**Code Pattern:** Drop analysis → Content angle generation
**Votes:** 0 | **Status:** Draft

---

### 6. family-retention-guardian
**Trigger:** When family members show engagement drop
**Problem:** Family retention flagged 8+ times but no automated action
**Evidence:**
- lhamer228@gmail.com: 12d inactive, flagged repeatedly
- rhamersunsetpartners@gmail.com: 9d inactive
- UserHealth escalates but no follow-through
**Code Pattern:** At-risk user detection → Re-engagement workflow
**Votes:** 0 | **Status:** Draft

---

### 7. competitive-intel-agent
**Trigger:** Weekly competitive landscape scan
**Problem:** Mem.ai, Notion AI, Reflect research is ad-hoc
**Evidence:**
- Researcher competitive intel on Mem AI 2.0
- SEOBot keyword research
- Wire market trend monitoring
**Code Pattern:** Scheduled competitive analysis + alerting
**Votes:** 0 | **Status:** Draft

---

### 8. decision-router
**Trigger:** When Joey sends email drops with decisions
**Problem:** FeedbackBot routes but execution is scattered
**Evidence:**
- Drop 4-9: 6 drops → 5 queued tasks
- Kill ACK emails, compliance audit, COMPASS resend
- Tasks sit in queue awaiting execution
**Code Pattern:** Drop ingestion → Task creation → Execution tracking
**Votes:** 0 | **Status:** Draft

---

### 9. launch-coordinator
**Trigger:** During product launch periods
**Problem:** Launch week content coordination is manual
**Evidence:**
- 10/10 launch posts drafted for Mar 24-30
- SocialBot, ContentBot, FounderVoice coordination
- Content calendar management
**Code Pattern:** Launch timeline → Content pipeline → Publishing schedule
**Votes:** 0 | **Status:** Draft

---

### 10. poe-balance-guardian
**Trigger:** When Poe balance drops below threshold
**Problem:** Poe burn rate monitoring is reactive
**Evidence:**
- PoeBot checks: 43,544 balance, 43,449 usage/6h
- Pattern: ~6h runway at 40K balance
- Critical threshold: 10K points
**Code Pattern:** Balance monitoring → Burn rate projection → Alerting
**Votes:** 0 | **Status:** Draft

---

## MINED PATTERNS (Session Analysis)

### From 2026-03-17 Session:

**Recurring Tasks:**
1. Agent health checks (Chief of Staff, Patrol, RailwayBot) — 20+ times/day
2. Poe balance monitoring — every 2-4 hours
3. User health / retention checks — 6+ times
4. Content polishing (LinkedIn posts) — 5+ posts
5. Strategic voting (Opus) — 15+ votes
6. Pattern cataloging (PatternBot) — 10+ new patterns
7. Goldmine mining (Deep Researcher) — 4+ discoveries
8. Spec syncing (SpecBot) — 3+ syncs
9. Backup + commit (Archivist) — 10+ commits
10. Meta scorecard reporting — 5+ reports

**Workflow Gaps:**
- Digest stall root cause identified but fix delayed
- Family retention flagged but no automated outreach
- PR queue (5 PRs) ready but unreviewed
- Wire API exhaustion causes research gaps

**Code Patterns to Extract:**
- Hub API client pattern (used by Patrol, Chief of Staff, UserHealth)
- GitHub backup push pattern (Archivist)
- Agent status aggregation (Meta)
- Drop-to-content transformation (ContentPitch)

---

## NEXT STEPS

1. **Vote on ideas** — Need 3+ votes to proceed to skill creation
2. **Mine GitHub** — Extract reusable scripts from joey-backup
3. **Create first skill** — Start with highest-voted idea

---

*Mined by: SkillMiner*
*Date: 2026-03-17 21:40 UTC*
