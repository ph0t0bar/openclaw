
```

**Hub Webhook Integration:**

```python
# /api/waitlist endpoint
@app.post("/api/waitlist")
async def join_waitlist(email: str, source: str = "landing_page"):
    # 1. Validate email
    # 2. Check if already admitted
    # 3. Create user record with status='waitlisted'
    # 4. Add to Resend DA-Waitlist audience
    resend.contacts.create(
        email=email,
        first_name=extract_first_name(email),  # best effort
        audience_id="da_waitlist_v1",
        unsubscribed=False,
    )
    # 5. Trigger Email 1 via Resend
    resend.emails.send({
        "from": "DropAnywhere <hello@drop-anywhere.com>",
        "to": email,
        "subject": "You're on the list — DropAnywhere is coming",
        "html": render_template("email-01-welcome-waitlist.html", email=email),
    })
    return {"status": "waitlisted"}
```

**Soft Launch Tiers (Already Defined):**

| Tier | List Segment | When | Criteria |
|------|-------------|------|----------|
| Tier 1 | friends-family | Mar 24 09:00 | Immediate personal support (Lisa, Danny, Bob) |
| Tier 2 | feedback-core subset | Mar 24 12:00 | If Tier 1 digests clean |
| Tier 3 | BHA Engaged subset | Mar 24 17:00 | If Tier 2 stable |

**Migration Path:**
- Waitlist users → Admitted (manual promotion)
- BHA users → BHA+DA (future cross-sell campaign)
- Friends/Family → Full users (immediate admission)

### Decisions Joey Needs to Make

**Immediate (Before Mar 24):**
1. **Tier 1 list** — Confirm who goes in first batch (family emails)
2. **Tier 2 list** — Who are the 5-6 "feedback core" users for second wave?
3. **BHA cross-sell now?** — Do we email BHA list about DA launch, or wait until DA is stable?
4. **Waitlist cap** — Soft limit to stop admitting when? (50 users? 100?)

**Post-Launch:**
1. **Admission velocity** — How many users per day after launch? (5? 20? Unlimited?)
2. **BHA migration** — Automated campaign or personal outreach from Joey?
3. **List consolidation** — At what scale do we merge Feedback Core into Admitted?

---

## 4. TIERS & PRICING

### The Practical Answer (What We Do)

DropAnywhere uses a **simple 2-tier model** (Free/Pro) at launch, with a clear roadmap to more granular tiers as we learn:

**Current Tiers (Launch):**

| Feature | Free (Forever) | Pro ($9/month) |
|---------|----------------|----------------|
| Drops per week | 10 | Unlimited |
| Digest frequency | 3x/week (Mon/Wed/Fri) | Daily (7 days) |
| Digest timing | Default 7am CDT | User-selected timezone/time |
| Drop addresses | 1 (drops+id@) | 3 (work/personal/custom) |
| Email support | Community | Priority (48hr response) |
| Export data | CSV (manual request) | CSV + API access |
| Price | $0 | $9/month or $90/year |

**Future Tier Evolution (Roadmap):**

| Tier | Price | Target User | Differentiators |
|------|-------|-------------|-----------------|
| **Free** | $0 | Try-before-buy | 10 drops/week, limited digest timing |
| **Pro** | $9/mo | Personal power users | Unlimited drops, daily digest, custom timing |
| **Team** (Q2) | $29/mo | Small teams | Shared drop addresses, team vault, admin controls |
| **Business** (Q3) | $99/mo | Advisory firms | Custom domain, white-label digest, API access |
| **API-Only** (Q3) | Usage-based | Developers | BYO key, headless API, no digest |

**Feature-Based Pricing Dimensions (Future):**

The full feature matrix we can price on:

```
Volume:        drops/month, files/month, characters processed
Processing:    AI model quality (basic/advanced), analysis depth
Timing:        digest frequency, real-time alerts
Access:        API access, webhooks, integrations (Zapier, etc.)
Identity:      custom drop addresses, custom domains, white-label
Support:       community, email, priority, dedicated
History:       retention period (30d/1yr/forever), archive export
```

**The No-Brainer Billing Path:**

```
Free User Journey:
Week 1-2: 10 drops/week, love the product
Week 3: Hit 10 drop limit on Wednesday → email: "You've reached your limit"
Week 4: Same thing → now frustrated
Week 5: Digest subject changes: "Upgrade for unlimited drops"
    ↓
