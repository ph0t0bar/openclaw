---
name: heartbeat-consolidator
description: Consolidates redundant system health checks across multiple agents to prevent API overlap and reduce duplicate Hub calls. Single source of truth for system metrics with intelligent agent notification. Use when multiple agents need same health metrics, during 30min heartbeat cycles, when API rate limits are approached, or for heartbeat optimization.
---

# Heartbeat Consolidator

Eliminates redundant health checks across agents by providing a single source of truth for system metrics with intelligent distribution.

## Problem This Solves

**DETECTED PATTERN**: 3+ agents doing identical health checks every 30 minutes
- **Chief of Staff**: Checks DA users/drops, BHA stats, Poe balance, digest status
- **Ops Monitor**: Checks identical DA/BHA/Poe metrics, Stripe, Resend, errors
- **Unified Ops Monitor**: Duplicate of Ops Monitor with same API calls
- **Result**: 20+ duplicate Hub API calls per day for identical data

**Evidence from sessions 2026-03-17/18**:
```
Chief of Staff, Patrol, OpsMonitor running same Hub API calls
Same metrics: users/drops/digests/poe/stripe/errors
20+ duplicate health checks per day
```

## When to Use

**Automatic triggers:**
- Multiple agents requesting same health metrics within 30min window
- API rate limit warnings from Hub dashboard endpoint
- Heartbeat optimization cycles

**Manual triggers:**
- "Consolidate heartbeats" or "Optimize health checks"
- "Single source system metrics" 
- "Reduce API overlap"

## How It Works

1. **Unified Collection**: Single agent fetches all system metrics every 30min
2. **Smart Caching**: Stores results in shared memory for agent access
3. **Intelligent Distribution**: Each agent gets only relevant metric slice
4. **Change Detection**: Only alerts when metrics actually change
5. **Emergency Override**: Critical alerts bypass consolidation delays

## Core Components

### 1. Master Health Collector
```bash
python scripts/collect_health.py
```
- Fetches Hub dashboard (`/api/ops/dashboard`)
- Collects Stripe, Resend, GitHub CI, Dropper-Code status
- Caches results with 30min TTL
- Generates change-only alerts

### 2. Agent Health Distributor
```bash
python scripts/distribute_health.py --agent chief-of-staff
python scripts/distribute_health.py --agent ops-monitor  
```
- Filters cached metrics by agent needs
- Returns only changed/relevant data
- Prevents duplicate alerts across agents

### 3. Health Status API
```bash
python scripts/health_api.py --port 8081
```
- Local HTTP endpoint for agents to query
- Cached responses reduce Hub API load
- Agent-specific metric filtering
- Change detection and alerting

## Agent Integration

### Chief of Staff
Gets: Digest pipeline status, family user metrics, CI failures, critical escalations
```bash
curl http://localhost:8081/health/chief-of-staff
```

### Ops Monitor  
Gets: DA/BHA user counts, Poe balance, Stripe revenue, error counts
```bash
curl http://localhost:8081/health/ops-monitor
```

### UserHealth
Gets: User activity metrics, engagement scores, family member status
```bash
curl http://localhost:8081/health/user-health
```

## Configuration

**Cache Settings** (`config/heartbeat.json`):
```json
{
  "cache_ttl_seconds": 1800,
  "collection_interval": 1800,
  "emergency_override_keywords": ["critical", "down", "failed", "error"],
  "agent_filters": {
    "chief-of-staff": ["digest_pipeline", "family_users", "ci_status"],
    "ops-monitor": ["da_users", "bha_users", "poe_balance", "stripe"],
    "user-health": ["active_users", "engagement", "family_members"]
  }
}
```

**Hub API Settings**:
- Endpoint: `HUB_API_KEY` for dashboard access
- Rate limit: 60 requests/hour (consolidated = 2 requests/hour)
- Fallback: Individual agent calls if consolidator fails

## Scripts

### `scripts/collect_health.py`
Master collector that fetches all system metrics and caches results.

**Features:**
- Hub dashboard API integration
- Multi-service health aggregation
- Change detection with diff tracking
- Emergency alert bypass for critical status

### `scripts/distribute_health.py`
Intelligent distribution of cached metrics to requesting agents.

**Usage:**
```bash
# Get metrics for specific agent
python scripts/distribute_health.py --agent chief-of-staff

# Check what metrics are available
python scripts/distribute_health.py --list-metrics

# Get only changed metrics since last check
python scripts/distribute_health.py --agent ops-monitor --changes-only
```

### `scripts/health_api.py`
Local HTTP server for agent metric access with filtering and caching.

**Endpoints:**
- `GET /health/{agent-name}` - Filtered metrics for specific agent
- `GET /health/all` - Complete system status (emergency use)
- `GET /health/changes` - Only metrics that changed recently
- `POST /health/collect` - Force immediate metric collection

## Success Metrics

**Efficiency Gains:**
- API calls reduced from 20+/day to 2/day (90% reduction)
- Agent response time improved (cached vs API calls)
- Hub API rate limit headroom increased

**Reliability Improvements:**
- Single point of metric collection reduces inconsistency
- Change detection prevents alert fatigue
- Emergency override ensures critical alerts reach agents

**Agent Coordination:**
- No duplicate alerts for same issue
- Consistent metric definitions across agents
- Reduced bandwidth and processing overhead

## Emergency Procedures

**If Consolidator Fails:**
1. Agents automatically fallback to direct Hub API calls
2. Emergency override bypasses cache for critical alerts
3. Local fallback uses last cached data with staleness warnings

**Critical Alert Override:**
- Keywords: "critical", "down", "failed", "error" bypass consolidation
- Family member alerts always bypass (personal priority)
- Digest pipeline failures trigger immediate distribution

## Integration Points

**Works with existing agents:**
- **Chief of Staff**: Gets digest/family/CI status without API calls
- **Ops Monitor**: Receives cached DA/BHA metrics efficiently  
- **UserHealth**: Family member tracking with change detection
- **Patrol**: Infrastructure monitoring without Hub API pressure

**Data sources:**
- Hub dashboard API (primary)
- Stripe API (payment status)
- Resend API (email delivery)
- GitHub API (CI status)
- Dropper-Code status endpoint

## Testing

```bash
# Test metric collection
python scripts/test_collection.py

# Test agent distribution
python scripts/test_distribution.py --agent chief-of-staff

# Test API server
python scripts/test_api.py --port 8081

# Test emergency override
python scripts/test_emergency.py --simulate-critical
```

## Implementation Notes

**Caching Strategy:**
- 30min cache TTL matches agent heartbeat cycles
- Change detection prevents stale alert repetition  
- Emergency keywords bypass all caching

**Agent Migration:**
- Agents check consolidator first, fallback to direct API
- Gradual rollout prevents service disruption
- Monitoring ensures no metric gaps during migration

## Related Skills

- **digest-pipeline-monitor**: Uses consolidated metrics for pipeline health
- **family-retention-guardian**: Gets family member data efficiently
- **poe-balance-guardian**: Receives Poe balance from consolidated source

---

**Created**: 2026-03-18 08:27 UTC  
**Evidence**: 20+ duplicate Hub API calls/day across Chief of Staff, Ops Monitor, Unified Ops Monitor  
**Pattern**: Agent coordination inefficiency causing API overhead  
**Priority**: MEDIUM - Efficiency optimization for infrastructure health