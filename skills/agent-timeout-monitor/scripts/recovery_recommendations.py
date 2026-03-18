#!/usr/bin/env python3
"""
Agent Recovery Recommendations Generator - Automated recovery procedures based on timeout patterns

Usage:
    python3 recovery_recommendations.py [--threshold N] [--json] [--execute]
    
Generates specific recovery procedures for agents with timeout patterns and optionally executes them.
"""

import json
import sys
import argparse
from datetime import datetime
from pathlib import Path
import subprocess

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

def analyze_failure_patterns(agents_data, threshold=3):
    """Identify agents needing recovery based on failure patterns."""
    recovery_candidates = []
    
    for agent_name, agent_data in agents_data.items():
        if not isinstance(agent_data, dict) or "recentRuns" not in agent_data:
            continue
        
        runs = agent_data["recentRuns"]
        if not runs:
            continue
        
        # Count consecutive failures from most recent
        consecutive_failures = 0
        for run in reversed(runs):
            if run.get("status") == "failed":
                consecutive_failures += 1
            else:
                break
        
        # Calculate recent failure rate
        recent_runs = runs[-10:]  # Last 10 runs
        failure_rate = sum(1 for r in recent_runs if r.get("status") == "failed") / len(recent_runs)
        
        if consecutive_failures >= threshold or failure_rate > 0.7:
            recovery_candidates.append({
                "agent": agent_name,
                "consecutive_failures": consecutive_failures,
                "failure_rate": round(failure_rate * 100, 1),
                "severity": get_severity_level(consecutive_failures, failure_rate),
                "last_success": get_last_success_time(runs)
            })
    
    return sorted(recovery_candidates, key=lambda x: x["consecutive_failures"], reverse=True)

def get_severity_level(consecutive_failures, failure_rate):
    """Determine severity level based on failure patterns."""
    if consecutive_failures >= 8 or failure_rate > 0.9:
        return "critical"
    elif consecutive_failures >= 5 or failure_rate > 0.7:
        return "high"
    elif consecutive_failures >= 3 or failure_rate > 0.5:
        return "medium"
    else:
        return "low"

def get_last_success_time(runs):
    """Find the last successful run timestamp."""
    for run in reversed(runs):
        if run.get("status") == "success":
            return run.get("timestamp", "unknown")
    return "no_recent_success"

def generate_recovery_procedures(recovery_candidates):
    """Generate specific recovery procedures for each agent."""
    procedures = []
    
    for candidate in recovery_candidates:
        agent_name = candidate["agent"]
        severity = candidate["severity"]
        consecutive = candidate["consecutive_failures"]
        
        procedure = {
            "agent": agent_name,
            "severity": severity,
            "timestamp": datetime.utcnow().isoformat(),
            "analysis": candidate,
            "immediate_actions": [],
            "optimization_steps": [],
            "monitoring_plan": [],
            "success_criteria": [],
            "commands": []
        }
        
        # Generate immediate actions based on severity
        if severity == "critical":
            procedure["immediate_actions"] = [
                f"DISABLE {agent_name} immediately to prevent resource waste",
                "Investigate infrastructure capacity and bottlenecks",
                "Review prompt complexity and context window usage",
                "Check for memory leaks or resource exhaustion"
            ]
            procedure["commands"] = [
                f"# Disable {agent_name} cron job",
                f"cron disable {agent_name}",
                f"# Check system resources",
                "htop",
                "df -h",
                "free -m"
            ]
        
        elif severity == "high":
            procedure["immediate_actions"] = [
                f"Reduce {agent_name} execution frequency by 50%",
                "Optimize agent prompt for reduced complexity",
                "Clear any cached context that may be stale",
                "Monitor infrastructure correlation"
            ]
            procedure["commands"] = [
                f"# Temporarily reduce {agent_name} frequency",
                f"cron update {agent_name} --frequency reduced",
                f"# Clear agent context cache if applicable",
                f"rm -f /tmp/{agent_name}_cache_*"
            ]
        
        else:  # medium/low
            procedure["immediate_actions"] = [
                f"Monitor {agent_name} for 2 more cycles",
                "Check for recent prompt or configuration changes",
                "Validate input data quality",
                "Review timeout configuration"
            ]
        
        # Generate optimization steps
        optimization_steps = get_agent_optimizations(agent_name, consecutive)
        procedure["optimization_steps"] = optimization_steps
        
        # Monitoring plan
        procedure["monitoring_plan"] = [
            "Monitor success rate for next 6 cycles",
            "Track error patterns and types",
            "Correlate with system performance metrics",
            "Alert if pattern continues after intervention"
        ]
        
        # Success criteria
        procedure["success_criteria"] = [
            "Zero consecutive failures for 3+ cycles",
            f"Success rate above 90% over 10 cycles",
            "Error rate below 10% sustained",
            "No timeout clusters involving this agent"
        ]
        
        procedures.append(procedure)
    
    return procedures

