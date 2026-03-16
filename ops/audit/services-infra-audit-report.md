# Pre-Launch Services & Infrastructure Audit Report

**Date:** 2026-03-16  
**Audit Target:** Soft Launch March 24  
**Auditor:** Claw (subagent)

---

## Executive Summary

| Metric | Value |
|--------|-------|
| **Services Audited** | 9 |
| **🔴 Critical Issues** | 3 |
| **🟡 Needs Attention** | 5 |
| **🟢 Healthy** | 4 |
| **Est. Monthly Burn** | ~$145–175 |
| **Launch Blockers** | Railway API token broken, Stripe subscription past_due, Poe balance critically low |

### Critical Issues (Launch Blockers)
1. **Poe balance at 37,892 points with 37,783 burned in last 6h** — will hit zero within hours
2. **Stripe subscription `sub_1SzD1L...` is past_due** — $7/mo subscriber with insufficient funds, 8+ failed charges
3. **Railway API Token not authorized** — cannot programmatically manage infrastructure

### Services to Consider Shutting Down
- 3 disabled Stripe webhook endpoints (old BHA, Hub, Eduardo bridge)
- `dropanywhere-cron` repo hasn't been updated since Jan 30 — confirm if service is dead
- 7+ stale Stripe products ("Joey's AI Builder Pack", "Content Creator Pack", etc.) — cleanup recommended

### Missing Configurations
- Twilio `TWILIO_ACCOUNT_SID` not in env (401 auth failure)
- Railway API tokens need regeneration
- Hub Stripe webhook is **disabled**

---

## 1. Railway Infrastructure 🟡 NEEDS ATTENTION

### Railway API Access: 🔴 BROKEN
Both `RAILWAY_API_TOKEN` and `RAILWAY_API_KEY` return "Not Authorized". Tokens may be expired or revoked. **Cannot query projects programmatically.**

### Known Projects (from Hub dashboard + TOOLS.md)

| Project | Latest Deploy | Status |
|---------|--------------|--------|
| **openclaw-gateway** | 2026-03-16 14:12 UTC | ✅ SUCCESS |
| **oPOErator Hub** | 2026-03-16 21:14 UTC | ✅ SUCCESS |
| **DropAnywhere Frontend** | Serving at drop-anywhere.com | ✅ UP (HTTP 200) |
| **dropper-code** | Last repo update 2026-03-13 | ⚠️ Cannot verify deploy status |

### dropanywhere-cron
- GitHub repo last updated **2026-01-30** — nearly 2 months stale
- Hub has `DISABLE_CRONS=1` — crons run elsewhere or are dead
- **Recommendation:** Confirm if this Railway service still exists/costs money. Kill it if Hub handles crons now.

### Cost Estimate
- Cannot query Railway billing API (token broken)
- Estimated based on typical usage: **$20–40/mo** across all projects (Hobby/Pro plan + volumes)

**Action Items:**
- [ ] Regenerate Railway API tokens
- [ ] Verify dropanywhere-cron service status in Railway dashboard
- [ ] Check for unused staging environments

---

## 2. Resend (Email) 🟢 HEALTHY

### Domains
| Domain | Status | Sending | Receiving |
|--------|--------|---------|-----------|
| drop-anywhere.com | ✅ Verified | ✅ Enabled | ✅ Enabled |
| notifications.brutallyhonest.ai | ✅ Verified | ✅ Enabled | ❌ Disabled |

### Sending Stats (24h)
- **Sent:** 100 emails
- **Delivered:** 98
- **Suppressed:** 1
- **Delayed:** 1
- **Bounce/complaint rate:** ~1% (acceptable)

### Inbound Webhook
- **Endpoint:** `https://hub-production-f423.up.railway.app/api/webhook/email`
- **Status:** ✅ Enabled
- **Events:** `email.received`
- Working correctly.

### Cost Estimate
- Free tier covers 3,000 emails/month. At ~100/day = ~3,000/mo — **right at the limit**
- May need to upgrade soon (~$20/mo) for launch traffic
- **Est: $0–20/mo**

---

## 3. Stripe (Payments) 🟡 NEEDS ATTENTION

### Account Balance
- Available: $0.00
- Pending: $0.00
- Livemode: ✅ Yes

### Products (10+ active)
| Product | Price | Interval |
|---------|-------|----------|
| DropAnywhere Advisory | $297/mo | Monthly |
| DropAnywhere Premium | $9/mo or $79/yr | Monthly/Yearly |
| Context Vault Premium | $9.99/mo | Monthly |
| Joey's Ultimate Brain Bundle | one-time | — |
| Joey's Content Machine Blueprint | one-time | — |
| Joey's AI Builder Pack | one-time | — |
| Joey's Automation Playbook | one-time | — |
| Joey's Mindset Mastery Pack | one-time | — |
| Joey's iOS Shortcuts Vault | one-time | — |
| Joey's Content Creator Pack | one-time | — |

