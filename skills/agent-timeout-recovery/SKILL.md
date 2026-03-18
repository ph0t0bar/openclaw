---
name: agent-timeout-recovery
description: Diagnose and recover agents with >3 consecutive timeout failures. Atomic scope — one agent at a time, <15 min, clear success/fail.
trigger: Agent timeout >3 consecutive failures, Pattern 302 (Agent Timeout Cluster)
version: 1.0.0
---

# Agent Timeout Recovery

Automated diagnosis and recovery for agents experiencing consecutive timeout failures.

## When to Use

- An agent has 3+ consecutive timeout failures
- Multiple agents are failing (run once per agent, sequentially)
- Infrastructure strain detected before a launch or critical period

## How It Works

1. **Diagnose** — `scripts/diagnose_agent.py` analyzes the agent's failure pattern (log timestamps, error types, resource state)
2. **Recover** — `scripts/recover_agent.py` attempts recovery (restart, config reset, dependency check, graceful degradation)
3. **Verify** — Confirms agent is healthy or flags for manual intervention

## Usage

```bash
# Diagnose a specific agent
python3 scripts/diagnose_agent.py --agent "DocBot"

# Attempt recovery
python3 scripts/recover_agent.py --agent "DocBot"

# Run tests
python3 scripts/test_recovery.py
```

## Pattern 299 Compliance

| Constraint | Implementation |
|-----------|---------------|
| Single responsibility | One agent per invocation |
| Time-bounded | 15-minute hard timeout on recovery |
| Clear success criteria | Agent responds to health check OR marked degraded |
| Dependency-free | Uses only stdlib + OpenClaw APIs |

## Recovery Strategy (ordered)

1. **Soft restart** — Send restart signal via OpenClaw gateway
2. **Config reset** — Reset agent config to last-known-good
3. **Dependency check** — Verify upstream services (gateway, APIs)
4. **Graceful degradation** — Disable agent, notify operator, log state

## Output

Recovery produces a JSON result:

```json
{
  "agent": "DocBot",
  "status": "recovered|degraded|failed",
  "diagnosis": "timeout_cascade|resource_exhaustion|upstream_failure|config_error",
  "actions_taken": ["soft_restart"],
  "duration_seconds": 12,
  "timestamp": "2026-03-17T23:56:00Z"
}
```

## Escalation

If recovery fails, the skill outputs a summary for manual intervention. It does NOT retry indefinitely or chain to other skills.
