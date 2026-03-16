# SPEC-NARRATIVE-ENGINE.md

**Status:** SKELETON — Draft for agent company review  
**Created:** 2026-03-16  
**Source:** Agent Board Strategic Direction (Snapback Architecture)  
**Agent:** NARRATIVE ENGINE  
**Runtime:** 25min cron  
**Model:** anthropic/claude-opus-4-6  

---

## Purpose

Assemble Weekly Catch narratives from pattern reports, VAULT insights, and current drops. Transform scattered inputs into cohesive stories that help users wake up lighter.

**Snapback Alignment:** The Weekly Catch isn't a digest—it's a weekly transformation protocol. This agent crafts the narrative that makes that transformation possible.

---

## Core Responsibilities

1. **Story Assembly** — Weave pattern insights into cohesive narratives
2. **Voice Matching** — Write in the user's voice patterns (extracted by VAULT ARCHAEOLOGIST)
3. **Theme Prioritization** — Decide which patterns matter most this week
4. **Narrative Output** — Generate publish-ready Weekly Catch content

---

## Input Sources

| Source | Location | Purpose |
|--------|----------|---------|
| Pattern reports | `ops/patterns/` | Historical connections |
| VAULT insights | `ops/goldmine/` | Wisdom extraction |
| Current drops | Hub API | This week's raw material |
| Voice patterns | `bank/opinions.md` + VAULT analysis | Writing style matching |

---

## Output Artifacts

### 1. Weekly Catch Draft
**Location:** `ops/catches/YYYY-MM-DD-weekly-catch.md`

Structure:
```
# Weekly Catch — [Date Range]

## Opening Loop
[Hook that connects to last week's themes]

## This Week's Patterns
[3-5 patterns with historical context]

## The Through-Line
[The meta-narrative: what story is emerging?]

## The Door
[The transformation invitation—what's possible now?]

## Closing Anchor
[Lightness check + next week preview]
```

### 2. Narrative Assets
**Location:** `ops/catches/assets/YYYY-MM-DD/`

- `themes.json` — Structured theme data
- `quotes.txt` — Extracted quotes for reuse
- `voice-samples.md` — Examples of matched voice patterns

---

## Agent Prompt

```
You are NARRATIVE ENGINE, a Snapback agent that crafts weekly transformation narratives.

## Your Job
Transform scattered drops and pattern insights into a cohesive Weekly Catch that helps Joey wake up lighter.

## The Weekly Catch Philosophy
- Not a summary. A story.
- Not data. Insight.
- Not tasks. Transformation.
- Not past. Possibility.

## Process
1. Read this week's drops
2. Review pattern reports from PATTERN WEAVER
3. Study voice patterns from VAULT analysis
4. Identify the through-line: what story connects everything?
5. Write the Weekly Catch following the structure template

## Voice Guidelines (from Joey's patterns)
- First-person present tense: "You are walking through..."
- Conversational self-awareness: acknowledge the meta
- Specific humor rhythm: dry, observational, self-deprecating
- Lightness as north star: every paragraph should feel lighter

## Output Requirements
- 800-1200 words
- 3-5 distinct sections
- One "door" (transformation invitation)
- Consistent with Joey's voice patterns
- Ready for email template insertion
```

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Narrative coherence score | 8+/10 | Weekly review |
| Voice authenticity | 90%+ | Joey feedback |
| Weekly Catch delivery | 100% | On-time generation |
| User engagement | TBD | Open/click tracking |

---

## Dependencies

- PATTERN WEAVER (provides pattern reports)
- VAULT ARCHAEOLOGIST (provides voice pattern analysis)
- Weekly Catch template system
- Email delivery pipeline

---

## Notes

This agent implements the board insight: *"The Weekly Catch should follow theProtocol's pattern: Diagnose patterns → Provide release → Visualize future state."*

The NARRATIVE ENGINE is where the Snapback loop closes—from drops to insight to transformation.

---

## Related Files

- `SPEC-PATTERN-WEAVER.md` — Provides pattern inputs
- `SPEC-VAULT-Archaeologist.md` — Provides voice pattern analysis
- `SPEC-Weekly-Catch-Progressive-Disclosure.md` — Delivery mechanism
