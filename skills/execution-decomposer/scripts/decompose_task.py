#!/usr/bin/env python3
"""
Task Decomposition Script for Execution Decomposer
Breaks down complex tasks into atomic, executable subtasks
"""

import sys
import json
import re
import uuid
from typing import Dict, List, Any
from datetime import datetime

def decompose_task(task_description: str, mode: str = "atomic") -> Dict[str, Any]:
    """Break down task into atomic subtasks following Pattern 299"""
    
    task_lower = task_description.lower()
    subtasks = []
    
    # Domain-specific decomposition patterns
    if 'digest' in task_lower and ('pipeline' in task_lower or 'fail' in task_lower):
        subtasks = [
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Check digest service status',
                'description': 'Verify if dropanywhere-cron service is running and accessible',
                'time_estimate': 5,
                'success_criteria': 'Service responds with 200 status or clear error message',
                'dependencies': [],
                'type': 'verification'
            },
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Test single user digest',
                'description': 'Manually trigger digest for one specific user to isolate the failure',
                'time_estimate': 10,
                'success_criteria': 'Single digest generates successfully or specific error identified',
                'dependencies': [],
                'type': 'isolation'
            },
            {
                'id': str(uuid.uuid4())[:8], 
                'title': 'Identify failure point',
                'description': 'Review logs/errors to pinpoint exact failure location in pipeline',
                'time_estimate': 10,
                'success_criteria': 'Specific failure point documented with error details',
                'dependencies': [],
                'type': 'diagnosis'
            },
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Apply targeted fix',
                'description': 'Implement minimal fix for identified failure point',
                'time_estimate': 15,
                'success_criteria': 'Fix applied and single user digest works',
                'dependencies': [],
                'type': 'execution'
            }
        ]
    
    elif 'template' in task_lower and 'deploy' in task_lower:
        subtasks = [
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Validate template structure',
                'description': 'Check HTML structure, required sections, and asset dependencies',
                'time_estimate': 5,
                'success_criteria': 'Template passes validation script without errors',
                'dependencies': [],
                'type': 'validation'
            },
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Deploy to staging',
                'description': 'Upload template to staging environment for testing',
                'time_estimate': 10,
                'success_criteria': 'Template successfully deployed to staging with no errors',
                'dependencies': [],
                'type': 'staging'
            },
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Test staging deployment',
                'description': 'Send test emails using staging template, verify rendering',
                'time_estimate': 10,
                'success_criteria': 'Test emails render correctly across email clients',
                'dependencies': [],
                'type': 'testing'
            },
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Deploy to production',
                'description': 'Deploy validated template to production email service',
                'time_estimate': 10,
                'success_criteria': 'Template live in production with backup created',
                'dependencies': [],
                'type': 'production'
            }
        ]
    
    elif 'family' in task_lower and ('retention' in task_lower or 'engagement' in task_lower):
        subtasks = [
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Query family member status',
                'description': 'Check current engagement scores and activity for all family members',
                'time_estimate': 5,
                'success_criteria': 'Family member statuses retrieved with engagement scores',
                'dependencies': [],
                'type': 'analysis'
            },
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Generate re-engagement content',
                'description': 'Create personalized re-engagement message for at-risk family member',
                'time_estimate': 10,
                'success_criteria': 'Personalized message generated with specific context',
                'dependencies': [],
                'type': 'content'
            },
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Send outreach message',
                'description': 'Deliver re-engagement message via appropriate channel (WhatsApp/SMS/email)',
                'time_estimate': 5,
                'success_criteria': 'Message sent successfully and delivery confirmed',
                'dependencies': [],
                'type': 'communication'
            },
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Schedule follow-up',
                'description': 'Create cron job to check engagement in 3-7 days',
                'time_estimate': 5,
                'success_criteria': 'Follow-up scheduled with specific criteria',
                'dependencies': [],
                'type': 'automation'
            }
        ]
    
    elif 'launch' in task_lower or 'campaign' in task_lower:
        subtasks = [
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'List required launch assets',
                'description': 'Enumerate all assets needed for launch (posts, templates, etc.)',
                'time_estimate': 10,
                'success_criteria': 'Complete list of launch assets with priorities',
                'dependencies': [],
                'type': 'planning'
            },
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Select highest priority asset',
                'description': 'Pick one specific asset to complete based on blocking status',
                'time_estimate': 5,
                'success_criteria': 'Single asset selected with clear completion criteria',
                'dependencies': [],
                'type': 'prioritization'
            },
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Complete selected asset',
                'description': 'Fully complete the selected asset to shippable state',
                'time_estimate': 25,
                'success_criteria': 'Asset completed and ready for launch use',
                'dependencies': [],
                'type': 'execution'
            },
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Queue next asset',
                'description': 'Identify and queue the next highest priority asset',
                'time_estimate': 5,
                'success_criteria': 'Next asset queued with clear assignment',
                'dependencies': [],
                'type': 'continuation'
            }
        ]
    
    elif 'revenue' in task_lower:
        subtasks = [
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'List revenue opportunities',
                'description': 'Enumerate existing revenue opportunities with effort estimates',
                'time_estimate': 10,
                'success_criteria': 'List of opportunities with effort/impact scores',
                'dependencies': [],
                'type': 'discovery'
            },
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Select lowest-effort opportunity',
                'description': 'Pick opportunity with highest ROI and lowest implementation cost',
                'time_estimate': 5,
                'success_criteria': 'Single opportunity selected with rationale',
                'dependencies': [],
                'type': 'selection'
            },
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Define minimal test',
                'description': 'Design minimal viable test for selected opportunity',
                'time_estimate': 10,
                'success_criteria': 'Test plan with success metrics and timeline',
                'dependencies': [],
                'type': 'planning'
            },
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Execute test',
                'description': 'Implement and run the minimal test',
                'time_estimate': 30,
                'success_criteria': 'Test executed with measurable results',
                'dependencies': [],
                'type': 'execution'
            }
        ]
    
    else:
        # Generic decomposition for other tasks
        subtasks = [
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Define success criteria',
                'description': 'Clearly define what completion looks like for this task',
                'time_estimate': 5,
                'success_criteria': 'Specific, measurable success criteria documented',
                'dependencies': [],
                'type': 'definition'
            },
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Identify core deliverable',
                'description': 'Determine the single most important output of this task',
                'time_estimate': 5,
                'success_criteria': 'Core deliverable clearly identified and scoped',
                'dependencies': [],
                'type': 'scoping'
            },
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Execute core task',
                'description': 'Complete the core deliverable',
                'time_estimate': 20,
                'success_criteria': 'Core deliverable completed to success criteria',
                'dependencies': [],
                'type': 'execution'
            },
            {
                'id': str(uuid.uuid4())[:8],
                'title': 'Verify completion',
                'description': 'Validate that task meets success criteria',
                'time_estimate': 5,
                'success_criteria': 'Completion verified against original criteria',
                'dependencies': [],
                'type': 'verification'
            }
        ]
    
    # Calculate totals
    total_time = sum(task['time_estimate'] for task in subtasks)
    parallel_time = max([task['time_estimate'] for task in subtasks]) if subtasks else 0
    
    return {
        'original_task': task_description,
        'decomposition_mode': mode,
        'timestamp': datetime.utcnow().isoformat(),
        'subtasks': subtasks,
        'total_time_estimate': total_time,
        'parallel_time_estimate': parallel_time,
        'subtask_count': len(subtasks),
        'pattern_299_compliance': all(task['time_estimate'] <= 30 for task in subtasks),
        'meta_commentary_prevention': all('analysis' not in task['type'] and 'strategy' not in task['type'] for task in subtasks)
    }

