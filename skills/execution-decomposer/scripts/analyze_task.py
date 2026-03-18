#!/usr/bin/env python3
"""
Task Analysis Script for Execution Decomposer
Identifies complexity vectors and Meta-Commentary Disease symptoms
"""

import sys
import json
import re
from typing import Dict, List, Any

def analyze_task_complexity(task_description: str) -> Dict[str, Any]:
    """Analyze task for complexity indicators and decomposition needs"""
    
    # Complexity indicators
    complexity_signals = {
        'system_count': len(re.findall(r'\b(pipeline|service|system|infrastructure|deployment|integration)\b', task_description.lower())),
        'verb_count': len(re.findall(r'\b(fix|deploy|implement|integrate|coordinate|manage|optimize|analyze)\b', task_description.lower())),
        'stakeholder_count': len(re.findall(r'\b(team|user|customer|family|agent|service)\b', task_description.lower())),
        'temporal_scope': any(word in task_description.lower() for word in ['launch', 'campaign', 'rollout', 'migration', 'upgrade']),
        'cross_domain': any(word in task_description.lower() for word in ['and', '&', 'plus', 'also', 'including'])
    }
    
    # Meta-Commentary Disease indicators
    meta_commentary_signals = {
        'analysis_words': len(re.findall(r'\b(analyze|discuss|consider|evaluate|assess|review|examine)\b', task_description.lower())),
        'strategy_words': len(re.findall(r'\b(strategy|approach|methodology|framework|process)\b', task_description.lower())),
        'vague_scope': any(word in task_description.lower() for word in ['improve', 'enhance', 'optimize', 'better']),
        'coordination_heavy': any(word in task_description.lower() for word in ['coordinate', 'align', 'sync', 'orchestrate'])
    }
    
    # Calculate complexity score
    complexity_score = (
        complexity_signals['system_count'] * 2 +
        complexity_signals['verb_count'] * 1.5 +
        complexity_signals['stakeholder_count'] * 1 +
        (2 if complexity_signals['temporal_scope'] else 0) +
        (2 if complexity_signals['cross_domain'] else 0)
    )
    
    # Calculate Meta-Commentary Disease risk
    meta_commentary_risk = (
        meta_commentary_signals['analysis_words'] * 2 +
        meta_commentary_signals['strategy_words'] * 1.5 +
        (3 if meta_commentary_signals['vague_scope'] else 0) +
        (2 if meta_commentary_signals['coordination_heavy'] else 0)
    )
    
    # Determine recommendation
    if complexity_score <= 3 and meta_commentary_risk <= 2:
        recommendation = "ATOMIC"
        reason = "Low complexity, suitable for direct execution"
    elif complexity_score <= 6 and meta_commentary_risk <= 4:
        recommendation = "SIMPLE_DECOMPOSITION"
        reason = "Moderate complexity, break into 2-3 subtasks"
    else:
        recommendation = "COMPLEX_DECOMPOSITION"
        reason = "High complexity or Meta-Commentary Disease risk detected"
    
    # Generate specific warnings
    warnings = []
    if meta_commentary_risk > 4:
        warnings.append("🚨 HIGH META-COMMENTARY DISEASE RISK - Contains analysis/strategy focus without concrete actions")
    if complexity_signals['system_count'] > 2:
        warnings.append("⚠️ MULTI-SYSTEM TASK - Involves multiple systems/services")
    if complexity_signals['cross_domain']:
        warnings.append("⚠️ CROSS-DOMAIN TASK - Spans multiple domains/responsibilities")
    if meta_commentary_signals['vague_scope']:
        warnings.append("⚠️ VAGUE SCOPE - Contains improvement words without specific targets")
    
    return {
        'task': task_description,
        'complexity_score': complexity_score,
        'meta_commentary_risk': meta_commentary_risk,
        'recommendation': recommendation,
        'reason': reason,
        'warnings': warnings,
        'complexity_signals': complexity_signals,
        'meta_commentary_signals': meta_commentary_signals,
        'suggested_subtask_count': min(max(2, int(complexity_score / 2)), 8)
    }

