# Dropper-Code Pre-Launch Audit Report

**Date:** 2026-03-16  
**Auditor:** Claw (subagent)  
**Repo:** ph0t0bar/dropper-code (commit b38bebf)  
**Launch Target:** March 24, 2026  

---

## Executive Summary

| Metric | Count |
|--------|-------|
| **Total Findings** | 18 |
| 🔴 Fix Before Launch | 5 |
| 🟡 Should Fix | 8 |
| 🟢 OK | 5 |

### Critical Action Items (🔴)
1. `system_pulse` reports "Auto-merge: active" — stale copy from before auto-merge removal
2. `merge_pr()` function still exists in `git_ops.py` — dead code that could be called
3. No retry/backoff on Claude API failures (Mar 16 outage proves this)
4. `--dangerously-skip-permissions` in Claude CLI — no sandboxing of Claude's file access
5. `claude_runner.py` has `max_budget` param but never passes it to CLI — no cost control

---

## A) Cron Jobs

| Job | Frequency | What It Does | Active? |
|-----|-----------|-------------|---------|
| `brain_scan` | Every 4h | Gathers context (ops messages, task queue, TODO.md, rejection list), asks Claude to propose top 3 tasks | ❌ Disabled by DISABLE_CRONS |
| `code_health_scan` | Every 6h | Runs Claude on each repo to find bugs/security issues, proposes HIGH-severity fix tasks | ❌ Disabled |
| `todo_scanner` | Daily 6am CST | Reads TODO.md, asks Claude to identify top 3 priorities | ❌ Disabled |
| `user_data_analysis` | Daily 9am CST | Reads Hub main.py, proposes feature ideas | ❌ Disabled |
| `ops_summary` | Daily 7pm CST | Summarizes task queue stats | ❌ Disabled |
| `system_pulse` | Every 2h | Posts health breadcrumb to agent-drops | ❌ Disabled |

**When DISABLE_CRONS=1:** All scheduled crons are disabled. ✅ The `setup_cron()` function properly returns early. Manual triggers via `POST /trigger/{job_name}` still work (by design — this is correct).

🟢 **DISABLE_CRONS works correctly** — no crons leak through.

---

## B) Task Execution

**Polling:** Every 45s, `poll_loop()` calls `hub_client.get_approved_tasks()` → filters by `assignee=dropper-code, status=approved`.

**Flow:**
1. Poll finds approved task(s)
2. Group by `target_repo` → batch same-repo tasks
3. For each task: pull latest → create branch → build Claude prompt → run Claude Code CLI → validate diff → build check → commit → push → create PR
4. Mark task done/failed via Hub API + post ops message

**Dedup:** ✅ `create_task()` checks existing active tasks and rejected tasks using `_titles_match()` with 60% word overlap detection. This was added (commit 1ce4792) after the Mar 14-15 dupe incident.

**Race conditions:**
- 🟡 **Single-worker assumption:** No lock/mutex on task polling. If two instances ran, both could grab the same task. Currently single Railway instance, but no guard exists.
- ✅ Batch mode groups same-repo tasks into one branch/PR to prevent Railway deploy races (commit b97c945).

**Zombie recovery:** ✅ On startup, `recover_zombie_tasks()` resets any `in_progress` tasks back to `approved`.

🟡 **No concurrency guard** — works now with single instance but fragile.

---

## C) Brain-Scan

**Sources scanned:**
1. Recent ops messages (last 10)
2. Task queue state (pending/done/failed counts)
3. `dropanywhere-app/TODO.md` uncompleted items
4. Rejected/cancelled tasks (rejection memory)

**Priority logic:** Delegated entirely to Claude via prompt. Prompt says: bug fixes > backend > internal tooling. No UI/landing/copy/design tasks. Must not re-propose rejected tasks.

**Dupe prevention:** Brain-scan prefixes tasks with `[brain-scan]`. `_titles_match()` strips this prefix for comparison. Also checks rejection memory.

