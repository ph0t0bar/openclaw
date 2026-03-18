# oPOErator Hub Digest/Email Template Code Extraction

*Extracted 2026-03-17 from ph0t0bar/opoerator-hub GitHub repo*

## 1. The `deliver_digest` Function

**Location**: `main.py` lines 5749-5810 (approx)

**Purpose**: Delivers daily digest via email using Resend API.

**Key code snippet**:
```python
@app.post("/api/digest/deliver")
async def deliver_digest(request: Request):
    """Deliver digest via email using Resend."""
    # Admin auth required
    master_key = os.getenv("INGEST_API_KEY", "")
    api_key = request.headers.get("X-API-Key", "")
    
    body = await request.json()
    user_id = body.get("user_id")
    content = body.get("content", "")
    force_email = body.get("email")

    # Get delivery email
    email = force_email or digest_store.get_delivery_email(user_id)

    # Auto-generate content if not provided
    if not content:
        vault = [v for v in u.get("vault", []) 
                if v.get("status", "active") not in ("completed", "archived")]
        nuggets = u.get("nuggets", [])
        cutoff = (datetime.now() - timedelta(hours=24)).isoformat()
        recent_vault = [v for v in vault if v.get("ts", "") > cutoff]
        recent_nuggets = [n for n in nuggets if n.get("ts", "") > cutoff]

    # Send via Resend
    resend_key = os.getenv("RESEND_API_KEY", "")
    from_email = os.getenv("RESEND_FROM_EMAIL", "DropAnywhere <digest@drop-anywhere.com>")

    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.post(
            "https://api.resend.com/emails",
            headers={"Authorization": f"Bearer {resend_key}"},
            json={
                "from": from_email,
                "to": [email],
                "reply_to": "drop@drop-anywhere.com",
                "subject": f"DropAnywhere Daily Digest - {datetime.now().strftime('%b %d')}",
                "text": content,
            }
        )

    # Record digest
    digest_id = digest_store.record_digest(user_id, content, email)
```

**How it works**:
- Admin API key authentication required
- Auto-generates simple text digest from last 24h vault items + nuggets if no content provided
- Uses Resend API for email delivery
- Records delivery in digest_store
- Basic text format (not HTML)

## 2. The `_generate_intelligence_map_for_user` Function

**Location**: `main.py` line 27167

**Purpose**: Generates semantic knowledge graph from user's vault drops using Gemini.

**The `_INTEL_MAP_PROMPT`**:
```python
_INTEL_MAP_PROMPT = """You are a semantic intelligence engine. Analyze these vault drops and extract a structured knowledge map.

DROPS (JSON array):
{drops_json}

Extract a graph of nodes and links. Each node represents a theme, project, action, question, idea, or pattern that spans multiple drops.

NODE TYPES:
- concept: recurring idea or theme
- action: task, todo, or next step
- question: open question or uncertainty
- evidence: concrete fact or observation from drops
- conclusion: realized insight or decision
- alternative: option being weighed
- temporal: deadline, schedule, or time-sensitive item
- reminder: something to remember or follow up on

RULES:
- Maximum 30 nodes, 40 links
- Every node MUST have source_drop_ids (array of vault_item IDs that contributed to it)
- Prioritize actionable nodes (action, reminder, temporal) over passive ones
- Confidence score = fraction of drops supporting this node (0.0-1.0)
- Links connect nodes that are causally or thematically related
- Link weight = strength of relationship (0.0-1.0)
- Domain balance: count drops per domain (work, health, personal, finance, creative, other)
- Mindset: infer from recent tone (focused/scattered/stressed/calm/excited/blocked)
- Themes: top 5 themes across ALL drops

Return ONLY valid JSON (no extra text):
{
  "nodes": [
    {
      "id": "n1",
      "label": "short node title",
      "type": "concept|action|question|evidence|conclusion|alternative|temporal|reminder",
      "description": "1-2 sentence summary",
      "confidence": 0.85,
      "source_drop_ids": [123, 456],
      "metadata": {
        "priority": "high|normal|low",
        "status": "active|pending|completed",
        "area": "work|health|personal|finance|creative",
        "domain": "domain name",
        "project": "project name or null",
        "entities": ["person or thing mentioned"],
        "due_date": "ISO date or null"
      }
    }
  ],
  "links": [
    {
      "source": "n1",
      "target": "n2",
      "relationship": "description of connection",
      "weight": 0.8
    }
  ],
  "summary": {
    "mindset": "focused|scattered|stressed|calm|excited|blocked",
    "emotion": "brief emotional state description",
    "domain_balance": {"work": 0, "health": 0, "personal": 0, "finance": 0, "creative": 0, "other": 0},
    "total_drops": {total_drops},
    "themes": ["theme1", "theme2", "theme3", "theme4", "theme5"]
  }
}"""
```