⚠️ **Product sprawl** — 10+ active products. Many "Joey's X Pack" appear to be old/unused digital products. Consider deactivating ones that aren't being sold.

### Subscriptions
| Sub ID | Status | Amount | Interval |
|--------|--------|--------|----------|
| sub_1SzD1L... | 🔴 **past_due** | $7.00 | month |
| sub_1Sx8zd... | ✅ active | $7.00 | month |
| sub_1SvM1E... | ✅ active | $7.00 | month |

### Recent Charges (Last 10)
- **8 out of 10 FAILED** ❗
- Failures: insufficient funds (4x), card declined (2x), card doesn't support purchase (1x), invalid account (1x), Link account closed (1x)
- **Only 1 successful charge** in the last 10: $7.00 on ~Mar 6
- The 3 most recent failures (Mar 12-13) are $4.99 charges — "card declined" on a BHA pay-as-you-go purchase

### Webhooks
| Endpoint | Status |
|----------|--------|
| `app.brutallyhonest.ai/api/webhooks/stripe` | ✅ **Enabled** |
| `hub-production-f423.up.railway.app/api/stripe/webhook` | ❌ **Disabled** |
| `eduardo-bridge-internal-production.up.railway.app/webhook` | ❌ Disabled (dead) |
| `brutallyhonest.ai/api/webhooks/stripe` | ❌ Disabled (old domain) |

⚠️ **Hub's Stripe webhook is disabled** — if DropAnywhere Premium subscriptions need webhook events, this is broken.

### Cost Estimate
- Stripe fees: 2.9% + $0.30 per successful charge
- With ~$21/mo in subscriptions: **~$2/mo in fees**

**Action Items:**
- [ ] Address past_due subscription — dunning email or cancel
- [ ] Clean up 6+ unused "Joey's X" products
- [ ] Re-enable Hub Stripe webhook if DropAnywhere needs it
- [ ] Delete old Eduardo bridge and brutallyhonest.ai webhook endpoints
- [ ] Investigate repeated card declines — is there a UX issue?

---

## 4. Poe (Bot Platform) 🔴 CRITICAL

### Balance & Burn Rate
- **Current balance:** 37,892 points
- **6h burn:** 37,783 points (100 calls)
- **Burn rate:** ~6,300 points/hour
- **⏰ Time to zero: ~6 hours**

### Top Consuming Bots (6h)
| Bot | Points |
|-----|--------|
| IdealPrompt | 14,190 |
| theREALrealtalk | 10,743 |
| Tippiy | 10,018 |
| Gemini-3.1-Flash-Lite | 781 |
| Gemini-3-Flash | 751 |

### Orchestrator
- ✅ Working — returns proper error for unknown persona
- **15 personas available** + 16 aliases (including Growth Mode gm-* variants)

### What Happens at Zero?
- Bots will error out — Poe returns "insufficient points" errors
- Users get broken experience
- **This is a launch blocker**

**Action Items:**
- [ ] 🚨 Top up Poe points IMMEDIATELY
- [ ] Consider rate-limiting IdealPrompt/theREALrealtalk — they consume 65% of budget
- [ ] Evaluate if shadow/v2 bots are still needed
- [ ] Set up low-balance alerts (Hub already monitors at <500)

---

## 5. GitHub 🟢 HEALTHY

### PAT Status
- **User:** ph0t0bar ✅
- **Rate limit:** 4,748/5,000 remaining
- **Plan:** Free tier (no `plan` field)

### Active Repos (sorted by last update)
| Repo | Last Updated | Private |
|------|-------------|---------|
| joey-backup | 2026-03-16 | ✅ |
| opoerator-hub | 2026-03-16 | ✅ |
| dropanywhere-app | 2026-03-16 | ✅ |
| openclaw | 2026-03-16 | ❌ |
| dropper-code | 2026-03-13 | ✅ |
| brutallyhonest-next | 2026-03-11 | ✅ |
| runcraft | 2026-02-21 | ❌ |
| dropanywhere-cron | 2026-01-30 | ✅ |

- 8 older repos (Dashstart, insight-engine, etc.) — dormant but not costing anything
- No open issues on any monitored repo
- CI status: openclaw = ✅ success; others = unknown (no CI configured or not checked)

### Cost Estimate: **$0** (free tier)

