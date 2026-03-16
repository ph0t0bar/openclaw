# PRD: Desktop vs Mobile App Differentiation

**Product:** DropAnywhere (drop-anywhere.com)  
**Author:** OpenClaw (on behalf of Joey Hamer)  
**Date:** 2026-03-10  
**Status:** Draft  
**Target Repo:** `ph0t0bar/dropanywhere-app` (Next.js 14, Pages Router)

---

## 1. Core Insight

> "It's not just desktop/mobile onboarding — it's having the desktop version of the app versus the mobile version. Mobile should not be treated the same."  
> — Joey Hamer

**DropAnywhere is two different products sharing one codebase.**

On desktop, Joey sits down, opens the vault, reads his digest, explores connections in the intelligence map, tweaks settings — it's a *reflection studio*. The screen real estate invites depth. You linger. You think.

On mobile, you had a thought in the shower, an idea on the train, a voice memo while walking the dog. You open the app, drop it, close the app. Done. *Capture instrument.* Three seconds, tops.

Today, the app serves the identical experience to both form factors. Responsive CSS adapts the layout, but the *product* doesn't adapt. A mobile user sees the same intelligence map, the same settings panel, the same nav structure as desktop. This is wrong. It creates friction on mobile (too much surface area) and undersells desktop (doesn't leverage the space).

**Product philosophy:** *"Drop it. Forget it. Wake up lighter."*

- **Mobile** fulfills "Drop it. Forget it." — the capture half.
- **Desktop** fulfills "Wake up lighter." — the reflection half.

---

## 2. Mobile Experience Spec

### 2.1 What Mobile IS

A **capture instrument**. The fastest path from thought → drop. Nothing else matters on this screen size.

### 2.2 What to Show

| Element | Behavior |
|---------|----------|
| **Drop input** | Hero element. Full-width, always visible, auto-focused on launch. Big, inviting, impossible to miss. |
| **Voice button** | Prominent — one-tap voice capture. Microphone icon, hold-to-record or tap-to-toggle. |
| **Camera button** | Quick photo/screenshot capture. Opens native camera picker. |
| **Recent drops** | Minimal list (last 3-5) below the input, for reassurance ("yes, your stuff is here"). |
| **Vault** | Simplified — scrollable list view, search bar, no grid/card layout. |
| **Digest** | Read-only. Today's digest, clean and scrollable. No editing, no history browser. |
| **Bottom tab bar** | 3 tabs: **Drop** (home), **Vault**, **Digest** |

### 2.3 What to Hide on Mobile

