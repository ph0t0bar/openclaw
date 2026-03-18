---
name: agent-timeout-monitor
description: Monitors OpenClaw agent health, detects timeout patterns, and provides recovery recommendations. Use when agent failures exceed 3 consecutive cycles, system success rate drops below 95%, or infrastructure strain is detected through timeout clusters. Provides automated recovery procedures and prompt optimization recommendations.
---

# Agent Timeout Monitor

Monitors OpenClaw agent ecosystem health and provides automated recovery when infrastructure strain causes timeout clusters.

## When to use this skill

- Agent failures exceed 3 consecutive cycles for any agent
- System-wide success rate drops below 95% target
- Infrastructure strain detected (multiple agents timing out)
- Need to diagnose recurring timeout patterns
- Agent optimization or disable/restart procedures required

## Problem this solves

**CRITICAL: Infrastructure degradation detected 2026-03-18**
- DocBot: 8 consecutive failures (91% failure rate)
- Creative Review Emailer: 4 consecutive failures
- SkillMiner: 3 consecutive failures
- Meta oversight: 91% failure rate
- Governance: 100% failure rate (7/7 cycles)
- System-wide success rate: 73% (below 95% target)

Pattern: Agent timeout clusters correlate with infrastructure strain and need proactive intervention before system-wide failures cascade.

## Evidence from sessions

**Agent Timeout Crisis (Pattern 291)**:
- DocBot timeout cluster escalating (8 consecutive failures)
- Multiple agents hitting similar patterns simultaneously
- No automated recovery or self-healing response
- Manual intervention required but no clear procedure

**Infrastructure correlation**:
- Higher timeout rates during peak agent activity
- Certain agents more susceptible (DocBot, Meta, Governance)
- Timeout clusters predict broader system instability

## Quick start

### Check agent health dashboard
```bash
cd /root/.openclaw/workspace/skills/agent-timeout-monitor
python3 scripts/check_agent_health.py
```

### Analyze timeout patterns for specific agent
```bash
python3 scripts/analyze_timeouts.py --agent DocBot --window 24h
```

### Generate recovery recommendations
```bash
python3 scripts/recovery_recommendations.py --threshold 3
```

## How it works

1. **Health Monitoring**: Tracks agent success/failure patterns across all cron jobs
2. **Pattern Detection**: Identifies timeout clusters and infrastructure strain
3. **Root Cause Analysis**: Correlates timeouts with system load, prompt complexity
4. **Recovery Procedures**: Automated prompt optimization, restart procedures
5. **Escalation**: Recommends agent disable/reconfiguration when needed

## Configuration

**Agent health thresholds**:
- Warning: 2 consecutive failures
- Critical: 3+ consecutive failures
- Emergency: >90% failure rate over 6+ cycles

**System health targets**:
- Normal: >95% success rate
- Degraded: 85-95% success rate
- Critical: <85% success rate

## Scripts

### `scripts/check_agent_health.py`
Real-time agent health dashboard with timeout pattern analysis.

**Returns:**
- Per-agent success/failure statistics
- Timeout cluster detection
- System-wide health metrics
- Infrastructure correlation indicators

### `scripts/analyze_timeouts.py`
Deep analysis of timeout patterns for specific agents or time windows.

**Features:**
- Timeout frequency analysis
- Correlation with system events
- Prompt complexity scoring
- Recovery time estimation

### `scripts/recovery_recommendations.py`
Automated recovery procedure generation based on timeout patterns.

**Provides:**
- Prompt optimization suggestions
- Agent restart procedures
- Disable/reconfigure recommendations
- Infrastructure scaling guidance

## Integration points

**Works with existing agents:**
- Meta: Provides agent performance data for oversight
- Chief of Staff: Infrastructure health correlation
- Governance: Constitutional health monitoring
- All agents: Health status and optimization feedback

**Data sources:**
- Agent status JSON from dashboard
- Cron job execution logs
- System performance metrics
- Agent configuration files

## Recovery procedures

**Timeout cluster response:**
1. Identify affected agent subset
2. Analyze common failure patterns
3. Apply prompt optimization or restart procedures
4. Monitor recovery effectiveness

**Individual agent optimization:**
1. Analyze recent failure patterns
2. Identify prompt complexity or resource issues
3. Generate optimization recommendations
4. Test recovery with controlled restart

**System-wide intervention:**
1. Assess infrastructure capacity
2. Prioritize critical agents for recovery
3. Implement staged restart procedures
4. Monitor system stability during recovery

## Success metrics

- **Detection speed**: Timeout patterns identified within 30min
- **Recovery time**: Agent health restored within 2h of intervention
- **System stability**: >95% success rate maintained
- **Proactive intervention**: Prevent timeout clusters from cascading

## Related skills

- **digest-pipeline-monitor**: Infrastructure monitoring patterns
- **execution-decomposer**: Task complexity analysis
- **heartbeat-consolidator**: System health aggregation (when available)

---

**Created**: 2026-03-18 07:40 UTC
**Evidence**: 73% system success rate, 8+ consecutive agent failures, infrastructure strain
**Pattern 291**: Agent timeout crisis requiring proactive intervention
**Priority**: HIGH - Infrastructure health critical for system stability