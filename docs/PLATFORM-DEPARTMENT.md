# AGENT-COMPANY-v3.1.md — Platform & Integrations Department

**Addition to v3.0: The Integration Layer**  
**Date:** 2026-03-15  
**Status:** Platform Department Specification  

---

## NEW: Platform Department (The "Connective Tissue")

**Mission:** Manage all external tools, APIs, tokens, and integrations. Ensure connectivity across the ecosystem.

**Why This Matters:**
- 15+ external services currently in use
- Tokens expire, APIs break, quotas hit
- No single source of truth for integration health
- New tools added ad-hoc, old tools never cleaned up
- Switching providers (e.g., SendGrid → Resend) requires coordination

**The Problem:**
```
Right now: Stripe token expires → payment fails → Joey notices → panic fix
With PlatformBot: Token expires 30d warning → auto-rotation → zero downtime
```

---

## Platform Department Agents

| Agent | Role | Focus | Status |
|-------|------|-------|--------|
| **PlatformBot** ⭐ | Integration Platform Manager | All tools, APIs, tokens | 🟡 Create |
| **TokenRotationBot** | Credential Manager | Token lifecycle, rotation | 🟡 Create |
| **APIHealthBot** | API Monitoring | Uptime, latency, quotas | 🟡 Create |
| **VendorBot** | Vendor Relations | Contracts, pricing, alternatives | 🟡 Create |
| **MigrationBot** | Migration Specialist | Tool switching, deprecations | 🟡 Create |

---

## PlatformBot ⭐ — The Integration Nervous System

### Responsibilities

#### 1. Integration Inventory

**Maintains canonical list of all external dependencies:**

```yaml
# platform-inventory.yaml
integrations:
  # Email
  resend:
    type: email_delivery
    env_var: RESEND_API_KEY
    health_endpoint: https://api.resend.com/emails
    usage_metric: emails_sent_24h
    quota_limit: 100000  # emails/month
    rotation_schedule: 90d
    alert_threshold: 80%
    status: active
    
  # AI/LLM
  anthropic:
    type: llm_api
    env_var: ANTHROPIC_API_KEY
    health_endpoint: https://api.anthropic.com/v1/models
    usage_metric: tokens_consumed
    quota_limit: null  # pay per use
    rate_limit: 4000  # requests/min
    rotation_schedule: 180d
    fallback: openrouter
    status: active
    
  openrouter:
    type: llm_router
    env_var: OPENROUTER_API_KEY
    health_endpoint: https://openrouter.ai/api/v1/models
    usage_metric: credits_spent
    quota_limit: null
    balance_alert: 10.00  # USD
    rotation_schedule: 180d
    status: active
    
  poe:
    type: bot_platform
    env_var: POE_API_KEY
    health_endpoint: https://api.poe.com/bots
    usage_metric: points_consumed
    quota_limit: null  # auto-refill
    balance_alert: 50000  # points
    rotation_schedule: 180d
    status: active
    
  # Payments
  stripe:
    type: payment_processor
    env_var: STRIPE_SECRET_KEY
    health_endpoint: https://api.stripe.com/v1/account
    usage_metric: revenue_24h
    webhook_secret: STRIPE_WEBHOOK_SECRET
    rotation_schedule: 365d
    status: active
    
  # Infrastructure
  railway:
    type: hosting_platform
    env_var: RAILWAY_API_TOKEN
    health_endpoint: https://backboard.railway.app/graphql
    usage_metric: resource_usage
    quota_limit: null  # team plan
    rotation_schedule: 180d
    status: active
    
  # Analytics
  google_analytics:
    type: web_analytics
    env_var: GA_MEASUREMENT_ID, GA_API_SECRET
    health_endpoint: https://analytics.google.com
    usage_metric: pageviews
    status: active
    
  google_search_console:
    type: seo_analytics
    env_var: GSC_API_KEY
    health_endpoint: https://searchconsole.googleapis.com
    usage_metric: impressions
    status: active
    
  # Commerce
  gumroad:
    type: digital_commerce
    env_var: GUMROAD_ACCESS_TOKEN
    health_endpoint: https://api.gumroad.com/v2/products
    usage_metric: sales_24h
    rotation_schedule: 180d
    status: active
    
  # Communication
  twilio:
    type: sms_voice
    env_var: TWILIO_AUTH_TOKEN
    usage_metric: sms_sent
    quota_limit: null
    balance_alert: 20.00  # USD
    status: active
    
  # Code/Deployment
  github:
    type: code_hosting
    env_var: GH_TOKEN
    health_endpoint: https://api.github.com/user
    usage_metric: api_calls
    rate_limit: 5000  # per hour
    rotation_schedule: 90d
    status: active
```

