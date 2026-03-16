# Digest Policy — DO NOT CHANGE WITHOUT JOEY'S APPROVAL

**Last Updated:** 2026-03-16 by Joey (direct instruction)

## Current State: DIGESTS ARE OFF (BY DESIGN)

- `DISABLE_CRONS=1` on Hub — intentional
- `dropanywhere-cron` service is not running — intentional
- Only **Joey** (joeyhamer@gmail.com) should receive any emails

## Admission Process

1. Users join the **waitlist** first
2. Users are **admitted** when the platform is ready
3. Only admitted users receive digests
4. BHA users are **NOT** DropAnywhere users — they did not sign up and must NOT receive DA emails

## When Digests Go Live

- Joey will flip the switch when ready
- Service will be **email-only** (no dashboard initially)
- Resend is the delivery mechanism (already configured)

## Rules for Agents / Dropper-Code

- ❌ DO NOT create "fix digest stall" tasks — the low numbers are by design
- ❌ DO NOT enable digest sending for unadmitted users
- ❌ DO NOT auto-approve any task that changes digest delivery scope
- ✅ DO fix digest code quality (error handling, templates, etc.) — just don't enable delivery
- ✅ DO flag actual bugs in digest generation logic (but don't turn on sending)
