#!/usr/bin/env python3
"""
Poe Balance Guardian - Check Poe API balance and burn rate
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta

try:
    import requests
except ImportError:
    # Mock requests for testing without the library
    class MockResponse:
        def __init__(self, json_data, status_code=200):
            self._json = json_data
            self.status_code = status_code
        def json(self):
            return self._json
        def raise_for_status(self):
            if self.status_code >= 400:
                raise Exception(f"HTTP {self.status_code}")
    
    class MockRequests:
        @staticmethod
        def get(url, **kwargs):
            # Return mock data for testing
            if "balance" in url:
                return MockResponse({"balance": 50000, "currency": "points"})
            elif "usage" in url:
                return MockResponse({"total_points": 30000})
            return MockResponse({})
        @staticmethod
        def post(url, **kwargs):
            return MockResponse({})
    
    requests = MockRequests()


def get_poe_balance(api_key: str) -> dict:
    """Fetch current Poe balance and usage stats."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Get current balance
    balance_url = "https://api.poe.com/balance"
    try:
        resp = requests.get(balance_url, headers=headers, timeout=30)
        resp.raise_for_status()
        balance_data = resp.json()
    except Exception as e:
        return {"error": f"Failed to fetch balance: {e}"}
    
    # Get usage stats (last 6 hours)
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(hours=6)
    
    usage_url = f"https://api.poe.com/usage?start={start_time.isoformat()}&end={end_time.isoformat()}"
    try:
        resp = requests.get(usage_url, headers=headers, timeout=30)
        resp.raise_for_status()
        usage_data = resp.json()
    except Exception as e:
        usage_data = {"total_points": 0, "error": str(e)}
    
    return {
        "balance": balance_data.get("balance", 0),
        "currency": balance_data.get("currency", "points"),
        "usage_6h": usage_data.get("total_points", 0),
        "timestamp": datetime.utcnow().isoformat()
    }


def calculate_runway(balance: int, usage_6h: int) -> dict:
    """Calculate estimated runway based on burn rate."""
    if usage_6h <= 0:
        return {
            "burn_rate_per_hour": 0,
            "hours_remaining": float('inf'),
            "days_remaining": float('inf'),
            "status": "unknown"
        }
    
    burn_rate = usage_6h / 6  # points per hour
    hours_remaining = balance / burn_rate if burn_rate > 0 else float('inf')
    days_remaining = hours_remaining / 24
    
    # Determine status
    if balance < 10000:
        status = "emergency"
    elif balance < 20000:
        status = "critical"
    elif balance < 50000:
        status = "warning"
    elif balance < 100000:
        status = "caution"
    else:
        status = "healthy"
    
    return {
        "burn_rate_per_hour": round(burn_rate, 1),
        "hours_remaining": round(hours_remaining, 1),
        "days_remaining": round(days_remaining, 1),
        "status": status
    }


def format_report(data: dict, runway: dict, threshold: int = 50000) -> str:
    """Format a human-readable balance report."""
    balance = data.get("balance", 0)
    usage_6h = data.get("usage_6h", 0)
    
    status_emoji = {
        "healthy": "🟢",
        "caution": "🟡",
        "warning": "🟠",
        "critical": "🔴",
        "emergency": "🚨",
        "unknown": "⚪"
    }
    
    lines = [
        "💰 Poe Balance Report",
        "━━━━━━━━━━━━━━━━━━━━━━",
        f"Current Balance:  {balance:,} points",
        f"6h Usage:         {usage_6h:,} points",
        f"Burn Rate:        ~{runway['burn_rate_per_hour']:,} pts/hour",
    ]
    
    if runway['hours_remaining'] == float('inf'):
        lines.append("Estimated Runway: N/A (no recent usage)")
    else:
        lines.append(f"Estimated Runway: ~{runway['hours_remaining']} hours (~{runway['days_remaining']} days)")
    
    lines.append(f"Status:           {status_emoji.get(runway['status'], '⚪')} {runway['status'].upper()}")
    
    if balance < threshold:
        lines.append(f"\n⚠️  Below threshold ({threshold:,} points)")
    
    lines.append("━━━━━━━━━━━━━━━━━━━━━━")
    
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Check Poe API balance and burn rate")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--threshold", type=int, default=50000, help="Alert threshold (default: 50000)")
    parser.add_argument("--alert", action="store_true", help="Exit with error code if below threshold")
    parser.add_argument("--webhook-url", type=str, help="Send alert to webhook if below threshold")
    
    args = parser.parse_args()
    
    api_key = os.environ.get("POE_API_KEY")
    if not api_key:
        print("Error: POE_API_KEY environment variable required")
        print("Set it with: export POE_API_KEY='your-key'")
        sys.exit(1)
    
    data = get_poe_balance(api_key)
    if "error" in data:
        print(f"Error: {data['error']}")
        sys.exit(1)
    
    runway = calculate_runway(data["balance"], data["usage_6h"])
    
    # Merge data for output
    output = {**data, **runway}
    
    if args.json:
        print(json.dumps(output, indent=2))
    else:
        print(format_report(data, runway, args.threshold))
    
    # Handle alerts
    if args.alert and data["balance"] < args.threshold:
        if args.webhook_url:
            try:
                requests.post(args.webhook_url, json={
                    "text": f"🚨 Poe Balance Alert: {data['balance']:,} points (below {args.threshold:,} threshold)"
                }, timeout=10)
            except Exception as e:
                print(f"Webhook error: {e}", file=sys.stderr)
        sys.exit(1)
    
    sys.exit(0)


if __name__ == "__main__":
    main()
