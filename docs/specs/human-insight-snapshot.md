# Human Insight Snapshot — Quick-Build Onboarding

**Status:** Concept | **Target:** DropAnywhere / BHA Onboarding | **Est. Completion:** 3-4 minutes

---

## The Problem

Traditional onboarding surveys are exhaustive (25+ sections, 100+ questions) and suffer from massive drop-off. People bounce before you capture the signal needed to personalize their experience.

## The Solution

A **"Human Insight Snapshot"** — a 3-4 minute micro-survey that trades breadth for depth. Captures the *essential* signals needed to:
- Route users to the right persona/AI assistant
- Personalize digest content and recommendations
- Build an initial "Intelligence Map" of who they are
- Surface relevant prompts, workflows, and connections

---

## The Snapshot (5 Sections, ~4 Minutes)

### 1. Your Links (30 seconds)
Drop links that represent you:
- Public profiles (LinkedIn, Twitter/X, personal site, portfolio)
- Content you vibe with (YouTube channels, podcasts, newsletters, creators)

*Why:* External context > self-reported identity. Links tell us more than checkboxes.

---

### 2. Bot Conversations You Love (60 seconds)
- **Drop 1-3 favorite AI responses** you've received — what made them land? *(screenshots, copy/paste, or describe the vibe)*
- **What were you wrestling with** when you asked? *(context = everything)*

*Why:* Shows us the *quality bar* for what "good" looks like to this user. Reveals emotional triggers and use cases.

---

### 3. Prompts That Hit Different (45 seconds)
- Share 2-3 prompts you return to or wish existed
- What do they unlock for you?

*Why:* Surfaces intent and workflow. Users who can't articulate this are likely casual; users who can are power users.

---

### 4. Your Operating System (60 seconds)
- **What are you building?** *(project, career, side hustle, creative pursuit — 1 sentence)*
- **What's the friction?** *(the thing you keep circling back to)*
- **What have you already solved?** *(a win that shaped you)*

*Why:* The "build/friction/solved" triad creates a narrative arc. Shows trajectory, blockers, and confidence level.

---

### 5. The Vibe Check (30 seconds)
Pick 3-5 tags that describe you:
```
[ ] founder        [ ] creative        [ ] parent
[ ] neurodivergent [ ] recovering perfectionist
[ ] multipotentialite                  [ ] recently laid off
[ ] rebuilding     [ ] scaling         [ ] exploring
[ ] other: ___________________
```

**One thing you're deeply curious about right now:**

*Bonus:* Drop a screenshot, link, or describe a piece of content that *feels* like you — OR name 3 artists/authors/personalities who shaped how you think.

*Why:* Tags enable filtering/segmentation. Curiosity signals direction. Cultural references unlock voice matching.

---

## Data Model

```json
{
  "snapshot": {
    "submitted_at": "ISO-8601",
    "completion_time_seconds": 240,
    "sections": {
      "links": {
        "profiles": ["url"],
        "content_vibes": ["url"]
      },
      "loved_conversations": [
        {
          "content": "string | screenshot_url",
          "context": "what they were wrestling with",
          "why_it_landed": "optional user description"
        }
      ],
      "favorite_prompts": [
        {
          "prompt": "string",
          "unlocks": "what it enables"
        }
      ],
      "operating_system": {
        "building": "string",
        "friction": "string",
        "solved": "string"
      },
      "vibe_check": {
        "tags": ["tag_id"],
        "curiosity": "string",
        "cultural_references": ["string"],
        "content_that_feels_like_me": "url | description"
      }
    },
    "derived": {
      "persona_match": ["persona_id"],
      "intelligence_map_seed": true,
      "archetype": "builder | explorer | resolver | creator"
    }
  }
}
```

---

## Integration Points

### Immediate (On Submit)
1. **Persona Routing:** Match to top 3 BHA personas based on tags + friction + curiosity
2. **Prompt Recommendations:** Surface 3 starter prompts from the "favorite prompts" taxonomy
3. **Intelligence Map:** Create initial "About Me" node in user's vault

### Ongoing (As System Learns)
1. **Digest Personalization:** Weight content by `building`, `friction`, `curiosity` signals
2. **Drop Suggestions:** Proactive prompts based on `operating_system.friction`
3. **Community Matching:** Connect users with similar `vibe_check.tags` + `cultural_references`

---

## Open Questions

1. **Incentivization:** Should completing the Snapshot unlock something? (Premium credits? Early access? Custom persona?)
2. **Optional vs Required:** Is this skippable? Partial credit if abandoned mid-way?
3. **Update Cadence:** Should users be prompted to refresh their Snapshot quarterly? After major life events?
4. **AI-Assisted Completion:** Could we pre-fill sections by scraping their links? (Privacy trade-off)
5. **Comparison to Passive Signals:** How much of this do we already capture from their first 10 drops?

---

## Related Documents

- `PRD-Action-Plan-latest.md` — Section on onboarding flow
- `docs/reference/BACKLOG.md` — Feature prioritization
- `specs/content-transformation-system-dec2025.md` — VAULT → GOLDMINE → FORGE → OUTPUT pipeline

---

**Next Steps:**
- [ ] Review with Joey for strategic fit
- [ ] Design wireframe for web implementation
- [ ] A/B test completion rates vs. traditional long-form survey
- [ ] Define derived signals / ML model for persona matching

---

*Filed: 2026-03-15 | Concept by Joey | Documented by Claw*