- ❌ Intelligence Map (too complex for small screens; defer to desktop)
- ❌ Settings panel (accessible via profile icon → modal, not a main nav item)
- ❌ Sidebar navigation
- ❌ Digest history browser (just show today's / most recent)
- ❌ Advanced vault filters
- ❌ Context bank editor
- ❌ Analytics / stats dashboards

### 2.4 Interaction Patterns

- **Quick capture flow:** Open → type/speak/snap → auto-save → haptic feedback → done
- **Voice-first:** Prominent mic button. Dictation should feel native (use Web Speech API or native input).
- **Camera capture:** Photo drops — snap, optional caption, drop it.
- **Share sheet integration:** Accept text/images/URLs from other apps via Web Share Target API (PWA).
- **Pull-to-refresh** on vault and digest.
- **Swipe gestures:** Swipe left on a drop to delete, swipe right to star/pin.
- **No modals for primary actions.** Drop creation is inline, not modal.
- **Auto-dismiss keyboard** after drop is submitted. Smooth return to empty state.

### 2.5 Mobile Visual Language

- Large touch targets (min 48px)
- High contrast, minimal chrome
- Single-column layout always
- Generous whitespace — breathe
- Subtle animations on drop submission (checkmark fade, gentle bounce)
- Dark mode support (follow system preference)

---

## 3. Desktop Experience Spec

### 3.1 What Desktop IS

A **reflection studio**. Where you process, review, connect, and configure. The place you come to *after* the drops have landed.

### 3.2 What to Surface

| Element | Behavior |
|---------|----------|
| **Sidebar navigation** | Persistent left sidebar: Drop, Vault, Intelligence Map, Digests, Context Bank, Settings |
| **Drop input** | Available but not the hero. Sidebar shortcut or top-bar quick-drop. Desktop users drop too, but it's not the *only* thing. |
| **Vault dashboard** | Rich grid/card view with filters, tags, date ranges, search. Multi-select, bulk actions. |
| **Intelligence Map** | Full visualization — connections between drops, themes, clusters. Interactive, zoomable. |
| **Digest history** | Browse past digests by date. Compare, re-read, track themes over time. |
| **Settings** | Full settings panel: notification preferences, digest timing, connected accounts, context bank management. |
| **Context Bank** | View and edit the AI context that shapes digests. Add life context, goals, preferences. |
| **Reflection tools** | Long-form journaling input, weekly summaries, trend spotting. |
| **Stats / Analytics** | Drop frequency, category breakdown, streak tracking. |

### 3.3 Desktop Visual Language

- Multi-column layouts (sidebar + main + optional detail panel)
- Hover states, tooltips, keyboard shortcuts
- Dense information display (more data per screen)
- Drag-and-drop for vault organization
- Resizable panels
- Command palette (⌘K) for power users

### 3.4 Desktop-Only Features

- Intelligence Map (complex visualization)
- Digest history browser with date picker
- Context Bank editor
- Bulk vault operations
- Settings panel as main nav item
- Keyboard shortcuts overlay
- Analytics dashboard

---

## 4. Navigation Differences

### Mobile: Bottom Tab Bar

```
┌─────────────────────────────┐
│                             │
│      [Content Area]         │
│                             │
├─────────┬─────────┬─────────┤
│  ✏️ Drop │ 📦 Vault│ 📬 Digest│
└─────────┴─────────┴─────────┘
```

- **3 tabs only.** Drop (default/home), Vault, Digest.
- Profile/settings accessible via avatar icon in top-right corner → slides in a sheet.
- Active tab highlighted. Badge on Digest tab when new digest available.

### Desktop: Persistent Sidebar

```
┌──────────┬──────────────────────────┐
│ 🦜 DA    │                          │
│──────────│                          │
│ ✏️ Drop   │      [Content Area]      │
│ 📦 Vault  │                          │
│ 🗺️ Map    │                          │
│ 📬 Digests│                          │
│ 🧠 Context│                          │
│ ⚙️ Settings│                          │
│          │                          │
│ [Avatar] │                          │
└──────────┴──────────────────────────┘
```

- Full navigation always visible.
- Collapsible sidebar (icon-only mode) for more content space.
- Quick-drop shortcut in top bar regardless of active page.

---

## 5. Technical Approach

### 5.1 Strategy: Responsive Layouts + Feature Gating (NOT separate apps)

We keep one codebase, one deployment, one URL. The differentiation happens at the component level through a combination of:

1. **`useIsMobile()` hook** — client-side device detection via media query
2. **CSS media queries** — for purely visual differences
3. **Conditional rendering** — for feature-level differences (show/hide entire sections)

### 5.2 The Hook: `useIsMobile()`

```tsx
// hooks/useIsMobile.ts
import { useEffect, useState } from 'react';

const MOBILE_BREAKPOINT = 768; // px

export function useIsMobile(): boolean {
  const [isMobile, setIsMobile] = useState(false);

  useEffect(() => {
    const mql = window.matchMedia(`(max-width: ${MOBILE_BREAKPOINT}px)`);
    const handler = (e: MediaQueryListEvent) => setIsMobile(e.matches);
    setIsMobile(mql.matches);
    mql.addEventListener('change', handler);
    return () => mql.removeEventListener('change', handler);
  }, []);

  return isMobile;
}
```

### 5.3 Layout Architecture

```
pages/
├── _app.tsx          ← wraps with <AppShell> that reads useIsMobile()
├── index.tsx         ← drop page (both platforms, different layouts)
├── vault.tsx         ← vault (simplified on mobile, rich on desktop)
├── digest.tsx        ← digest view
├── map.tsx           ← desktop only (redirect or hide on mobile)
├── settings.tsx      ← desktop: full page; mobile: bottom sheet from profile
└── context.tsx       ← desktop only

components/
├── layout/
│   ├── AppShell.tsx       ← orchestrates mobile vs desktop layout
│   ├── Sidebar.tsx        ← desktop only
│   ├── BottomTabBar.tsx   ← mobile only
│   ├── MobileHeader.tsx   ← mobile top bar
│   └── DesktopTopBar.tsx  ← desktop top bar with quick-drop
├── drop/
│   ├── DropInput.tsx      ← shared, but sized differently
│   ├── MobileDropHero.tsx ← full-screen capture mode
│   └── DesktopDropCard.tsx← compact sidebar/card version
├── vault/
│   ├── VaultGrid.tsx      ← desktop: grid with filters
│   └── VaultList.tsx      ← mobile: simple scrollable list
└── shared/
    └── DeviceGate.tsx     ← <DesktopOnly>, <MobileOnly> wrappers
```

### 5.4 DeviceGate Components

```tsx
// components/shared/DeviceGate.tsx
import { useIsMobile } from '@/hooks/useIsMobile';

export function MobileOnly({ children }: { children: React.ReactNode }) {
  const isMobile = useIsMobile();
  if (!isMobile) return null;
  return <>{children}</>;
}

export function DesktopOnly({ children }: { children: React.ReactNode }) {
  const isMobile = useIsMobile();
  if (isMobile) return null;
  return <>{children}</>;
}
```

### 5.5 Why NOT Separate Codebases / Routes

- **One codebase** = one deployment, one set of APIs, one auth flow
- Pages Router already supports conditional rendering fine
- Shared state (auth, user data, drops) stays unified
- SEO: same URLs for both (no `/m/` prefix nonsense)
- Progressive — features can migrate between platforms as the product evolves

### 5.6 SSR Considerations

`useIsMobile()` runs client-side only (`useEffect`). For SSR:
- Default to desktop layout on server (most crawlers are desktop)
- Use `User-Agent` sniffing in `getServerSideProps` for critical above-the-fold differences
- Hydration mismatch is minimal since the structural difference is conditional `display: none` / component mounting

---

## 6. Implementation Phases

### Phase 1: Quick Wins — Hide/Show (1-2 weeks)

**Goal:** Make mobile feel capture-first by hiding desktop features. No new components needed.

| Task | Detail |
|------|--------|
| Create `useIsMobile()` hook | Media query based, 768px breakpoint |
| Create `<MobileOnly>` / `<DesktopOnly>` wrappers | Conditional rendering gates |
| Hide Intelligence Map on mobile | Wrap map section in `<DesktopOnly>` |
| Hide Settings from mobile main nav | Move to profile menu / bottom sheet |
| Hide Context Bank on mobile | Desktop-only feature |
| Add bottom tab bar on mobile | 3 tabs: Drop, Vault, Digest. CSS-hidden on desktop. |
| Hide sidebar on mobile | Already likely responsive, but enforce it |
| Make Drop input the hero on mobile | Full-width, auto-focus, prominent voice/camera buttons |
| Simplify Vault on mobile | List view only, hide grid toggle and advanced filters |

**Success metric:** Mobile user can drop in < 3 seconds. Desktop user sees full feature set.

**LHFPLR score:** 🔥🔥🔥 (high impact, low effort — mostly CSS + conditional wrappers)

### Phase 2: Layout Divergence (2-4 weeks)

**Goal:** Distinct layout systems for each platform.

| Task | Detail |
|------|--------|
| `AppShell` component | Renders `<MobilLayout>` or `<DesktopLayout>` based on device |
| Desktop sidebar | Persistent, collapsible, full nav |
| Mobile header | Minimal — logo, avatar, notification bell |
| Desktop vault redesign | Grid cards, filters sidebar, bulk actions |
| Mobile vault redesign | Single-column list, pull-to-refresh, swipe actions |
| Desktop digest browser | Date picker, history timeline, compare mode |
| Mobile digest view | Today only, clean scroll, share button |
| Desktop quick-drop in top bar | Always-accessible drop input in desktop header |

### Phase 3: Mobile-Native Features (4-8 weeks)

**Goal:** Make mobile feel like a native app.

| Task | Detail |
|------|--------|
| PWA manifest + service worker | Install to home screen, offline drop queue |
| Web Share Target API | Accept shares from other apps |
| Voice-first capture | Tap mic → dictate → auto-submit. Native-feeling. |
| Camera capture | Photo drops with optional caption |
| Haptic feedback | `navigator.vibrate()` on drop submission |
| Offline drop queue | Store drops in IndexedDB, sync when online |
| Push notifications | New digest available, weekly summary |
| Mobile-optimized onboarding | 3-screen swipe: "Drop it → Forget it → Wake up lighter" |

### Phase 4: Desktop Power Features (future)

| Task | Detail |
|------|--------|
| Command palette (⌘K) | Quick access to any feature |
| Keyboard shortcuts | Navigation, drop creation, vault search |
| Drag-and-drop vault | Organize drops manually |
| Split-pane views | Vault + detail side-by-side |
| Desktop widgets | Pinned stats, recent drops, digest preview |

---

## 7. Metrics & Success Criteria

| Metric | Target | How |
|--------|--------|-----|
| Mobile time-to-drop | < 3 seconds from app open | Analytics event timing |
| Mobile bounce rate | Decrease 20% | Fewer users overwhelmed by features |
| Desktop session length | Increase 15% | More to explore, more reason to stay |
| Desktop feature discovery | Intelligence Map usage +30% | Prominent in sidebar |
| Mobile daily active drops | Increase 25% | Lower friction = more drops |

---

## 8. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Hydration mismatch (SSR vs client) | Default to desktop on server; client overrides on mount. Minimal flash. |
| Maintaining two "products" in one codebase | DeviceGate components keep concerns separated. Shared logic stays shared. |
| Breakpoint edge cases (tablets, landscape phones) | 768px is the line. Tablets get desktop experience (they have the screen space). |
| Scope creep across phases | Strict phase boundaries. Phase 1 is hide/show ONLY. No new components. |

---

## 9. Open Questions

1. **Tablet behavior:** Default to desktop? Or a third tier? → **Recommendation:** Desktop. Tablets have screen space.
2. **PWA timeline:** Phase 3 includes PWA features. Is there appetite to accelerate? Share Target would be high-impact for mobile capture.
3. **Voice capture implementation:** Web Speech API vs third-party? Web Speech API is free but inconsistent across browsers.
4. **Digest frequency on mobile notifications:** Daily? Or let user configure?

---

## 10. References

- **Repo:** `ph0t0bar/dropanywhere-app`
- **Stack:** Next.js 14, Pages Router, TypeScript
- **Live:** https://drop-anywhere.com
- **Backend:** oPOErator Hub (`hub-production-f423.up.railway.app`)
- **Related:** [DropAnywhere Product Philosophy](https://drop-anywhere.com)

---

*"The phone is for dropping. The laptop is for thinking. Same product, different posture."*
