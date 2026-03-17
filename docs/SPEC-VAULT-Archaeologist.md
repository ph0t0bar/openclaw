# SPEC-VAULT-Archaeologist — Historical Pattern Mining Agent

**Status:** SKELETON — Drafted 2026-03-16 by SpecBot  
**Priority:** HIGH — Unlocks 2,462 conversations of dormant wisdom  
**Related:** `PRD-Action-Plan-2026-03-11.md` (VAULT→GOLDMINE→FORGE→OUTPUT pipeline)

---

## Problem Statement

Joey has **2,462 OpenAI conversations** and **467 Poe bots** archived in `joey-backup/Ingestion/` — representing $100K+ worth of cognitive work since Dec 2022. This VAULT sits dormant while current agents struggle to deliver value in 300s windows.

**The Waste:** Historical insights that could inform weekly narratives, surface recurring patterns, and accelerate decision-making remain buried.

**The Opportunity:** An agent that systematically excavates the VAULT by theme, connecting current drops to historical wisdom.

---

## Vision

> The VAULT ARCHAEOLOGIST transforms 3 years of archived thinking into living intelligence — surfacing relevant historical patterns when users need them most.

When someone drops "I feel stuck on music," the system mines 50+ historical conversations about creative blocks, music production, and breakthrough moments. The Weekly Catch becomes not just this week's summary — it's a **personalized narrative woven from years of context**.

---

## Core Capabilities

### 1. Theme-Based Excavation
- **Input:** User drops, Weekly Catch themes, or explicit queries
- **Process:** Search VAULT for semantically related conversations
- **Output:** Historical context clusters with relevance scores

### 2. Pattern Recognition
- Identify recurring themes across time (e.g., "creative block → breakthrough" cycles)
- Surface forgotten insights that apply to current situations
- Detect evolution in thinking ("Joey's approach to X has shifted from Y to Z")

### 3. Narrative Enrichment
- Inject relevant historical quotes into Weekly Catches
- Create "memory lane" moments: "3 years ago you solved a similar problem by..."
- Build thematic threads that span months/years

### 4. Goldmine Extraction
- Pull specific prompts, frameworks, and workflows from historical conversations
- Extract persona definitions, system prompts, and tool configurations
- Stage valuable content in FORGE for productization

---

## Data Sources

| Source | Location | Size | Content |
|--------|----------|------|---------|
| ChatGPT VAULT | `joey-backup/Ingestion/0_VAULT/conversations/` | 2,070 files | Full conversation exports Dec 2022–Jul 2024 |
| Poe Bots | `joey-backup/Ingestion/.claude/context/` | 34 files | Personas, system prompts, brain states |
| BHA Archive | `joey-backup/Ingestion/0_VAULT/BHA/` | 52 files | Notion exports: Personas, KB, Messages |
| Recent Drops | `joey-backup/Ingestion/2026*/` | 80+ files | Jan–Mar 2026 drops and chats |

---

## Technical Architecture

### Processing Pipeline

```
VAULT (raw conversations)
    ↓
[INGESTION] — Parse JSON, extract messages, metadata
    ↓
[EMBEDDING] — Generate embeddings for semantic search
    ↓
[INDEX] — Vector store (ChromaDB/Pinecone/similar)
    ↓
[QUERY] — Theme-based retrieval + relevance ranking
    ↓
[GOLDMINE] — Extracted patterns, quotes, frameworks
    ↓
[ENRICH] — Inject into Weekly Catch / agent context
```

### Key Components

1. **Parser Module**
   - Handle ChatGPT export format (conversations.json structure)
   - Parse Poe bot definitions (markdown frontmatter)
   - Extract timestamps, topics, message threads

2. **Embedding Engine**
   - Model: `text-embedding-3-large` or similar
   - Chunking: By conversation thread + semantic breaks
   - Metadata: Date, topic tags, conversation ID

3. **Retrieval System**
   - Semantic search across all VAULT content
   - Time-decay weighting (recent = more relevant)
   - Cross-reference with current drops for context

4. **Pattern Detector**
   - Cluster similar themes across time
   - Identify recurring keywords, sentiments, decisions
   - Surface "invisible" patterns humans miss

---

## Integration Points

| System | Integration | Purpose |
|--------|-------------|---------|
| Weekly Catch Generator | API call with theme | Enrich narratives with historical context |
| DropAnywhere Hub | `/api/memory/context` endpoint | Surface relevant past drops |
| Opus Strategist | Shared workspace reads | Strategic insights from historical patterns |
| Goldmine Index | Write to `docs/reference/goldmine/` | Staged extraction for FORGE pipeline |

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Coverage | 100% VAULT indexed | File count / total |
| Retrieval accuracy | >80% relevance | Manual spot-checks |
| Weekly enrichment | 3+ historical refs per Catch | Automated count |
| Pattern discoveries | 5+ new patterns/week | Agent-reported + validated |
| User value | "This resonates" feedback | Qualitative tracking |

---

## Implementation Phases

### Phase 1: Foundation (Week 1)
- [ ] Parse ChatGPT conversation exports
- [ ] Generate embeddings for 100 test conversations
- [ ] Build basic semantic search
- [ ] Manual validation of retrieval quality

### Phase 2: Integration (Week 2)
- [ ] Connect to Weekly Catch pipeline
- [ ] Auto-inject historical context
- [ ] Build Pattern Detector v1
- [ ] Create GOLDMINE staging output

### Phase 3: Scale (Week 3-4)
- [ ] Index full 2,462 conversations
- [ ] Add Poe bot parsing
- [ ] Real-time enrichment API
- [ ] Self-improving relevance ranking

---

## Open Questions

1. **Storage:** Where do embeddings live? (ChromaDB local, Pinecone cloud, or Hub Postgres?)
2. **Privacy:** Any conversations that should be excluded from indexing?
3. **Compute:** Embedding 2,462 conversations = ~$X in API costs — budget approval?
4. **Refresh:** How often to re-index? Incremental updates vs full rebuild?
5. **Ownership:** Which agent owns the VAULT long-term? ARCHAEOLOGIST or ARCHIVIST?

---

## Related Work

- `PRD-Action-Plan-2026-03-11.md` — Section 9: Transformation Engine (VAULT→GOLDMINE→FORGE→OUTPUT)
- `goldmine-index.md` — Existing goldmine staging area
- `ops/agent-board.md` — OPUS STRATEGIST vision for VAULT mining
- `SPEC-Adaptive-Weekly-Catch-2026-03-11.md` — Weekly Catch system to enrich

---

## Appendix: Sample Queries

```
"Find all conversations about creative blocks and breakthroughs"
"What frameworks has Joey used for decision-making?"
"Show me the evolution of Joey's approach to AI assistants"
"Extract all system prompts for Poe bots"
"Find music-related drops from the past 3 years"
"What did Joey write about Transurfing before March 2026?"
```

---

*Skeleton drafted by SpecBot — 2026-03-16*  
*Ready for expansion when priority confirmed*

