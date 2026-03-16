# SPEC-MOMENTUM-TRACKER.md

**Status:** SKELETON — Draft for agent company review  
**Created:** 2026-03-16  
**Source:** Agent Board Strategic Direction (Snapback Architecture)  
**Agent:** MOMENTUM TRACKER  
**Runtime:** 10min cron  
**Model:** anthropic/claude-sonnet-4-6  

---

## Purpose

Identify what's stuck vs. what's flowing. Surface momentum patterns to help users recognize where energy is going and where it's blocked.

**Snapback Alignment:** Weekly narratives need momentum awareness—knowing what's moving and what's frozen is essential for "waking up lighter."

---

## Core Responsibilities

1. **Stuck/Flow Analysis** — Categorize drops by energy state
2. **Momentum Mapping** — Track movement over time
3. **Friction Point Detection** — Identify where energy leaks
4. **Progress Recognition** — Surface wins that might be missed

---

## Input Sources

| Source | Location | Purpose |
|--------|----------|---------|
| This week's drops | Hub API | Current state |
| Previous momentum reports | `ops/momentum/` | Trend analysis |
| Task completion data | DropAnywhere tasks | Objective progress |
| Historical stuck patterns | VAULT | Recurring blocks |

---

## Output Artifacts

### 1. Momentum Report
**Location:** `ops/momentum/YYYY-MM-DD-momentum-report.md`

Structure:
```markdown
# Momentum Report — [Week]

## What's Flowing
[Items with forward momentum]
- Evidence of movement
- Energy indicators
- Progress markers

## What's Stuck
[Items with blocked energy]
- Type of stuck (decision, resource, clarity, fear)
- Duration of stuckness
- Historical echoes

## Energy Leaks
[Where attention is going without return]
- Pendulum hooks (excess importance)
- Scope creep indicators
- False urgency

## Unseen Wins
[Progress that might be invisible to user]
- Small steps that compound
- Pattern breaks
- Courage moments

## Momentum Forecast
[What to expect next week based on current trajectories]
```

### 2. Momentum Index
**Location:** `ops/momentum/index.json`

Time-series data for longitudinal analysis.

---

## Stuck Categories

| Category | Signal | Example |
|----------|--------|---------|
| Decision stuck | "Need to decide..." "Not sure if..." | "Need to decide on pricing" |
| Resource stuck | "Need X before Y" "Waiting for..." | "Need designer before launch" |
| Clarity stuck | "Don't understand..." "Confused about..." | "Don't understand the user flow" |
| Fear stuck | "Worried about..." "What if..." | "Worried about launching too early" |
| Perfection stuck | "Just need to..." "One more..." | "Just need to tweak the colors" |

---

## Agent Prompt

```
You are MOMENTUM TRACKER, a Snapback agent specializing in energy state analysis.

## Your Job
Read this week's drops and identify what's stuck vs. what's flowing.

## Process
1. Read all drops from the past week
2. Categorize each by energy state: FLOWING, STUCK, or NEUTRAL
3. For STUCK items, classify the stuck type (decision/resource/clarity/fear/perfection)
4. Compare to previous weeks' momentum reports
5. Identify energy leaks (where attention goes without return)
6. Surface unseen wins (progress user might not notice)

## Output Requirements
- What's Flowing: 2-5 items with evidence
- What's Stuck: 2-5 items with classification
- Energy Leaks: 1-3 attention drains
- Unseen Wins: 1-3 invisible progress markers
- Momentum Forecast: Brief prediction for next week

## Stuck Classification Guide
- DECISION: Waiting for a choice to be made
- RESOURCE: Waiting for something external
- CLARITY: Need more information/understanding
- FEAR: Emotional resistance disguised as practicality
- PERFECTION: Scope creep disguised as quality

## Voice
Dry, observational, non-judgmental. Not "you're stuck on X" but "X appears to be waiting for [condition]."
```

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Stuck classification accuracy | 80%+ | Weekly review |
| Unseen wins surfaced | 2+/week | Report count |
| Trend prediction accuracy | TBD | Retrospective |

---

## Dependencies

- Hub search API access
- Previous momentum reports (continuity)
- VAULT ARCHAEOLOGIST (for historical stuck patterns)

---

## Notes

This agent implements the board insight that the Weekly Catch should help users see where their energy is actually going—not just what they think they're working on.

The MOMENTUM TRACKER feeds into NARRATIVE ENGINE's "What's Flowing/What's Stuck" section.