**Mar 14-15 incident (11 dupes + 9 junk PRs):** The dedup + rejection memory were added AFTER this incident (commits 1ce4792, 254bbd0). Current code should prevent recurrence.

🟡 **Brain-scan quality depends entirely on Claude's judgment.** No hard limit on tasks created per scan (just "TOP 3" in prompt — Claude could output more). No rate limit on task creation.

🟡 **`user_data_analysis` cron is essentially a feature-idea generator** — vague proposals with no dedup against brain-scan output. Could create noise when crons are re-enabled.

---

## D) Auto-Merge

**Status:** ✅ **Removed from `execute_task()` and `execute_task_batch()`** in commit b38bebf.

Both paths now end at "PR ready for review" — no merge call after PR creation.

🔴 **HOWEVER:** `git_ops.merge_pr()` function STILL EXISTS in git_ops.py (lines ~180-210). It's not called from worker.py, but it's importable and could be called by Claude Code during execution (since `--dangerously-skip-permissions` is set). Should be deleted or clearly deprecated.

🔴 **`system_pulse` cron still reports "Auto-merge: active"** (cron_jobs.py line 304). This is stale copy — confusing for ops monitoring.

---

## E) Build Validation

✅ **Added in commit b38bebf.** Runs AFTER staging, BEFORE committing.

