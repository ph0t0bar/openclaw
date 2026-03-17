# Intelligence Map — Full Architecture Reference

**Last Updated:** 2026-03-17 05:53 CDT  
**Source:** `ph0t0bar/opoerator-hub` main.py + `ph0t0bar/dropanywhere-app` IntelligenceView.tsx + extract-intelligence.ts  
**Author:** Claw (mined from GitHub source code)

---

## Overview

The Intelligence Map is DropAnywhere's core value proposition — it takes raw "drops" (thoughts, voice notes, screenshots, emails) and produces a structured knowledge graph + prose synthesis showing the user what their mind is actually doing.

**Two-stage pipeline:** Gemini-3-Flash extracts structure → specialist bot (or Gemini itself) writes prose.

**Three rendering surfaces:**
1. **Frontend dashboard** — IntelligenceView.tsx (interactive, animated, Framer Motion)
2. **Email digest** — HTML email (the email-only product for March 24 launch)
3. **API** — `/api/intelligence/generate` and `/api/intelligence/latest` (raw JSON)

---

## Stage 1: Hub Backend — Graph Generation

**File:** `opoerator-hub/main.py` lines 27034-27350  
**Endpoint:** `POST /api/intelligence/generate`  
**Model:** Gemini-3-Flash via Poe API (fastpath-preview)  
**Cache:** 20-hour TTL in `intelligence_maps` Postgres table

### Input
- ALL active vault drops for a user (status NOT IN archived/completed)
- Fields: id, text, title, drop_type, area, domain, priority, tags, entities, due_date, created_at
- Batched in groups of 100 (Gemini context window limit)
- Node IDs re-namespaced across batches (`b0_n1`, `b1_n1`, etc.)

### Prompt (_INTEL_MAP_PROMPT)
Asks Gemini to extract a graph with:

**Node Types (8):**
| Type | Description |
|------|-------------|
| `concept` | Recurring idea or theme |
| `action` | Task, todo, or next step |
| `question` | Open question or uncertainty |
| `evidence` | Concrete fact or observation |
| `conclusion` | Realized insight or decision |
| `alternative` | Option being weighed |
| `temporal` | Deadline, schedule, time-sensitive |
| `reminder` | Something to follow up on |

**Node Schema:**
```json
{
  "id": "n1",
  "label": "short node title",
  "type": "concept|action|question|...",
  "description": "1-2 sentence summary",
  "confidence": 0.85,
  "source_drop_ids": [123, 456],
  "metadata": {
    "priority": "high|normal|low",
    "status": "active|pending|completed",
    "area": "work|health|personal|finance|creative",
    "domain": "domain name",
    "project": "project name or null",
    "entities": ["person or thing"],
    "due_date": "ISO date or null"
  }
}
```

**Link Schema:**
```json
{
  "source": "n1",
  "target": "n2",
  "relationship": "description of connection",
  "weight": 0.8
}
```

**Summary Schema:**
```json
{
  "mindset": "focused|scattered|stressed|calm|excited|blocked",
  "emotion": "brief emotional state description",
  "domain_balance": {"work": 8, "health": 0, "personal": 2, "finance": 0, "creative": 4, "other": 0},
  "total_drops": 14,
  "themes": ["theme1", "theme2", "theme3", "theme4", "theme5"]
}
```

**Limits:** Max 30 nodes, 40 links per generation.

### Fallback
`_intel_map_fallback()` — keyword-based grouping when Gemini fails:
- Groups drops by area/domain
- Extracts action nodes from completable/task drops
- Word frequency for themes (words > 5 chars)
- Marked with `"_fallback": true`

### Storage
```sql
INSERT INTO intelligence_maps (user_id, map_data, node_count, link_count, drop_count, generation_time_ms)
```

### API Response
```json
{
  "status": "generated|cached",
  "id": 42,
  "map_data": { "nodes": [...], "links": [...], "summary": {...} },
  "node_count": 22,
  "link_count": 18,
  "drop_count": 14,
  "generated_at": "2026-03-17T10:00:00Z",
  "generation_time_ms": 4500
}
```

---

## Stage 1b: Frontend Intelligence Extraction

