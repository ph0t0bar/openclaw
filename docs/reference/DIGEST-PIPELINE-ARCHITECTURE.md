# Digest Pipeline — Full Architecture Reference

**Last Updated:** 2026-03-17 05:53 CDT  
**Source:** `ph0t0bar/opoerator-hub` main.py (27,526 lines)  
**Author:** Claw (mined from GitHub source code)

---

## Overview

The digest pipeline transforms raw drops into personalized AI-synthesized email digests. It's the core product loop:

```
DROP → INGEST → CLASSIFY → EXTRACT → ANALYZE → RENDER → DELIVER
```

---

## Pipeline Stages

### Stage 0: Drop Ingestion & Classification

**Lines:** 1720-1878 (classify_drop_v2)  
**Model:** Gemini-3-Flash via Poe (8-second timeout, regex fallback)

Every drop gets classified on ingestion:
- `drop_type`: task, idea, question, observation, note, etc.
- `area`: work, health, personal, finance, creative, other
- `completable`: boolean (is this a task?)
- `entities`: extracted people, places, things
- `priority`: high/normal/low

Fallback: `classify_drop_content()` — regex-based keyword matching when Gemini is unavailable.

### Stage 1: Node Extraction via Gemini

**Function:** `extract_nodes_with_gemini()` (line 11437)  
**Model:** Gemini-3-Flash  
**Purpose:** Extract structured "nodes" from raw drops — themes, actions, patterns, connections

Input: Full drop content concatenated  
Output: JSON with extracted nodes (themes, key phrases, relationships)

Features:
- Respects user style preferences (if set)
- 30-second async timeout
- Graceful fallback on failure
- Called for EVERY digest generation

### Stage 2: Specialist Bot Routing

**Lines:** 11719-11970  
**Purpose:** Route extracted nodes to a specialist analysis bot

**Auto-routing (default):** When `analyzer="auto"`, Gemini's own recommendation from Stage 1 picks the specialist. The system has 15+ analyzers:

| Key | Bot/Style | What It Does |
|-----|-----------|-------------|
| `auto` | Gemini picks | Default — selects best style for the drops |
| `clarity` | Clarity Engine | Organized themes, focus report |
| `action` | Action Catch | Prioritized action items |
| `pattern` | Pattern Mirror | Cross-drop thread detection |
| `reflection` | Deep Mirror | No actions, just meaning |
| `surpiphany` | Surpiphany | Morning epiphany + prompt |
| `orchestr8` | Orchestr8 | FULL strategic analysis (priorities, emotional state, recommendations) |
| `mirror` | Mirror | Reflective (Jason's config) |
| `organize` | Organize | Structure-focused |
| `insight` | Insight | Pattern + aha moments |
| `support` | Support | Emotional support |
| `research` | Research | Research synthesis |
| `strategic` | Strategic | Business/project strategy |
| `idealstate` | IdealState | Transurfing/vision alignment |
| `acceptai` | Accept.AI | Adaptive emotional intelligence, NLP style matching |

The specialist receives Gemini's extracted nodes as context and writes the final prose.

### Stage 3: HTML Rendering

**Template:** `templates/dripdrops_digest.html` (Hub repo)  
**New templates:** `workspace/templates/intelligence-map-weekly-v2.html`

The analyzer output gets wrapped in styled HTML for email delivery.

### Stage 4: Email Delivery

**Service:** Resend  
**From:** `DropAnywhere <hello@drop-anywhere.com>`  
**Delivery window:** Staggered (±10 min jitter to avoid Resend rate limits)

---

## Digest Scheduler

Hub has a full async scheduler with:
- Per-user digest timing (daily or weekly)
- Staggered delivery windows
- Eligibility checks (digest_enabled, has drops, not paused)
- Skip logic for users with no new drops since last digest

**Hub env flags:**
- `ENABLE_DIGEST_SCHEDULER=true`
- `DISABLE_CRONS=1` (crons disabled on Hub service — they run elsewhere)

---

## User Settings That Affect Digests

| Setting | Values | Effect |
|---------|--------|--------|
| `digest_enabled` | true/false | Whether user receives digests at all |
| `digest_frequency` | daily/weekly | How often |
| `preferred_digest_style` | clarity/action/pattern/etc. | Which analyzer to use |
| `compass` | free text | Prepended to extraction prompt as "north star" |
| `communication_style` | free text | Influences analyzer tone |
| `timezone` | IANA timezone | Delivery window targeting |

---

## DCS Worker Synthesis

Some vault items contain processed intelligence from the DCS (DropAnywhere Code System) worker:
- Tagged `DCS_WORKER`, `SYNTHESIS`
- Contains strategic analysis outputs
- Prioritized OVER raw drops in digest generation
- Referenced in vault_context building (line 5416-5476)

---

## Key Metrics

| Metric | Value (Mar 17) |
|--------|----------------|
| Total digests sent | 173+ |
| Eligible users | ~41 |
| Delivery rate | ~90% (Resend) |
| Avg generation time | 4-8 seconds |
| Model cost per digest | ~$0.01-0.05 |

---

## Known Issues

1. **digest_enabled field location** — inconsistency between settings locations
2. **dropanywhere-cron service** — returns 404 (down), affects scheduled digests
3. **text_content() vs raw string** — token counting edge case in long drops
4. **Auto-admit timing** — edge cases with drip sequence triggers

---

*This is a living reference. Update when Hub code changes.*
