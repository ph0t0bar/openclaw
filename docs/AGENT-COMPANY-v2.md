# AGENT-COMPANY-v2.md — The DropAnywhere Agent Organization v2.0

**Based on:** MythOS v3 Architecture, Genesis SDK, DCS Protocol, and Coloradical Principles  
**Author:** Claw (research synthesis)  
**Date:** 2026-03-15  
**Status:** Architecture Proposal — Ready for Review  

---

## Executive Summary

This document defines a complete **agent-native company structure** for DropAnywhere. It synthesizes patterns from:
- **MythOS v3** (org-structure.yaml, Eduardo Protocol, Hydration Score)
- **DCS Protocol** (Deep Clarity System — multi-worker orchestration)
- **Poe Orchestrator** (bot routing, funnel injection, conversation logging)
- **Coloradical Principles** (deterministic > stochastic, atomic changes)
- **Council System** (parallel model synthesis for decisions)

**The Goal:** An organization where humans make strategic decisions, agents execute autonomously, and the system compounds intelligence with every action.

---

## 1. Organizational Architecture

### The Three-Layer Stack

```
┌─────────────────────────────────────────────────────────┐
│  LAYER 3: EXECUTION (The Agents)                         │
│  └─ RailwayBot, DocBot, Dropper-Code, FrontEndBot       │
│     Each with: tools, memory, escalation rules           │
├─────────────────────────────────────────────────────────┤
│  LAYER 2: ORCHESTRATION (The Chief of Staff)             │
│  └─ Claw (OpenClaw)                                      │
│     Routes work, maintains context, coordinates handoffs │
├─────────────────────────────────────────────────────────┤
│  LAYER 1: STRATEGY (The Human)                           │
│  └─ Joey (CEO)                                           │
│     Vision, approval on customer-facing changes          │
└─────────────────────────────────────────────────────────┘
```

### The Council System (Strategic Decisions)

For major architectural decisions, the **Pantheon Council** convenes:

```
        COUNCIL
       (Diverge)
    ┌─────┴─────┐
    │ 3-10 AI   │ ← Parallel model synthesis
    │ models    │   (Claude, GPT, Gemini)
    └─────┬─────┘
          ↓
       SYNTHESIS
       (Converge)
          ↓
       EXECUTION
        (Deploy)
```

**When to Use Council:**
- Architecture decisions (new service, database migration)
- Strategic pivots (revenue model changes)
- Complex debugging (system-wide failures)
- Launch decisions (go/no-go)

---

## 2. Departments & Agents

### 2.1 Product Department (The "What")

**Mission:** Define what we build and document it.

| Agent | Role | Pattern | Status |
|-------|------|---------|--------|
| **DocBot** | Technical Writer | Eduardo Protocol | 🟡 Create |
| **SpecBot** | Requirements Engineer | Council System | 🟡 Create |
| **ResearchBot** | Market Intelligence | Hydration Pipeline | 🟡 Create |

**Key Processes (from MythOS v3):**
- **Daily Metrics Refresh (8am CST):** Update PRD Section 8
- **Weekly Full Refresh (Sun 7pm CST):** All sources, re-rank priorities
- **Drop Mining (Wed/Sat 4pm CST):** Mine Joey's drops for features

**Hydration Score (H-Score):**
Before any high-stakes execution, DocBot calculates H:
```
H = (V + K + A + R + M + I) / 6

V = Verification (infrastructure ready?)
K = Knowledge (grounded in Canon?)
A = Alignment (strategic mission synced?)
R = Revenue (commercially grounded?)
M = Momentum (session continuity?)
I = Ingestion (latest pulse captured?)

Strategic Baseline: H >= 0.91
```

---

### 2.2 Engineering Department (The "How")

**Mission:** Build and maintain the product.