**File:** `dropanywhere-app/pages/api/thought-map/extract-intelligence.ts`  
**Model:** Gemini-3-Flash via Poe chat completions API  
**Temperature:** 0.3  
**Drop limit:** Up to 500 (from 1000 fetched)

This is a SECOND, richer extraction that runs client-side (triggered by the Intelligence tab). It produces categorized items + emotion analysis on top of the graph nodes.

### Item Categories (5)

| Category | Label | Icon | Badge Type |
|----------|-------|------|------------|
| `active_project` | Active Projects | Rocket | status (in_progress/stalled/needs_attention) |
| `open_question` | Open Questions | HelpCircle | urgency (high/medium/low) |
| `reminder_task` | Reminders & Tasks | Bell | due_hint (tomorrow/this_week/soon/someday) |
| `key_idea` | Key Ideas | Lightbulb | strength (strong/emerging/speculative) |
| `action` | Actions | Zap | priority (high/medium/low) |

### Item Schema
```json
{
  "id": "unique-kebab-id",
  "title": "Short descriptive title (max 50 chars)",
  "summary": "One or two sentences explaining what and why.",
  "category": "active_project|open_question|reminder_task|key_idea|action",
  "status": "in_progress|stalled|needs_attention",
  "urgency": "high|medium|low",
  "due_hint": "tomorrow|this_week|soon|someday",
  "strength": "strong|emerging|speculative",
  "priority": "high|medium|low",
  "confidence": 0.85,
  "source_drop_ids": ["drop-id-1"],
  "emotion": "frustrated|anxious|stuck|hopeful|energized|neutral",
  "intensity": 0.6,
  "related_items": ["other-item-id"],
  "topic_tags": ["tag1", "tag2"]
}
```

### Emotion Summary Schema
```json
{
  "dominant_emotion": "hopeful",
  "emotion_distribution": {
    "frustrated": 0.1,
    "anxious": 0.15,
    "stuck": 0.1,
    "hopeful": 0.4,
    "energized": 0.25,
    "neutral": 0.0
  },
  "mindset_trend": "improving|declining|stable|shifting",
  "key_themes": ["theme1", "theme2", "theme3"],
  "suggested_focus": "One actionable insight based on the emotional pattern"
}
```

### Emotion Colors (from IntelligenceView.tsx)
| Emotion | Color | Hex |
|---------|-------|-----|
| frustrated | Dusty Rose | #D4A5A5 |
| anxious | Warm Gold | #E8C97A |
| stuck | Gray | #B0B0B0 |
| hopeful | Sage Green | #A8B5A0 |
| energized | Warm Caramel | #C4A484 |
| neutral | Muted Brown | #8B8680 |

### Compass Integration
If the user has a `compass` field in their profile settings, it's prepended to the prompt:
```
COMPASS (the user's north star — filter everything through this lens):
  {user's compass text}
```
Same for `communication_style`.

### Filtering Rules (in prompt)
- SKIP test drops, code dumps, bot messages, system logs, noise
- SKIP drops that are just URLs with no context
- Only extract meaningful human thoughts, plans, questions, ideas

---

## Stage 2: Digest Pipeline (Two-Stage)

**File:** `opoerator-hub/main.py` lines 11437-11970  
**Purpose:** Generate the prose digest email that wraps around the intelligence data.

### Stage 2a: Node Extraction via Gemini
`extract_nodes_with_gemini()` — line 11437

- Runs on ALL user drops for digest window
- Extracts structured nodes (themes, actions, patterns, connections)
- Includes style preferences if available
- 30-second timeout, falls back gracefully

### Stage 2b: Specialist Bot Routing
When `analyzer` is `"auto"` (default), Gemini's own recommendation picks the specialist:

