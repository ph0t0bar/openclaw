#!/usr/bin/env python3
"""
Digest Pipeline Health Monitor - Core pipeline health check
Monitors DropAnywhere digest delivery vs expected baseline
"""

import os
import sys
import json
import requests
from datetime import datetime, timedelta
import argparse

def get_hub_metrics():
    """Fetch digest metrics from Hub dashboard API"""
    try:
        api_key = os.getenv('HUB_API_KEY') or os.getenv('INGEST_API_KEY')
        if not api_key:
            return {"error": "HUB_API_KEY not found"}
        
        url = "https://hub-production-f423.up.railway.app/api/ops/dashboard"
        headers = {"X-API-Key": api_key}
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        return {
            "users_total": data.get("users", 0),
            "digests_sent_24h": data.get("digests_sent", 0),
            "drops_24h": data.get("drops_24h", 0),
            "active_users_24h": data.get("active_24h", 0),
            "errors_24h": data.get("errors", 0),
            "status": "success"
        }
        
    except Exception as e:
        return {"error": f"Hub API error: {str(e)}"}

def check_dropper_code_health():
    """Check Dropper-Code service health and credit status"""
    try:
        # Health endpoint
        response = requests.get("https://dropper-code-production.up.railway.app/health", timeout=5)
        if response.status_code == 200:
            health_data = response.json()
            return {
                "status": "healthy",
                "service": health_data,
                "credit_status": "unknown"  # Would need specific endpoint for this
            }
        else:
            return {"status": "degraded", "http_code": response.status_code}
            
    except Exception as e:
        return {"status": "failed", "error": str(e)}

def calculate_expected_digests(total_users, active_users_24h):
    """Calculate expected digest count based on user base"""
    # Historical baseline: ~70-85% of total users get digests
    # Factor in active users as higher priority
    
    # Conservative estimate: 70% of total users
    base_expected = int(total_users * 0.70)
    
    # Adjust for activity level
    if active_users_24h > 0:
        activity_factor = min(active_users_24h / total_users, 0.3)  # Cap at 30% boost
        base_expected = int(base_expected * (1 + activity_factor))
    
    return base_expected

def analyze_pipeline_health(metrics):
    """Analyze pipeline health and return status assessment"""
    if "error" in metrics:
        return {
            "status": "unknown",
            "severity": "critical", 
            "message": f"Cannot assess: {metrics['error']}"
        }
    
    total_users = metrics["users_total"]
    digests_sent = metrics["digests_sent_24h"]
    expected_digests = calculate_expected_digests(total_users, metrics["active_users_24h"])
    
    if expected_digests == 0:
        delivery_rate = 0
    else:
        delivery_rate = (digests_sent / expected_digests) * 100
    
    # Status assessment
    if delivery_rate >= 75:
        status = "healthy"
        severity = "info"
    elif delivery_rate >= 50:
        status = "degraded"
        severity = "warning"
    elif delivery_rate >= 25:
        status = "critical"
        severity = "critical"
    else:
        status = "failed"
        severity = "emergency"
    
    # Special case: Zero digests with significant user base
    if digests_sent == 0 and total_users > 50:
        status = "stalled"
        severity = "emergency"
    
    return {
        "status": status,
        "severity": severity,
        "delivery_rate": round(delivery_rate, 1),
        "digests_sent": digests_sent,
        "digests_expected": expected_digests,
        "users_total": total_users,
        "users_affected": max(0, expected_digests - digests_sent),
        "message": f"{digests_sent}/{expected_digests} digests sent ({delivery_rate:.1f}% delivery rate)"
    }

def main():
    parser = argparse.ArgumentParser(description="Check digest pipeline health")
    parser.add_argument("--format", choices=["json", "human"], default="human")
    parser.add_argument("--threshold", type=int, default=50, help="Alert threshold percentage")
    args = parser.parse_args()
    
    # Get metrics
    metrics = get_hub_metrics()
    dropper_health = check_dropper_code_health()
    
    # Analyze health
    health = analyze_pipeline_health(metrics)
    
    # Combine results
    result = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "pipeline": health,
        "infrastructure": {
            "hub": "healthy" if "error" not in metrics else "failed",
            "dropper_code": dropper_health["status"]
        },
        "raw_metrics": metrics if "error" not in metrics else {},
        "alert_required": health["delivery_rate"] < args.threshold if "delivery_rate" in health else True
    }
    
    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        # Human readable output
        print(f"🔍 DIGEST PIPELINE HEALTH CHECK - {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        if health["status"] == "healthy":
            emoji = "✅"
        elif health["status"] == "degraded":
            emoji = "⚠️"
        elif health["status"] in ["critical", "failed", "stalled"]:
            emoji = "🚨"
        else:
            emoji = "❓"
            
        print(f"{emoji} Status: {health['status'].upper()}")
        print(f"📊 {health['message']}")
        
        if "users_affected" in health and health["users_affected"] > 0:
            print(f"👥 Users affected: {health['users_affected']}")
        
        print(f"\n🏗️  Infrastructure:")
        print(f"   Hub API: {result['infrastructure']['hub']}")
        print(f"   Dropper-Code: {result['infrastructure']['dropper_code']}")
        
        if result["alert_required"]:
            print(f"\n🚨 ALERT: Delivery rate below {args.threshold}% threshold")
            
        # Next steps
        if health["status"] in ["critical", "failed", "stalled"]:
            print(f"\n🔧 RECOMMENDED ACTIONS:")
            if result['infrastructure']['dropper_code'] != 'healthy':
                print(f"   • Check Dropper-Code service health and credit status")
            if health['digests_sent'] == 0:
                print(f"   • Consider emergency digest generation for VIP users")
                print(f"   • Check Hub scheduler and cron job configuration") 
            print(f"   • Monitor error logs around {datetime.utcnow().strftime('%Y-%m-%d %H:00')} UTC")

if __name__ == "__main__":
    main()