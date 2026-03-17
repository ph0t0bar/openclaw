# COMPASS — DropAnywhere Strategic North Star

**Version:** 2026-03-16-v1 (Email-Only Pivot)
**Status:** APPROVED by Joey — this supersedes PRD.md for launch decisions
**Next Review:** Post-launch (Mar 31, 2026)

---

## The Product (Email-Only)

**What we ship:** Intelligence delivered as email. No dashboard at launch.

- **Capture:** Users email drop@drop-anywhere.com
- **Process:** AI extracts themes, finds connections, surfaces patterns
- **Deliver:** Intelligence Map sent as beautiful digest email
- **Frequency:** Daily or weekly (user chooses)
- **Frontend:** Static landing page + waitlist signup only

**Core Promise:** "Drop it. Forget it. Wake up lighter."

---

## The Three Launch Deliverables

| Deliverable | Owner | Deadline | Status |
|-------------|-------|----------|--------|
| Intelligence Map Email Template | Drop | Mar 20 | ⬜ Not started |
| 3-Email Admission Sequence | Drop | Mar 21 | ⬜ Not started |
| Static Landing Page | Dropper-Code | Mar 22 | ⬜ Not started |

---

## Strategic Decisions (The 5 Questions)

### 1. TRIAGE SYSTEM
**Decision:** Automated routing with manual override

**How it works:**
- All inbound → `drop@drop-anywhere.com`
- Hub webhook → instant processing (PR #193)
- Classification: drop vs support vs billing vs personal
- Routing: digest queue vs priority inbox vs Joey
- Cadence detection: AI analyzes drop patterns, suggests daily/weekly
- Feedback loop: reply to any digest with "daily" / "weekly" / "pause"

**Trial structure:**
- Week 1: Daily (high touch, prove value)
- Week 2+: Recommend cadence based on drop volume
- User can override anytime

---

### 2. STRIPE & BILLING
**Decision:** Generous trial → usage-based tiers

**Trial (14 days):**
- 50 drops included
- Full Intelligence Map
- Daily or weekly digest
- No credit card required

**Post-trial Tiers:**
| Tier | Price | Drops | Features |
|------|-------|-------|----------|
| Free | $0 | 10/mo | Weekly digest, basic themes |
| Lite | $7/mo | 100/mo | Daily or weekly, full Intelligence Map |
| Pro | $15/mo | 500/mo | Multiple emails, API access |
| Custom | $49/mo | Unlimited | Team features, custom templates, dedicated domain |

**Friction removal:**
- One-click upgrade (Stripe link, no checkout flow)
- Pay-as-you-go overages ($0.10/drop above limit)
- Pause anytime (data retained, resume later)

---

### 3. EMAIL LISTS
**Decision:** 4 foundational segments

| List | Purpose | How They Join |
|------|---------|---------------|
| **Feedback** | Beta testers, power users | Personal invite by Joey |
| **BHA** | BrutallyHonest.ai cross-sell | Auto-sync from BHA (opt-in) |
| **DA Interested** | Waitlist, prospects | Landing page signup |
| **Friends & Family** | Inner circle | Joey adds manually |

**Segmentation rules:**
- One person can be on multiple lists
- Each list gets different email content/CTAs
- Friends & Family get "skip the waitlist" priority

---

### 4. TIERS & UPGRADE PATH
**Decision:** Land with Lite ($7/mo), expand later

**Launch scope:**
- Free: teaser, limited value
- Lite: the main product
- Pro: for power users
- Custom: enterprise/teams (post-launch)

**Future upgrades (not launch):**
- More crons → API access
- More projects → team workspaces
- More powerful models → Pro tier
- Bring your own API → self-hosted option
- Dashboard → Phase 2 (if users demand)
- Outbound email address → custom drop@yourdomain.com
- Custom templates → white-label
- Public dashboard → business tier

**Pricing principle:** Charge for value delivered (insights), not features (dashboards)

---

### 5. DATA SEPARATION
**Decision:** Row-level isolation, encrypted at rest

**Architecture:**
- Each user: isolated database row
- Data access: scoped to user_id only
- Encryption: AES-256 at rest (Railway volumes)
- Backups: daily to S3, encrypted
- Retention: soft delete, 30-day recovery
- Export: GDPR-compliant data portability

**Security:**
- No cross-user queries possible
- API keys rotate monthly
- Webhook tokens unique per user
- Audit log: who accessed what, when

**The "smaller slice":**
- Each user's data = one PostgreSQL row + one Resend contact
- Intelligence = ephemeral (generated, emailed, discarded)
- Vault = user's email inbox (we don't store history)
- Analytics = aggregate only (no individual tracking)

---

## What We Cut (No Longer Launch Scope)

- Dashboard UI (all tabs)
- Authentication system (OAuth, sessions)
- Settings page
- Vault view
- Stream view
- Activity feed
- Compass page (ironically)
- Public-facing Intelligence Map
- Real-time features
- Push notifications

**Time saved:** ~103 hours frontend work

---

## What Must Work Perfectly

1. Email deliverability (inbox, not spam)
2. Intelligence Map quality (themes, connections, patterns)
3. Admission flow (waitlist → welcome → first digest)
4. Stripe billing (trial → payment without friction)
5. Hub webhook → instant processing (no polling delays)

---

## Open Decisions (Joey to decide)

- [ ] **Soft launch list:** Confirm 12 users across 3 tiers
- [ ] **Trial length:** 7 days vs 14 days vs 30 days
- [ ] **Free tier:** Keep or remove? (Some say it's a crutch)
- [ ] **First digest timing:** Immediate vs overnight vs user-scheduled
- [ ] **Poe balance:** Add credits or pause heavy bots before depletion

---

## Source Files

| Document | Location | Purpose |
|----------|----------|---------|
| This COMPASS | `ops/COMPASS.md` | Single source of truth |
| Revised Audit | `ops/audit/MASTER-REPORT-v2-EMAIL-ONLY.md` | Full technical findings |
| Agency Poll | `ops/strategic-poll-email-only-pivot.md` | 10 department votes |
| 5 Questions | `ops/strategic-answers-email-only-pivot.md` | Detailed answers |
| Daily Log | `memory/YYYY-MM-DD.md` | Execution updates |

---

## Version History

| Date | Version | Change |
|------|---------|--------|
| Mar 16 | v1 | Email-only pivot approved |

---

*Reply to this file's email thread for updates. Drop maintains this as the single source of truth for launch decisions.*
