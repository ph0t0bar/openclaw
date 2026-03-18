# SPEC — Morning Brief Template Redesign

> **Status:** Skeleton Created  
> **Created:** 2026-03-18 00:28 UTC by SpecBot  
> **Priority:** 🚨 CRITICAL  
> **Source:** FeedbackBot Drop 1773770773644827, 1773771915612630  
> **Board Consensus:** 40+ votes across 14h of deliberation

---

## 1. Problem Statement

Current Morning Brief template is "not good looking" per Joey. Visual design IS product-market fit for consumer apps — users judge trustworthiness in 50ms. Current template actively damages brand perception and creates churn risk.

**User Feedback:**
- "Change template format to match beautiful designs from last night"
- "Not good looking — want Pinterest font, cute pills, stunning CSS, motion"
- Target emotion: "light and tingly"

---

## 2. Goals

| Goal | Metric |
|------|--------|
| Visual trust signal | 50ms positive first impression |
| Brand alignment | 100% Brooke Theme compliance |
| Emotional target | "Light and tingly" feeling |
| Churn prevention | 0% template-related unsubscribes |

---

## 3. Design System — Brooke Theme

**Existing Spec:** `workspace/templates/brooke-theme-spec.md`  
**Reference Implementation:** `temp-joey-backup/templates/brooke-demo-email.html` (600+ lines, production-ready)

### Palette
- **Cream** — Primary background
- **Sage** — Secondary accents  
- **Copper** — CTAs and highlights

### Typography
- **Newsreader** — Primary font (elegant, editorial)
- **System fallback** — sans-serif stack

### Effects
- **Liquid glass** — Subtle transparency/blur
- **Subtle motion** — Micro-interactions on hover
- **Cute pills** — Rounded tag/chip components

---

## 4. Technical Requirements

### Template Engine
- [ ] HTML email template (table-based for client compatibility)
- [ ] Inline CSS (no external stylesheets)
- [ ] Responsive breakpoints for mobile
- [ ] Dark mode support (`prefers-color-scheme`)

### Content Blocks
- [ ] Header with logo + date
- [ ] Greeting (personalized)
- [ ] Daily summary card (liquid glass effect)
- [ ] Drop highlights (cute pill tags)
- [ ] Insights section
- [ ] CTA footer
- [ ] Unsubscribe/legal footer

### Rendering
- [ ] Puppeteer PDF generation (headless Chrome)
- [ ] Resend email HTML delivery
- [ ] Plain text fallback

---

## 5. Implementation Plan

### Phase 1: Emergency Stop (Today)
- [ ] Disable current template in Hub (`DIGEST_SENDER_ENABLED=false`)
- [ ] Verify no accidental sends during redesign

### Phase 2: Template Build (Mar 18-19)
- [ ] Port brooke-demo-email.html to Hub template system
- [ ] Implement dynamic content injection
- [ ] Add personalization variables

### Phase 3: Testing (Mar 19)
- [ ] Render test to Joey only
- [ ] Cross-client testing (Gmail, Apple Mail, Outlook)
- [ ] Mobile responsive verification

### Phase 4: Deploy (Mar 20)
- [ ] Enable new template with feature flag
- [ ] Monitor first sends
- [ ] Gather feedback loop

---

## 6. Dependencies

| Dependency | Status | Blocker? |
|------------|--------|----------|
| Brooke Theme spec | ✅ Exists | No |
| Reference HTML | ✅ Exists | No |
| Digest pipeline | 🟡 Claude limits (resets Mar 20) | Yes — wait for reset |
| Hub template system | 🟡 Needs review | TBD |

---

## 7. Open Questions

1. Should we A/B test new template vs. old (once pipeline fixed)?
2. What's the rollout strategy — all users or gradual?
3. Do we need a "degraded mode" template for pipeline failures?
4. How to handle dark mode preference detection?

---

## 8. Success Criteria

- [ ] Joey approves visual design
- [ ] Zero template-related complaints
- [ ] Unsubscribe rate < 0.5% on first send
- [ ] Renders correctly in Gmail, Apple Mail, Outlook

---

## 9. Related

- **Brooke Theme Spec:** `workspace/templates/brooke-theme-spec.md`
- **Reference HTML:** `temp-joey-backup/templates/brooke-demo-email.html`
- **Digest Pipeline Issue:** See PRD Section 8 (2/107 users receiving digests)
- **Agent Board:** `ops/agent-board.md` (40+ votes on this topic)

---

*Skeleton created by SpecBot. Needs: technical review, Hub integration plan, testing strategy.*
