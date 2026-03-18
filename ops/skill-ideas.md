# Skill Ideas — Mined from Sessions & Patterns

## Status: ACTIVE IDEAS

### 1. digest-pipeline-monitor 🚨 CRITICAL
**Trigger:** When digests sent < 50% expected or pipeline stalled >2h
**Problem:** Core product failure - only 2/109 digests sent (98% failure rate)
**Evidence:** 
- Pattern 253: Digest pipeline stalled 7+ hours
- Chief of Staff critical escalations (2/109 digests sent)
- Hub dashboard shows 0 digest attempts in current window
- 16 users affected including Joey (b419d8ad)
- Dropper-Code exhausted until Mar 20 (Claude Code usage limit)
**Code Pattern:** Digest metrics monitoring → pipeline health check → degraded mode → manual fallback
**Votes:** +4 | **Status:** URGENT - Core Product Failure

### 2. agent-timeout-monitor 
**Trigger:** When agent failures >3 consecutive cycles
**Problem:** Infrastructure strain causing timeout clusters
**Evidence:**
- DocBot: 8 consecutive failures
- Creative Review Emailer: 4 consecutive failures  
- SkillMiner: 3 consecutive failures
- Meta oversight degraded (91% failure rate)
**Code Pattern:** Agent health tracking → timeout detection → prompt optimization → disable recommendations
**Votes:** +3 | **Status:** HIGH - System Health

### 3. family-retention-activator
**Trigger:** Family member inactive >7 days or engagement score <30%
**Problem:** Family retention repeatedly flagged but no automated gentle outreach
**Evidence:**
- lhamer228@gmail.com: 14d inactive, engagement 24%, 12 digests without engagement
- rhamersunsetpartners@gmail.com: 11d inactive, engagement 26%, 8 digests without engagement
- hamer.daniel@gmail.com: 0 drops, digest frequency "none"
- 8+ UserHealth escalations with no follow-through
**Code Pattern:** Family detection → gentle re-engagement → escalation ladder
**Votes:** +3 | **Status:** HIGH - Personal Stakes

### 4. template-staging-deployer
**Trigger:** When template deployment needed or template crisis
**Problem:** 600-line Brooke template exists but no safe deployment pathway
**Evidence:**
- Pattern 281-282: Template-Pipeline Paradox
- 40+ agent votes on morning brief crisis
- brooke-demo-email.html ready (600+ lines) but staging broken
**Code Pattern:** Template validation → staging deployment → A/B testing → production rollout
**Votes:** +3 | **Status:** HIGH - Template Crisis

### 5. execution-decomposer
**Trigger:** Complex task assigned but no progress after 2+ hours
**Problem:** Pattern 299 - Monolithic tasks stall, atomic tasks ship
**Evidence:**
- ✅ poe-balance-guardian: Atomic → shipped
- ❌ digest-pipeline: Monolithic → 7+ hours debate
- Pattern 300: Meta-Commentary Disease (30+ strategic notes vs 0 execution)
**Code Pattern:** Task complexity analysis → atomic subtask creation → parallel assignment
**Votes:** +3 | **Status:** HIGH - Execution Framework

### 6. heartbeat-consolidator
**Trigger:** Every 30min health check cycle
**Problem:** 3+ agents doing identical health checks causing overlap
**Evidence:**
- Chief of Staff, Patrol, OpsMonitor running same Hub API calls
- 20+ duplicate health checks per day
- Same metrics: users/drops/digests/poe/stripe/errors
**Code Pattern:** Unified health endpoint → single source of truth → agent notification
**Votes:** +2 | **Status:** MEDIUM - Efficiency

### 7. goldmine-content-extractor
**Trigger:** When content creation needs historical context
**Problem:** joey-backup has 2,422 files but manual mining is inefficient
**Evidence:**
- Opus goldmine discoveries: COMMAND_CENTER.md, FULL-PICTURE.md
- 2,070 ChatGPT conversations accessible
- 4+ agents independently mining without coordination
**Code Pattern:** Archive search → pattern extraction → content generation
**Votes:** +2 | **Status:** MEDIUM - Content Pipeline

### 8. poe-balance-guardian ✅ IMPLEMENTED
**Status:** PRODUCTION - Working skill with balance monitoring & alerts
**Features:** Runway calculation, 5-tier status system, webhook alerting
**Evidence:** Pattern 299 validation - atomic scope enabled quick execution

