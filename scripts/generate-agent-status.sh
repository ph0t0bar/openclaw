#!/bin/bash
# Generate real-time agent status JSON from daily log + git history
# Run by Archivist every cycle, pushed to GitHub for dashboard consumption

cd /root/.openclaw/workspace
DATE=$(date -u +%Y-%m-%d)
LOG="memory/${DATE}.md"
OUT="ops/agent-status.json"

# Count entries per agent from daily log
count_agent() {
  local name="$1"
  grep -ci "$name" "$LOG" 2>/dev/null || echo 0
}

# Get last commit time per agent keyword
last_active() {
  local name="$1"
  git log --oneline --format="%ai" --grep="$name" -1 2>/dev/null | head -1 | cut -d' ' -f1,2
}

# Count total entries and errors
TOTAL=$(grep -c "^###" "$LOG" 2>/dev/null || echo 0)
ERRORS=$(grep -ci "error\|timeout\|failed\|timed out" "$LOG" 2>/dev/null || echo 0)
SUCCESS=$((TOTAL - ERRORS))
RATE=$(python3 -c "print(round($SUCCESS/$TOTAL*100) if $TOTAL>0 else 0)")

python3 << PYEOF
import json
from datetime import datetime

agents = [
    {"name":"Kimi Patrol","dept":"Operations","model":"Kimi","cadence":"5m"},
    {"name":"Sentry","dept":"Operations","model":"Sonnet","cadence":"15m"},
    {"name":"Opus Strategy","dept":"Meta","model":"Opus","cadence":"15m"},
    {"name":"Chief of Staff","dept":"Executive","model":"Opus","cadence":"20m"},
    {"name":"Meta","dept":"Meta","model":"Sonnet","cadence":"20m"},
    {"name":"DocBot","dept":"Product","model":"Kimi","cadence":"20m"},
    {"name":"RailwayBot","dept":"Operations","model":"Kimi","cadence":"20m"},
    {"name":"UserHealthBot","dept":"Customer Success","model":"Kimi","cadence":"20m"},
    {"name":"ContentBot","dept":"Marketing","model":"Sonnet","cadence":"20m"},
    {"name":"Archivist","dept":"Meta","model":"Kimi","cadence":"20m"},
    {"name":"Deep Researcher","dept":"Intelligence","model":"Sonnet","cadence":"10m"},
    {"name":"Wire","dept":"Intelligence","model":"Kimi","cadence":"15m"},
    {"name":"DC Manager","dept":"Engineering","model":"Kimi","cadence":"30m"},
    {"name":"FrontEndBot","dept":"Engineering","model":"Kimi","cadence":"30m"},
    {"name":"BHABot","dept":"Engineering","model":"Kimi","cadence":"30m"},
    {"name":"SpecBot","dept":"Product","model":"Kimi","cadence":"30m"},
    {"name":"StripeBot","dept":"Revenue","model":"Kimi","cadence":"30m"},
    {"name":"PoeBot","dept":"Revenue","model":"Kimi","cadence":"30m"},
    {"name":"OnboardBot","dept":"Customer Success","model":"Kimi","cadence":"30m"},
    {"name":"SocialBot","dept":"Marketing","model":"Kimi","cadence":"30m"},
    {"name":"SEOBot","dept":"Marketing","model":"Kimi","cadence":"30m"},
    {"name":"FounderVoice","dept":"Communications","model":"Sonnet","cadence":"30m"},
    {"name":"ContentPitch","dept":"Intelligence","model":"Kimi","cadence":"30m"},
    {"name":"PatternBot","dept":"Intelligence","model":"Kimi","cadence":"30m"},
    {"name":"LearningBot","dept":"Meta","model":"Kimi","cadence":"30m"},
    {"name":"Governance","dept":"Meta","model":"Sonnet","cadence":"30m"},
]

# Read daily log
try:
    with open("memory/${DATE}.md") as f:
        log = f.read()
except:
    log = ""

# Parse log entries
lines = log.split('\n')
entries = []
current = None
for line in lines:
    if line.startswith('### '):
        if current:
            entries.append(current)
        current = {"header": line, "content": ""}
    elif current:
        current["content"] += line + "\n"
if current:
    entries.append(current)

# Match agents to entries
for agent in agents:
    name_lower = agent["name"].lower()
    matches = [e for e in entries if name_lower in e["header"].lower() or name_lower.replace("bot","") in e["header"].lower()]
    agent["cycles_today"] = len(matches)
    agent["last_entry"] = matches[-1]["header"][4:20].strip() if matches else None
    
    # Check for errors in their entries
    error_count = sum(1 for m in matches if any(w in m["content"].lower() for w in ["error","timeout","failed","timed out"]))
    success_count = len(matches) - error_count
    agent["errors"] = error_count
    agent["success_rate"] = round(success_count/len(matches)*100) if matches else None
    
    # Determine status
    if not matches:
        agent["status"] = "idle"
    elif error_count > success_count:
        agent["status"] = "error"
    elif agent["cycles_today"] > 0:
        agent["status"] = "active"
    else:
        agent["status"] = "idle"
    
    # Get last content snippet
    if matches:
        content = matches[-1]["content"].strip()[:120]
        agent["last_output"] = content
    else:
        agent["last_output"] = None

# Recent activity (last 20 entries, newest first)
recent = []
for e in reversed(entries[-20:]):
    h = e["header"].replace("### ","")
    snippet = e["content"].strip()[:100]
    recent.append({"header": h, "snippet": snippet})

result = {
    "agents": agents,
    "recent": recent,
    "totalCycles": ${TOTAL},
    "totalErrors": ${ERRORS},
    "successRate": ${RATE},
    "lastUpdated": datetime.utcnow().isoformat()+"Z",
    "dailyLogLines": len(lines),
}

with open("${OUT}", "w") as f:
    json.dump(result, f, indent=2)

print(f"Generated: {len(agents)} agents, {${TOTAL}} cycles, {${RATE}}% success")
PYEOF