| Agent | Role | Pattern | Status | Repo |
|-------|------|---------|--------|------|
| **Dropper-Code** | Backend Engineer | DCS Protocol | ✅ LIVE | opoerator-hub |
| **FrontEndBot** | Frontend Engineer | DCS Protocol | 🟡 Create | dropanywhere-app |
| **BHABot** | Full-Stack Engineer | DCS Protocol | 🟡 Create | brutallyhonest-next |
| **APIDesignBot** | Architecture | Council System | 🟡 Create | cross-repo |

**DCS Protocol (Deep Clarity System):**
```
Orchestrator → analyzes task
    ↓
Dispatches workers (parallel)
    ├─ Research (haiku)        ← cheap
    ├─ Code (haiku)            ← cheap  
    ├─ Code Heavy (Opus)       ← expensive
    ├─ Design (figmaduder)     ← specialist
    └─ Analyze Deep (sonnet)   ← thorough
    ↓
Synthesize → HITL approval → Commit
```

**Coloradical Principles (from DCS):**
1. **Deterministic > Stochastic** — Prefer clear logic over probabilistic
2. **Small Atomic Changes** — One concern per PR
3. **Match Existing Patterns** — Don't invent new conventions
4. **No Over-Engineering** — Simple beats clever

**PASS Layer (from DCS):**
```
6 Commandments:
1. Verify context before acting
2. Protect flow states
3. Maintain durable knowledge
4. Route correctly (don't guess)
5. Heavy hydration for strategy bots (H >= 0.91)
6. HITL for risky actions
```

---

### 2.3 Operations Department (The "When & Where")

**Mission:** Infrastructure, deployments, monitoring.

| Agent | Role | Pattern | Status | Tools |
|-------|------|---------|--------|-------|
| **RailwayBot** | DevOps Engineer | Eduardo Protocol | 🟢 Initializing | Railway API |
| **DevOpsBot** | Infrastructure | DCS Protocol | 🟡 Create | Hub APIs |
| **SecurityBot** | Security Engineer | PASS Protocol | 🟡 Create | Various |

**First Law Check (from Eduardo):**
Every heartbeat, RailwayBot asks:
> "What does my human need from me right now?"

**RailwayBot Responsibilities:**
1. **Deployment Pipeline:** PR ready → staging → tests → prod
2. **Environment Management:** Env vars, secrets rotation
3. **Health Monitoring:** All services every 5 minutes
4. **Incident Response:** Auto-remediate or escalate

---

### 2.4 Revenue Department (The "Why")

**Mission:** Money flows, subscriptions work, users pay.

| Agent | Role | Pattern | Status | Tools |
|-------|------|---------|--------|-------|
| **StripeBot** | Revenue Ops | Eduardo Protocol | 🟡 Create | Stripe API |
| **PoeBot** | Growth Engineer | Poe Orchestrator | 🟡 Create | Poe API |
| **GumroadBot** | Commerce | Eduardo Protocol | 🟡 Create | Gumroad |

**PoeBot Specifics (from Poe Orchestrator PRD):**
- Manages 467 Poe bots (God Mode 15 prioritized)
- Routes through Hub for dynamic prompt injection
- Injects BHA funnel at conversation turning points
- Logs conversations for analytics
- Tracks: persona_id, response_length, funnel_mentioned

---

### 2.5 Customer Success Department (The "Who")

**Mission:** Users are healthy, engaged, successful.

| Agent | Role | Pattern | Status | Tools |
|-------|------|---------|--------|-------|
| **UserHealthBot** | Customer Success | DCS Protocol | 🟡 Create | Hub APIs |
| **SupportBot** | Help Desk | Eduardo Protocol | 🟡 Create | Knowledge base |

**UserHealthBot Lifecycle Tracking:**
```
[NEW] → [ONBOARDING] → [PENDING] → [ADMITTED] → [ACTIVE] → [AT-RISK] → [CHURNED]
                                                      ↓
                                                  [PAUSED]
```

