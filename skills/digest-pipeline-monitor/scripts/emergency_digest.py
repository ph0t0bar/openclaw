#!/usr/bin/env python3
"""
Emergency Digest Generator - Manual digest creation when automation fails
Bypasses failed Dropper-Code service to generate critical digests
"""

import os
import sys
import json
import requests
import argparse
from datetime import datetime, timedelta

def get_user_drops(user_id, hours=24):
    """Fetch recent drops for a user from Hub API"""
    try:
        api_key = os.getenv('HUB_API_KEY') or os.getenv('INGEST_API_KEY')
        if not api_key:
            return {"error": "HUB_API_KEY not found"}
        
        url = f"https://hub-production-f423.up.railway.app/api/search?user_id={user_id}&limit=20"
        headers = {"X-API-Key": api_key}
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Filter to recent drops within time window
        cutoff = datetime.utcnow() - timedelta(hours=hours)
        recent_drops = []
        
        for drop in data.get('results', []):
            created_at = drop.get('created_at', '')
            if created_at:
                try:
                    drop_time = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                    if drop_time.replace(tzinfo=None) > cutoff:
                        recent_drops.append(drop)
                except:
                    # Include if we can't parse date (better safe than sorry)
                    recent_drops.append(drop)
        
        return {"drops": recent_drops, "total": len(recent_drops)}
        
    except Exception as e:
        return {"error": f"Hub API error: {str(e)}"}

def generate_digest_content(drops_data):
    """Generate digest content from user drops"""
    if "error" in drops_data:
        return {"error": drops_data["error"]}
    
    drops = drops_data["drops"]
    total = drops_data["total"]
    
    if total == 0:
        return {
            "subject": "Your DropAnywhere Digest (No New Content)",
            "content": """
<h2>Your Daily Digest</h2>
<p>No new drops captured in the last 24 hours.</p>
<p>Remember: you can capture content by:</p>
<ul>
<li>Emailing to your DropAnywhere address</li>
<li>Using the browser extension</li>
<li>Forwarding interesting content</li>
</ul>
<p>Your vault is ready when inspiration strikes! 🦜</p>
"""
        }
    
    # Group drops by source
    sources = {}
    for drop in drops:
        source = drop.get('source', 'unknown')
        if source not in sources:
            sources[source] = []
        sources[source].append(drop)
    
    # Generate content sections
    content_parts = [
        f"<h2>Your Daily Digest - {total} New Items</h2>",
        f"<p>Captured between {datetime.utcnow().strftime('%Y-%m-%d')} and today.</p>"
    ]
    
    for source, source_drops in sources.items():
        content_parts.append(f"<h3>From {source.title()} ({len(source_drops)} items)</h3>")
        content_parts.append("<ul>")
        
        for drop in source_drops[:10]:  # Limit to 10 items per source
            content = drop.get('content', 'No content')[:200]  # Truncate long content
            timestamp = drop.get('created_at', '')
            
            content_parts.append(f"<li><strong>{content}</strong>")
            if timestamp:
                try:
                    dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                    content_parts.append(f" <em>({dt.strftime('%H:%M')})</em>")
                except:
                    pass
            content_parts.append("</li>")
        
        if len(source_drops) > 10:
            content_parts.append(f"<li><em>...and {len(source_drops) - 10} more items</em></li>")
        
        content_parts.append("</ul>")
    
    content_parts.append('<p style="margin-top: 30px; color: #666;">Generated manually due to pipeline issues - we\'re working on it! 🦜</p>')
    
    return {
        "subject": f"Your DropAnywhere Digest - {total} New Items",
        "content": "\n".join(content_parts)
    }

