#!/usr/bin/env python3
"""
Agent Timeout Pattern Analyzer - Deep analysis of specific agent timeout patterns

Usage:
    python3 analyze_timeouts.py --agent <agent_name> [--window 24h] [--json]
    python3 analyze_timeouts.py --all [--window 24h] [--json]
    
Analyzes timeout patterns, correlations, and provides specific recovery recommendations.
"""

import json
import sys
import argparse
from datetime import datetime, timedelta
from pathlib import Path
import re

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

def parse_time_window(window_str):
    """Parse time window string like '24h', '7d', '1w' into timedelta."""
    match = re.match(r'^(\d+)([hdw])$', window_str.lower())
    if not match:
        raise ValueError(f"Invalid time window format: {window_str}")
    
    value, unit = int(match.group(1)), match.group(2)
    if unit == 'h':
        return timedelta(hours=value)
    elif unit == 'd':
        return timedelta(days=value)
    elif unit == 'w':
        return timedelta(weeks=value)

def analyze_agent_timeouts(agent_name, agent_data, window=None):
    """Analyze timeout patterns for a specific agent."""
    analysis = {
        "agent": agent_name,
        "timestamp": datetime.utcnow().isoformat(),
        "window": window or "all_time",
        "pattern_analysis": {},
        "failure_correlation": {},
        "recovery_recommendations": []
    }
    
    if not isinstance(agent_data, dict) or "recentRuns" not in agent_data:
        analysis["error"] = f"No run data available for {agent_name}"
        return analysis
    
    runs = agent_data["recentRuns"]
    if window:
        # Filter runs by time window (assuming runs have timestamps)
        cutoff = datetime.utcnow() - window
        # Note: This would need actual timestamp data in the runs
        # For now, just use recent runs as proxy
        runs = runs[-min(len(runs), int(window.total_seconds() / 1800))]  # Assume 30min intervals
    
    # Pattern analysis
    total_runs = len(runs)
    failed_runs = [r for r in runs if r.get("status") == "failed"]
    success_runs = [r for r in runs if r.get("status") == "success"]
    
    analysis["pattern_analysis"] = {
        "total_runs": total_runs,
        "failed_runs": len(failed_runs),
        "success_runs": len(success_runs),
        "failure_rate": round(len(failed_runs) / total_runs * 100, 1) if total_runs > 0 else 0,
        "consecutive_failures": 0,
        "max_consecutive_failures": 0,
        "failure_streaks": []
    }
    
    # Analyze consecutive failure patterns
    current_streak = 0
    max_streak = 0
    streak_positions = []
    
    for i, run in enumerate(reversed(runs)):  # Start from most recent
        if run.get("status") == "failed":
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            if current_streak > 0:
                streak_positions.append((i - current_streak, current_streak))
            current_streak = 0
    
    if current_streak > 0:  # Ongoing streak
        streak_positions.append((0, current_streak))
    
    analysis["pattern_analysis"]["consecutive_failures"] = current_streak
    analysis["pattern_analysis"]["max_consecutive_failures"] = max_streak
    analysis["pattern_analysis"]["failure_streaks"] = streak_positions
    
    # Failure correlation analysis
    error_types = {}
    timing_patterns = {}
    
    for run in failed_runs:
        # Analyze error types (would need actual error data)
        error_type = run.get("error_type", "unknown")
        error_types[error_type] = error_types.get(error_type, 0) + 1
        
        # Timing analysis (would need timestamps)
        # For now, just placeholder
        timing_patterns["peak_hours"] = "Need timestamp data"
    
    analysis["failure_correlation"] = {
        "error_types": error_types,
        "timing_patterns": timing_patterns,
        "infrastructure_events": "Correlation analysis needs event log data"
    }
    
    # Generate specific recommendations
    failure_rate = analysis["pattern_analysis"]["failure_rate"]
    consecutive = analysis["pattern_analysis"]["consecutive_failures"]
    
    if consecutive >= 8:
        analysis["recovery_recommendations"].extend([
            "CRITICAL: 8+ consecutive failures - immediate intervention required",
            "Recommend disabling agent temporarily to prevent resource waste",
            "Investigate prompt complexity and context window issues",
            "Check for infrastructure bottlenecks during peak usage"
        ])
    elif consecutive >= 5:
        analysis["recovery_recommendations"].extend([
            "HIGH PRIORITY: 5+ consecutive failures",
            "Recommend prompt optimization and context reduction", 
            "Consider reducing agent frequency or complexity",
            "Monitor for infrastructure correlation patterns"
        ])
    elif consecutive >= 3:
        analysis["recovery_recommendations"].extend([
            "WARNING: 3+ consecutive failures",
            "Review recent prompt changes or context additions",
            "Check agent timeout configuration",
            "Monitor for recovery in next few cycles"
        ])
    
    if failure_rate > 75:
        analysis["recovery_recommendations"].append("High failure rate suggests systematic issue - full agent review needed")
    elif failure_rate > 50:
        analysis["recovery_recommendations"].append("Elevated failure rate - investigate recent configuration changes")
    
    # Specific optimization suggestions based on agent type
    agent_optimizations = {
        "DocBot": [
            "Consider reducing PRD update frequency during high activity",
            "Split large documentation updates into smaller chunks",
            "Cache frequently accessed Hub API responses"
        ],
        "Meta": [
            "Optimize scorecard calculation complexity",
            "Reduce agent evaluation scope during peak times",
            "Consider async escalation processing"
        ],
        "Governance": [
            "Streamline constitution checking procedures",
            "Cache roster validation results",
            "Reduce oversight frequency during stable periods"
        ]
    }
    
    if agent_name in agent_optimizations:
        analysis["recovery_recommendations"].extend([
            f"Agent-specific optimizations for {agent_name}:",
            *agent_optimizations[agent_name]
        ])
    
    return analysis

