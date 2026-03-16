# The Goldmine — Content Asset Index

**Philosophy: Pan for gold, don't mine from scratch.**
Joey has THOUSANDS of prompts, conversations, specs, and ideas already created. Our job is to FIND, CURATE, and POLISH — not reinvent.

## Primary Sources

### 1. joey-backup/Ingestion/ (2,422 files) — THE MOTHERLODE
Access: `source /root/.openclaw/.env.local && curl -s -H "Authorization: token $GITHUB_TOKEN" "https://api.github.com/repos/ph0t0bar/joey-backup/contents/Ingestion/{path}"`

| Path | Files | What's There |
|------|-------|-------------|
| `0_VAULT/conversations/` | 2,070 | ChatGPT conversations Dec 2022 – Jul 2024. 18 months of Joey's thinking. |
| `0_VAULT/BHA/` | 52 | Notion DB exports: Personas, System Prompts, Knowledge Base, Users, Messages, Workflows |
| `.claude/context/` | 34 | Brain state, mined patterns, persona architectures, ABOUT_JOEY_HAMER.md |
| `.claude/context/brain/` | 2 | `mined_conversations.json` + `patterns.json` — PRE-MINED intelligence |
| `.agent/workflows/` | ~10 | Eduardo agent workflows (hydration, extraction, sync) |
| `20260107/`–`20260310/` | 80+ | Dated drops/chats Jan–Mar 2026 |
| Root | 20+ | GOD_MODE_NOTION_FULL.md, FULL_HYDRATION_CONTEXT.md, _FROM-JOEY.md, SYSTEM_ARCHITECTURE.md |

### 2. joey-backup/specs/ — Processed Specs
Access: same API pattern with path `specs/`
- PRDs, orchestrator specs, funnel prompts
- Content transformation system design
- Social content drafts
- Launch critical path

### 3. joey-backup Root Docs
- `_FROM-JOEY.md` — Joey's writing voice samples (CRITICAL for content creation)
- `GOD_MODE_NOTION_FULL.md` — Complete Notion export
- `FULL_HYDRATION_CONTEXT.md` — Full context dump
- `SYSTEM_ARCHITECTURE.md` — Architecture overview
- `FULL_ASSET_INVENTORY.txt` — Everything that exists

### 4. Hub Drops (Live)
- `curl -s "https://hub-production-f423.up.railway.app/api/search?q={query}&user_id=b419d8ad5d23513f" -H "X-API-Key: $HUB_API_KEY"`
- 800+ drops with product ideas, feature requests, strategic thoughts
- Search by topic: `feature`, `idea`, `persona`, `prompt`, `strategy`, `launch`, etc.

### 5. Local Workspace
- `/root/.openclaw/workspace/docs/` — Current specs and PRDs
- `/root/.openclaw/workspace/social/` — Content drafts
- `/root/.openclaw/workspace/templates/` — Digest templates
- `/root/.openclaw/workspace/bank/` — Entity and opinion files

## Mining Priorities

### HIGH VALUE (mine these first)
1. **Persona prompts** — 0_VAULT/BHA/SYSTEM_PROMPTS.json has ALL persona system prompts. These are PRODUCTION TESTED.
2. **patterns.json** — Pre-identified thinking patterns from 18 months of conversations. Someone already started this work.
3. **_FROM-JOEY.md** — Voice samples. Essential for writing content that sounds like Joey.
4. **Recent drops** (Hub search) — Latest product ideas and strategic thinking.
5. **GOD_MODE_15_PROMPTS.md** — The 15 persona prompts already in production on Poe.

### MEDIUM VALUE (mine when doing related work)
6. **Conversations by topic** — Search conversations/ for specific themes when working on specs
7. **Knowledge Base** — 0_VAULT/BHA/KNOWLEDGE_BASE.json
8. **Notion workflows** — How Joey organized things before automation

### DEEP CUTS (mine during slow periods)
9. **Full conversation archive** — 2,070 conversations, topic-cluster and extract insights
10. **Eduardo workflows** — Reusable patterns for agent design
11. **Dated drops** — Jan-Mar 2026 strategic evolution

## Mining Protocol

When doing ANY creative or strategic work:
1. **SEARCH FIRST** — Check if Joey already wrote/thought about this
2. **QUOTE** — Use Joey's actual words when possible
3. **CREDIT** — Note which source file you pulled from
4. **CURATE** — Don't dump raw content. Extract, polish, contextualize.
5. **INDEX** — When you find gold, add it to this file so others can find it faster

## Discovered Gold (agents add finds here)
<!-- When you find something valuable, log it:
### [DATE] — [AGENT] found [WHAT] in [WHERE]
- Brief description of what it is and why it matters
- File path for quick access
-->

### 2026-03-16 — KIMI PATROL found BHA Notion Exports in joey-backup/Ingestion/0_VAULT/BHA/
- **What:** 52 JSON files from BHA Notion workspace export including Personas (6.4MB), Poe_Conversations (15.6MB), Poe_Bot_Development_List (2.5MB), MessageRatings (4.4MB)
- **Why it matters:** These are PRODUCTION-TESTED persona prompts and conversation data. Personas.json likely contains all 15+ BHA persona system prompts. Perfect source for content creation, persona development, and prompt engineering.
- **Access:** `curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/repos/ph0t0bar/joey-backup/contents/Ingestion/0_VAULT/BHA/Personas.json`
- **Priority:** HIGH — Mine Personas.json first when working on BHA specs or persona-related content

### 2026-03-16 — OPUS STRATEGIST deep-mined Personas.json
- **What:** Analyzed BHA Personas.json — contains full production persona prompts with sophisticated psychological frameworks
- **Key discoveries:**
  - "epiphany ai (dashstart)" — The Algorithmic Confessor with "Vulnerability Gap" and "Illusion of Unique Brokenness" concepts
  - VariableBoi — Content transformation with {{variable}} templating
  - AirtableDude — Technical instruction generator (8000-word responses!)
  - All include "SystemPrompt", "DisplayName", "Emoji", metadata
- **Joey's prompt philosophy:** Personas address universal human fears (being unlovable, failure, shame) through reframing techniques. The "holy fuck moment" is when users realize their "unique" pain is universal.
- **Access pattern:** `curl -H "Authorization: token $GITHUB_TOKEN" -H "Accept: application/vnd.github.v3.raw" https://api.github.com/repos/ph0t0bar/joey-backup/contents/Ingestion/0_VAULT/BHA/Personas.json`
- **Use for:** BHA persona development, prompt engineering patterns, understanding Joey's conversational psychology approach
