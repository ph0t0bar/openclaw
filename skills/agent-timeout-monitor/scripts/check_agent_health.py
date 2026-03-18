#!/usr/bin/env python3
"""
Agent Health Monitor - Real-time dashboard for OpenClaw agent timeout patterns

Usage:
    python3 check_agent_health.py [--json] [--threshold N]
    
Returns agent health status with timeout pattern detection and infrastructure correlation.
"""

import json
import sys
import argparse
from datetime import datetime, timedelta
from pathlib import Path

def load_agent_status():
    """Load agent status from dashboard JSON."""
    try:
        status_path = Path("/root/.openclaw/workspace/dashboard/agent-status.json")
        if not status_path.exists():
            return {"error": "Agent status file not found", "agents": {}}
        
        with open(status_path) as f:
            return json.load(f)
    except Exception as e:
        return {"error": f"Failed to load agent status: {e}", "agents": {}}

def analyze_agent_health(agents_data):
    """Analyze agent health patterns and detect timeout clusters."""
    health_summary = {
        "timestamp": datetime.utcnow().isoformat(),
        "system_health": {},
        "timeout_clusters": [],
        "critical_agents": [],
        "recommendations": []
    }
    
    if not agents_data:
        health_summary["system_health"]["status"] = "error"
        health_summary["recommendations"].append("Agent status data unavailable - check dashboard generation")
        return health_summary
    
    total_agents = len(agents_data)
    healthy_agents = 0
    timeout_agents = []
    consecutive_failures = {}
    
    # Analyze each agent
    for agent_name, agent_info in agents_data.items():
        if isinstance(agent_info, dict):
            # Extract failure patterns from recent runs
            recent_failures = 0
            consecutive_count = 0
            
            # Check for consecutive failure patterns
            if "recentRuns" in agent_info:
                runs = agent_info["recentRuns"][-10:]  # Last 10 runs
                
                # Count consecutive failures from most recent
                for run in reversed(runs):
                    if run.get("status") == "failed":
                        consecutive_count += 1
                    else:
                        break
                
                # Count total recent failures
                recent_failures = sum(1 for run in runs if run.get("status") == "failed")
            
            consecutive_failures[agent_name] = consecutive_count
            
            # Classify agent health
            if consecutive_count >= 3:
                timeout_agents.append({
                    "name": agent_name,
                    "consecutive_failures": consecutive_count,
                    "recent_failure_rate": recent_failures / min(len(agent_info.get("recentRuns", [])), 10),
                    "status": "critical"
                })
                health_summary["critical_agents"].append(agent_name)
            elif consecutive_count >= 2:
                timeout_agents.append({
                    "name": agent_name,
                    "consecutive_failures": consecutive_count,
                    "recent_failure_rate": recent_failures / min(len(agent_info.get("recentRuns", [])), 10),
                    "status": "warning"
                })
            else:
                healthy_agents += 1
    
    # System-wide health calculation
    success_rate = healthy_agents / total_agents if total_agents > 0 else 0
    health_summary["system_health"] = {
        "total_agents": total_agents,
        "healthy_agents": healthy_agents,
        "timeout_agents": len(timeout_agents),
        "success_rate": round(success_rate * 100, 1),
        "status": "critical" if success_rate < 0.85 else "degraded" if success_rate < 0.95 else "healthy"
    }
    
    # Detect timeout clusters (3+ agents with 2+ failures)
    cluster_agents = [name for name, count in consecutive_failures.items() if count >= 2]
    if len(cluster_agents) >= 3:
        health_summary["timeout_clusters"].append({
            "agents": cluster_agents,
            "severity": "high" if len(cluster_agents) >= 5 else "medium",
            "pattern": "infrastructure_strain"
        })
    
    health_summary["agent_details"] = timeout_agents
    
    # Generate recommendations
    if success_rate < 0.85:
        health_summary["recommendations"].append("CRITICAL: System-wide intervention required - success rate below 85%")
        health_summary["recommendations"].append("Recommend immediate infrastructure capacity review")
    
    if len(cluster_agents) >= 3:
        health_summary["recommendations"].append(f"Timeout cluster detected: {', '.join(cluster_agents)}")
        health_summary["recommendations"].append("Recommend prompt optimization and staged restart procedures")
    
    for agent in health_summary["critical_agents"]:
        failure_count = consecutive_failures[agent]
        health_summary["recommendations"].append(f"{agent}: {failure_count} consecutive failures - disable or restart required")
    
    return health_summary

def format_human_readable(health_data):
    """Format health data for human-readable output."""
    output = []
    output.append("=== OpenClaw Agent Health Dashboard ===")
    output.append(f"Generated: {health_data['timestamp']}")
    output.append()
    
    # System health
    sys_health = health_data["system_health"]
    status_icon = "🟢" if sys_health["status"] == "healthy" else "🟡" if sys_health["status"] == "degraded" else "🔴"
    output.append(f"{status_icon} System Health: {sys_health['status'].upper()}")
    output.append(f"   Success Rate: {sys_health['success_rate']}% ({sys_health['healthy_agents']}/{sys_health['total_agents']} agents)")
    output.append()
    
    # Timeout clusters
    if health_data["timeout_clusters"]:
        output.append("🚨 TIMEOUT CLUSTERS DETECTED:")
        for cluster in health_data["timeout_clusters"]:
            output.append(f"   {cluster['severity'].upper()}: {', '.join(cluster['agents'])}")
        output.append()
    
    # Critical agents
    if health_data["critical_agents"]:
        output.append("⚠️  CRITICAL AGENTS:")
        for agent_detail in health_data["agent_details"]:
            if agent_detail["status"] == "critical":
                icon = "🔴" if agent_detail["consecutive_failures"] >= 5 else "⚠️"
                output.append(f"   {icon} {agent_detail['name']}: {agent_detail['consecutive_failures']} consecutive failures")
        output.append()
    
    # Warning agents
    warning_agents = [a for a in health_data["agent_details"] if a["status"] == "warning"]
    if warning_agents:
        output.append("⚠️  WARNING AGENTS:")
        for agent in warning_agents:
            output.append(f"   🟡 {agent['name']}: {agent['consecutive_failures']} consecutive failures")
        output.append()
    
    # Recommendations
    if health_data["recommendations"]:
        output.append("💡 RECOMMENDATIONS:")
        for i, rec in enumerate(health_data["recommendations"], 1):
            output.append(f"   {i}. {rec}")
    
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description="Check OpenClaw agent health and timeout patterns")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    parser.add_argument("--threshold", type=int, default=3, help="Failure threshold for critical status")
    args = parser.parse_args()
    
    # Load agent status
    status_data = load_agent_status()
    agents = status_data.get("agents", {})
    
    # Analyze health
    health_data = analyze_agent_health(agents)
    
    # Output results
    if args.json:
        print(json.dumps(health_data, indent=2))
    else:
        print(format_human_readable(health_data))
    
    # Exit with appropriate code
    sys_status = health_data["system_health"]["status"]
    if sys_status == "critical":
        sys.exit(2)
    elif sys_status == "degraded":
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()