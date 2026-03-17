# CEO Email Operating System

**Principle:** If it's not in Joey's inbox, it doesn't exist.

---

## Email Streams (All from hello@drop-anywhere.com)

### 1. 🌅 Morning Brief (daily, 8am CST)
**Subject:** "☀️ Morning Brief — [Date]"
- Systems health (green/red)
- Overnight work (PRs, agent output, tasks completed)
- Decisions needed (with reply prompts)
- Pipeline metrics (users, drops, MRR)
- Today's launch countdown
**Reply:** Any text → routes to ops decisions

### 2. 🦜 Creative Review (every 4h, only when new content)
**Subject:** "🦜 Creative Review — [count] items"
- New social posts, specs, content
- Each item: full text + ✅/🔄/❌ prompt
**Reply:** Feedback per item → routes to content agents

### 3. ⚙️ Task Approvals (as needed, batched hourly)
**Subject:** "⚙️ [count] tasks need your call"
- Customer-facing tasks from Dropper-Code
- Each: title, description, risk level
- Reply: "approve 1, reject 2, hold 3"
**Reply:** Decisions → auto-approve/reject via Hub API

### 4. 🚨 Alerts (immediate, critical only)
**Subject:** "🚨 [SYSTEM] — [issue]"
- Poe balance critical
- Service down
- Payment failures
- Family user at risk
**Reply:** Instructions → Drop acts on them

### 5. 📊 Weekly Report (Sunday evening)
**Subject:** "📊 Week in Review — [date range]"
- Full metrics with week-over-week
- What shipped
- What's blocked
- Strategic recommendations
- Next week priorities
**Reply:** Direction setting → updates PRD

### 6. 💬 Drop Conversation (replaces WhatsApp)
**Subject:** "💬 Drop — [topic]" or RE: ongoing thread
- Anything I'd normally say on WhatsApp
- Context-rich, searchable, persistent
- Threaded conversation via email replies
**Reply:** Joey replies → I respond via next email

---

## Inbound Routing

ALL replies to hello@drop-anywhere.com hit:
1. Resend webhook → Hub /api/webhook/email
2. Hub stores as drop (source: email, user: Joey)
3. FeedbackBot + DecisionBot read drops, route actions:
   - "approve" / "reject" → Hub task API
   - Creative feedback → agent board + review files
   - Questions/conversation → triggers Drop response email
   - Strategic direction → PRD updates

## What Dies
- WhatsApp as primary channel (keep for true emergencies only)
- Dashboard as review surface
- Any agent output that doesn't reach email

## What Lives
- Email is the ONLY interface
- Every email is actionable (reply = decision)
- Every reply generates a drop (searchable forever)
- Conversation history lives in your inbox AND your vault

