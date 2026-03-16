# Weekly Catch — Visual Style Guide

**Template:** `template.html`  
**Theme:** Brooke (warm editorial)

This is the **visual wrapper only**. Content structure, narrative voice, analyzer selection, and personalization are determined by the Hub's digest/Snapback pipeline based on drop context, user feedback, and analysis mode.

---

## Colors

| Token | Hex | Usage |
|-------|-----|-------|
| `soft-black` | `#2D2A26` | Body text, headings |
| `muted` | `#9B9590` | Date labels, captions, secondary text |
| `copper` | `#C4A484` | Accent lines, links, neutral callout borders |
| `sage` | `#A8B5A0` | Positive metrics, quote borders, success callouts |
| `rose` | `#D4A5A5` | Warning/attention callout borders |
| `cream-fill` | `#F4F1EC` | Callout box backgrounds |
| `separator` | `#D5CEC5` | Horizontal rules, table bottom borders |
| `table-border` | `#E8E2DA` | Table row borders |

## Typography

| Element | Font | Size | Weight | Notes |
|---------|------|------|--------|-------|
| Title | Georgia, serif | 28px | 400 | -0.5px letter-spacing |
| Date | system sans | 12px | 400 | uppercase, 2px tracking |
| Section headers | Georgia, serif | 20px | 500 | |
| Body | Georgia, serif | 16px | 400 | 1.7 line-height |
| Tables | system sans | 13px | 400 | |
| Table headers | system sans | 11px | 400 | uppercase, 1px tracking, muted |
| Callout text | system sans | 13px | 400 | 1.6 line-height |
| Pull quotes | Georgia, serif | 15px | 400 | italic, 1.55 line-height |

## Layout

- **Max width:** 600px centered
- **Padding:** 40px top/bottom, 24px sides
- **Body line-height:** 1.7

---

## Components

### Watercolor Accent Bar
Always at the top. Sage → cream → copper → rose gradient, 6px tall, 70% opacity.
```html
<div style="width: 100%; height: 6px; background: linear-gradient(to right, #A8B5A0 0%, #B5BFA8 18%, #C9C4B0 32%, #D4B8A0 48%, #D4A5A5 62%, #C9B5A8 78%, #BDB8A5 100%); opacity: 0.7; margin-bottom: 32px;"></div>
```

### Metrics Table
Week-over-week with delta column. Copper header border. Sage for positive deltas.
```html
<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, sans-serif; font-size: 13px; margin: 16px 0;">
  <tr style="border-bottom: 2px solid #C4A484;">
    <th style="text-align: left; padding: 8px 12px; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #9B9590;"></th>
    <th style="text-align: right; ...">Previous</th>
    <th style="text-align: right; ...">Current</th>
    <th style="text-align: right; ..."></th>
  </tr>
  <tr>
    <td style="padding: 8px 12px; border-bottom: 1px solid #E8E2DA;">Label</td>
    <td style="text-align: right; padding: 8px 12px; border-bottom: 1px solid #E8E2DA;">old</td>
    <td style="text-align: right; padding: 8px 12px; border-bottom: 1px solid #E8E2DA; font-weight: 600;">new</td>
    <td style="text-align: right; padding: 8px 12px; border-bottom: 1px solid #E8E2DA; color: #A8B5A0;">+delta</td>
  </tr>
</table>
```

### Pull Quote
User's own words, sage border. Use `#C4A484` border for non-user quotes.
```html
<div style="border-left: 3px solid #A8B5A0; padding-left: 20px; margin: 28px 0;">
  <p style="font-family: Georgia, serif; font-style: italic; font-size: 15px; line-height: 1.55; color: #2D2A26;">"Their words."</p>
</div>
```

### Callout Boxes
Three border colors by intent:

| Intent | Border Color | When |
|--------|-------------|------|
| **Rose** | `#D4A5A5` | Fixes, warnings, blockers |
| **Copper** | `#C4A484` | Decisions, neutral actions |
| **Sage** | `#A8B5A0` | Momentum, completed, positive |

```html
<div style="background: #F4F1EC; border-radius: 6px; padding: 16px 20px; margin: 16px 0; border-left: 4px solid #A8B5A0;">
  <p style="font-family: -apple-system, sans-serif; font-size: 13px; margin: 0; line-height: 1.6;"><strong>Text.</strong></p>
</div>
```

### Bottom Accent
```html
<div style="text-align: center; margin-top: 32px;">
  <div style="width: 40px; height: 2px; background: #C4A484; margin: 0 auto;"></div>
</div>
```

---

## Rules

- No emoji (headless Chrome can't render them in PDF exports)
- Closing line is always: *"Drop everything else. Catch it Sunday."*
- Max 3 callout boxes per email
- Metrics table: 4-7 rows max
- Pull quotes: always the user's actual words from their drops

---

*Format approved by Joey, March 15, 2026.*