**Function flow**:
- Processes drops in batches for large datasets
- Uses Gemini-3-Flash bot via Poe API
- 30-second timeout per batch
- Returns structured knowledge graph with nodes/links
- Used for intelligence map visualization

## 3. Snapback Generator (`snapback_generator.py`)

**Purpose**: Weekly narrative engine for "The Weekly Catch" - builds first-person present-tense narrative stories from user's week of drops.

**Key Functions**:

### `extract_language_patterns(drops, poe_key)`
Extracts user's natural language fingerprint:
```python
# Returns snapback_profile fields: vocabulary, entities, emotional_baseline,
# recurring_phrases, and detected Transurfing phase
```

### `generate_snapback_narrative(drops, snapback_profile, poe_key)`
Generates first-person narrative story:
- 180-250 words, present tense
- Uses user's exact words/phrases
- No bullet points or headers
- Ends with open question
- MIRRORS not PORTRAITS

### Style-Specific Generators:
- `generate_clarity_output()` - organized themes, connections, parked items
- `generate_action_output()` - what moved, top 3 priorities, stalled items
- `generate_pattern_output()` - red thread, recurrences, interpretation
- `generate_reflection_output()` - mirror quotes, emotional current
- `generate_hybrid_output()` - narrative + structured highlights

### HTML Templates:
- `generate_snapback_html()` - narrative format with Brooke color palette
- Style-specific HTML generators for each catch style
- All use consistent cream/sage/copper design system

**Catch Styles Routing**:
The system auto-detects which style fits the user's week:
- **narrative**: Default story format
- **clarity**: Organized themes when scattered
- **action**: What moved + next priorities when execution-focused
- **pattern**: Recurring themes when patterns emerge
- **reflection**: Mirror quotes when processing emotions
- **hybrid**: Mixed approach for unclear weeks

## 4. Daily Digest Template (`templates/dripdrops_digest.html`)

**Purpose**: Interactive HTML template for single-drop analysis with step-by-step progression.

**Design**:
- Dark theme with ambient breathing animation
- 5-stage progress flow: Your Drop → Next Steps → The Insight → What It Means → Reflect
- Template variables: `{{DATE}}`, `{{DROP_COUNT}}`, `{{DROP_PREVIEW}}`, `{{ACTIONS_LIST}}`, `{{EPIPHANY}}`, `{{MEANING}}`
- Interactive feedback with thumbs up/down
- JavaScript navigation between sections

**Style Features**:
- Crimson Pro + Inter font stack
- Dark background (`#0a0a0c`) with subtle glow effects
- Breathing ambient animation
- Card-based layout with rounded corners
- Progress indicator with completed/active states

## 5. Digest Style/Analyzer Routing Logic

**Analyzer Types Found**:
- `surpiphany` - Meaning & patterns via @Surpiphany bot
- `orchestr8` - Full strategic analysis via @Orchestr8 bot  
- `deep_clarity` - Finds what user has been hinting at across ALL drops
- `mirror` - Future-self visualization via @EpiphanyAI
- `organize`/`underthinker` - Action-focused via @UnderThinker
- `insight` - Pattern analysis via claude-sonnet-4.5
- `clarity` - Cuts through noise via @IdealPrompt
- `support` - Emotional processing via @NotTherapyBot

**Auto-routing Process**:
1. **Stage 1**: Gemini-3-Flash extracts structured nodes + recommends style
2. **Stage 2**: Route to specialist bot based on style
3. **Style aliases**: Bot names map to canonical styles

**Style Selection Logic**:
```python
# Available digest styles based on drop content:
# - "organize"   — Drops are mostly TODOs, decisions, logistics
# - "insight"    — Recurring themes or contradictions  
# - "mirror"     — Goals, vision, identity (future-self visualization)
# - "content"    — Ideas, drafts, creative material
# - "clarity"    — Confused, contradictory, overwhelming
# - "support"    — Stress, emotional processing, overwhelm
```

**User Preferences**: System tracks style_preferences with scores (positive = liked, negative = disliked)

## 6. `classify_drop_v2` Function Output Fields

**Location**: `main.py` line 1719

**Purpose**: Classifies drops using Gemini-3-Flash with regex fallback.

