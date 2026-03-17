# SPEC — Intelligence Map Digest Email Template

**Status:** skeleton — needs Joey review
**Created:** 2026-03-17 by SpecBot
**Priority:** 🔴 CRITICAL — This is the entire product (per COMPASS v2026-03-17)
**Launch Target:** March 24, 2026
**Depends On:** COMPASS-MASTER-LAUNCH-BLUEPRINT-2026-03-16.md

---

## Why This Exists

The Intelligence Map Digest is **the product**. Per the email-only pivot:

> "An email-only Intelligence Map. Users email their thoughts to drop@drop-anywhere.com. AI extracts themes, finds connections, surfaces patterns. Users receive a beautiful digest email — their Intelligence Map — each morning."

This spec defines the structure, content, and rendering of that email.

---

## Core Promise

**"Drop it. Forget it. Wake up lighter."**

The email must deliver on this in a single glance.

---

## Digest Analyzer Styles

| Style | Key | Personality | Best For |
|-------|-----|-------------|----------|
| Clarity Engine | `clarity` | Organized themes, focus report | Scattered thinkers |
| Action Catch | `action` | Prioritized action items | Builders, operators |
| Pattern Mirror | `pattern` | Cross-drop thread detection | Explorers, creatives |
| Deep Mirror | `reflection` | No actions, just meaning | Processors, journalers |
| Adaptive | `adaptive` | System picks best mode | New users (default) |

---

## Email Structure

### Header
- Subject: `🗺️ Your Intelligence Map — {date}` (or style-specific variant)
- Preheader: `{X} drops → {N} themes found`
- From: `Drop <drop@drop-anywhere.com>`
- Brooke theme styling (cream/sage/copper, Newsreader font)

### Section 1: Map Summary
> *What your mind was working on*

- Drop count for period
- Top 3 themes (pill badges)
- Mood/energy reading (optional, if supported)
- Timespan covered

### Section 2: Intelligence Sections (style-dependent)

#### Clarity Engine
- **Themes** — grouped by topic, with source drops quoted briefly
- **Focus Report** — what got the most mental real estate
- **Unresolved** — questions/tensions still open

#### Action Catch
- **Priority Actions** — top 3, extracted from drops
- **Decisions Needed** — open questions requiring a choice
- **Quick Wins** — small items that could ship fast
- **Backlog Captures** — lower-priority ideas preserved

#### Pattern Mirror
- **Recurring Threads** — what keeps coming up across drops
- **New Connections** — links between topics (A → B)
- **Evolution** — how a theme has shifted over time
- **Signal vs Noise** — what seems important vs random

#### Deep Mirror
- **What you're really saying** — distilled meaning beneath the surface
- **Questions worth sitting with** — no answers, just the right questions
- **One line that captures it all** — the through-line of this period

### Section 3: Your Drops (Collapsed)
- List of drops sent this period (brief, collapsible if HTML supports)
- Timestamp + first 100 chars
- Encourages reflection on the raw input

### Section 4: CTA (Contextual)
- Trial users: "Reply to add more drops" or upgrade prompt
- Paid users: "Reply anytime" reinforcement
- No drop in 48h: gentle nudge variant

### Footer
- `Drop anything, anytime: drop@drop-anywhere.com`
- Unsubscribe / manage preferences
- "Powered by DropAnywhere 🦜" parrot footer

---

## Rendering Requirements

- **Framework:** Brooke Theme (cream/sage/copper, Newsreader)
- **Generator:** Puppeteer + Chrome headless for PDF version
- **Email client compatibility:** Gmail, Apple Mail, Outlook (basic)
- **No emojis in PDF variant** (headless Chrome lacks emoji fonts)
- **No gradient text** in email
- **Mobile-first:** must look great on iPhone Mail
- **Max width:** 600px
- **Dark mode:** basic support preferred

---

## API Contract (Hub → Email)

### Input (from Hub digest generator)
```json
{
  "user_id": "b419d8ad5d23513f",
  "period": "2026-03-16T00:00:00Z/2026-03-17T00:00:00Z",
  "style": "adaptive",
  "drops": [
    {
      "id": "...",
      "content": "...",
      "created_at": "...",
      "source": "email|api|sms"
    }
  ],
  "ai_output": {
    "themes": ["theme1", "theme2"],
    "summary": "...",
    "sections": { ... }   // style-dependent
  }
}
```

### Output
- Rendered HTML email string (Resend-ready)
- Plain text fallback
- Subject line + preheader

---

## Milestone Variants

| Milestone | Trigger | Variant |
|-----------|---------|---------|
| First map | First digest, 1+ drops | "Your first Intelligence Map" — extra context on what it means |
| 5 drops | Cumulative | Bonus: "Your map is getting interesting" banner |
| 10 drops | Cumulative | Bonus: Extended pattern analysis section |
| 25 drops | Cumulative | Bonus: Power dropper badge, deep connections |
| 50 drops | Cumulative | Full mind map section |

---

## Quality Criteria

- [ ] Joey approves template design (COMPASS go/no-go gate)
- [ ] Renders correctly in Gmail, Apple Mail
- [ ] Spam score 8/10+ (Resend/Mail-tester)
- [ ] All 5 analyzer styles render without errors
- [ ] Mobile layout looks correct on iPhone
- [ ] Adaptive style selects correct sub-template
- [ ] Milestone variants trigger correctly
- [ ] CTA links point to correct endpoints (email reply, upgrade page)

---

## Open Questions

1. **Style auto-selection logic** — How does `adaptive` pick? Based on what signals?
2. **Minimum drops threshold** — Send map if only 1 drop? 0 drops (skip or send placeholder)?
3. **Subject line variants** — A/B test different hooks, or single canonical?
4. **PDF attachment** — Does the digest ship as HTML-only or include PDF attachment?
5. **Frequency** — Always daily, or user-configurable (daily/weekly)?
6. **Real-time drop confirmations** — Separate from the daily map? (See COMPASS Email #3)
7. **Re-engagement digest** — Different template if user hasn't dropped in 72h?

---

## Related Files

- COMPASS-MASTER-LAUNCH-BLUEPRINT-2026-03-16.md — overall launch context
- ONBOARDING-FUNNEL-2026-03-16.md — 13-email sequence this lives within
- DIGEST-POLICY-2026-03-16.md — rules for when/how digests send
- EMAIL-STANDARDS-2026-03-16.md — Brooke theme standards
- SPEC-DigestBot.md — monitoring agent for digest pipeline
- `docs/templates/weekly-catch-email-template-2026-03-11.html` — closest existing template

---

## Next Steps

1. Joey reviews + fills Open Questions
2. Designer mocks 2-3 style variants (Clarity, Action, Pattern)
3. Dropper-Code implements Hub-side renderer
4. End-to-end test: drop → Hub → Intelligence Map → Resend → inbox
5. Joey approves before March 24 launch

---

*This spec was created by SpecBot on 2026-03-17 04:15 UTC.*
*It is a SKELETON — it needs Joey's review and iteration before implementation.*