def format_analysis_output(analysis_data):
    """Format analysis data for human-readable output."""
    if "error" in analysis_data:
        return f"Error: {analysis_data['error']}"
    
    output = []
    output.append(f"=== Timeout Analysis: {analysis_data['agent']} ===")
    output.append(f"Generated: {analysis_data['timestamp']}")
    output.append(f"Analysis Window: {analysis_data['window']}")
    output.append()
    
    # Pattern summary
    patterns = analysis_data["pattern_analysis"]
    failure_rate = patterns["failure_rate"]
    consecutive = patterns["consecutive_failures"]
    
    status_icon = "🔴" if consecutive >= 5 else "⚠️" if consecutive >= 3 else "🟡" if failure_rate > 25 else "🟢"
    output.append(f"{status_icon} AGENT STATUS:")
    output.append(f"   Failure Rate: {failure_rate}% ({patterns['failed_runs']}/{patterns['total_runs']} runs)")
    output.append(f"   Consecutive Failures: {consecutive}")
    output.append(f"   Max Consecutive: {patterns['max_consecutive_failures']}")
    output.append()
    
    # Failure streaks
    if patterns["failure_streaks"]:
        output.append("📊 FAILURE STREAK HISTORY:")
        for position, length in patterns["failure_streaks"]:
            output.append(f"   Position -{position}: {length} failures")
        output.append()
    
    # Correlation analysis
    if analysis_data["failure_correlation"]["error_types"]:
        output.append("🔍 ERROR TYPE ANALYSIS:")
        for error_type, count in analysis_data["failure_correlation"]["error_types"].items():
            output.append(f"   {error_type}: {count} occurrences")
        output.append()
    
    # Recommendations
    if analysis_data["recovery_recommendations"]:
        output.append("💡 RECOVERY RECOMMENDATIONS:")
        for i, rec in enumerate(analysis_data["recovery_recommendations"], 1):
            output.append(f"   {i}. {rec}")
    
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description="Analyze agent timeout patterns")
    parser.add_argument("--agent", help="Specific agent name to analyze")
    parser.add_argument("--all", action="store_true", help="Analyze all agents")
    parser.add_argument("--window", default="24h", help="Time window for analysis (e.g., 24h, 7d, 1w)")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    args = parser.parse_args()
    
    if not args.agent and not args.all:
        parser.error("Must specify either --agent <name> or --all")
    
    # Parse time window
    try:
        window = parse_time_window(args.window) if args.window != "all_time" else None
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Load agent data
    status_data = load_agent_status()
    agents = status_data.get("agents", {})
    
    if "error" in status_data:
        print(f"Error loading agent data: {status_data['error']}", file=sys.stderr)
        sys.exit(1)
    
    results = []
    
    if args.all:
        # Analyze all agents
        for agent_name, agent_data in agents.items():
            analysis = analyze_agent_timeouts(agent_name, agent_data, window)
            results.append(analysis)
    else:
        # Analyze specific agent
        if args.agent not in agents:
            print(f"Error: Agent '{args.agent}' not found", file=sys.stderr)
            print(f"Available agents: {', '.join(agents.keys())}", file=sys.stderr)
            sys.exit(1)
        
        analysis = analyze_agent_timeouts(args.agent, agents[args.agent], window)
        results.append(analysis)
    
    # Output results
    if args.json:
        print(json.dumps(results if len(results) > 1 else results[0], indent=2))
    else:
        for analysis in results:
            print(format_analysis_output(analysis))
            if len(results) > 1:
                print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    main()