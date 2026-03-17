#!/bin/bash
# Hub Metrics Snapshot Script
# Fetches key metrics from Hub API and outputs formatted summary

HUB_URL="https://hub-production-f423.up.railway.app"

# Fetch DA stats
echo "=== DropAnywhere Metrics ==="
curl -s -H "X-API-Key: $HUB_API_KEY" "$HUB_URL/api/admin/stats" | python3 -c "
import sys, json
data = json.load(sys.stdin)['stats']
print(f\"DA: {data['total_users']} users, {data['total_drops']} drops, {data['total_digests_sent']} digests\")
print(f\"     Active 24h: {data['active_24h']} | Active 7d: {data['active_7d']} | Premium: {data['premium_users']}\")
"

echo ""
echo "=== BHA / Poe ==="
echo "BHA: (see latest daily log for cached values)"
echo "Poe: (see latest daily log for cached values)"