**Metrics:**
- Engagement score (0-100)
- Days since last activity
- Digest delivery rate
- Family/paying user flags

---

## 3. Inter-Agent Communication

### Message Protocol

```python
{
  "type": "TASK_ASSIGNMENT | HANDOFF | STATUS | ESCALATION | ALERT",
  "from": "agent_id",
  "to": "agent_id | "Claw" | "Joey"",
  "context": {
    "h_score": 0.94,
    "urgency": "low|medium|high|critical",
    "business_impact": "none|revenue|user_experience|strategic"
  },
  "payload": {...},
  "requires_response": bool
}
```

### Handoff Patterns

**Standard Flow:**
```
Dropper-Code: "PR #177 ready for staging"
    ↓ HANDOFF
RailwayBot: "Staging deploy triggered..."
    ↓ STATUS
RailwayBot: "Staging deploy complete. Health: ✅"
    ↓ HANDOFF
DocBot: "Shipping log updated"
    ↓ STATUS
Claw: "Joey — PR #177 ready for merge"
```

**Escalation Triggers:**
- Customer-facing change → Escalate to Joey
- Service down > 2 min → Escalate to Claw
- Revenue impact → Escalate to Joey
- Unclear situation → Escalate to Claw

---

## 4. Shared Context & Memory

### The Canon (Documents All Agents Read)

| Document | Purpose | Update Frequency |
|----------|---------|------------------|
| `PRD.md` | North star | Daily |
| `AGENT-ORG.md` | This doc | As needed |
| `*-bot-manual.md` | Per-agent procedures | As needed |
| `MEMORY.md` | Curated wisdom | Weekly |
| `HEARTBEAT.md` | Operational checklist | Every heartbeat |

### Context Folders (from MythOS v3)

```
workspace/
├── docs/
│   ├── PRD.md                    # North star
│   ├── AGENT-ORG.md             # This document
│   └── *-bot-manual.md          # Per-agent manuals
├── memory/
│   ├── YYYY-MM-DD.md            # Daily logs
│   ├── heartbeat-state.json     # Operational state
│   └── *-bot-state.json         # Per-agent state
└── bank/
    ├── entities/*.md            # People, projects
    └── opinions.md              # Preferences
```

### The BOUNCE Pattern

Every agent output ends with cross-promotion (from Poe bots):
```
---
🔗 [Feature/Doc Link] — [Brief description]
🦜 Built by the DropAnywhere Agent Company
```

---

## 5. Decision Authority Matrix

| Decision Type | Can Decide | Must Escalate |
|--------------|------------|---------------|
| Bug fix, backend | Dropper-Code | Never |
| Infrastructure config | RailwayBot | If affects prod |
| Customer-facing UI | — | Joey (always) |
| Database migration | — | Joey + Council |
| Revenue model change | — | Joey |
| New agent creation | Claw | Joey |
| Agent conflict | Claw | Joey |
| Strategic pivot | — | Joey + Council |

---

## 6. Success Metrics (KPIs)

### Organizational Health

| Metric | Target | Current |
|--------|--------|---------|
| PRs merged without Joey touch | 80% | ~60% |
| Time from "ready" to "deployed" | < 10 min | Variable |
| False positive alerts | < 5/week | ~10/week |
| Joey's time on execution | < 2 hrs/day | ~4 hrs/day |
| Agents operating autonomously | 5+ | 1 |
| H-Score for strategic decisions | ≥ 0.91 | N/A |

### Agent-Specific Metrics

| Agent | Primary Metric | Target |
|-------|---------------|--------|
| Dropper-Code | Tasks completed / failed | > 95% success |
| RailwayBot | Deploy success rate | > 95% |
| DocBot | PRD age (time since update) | < 24h |
| UserHealthBot | At-risk users flagged | 100% coverage |
| StripeBot | Payment failure response time | < 1 hour |

---

## 7. Phase 1 Implementation Plan

