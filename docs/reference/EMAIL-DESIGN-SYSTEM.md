# Email Design System — globals.css → Email Translation

**Last Updated:** 2026-03-17  
**Source:** DropAnywhere globals.css + Poe research (Apple Mail optimization)  
**Standard:** Every email from hello@drop-anywhere.com MUST follow this.

---

## Color Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `--cream` | `#FAF8F5` | Page/body background |
| `--warm-white` | `#FFFEFA` | Card backgrounds |
| `--soft-black` | `#2D2A26` | Primary text, dark hero BG |
| `--muted` | `#8B8680` | Secondary text, labels |
| `--accent` | `#C4A484` | Warm highlight numbers |
| `--accent-light` | `#E8DFD5` | Subtle tint backgrounds |
| `--rose` | `#D4A5A5` | Emotional/personal theme tags |
| `--sage` | `#A8B5A0` | Growth/clarity theme tags |
| `--system-green` | `#34C759` | Success states |
| `--system-red` | `#FF3B30` | Blocked/critical alerts |

## Typography
- **Font stack:** `-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif`
- **NO Georgia/serif** for user-facing emails
- Headlines: 28-34px, font-weight 700, letter-spacing -0.7px to -1px
- Body: 14-16px, line-height 1.52-1.58
- Labels: 10px, font-weight 700, letter-spacing 1px, uppercase

## Layout
- **Max width:** 580px (not 600 — breathes better)
- **Border radius:** 22px cards, 16px stat cards, 100px buttons, 30px pills
- **Shadows:** `0 1px 4px rgba(0,0,0,0.04), 0 6px 16px rgba(0,0,0,0.03)`
- **Borders:** `0.5px solid rgba(139,134,128,0.13)` (hairline)
- **Dividers:** `0.5px solid rgba(139,134,128,0.1)`
- **Table-based layout** (no flexbox — Outlook compat)

## Dark Mode (Apple Mail 70% adoption)
```css
@media (prefers-color-scheme: dark) {
  body { background: #1C1A17 !important; }
  .card-bg { background: #242220 !important; }
  .hero-bg { background: linear-gradient(150deg, #1C1A17, #2A2724) !important; }
  .label-primary { color: #FFFEFA !important; }
  .label-secondary { color: rgba(255,254,250,0.5) !important; }
  .label-muted { color: rgba(255,254,250,0.35) !important; }
}
```

## Components

### Dark Hero Card
- Background: `linear-gradient(150deg, #2D2A26, #3A3733)`
- Text: `#FFFEFA` (primary), `rgba(255,254,250,0.48)` (secondary)
- Accent numbers: `#C4A484`

### Stat Cards (4-up row)
- Individual white cards with subtle shadow
- Number: 26px, weight 700
- Label: 10px uppercase muted

### Pill Badges
- Background: `rgba(color, 0.14)`, text: darker shade
- Padding: 2-5px 9-13px, border-radius: 30px
- Sage: `rgba(168,181,160,0.14)` / `#4E7047`
- Accent: `rgba(196,164,132,0.14)` / `#7A5A30`
- Rose: `rgba(212,165,165,0.14)` / `#8B4F4F`

### Signal/Nudge Card
- Background: `linear-gradient(135deg, rgba(168,181,160,0.08), rgba(196,164,132,0.06))`
- Border: `0.5px solid rgba(168,181,160,0.21)`

### CTA Buttons
- Primary: `#2D2A26` bg, `#FFFEFA` text, `border-radius: 100px`, `padding: 16px 36px`
- Secondary: `#A8B5A0` bg (sage)
- Min tap target: 44x44pt (Apple HIG)
- Full-width on mobile via `@media`

### Footer (REQUIRED on every email)
- Tagline: "Drop it. Forget it. Wake up lighter."
- Parrot: 🦜
- Contact: hello@drop-anywhere.com
- Legal: DropAnywhere · Chicago, IL · USA
- Links: Unsubscribe · Email Preferences · Privacy Policy
- Color: `rgba(139,134,128,0.6)` for text, `0.7` for links

## Constraints
- Inline CSS only (email clients strip `<style>` blocks — keep `<style>` for dark mode + responsive only)
- No flexbox in layout (use `<table role="presentation">`)
- No JavaScript
- No CSS variables (use hex values)
- No backdrop-filter (use solid backgrounds)
- Gmail clips at 102KB — keep under 70KB target
- `role="presentation"` on all layout tables
- `alt=""` on all images
- Preheader text on every email (hidden div)

## Template Variables
All use `{{double_brace}}` format:
- `{{first_name}}`, `{{drop_count}}`, `{{theme_count}}`
- `{{clarity_pct}}`, `{{streak_days}}`
- `{{theme_N_name}}`, `{{theme_N_insight}}`, `{{theme_N_emoji}}`, `{{theme_N_count}}`
- `{{ai_signal_quote}}`
- `{{drop_N_content}}`, `{{drop_N_time}}`, `{{drop_N_theme}}`, `{{drop_N_emoji}}`
- `{{vault_url}}`, `{{upgrade_url}}`
- `{{unsubscribe_url}}`, `{{prefs_url}}`, `{{privacy_url}}`
