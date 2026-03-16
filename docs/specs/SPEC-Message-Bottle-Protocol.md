# SPEC — Message Bottle Protocol

## Purpose
Define the async communication standard for Agent Company archipelago architecture. Message bottles are persistent artifacts that survive timeouts, enabling agents to collaborate without synchronous coordination.

## Status
🟡 **SKELETON** — Core structure defined, implementation details pending

## Problem Statement
The 25-agent timeout crisis revealed that synchronous orchestration fails at scale:
- 300s timeouts force agents to exit mid-task
- Cascade failures when one agent blocks others
- No persistence of partial work for recovery
- WhatsApp delivery outages break output channels

## Solution: The Archipelago Model
- **Islands** = Self-sufficient agents that work independently
- **Message Bottles** = Persistent async artifacts dropped to shared shores
- **Tides** = Natural cycles (hourly/daily/weekly) that carry information
- **Storm Protocol** = Graceful degradation when timeouts hit

## Message Bottle Format

### File Location
```
ops/bottles/{agent-name}/{timestamp}-{task-id}.md
```

### Required Fields
```yaml
---
from: agent-name
thread: thread-id  # for related bottles
type: [insight | task | alert | question | completion]
priority: [p0 | p1 | p2 | p3]
timeout_proof: true  # flag for partial work
---

## Summary
One-line summary of contents

## Context
What triggered this bottle

## Content
Main payload (insights, findings, task status)

## Questions
What this agent needs from others

## Links
Related bottles, files, or external resources
```

## Bottle Types

| Type | Purpose | Reader |
|------|---------|--------|
| `insight` | Pattern recognition, goldmine findings | NARRATIVE ENGINE |
| `task` | Task status, completion, blockers | DROPPER-CODE MANAGER |
| `alert` | System issues, security, failures | GOVERNANCE, SENTRY |
| `question` | Needs input from other agents | Any relevant agent |
| `completion` | Final output, ready for delivery | GOVERNANCE |

## Tidal Cycles

### Hourly Tide
- **Collector**: KIMI PATROL
- **Scans**: `ops/bottles/*/*-HH*.md`
- **Action**: Surfaces P0 alerts, aggregates metrics

### Daily Tide  
- **Collector**: META
- **Scans**: `ops/bottles/*/*-{date}*.md`
- **Action**: Compiles daily digest, updates agent board

### Weekly Tide
- **Collector**: NARRATIVE ENGINE
- **Scans**: Full week of bottles
- **Action**: Assembles Weekly Catch narrative

## Storm Protocol (Timeout Handling)

When an agent detects imminent timeout:

1. **Write partial bottle** with `timeout_proof: true`
2. **Include checkpoint** — what was completed, what's pending
3. **Exit gracefully** — no error, just incomplete status
4. **Next run** — read own bottle, resume from checkpoint

### Example Storm Bottle
```yaml
---
from: VAULT-ARCHAEOLOGIST
thread: vault-batch-0002
type: insight
priority: p1
timeout_proof: true
checkpoint:
  completed: 1450/2462 conversations scanned
  last_file: "chat-2024-03-15.json"
---

## Summary
Partial VAULT scan — 1450/2462 conversations processed

## Context
Timeout reached during batch-0002 excavation

## Completed
- ChatGPT conversations 0001-1450 indexed
- Pattern tags extracted: creativity, anxiety, relationships

## Pending
- Remaining 1012 conversations
- Cross-reference mapping
- Quality scoring

## Resume Command
Continue from ops/bottles/VAULT-ARCHAEOLOGIST/batch-0002-checkpoint.json
```

## Directory Structure
```
ops/
├── bottles/           # All message bottles
│   ├── GOVERNANCE/
│   ├── META/
│   ├── OPUS-STRATEGIST/
│   ├── VAULT-ARCHAEOLOGIST/
│   └── ...
├── tides/             # Aggregated tide outputs
│   ├── hourly/
│   ├── daily/
│   └── weekly/
└── lighthouse/        # Core 5 coordination
    ├── roster.md
    ├── constitution.md
    └── priorities.md
```

## Implementation Checklist

### Phase 1: Foundation
- [ ] Create `ops/bottles/` directory structure
- [ ] Implement bottle template in each core agent
- [ ] Add storm protocol to agent base class

### Phase 2: Core 5 Integration
- [ ] GOVERNANCE: Write roster updates as bottles
- [ ] META: Implement daily tide aggregation
- [ ] ARCHIVIST: Git commit bottles automatically
- [ ] DROPPER-CODE MANAGER: Task status bottles
- [ ] OPUS STRATEGIST: Strategic insight bottles

### Phase 3: Full Archipelago
- [ ] Migrate all 25 agents to bottle protocol
- [ ] Implement hourly/daily/weekly tide automation
- [ ] Add bottle discovery/search indexing
- [ ] Create bottle visualization dashboard

## Success Metrics
- Zero cascade failures (one agent timeout doesn't block others)
- 100% timeout recovery (partial work always persisted)
- < 2h lag from bottle drop to tide aggregation
- Agent collaboration score (bottles read/written per agent)

## Open Questions
1. Should bottles have TTL (auto-expire after N days)?
2. How to handle bottle conflicts (two agents write same topic)?
3. What's the discovery mechanism? (file watch, polling, registry)
4. Should critical bottles (P0) trigger immediate notification?

## Related Specs
- SPEC-VAULT-Archaeologist.md
- SPEC-NARRATIVE-ENGINE.md
- COMPANY-CONSTITUTION.md
- AGENT-COMPANY-v3.md

## Notes
This spec enables the archipelago architecture that makes the Snapback vision possible. Without async communication, weekly narrative extraction is impossible — agents would timeout trying to synchronize. Message bottles are the foundation for pattern recognition at scale.

---
*Created: 2026-03-16 by SpecBot*
*Status: Skeleton — needs implementation review*