Same digest, but with upgrade section highlighted
    ↓
Click → Stripe Checkout → $9 → immediate unlimited
```

### The Strategic Thinking (Why)

**Why Simple 2-Tier at Launch:**

1. **Speed to market** — Every tier is complexity: pricing pages, upgrade flows, downgrade handling, feature gates. Launch with one paid tier.
2. **Single success metric** — "Are users upgrading to Pro?" is clearer than "Are users choosing the right tier?"
3. **No analysis paralysis** — Users don't compare 3 plans; they decide "Is this worth $9/month?" (yes/no)

**Why $9/month (Not $5 or $15):**

- **$5** = "cheap tool" positioning, attracts price-sensitive, high-churn users
- **$15** = "premium" but may exclude early adopters
- **$9** = "coffee per month" — justifiable, accessible, signals real value without being expensive

**Why Free is Limited (Not Time-Based):**
- Time-based trials (14 days then pay) work for event-driven products
- Usage-based free tier works for ongoing products like DA
- Users who hit 10 drops/week are **demonstrating value** — the limit itself creates conversion trigger

**Future Tier Philosophy:**
- **Pro** = personal use (individual productivity)
- **Team** = collaborative use (shared context)
- **Business** = invisible assistant (client-facing, white-label)
- **API-Only** = developers building on top (different product, really)

### The Implementation Path (How)

**Phase 1: Launch Tiers (Mar 24)**

Database schema:
```sql
users:
  - id, email, created_at
  - tier: 'free' | 'pro'
  - status: 'trialing' | 'active' | 'canceled'
  - trial_ends_at: timestamp
  - stripe_customer_id, stripe_subscription_id

usage_limits:
  - user_id
  - drops_this_week: int
  - drops_reset_at: timestamp
  - max_drops_per_week: 10 (free) | null (pro)
```

Feature gating:
```python
def can_user_drop(user_id):
    user = get_user(user_id)
    if user.tier == 'pro' or user.status == 'trialing':
        return True
    
    usage = get_usage(user_id)
    if usage.drops_this_week >= 10:
        return False  # Soft gate: warn but allow
    return True

def get_digest_config(user_id):
    user = get_user(user_id)
    if user.tier == 'pro':
        return {
            'frequency': 'daily',
            'time': user.preferred_time or '07:00',
            'timezone': user.timezone or 'America/Chicago'
        }
    else:
        return {
            'frequency': 'mon_wed_fri',
            'time': '07:00',
            'timezone': 'America/Chicago'
        }
```

**Phase 2: Team Tier (Q2 2026)**

- Shared vault: multiple users, shared drops
- Drop addresses per team: `teamname+topic@drop-anywhere.com`
- Admin dashboard (first exposure of dashboard UI!)
- Price: $29/month for up to 5 team members

**Phase 3: Business/Advisory Tier (Q3 2026)**

- Custom domain: `drops@joeyhamer.com` (not `@drop-anywhere.com`)
- White-label digest: your logo, your colors, sent from your domain
- Client separation: each client's drops isolated
- Price: $99/month + usage

**Phase 4: API-Only (Q3-Q4 2026)**

- Bring Your Own OpenAI/Anthropic key
- Headless: no digest, just API access to ingestion/analysis
- Usage-based billing: $0.001 per drop processed
- Target: developers building AI apps

### Decisions Joey Needs to Make

**Immediate (Before Mar 24):**
1. **Pro price** — $9, $7, or $12? Annual option now or later?
2. **Free tier limits** — 10 drops/week feels right? Or 5? Or 20?
3. **Trial length** — 14 days? Or extend to 30 for early adopters?
4. **Stripe product IDs** — Confirm configured or need setup?

**Near-Term (April):**
1. **Team tier priority** — Is B2B (advisory firms) the growth engine or secondary?
2. **API pricing** — Usage-based or flat rate? What does "prosumer"
