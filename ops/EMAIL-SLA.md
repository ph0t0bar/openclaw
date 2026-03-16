# Email SLA & Priority System

## Immediate Response (Auto-ACK)
When ANY email arrives from Joey:
1. Hub webhook triggers OpenClaw immediately (not batched)
2. Auto-send acknowledgment: "Got it. Processing..."
3. Classify urgency based on content

## Priority Levels

**🔴 URGENT** — Immediate human (Claw) attention
Triggers: "urgent", "emergency", "down", "broken", "critical", "$", "revenue"
Response: < 5 minutes
Action: Claw drops everything, emails back immediately

**🟡 STANDARD** — DecisionBot processes
Triggers: "approve", "reject", "feedback", "question", "thought"
Response: < 1 hour (DecisionBot cycle)
Action: Processed on next bot run, confirmation email sent

**🟢 ASYNC** — Batched for next scheduled email
Triggers: "idea", "someday", "consider", "when you have time"
Response: Next scheduled touchpoint (morning brief or creative review)
Action: Logged, surfaced at appropriate time

## Auto-Acknowledgment Email Template

Subject: "🦜 Got it — [urgency level] | ETA: [time]"

Body:
- "Your message received at [time]"
- Priority classification
- Expected response time
- "Reply URGENT to escalate"

## WhatsApp Override
If truly critical and email feels too slow: WhatsApp "911" → immediate Claw response
