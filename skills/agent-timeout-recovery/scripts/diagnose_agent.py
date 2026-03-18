#!/usr/bin/env python3
"""Diagnose agent timeout failures by analyzing logs and state."""

import argparse
import json
import os
import glob
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

WORKSPACE = os.environ.get("OPENCLAW_WORKSPACE", "/root/.openclaw/workspace")
STATE_DIR = os.environ.get("OPENCLAW_STATE", "/root/.openclaw")
AGENTS_DIR = os.path.join(STATE_DIR, "agents")


def find_agent_logs(agent_name: str) -> list[str]:
    """Find log files related to the agent."""
    patterns = [
        os.path.join(STATE_DIR, "**", f"*{agent_name.lower().replace(' ', '*')}*"),
        os.path.join(STATE_DIR, "logs", "**", "*.log"),
    ]
    files = []
    for p in patterns:
        files.extend(glob.glob(p, recursive=True))
    return files


def parse_session_failures(agent_name: str) -> dict:
    """Check agent session directories for failure indicators."""
    sessions_dir = os.path.join(AGENTS_DIR, "main", "sessions")
    failures = []
    
    if not os.path.isdir(sessions_dir):
        return {"consecutive_failures": 0, "failures": [], "source": "no_sessions_dir"}

    for f in sorted(os.listdir(sessions_dir), reverse=True)[:50]:
        fpath = os.path.join(sessions_dir, f)
        if not os.path.isfile(fpath):
            continue
        try:
            content = open(fpath, "r", errors="ignore").read(4096)
            if agent_name.lower() in content.lower() and any(
                kw in content.lower() for kw in ["timeout", "error", "fail", "timed out"]
            ):
                failures.append({"file": f, "snippet": content[:200]})
        except Exception:
            continue

    return {
        "consecutive_failures": len(failures),
        "failures": failures[:10],
        "source": "session_scan",
    }


def check_gateway_health() -> dict:
    """Check if the OpenClaw gateway is responsive."""
    import subprocess
    try:
        r = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
             "--max-time", "10", "http://localhost:8080/health"],
            capture_output=True, text=True, timeout=15,
        )
        code = r.stdout.strip()
        return {"gateway_healthy": code == "200", "http_code": code}
    except Exception as e:
        return {"gateway_healthy": False, "error": str(e)}


def check_system_resources() -> dict:
    """Check CPU, memory, disk."""
    import subprocess
    info = {}
    try:
        r = subprocess.run(["df", "-h", "/root/.openclaw"], capture_output=True, text=True, timeout=5)
        lines = r.stdout.strip().split("\n")
        if len(lines) >= 2:
            parts = lines[1].split()
            info["disk_use_pct"] = parts[4] if len(parts) > 4 else "unknown"
    except Exception:
        info["disk_use_pct"] = "unknown"

    try:
        with open("/proc/meminfo") as f:
            mem = f.read()
        total = int(re.search(r"MemTotal:\s+(\d+)", mem).group(1))
        avail = int(re.search(r"MemAvailable:\s+(\d+)", mem).group(1))
        info["mem_available_pct"] = round(avail / total * 100, 1)
    except Exception:
        info["mem_available_pct"] = "unknown"

    try:
        with open("/proc/loadavg") as f:
            info["load_avg_1m"] = float(f.read().split()[0])
    except Exception:
        info["load_avg_1m"] = "unknown"

    return info


def diagnose(agent_name: str) -> dict:
    """Run full diagnosis for an agent."""
    result = {
        "agent": agent_name,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "diagnosis": "unknown",
        "details": {},
    }

    # 1. Check session failures
    session_data = parse_session_failures(agent_name)
    result["details"]["sessions"] = session_data

    # 2. Check gateway
    gw = check_gateway_health()
    result["details"]["gateway"] = gw

    # 3. Check resources
    res = check_system_resources()
    result["details"]["resources"] = res

    # 4. Determine diagnosis
    if not gw.get("gateway_healthy"):
        result["diagnosis"] = "upstream_failure"
    elif isinstance(res.get("mem_available_pct"), (int, float)) and res["mem_available_pct"] < 10:
        result["diagnosis"] = "resource_exhaustion"
    elif isinstance(res.get("load_avg_1m"), (int, float)) and res["load_avg_1m"] > 4.0:
        result["diagnosis"] = "resource_exhaustion"
    elif session_data["consecutive_failures"] >= 3:
        result["diagnosis"] = "timeout_cascade"
    else:
        result["diagnosis"] = "config_error"

    # 5. Find related logs
    logs = find_agent_logs(agent_name)
    result["details"]["related_log_files"] = logs[:5]

    return result


def main():
    parser = argparse.ArgumentParser(description="Diagnose agent timeout failures")
    parser.add_argument("--agent", required=True, help="Agent name to diagnose")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    result = diagnose(args.agent)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"=== Diagnosis: {result['agent']} ===")
        print(f"Diagnosis: {result['diagnosis']}")
        print(f"Gateway healthy: {result['details']['gateway'].get('gateway_healthy')}")
        print(f"Memory available: {result['details']['resources'].get('mem_available_pct')}%")
        print(f"Load avg (1m): {result['details']['resources'].get('load_avg_1m')}")
        print(f"Session failures found: {result['details']['sessions']['consecutive_failures']}")
        if result["details"]["related_log_files"]:
            print(f"Related logs: {', '.join(result['details']['related_log_files'][:3])}")
        print(f"\nFull result: {json.dumps(result, indent=2)}")

    return 0 if result["diagnosis"] != "unknown" else 1


if __name__ == "__main__":
    sys.exit(main())