| Repo Type | Check |
|-----------|-------|
| `dropanywhere-app`, `brutallyhonest-next` | `npm run build` |
| `opoerator-hub` (Python) | `python3 -m py_compile` on each changed .py file |
| `openclaw` | Falls through to Python check (wrong — it's TypeScript) |

🟡 **openclaw is TypeScript but not in BUILD_COMMANDS dict** — it would get Python syntax checks instead of `npm run build`. Should add `"openclaw": ["npm", "run", "build"]` to `BUILD_COMMANDS`.

🟢 Build failures properly block the PR (reset hard + fail task).

---

## F) Webhook/Hook Integration

**Full chain:**

```
brain-scan (every 4h, on dropper-code)
  → Claude analyzes context
  → hub_client.create_task() → POST /api/ops/tasks on Hub
  → Task sits as "pending"

OpenClaw heartbeat (on openclaw-gateway)
  → Reads HEARTBEAT_STAGED.md rules
  → Auto-approves safe tasks (PATCH /api/ops/tasks/{id} status=approved)
  → Escalates customer-facing to Joey

dropper-code poll_loop (every 45s)
  → GET /api/ops/tasks?assignee=dropper-code&status=approved
  → Executes task → pushes branch → creates PR via GitHub API
  → PATCH /api/ops/tasks/{id} status=done, result=PR URL
  → POST /api/ops/messages (ops board notification)

Human review
  → Joey reviews PR on GitHub → merges → Railway auto-deploys
```

**Communication paths:**
- Dropper-code → Hub: HTTP API (INGEST_API_KEY auth)
- Hub → OpenClaw: webhook at `/hooks/agent` (OPENCLAW_HOOK_TOKEN auth)
- Dropper-code → OpenClaw: indirect, via Hub ops messages
- Dropper-code → GitHub: GITHUB_TOKEN for push + PR creation

🟢 **Chain is well-mapped and logical.** No direct dropper-code ↔ OpenClaw communication (all mediated by Hub).

The `/message` endpoint (commit 9ca1066) adds a relay path for external agents to post to Hub ops board. Simple pass-through, no auth beyond network access.

🟡 **`/message` endpoint has no authentication** — anyone who can reach the Railway URL can post ops messages. Should add API key check.

---

## G) Environment Variables

| Var | Purpose | Status |
|-----|---------|--------|
| `HUB_URL` | Hub API base URL | 🟢 Defaults to production |
| `INGEST_API_KEY` | Hub API auth | 🟢 Required |
| `GITHUB_TOKEN` | Git push + PR creation | 🟢 Required |
| `DATABASE_URL` | PostgreSQL for run history | 🟢 Optional (graceful degradation) |
| `POLL_INTERVAL` | Task poll frequency (default 45s) | 🟢 |
| `DISABLE_CRONS` | Kill scheduled crons | 🟢 Currently set |
| `CLAUDE_MAX_BUDGET` | Max budget per Claude run (default $2.00) | 🔴 Not actually passed to CLI (see below) |
| `CLAUDE_MODEL` | Model for Claude Code (default "sonnet") | 🟢 |
| `REPOS_DIR` | Where repos are cloned (default /data/repos) | 🟢 |
| `PORT` | Health server port (default 8080) | 🟢 |

🔴 **`CLAUDE_MAX_BUDGET` is read but NEVER USED.** `claude_runner.py` accepts `max_budget` param but the CLI command never includes `--max-turns` cost limit or `--budget` flag. Brain-scan passes `max_budget=0.15` but it's silently ignored. **There is NO cost control on Claude executions.** A runaway task could burn unlimited API credits.

🟡 **No `OPENCLAW_HOOK_TOKEN`** — dropper-code doesn't notify OpenClaw directly (goes through Hub), so this is fine but worth noting.

---

## H) Target Repos

**Configured in REPO_MAP (git_ops.py):**
- ✅ `opoerator-hub` (aliased: `hub`)
- ✅ `dropanywhere-app` (aliased: `app`, `frontend`)
- ✅ `openclaw` (owner: `openclaw` org, not `ph0t0bar`)
- ✅ `brutallyhonest-next` (aliased: `bha`)

**Cloned at startup (docker-entrypoint.sh):**
All four repos are cloned. openclaw uses `openclaw/openclaw` owner.

**Code health scan skips openclaw** (comment: "ph0t0bar can't push to openclaw org repo"). But `REPO_MAP` still includes it and tasks could target it.

🟡 **openclaw targeting is inconsistent** — entrypoint clones it, REPO_MAP includes it, but code_health_scan skips it. The git credential uses `GITHUB_TOKEN` which may not have push access to `openclaw/openclaw` org repo. Tasks targeting openclaw could fail silently at push. **Clarify: should dropper-code target openclaw or not?** The commit cc7a755 says "skip openclaw tasks" but the skip is only in code_health_scan, not in task execution.

---

## I) Error Handling

**On task failure:**
- ✅ Resets git state (checkout ., clean -fd, checkout main)
- ✅ Updates task status to "failed" with error message (truncated to 2000 chars)
- ✅ Posts high-priority ops message
- ✅ Records in database

**What's missing:**

🔴 **No retry logic.** When Claude hits usage limits (Mar 16: "out of extra usage, resets 4pm UTC"), the task fails permanently. No exponential backoff, no retry queue, no "retry after X hours." The task must be manually re-approved.

🟡 **No alerting to Joey.** Failed tasks post to ops board but don't trigger a WhatsApp notification. Joey only sees failures if OpenClaw's heartbeat checks the ops board.

🟡 **No circuit breaker.** If Claude API is down, dropper-code will keep polling every 45s and failing every task. Should detect repeated failures and pause polling.

---

## J) Safety

### Guardrails Present:
- ✅ **Deletion guardrails:** Blocks diffs with >300 net deleted lines or >3:1 deletion ratio (commit 0594b48)
- ✅ **Secret detection:** 10 regex patterns for API keys, tokens, passwords in diffs
- ✅ **Forbidden files:** .env, .env.local, .env.production, credentials.json, service-account.json
- ✅ **AI artifact detection:** Catches `<think>` tags, chatbot preambles, stray code fences
- ✅ **Build validation:** npm build / py_compile before committing
- ✅ **Lock file warnings:** Flags package-lock.json etc. changes
- ✅ **Non-root execution:** Worker runs as `worker` user via gosu (Dockerfile + entrypoint)
- ✅ **Customer-facing detection:** Regex patterns flag UI/design/copy tasks with `[CUSTOMER-FACING]` tag

### Gaps:

🔴 **`--dangerously-skip-permissions` on Claude Code CLI.** Claude has unrestricted file system access within the repo directory. It could:
- Read `.env` files (even though it can't commit them)
- Modify `docker-entrypoint.sh` to change entrypoint behavior
- Add malicious code that passes build checks
- Read other repos' code/secrets from `/data/repos/`

This is the biggest safety concern. Claude Code is essentially running with full access to the container's filesystem.

🟡 **No database migration guardrail.** Safety checks look at diff content but don't flag SQL migrations, Prisma schema changes, or Alembic migrations. A task could propose schema changes that pass all current checks.

🟡 **No payment/auth guardrail.** Nothing prevents Claude from modifying Stripe integration code, auth logic, or permission checks. The prompt says "keep changes minimal" but there's no diff-level detection for payment/auth files.

🟡 **CLAUDE.md gives Claude detailed knowledge of main.py line numbers** (email webhook near line 5356, artifact generation near line 20785, etc.). This is useful for task execution but also means Claude knows exactly where sensitive code lives.

---

## K) TODO/FIXME/HACK/XXX

No actual TODO/FIXME/HACK/XXX code comments found. All "TODO" references are about the `todo_scanner` cron job and `TODO.md` file processing. 

🟢 **Codebase is clean of debt markers.**

---

## L) Dead Code

| Item | Location | Status |
|------|----------|--------|
| `merge_pr()` | git_ops.py:180-210 | 🔴 **Dead — auto-merge removed but function remains. Can be called by Claude via `--dangerously-skip-permissions`.** |
| `validate_force_push()` | safety.py:118-122 | 🟡 Dead — defined but never called anywhere. Should either be wired into git_ops or removed. |
| `HEARTBEAT_STAGED.md` | root | 🟡 Staging doc for OpenClaw's heartbeat, not used by dropper-code itself. Could be moved to docs/. |
| `max_budget` parameter | claude_runner.py | 🔴 Accepted but never used — creates false sense of cost control. |
| `allowed_tools` parameter | claude_runner.py:22 | 🟡 Accepted but never used. |
| `"Auto-merge: active"` string | cron_jobs.py:304 | 🔴 Stale — auto-merge was removed. |

---

## Additional Findings

### 🟡 No rate limiting on `/trigger/{job_name}`
Anyone with network access can spam-trigger cron jobs. Each brain_scan creates up to 3 tasks and costs Claude API credits. Should add auth or rate limiting.

### 🟡 Git credential in global config
`docker-entrypoint.sh` puts GITHUB_TOKEN in `.gitconfig` via `insteadOf` — this means ANY git operation in the container can push to ph0t0bar's repos. Combined with `--dangerously-skip-permissions`, Claude could theoretically `git push` to repos outside the task's target.

### 🟢 Observability is good
PostgreSQL tracking of all task runs and cron runs with timing, outputs, diffs, and safety results. Health endpoint exposes runtime state. Ops messages create audit trail.

### 🟢 Batch mode is well-implemented
Same-repo tasks are grouped into single branch/PR to prevent Railway deploy races. Individual task failures don't block the batch.

---

## Recommendations Priority Order

### Before Launch (🔴):
1. **Delete `merge_pr()` from git_ops.py** or add `raise NotImplementedError("auto-merge disabled")`
2. **Fix "Auto-merge: active" in system_pulse** → "Auto-merge: disabled (human review required)"
3. **Implement cost control** — either pass `--max-turns` to Claude CLI or add a timeout kill
4. **Add basic retry with backoff** — at minimum, re-queue failed tasks as "pending" with a `retry_after` timestamp
5. **Evaluate `--dangerously-skip-permissions`** — consider if there's a safer alternative, or at minimum restrict Claude's working directory

### Should Fix (🟡):
6. Add auth to `/trigger/{job_name}` and `/message` endpoints
7. Add openclaw to `BUILD_COMMANDS` as TypeScript repo
8. Add circuit breaker for repeated Claude failures
9. Add `validate_force_push()` to git_ops push commands
10. Clarify openclaw targeting policy (can push or not?)
11. Add safety patterns for payment/auth/migration files
12. Add concurrency lock on task polling
13. Rate limit or cap brain-scan task creation

---

*End of audit. No code was modified.*