def get_agent_optimizations(agent_name, consecutive_failures):
    """Get agent-specific optimization recommendations."""
    base_optimizations = [
        "Review and simplify agent prompt",
        "Reduce context window usage",
        "Optimize API call patterns",
        "Check timeout configuration"
    ]
    
    # Agent-specific optimizations
    specific_optimizations = {
        "DocBot": [
            "Split large PRD updates into smaller chunks",
            "Cache Hub API responses for 5 minutes",
            "Reduce documentation processing complexity",
            "Use incremental update patterns vs full rewrites"
        ],
        "Meta": [
            "Simplify agent evaluation criteria",
            "Reduce scorecard calculation frequency",
            "Cache pattern recognition results",
            "Use sampling for large agent datasets"
        ],
        "Governance": [
            "Streamline constitution checking logic", 
            "Cache roster validation results",
            "Reduce oversight scope during stable periods",
            "Use diff-based change detection"
        ],
        "Chief of Staff": [
            "Consolidate health check API calls",
            "Cache infrastructure status for 2 minutes",
            "Simplify crisis detection logic",
            "Use event-based vs polling architecture"
        ],
        "UserHealth": [
            "Optimize user query patterns",
            "Cache engagement calculations",
            "Use batch user processing",
            "Reduce family detection complexity"
        ],
        "ContentBot": [
            "Reduce content generation scope",
            "Cache voice pattern analysis",
            "Use template-based vs generative approach",
            "Optimize content validation logic"
        ]
    }
    
    optimizations = base_optimizations.copy()
    if agent_name in specific_optimizations:
        optimizations.extend(specific_optimizations[agent_name])
    
    # Add severity-based recommendations
    if consecutive_failures >= 8:
        optimizations.extend([
            "Consider complete agent redesign",
            "Implement circuit breaker pattern",
            "Add exponential backoff",
            "Split agent into smaller components"
        ])
    elif consecutive_failures >= 5:
        optimizations.extend([
            "Implement retry logic with backoff",
            "Add graceful degradation modes",
            "Improve error handling and recovery",
            "Add health check endpoint"
        ])
    
    return optimizations

def execute_recovery_commands(procedures, dry_run=True):
    """Execute recovery commands for agents (with dry run option)."""
    execution_results = []
    
    for procedure in procedures:
        agent_name = procedure["agent"]
        commands = procedure["commands"]
        
        result = {
            "agent": agent_name,
            "executed": [],
            "errors": [],
            "dry_run": dry_run
        }
        
        for command in commands:
            if command.startswith("#"):
                # Comment, skip
                continue
                
            try:
                if dry_run:
                    result["executed"].append(f"[DRY RUN] {command}")
                else:
                    # Execute actual command
                    subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
                    result["executed"].append(command)
                    
            except subprocess.CalledProcessError as e:
                error_msg = f"Command failed: {command} - {e.stderr}"
                result["errors"].append(error_msg)
        
        execution_results.append(result)
    
    return execution_results

def format_procedures_output(procedures, execution_results=None):
    """Format recovery procedures for human-readable output."""
    if not procedures:
        return "No agents require recovery procedures at this time."
    
    output = []
    output.append("=== Agent Recovery Procedures ===")
    output.append(f"Generated: {datetime.utcnow().isoformat()}")
    output.append(f"Agents requiring intervention: {len(procedures)}")
    output.append()
    
    for procedure in procedures:
        agent_name = procedure["agent"]
        severity = procedure["severity"]
        consecutive = procedure["analysis"]["consecutive_failures"]
        failure_rate = procedure["analysis"]["failure_rate"]
        
        severity_icon = "🔴" if severity == "critical" else "⚠️" if severity == "high" else "🟡"
        output.append(f"{severity_icon} {agent_name.upper()} - {severity.upper()} PRIORITY")
        output.append(f"   Consecutive Failures: {consecutive}")
        output.append(f"   Failure Rate: {failure_rate}%")
        output.append()
        
        output.append("   IMMEDIATE ACTIONS:")
        for i, action in enumerate(procedure["immediate_actions"], 1):
            output.append(f"   {i}. {action}")
        output.append()
        
        output.append("   OPTIMIZATION STEPS:")
        for i, step in enumerate(procedure["optimization_steps"][:5], 1):  # Show top 5
            output.append(f"   {i}. {step}")
        output.append()
        
        output.append("   SUCCESS CRITERIA:")
        for criterion in procedure["success_criteria"]:
            output.append(f"   ✓ {criterion}")
        output.append()
        
        if procedure["commands"]:
            output.append("   COMMANDS TO EXECUTE:")
            for cmd in procedure["commands"]:
                output.append(f"   $ {cmd}")
            output.append()
        
        output.append("-" * 80)
        output.append()
    
    # Add execution results if available
    if execution_results:
        output.append("=== Execution Results ===")
        for result in execution_results:
            agent = result["agent"]
            output.append(f"{agent}:")
            if result["executed"]:
                output.append("   Executed:")
                for cmd in result["executed"]:
                    output.append(f"   ✓ {cmd}")
            if result["errors"]:
                output.append("   Errors:")
                for error in result["errors"]:
                    output.append(f"   ✗ {error}")
            output.append()
    
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description="Generate agent recovery recommendations")
    parser.add_argument("--threshold", type=int, default=3, help="Failure threshold for recovery consideration")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    parser.add_argument("--execute", action="store_true", help="Execute recovery commands (default is dry run)")
    args = parser.parse_args()
    
    # Load agent data
    status_data = load_agent_status()
    agents = status_data.get("agents", {})
    
    if "error" in status_data:
        print(f"Error loading agent data: {status_data['error']}", file=sys.stderr)
        sys.exit(1)
    
    # Analyze failure patterns
    recovery_candidates = analyze_failure_patterns(agents, args.threshold)
    
    # Generate recovery procedures
    procedures = generate_recovery_procedures(recovery_candidates)
    
    # Execute commands if requested
    execution_results = None
    if procedures and (args.execute or not args.json):
        execution_results = execute_recovery_commands(procedures, dry_run=not args.execute)
    
    # Output results
    if args.json:
        output_data = {
            "procedures": procedures,
            "execution_results": execution_results,
            "summary": {
                "agents_analyzed": len(agents),
                "recovery_candidates": len(recovery_candidates),
                "procedures_generated": len(procedures)
            }
        }
        print(json.dumps(output_data, indent=2))
    else:
        print(format_procedures_output(procedures, execution_results))

if __name__ == "__main__":
    main()