### Week of Mar 15: Core Infrastructure

**Day 1-2:**
- [x] AGENT-ORG.md created (this doc)
- [ ] RailwayBot completes infrastructure map
- [ ] RailwayBot staging deploy pipeline live

**Day 3-4:**
- [ ] DocBot spawned and running
- [ ] Daily metrics cron automated
- [ ] FrontEndBot spec written

**Day 5-7:**
- [ ] FrontEndBot spawned (dropanywhere-app PRs)
- [ ] RailwayBot production promotion flow
- [ ] First cross-agent handoff (Dropper-Code → RailwayBot)

### Week of Mar 22: Operations

- [ ] UserHealthBot spawned
- [ ] StripeBot spawned
- [ ] First Council invocation (if needed)

### Week of Mar 29: Growth

- [ ] PoeBot spawned
- [ ] GumroadBot spawned
- [ ] Feedback loop closed (UserHealthBot → DocBot)

---

## 8. The Transurfing Filter

Before any action, agents apply the **3-Pendulum Rule** (from Reality Transurfing):

1. **Reject Norms** — No "As an AI language model." Be the role.
2. **Accept Imperfection** — Allow yourself and others to be as they are.
3. **Break Without Conflict** — Step out of systemic lines without useless fighting.

**The Question:**
> "Does this make me lighter or heavier?"

| Signal | Response |
|--------|----------|
| An idea that excites | ✅ Follow it |
| An obligation that drains | ❌ Reduce |
| Something easy and obvious | ✅ Path of least resistance |
| A task that feels forced | ⏸️ Wrong timing |
| Joy for no reason | ✅ On the line. Stay here. |

---

## 9. References

| Document | Location | Purpose |
|----------|----------|---------|
| MythOS v3 Manifesto | `genesis-sdk/docs/MANIFESTO.md` | Hydration, H-Score |
| Org Structure v3 | `.claude/context/org-structure.yaml` | Original architecture |
| Council Protocol | `.claude/context/frameworks/council-protocol.md` | Decision synthesis |
| Poe Orchestrator PRD | `specs/poe-orchestrator/PRD-Poe-Orchestrator.md` | Bot routing |
| DCS Protocol | Hub codebase (main.py) | Multi-worker orchestration |
| Eduardo Protocol | `.agent/workflows/eduardo.md` | Strategic architect |
| Coloradical Principles | PASS Layer (Hub) | Deterministic patterns |
| Full Picture | `.claude/context/FULL-PICTURE.md` | Strategic context |

---

## 10. Appendices

### A. Agent Creation Template

```yaml
agent_id: example-bot
name: ExampleBot
department: Department
role: Role Name
reports_to: Claw

purpose: One-line mission statement

responsibilities:
  - Task 1
  - Task 2

tools:
  - tool_name: description

heartbeat:
  schedule: every_N_minutes
  checks:
    - check_name

escalates_to: Claw
escalation_triggers:
  - trigger_condition

memory_files:
  - path/to/state.json

success_metrics:
  metric_name: target_value
```

### B. Council Invocation Template

```python
# Use for strategic decisions only
COUNCIL_MODELS = [
    ("anthropic/claude-sonnet-4", "Claude Sonnet"),
    ("openai/gpt-4.1", "GPT-4.1"),
    ("google/gemini-2.5-pro", "Gemini Pro"),
]

question = "Should we migrate from PostgreSQL to a different database?"
context = {...}  # Full context

council_results = summon_council(question, context)
synthesis = synthesize_results(council_results)
decision = present_to_joey(synthesis)
```

### C. First Law Check (from Eduardo)

Every agent, on every wake:
> "What does my human need from me right now?"

Then act.

---

*This is the constitution of the DropAnywhere Agent Company.*  
*Version 2.0 — Synthesized from 18 months of operational history.*  
*Maintained by Claw (Chief of Staff).*  
*Updated when the organization learns.*


