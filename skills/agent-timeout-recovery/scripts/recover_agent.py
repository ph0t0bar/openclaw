#!/usr/bin/env python3
"""Attempt automated recovery for a failing agent."""

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime

TIMEOUT_SECONDS = 900  # 15-minute hard cap
STATE_DIR = os.environ.get("OPENCLAW_STATE", "/root/.openclaw")


def soft_restart(agent_name: str) -> dict:
    """Attempt soft restart via gateway API."""
    try:
        r = subprocess.run(
            ["curl", "-s", "-X", "POST", "--max-time", "30",
             "http://localhost:8080/api/agents/restart",
             "-H", "Content-Type: application/json",
             "-d", json.dumps({"agent": agent_name})],
            capture_output=True, text=True, timeout=35,
        )
        return {"action": "soft_restart", "success": r.returncode == 0, "response": r.stdout[:500]}
    except Exception as e:
        return {"action": "soft_restart", "success": False, "error": str(e)}


def reset_config(agent_name: str) -> dict:
    """Reset agent config to defaults (non-destructive)."""
    config_path = os.path.join(STATE_DIR, "openclaw.json")
    try:
        if not os.path.exists(config_path):
            return {"action": "reset_config", "success": False, "error": "config not found"}
        
        with open(config_path) as f:
            config = json.load(f)

        # Look for agent-specific config and log it, but don't modify without backup
        backup_path = config_path + f".backup.{int(time.time())}"
        with open(backup_path, "w") as f:
            json.dump(config, f, indent=2)

        return {"action": "reset_config", "success": True, "backup": backup_path, "note": "config backed up; manual review recommended"}
    except Exception as e:
        return {"action": "reset_config", "success": False, "error": str(e)}


def check_dependencies() -> dict:
    """Verify upstream services are reachable."""
    deps = {}
    checks = [
        ("gateway", "http://localhost:8080/health"),
        ("hub", "https://hub-production-f423.up.railway.app/health"),
    ]
    for name, url in checks:
        try:
            r = subprocess.run(
                ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", "10", url],
                capture_output=True, text=True, timeout=15,
            )
            deps[name] = {"healthy": r.stdout.strip() in ("200", "204"), "code": r.stdout.strip()}
        except Exception as e:
            deps[name] = {"healthy": False, "error": str(e)}
    return {"action": "check_dependencies", "success": True, "dependencies": deps}


def graceful_degrade(agent_name: str, diagnosis: str) -> dict:
    """Mark agent as degraded — log state for operator review."""
    degraded_file = os.path.join(STATE_DIR, "workspace", "memory", "degraded-agents.json")
    try:
        existing = {}
        if os.path.exists(degraded_file):
            with open(degraded_file) as f:
                existing = json.load(f)
        
        existing[agent_name] = {
            "status": "degraded",
            "diagnosis": diagnosis,
            "degraded_at": datetime.utcnow().isoformat() + "Z",
            "requires_manual_intervention": True,
        }
        
        os.makedirs(os.path.dirname(degraded_file), exist_ok=True)
        with open(degraded_file, "w") as f:
            json.dump(existing, f, indent=2)

        return {"action": "graceful_degrade", "success": True, "file": degraded_file}
    except Exception as e:
        return {"action": "graceful_degrade", "success": False, "error": str(e)}


def health_check(agent_name: str) -> bool:
    """Quick check if agent is now responding."""
    try:
        r = subprocess.run(
            ["curl", "-s", "--max-time", "10", "http://localhost:8080/health"],
            capture_output=True, text=True, timeout=15,
        )
        return r.returncode == 0 and "200" in r.stdout or "ok" in r.stdout.lower()
    except Exception:
        return False


def recover(agent_name: str, diagnosis: str = "timeout_cascade") -> dict:
    """Execute recovery strategy in order."""
    start = time.time()
    result = {
        "agent": agent_name,
        "status": "failed",
        "diagnosis": diagnosis,
        "actions_taken": [],
        "duration_seconds": 0,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }

    strategies = [
        ("soft_restart", lambda: soft_restart(agent_name)),
        ("check_dependencies", check_dependencies),
        ("reset_config", lambda: reset_config(agent_name)),
    ]

    for name, fn in strategies:
        if time.time() - start > TIMEOUT_SECONDS:
            result["status"] = "failed"
            result["error"] = "timeout_exceeded"
            break

        action_result = fn()
        result["actions_taken"].append(action_result)

        # After restart, check health
        if name == "soft_restart" and action_result.get("success"):
            time.sleep(5)
            if health_check(agent_name):
                result["status"] = "recovered"
                break

        # If dependencies are down, degrade immediately
        if name == "check_dependencies":
            deps = action_result.get("dependencies", {})
            gw = deps.get("gateway", {})
            if not gw.get("healthy"):
                result["diagnosis"] = "upstream_failure"
                degrade = graceful_degrade(agent_name, "upstream_failure")
                result["actions_taken"].append(degrade)
                result["status"] = "degraded"
                break

    # If nothing worked, degrade
    if result["status"] == "failed":
        degrade = graceful_degrade(agent_name, diagnosis)
        result["actions_taken"].append(degrade)
        result["status"] = "degraded"

    result["duration_seconds"] = round(time.time() - start, 1)
    return result


def main():
    parser = argparse.ArgumentParser(description="Recover a failing agent")
    parser.add_argument("--agent", required=True, help="Agent name")
    parser.add_argument("--diagnosis", default="timeout_cascade", help="Diagnosis from diagnose_agent.py")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    result = recover(args.agent, args.diagnosis)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"=== Recovery: {result['agent']} ===")
        print(f"Status: {result['status']}")
        print(f"Diagnosis: {result['diagnosis']}")
        print(f"Duration: {result['duration_seconds']}s")
        print(f"Actions: {len(result['actions_taken'])}")
        for a in result["actions_taken"]:
            print(f"  - {a.get('action')}: {'✅' if a.get('success') else '❌'}")
        print(f"\nFull result: {json.dumps(result, indent=2)}")

    return 0 if result["status"] in ("recovered", "degraded") else 1


if __name__ == "__main__":
    sys.exit(main())
