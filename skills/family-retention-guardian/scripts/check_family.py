#!/usr/bin/env python3
"""
Family Retention Guardian - Main Monitoring Script

Monitors Joey's family members in DropAnywhere and creates re-engagement 
tasks when they become inactive. Addresses Pattern 285: Family retention 
as execution canary.

Usage:
    python3 check_family.py                    # Check all family members
    python3 check_family.py --email EMAIL     # Check specific member
    python3 check_family.py --create-tasks    # Create re-engagement tasks
"""

import os
import sys
import json
import requests
import argparse
from datetime import datetime, timedelta
from typing import List, Dict, Optional

# Hub API configuration
HUB_URL = os.getenv("HUB_URL", "https://hub-production-f423.up.railway.app")
API_KEY = os.getenv("HUB_API_KEY") or os.getenv("INGEST_API_KEY")

if not API_KEY:
    print("❌ Error: HUB_API_KEY not found in environment")
    sys.exit(1)

HEADERS = {
    "X-API-Key": API_KEY,
    "Content-Type": "application/json"
}

# Family member patterns (auto-detected)
FAMILY_PATTERNS = [
    "hamer.daniel@gmail.com",
    "lhamer228@gmail.com", 
    "rhamersunsetpartners@gmail.com"
]

# Risk thresholds
RISK_THRESHOLDS = {
    "HEALTHY": {"days": 7, "engagement": 70},
    "AT_RISK": {"days": 14, "engagement": 30},
    "CRITICAL": {"days": 30, "engagement": 10},
    "ABANDONED": {"days": 60, "engagement": 0}
}

def get_user_data():
    """Fetch all users from Hub API."""
    try:
        response = requests.get(f"{HUB_URL}/api/admin/users", headers=HEADERS)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Failed to fetch users: {response.status_code}")
            return []
    except requests.RequestException as e:
        print(f"❌ API request failed: {e}")
        return []

def identify_family_members(users) -> List[Dict]:
    """Identify family members from user list."""
    family_members = []
    
    # Handle case where users might be a list of strings or other format
    if not users or not isinstance(users, list):
        return family_members
        
    for user in users:
        # Handle different user object formats
        if isinstance(user, str):
            email = user.lower()
            user_obj = {"email": user}
        elif isinstance(user, dict):
            # Use delivery_email from API response
            email = user.get("delivery_email", "").lower()
            user_obj = user
        else:
            continue
        
        # Skip if no email
        if not email:
            continue
        
        # Check against known family patterns
        if any(pattern.lower() in email for pattern in FAMILY_PATTERNS):
            family_members.append(user_obj)
            continue
            
        # Check for Hamer family name pattern
        if "hamer" in email and "@" in email:
            family_members.append(user_obj)
    
    return family_members

def calculate_engagement_score(user: Dict) -> int:
    """Calculate engagement score based on activity patterns."""
    # Simple scoring based on available data
    score = 100
    
    # Reduce score based on inactivity
    if user.get("last_drop"):
        last_drop = datetime.fromisoformat(user["last_drop"].replace('Z', '+00:00'))
        days_inactive = (datetime.now() - last_drop.replace(tzinfo=None)).days
        score -= min(days_inactive * 5, 80)  # Max 80 point deduction
    else:
        score = 0  # No drops ever
    
    # Boost score for recent vault activity
    vault_count = user.get("vault_count", 0)
    if vault_count > 0:
        score += min(vault_count * 2, 20)  # Max 20 point boost
    
    return max(0, min(100, score))

def assess_risk_level(user: Dict, engagement_score: int) -> str:
    """Determine risk level for family member."""
    if user.get("last_drop"):
        last_drop = datetime.fromisoformat(user["last_drop"].replace('Z', '+00:00'))
        days_inactive = (datetime.now() - last_drop.replace(tzinfo=None)).days
    else:
        days_inactive = 999  # Never active
    
    if days_inactive >= RISK_THRESHOLDS["ABANDONED"]["days"]:
        return "ABANDONED"
    elif days_inactive >= RISK_THRESHOLDS["CRITICAL"]["days"] or engagement_score <= RISK_THRESHOLDS["CRITICAL"]["engagement"]:
        return "CRITICAL"
    elif days_inactive >= RISK_THRESHOLDS["AT_RISK"]["days"] or engagement_score <= RISK_THRESHOLDS["AT_RISK"]["engagement"]:
        return "AT_RISK"
    else:
        return "HEALTHY"

def create_reengagement_task(user: Dict, risk_level: str) -> Optional[Dict]:
    """Create re-engagement task for at-risk family member."""
    
    email = user.get("delivery_email")
    user_id = user.get("user_id")
    
    if risk_level == "HEALTHY":
        return None
        
    # Generate appropriate message based on risk level
    messages = {
        "AT_RISK": f"Hey! Haven't seen any drops from you lately. Everything okay? No pressure, just checking in. 💜",
        "CRITICAL": f"Missing your perspective in DropAnywhere. Would love to hear what's on your mind. 🤗",
        "ABANDONED": f"Haven't heard from you in a while. Hope you're doing well! Thinking of you. ❤️"
    }
    
    task = {
        "type": "family_reengagement",
        "priority": "high" if risk_level == "CRITICAL" else "medium",
        "target_email": email,
        "target_user_id": user_id,
        "risk_level": risk_level,
        "suggested_message": messages.get(risk_level),
        "action_required": "gentle_personal_outreach",
        "deadline": (datetime.now() + timedelta(days=2)).isoformat(),
        "created_by": "family-retention-guardian",
        "notes": f"Family member {email} assessed as {risk_level}. Requires personal touch from Joey."
    }
    
    return task