#### 2. Token Lifecycle Management

**TokenRotationBot handles:**

```
Creation → Rotation Schedule → Expiry Warning → Rotation → Archival
     │                              │                │           │
     │                              │                │           └─ Keep old for 7d (rollback)
     │                              │                └─ Zero-downtime swap
     │                              └─ 30d, 7d, 1d alerts
     └─ Stored in Railway env vars (encrypted)
```

**Rotation Process:**
1. Generate new token via provider API
2. Add to Railway as `SERVICE_KEY_NEW`
3. Update service to use new var
4. Deploy (zero downtime)
5. Rename: `SERVICE_KEY` → `SERVICE_KEY_OLD`
6. Rename: `SERVICE_KEY_NEW` → `SERVICE_KEY`
7. Wait 7 days
8. Delete `SERVICE_KEY_OLD`
9. Revoke old token via provider API

#### 3. API Health Monitoring

**APIHealthBot checks every 5 minutes:**

| Check | Action on Fail |
|-------|----------------|
| Authentication valid | Alert PlatformBot → Escalate if not resolved in 10min |
| Rate limit approaching | Alert Claw → Throttle or queue requests |
| Quota/balance low | Alert Claw → Auto-top-up if configured |
| Endpoint latency | Log + alert if > 2s for 3+ checks |
| Webhook delivery | Retry queue + alert on repeated failures |

**Health Dashboard (auto-generated):**
```
┌─────────────────────────────────────────────────────────┐
│ PLATFORM HEALTH — 2026-03-15 08:00 CST                  │
├─────────────────────────────────────────────────────────┤
│ ✅ Anthropic        200ms   Tokens: 45% of quota        │
│ ✅ OpenRouter       180ms   Balance: $247.50            │
│ ⚠️  Poe            320ms   Points: 33K (burning fast)   │
│ ✅ Stripe          150ms   Webhooks: 100% delivery      │
│ ✅ Resend          120ms   Quota: 12% used              │
│ ✅ Railway         200ms   All services healthy         │
│ ⚠️  Twilio         —       Balance: $18.50 (< $20)      │
└─────────────────────────────────────────────────────────┘
```

#### 4. Usage & Cost Tracking

**VendorBot aggregates:**

| Service | Monthly Cost | Trend | Alert |
|---------|--------------|-------|-------|
| Anthropic | $347.50 | ↑ 23% | None |
| OpenRouter | $128.20 | ↑ 15% | None |
| Poe | $89.00 | ↓ 12% | Low balance |
| Railway | $47.00 | → 0% | None |
| Stripe | $0.00 (revenue) | — | — |
| **Total** | **$611.70** | ↑ 8% | None |

**Anomaly Detection:**
- Cost spike > 50% → Alert Claw
- Unexpected service usage → Investigate
- Unused services flagged for cleanup

#### 5. Migration Management

**MigrationBot handles tool switches:**

**Example: SendGrid → Resend migration**
```
Phase 1: Discovery
- Audit all SendGrid usage (code search)
- Map SendGrid features to Resend equivalents
- Identify gaps

Phase 2: Parallel Setup
- Add Resend to Platform inventory
- Implement dual-send (SendGrid + Resend)
- Verify deliverability parity

Phase 3: Cutover
- Switch default to Resend
- Monitor for 7 days

Phase 4: Cleanup
- Remove SendGrid code
- Revoke SendGrid tokens
- Update documentation
- Archive SendGrid from inventory
```

#### 6. Integration Onboarding Process

**When adding a new tool:**

```yaml
new_integration_request:
  service: linear
  purpose: Project management for agent tasks
  requested_by: Claw
  
  checklist:
    - [ ] Security review (VendorBot)
    - [ ] Pricing evaluation (VendorBot)
    - [ ] Env var naming convention (PlatformBot)
    - [ ] Health check endpoint identified (PlatformBot)
    - [ ] Fallback/migration plan (MigrationBot)
    - [ ] Documentation updated (DocBot)
    - [ ] Added to inventory (PlatformBot)
    - [ ] Token rotation schedule set (TokenRotationBot)
    - [ ] Alerts configured (APIHealthBot)
```

---

## Integration Workflows

### Workflow: Token Expiry Prevention

```
TokenRotationBot scans all tokens daily
    ↓
Finds: Stripe token expires in 30 days
    ↓
Generates new token via Stripe API
    ↓
Stashes in Railway as STRIPE_SECRET_KEY_NEW
    ↓
Notifies Claw: "Token rotation pending for Stripe"
    ↓
Claw approves
    ↓
RailwayBot deploys with new token
    ↓
TokenRotationBot monitors for 7 days
    ↓
Revokes old token
    ↓
Updates inventory
```

