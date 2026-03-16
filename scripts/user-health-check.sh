#!/bin/bash
# User Health Check Script - DropAnywhere Hub
# Checks for at-risk users, digest failures, and inactivity

HUB_URL="https://hub-production-f423.up.railway.app"
API_KEY="${HUB_API_KEY:-${INGEST_API_KEY}}"

if [ -z "$API_KEY" ]; then
    echo "ERROR: HUB_API_KEY or INGEST_API_KEY not set"
    exit 1
fi

echo "=== DropAnywhere User Health Check ==="
echo "Timestamp: $(date -u '+%Y-%m-%d %H:%M UTC')"
echo ""

# Fetch admin stats
echo "--- Admin Stats ---"
STATS=$(curl -s -H "X-API-Key: $API_KEY" "$HUB_URL/api/admin/stats" 2>/dev/null)
echo "$STATS" | head -20

# Fetch users list  
echo ""
echo "--- User List ---"
USERS=$(curl -s -H "X-API-Key: $API_KEY" "$HUB_URL/api/admin/users" 2>/dev/null)
echo "$USERS" | head -50

# Check for family members
echo ""
echo "--- Family Members Status ---"
echo "$USERS" | grep -E "(lhamer228|rhamersunsetpartners|hamer.daniel|danny|daniel)" || echo "Family members not found in user list"

# Fetch recent drop activity
echo ""
echo "--- Recent Drop Activity ---"
ACTIVITY=$(curl -s -H "X-API-Key: $API_KEY" "$HUB_URL/api/admin/drops/activity?limit=50" 2>/dev/null)
echo "$ACTIVITY" | head -30

echo ""
echo "=== End Health Check ==="
