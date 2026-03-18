---
name: family-retention-guardian
description: Monitor family member engagement and automate re-engagement outreach when family members become inactive in DropAnywhere. Use when family engagement alerts are triggered or when analyzing user retention patterns for family accounts.
---

# Family Retention Guardian

Proactive monitoring and re-engagement system for family member accounts in DropAnywhere.

## When to Use

- Family member shows engagement decline (score < 50%)
- Family member inactive >7 days  
- UserHealth escalates family retention risk
- Periodic family engagement health checks
- Manual family user review requested

## Family Member Detection

Family members are identified by:
- Email domains: `@gmail.com` with surnames: `hamer`, `lhamer` 
- Known family emails:
  - `lhamer228@gmail.com` (Lisa Hamer)
  - `rhamersunsetpartners@gmail.com` (Ryan Hamer) 
  - `hamer.daniel@gmail.com` (Daniel Hamer)
  - `mitch.p.hamer@gmail.com` (Mitch Hamer)

## Engagement Scoring Algorithm

**Score Components (0-100):**
- Recency: 50% (days since last drop: 0d=50pts, 7d=25pts, 14d=0pts)
- Frequency: 30% (drops per week: 5+=30pts, 3-4=20pts, 1-2=10pts, 0=0pts)  
- Depth: 20% (vault size: 10+=20pts, 5-9=15pts, 1-4=10pts, 0=0pts)

**Risk Levels:**
- 80-100: Healthy 🟢
- 60-79: Watch 🟡  
- 40-59: At Risk 🟠
- 20-39: Critical 🔴
- 0-19: Emergency 🚨

## Re-engagement Pipeline

### Level 1: Gentle Nudge (score 40-59)
- Personalized email with recent family updates
- "Saw you haven't dropped anything lately..." tone
- Include 1-2 recent interesting vault finds

### Level 2: Direct Outreach (score 20-39)  
- Personal message from Joey via WhatsApp/text
- "Hey [name], everything okay? Haven't heard from you..."
- Offer to help with any DropAnywhere issues

### Level 3: Emergency Alert (score 0-19)
- Immediate alert to Joey via WhatsApp
- Full context: last activity, digest history, vault status
- Suggested personal intervention actions

## Core Workflow

1. **Family Detection**: Query Hub API for family email patterns
2. **Engagement Analysis**: Calculate scores using Hub activity data  
3. **Risk Assessment**: Categorize each family member by risk level
4. **Action Dispatch**: Execute appropriate re-engagement based on score
5. **Tracking**: Log all actions and outcomes for pattern analysis

## Hub API Integration

**Required Endpoints:**
- `/api/admin/users` - Get user list with activity data
- `/api/search` - Check vault content for engagement depth  
- `/api/alerts` - Send re-engagement alerts to Joey
- `/api/memory` - Log family retention actions for tracking

**Authentication:** Uses `HUB_API_KEY` from environment

## Usage Examples

**Check all family members:**
```bash
python scripts/check_family_health.py --all
```

**Monitor specific family member:**  
```bash
python scripts/check_family_health.py --email lhamer228@gmail.com
```

**Generate family engagement report:**
```bash
python scripts/family_report.py --format json
```

**Test re-engagement templates:**
```bash  
python scripts/test_templates.py --dry-run
```

## Templates

### Email Template: Gentle Nudge
```
Subject: Missing your updates! 

Hey [name],

I noticed you haven't sent anything to DropAnywhere lately. Everything okay?

Your vault has some great stuff in it - just saw your note about [recent_vault_item]. 

If you're having any trouble with the system or just been busy, no worries! Just wanted to check in.

Love,
Joey 
```

### WhatsApp Template: Direct Outreach  
```
Hey [name] - haven't seen you drop anything in DropAnywhere for a couple weeks. Everything good? Let me know if you need help with anything or if the system isn't working right for you! 😊
```

## Error Handling

- **Hub API failures**: Graceful degradation, retry with exponential backoff
- **Email delivery failures**: Log error, flag for manual follow-up
- **Missing family data**: Continue with available data, warn about gaps  
- **Score calculation errors**: Use conservative defaults (mark as "watch")

## Success Metrics

- Family member re-engagement rate within 7 days of outreach
- Reduction in family members reaching "critical" risk level  
- Time to Joey awareness of family retention issues
- False positive rate (healthy members flagged as at-risk)

## Testing

Run test suite:
```bash
python scripts/test_family_guardian.py
```

**Test Coverage:**
- Family member detection accuracy
- Engagement scoring algorithm  
- Template personalization
- Hub API integration
- Error handling scenarios
- Alert delivery confirmation

## Automation Integration

**Heartbeat Integration:**
- Add family check to heartbeat routine (every 6-12 hours)
- Include family status in heartbeat summary

**Cron Integration:**
- Daily family health check at 08:00 UTC  
- Weekly family engagement report on Sundays
- Emergency alerts triggered immediately (no scheduling)

## Privacy & Sensitivity

This skill handles family relationships with extra care:
- Personal, warm tone (not corporate)
- Respect privacy boundaries  
- Clear escalation to Joey for serious concerns
- No automated public/social posts about family issues
- Logs exclude sensitive personal details

## Dependencies

- Hub API access via `HUB_API_KEY`
- WhatsApp integration for Joey alerts
- Email integration for gentle nudges
- JSON file storage for family member configuration

---

**Implementation Status:** Ready for testing
**Created:** 2026-03-18 by SkillMiner  
**Priority:** URGENT - Pattern 285 evidence (8+ escalations, 0 action)
**Success Pattern:** Atomic scope (detection → scoring → outreach → escalation)