def print_decomposition(decomposition: Dict[str, Any]):
    """Print decomposition in human-readable format"""
    
    print(f"🔨 TASK DECOMPOSITION")
    print(f"====================")
    print(f"Original: {decomposition['original_task']}")
    print(f"Subtasks: {decomposition['subtask_count']}")
    print(f"Total Time: {decomposition['total_time_estimate']} minutes")
    print(f"Parallel Time: {decomposition['parallel_time_estimate']} minutes")
    print(f"Pattern 299 Compliant: {'✅' if decomposition['pattern_299_compliance'] else '❌'}")
    print()
    
    print("📋 ATOMIC SUBTASKS")
    print("==================")
    for i, task in enumerate(decomposition['subtasks'], 1):
        print(f"{i}. {task['title']} ({task['time_estimate']} min)")
        print(f"   {task['description']}")
        print(f"   ✓ Success: {task['success_criteria']}")
        print(f"   🏷️ Type: {task['type']}")
        print(f"   🆔 ID: {task['id']}")
        print()
    
    if decomposition['pattern_299_compliance']:
        print("✅ PATTERN 299 COMPLIANCE")
        print("All subtasks ≤30 minutes - shipping probability high!")
    else:
        print("⚠️ PATTERN 299 WARNING")
        print("Some subtasks >30 minutes - further decomposition recommended")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 decompose_task.py '<task_description>' [--mode atomic|simple] [--json]")
        print("Example: python3 decompose_task.py 'Fix the digest pipeline' --mode atomic")
        sys.exit(1)
    
    task_description = sys.argv[1]
    mode = "atomic"
    
    # Parse arguments
    if '--mode' in sys.argv:
        mode_index = sys.argv.index('--mode') + 1
        if mode_index < len(sys.argv):
            mode = sys.argv[mode_index]
    
    # Decompose task
    decomposition = decompose_task(task_description, mode)
    
    # Output results
    if '--json' in sys.argv:
        print(json.dumps(decomposition, indent=2))
    else:
        print_decomposition(decomposition)
        
        if '--json' in sys.argv:
            print("\nJSON OUTPUT:")
            print(json.dumps(decomposition, indent=2))

if __name__ == "__main__":
    main()