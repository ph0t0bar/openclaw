# Poe Orchestrator — Full Architecture Reference

**Last Updated:** 2026-03-17 05:53 CDT  
**Source:** `ph0t0bar/opoerator-hub` poe_orchestrator.py (477 lines) + main.py  
**Author:** Claw (mined from GitHub + MEMORY.md)

---

## Overview

The Poe Orchestrator is Hub's intelligence layer for the God Mode 15 persona bots. It intercepts Poe bot conversations and injects:
1. Real system prompts (from `GOD_MODE_15_PROMPTS.md`, not the Poe bot's built-in prompt)
2. BHA funnel CTAs (dynamically, on every conversation)
3. Conversation logging to vault (async)

---

## Architecture

```
User on Poe → Shadow Bot (e.g. theREALrealtalk-v2)
  → Poe API calls Hub: POST /poe/v1/chat/completions
  → Hub looks up persona prompt from GOD_MODE_15_PROMPTS.md
  → Hub injects BHA funnel CTA
  → Hub routes to actual model via OpenRouter/Poe
  → Response streams back to user
  → Conversation logged to vault (async)
```

### Key Endpoint
`POST /poe/v1/chat/completions` (on Hub)  
**Auth:** `POE_ORCHESTRATOR_KEY` env var

### Why Shadow Bots?
- Can't PATCH existing Poe prompt bots (Poe returns 500 on write)
- Solution: 16 shadow API bots created (theREALrealtalk-v2, BrutallyHonest-v2, etc.)
- All route through Hub orchestrator
- Original bots still work but don't get dynamic features

---

## God Mode 15 Personas

**Source file:** `GOD_MODE_15_PROMPTS.md` (1,578 lines, 47K chars, Personality Layer v2.0)

All prompts are loaded from this file, NOT from Poe's built-in bot prompt field.

### Alias System
Maps 30+ model names to actual personas:
- `gm-*` prefixed names
- Real Poe handles (theREALrealtalk, BrutallyHonestAI, etc.)
- Variant names (v2, shadow, etc.)

### BHA Funnel CTA Injection
On every Poe conversation, the orchestrator dynamically appends a BHA CTA. This is the cross-sell mechanism — free Poe bot users → paid BHA subscribers.

---

## Model Routing (BHA)

**Current state:** ALL presets route through `therealrealtalk` Poe bot handle.

**BHA model tiers:**
| Tier | Model | Use Case |
|------|-------|----------|
| Reflex | GPT-4o-mini | Quick responses |
| Reason | Gemini 2.5 Flash | Analytical |
| Resolve | Claude Sonnet 4.5 | Deep/nuanced |

**System prompts:** Come from Notion per persona (NOTION_PERSONAS_DB_ID), NOT from the Poe bot's built-in prompt.

### To Add New Bots
1. Update GOD_MODE_15 list in `config.ts`
2. Ensure Notion entry has system prompt
3. Add showcase entries
4. Create shadow API bot on Poe if needed

---

## Poe Cost Tracking

**File:** `poe_cost_tracker.py`  
**Alert threshold:** Balance < 500 points = critical alert  
**High burn threshold:** > 5,000 points per 6 hours

### Current State (Mar 17)
| Metric | Value |
|--------|-------|
| Balance | ~20K points |
| Burn rate | ~6,300/hr (high) |
| Status | CRITICAL |
| Runway | ~3 hours at current rate |

---

## Key Files

| File | Repo | Lines | Purpose |
|------|------|-------|---------|
| `poe_orchestrator.py` | opoerator-hub | 477 | Orchestrator routing, CTA injection |
| `GOD_MODE_15_PROMPTS.md` | opoerator-hub | 1,578 | All 15 persona system prompts |
| `poe_cost_tracker.py` | opoerator-hub | — | Balance monitoring, alerts |
| `main.py` (various) | opoerator-hub | — | Poe API integration, bot_name routing |

---

## PAT & Auth

- **POE_ORCHESTRATOR_KEY:** Stored on Hub Railway env + local `.env.local`
- **POE_API_KEY / POE_ACCESS_KEY_PCB:** For Poe API calls
- **POE_DROP_ACCESS_KEY:** For drop-specific Poe operations
- **GH_TOKEN PAT:** Upgraded to read+write for code/issues/PRs/hooks (was read-only, fixed Mar 9)

---

*This is a living reference. Update when orchestrator code changes.*
