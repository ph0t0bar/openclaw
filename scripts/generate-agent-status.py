import json, re, os
from datetime import datetime

DATE = datetime.utcnow().strftime("%Y-%m-%d")
LOG = f"memory/{DATE}.md"
OUT = "ops/agent-status.json"

os.chdir("/root/.openclaw/workspace")

agents_def = [
    {"name":"Patrol","dept":"Operations","model":"Kimi","cadence":"5m"},
    {"name":"Sentry","dept":"Operations","model":"Sonnet","cadence":"15m"},
    {"name":"Opus","dept":"Meta","model":"Opus","cadence":"15m"},
    {"name":"Chief of Staff","dept":"Executive","model":"Opus","cadence":"20m"},
    {"name":"Meta","dept":"Meta","model":"Sonnet","cadence":"20m"},
    {"name":"DocBot","dept":"Product","model":"Kimi","cadence":"20m"},
    {"name":"RailwayBot","dept":"Operations","model":"Kimi","cadence":"20m"},
    {"name":"UserHealth","dept":"Customer Success","model":"Kimi","cadence":"20m"},
    {"name":"ContentBot","dept":"Marketing","model":"Sonnet","cadence":"20m"},
    {"name":"Archivist","dept":"Meta","model":"Kimi","cadence":"20m"},
    {"name":"Researcher","dept":"Intelligence","model":"Sonnet","cadence":"10m"},
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

try:
    with open(LOG) as f: log = f.read()
except: log = ""

entries = []
current = None
for line in log.split('\n'):
    if re.match(r'^#{2,3}\s', line):
        if current: entries.append(current)
        current = {"header": line.lstrip('#').strip(), "content": ""}
    elif current:
        current["content"] += line + "\n"
if current: entries.append(current)

total = len(entries)
errs = sum(1 for e in entries if any(w in (e["header"]+e["content"]).lower() for w in ["error","timeout","failed","breach"]))
rate = round((total-errs)/total*100) if total>0 else 0

for a in agents_def:
    nl = a["name"].lower()
    matches = [e for e in entries if nl in e["header"].lower()]
    a["cycles_today"] = len(matches)
    a["last_entry"] = matches[-1]["header"][:30] if matches else None
    e2 = sum(1 for m in matches if any(w in m["content"].lower() for w in ["error","timeout","failed"]))
    a["errors"] = e2
    a["success_rate"] = round((len(matches)-e2)/len(matches)*100) if matches else None
    a["status"] = "error" if matches and e2>len(matches)//2 else "active" if matches else "idle"
    a["last_output"] = matches[-1]["content"].strip()[:150] if matches else None

recent = [{"header":e["header"],"snippet":e["content"].strip()[:120]} for e in reversed(entries[-25:])]

with open(OUT,"w") as f:
    json.dump({"agents":agents_def,"recent":recent,"totalCycles":total,"totalErrors":errs,"successRate":rate,"lastUpdated":datetime.utcnow().isoformat()+"Z"}, f, indent=2)