### Workflow: API Outage Response

```
APIHealthBot detects Anthropic 500 errors
    ↓
Checks: Is this widespread or just us?
    ↓
Confirms: Anthropic status page shows incident
    ↓
Notifies Claw + Engineering
    ↓
Engineering switches to OpenRouter fallback
    ↓
APIHealthBot monitors recovery
    ↓
Once stable: Switch back to Anthropic
    ↓
LearningBot documents: "Anthropic outage 2026-03-15, 23min"
```

### Workflow: Cost Spike Investigation

```
VendorBot detects Anthropic cost ↑ 150%
    ↓
Queries: Which service? Which endpoint?
    ↓
Finds: Hub digest generation using Claude-Opus instead of Haiku
    ↓
Notifies Claw + Engineering
    ↓
Engineering fixes model routing
    ↓
VendorBot confirms cost normalizes
    ↓
OrgEffectivenessBot: "Cost control gap identified, added monitoring"
```

---

## Tool Inventory (Current State)

### Active Integrations

| Category | Tool | Env Var | Health | Last Rotation |
|----------|------|---------|--------|---------------|
| **AI/LLM** | Anthropic | ANTHROPIC_API_KEY | ✅ | 2026-01-15 |
| | OpenRouter | OPENROUTER_API_KEY | ✅ | 2026-02-01 |
| | Poe | POE_API_KEY | ✅ | 2026-01-20 |
| | Gemini | GOOGLE_API_KEY | ✅ | 2026-02-10 |
| **Email** | Resend | RESEND_API_KEY | ✅ | 2026-03-01 |
| | Resend Webhook | RESEND_WEBHOOK_SECRET | ✅ | Never |
| **Payments** | Stripe | STRIPE_SECRET_KEY | ✅ | 2026-01-01 |
| | Stripe Webhook | STRIPE_WEBHOOK_SECRET | ✅ | Never |
| **Hosting** | Railway | RAILWAY_API_TOKEN | ✅ | 2026-02-15 |
| | Railway Staging | RAILWAY_STAGING_TOKEN | ✅ | 2026-02-15 |
| **Analytics** | Google Analytics | GA_MEASUREMENT_ID | ✅ | N/A |
| | Search Console | GSC_API_KEY | ✅ | N/A |
| **Comms** | Twilio | TWILIO_AUTH_TOKEN | ✅ | 2026-01-10 |
| **Code** | GitHub | GH_TOKEN | ✅ | 2026-03-01 |
| | GitHub (BHA) | GITHUB_TOKEN | ✅ | 2026-02-20 |
| **Commerce** | Gumroad | GUMROAD_ACCESS_TOKEN | ✅ | 2026-01-05 |
| **Storage** | PostgreSQL | HUB_DATABASE_URL | ✅ | N/A |
| | Railway Volume | — | ✅ | N/A |

### Integration Gaps to Address

1. **No automated token rotation** — All manual
2. **No cost anomaly detection** — Discovered via surprise bill
3. **No API health dashboard** — Check services individually
4. **No webhook failure alerts** — Silent failures possible
5. **No migration runbooks** — Each switch is ad-hoc
6. **No usage attribution** — Which agent used which API?

---

## Implementation

### Phase 1: Inventory & Monitoring (Week 1)
- [ ] PlatformBot spawned
- [ ] Complete inventory of all integrations
- [ ] APIHealthBot basic health checks
- [ ] Dashboard: Single view of all integrations

### Phase 2: Token Management (Week 2-3)
- [ ] TokenRotationBot rotation schedule
- [ ] 30/7/1 day expiry alerts
- [ ] First rotation (test with low-risk token)

### Phase 3: Cost & Usage (Week 4)
- [ ] VendorBot cost aggregation
- [ ] Anomaly detection rules
- [ ] Usage attribution by agent

### Phase 4: Automation (Month 2)
- [ ] Auto-top-up for pre-paid services
- [ ] Auto-fallback on outages
- [ ] Migration runbook templates

---

## The Vision: Self-Healing Infrastructure

**Current:**
```
API fails → User reports → Joey investigates → Manual fix
```

**With Platform Department:**
```
API fails → APIHealthBot detects → Auto-fallback activated → 
Claw notified → Engineering fixes root cause → 
LearningBot documents → MigrationBot verifies fix
```

**The Platform is the nervous system.** Every external connection monitored, every token rotated, every cost tracked. Nothing fails silently. Nothing expires unexpectedly.

---

*This is the infrastructure layer that makes the Agent Company reliable.*