def send_emergency_digest(user_email, subject, content, dry_run=False):
    """Send digest via Resend API"""
    if dry_run:
        return {"status": "dry_run", "message": "Would send digest", "preview": content[:500] + "..."}
    
    try:
        resend_key = os.getenv('RESEND_API_KEY')
        if not resend_key:
            return {"error": "RESEND_API_KEY not found"}
        
        from_email = os.getenv('RESEND_FROM_EMAIL', 'DropAnywhere <hello@drop-anywhere.com>')
        
        payload = {
            "from": from_email,
            "to": [user_email],
            "subject": subject,
            "html": content,
            "headers": {
                "X-Emergency-Digest": "true",
                "X-Reason": "pipeline-stalled"
            }
        }
        
        response = requests.post(
            "https://api.resend.com/emails",
            headers={
                "Authorization": f"Bearer {resend_key}",
                "Content-Type": "application/json"
            },
            json=payload,
            timeout=10
        )
        
        response.raise_for_status()
        result = response.json()
        
        return {
            "status": "sent",
            "email_id": result.get("id"),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        
    except Exception as e:
        return {"error": f"Email send error: {str(e)}"}

def main():
    parser = argparse.ArgumentParser(description="Generate emergency digest for user")
    parser.add_argument("--user-id", required=True, help="User ID (e.g., b419d8ad5d23513f)")
    parser.add_argument("--user-email", help="User email address (required for sending)")
    parser.add_argument("--hours", type=int, default=24, help="Hours of content to include")
    parser.add_argument("--reason", default="pipeline_stalled", help="Reason for emergency digest")
    parser.add_argument("--dry-run", action="store_true", help="Generate content but don't send")
    parser.add_argument("--format", choices=["json", "human"], default="human")
    
    args = parser.parse_args()
    
    # Fetch user drops
    print(f"🔍 Fetching drops for user {args.user_id} (last {args.hours}h)...")
    drops_data = get_user_drops(args.user_id, args.hours)
    
    if "error" in drops_data:
        if args.format == "json":
            print(json.dumps({"error": drops_data["error"]}))
        else:
            print(f"❌ Error: {drops_data['error']}")
        sys.exit(1)
    
    # Generate digest
    digest = generate_digest_content(drops_data)
    
    if "error" in digest:
        if args.format == "json":
            print(json.dumps({"error": digest["error"]}))
        else:
            print(f"❌ Error: {digest['error']}")
        sys.exit(1)
    
    result = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "user_id": args.user_id,
        "drops_found": drops_data["total"],
        "digest": digest,
        "dry_run": args.dry_run
    }
    
    # Send if email provided
    if args.user_email and not args.dry_run:
        print(f"📧 Sending digest to {args.user_email}...")
        send_result = send_emergency_digest(
            args.user_email, 
            digest["subject"], 
            digest["content"],
            args.dry_run
        )
        result["email"] = send_result
    elif args.user_email and args.dry_run:
        send_result = send_emergency_digest(
            args.user_email, 
            digest["subject"], 
            digest["content"],
            True
        )
        result["email"] = send_result
    
    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        # Human readable output
        print(f"\n🔧 EMERGENCY DIGEST GENERATION - {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"👤 User: {args.user_id}")
        print(f"📦 Drops found: {drops_data['total']} (last {args.hours}h)")
        print(f"📄 Subject: {digest['subject']}")
        
        if args.dry_run:
            print(f"🧪 DRY RUN - No email sent")
        elif args.user_email:
            if "email" in result and "error" not in result["email"]:
                print(f"✅ Email sent to {args.user_email}")
                if "email_id" in result["email"]:
                    print(f"📬 Email ID: {result['email']['email_id']}")
            elif "email" in result:
                print(f"❌ Email failed: {result['email'].get('error', 'Unknown error')}")
        else:
            print(f"📧 No email address provided - digest generated only")
        
        print(f"\n📝 Content preview:")
        preview = digest["content"][:300].replace("<", "&lt;").replace(">", "&gt;")
        print(f"   {preview}...")
        
        if not args.dry_run and args.user_email:
            print(f"\n💾 Audit trail:")
            print(f"   Reason: {args.reason}")
            print(f"   Generated: {result['timestamp']}")

if __name__ == "__main__":
    main()