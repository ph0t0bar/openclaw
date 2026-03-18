# Digest Pipeline Monitor

Monitors DropAnywhere digest delivery pipeline health and provides fallback mechanisms when automation fails.

## When to use this skill

- Core product failure: digest delivery rate drops below 50% of expected
- Pipeline stalled for >2 hours with 0 delivery attempts
- User reports missing daily digests
- Dropper-Code service degraded or out of credits
- Need to manually trigger digest generation for critical users

## Problem this solves

**CRITICAL: Core product failure detected 2026-03-18**
- Only 2/109 digests sent (98% failure rate) 
- Expected: ~80+ digests daily based on user base
- Hub shows 0 digest attempts in current delivery window
- 16 users affected including primary user Joey (b419d8ad)
- Pipeline stalled for 7+ hours while detection was perfect but execution failed

## Evidence from sessions

**Pattern 253**: Digest pipeline regression persists
- Repeated escalations from Chief of Staff, UserHealth, OpsMonitor
- Same crisis pattern across multiple sessions
- Detection accuracy: 100%, Execution success: 2%

**Infrastructure failure cascade:**
- Dropper-Code exhausted Claude Code usage limit (resets Mar 20 3am UTC)
- 24 errors spiked at 2026-03-17 19:00 UTC (1pm CST)
- Hub service running but digest scheduler appears stuck
- No automated recovery or manual fallback triggered

## Quick start

### Check digest pipeline health
```bash
cd /root/.openclaw/workspace/skills/digest-pipeline-monitor
python scripts/check_pipeline.py
```

### Generate emergency digest for user
```bash
python scripts/emergency_digest.py --user-id b419d8ad5d23513f --reason "pipeline_stalled"
```

### Monitor digest delivery rates
```bash
python scripts/monitor_delivery.py --window 24h --threshold 50
```

## How it works

1. **Health Monitoring**: Checks digest delivery metrics vs expected baseline
2. **Stall Detection**: Identifies when pipeline attempts drop to 0 for >2h
3. **Infrastructure Check**: Validates Dropper-Code, Hub scheduler status
4. **Emergency Mode**: Manual digest generation bypassing failed automation
5. **Escalation**: Alerts when manual intervention required

## Configuration

**Hub API endpoint**: Uses HUB_API_KEY for dashboard metrics
**Alert thresholds**:
- Warning: <75% expected delivery rate
- Critical: <50% expected delivery rate  
- Emergency: 0 attempts for >2 hours

**Expected baselines**:
- 109 total users, ~80 daily digest recipients
- Peak delivery window: 14:00-16:00 UTC
- Normal delivery rate: 70-85% of eligible users

## Scripts

### `scripts/check_pipeline.py`
Core pipeline health check with JSON output for automation integration.

**Returns:**
- Current delivery metrics (sent/expected)
- Pipeline status (healthy/degraded/stalled/failed)
- Infrastructure health (Hub, Dropper-Code)
- Runway estimates for manual intervention

### `scripts/emergency_digest.py`  
Manual digest generation for critical users when automation fails.

**Features:**
- Bypass failed Dropper-Code service
- Generate digest from recent drops
- Email delivery via Resend API
- Audit trail for manual interventions

### `scripts/monitor_delivery.py`
Continuous monitoring with alerting for proactive failure detection.

**Monitors:**
- Digest delivery rates vs historical baseline
- Error spike detection in Hub logs
- Dropper-Code service health and credit status
- Recovery time estimates based on infrastructure status

## Integration points

**Works with existing agents:**
- Chief of Staff: Provides pipeline metrics for daily reports
- UserHealth: Identifies users missing digests for retention
- OpsMonitor: Infrastructure health correlation
- Patrol: Hub API health validation

**Data sources:**
- Hub dashboard API (`/api/ops/dashboard`)
- Resend delivery metrics
- Dropper-Code task queue status
- Individual user digest preferences

## Trigger patterns

**Automatic triggers:**
- Scheduled health checks (every 30min)
- Alert webhooks from Hub error monitoring
- User complaint ingestion via support channels

**Manual triggers:**
- "Check digest pipeline" or "Why no digest?"
- "Generate emergency digest for [user]"
- "Pipeline health report"

## Emergency procedures

**When Dropper-Code fails:**
1. Validate credit/usage limits (Claude Code, OpenAI)
2. Check task queue for stuck jobs
3. Manual digest generation for VIP users (Joey, family)
4. Estimate recovery timeline based on credit reset schedule

**When Hub scheduler stalls:**
1. Check Hub service health and recent deployments
2. Validate digest cron job configuration
3. Manual scheduler restart via Railway API if needed
4. Temporary digest generation pipeline bypassing scheduler

**When mass delivery failure:**
1. Check Resend API health and quota
2. Validate email templates and delivery endpoints
3. Staged recovery: VIP users first, then general population
4. Communication plan for affected users

## Testing

```bash
# Test pipeline health check
python scripts/test_pipeline_check.py

# Test emergency digest generation (dry run)
python scripts/test_emergency_digest.py --dry-run

# Test monitoring with mock data
python scripts/test_monitor.py --mock-failure
```

## Success metrics

- **Detection latency**: Pipeline failures detected within 30min
- **Recovery time**: Manual intervention completed within 2h of detection
- **User impact**: Critical users (family, VIPs) never miss >1 digest
- **Communication**: Affected users notified within 4h of mass failure

## Related skills

- **poe-balance-guardian**: Infrastructure monitoring patterns
- **family-retention-guardian**: VIP user identification
- **heartbeat-consolidator**: Health check aggregation (when available)

---

**Created**: 2026-03-18 06:52 UTC  
**Evidence**: Core product 98% failure rate, 7+ hour stall, 0 execution despite perfect detection  
**Pattern 299**: Atomic scope skill to solve execution paralysis in digest delivery  
**Priority**: CRITICAL - Core product failure affecting 107/109 users