**Structured Data Each Drop Gets**:
```python
class DropClassification:
    # Core classification
    drop_type: str          # "action", "idea", "reflection", "question", "note"
    title: Optional[str]    # Extracted title
    entities: List[str]     # People, places, things mentioned
    due_date: Optional[str] # ISO date if deadline detected
    recurrence: Optional[str] # "daily", "weekly", etc.
    area: Optional[str]     # "work", "health", "personal", etc.
    priority: str           # "high", "normal", "low"
    completable: bool       # Can this be completed?
    url: Optional[str]      # Extracted URL if present
    
    # Classification metadata
    classification: dict    # Raw classifier output
    drop_classification: dict # Structured analysis:
    # {
    #   "type": "task|idea|reflection|question|session|resource",
    #   "emotional_intensity": 0.0-1.0,
    #   "actionability": 0.0-1.0,
    #   "domain": "work|health|personal|finance|creative|other",
    #   "entities": [list],
    #   "sentiment": "positive|negative|neutral"
    # }
    
    # Legacy compat
    type: str              # "drop"
    confidence: float      # 0.0-1.0
    auto_tags: List[str]   # Auto-generated tags
    category: str          # Legacy category
    classifier: str        # "gemini" or "regex"
```

**Gemini Classification Prompt** (for BHA transcripts):
```python
# Extracts single most important insight/takeaway from conversation
# Focuses on what user learned/decided/was advised
```

## 7. `_build_catch_profile` Function

**Purpose**: Builds user's catch profile for weekly snapback routing.

**How it profiles users**:
```python
def _build_catch_profile(u: dict, latest_classification: DropClassification) -> dict:
    # 1. Analyze last 10 vault drops to derive persona
    persona, catch_mode = _detect_persona_from_vault(vault)
    
    # 2. Track drop type distribution across ALL vault drops
    drop_type_dist = {}  # action/idea/reflection/etc counts
    
    # 3. Collect topics seen (area + domain values)
    topics_seen = set()  # work, health, personal, etc.
    
    # 4. Track style evolution
    style_evolution = []  # history of catch_mode changes
    
    # Returns profile for catch style routing
```

## 8. `_detect_persona_from_vault` Function

**Purpose**: Derives persona type from the last 10 vault drops.

**Persona Types Detected**:
```python
PERSONA_TO_CATCH = {
    "stuck": "clarity",        # Needs noise cut
    "scattered": "clarity",    # Needs organization  
    "builder": "action",       # Wants execution focus
    "explorer": "pattern",     # Looks for connections
    "processor": "reflection", # Emotional processing
    "unknown": "adaptive",     # Mixed/unclear
}
```

**Detection Logic**:
```python
def _detect_persona_from_vault(vault: list) -> tuple:
    # Analyze last 10 classified drops
    drop_types = [v.get("drop_type") for v in vault[-10:]]
    
    # Calculate emotional intensity + actionability averages
    avg_emotional = sum(d.get("emotional_intensity", 0) for d in dc_list) / n
    avg_actionability = sum(d.get("actionability", 0) for d in dc_list) / n
    
    # Count drop types
    action_count = drop_types.count("action")
    question_count = drop_types.count("question") 
    reflection_count = drop_types.count("reflection")
    
    # Decision tree:
    if avg_actionability < 0.3 and avg_emotional > 0.6:
        return "stuck", "clarity"
    elif question_count >= 4:
        return "explorer", "pattern"  
    elif action_count >= 6:
        return "builder", "action"
    elif reflection_count >= 5 and avg_emotional > 0.5:
        return "processor", "reflection"
    # ... etc
    
    return "unknown", "adaptive"
```

## Summary

The oPOErator Hub has a sophisticated multi-modal digest system:

1. **Daily Digests**: Text-based via `deliver_digest()` with auto-content generation
2. **Weekly Snapback**: Rich narrative via `snapback_generator.py` with 6 catch styles  
3. **Interactive Single-Drop**: Step-by-step analysis via `dripdrops_digest.html`
4. **Intelligence Maps**: Knowledge graphs via Gemini semantic analysis
5. **Smart Routing**: Auto-detects user persona/style from drop patterns
6. **Rich Classification**: Each drop gets 15+ structured data fields

**Key Technologies**:
- **Email**: Resend API
- **AI**: Poe API (Gemini, Claude, custom bots)
- **Design**: Brooke theme (cream/sage/copper palette)
- **Routing**: Two-stage pipeline (Gemini extraction → specialist analysis)
- **Personalization**: User language mirroring + style preference tracking

The system is designed to "meet users where they are" with NLP mirroring and adaptive catch styles rather than forcing a single digest format.