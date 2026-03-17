# Hub main.py — Code Map (27,526 lines)

**Last Updated:** 2026-03-17 05:53 CDT  
**Source:** `ph0t0bar/opoerator-hub` main.py (main branch)  
**Author:** Claw (grep + read analysis)

---

## Overview

`main.py` is the monolith. 27,526 lines of Python (Starlette/FastAPI + asyncpg + Poe fastpath). Everything lives here — ingestion, classification, digests, intelligence maps, alerts, admin, sequences, webhooks.

---

## Major Sections by Line Range

| Lines | Section | Key Functions/Endpoints |
|-------|---------|------------------------|
| 1-200 | Imports, config, globals | DB pool, Poe key, env vars |
| 1720-1878 | **Drop Classification** | `classify_drop_v2()` — Gemini-3-Flash + regex fallback |
| 3335-3465 | **Feature Registry** | `intelligence_maps` endpoints, capabilities |
| 3465-3530 | **Content Extraction** | MemoryVault-2.0 (Gemini 2.0 Flash) extraction |
| 3976+ | **Entity Extraction** | Connection surfacing (Phase 1 Intelligence Layer) |
| 4671-4690 | **Intelligence Classification** | Per-drop intelligence layer classification |
| 5416-5476 | **DCS Worker Synthesis** | Processed intelligence from code agent |
| 9320+ | **Phase 1 Intelligence Layer** | Background processing display |
| 10529-10650 | **Extracted Nodes Integration** | Stage 1 Gemini nodes → Stage 2 specialist |
| 10839+ | **Accept.AI** | Adaptive emotional intelligence analyzer |
| 10958 | **Bot Name Aliases** | Maps analyzer keys to Poe bot names |
| 11437-11580 | **Node Extraction** | `extract_nodes_with_gemini()` — Stage 1 of digest |
| 11719-11970 | **Digest Pipeline** | Full two-stage digest generation |
| 20204-20212 | **Archive/Complete Logic** | Excluded from digests + intelligence maps |
| 21475-21478 | **Intelligence Scheduler** | Daily map generation startup |
| 27034-27167 | **Intelligence Map Prompt** | `_INTEL_MAP_PROMPT` + `_intel_map_fallback()` |
| 27167-27350 | **Intelligence Map Generation** | `_generate_intelligence_map_for_user()` + API endpoints |
| 27273-27382 | **Intelligence API** | `/api/intelligence/generate`, `/api/intelligence/latest`, `/api/intelligence/history` |

---

## All Python Files in Hub

| File | Purpose |
|------|---------|
| `main.py` | The monolith (27,526 lines) |
| `config.py` | Configuration, env vars |
| `db.py` | Database connection, pool management |
| `audit_log.py` | Audit logging |
| `bookmark_parser.py` | Bookmark import parsing |
| `catch_router.py` | Catch/digest routing logic |
| `export_routes.py` | Data export endpoints |
| `list_models.py` | Available model listing |
| `migrate_to_postgres.py` | JSON→Postgres migration |
| `openai_bridge.py` | OpenAI API compatibility layer |
| `opoerator_cli.py` | CLI tools |
| `opoerator_test_suite.py` | Test suite |
| `pass_layer.py` | PASS Protocol layer (internal, never expose to users) |
| `poe_cost_tracker.py` | Poe balance monitoring |
| `poe_orchestrator.py` | God Mode 15 routing (477 lines) |
| `public_mark_generator.py` | Public sharing mark generation |
| `retry_util.py` | Retry logic utilities |
| `screenshot_service.py` | Screenshot processing |
| `sequences.py` | Drip/onboarding email sequences |
| `snapback_generator.py` | Snapback email generation |
| `scripts/ai_test_team.py` | AI-powered testing |
| `tools/fire_to_orchestr8.py` | Manual orchestr8 trigger |
| `tools/generate_hydration_pack.py` | Hydration pack generator |
| `tools/maintenance_audit.py` | Maintenance audit tool |

---

## Key API Endpoints (from code analysis)

### Drop Management
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/ingest` | POST | Drop ingestion (all sources) |
| `/api/drops/{user_id}` | GET | Fetch user drops |
| `/api/search` | GET | Search drops |

### Intelligence
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/intelligence/generate` | POST | Generate intelligence map |
| `/api/intelligence/latest` | GET | Get latest cached map |
| `/api/intelligence/history` | GET | Map generation history |
| `/api/intelligence/{user_id}` | GET | User's intelligence data |

### Digests
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/digest/generate` | POST | Trigger digest for user |
| `/api/digest/schedule` | GET/POST | Digest scheduling |

### Admin
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/admin/stats` | GET | User stats, drop counts |
| `/api/admin/drops/activity` | GET | Drop activity feed |
| `/api/admin/users` | GET | User list |
| `/api/ops/dashboard` | GET | System health |
| `/api/ops/tasks` | GET/POST | Task queue |
| `/api/ops/tasks/{id}` | PATCH | Approve/reject tasks |

### Settings
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/settings/{user_id}` | GET/PUT | User settings (compass, style, etc.) |

### Alerts
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/alerts` | POST | Send alerts |
| `/api/alerts/daily-summary` | POST | Trigger daily summary |
| `/api/alerts/run-monitors` | POST | Manual monitor trigger |

### Webhooks
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/webhook/email` | POST | Resend email webhook |
| `/hooks/agent` | POST | OpenClaw agent webhook |

### Poe
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/poe/v1/chat/completions` | POST | Poe orchestrator (God Mode 15) |

---

## Database Tables (inferred)

| Table | Key Fields |
|-------|-----------|
| `vault_items` | id, user_id, text, title, drop_type, area, domain, priority, status, entities, tags, due_date, classification, created_at, completed_at |
| `intelligence_maps` | id, user_id, map_data (jsonb), node_count, link_count, drop_count, generation_time_ms, generated_at |
| `users` | user_id, email, name, digest_enabled, digest_frequency, settings, created_at |
| `digests` | id, user_id, content, analyzer, sent_at |
| `tasks` | id, title, description, assignee, target_repo, type, priority, status, result, created_by, created_at |

---

## Gemini Usage Map

| Function | Model | Purpose | Timeout |
|----------|-------|---------|---------|
| `classify_drop_v2()` | Gemini-3-Flash | Drop classification | 8s |
| `extract_nodes_with_gemini()` | Gemini-3-Flash | Digest node extraction | 30s |
| `_generate_intelligence_map_for_user()` | Gemini-3-Flash | Full intelligence map | 30s |
| Content extraction (line 3522) | MemoryVault-2.0 (Gemini 2.0 Flash) | Intelligent extraction | — |
| Frontend extract-intelligence.ts | Gemini-3-Flash | Rich item extraction | — |

---

## Alert Monitors (Hub-Side)

All run inside Hub with `ENABLE_ALERT_MONITORS=true`:

| Monitor | Interval | Alert Condition |
|---------|----------|-----------------|
| Hub Health | 1h | Latency > 5s |
| Digest Pipeline | 1h | Stalled users (no digest in 36h) |
| Error Rate | 1h | > 20 errors/hour |
| Stripe | 4h | New sales or failed charges |
| GitHub CI + Security | 6h | Failed workflows, dependabot alerts |
| Poe Costs | 6h | Balance < 500, burn > 5K/6h |
| Resend Email | 6h | Bounces, delivery issues |
| Railway | 6h | Failed deployments |
| Google Analytics | 6h | Traffic data |
| Daily Ops Summary | 24h (~9am UTC) | Full metrics summary |

---

*This is a living reference. Update after significant Hub deploys or refactors.*
