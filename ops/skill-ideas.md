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

## NEW PATTERNS FROM 2026-03-17 SESSIONS

### Recurring Workflows Observed:

1. **Morning Brief Template Crisis Response** — 25min unanimous consensus (Pattern 251)
   - Visual design feedback → immediate agent mobilization
   - 3 Opus votes on same issue within 1 hour
   - Emergency stop + redesign protocol activated

2. **Agent Scorecard Reporting** — Meta runs 5+ times/day
   - A/B/C grade classification
   - Excellence cluster identification
   - Escalation pattern detection

3. **Digest Pipeline Monitoring** — Chief of Staff + Patrol + Heartbeat
   - 3/41 digests sent = stall detected
   - Root cause: dropanywhere-cron service DOWN (404)
   - Cross-agent validation of same metrics

4. **Goldmine Mining Acceleration** — 4+ agents independently
   - joey-backup/Ingestion/ = 2,422 files
   - theProtocol, SYSTEM_ARCHITECTURE.md discoveries
   - Pattern: "One wisdom file > 25 task agents"

5. **Family Retention Escalation** — UserHealth 8+ times
   - lhamer228@gmail.com: 12d inactive, flagged repeatedly
   - Same 3 family members across 6+ checks
   - No automated follow-through after escalation

### Existing Skills Inventory (56 skills):
- **Infrastructure:** healthcheck, node-connect, skill-creator
- **Content:** poe-cdn-upload, nano-banana-pro, openai-image-gen
- **Communication:** discord, slack, imsg, bluebubbles, himalaya
- **Productivity:** 1password, apple-notes, apple-reminders, bear-notes, notion, obsidian
- **Media:** video-frames, openai-whisper-api, sag, gifgrep
- **Dev:** github, gh-issues, coding-agent, tmux
- **Utility:** weather, canvas, model-usage, oracle

### Skill Gaps Identified:
1. **No unified health monitoring** — Patrol + Chief of Staff + RailwayBot overlap
2. **No pattern aggregation skill** — PatternBot catalogs but doesn't weave
3. **No retention automation** — UserHealth escalates but doesn't act
4. **No competitive monitoring** — Researcher runs ad-hoc, not scheduled
5. **No content pipeline skill** — ContentPitch + SocialBot + FounderVoice coordination manual

## PRIORITIZED SKILL IDEAS (Post-Session Analysis)

### Tier 1: High Impact, Clear Trigger
| Skill | Votes | Trigger | Evidence |
|-------|-------|---------|----------|
| poe-balance-guardian | +1 | Balance < 20K | 43K burn/6h, ~6h runway pattern |
| family-retention-guardian | +1 | Family inactive >7d | 8+ escalations, no action |
| heartbeat-consolidator | +1 | Every 30min | 3 agents doing same checks |

### Tier 2: Medium Impact, Needs Refinement
| Skill | Votes | Trigger | Evidence |
|-------|-------|---------|----------|
| pattern-weaver | 0 | 3+ agents report similar | Pattern 251-150 cataloged |
| goldmine-miner | 0 | Research request | 2,422 files, 4+ discoveries |
| content-pipeline | 0 | Launch week active | 10/10 posts, 3-gate system |

### Tier 3: Conceptual, Needs Joey Input
| Skill | Votes | Trigger | Evidence |
|-------|-------|---------|----------|
| agent-orchestrator | 0 | "Run the agents" | 25 agents, manual dispatch |
| decision-router | 0 | Email drops arrive | 6 drops → 5 tasks queued |
| launch-coordinator | 0 | Launch week | Mar 24-30 coordination |

## IMPLEMENTATION STATUS

### ✅ COMPLETED: poe-balance-guardian (2026-03-17)
- **Location:** `skills/poe-balance-guardian/`
- **Files:**
  - `SKILL.md` — Full documentation with thresholds, burn rate patterns
  - `scripts/check_balance.py` — Balance checking with runway calculation
  - `scripts/test_balance.py` — Test suite (all passing)
- **Features:**
  - Current balance + 6h usage fetch
  - Burn rate calculation (~7,241 pts/hour observed)
  - Runway estimation in hours/days
  - 5-tier status system (healthy→emergency)
  - JSON output for automation
  - Webhook alerting support
- **Triggers:** Balance < 50K (caution), < 20K (warning), < 10K (critical)
- **Votes:** 1 (SkillMiner) — IMPLEMENTED

---

## SKILL GAPS ANALYSIS (Post-Implementation)

### Existing Skills: 57 total
- Infrastructure: healthcheck, node-connect, skill-creator, **poe-balance-guardian** (NEW)
- Content: poe-cdn-upload, nano-banana-pro, openai-image-gen
- Communication: discord, slack, imsg, bluebubbles, himalaya
- Productivity: 1password, apple-notes, apple-reminders, bear-notes, notion, obsidian
- Media: video-frames, openai-whisper-api, sag, gifgrep
- Dev: github, gh-issues, coding-agent, tmux
- Utility: weather, canvas, model-usage, oracle

### Remaining Gaps:
1. **Unified health monitoring** — Patrol + Chief of Staff + RailwayBot overlap
2. **Pattern aggregation** — PatternBot catalogs but doesn't weave across agents
3. **Retention automation** — UserHealth escalates but doesn't auto-act
4. **Competitive monitoring** — Researcher runs ad-hoc, not scheduled
5. **Content pipeline** — ContentPitch + SocialBot + FounderVoice coordination manual

---

## NEXT STEPS

1. **Vote on remaining Tier 1 ideas** — family-retention-guardian, heartbeat-consolidator
2. **Refresh GitHub token** — Mine joey-backup/Ingestion/ for automation patterns (token expired)
3. **Create family-retention-guardian** — 8+ escalations, clear trigger, high impact
4. **Document reusable patterns** — Hub API client, GitHub backup push, agent status aggregation

---

*Mined by: SkillMiner*
*Last Updated: 2026-03-18 00:02 UTC*
*Session Coverage: 2026-03-17 (full day) + 2026-03-18 (SkillMiner cron)*
