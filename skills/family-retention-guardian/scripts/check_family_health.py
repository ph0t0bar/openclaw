#!/usr/bin/env python3
"""
Family Retention Guardian - Core health checking script
Monitors family member engagement in DropAnywhere and triggers re-engagement as needed.
"""

import json
import os
import sys
import urllib.request
import urllib.parse
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import argparse

class FamilyRetentionGuardian:
    def __init__(self):
        self.hub_api_key = os.getenv('HUB_API_KEY') or os.getenv('INGEST_API_KEY')
        self.hub_url = 'https://hub-production-f423.up.railway.app'
        self.family_emails = {
            'lhamer228@gmail.com': 'Lisa Hamer',
            'rhamersunsetpartners@gmail.com': 'Ryan Hamer', 
            'hamer.daniel@gmail.com': 'Daniel Hamer',
            'mitch.p.hamer@gmail.com': 'Mitch Hamer'
        }
        
        if not self.hub_api_key:
            raise ValueError("HUB_API_KEY or INGEST_API_KEY must be set in environment")
    
    def get_user_activity(self, email: str) -> Optional[Dict]:
        """Get user activity data from Hub API"""
        try:
            url = f'{self.hub_url}/api/admin/users'
            req = urllib.request.Request(url)
            req.add_header('X-API-Key', self.hub_api_key)
            req.add_header('Content-Type', 'application/json')
            
            with urllib.request.urlopen(req, timeout=30) as response:
                if response.getcode() != 200:
                    print(f"ERROR: Hub API returned {response.getcode()}")
                    return None
                
                data = response.read().decode('utf-8')
                users = json.loads(data)
                
                for user in users:
                    if user.get('email', '').lower() == email.lower():
                        return user
                return None
        except Exception as e:
            print(f"ERROR: Failed to get user data for {email}: {e}")
            return None
    
    def calculate_engagement_score(self, user_data: Dict) -> Tuple[int, str]:
        """Calculate engagement score (0-100) and risk level"""
        if not user_data:
            return 0, "emergency"
        
        # Get key metrics
        last_drop_str = user_data.get('last_drop', '')
        vault_count = user_data.get('vault_count', 0)
        total_drops = user_data.get('total_drops', 0)
        
        score = 0
        
        # Recency Score (50% weight)
        if last_drop_str:
            try:
                last_drop = datetime.fromisoformat(last_drop_str.replace('Z', '+00:00'))
                days_ago = (datetime.now() - last_drop.replace(tzinfo=None)).days
                
                if days_ago == 0:
                    score += 50
                elif days_ago <= 3:
                    score += 40
                elif days_ago <= 7:
                    score += 25
                elif days_ago <= 14:
                    score += 10
                # 0 points for >14 days
            except:
                pass  # No recency points if date parsing fails
        
        # Frequency Score (30% weight) - approximate drops per week
        if total_drops > 0:
            # Rough estimate based on total drops (could be improved with date range)
            weekly_drops = total_drops / 4  # Assume 4 weeks of activity
            if weekly_drops >= 5:
                score += 30
            elif weekly_drops >= 3:
                score += 20
            elif weekly_drops >= 1:
                score += 10
            # 0 points for < 1 drop per week
        
        # Depth Score (20% weight) - vault engagement
        if vault_count >= 10:
            score += 20
        elif vault_count >= 5:
            score += 15
        elif vault_count >= 1:
            score += 10
        # 0 points for empty vault
        
        # Determine risk level
        if score >= 80:
            risk_level = "healthy"
        elif score >= 60:
            risk_level = "watch"
        elif score >= 40:
            risk_level = "at_risk"
        elif score >= 20:
            risk_level = "critical"
        else:
            risk_level = "emergency"
        
        return score, risk_level
    
    def format_last_activity(self, last_drop_str: str) -> str:
        """Format last activity time in human-readable format"""
        if not last_drop_str:
            return "Never"
        
        try:
            last_drop = datetime.fromisoformat(last_drop_str.replace('Z', '+00:00'))
            days_ago = (datetime.now() - last_drop.replace(tzinfo=None)).days
            
            if days_ago == 0:
                return "Today"
            elif days_ago == 1:
                return "Yesterday"
            else:
                return f"{days_ago} days ago"
        except:
            return "Unknown"
    
    def check_family_member(self, email: str) -> Dict:
        """Check engagement status for a single family member"""
        name = self.family_emails.get(email, email)
        user_data = self.get_user_activity(email)
        
        if not user_data:
            return {
                'email': email,
                'name': name,
                'status': 'not_found',
                'score': 0,
                'risk_level': 'emergency',
                'last_activity': 'Never',
                'vault_count': 0,
                'total_drops': 0,
                'needs_action': True,
                'action_type': 'manual_investigation'
            }
        
        score, risk_level = self.calculate_engagement_score(user_data)
        last_activity = self.format_last_activity(user_data.get('last_drop', ''))
        vault_count = user_data.get('vault_count', 0)
        total_drops = user_data.get('total_drops', 0)
        
        # Determine if action needed
        needs_action = risk_level in ['at_risk', 'critical', 'emergency']
        action_type = None
        if risk_level == 'at_risk':
            action_type = 'gentle_nudge'
        elif risk_level == 'critical':
            action_type = 'direct_outreach'
        elif risk_level == 'emergency':
            action_type = 'emergency_alert'
        
        return {
            'email': email,
            'name': name,
            'status': 'active' if user_data else 'inactive',
            'score': score,
            'risk_level': risk_level,
            'last_activity': last_activity,
            'vault_count': vault_count,
            'total_drops': total_drops,
            'needs_action': needs_action,
            'action_type': action_type
        }
    
    def check_all_family(self) -> List[Dict]:
        """Check engagement status for all family members"""
        results = []
        for email in self.family_emails:
            result = self.check_family_member(email)
            results.append(result)
        return results
    
    def format_report(self, results: List[Dict], format_type: str = 'text') -> str:
        """Format family engagement report"""
        if format_type == 'json':
            return json.dumps(results, indent=2)
        
        # Text format
        report = []
        report.append("=== FAMILY RETENTION GUARDIAN REPORT ===")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
        report.append("")
        
        # Summary
        at_risk = sum(1 for r in results if r['needs_action'])
        healthy = len(results) - at_risk
        report.append(f"SUMMARY: {healthy} healthy, {at_risk} need attention")
        report.append("")
        
        # Individual status
        emoji_map = {
            'healthy': '🟢',
            'watch': '🟡', 
            'at_risk': '🟠',
            'critical': '🔴',
            'emergency': '🚨'
        }
        
        for result in sorted(results, key=lambda x: x['score']):
            emoji = emoji_map.get(result['risk_level'], '❓')
            report.append(f"{emoji} {result['name']} ({result['email']})")
            report.append(f"   Score: {result['score']}/100 ({result['risk_level'].upper()})")
            report.append(f"   Last Activity: {result['last_activity']}")
            report.append(f"   Vault: {result['vault_count']} items | Total Drops: {result['total_drops']}")
            
            if result['needs_action']:
                report.append(f"   ⚡ ACTION: {result['action_type'].replace('_', ' ').title()}")
            report.append("")
        
        return "\\n".join(report)

def main():
    parser = argparse.ArgumentParser(description='Check family member engagement health')
    parser.add_argument('--email', help='Check specific family member by email')
    parser.add_argument('--all', action='store_true', help='Check all family members')
    parser.add_argument('--format', choices=['text', 'json'], default='text', help='Output format')
    parser.add_argument('--action', action='store_true', help='Take action based on risk levels (not implemented)')
    
    args = parser.parse_args()
    
    if not args.email and not args.all:
        parser.print_help()
        return
    
    try:
        guardian = FamilyRetentionGuardian()
        
        if args.email:
            if args.email not in guardian.family_emails:
                print(f"ERROR: {args.email} is not a known family member")
                print(f"Known family emails: {list(guardian.family_emails.keys())}")
                return
            
            result = guardian.check_family_member(args.email)
            results = [result]
        else:
            results = guardian.check_all_family()
        
        report = guardian.format_report(results, args.format)
        print(report)
        
        # Return appropriate exit code
        any_critical = any(r['risk_level'] in ['critical', 'emergency'] for r in results)
        sys.exit(2 if any_critical else 0)
        
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()