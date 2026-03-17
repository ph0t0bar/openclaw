---
name: poe-balance-guardian
description: Monitor Poe API balance and burn rate, alerting when balance drops below critical thresholds. Use when tracking Poe credit usage, predicting runway, or setting up balance alerts. Part of the DropAnywhere Agency - Meta department.
homepage: https://poe.com
metadata:
  openclaw:
    emoji: "💰"
    requires:
      env: ["POE_API_KEY"]
---

# Poe Balance Guardian

Monitor Poe API balance and burn rate, alerting when balance drops below critical thresholds.

## When to Use

✅ **USE this skill when:**

- "Check Poe balance" or "How many Poe points left?"
- Setting up balance monitoring alerts
- Predicting runway based on burn rate
- Weekly/monthly usage reporting
- Investigating unexpected credit consumption

❌ **DON'T use this skill when:**

- You need to top up Poe balance (use Poe website)
- You need bot analytics (use Poe creator dashboard)
- You need message-level usage (check individual bot logs)

## Prerequisites

Set your Poe API key:
```bash
export POE_API_KEY="your-poe-api-key"
```

## Usage

### Check Current Balance

```bash
python3 ~/.openclaw/workspace/skills/poe-balance-guardian/scripts/check_balance.py
```

Output:
```
💰 Poe Balance Report
━━━━━━━━━━━━━━━━━━━━━━
Current Balance: 45,910 points
6h Usage:        43,449 points
Burn Rate:       ~7,241 pts/hour
Estimated Runway: ~6.3 hours
Status:          ⚠️  WARNING (below 50K threshold)
━━━━━━━━━━━━━━━━━━━━━━
```

### Check with Custom Threshold

```bash
python3 ~/.openclaw/workspace/skills/poe-balance-guardian/scripts/check_balance.py --threshold 20000
```

### Get JSON Output (for automation)

```bash
python3 ~/.openclaw/workspace/skills/poe-balance-guardian/scripts/check_balance.py --json
```

### Run as Cron Job

```bash
# Add to crontab for hourly checks
0 * * * * python3 ~/.openclaw/workspace/skills/poe-balance-guardian/scripts/check_balance.py --alert --webhook-url "YOUR_WEBHOOK"
```

## Thresholds

| Balance | Status | Action |
|---------|--------|--------|
| > 100K | 🟢 Healthy | No action |
| 50K - 100K | 🟡 Caution | Monitor closely |
| 20K - 50K | 🟠 Warning | Plan top-up soon |
| 10K - 20K | 🔴 Critical | Top up within hours |
| < 10K | 🚨 Emergency | Immediate top-up required |

## Burn Rate Patterns

From observed usage:
- **Normal operations**: ~5K-15K pts/hour
- **High activity (launches)**: ~20K-40K pts/hour
- **Peak burn**: ~43K pts/6h observed during agent cycles

## Tips

- Check balance before major launches or agent cycles
- Set up alerts at 50K, 20K, and 10K thresholds
- Top up during business hours to avoid weekend emergencies
- Monitor which bots consume the most (usually high-context bots)
- Balance resets don't happen - points accumulate until used

## Agency Context

This skill is part of the **DropAnywhere Agency**:
- **Department:** Meta / Operations
- **Reports to:** Claw (Executive)
- **Collaborates with:** Chief of Staff, Patrol, PoeBot agents

Created: 2026-03-17
Version: 1.0
