---
name: execution-decomposer
description: Break down complex monolithic tasks into atomic, executable subtasks to prevent Meta-Commentary Disease (Pattern 300). Use when tasks stall in debate for 2+ hours, when complex tasks generate more analysis than action, or when Pattern 299 decomposition is needed. Triggers on "decompose this task", "break this down", "task is stalling", or when monolithic task assignment fails.
---

# Execution Decomposer

Transforms complex monolithic tasks into atomic, executable subtasks based on Pattern 299: "Decomposition Enables Execution."

## Core Insight - Pattern 299

**PROVEN:**
- ✅ **poe-balance-guardian** (atomic scope) → shipped in 30 minutes
- ✅ **family-retention-guardian** (atomic scope) → shipped and working  
- ✅ **template-deployer** (atomic scope) → scripts created
- ❌ **digest-pipeline** (monolithic) → 7+ hours of debate, 0 fixes
- ❌ **revenue tasks** (monolithic) → infinite board analysis
- ❌ **template crisis** (monolithic) → 40+ votes, 0 deploys

**Rule:** Complex tasks need DECOMPOSITION_MODE before assignment, not during execution.

## When to Use

**AUTOMATIC TRIGGERS:**
- Task has been in discussion >2 hours with no concrete action
- Multiple agents voting/analyzing same issue without progress
- Task scope includes multiple systems/domains
- Previous attempts failed due to complexity

**MANUAL TRIGGERS:**
- "Decompose this task"
- "Break this down into atomic steps" 
- "Task is stalling"
- "Apply Pattern 299"
- "Meta-Commentary Disease detected"

## Decomposition Principles

### 1. Atomic Task Criteria
Each subtask must be:
- **Independent:** Can be completed without other subtasks
- **Testable:** Clear success/failure criteria
- **Time-bounded:** <30 minutes to complete
- **Single-responsibility:** Does one thing well
- **Dependency-free:** Minimal external coordination needed

### 2. Meta-Commentary Disease Prevention
Identify and eliminate:
- Analysis paralysis loops
- "Strategic discussion" without concrete next steps  
- Board voting on voting procedures
- Perfect solution optimization
- Cross-agent debate cycles

## Core Operations

### 1. Task Analysis
```bash
python scripts/analyze_task.py <task_description>
```
- Identifies complexity vectors
- Maps system dependencies  
- Detects Meta-Commentary Disease symptoms
- Generates decomposition candidates

### 2. Atomic Breakdown
```bash
python scripts/decompose_task.py <task_description> --mode atomic
```
- Creates atomic subtask list
- Assigns clear success criteria
- Estimates time bounds
- Identifies minimal viable progress

### 3. Dependency Mapping
```bash
python scripts/map_dependencies.py <task_list>
```
- Maps inter-task dependencies
- Identifies parallel execution opportunities
- Creates execution order recommendations
- Flags potential bottlenecks

### 4. Progress Tracking
```bash
python scripts/track_progress.py --task-id <id>
```
- Monitors atomic task completion
- Detects re-emergence of Meta-Commentary Disease
- Triggers escalation on stalls
- Reports completion rates

## Decomposition Patterns

### Pattern A: Technical Implementation
**Before:** "Fix the digest pipeline"
**After:** 
1. Identify error logs (5 min)
2. Test one user digest manually (10 min)  
3. Check service status (5 min)
4. Fix configuration if needed (15 min)

### Pattern B: Strategic Planning
**Before:** "Increase revenue"
**After:**
1. List existing revenue opportunities (10 min)
2. Pick one specific opportunity (5 min)
3. Define minimal viable test (15 min)
4. Execute test (30 min)

### Pattern C: Template/Asset Deployment  
**Before:** "Deploy template to production"
**After:**
1. Validate template locally (10 min)
2. Deploy to staging (10 min)
3. Test staging deployment (10 min)
4. Deploy to production (10 min)

## Success Metrics

- **Atomic tasks complete:** 90%+ success rate
- **Monolithic tasks stall:** <2 hour resolution
- **Meta-Commentary cycles:** Early detection and interruption
- **Board paralysis:** Automatic decomposition triggers

## Emergency Anti-Pattern Detection

**Red Flags for Immediate Decomposition:**
- 3+ agents analyzing same issue
- >30 "strategic notes" with no action
- Board voting on analysis methodology
- "Let's discuss the approach to discussing..." 
- Pattern 300 symptoms emerging

## Integration Points

- **Cron jobs:** Automatic stall detection
- **Agent board:** Decomposition recommendations
- **WhatsApp alerts:** Meta-Commentary Disease warnings
- **Git tracking:** Atomic task completion logs

## Usage Examples

**Crisis Response:**
```bash
# Detect stalled task
python scripts/analyze_task.py "Fix digest pipeline failure" 

# Generate atomic breakdown  
python scripts/decompose_task.py "Fix digest pipeline failure" --mode atomic

# Track execution
python scripts/track_progress.py --task-id digest-fix-001
```

**Preventive Mode:**
```bash
# Before assigning complex task
python scripts/analyze_task.py "Launch week coordination"
# Returns: COMPLEX - decomposition recommended

python scripts/decompose_task.py "Launch week coordination" --mode atomic
# Returns: 8 atomic tasks, 3 parallel streams
```

## Pattern 299 Enforcement

This skill embodies its own principle:
- **Single responsibility:** Task decomposition only
- **Atomic scope:** Each operation completes in minutes
- **Clear success criteria:** Measurable task breakdown
- **Dependency-free:** Works independent of other systems
- **Anti-paralysis:** Forces action over analysis