| Analyzer Key | Bot Name | Personality | Best For |
|-------------|----------|-------------|----------|
| `clarity` | Clarity Engine | Organized themes, focus report | Scattered thinkers |
| `action` | Action Catch | Prioritized action items | Builders, operators |
| `pattern` | Pattern Mirror | Cross-drop thread detection | Explorers, creatives |
| `reflection` | Deep Mirror | No actions, just meaning | Processors, journalers |
| `adaptive` | (system picks) | Best of all modes | New users (default) |
| `surpiphany` | Surpiphany | Morning meaning, epiphany + prompt | Morning digest |
| `orchestr8` | Orchestr8 | FULL strategic analysis | Deep strategic review |
| `mirror` | Mirror | Reflective | Jason's config |
| `organize` | Organize | Structure-focused | GTD types |
| `insight` | Insight | Pattern + aha moments | Creative thinkers |
| `support` | Support | Emotional support | Tough times |
| `research` | Research | Research synthesis | Learning mode |
| `strategic` | Strategic | Business/project strategy | Work mode |
| `idealstate` | IdealState | Transurfing/vision alignment | Manifestation |
| `acceptai` | Accept.AI | Adaptive emotional intelligence | Emotional coaching |

The specialist bot receives the Gemini-extracted nodes as context and writes the prose synthesis.

---

## Frontend Rendering — IntelligenceView.tsx

**File:** `dropanywhere-app/components/IntelligenceView.tsx` (828 lines)  
**Stack:** React, Framer Motion (AnimatePresence), Lucide icons

### Layout
- Collapsible section headers with item counts
- Grid of expandable cards (`minmax(280px, 1fr)`)
- Animated expand/collapse (motion.div, 0.15-0.2s)

### Card Features
- **Title row** with category-specific badge (status/urgency/due/strength/priority)
- **Source origin badge** — shows where the drop came from (email, SMS, voice, web, etc.)
- **PARA tags** — Projects/Areas/Resources/Archives classification (colored dots)
- **Topic tags** — regular tags in sage green pills
- **Confidence %** — subtle right-aligned text
- **Expanded view** adds: full summary, all tags, emotion badge with intensity %, confidence bar

### Interactivity
- Complete/uncomplete tasks (checkbox toggle, persisted to localStorage)
- Archive items (hidden from view)
- Copy item (title + summary to clipboard)
- Vault actions (triggerVaultAction callback)
- Navigate to PARA project (onNavigateToProject callback)

### Visual Design (Brooke Theme)
| Token | Value | Usage |
|-------|-------|-------|
| `--warm-white` | Card backgrounds | |
| `--accent-light` | Borders, muted backgrounds | |
| `--accent` | Caramel/copper accent | Active projects |
| `--sage` | Green | In progress, tags |
| `--rose` | Dusty rose | Questions, needs attention |
| `--soft-black` | Near-black | Titles, text |
| `--muted` | Gray-brown | Metadata, secondary text |

---

## Email Templates (New — March 2026)

### V1: Prose-First (`intelligence-map-weekly.html`)
**Location:** `workspace/templates/intelligence-map-weekly.html`  
**Approach:** Narrative-driven, reads like a letter from your second brain.

Sections:
1. Header (week dates, drop/theme/connection count)
2. The Pulse (one paragraph AI synthesis)
3. Themed Sections (5) with colored dots, drop counts, prose analysis, quoted drops
4. Connections Card (3 cross-theme insights)
5. Week in Numbers (stats table + domain balance bars)
6. One Thing (single actionable nudge)
7. CTA (mailto drop@drop-anywhere.com)

### V2: Data-Rich (`intelligence-map-weekly-v2.html`)
**Location:** `workspace/templates/intelligence-map-weekly-v2.html`  
**Approach:** Maps the full Gemini extraction output into email-friendly layout.

Sections:
1. Pulse Stats (drops/nodes/links/themes — 4 big numbers)
2. Mindset + Emotion (mindset label + emotion distribution bar with legend)
3. AI Synthesis (prose paragraph in styled blockquote)
4. Active Projects (cards with status badges)
5. Open Questions (cards with urgency levels)
6. Reminders & Tasks (table with due_hint badges)
7. Key Ideas (left-bordered quotes with strength indicators)
8. Connections (flattened graph links with relationship + weight)
9. Domain Balance (visual progress bars + week-over-week delta)
10. Suggested Focus (one actionable insight from emotion_summary)
11. CTA + Footer

