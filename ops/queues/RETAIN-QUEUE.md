# RETAIN QUEUE — User Health & Onboarding
# Updated: 2026-03-18
# Owner: RETAIN DRIVER

## Every Cycle Checks
- Run user health check: bash /root/.openclaw/workspace/scripts/user-health-check.sh
- Check new users (last 72h): are they dropping? Did drip emails fire?
- Check digest delivery: all eligible users receiving digests?
- Check family members: lhamer228 (mom), rhamersunsetpartners (dad/Bob), hamer.daniel (Danny)

## Alert Thresholds
- Family member at risk → ESCALATE (write to ops/escalations.md)
- New user inactive >48h after first drop → flag
- Digest delivery failure for multiple users → flag
- Any user explicitly unhappy → ESCALATE

## Current Known Issues
- Digests intentionally paused (see ops/DIGEST-POLICY.md) — do NOT flag this
- one@0it.us drops in Spanish — check if digest language matches

## Completed Actions
_(RETAIN DRIVER logs actions here)_