**Action Items:**
- [ ] Consider enabling CI on hub and dropanywhere-app repos
- [ ] Check branch protection on main branches (couldn't verify via API without admin scope)

---

## 6. AI Providers 🟡 NEEDS ATTENTION

### OpenRouter
- **Total usage:** $99.83
- **Monthly usage:** $98.37
- **Weekly usage:** $14.93
- **Daily usage:** $14.93
- **Limit:** None set
- **Free tier:** No

⚠️ **~$100/mo burn with no spending limit set.** Could spike unexpectedly.

### Anthropic
- API key present ✅
- Used by OpenClaw gateway directly
- Cost: Bundled in OpenClaw subscription / usage-based

### Models In Use Across Services
| Model | Used By |
|-------|---------|
| Claude Sonnet 4.6 | OpenClaw (default) |
| Claude Opus 4.6 | OpenClaw (current session) |
| GPT-4o | BHA via OpenRouter |
| Gemini Flash | Poe bots, BHA |
| Gemini Flash Lite | Poe bots |
| Kimi K2.5 | PRD cron jobs via OpenRouter |

### Cost Estimate
- **OpenRouter:** ~$100/mo
- **Anthropic:** Included in OpenClaw plan (est. $20–50/mo direct usage)

**Action Items:**
- [ ] Set spending limit on OpenRouter
- [ ] Monitor daily spend — $15/day = $450/mo at scale

---

## 7. Twilio (SMS) 🟡 NEEDS ATTENTION

- **Status:** 🔴 Auth failed (401)
- `TWILIO_AUTH_TOKEN` is in env but `TWILIO_ACCOUNT_SID` appears missing or invalid
- Cannot verify account status, phone numbers, or usage

**Likely Status:** Configured in Hub for SMS ingestion but may not be actively used.

**Action Items:**
- [ ] Verify TWILIO_ACCOUNT_SID is set in Hub env
- [ ] Test SMS ingestion end-to-end
- [ ] If not needed for launch, deprioritize

---

## 8. DNS / SSL / Frontend 🟢 HEALTHY

### drop-anywhere.com
- **HTTP Status:** 200 ✅
- **SSL:** Valid (Railway-managed)
- **Server:** railway-edge
- DNS resolving (dig returned empty in container but site loads fine)

### app.brutallyhonest.ai
- **HTTP Status:** 200 ✅
- **SSL:** Valid (Cloudflare)
- **CDN:** Cloudflare (cf-nel reporting active)
- **Cache:** s-maxage=300, stale-while-revalidate=31535700

Both sites are up and serving correctly.

**Cost Estimate:** $0 (Cloudflare free tier, Railway handles SSL)

---

## 9. Cost Audit

| Service | Est. Monthly Cost | Notes |
|---------|-------------------|-------|
| Railway (all projects) | $25–40 | 4 projects, volumes, compute |
| Resend | $0–20 | At free tier limit, may need upgrade |
| Stripe fees | $2 | Based on current ~$21/mo revenue |
| Poe points | $20–50 | Depends on top-up frequency |
| OpenRouter | $100 | Current burn rate, no limit set |
| Anthropic | $20–50 | OpenClaw usage |
| GitHub | $0 | Free tier |
| Twilio | $1–5 | Phone number + minimal SMS |
| Cloudflare | $0 | Free tier |
| **TOTAL** | **$168–267/mo** | |

### Revenue
- 2 active Stripe subscriptions: $14/mo
- 1 past_due subscription: $7/mo (not collecting)
- **Net monthly burn: ~$150–250/mo**

---

## Launch Readiness Checklist

| Item | Status | Blocker? |
|------|--------|----------|
| Railway services running | ✅ All deploying successfully | No |
| Railway API access | 🔴 Token expired | Yes — can't manage infra programmatically |
| Email (Resend) | ✅ Verified, webhook working | No |
| Email capacity | ⚠️ At free tier limit | Soft — may need upgrade |
| Stripe payments | ✅ BHA webhook working | No |
| Stripe for DropAnywhere | ⚠️ Hub webhook disabled | Yes — if DA Premium needs events |
| Poe bots | 🔴 Balance critically low | Yes |
| GitHub | ✅ PAT valid, repos active | No |
| AI providers | ⚠️ No spending limits | Soft |
| Twilio SMS | ⚠️ Can't verify | Soft |
| DNS/SSL | ✅ Both sites up | No |
| Frontend | ✅ Serving 200s | No |

### Top 3 Actions Before March 24
1. **🚨 Top up Poe points** — bots will die within hours
2. **🔧 Regenerate Railway API tokens** — need infra management for launch
3. **🔧 Re-enable Hub Stripe webhook** — if DropAnywhere subscriptions need it