def send_critical_alert(family_summary: Dict):
    """Send WhatsApp alert to Joey for critical family issues."""
    critical_members = [m for m in family_summary["members"] if m["status"] in ["CRITICAL", "ABANDONED"]]
    
    if not critical_members:
        return
        
    alert_text = "🚨 FAMILY ALERT 🚨\n\n"
    
    for member in critical_members:
        email = member["email"].split("@")[0]  # Remove domain for privacy
        days = member["days_inactive"]
        alert_text += f"• {email}: {days}d inactive ({member['status']})\n"
    
    alert_text += "\nGentle outreach recommended. Check DropAnywhere tasks for suggestions. 💜"
    
    # Would integrate with WhatsApp API here
    print(f"📱 WhatsApp Alert: {alert_text}")

def main():
    parser = argparse.ArgumentParser(description="Family Retention Guardian")
    parser.add_argument("--email", help="Check specific family member by email")
    parser.add_argument("--create-tasks", action="store_true", help="Create re-engagement tasks")
    args = parser.parse_args()
    
    print("👨‍👩‍👧‍👦 Family Retention Guardian")
    print("=" * 50)
    
    # Fetch user data
    api_response = get_user_data()
    if not api_response:
        print("❌ Could not fetch user data")
        return
        
    # Extract users array from API response
    users = api_response.get("users", []) if isinstance(api_response, dict) else api_response
    
    # Identify family members
    family_members = identify_family_members(users)
    
    if args.email:
        family_members = [u for u in family_members if u.get("email", "").lower() == args.email.lower()]
        if not family_members:
            print(f"❌ Family member {args.email} not found")
            return
    
    if not family_members:
        print("✅ No family members found (this might be an issue)")
        return
    
    # Analyze family members
    family_analysis = []
    tasks_created = []
    
    for user in family_members:
        engagement_score = calculate_engagement_score(user)
        risk_level = assess_risk_level(user, engagement_score)
        
        last_drop = user.get("last_drop")
        days_inactive = 0
        if last_drop:
            last_drop_dt = datetime.fromisoformat(last_drop.replace('Z', '+00:00'))
            days_inactive = (datetime.now() - last_drop_dt.replace(tzinfo=None)).days
        else:
            days_inactive = 999
            
        member_analysis = {
            "email": user.get("delivery_email"),
            "user_id": user.get("user_id"),
            "status": risk_level,
            "last_drop": last_drop,
            "days_inactive": days_inactive,
            "engagement_score": engagement_score,
            "vault_count": user.get("vault_count", 0),
            "digest_enabled": user.get("digest_enabled", False),
            "digests_since_engagement": user.get("digests_since_engagement", 0)
        }
        
        family_analysis.append(member_analysis)
        
        # Create re-engagement task if needed
        if args.create_tasks:
            task = create_reengagement_task(user, risk_level)
            if task:
                tasks_created.append(task)
    
    # Generate summary
    overall_status = "HEALTHY"
    critical_count = len([m for m in family_analysis if m["status"] in ["CRITICAL", "ABANDONED"]])
    at_risk_count = len([m for m in family_analysis if m["status"] == "AT_RISK"])
    
    if critical_count > 0:
        overall_status = "CRITICAL"
    elif at_risk_count > 0:
        overall_status = "AT_RISK"
    
    summary = {
        "timestamp": datetime.now().isoformat(),
        "family_status": overall_status,
        "total_family_members": len(family_analysis),
        "healthy": len([m for m in family_analysis if m["status"] == "HEALTHY"]),
        "at_risk": at_risk_count,
        "critical": len([m for m in family_analysis if m["status"] == "CRITICAL"]),
        "abandoned": len([m for m in family_analysis if m["status"] == "ABANDONED"]),
        "members": family_analysis,
        "tasks_created": tasks_created
    }
    
    # Display results
    print(f"\n📊 FAMILY STATUS: {overall_status}")
    print(f"Total members: {len(family_analysis)}")
    print(f"✅ Healthy: {summary['healthy']}")
    print(f"⚠️  At Risk: {summary['at_risk']}")
    print(f"🚨 Critical: {summary['critical']}")
    print(f"💀 Abandoned: {summary['abandoned']}")
    
    print("\n👥 MEMBER DETAILS:")
    for member in family_analysis:
        email_short = member["email"].split("@")[0] if member["email"] else "unknown"
        status_emoji = {"HEALTHY": "✅", "AT_RISK": "⚠️", "CRITICAL": "🚨", "ABANDONED": "💀"}
        emoji = status_emoji.get(member["status"], "❓")
        
        print(f"{emoji} {email_short}: {member['days_inactive']}d inactive, {member['engagement_score']}% engagement")
        
        if member["status"] != "HEALTHY":
            print(f"   └─ Action: {member['status']} - requires attention")
    
    if tasks_created:
        print(f"\n✉️  TASKS CREATED: {len(tasks_created)}")
        for task in tasks_created:
            print(f"• {task['type']} for {task['target_email'].split('@')[0]}")
    
    # Send alerts for critical issues
    if critical_count > 0:
        send_critical_alert(summary)
    
    # Output JSON for automation
    print(f"\n📄 JSON OUTPUT:")
    print(json.dumps(summary, indent=2, default=str))
    
    return summary

if __name__ == "__main__":
    main()