### Design System (Email)
| Element | Color | Hex |
|---------|-------|-----|
| Background | Brooke Cream | #f5f0e8 |
| Card | White | #ffffff |
| Border | Warm Sand | #d4c5a9 |
| Primary Text | Forest Green | #2d5016 |
| Accent | Gold | #8B6914 |
| Sage | Muted Green | #5a7a5a |
| Alert | Campaign Red | #C41E3A |
| Muted | Warm Gray | #b8a88a |
| Inner backgrounds | Light Cream | #f0ebe0, #faf8f4 |

### Email Rendering Constraints
- No CSS classes (inline styles only)
- No flexbox in Outlook (use tables for critical layouts)
- No web fonts (Georgia/Times fallback)
- No emoji fonts in headless Chrome PDF (use HTML entities)
- Keep total email size under 100KB (Cloudflare WAF limit)

---

## Database Schema

### intelligence_maps table
```sql
CREATE TABLE intelligence_maps (
  id SERIAL PRIMARY KEY,
  user_id TEXT NOT NULL,
  map_data JSONB NOT NULL,
  node_count INTEGER,
  link_count INTEGER,
  drop_count INTEGER,
  generation_time_ms INTEGER,
  generated_at TIMESTAMP DEFAULT NOW()
);
```

### vault_items (source data)
Key fields used by intelligence extraction:
- `id`, `user_id`, `text`, `title`, `drop_type`, `area`, `domain`
- `priority`, `status`, `entities` (array), `tags` (array)
- `due_date`, `classification` (jsonb), `created_at`
- `completed_at` (null = active), `status` NOT IN ('archived', 'completed')

---

## Intelligence Scheduler

**Line 21475 in main.py:**
```python
# Intelligence map scheduler: daily map generation for active users
```
- Runs daily for active users
- Generates and caches maps proactively
- 20-hour cache TTL means maps are fresh each day

---

## Integration Points

| System | How it connects |
|--------|----------------|
| **Digest pipeline** | Stage 1 node extraction feeds into digest specialist bot |
| **Frontend** | `/api/intelligence/generate` called when user opens Intelligence tab |
| **Email product** | Hub generates map → templates render to HTML → Resend delivers |
| **Compass** | User's north star text prepended to extraction prompt |
| **PARA** | Tags from drops surface as colored PARA badges in frontend |
| **Poe orchestrator** | All Gemini calls route through Poe API (bot_name="Gemini-3-Flash") |
| **Dropper-Code** | Can create tasks based on intelligence map findings |

---

## Key Files

| File | Repo | Purpose |
|------|------|---------|
| `main.py:27034-27350` | opoerator-hub | Intelligence map generation, API endpoints |
| `main.py:11437-11580` | opoerator-hub | Node extraction (extract_nodes_with_gemini) |
| `main.py:11719-11970` | opoerator-hub | Digest pipeline (two-stage) |
| `main.py:1720-1878` | opoerator-hub | Drop classification (Gemini + regex fallback) |
| `extract-intelligence.ts` | dropanywhere-app | Frontend intelligence extraction (richer schema) |
| `IntelligenceView.tsx` | dropanywhere-app | Frontend rendering (828 lines, Framer Motion) |
| `pages/api/intelligence/index.ts` | dropanywhere-app | API proxy to Hub |
| `templates/dripdrops_digest.html` | opoerator-hub | Original digest HTML template |
| `templates/intelligence-map-weekly.html` | workspace | V1 email template (prose-first) |
| `templates/intelligence-map-weekly-v2.html` | workspace | V2 email template (data-rich) |

---

## What Makes It "Amazing" (Joey's Words)

The magic happens when Gemini processes 50-500 drops and surfaces:
1. **Cross-drop connections** the user didn't consciously make
2. **Emotion tracking** showing how their mindset shifts over time
3. **Domain balance** revealing where they're over/under-investing
4. **Temporal patterns** (when they drop, what surfaces at night vs morning)
5. **Actionable synthesis** — not just "here's what you said" but "here's what it means"

The frontend made this interactive (expand, complete, archive, navigate). The email version needs to deliver the same "wow" moment in a static format — which is why the prose synthesis paragraph is the anchor.

---

*This is a living reference. Update when Hub or frontend code changes.*
