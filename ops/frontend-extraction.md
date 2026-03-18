# Frontend Extraction (dropanywhere-app)

**Extracted:** 2026-03-17 (agent hit context limits, partial extraction)

## Brooke Theme — Design System (globals.css)

### Color Palette
```css
--cream: #FAF8F5;
--warm-white: #FFFEFA;
--soft-black: #2D2A26;
--muted: #8B8680;
--accent: #C4A484;
--accent-light: #E8DFD5;
--rose: #D4A5A5;
--sage: #A8B5A0;
--deep-sage: #8B9D83;
```

### Semantic Colors (Light Mode)
```css
--background-primary: #FAF8F5;
--background-secondary: #FFFEFA;
--background-tertiary: #E8DFD5;
--label-primary: #2D2A26;
--label-secondary: #8B8680;
--label-tertiary: rgba(45, 42, 38, 0.5);
--separator: rgba(44, 36, 32, 0.04);
--fill-primary: rgba(139, 134, 128, 0.08);
--fill-secondary: rgba(139, 134, 128, 0.05);
```

### Shadow System
```css
--shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
--shadow-md: 0 1px 4px rgba(0, 0, 0, 0.04), 0 4px 12px rgba(0, 0, 0, 0.03);
--shadow-lg: 0 2px 8px rgba(0, 0, 0, 0.06), 0 8px 24px rgba(0, 0, 0, 0.05);
--shadow-hover: 0 4px 16px rgba(0, 0, 0, 0.08), 0 2px 4px rgba(0, 0, 0, 0.08);
```

### Elevation System
```css
--elevation-card: 0 1px 3px rgba(0,0,0,0.04), 0 2px 8px rgba(0,0,0,0.02);
--elevation-card-hover: 0 2px 8px rgba(0,0,0,0.06), 0 8px 24px rgba(0,0,0,0.04);
--elevation-modal: 0 8px 32px rgba(0,0,0,0.12), 0 2px 8px rgba(0,0,0,0.08);
```

### Typography Scale
```css
--text-display: 28px;
--text-title1: 22px;
--text-title2: 17px;
--text-body: 15px;
--text-callout: 13px;
--text-caption: 11px;
```

### 8pt Spacing Grid
```css
--space-xxs: 4px; --space-xs: 8px; --space-sm: 12px;
--space-md: 16px; --space-lg: 24px; --space-xl: 32px;
--space-xxl: 48px; --space-xxxl: 64px;
```

### Fonts
- Sans: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', system-ui, sans-serif
- Serif: 'Newsreader', Georgia, serif
- Mono: ui-monospace, SFMono-Regular, monospace

### Tailwind Palette (tailwind.config.js)
```js
cream: '#FAF8F5',
'warm-white': '#FFFEFA',
'soft-black': '#2D2A26',
sage: '#A8B5A0',
copper: '#C4A484',
rose: '#D4A5A5',
```

## TODO: Still needs extraction
- Landing page component (page.tsx) — hit context limit
- Intelligence Map component
- Digest display components
- Onboarding flow
- Settings pages
