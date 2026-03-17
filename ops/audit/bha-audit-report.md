# BrutallyHonest.ai Audit — Data Isolation from DropAnywhere

**Date:** 2026-03-16
**Repo:** `ph0t0bar/brutallyhonest-next`
**Context:** Ensure BHA and DA are properly separated — no data leakage between products

---

## a) Do BHA users automatically become DA users?

🔴 **FIX BEFORE LAUNCH — YES, there is cross-contamination.**

BHA has a `sync-to-opoerator` API route (`src/app/api/sync-to-opoerator/route.ts`) that:
- Sends BHA chat conversations to Hub's `/api/webhook/bha` endpoint
- Includes `user_email`, `persona`, and full message history
- Called from `Chat.tsx:316` after conversations

This means **every BHA user's email and conversations flow into the Hub (DA backend)**. While this is a webhook (not creating DA accounts), the Hub receives BHA user data, which blurs the isolation boundary.

**Additionally:** `src/app/api/vault/drop/route.ts:48` tags drops with `dropped_from: 'brutallyhonest.ai'` — so BHA data is explicitly flowing into the DA vault system.

**Fix:** Decide if this sync is intentional analytics or an isolation violation. If BHA and DA should be fully separate, remove the sync-to-opoerator route entirely.

---

## b) Shared database tables or user records?

🟢 **OK — Separate databases.**

BHA has its own Prisma schema with its own PostgreSQL database:
- `User`, `OTPCode`, `RateLimit`, `StripeEvent`, `BlockedEmail` tables
- No references to DA tables or Hub database
- User model is BHA-specific (credits, subscription, abuse flags)

The only cross-system data flow is the sync-to-opoerator webhook (see item a).

---

## c) Does BHA send emails from drop-anywhere.com?

🟢 **OK — All emails use BHA domains.**

| Sender | Domain | Used In |
|--------|--------|---------|
| `BrutallyHonest.ai <security@brutallyhonest.ai>` | ✅ BHA | Auth emails |
| `Joey from BrutallyHonest.ai <joey@notifications.brutallyhonest.ai>` | ✅ BHA | Milestone/credit emails |

No references to `@drop-anywhere.com` in any email sending code. Support email is `support@brutallyhonest.ai`.

---

## d) Stripe integration — properly scoped to BHA only?

🟢 **OK — BHA-specific Stripe links and products.**

- Stripe payment links are BHA-specific (`buy.stripe.com/...`)
- Products: Pay-as-you-Go ($4.99), Pro Monthly ($7/mo), Founders Mode ($47)
- Webhook handler (`src/app/api/webhooks/stripe/route.ts`) processes events against BHA's own User table
- No DA pricing or DA Stripe references

**Note:** Both BHA and DA use the same Stripe account (same `STRIPE_SECRET_KEY` on the gateway). This is fine architecturally — products/prices are separate — but worth knowing.

---

## e) Shared API keys between BHA and DA?

🟡 **SHOULD FIX — Some keys are shared.**

| Key | BHA Uses | DA Uses | Shared? |
|-----|----------|---------|---------|
| `RESEND_API_KEY` | Auth + milestone emails | Digest emails | ⚠️ Same Resend account |
| `HUB_API_KEY` | sync-to-opoerator calls | Core API auth | ⚠️ Same key |
| `STRIPE_SECRET_KEY` | BHA payments | DA payments (future) | ⚠️ Same Stripe account |
| `OPENROUTER_API_KEY` | BHA chat | Not used by DA | 🟢 BHA only |
| `NOTION_API_KEY` | BHA personas/users | Not used by DA | 🟢 BHA only |
| `DATABASE_URL` | BHA Postgres | DA Postgres (Hub) | 🟢 Different databases |

**Fix:** The shared Resend account is fine (different sender domains). The `HUB_API_KEY` sharing is the real concern — it means BHA can authenticate as DA to the Hub. Consider a separate `BHA_HUB_KEY` with limited scope.

---

## f) Cross-references to Hub/DA endpoints?

🔴 **FIX BEFORE LAUNCH — Active cross-references exist.**

| File | Reference | Risk |
|------|-----------|------|
| `src/lib/config.ts:220` | `API_URL` defaults to Hub production URL | Data flows to DA backend |
| `src/app/api/sync-to-opoerator/route.ts` | Posts to Hub's `/api/webhook/bha` | BHA conversations → DA |
| `src/components/chat/Chat.tsx:316` | Calls sync-to-opoerator after chats | Automatic data sharing |
| `src/app/api/vault/drop/route.ts:48` | Tags drops as `dropped_from: 'brutallyhonest.ai'` | BHA drops enter DA vault |

**The sync-to-opoerator pattern is the main isolation concern.** It's a deliberate integration, not accidental — but it means BHA user data (emails, conversations) flows into DA's Hub database.

**Decision needed:** Is this cross-pollination intentional (BHA feeds DA's intelligence) or a violation of data separation?

---

## g) TODO/FIXME/HACK Results

12 matches found:

| File | Issue | Severity |
|------|-------|----------|
| `src/lib/mythos/memory.ts:71` | `TODO: Implement Radiant query` | 🟡 Incomplete feature |
| `src/app/api/chat/route.ts:179` | `TODO: Check subscription status for premium personas` | 🔴 Revenue leak — premium personas accessible without check |
| `src/app/api/user/sync/route.ts` (4×) | `TODO: Add favorites/custom persona storage to Postgres` | 🟡 Missing feature |
| `src/app/api/user/data/route.ts` (3×) | `TODO: Implement with Postgres` | 🟡 Missing feature |
| `src/app/api/webhooks/stripe/route.ts:460-461` | `TODO: Send notification` + `TODO: Update subscription_status` | 🔴 Missing payment failure handling |

---

## Summary

| Category | Rating | Action |
|----------|--------|--------|
| User cross-contamination | 🔴 FIX BEFORE LAUNCH | sync-to-opoerator sends BHA data to DA Hub |
| Database isolation | 🟢 OK | Separate Postgres databases |
| Email domains | 🟢 OK | BHA uses @brutallyhonest.ai only |
| Stripe scoping | 🟢 OK | Products properly separated |
| API key sharing | 🟡 SHOULD FIX | HUB_API_KEY shared, consider scoped key |
| Hub cross-references | 🔴 FIX BEFORE LAUNCH | 4 active references to Hub endpoints |
| TODOs | 🟡 SHOULD FIX | 2 revenue-impacting TODOs |

**Key Decision for Joey:** The `sync-to-opoerator` integration is the #1 isolation concern. BHA conversations flow into the DA Hub. Is this:
1. **Intentional** — BHA is a feeder for DA intelligence? → Document it, secure it, add user consent
2. **A violation** — Users didn't consent to cross-product data sharing? → Remove the route, delete Hub-side BHA data
