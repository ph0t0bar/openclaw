# DropAnywhere Frontend — Code Map

**Last Updated:** 2026-03-17 05:53 CDT  
**Source:** `ph0t0bar/dropanywhere-app` (Next.js 14, main branch)  
**Status:** FROZEN for dashboard features (email-only pivot, March 2026)  
**Author:** Claw

---

## Overview

The frontend was a full dashboard app (Next.js 14, Tailwind CSS, Framer Motion). With the email-only pivot, it's being stripped to a static landing page + waitlist. Dashboard code preserved in `phase-2/dashboard` branch.

---

## Key Component Files

### Intelligence (the crown jewel)

| File | Lines | Purpose |
|------|-------|---------|
| `components/IntelligenceView.tsx` | 828 | Interactive intelligence map rendering |
| `pages/api/intelligence/index.ts` | ~30 | Proxy to Hub `/api/intelligence/{userId}` |
| `pages/api/intelligence/assess.ts` | — | Intelligence assessment endpoint |
| `pages/api/thought-map/extract-intelligence.ts` | ~200 | Gemini-3-Flash extraction (richer schema) |

**IntelligenceView features:**
- 5 collapsible sections (Active Projects, Open Questions, Reminders & Tasks, Key Ideas, Actions)
- Expandable card grid with Framer Motion animations
- PARA tag system (Projects/Areas/Resources/Archives) with colored badges
- Source origin badges (email, SMS, voice, web, etc.)
- Emotion badges with intensity %
- Confidence bars
- Complete/archive/copy actions
- Vault action integration
- Brooke Theme design tokens

### Design System (Brooke Theme)

| Token | Description |
|-------|-------------|
| `--warm-white` | Card/surface backgrounds |
| `--accent` | Caramel/copper accent (Active Projects) |
| `--accent-light` | Borders, muted backgrounds |
| `--sage` | Green (in progress, tags, positive) |
| `--rose` | Dusty rose (questions, attention needed) |
| `--soft-black` | Near-black text |
| `--muted` | Gray-brown metadata text |

**Typography:** Serif (Georgia fallback) for headings, system sans-serif for body.  
**Icons:** Lucide React (Rocket, HelpCircle, Bell, Lightbulb, Zap, etc.)  
**Animations:** Framer Motion (AnimatePresence, motion.div, layout animations)

### Types

**IntelligenceItem:** (from `@/types/thought-map`)
```typescript
interface IntelligenceItem {
  id: string;
  title: string;
  summary: string;
  category: IntelligenceCategory; // 'active_project' | 'open_question' | 'reminder_task' | 'key_idea' | 'action'
  status?: string;
  urgency?: string;
  due_hint?: string;
  strength?: string;
  priority?: string;
  confidence?: number;
  source_drop_ids: string[];
  emotion?: EmotionLabel;
  intensity?: number;
  related_items?: string[];
  topic_tags?: string[];
}

type EmotionLabel = 'frustrated' | 'anxious' | 'stuck' | 'hopeful' | 'energized' | 'neutral';
type IntelligenceCategory = 'active_project' | 'open_question' | 'reminder_task' | 'key_idea' | 'action';
```

### PARA System

**File:** `@/lib/para`

| Type | Color (bg) | Color (text) | Color (dot) |
|------|-----------|-------------|-------------|
| Project | — | — | — |
| Area | — | — | — |
| Resource | — | — | — |
| Archive | — | — | — |

Tags matching PARA format get special colored badges. Clickable to navigate to PARA project view.

---

## What Gets Cut (Email-Only Pivot)

~85 files, ~41K lines → stripped to ~10 files, ~2K lines

| Feature | Est Hours | Status |
|---------|-----------|--------|
| Vault view (search, browse, filter) | 20h | CUT |
| Intelligence Map tab | 16h | CUT |
| Stream view | 12h | CUT |
| Settings page | 10h | CUT |
| Auth flows (login, signup, password reset) | 12h | CUT |
| Mobile app shell / PWA | 15h | CUT |
| Onboarding wizard | 8h | CUT |
| Theme customization UI | 6h | CUT |
| Dashboard navigation | 4h | CUT |
| **TOTAL SAVED** | **~103 hours** | |

---

## What Stays (Landing Page)

- Static landing page with waitlist form
- Brooke Theme styling
- Email capture → Hub webhook
- "Drop it. Forget it. Wake up lighter." messaging
- MEGA campaign visual identity

---

## Recent Shipping Sprint (Mar 13-14)

Via Claude Code Local:
- Dead features removed (6 tabs, 220+ lines)
- Catches merged INTO Digests with Daily/Weekly toggle
- Command Center Phase 2 (5/8 gaps closed)
- Activity section removed from Stream
- Settings flattened (11→7 sections)
- Intelligence drop caps removed (30→200 default, 50→500 max)

---

*This is a living reference. Dashboard code preserved in phase-2/dashboard branch.*
