---
name: family-retention-guardian
description: Monitor family member engagement and create automated re-engagement tasks when family members become inactive. Prevents family relationship strain from productivity system neglect.
---

# Family Retention Guardian

Monitors Joey's family members in DropAnywhere and creates automated re-engagement workflows when they become inactive. Because family relationships matter more than product metrics.

## When to Use

**AUTOMATIC TRIGGERS:**
- Family member inactive >7 days
- Family member engagement score <50%
- Family member has vault_count=0 but account exists
- Family member getting digests but not dropping

**MANUAL TRIGGERS:**
- "Check family retention"
- "Family engagement audit"
- After UserHealth escalations mention family

## Family Members (Auto-Detected)

Based on email patterns + user data:
- `lhamer228@gmail.com` (family)
- `rhamersunsetpartners@gmail.com` (family) 
- `hamer.daniel@gmail.com` (family)
- Any user with "hamer" in email or profile
- Any user manually tagged as family

## Problem Solved

**Pattern 285:** "Family Retention as Execution Canary"
- If personal stakes don't override paralysis, nothing will
- 8+ UserHealth escalations, 0 action taken
- lhamer228@gmail.com: 13 days inactive, 12 digests since last engagement
- rhamersunsetpartners@gmail.com: 10 days inactive, 8 digests since engagement  
- hamer.daniel@gmail.com: ZERO drops ever, digest enabled but unused

## Features

### 1. Family Detection
- Scans Hub user database for Hamer family emails
- Identifies engagement patterns vs general users
- Tags family accounts for special monitoring

### 2. Risk Assessment
```
HEALTHY: <7d since last drop, engagement >70%
AT_RISK: 7-14d since last drop, engagement 30-70%  
CRITICAL: >14d since last drop, engagement <30%
ABANDONED: >30d since last drop OR vault_count=0
```

### 3. Automated Interventions
- **AT_RISK:** Gentle check-in message via DropAnywhere
- **CRITICAL:** Personal outreach via WhatsApp to Joey
- **ABANDONED:** Strategy session with Joey (relationship repair)

### 4. Escalation Ladder
```
Day 7: System notification (silent)
Day 10: Gentle re-engagement task created  
Day 14: Joey WhatsApp alert (urgent but respectful)
Day 21: Strategy session scheduled (relationship focus)
Day 30: Relationship repair consultation
```

## Quick Start

```bash
# Check all family members
python3 scripts/check_family.py

# Check specific family member  
python3 scripts/check_family.py --email lhamer228@gmail.com

# Generate re-engagement plan
python3 scripts/create_engagement_plan.py --user-id b419d8ad5d23513f
```

## Scripts

### `scripts/check_family.py`
Main family monitoring script:
- Fetches family user data from Hub API
- Calculates engagement scores and inactivity periods
- Generates status report with recommendations
- Creates re-engagement tasks when thresholds hit

### `scripts/create_engagement_plan.py` 
Re-engagement workflow generator:
- Analyzes user's previous drop patterns
- Suggests personalized re-engagement approach
- Creates task with specific messaging strategy
- Schedules follow-up checks

### `scripts/family_detector.py`
Family member detection and tagging:
- Scans user database for family patterns
- Updates family tags in user profiles
- Maintains family member registry

## Environment Variables

```bash
# Hub API access (same as other skills)
HUB_API_KEY=your_hub_api_key
HUB_URL=https://hub-production-f423.up.railway.app

# WhatsApp alerts for critical family issues
FAMILY_ALERT_WEBHOOK=your_whatsapp_webhook
```

## Example Output

```json
{
  "family_status": "CRITICAL", 
  "members": [
    {
      "email": "lhamer228@gmail.com",
      "user_id": "920d4d339900efd5", 
      "status": "CRITICAL",
      "last_drop": "2026-03-04",
      "days_inactive": 13,
      "engagement_score": 24,
      "digests_since_engagement": 12,
      "action": "WhatsApp alert to Joey + gentle outreach task created"
    }
  ],
  "tasks_created": [
    {
      "type": "gentle_outreach",
      "target": "lhamer228@gmail.com", 
      "message": "Hey! Missing your drops. Everything okay? No pressure, just checking in. 💜",
      "deadline": "2026-03-20"
    }
  ]
}
```

## Integration

- **UserHealth:** Triggered after family escalations
- **Chief of Staff:** Reports to family status in daily briefings
- **WhatsApp:** Sends critical alerts directly to Joey
- **Hub API:** Creates re-engagement tasks in task queue

## Success Metrics

- Reduced family escalation frequency
- Increased family member engagement
- Faster intervention response time (target: <24h)
- Maintained family relationships despite product focus

## Tips

- **Personal > Product:** Always prioritize relationship over metrics
- **Gentle Touch:** Re-engagement should feel supportive, not naggy
- **Context Aware:** Consider why someone might be inactive (busy, upset, confused)
- **Joey's Voice:** All outreach should sound like Joey, not a bot

## Notes

This skill addresses **Pattern 285** from SkillMiner analysis: "If personal stakes don't override paralysis, nothing will." Family retention is the canary in the coal mine for execution capability.

Created by SkillMiner on 2026-03-18.