def generate_decomposition_hints(analysis: Dict[str, Any]) -> List[str]:
    """Generate specific hints for task decomposition"""
    
    hints = []
    task = analysis['task'].lower()
    
    # System-specific hints
    if 'digest' in task and 'pipeline' in task:
        hints.extend([
            "1. Check digest service status/logs (5 min)",
            "2. Test single user digest manually (10 min)", 
            "3. Identify specific failure point (10 min)",
            "4. Apply targeted fix (15 min)"
        ])
    elif 'template' in task and 'deploy' in task:
        hints.extend([
            "1. Validate template locally (5 min)",
            "2. Deploy to staging environment (10 min)",
            "3. Test staging deployment (10 min)", 
            "4. Deploy to production (10 min)"
        ])
    elif 'family' in task and 'retention' in task:
        hints.extend([
            "1. Query family member status (5 min)",
            "2. Generate re-engagement message (10 min)",
            "3. Send via WhatsApp/SMS (5 min)",
            "4. Schedule follow-up check (5 min)"
        ])
    elif 'launch' in task or 'campaign' in task:
        hints.extend([
            "1. List required launch assets (10 min)",
            "2. Pick one specific asset to complete (5 min)",
            "3. Complete that single asset (25 min)",
            "4. Queue next asset (5 min)"
        ])
    elif 'revenue' in task:
        hints.extend([
            "1. List existing revenue opportunities (10 min)",
            "2. Pick lowest-effort opportunity (5 min)",
            "3. Define minimal test for that opportunity (10 min)",
            "4. Execute the test (30 min)"
        ])
    else:
        # Generic decomposition hints based on complexity
        if analysis['complexity_score'] > 6:
            hints.extend([
                "1. Identify core deliverable (10 min)",
                "2. List minimum requirements (10 min)",
                "3. Create/test minimal version (30 min)",
                "4. Validate with stakeholder (15 min)"
            ])
        else:
            hints.extend([
                "1. Define specific success criteria (5 min)",
                "2. Execute core task (20 min)",
                "3. Verify completion (5 min)"
            ])
    
    return hints

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 analyze_task.py '<task_description>'")
        print("Example: python3 analyze_task.py 'Fix the digest pipeline'")
        sys.exit(1)
    
    task_description = sys.argv[1]
    
    # Analyze task
    analysis = analyze_task_complexity(task_description)
    
    # Generate decomposition hints
    hints = generate_decomposition_hints(analysis)
    
    # Output results
    print(f"📊 TASK ANALYSIS")
    print(f"================")
    print(f"Task: {analysis['task']}")
    print(f"Complexity Score: {analysis['complexity_score']}/10")
    print(f"Meta-Commentary Risk: {analysis['meta_commentary_risk']}/10")
    print(f"Recommendation: {analysis['recommendation']}")
    print(f"Reason: {analysis['reason']}")
    print()
    
    # Print warnings
    if analysis['warnings']:
        print("⚠️  WARNINGS")
        for warning in analysis['warnings']:
            print(f"   {warning}")
        print()
    
    # Print decomposition hints
    if analysis['recommendation'] != "ATOMIC":
        print("🔨 SUGGESTED DECOMPOSITION")
        print("===========================")
        for hint in hints:
            print(f"   {hint}")
        print()
        print(f"💡 Suggested subtask count: {analysis['suggested_subtask_count']}")
        print()
    
    # Pattern 299 reminder
    if analysis['recommendation'] == "COMPLEX_DECOMPOSITION":
        print("🚨 PATTERN 299 ALERT")
        print("===================")
        print("Complex task detected. History shows:")
        print("✅ Atomic tasks ship in minutes")
        print("❌ Monolithic tasks generate hours of debate")
        print("🎯 BREAK THIS DOWN before assignment!")
        print()
    
    # JSON output for automation
    if '--json' in sys.argv:
        print("JSON OUTPUT:")
        print(json.dumps(analysis, indent=2))

if __name__ == "__main__":
    main()