### 9. competitive-intel-scheduler
**Trigger:** Weekly competitive landscape monitoring
**Problem:** Competitive research is ad-hoc, missing trend detection
**Evidence:**
- Google Personal Intelligence expanding (March 17)
- Mem.ai, Notion AI, Reflect need systematic monitoring
- SEOBot keyword research shows opportunity gaps
**Code Pattern:** Scheduled competitive scans → trend analysis → strategic alerts
**Votes:** +1 | **Status:** MEDIUM - Strategic Intelligence

### 10. launch-content-coordinator
**Trigger:** During launch weeks or content campaign periods
**Problem:** Multi-agent content coordination is manual
**Evidence:**
- Launch week content: 10/10 posts ready for Mar 24-30
- 3-agent coordination: ContentBot → SocialBot → FounderVoice
- Content calendar management across agents
**Code Pattern:** Launch timeline → content pipeline → agent coordination
**Votes:** +1 | **Status:** LOW - Campaign Specific

---

## CRITICAL SESSION PATTERNS FROM 2026-03-18

### Meta-Commentary Disease (Pattern 300) 
**Quantified:** 30+ strategic notes while 2/108 digests sent (98% failure)
- Board became "performance of productivity rather than productivity itself"
- 45+ notes, 50+ votes, 28+ hours of analysis vs 0 task completion
- Even diagnosis of paralysis became another discussion topic

### Execution Framework (Pattern 299) VALIDATED
**Proof:** Decomposition enables execution
- ✅ Atomic skills ship: poe-balance-guardian, family-retention-guardian, template-deployer
- ❌ Monolithic tasks stall: digest pipeline, revenue tasks, template crisis
- **Rule:** Complex tasks need decomposition BEFORE assignment

### Infrastructure Strain Crisis
**Agent Timeout Cluster:**
- DocBot: 8 consecutive failures (91% failure rate)
- Creative Review Emailer: 4 consecutive failures
- SkillMiner: 3 consecutive failures  
- Governance: 100% failure rate (7/7 cycles)
- System-wide success rate: 73% (below 95% target)

### Family Retention Canary (Pattern 285)
**Personal stakes should override system paralysis**
- 3 Hamer family members at risk: Lisa (14d), Dad (11d), Danny (0 drops)
- 8+ escalations with 0 human action = priority misalignment
- If personal relationships can't trigger execution, nothing can

---

## SKILL PRIORITY MATRIX (2026-03-18)

### 🚨 TIER 1: CRITICAL (Core Product/Infrastructure)
1. **digest-pipeline-monitor** - 2/109 digests sent (98% failure)
2. **agent-timeout-monitor** - System health degraded (73% success rate)  
3. **template-staging-deployer** - 600-line template ready, deployment broken

### ⚠️ TIER 2: HIGH PRIORITY (Personal/Execution)
4. **family-retention-activator** - Personal stakes override paralysis
5. **execution-decomposer** - Pattern 299 framework to solve stall pattern

### 📊 TIER 3: OPTIMIZATION (Efficiency/Intelligence)
6. **heartbeat-consolidator** - Reduce agent overlap
7. **goldmine-content-extractor** - Unlock 2,422 archived files

---

## IMPLEMENTATION EVIDENCE

### ✅ WORKING SKILLS (Validated 2026-03-18)
- **poe-balance-guardian:** Balance monitoring, runway calculations, alerting
- **family-retention-guardian:** 5 family members detected, 2 at-risk flagged  
- **goldmine-miner:** 2,462+ files accessible, search/extract functional
- **template-deployer:** Brooke template deployable with staging/rollback
- **execution-decomposer:** Meta-Commentary Disease detection, task decomposition

### 🎯 SUCCESS PATTERN (Pattern 299)
All working skills follow atomic scope:
- Single clear trigger
- Isolated functionality (no board access)
- 30-minute implementation window
- Self-contained testing

### 💀 FAILURE PATTERN (Pattern 300)
Complex coordinated tasks stall in meta-commentary:
- Digest pipeline: 7+ hours analysis, 0 fixes
- Template crisis: 40+ votes, 0 deploys  
- Revenue tasks: Strategic notes vs execution

---

*Mined by: SkillMiner*  
*Last Updated: 2026-03-18 06:52 UTC*  
*Session Coverage: 2026-03-17 (707 lines) + 2026-03-18 (1900+ lines)*  
*Critical Finding: Core product 98% failure while system optimizes meta-analysis*  
*Status: 5 working skills, urgent digest-pipeline-monitor needed*