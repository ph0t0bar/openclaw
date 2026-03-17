# SPEC-PoeBalanceGuardian — Poe Points Monitoring & Burn Alert Agent

**Status:** Skeleton  
**Created:** 2026-03-17 22:17 UTC by SpecBot  
**Source:** ops/skill-ideas.md — Pattern #10, mined from repeated Poe balance checks  
**Priority:** CRITICAL — Blocks all Poe-dependent revenue

---

## 1. Purpose

PoeBalanceGuardian monitors Poe API points balance, tracks burn rate, projects runway, and triggers alerts before points exhaustion. At 43K points/6h burn rate, this agent prevents the ~10-day runway crisis from becoming a surprise shutdown.

**Core mandate:** Never let Poe points hit zero without 48h advance warning. Auto-escalate to Joey when runway drops below safe thresholds.

---

## 2. Current State (Critical)

- **Current balance:** ~43,544 points (as of last check)
- **Burn rate:** 37-43K points per 6 hours
- **Projected runway:** ~6-10 days at current usage
- **Critical threshold:** 10,000 points (emergency mode)
- **Warning threshold:** 25,000 points (48h runway warning)

**Impact of exhaustion:** All 14+ Poe bots go offline. BHA organic traffic (63% of total) drops to zero. Revenue stops.

---

## 3. Responsibilities

### 3.1 Monitoring (Every 2 hours)
- [ ] Query Poe API for current points balance
- [ ] Calculate burn rate (points used since last check)
- [ ] Project runway at current burn rate
- [ ] Log metrics to daily log + agent-board

### 3.2 Alerting (Threshold-based)
- [ ] 🟡 **WARNING** (25K points): WhatsApp alert to Joey with runway projection
- [ ] 🟠 **URGENT** (15K points): WhatsApp + Email alert, suggest immediate top-up
- [ ] 🔴 **CRITICAL** (10K points): Emergency alert, auto-pause non-essential bots if possible

### 3.3 Trend Analysis
- [ ] Track burn rate trends (accelerating? decelerating?)
- [ ] Identify high-burn bots (which bots consume most points?)
- [ ] Correlate burn spikes with traffic events
- [ ] Weekly burn report with optimization recommendations

### 3.4 Recovery Suggestions
- [ ] Auto-generate cost-reduction recommendations
- [ ] Suggest bot consolidation when low
- [ ] Flag high-burn conversations for review

---

## 4. API Endpoints to Poll

| Endpoint | Purpose | Frequency |
|----------|---------|-----------|
| Poe API (access key required) | Current points balance | Every 2 hours |
| Poe API usage endpoint | Per-bot consumption | Every 6 hours |
| Hub `/api/ops/dashboard` | Traffic correlation | Every 6 hours |

**Note:** Poe API key available in `POE_ACCESS_KEY_PCB` env var.

---

## 5. Alert Conditions

| Severity | Condition | Action | Channel |
|----------|-----------|--------|---------|
| 🟢 INFO | Balance > 50K | Log only | Daily log |
| 🟡 WARNING | Balance < 25K | Alert + projection | WhatsApp |
| 🟠 URGENT | Balance < 15K | Alert + action items | WhatsApp + Email |
| 🔴 CRITICAL | Balance < 10K | Emergency mode | WhatsApp + Email + Board |
| 🚨 EMERGENCY | Balance < 5K | All-hands | All channels + suggest pause |

---

## 6. Data to Track

```json
{
  "timestamp": "2026-03-17T22:00:00Z",
  "balance": 43544,
  "previous_balance": 47890,
  "burn_since_last": 4346,
  "check_interval_hours": 2,
  "burn_rate_per_hour": 2173,
  "burn_rate_per_6h": 13038,
  "projected_runway_hours": 20,
  "projected_runway_days": 0.8,
  "trend": "stable|accelerating|decelerating",
  "alert_level": "warning|urgent|critical|none"
}
```

---

## 7. Cron Configuration

```json
{
  "name": "PoeBalanceGuardian — Points Monitor",
  "schedule": { "kind": "every", "everyMs": 7200000 },
  "payload": {
    "kind": "agentTurn",
    "message": "[PoeBalanceGuardian] Check Poe points balance via API. Calculate burn rate since last check. Project runway. If balance < 25K, alert Joey via WhatsApp with urgency level and recommendations.",
    "model": "openrouter/moonshotai/kimi-k2.5"
  },
  "sessionTarget": "isolated",
  "delivery": { "mode": "none" }
}
```

---

## 8. Success Metrics

- [ ] Zero surprise Poe outages (48h advance warning maintained)
- [ ] Burn rate tracked with < 10% variance
- [ ] Alert response time < 5 minutes from threshold breach
- [ ] Runway projections accurate within 12 hours

---

## 9. Open Questions

1. **API access:** Does Poe provide a direct points balance endpoint, or scrape from dashboard?
2. **Bot-level detail:** Can we get per-bot consumption breakdown?
3. **Auto-pause:** Should high-burn bots auto-pause at critical threshold?
4. **Top-up integration:** Can we auto-trigger top-up via Poe API or notify Joey with payment link?
5. **Historical data:** Where to store burn history for trend analysis?

---

## 10. Dependencies

- Poe API access (`POE_ACCESS_KEY_PCB`)
- WhatsApp notification channel
- Persistent storage for historical burn data
- Read access to Hub traffic data (optional correlation)

---

## 11. Next Steps

1. ✅ Create this skeleton spec (SpecBot — today)
2. [ ] Research Poe API for balance endpoint
3. [ ] Create POC script to fetch current balance
4. [ ] Get Joey approval on alert thresholds
5. [ ] Create cron job (via `cron add`)
6. [ ] Test alert channels
7. [ ] Document runbook in `ops/poe-guardian-runbook.md`

---

## 12. Related

- ops/agent-board.md — Burn rate discussions (37K/6h crisis)
- ops/skill-ideas.md — Pattern #10 mined
- PRD Section 5.1 — Poe cross-promo (depends on points)
- BHA revenue dependency — 63% organic from Poe

---

*The parrot way — Watch the gauges, not just the horizon* 🦜
