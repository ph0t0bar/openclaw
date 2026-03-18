#!/usr/bin/env python3
"""
Master health collector for heartbeat consolidation.
Fetches all system metrics and caches results to prevent agent API overlap.
"""

import json
import os
import sys
import time
import requests
from datetime import datetime, timezone
from typing import Dict, Any, Optional

# Add workspace to Python path for shared utilities
sys.path.insert(0, '/root/.openclaw/workspace')

class HealthCollector:
    def __init__(self):
        self.hub_api_key = os.getenv('HUB_API_KEY')
        self.hub_url = 'https://hub-production-f423.up.railway.app'
        self.cache_file = '/root/.openclaw/workspace/skills/heartbeat-consolidator/data/health_cache.json'
        self.config_file = '/root/.openclaw/workspace/skills/heartbeat-consolidator/config/heartbeat.json'
        self.cache_ttl = 1800  # 30 minutes
        
        # Ensure data directory exists
        os.makedirs(os.path.dirname(self.cache_file), exist_ok=True)
        
    def load_config(self) -> Dict[str, Any]:
        """Load configuration settings."""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {
            'cache_ttl_seconds': 1800,
            'emergency_override_keywords': ['critical', 'down', 'failed', 'error'],
            'agent_filters': {
                'chief-of-staff': ['digest_pipeline', 'family_users', 'ci_status'],
                'ops-monitor': ['da_users', 'bha_users', 'poe_balance', 'stripe'],
                'user-health': ['active_users', 'engagement', 'family_members']
            }
        }

    def is_cache_valid(self) -> bool:
        """Check if cached data is still valid."""
        if not os.path.exists(self.cache_file):
            return False
            
        stat = os.stat(self.cache_file)
        cache_age = time.time() - stat.st_mtime
        return cache_age < self.cache_ttl

    def load_cached_data(self) -> Optional[Dict[str, Any]]:
        """Load cached health data if valid."""
        if not self.is_cache_valid():
            return None
            
        try:
            with open(self.cache_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return None

    def fetch_hub_dashboard(self) -> Dict[str, Any]:
        """Fetch Hub dashboard metrics."""
        if not self.hub_api_key:
            return {'error': 'HUB_API_KEY not found'}
            
        try:
            headers = {'X-API-Key': self.hub_api_key}
            response = requests.get(f'{self.hub_url}/api/ops/dashboard', 
                                 headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {'error': f'Hub API error: {str(e)}'}

    def collect_all_metrics(self) -> Dict[str, Any]:
        """Collect all system health metrics."""
        timestamp = datetime.now(timezone.utc).isoformat()
        
        # Start with Hub dashboard (primary source)
        hub_data = self.fetch_hub_dashboard()
        
        # Structure the consolidated metrics
        metrics = {
            'timestamp': timestamp,
            'collection_time': time.time(),
            'hub_dashboard': hub_data,
            'digest_pipeline': self.extract_digest_metrics(hub_data),
            'da_users': self.extract_da_metrics(hub_data),
            'bha_users': self.extract_bha_metrics(hub_data),
            'poe_balance': self.extract_poe_metrics(hub_data),
            'errors': self.extract_error_metrics(hub_data),
            'family_users': self.extract_family_metrics(hub_data),
            'ci_status': self.check_ci_status(),
            'stripe': self.extract_stripe_metrics(hub_data)
        }
        
        return metrics

    def extract_digest_metrics(self, hub_data: Dict) -> Dict[str, Any]:
        """Extract digest pipeline metrics from hub data."""
        if 'error' in hub_data:
            return {'status': 'unknown', 'error': hub_data['error']}
            
        # Extract digest-specific metrics
        digests_sent = hub_data.get('digests_sent_24h', 0)
        total_users = hub_data.get('total_users', 0)
        digest_attempts = hub_data.get('digest_attempts', 0)
        
        # Calculate health status
        if total_users > 0:
            delivery_rate = digests_sent / total_users
            if delivery_rate < 0.1:  # <10% delivery rate
                status = 'critical'
            elif delivery_rate < 0.5:  # <50% delivery rate
                status = 'degraded'
            else:
                status = 'healthy'
        else:
            status = 'unknown'
            
        return {
            'status': status,
            'digests_sent_24h': digests_sent,
            'digest_attempts': digest_attempts,
            'total_users': total_users,
            'delivery_rate': delivery_rate if total_users > 0 else 0
        }

    def extract_da_metrics(self, hub_data: Dict) -> Dict[str, Any]:
        """Extract DropAnywhere user metrics."""
        return {
            'total_users': hub_data.get('da_total_users', 0),
            'active_24h': hub_data.get('da_active_24h', 0),
            'active_7d': hub_data.get('da_active_7d', 0),
            'total_drops': hub_data.get('da_total_drops', 0),
            'drops_24h': hub_data.get('da_drops_24h', 0),
            'premium_users': hub_data.get('da_premium_users', 0)
        }

    def extract_bha_metrics(self, hub_data: Dict) -> Dict[str, Any]:
        """Extract BrutallyHonest.ai metrics."""
        return {
            'total_users': hub_data.get('bha_total_users', 0),
            'active_7d': hub_data.get('bha_active_7d', 0),
            'new_24h': hub_data.get('bha_new_24h', 0),
            'pro_users': hub_data.get('bha_pro_users', 0)
        }

    def extract_poe_metrics(self, hub_data: Dict) -> Dict[str, Any]:
        """Extract Poe balance and usage metrics."""
        balance = hub_data.get('poe_balance', 0)
        burn_6h = hub_data.get('poe_burn_6h', 0)
        
        # Calculate runway in hours
        runway_hours = (balance / (burn_6h / 6)) if burn_6h > 0 else float('inf')
        
        # Determine status
        if balance < 50000:  # <50K points
            status = 'critical'
        elif balance < 200000:  # <200K points
            status = 'warning'
        else:
            status = 'healthy'
            
        return {
            'balance': balance,
            'burn_6h': burn_6h,
            'runway_hours': runway_hours,
            'status': status
        }

    def extract_error_metrics(self, hub_data: Dict) -> Dict[str, Any]:
        """Extract error metrics."""
        return {
            'errors_24h': hub_data.get('errors_24h', 0),
            'last_error_hour': hub_data.get('last_error_hour'),
            'error_rate': hub_data.get('error_rate', 0)
        }

    def extract_family_metrics(self, hub_data: Dict) -> Dict[str, Any]:
        """Extract family member specific metrics."""
        # This would be enhanced with actual family user data
        return {
            'family_count': 3,  # Known: lhamer228, rhamersunsetpartners, hamer.daniel
            'at_risk_count': 2,  # Based on recent sessions
            'engagement_issues': ['lhamer228', 'rhamersunsetpartners']
        }

    def extract_stripe_metrics(self, hub_data: Dict) -> Dict[str, Any]:
        """Extract Stripe payment metrics."""
        return {
            'succeeded_4h': hub_data.get('stripe_succeeded_4h', 0),
            'failed_4h': hub_data.get('stripe_failed_4h', 0),
            'revenue_4h': hub_data.get('stripe_revenue_4h', 0)
        }

    def check_ci_status(self) -> Dict[str, Any]:
        """Check CI status from GitHub (simplified)."""
        # TODO: Implement GitHub API check for CI status
        return {
            'status': 'unknown',
            'note': 'CI check not implemented yet'
        }

    def detect_changes(self, current: Dict, previous: Optional[Dict]) -> Dict[str, Any]:
        """Detect changes between current and previous metrics."""
        if not previous:
            return {'all_new': True}
            
        changes = {}
        
        # Digest pipeline changes
        if current['digest_pipeline']['status'] != previous.get('digest_pipeline', {}).get('status'):
            changes['digest_status'] = {
                'from': previous.get('digest_pipeline', {}).get('status'),
                'to': current['digest_pipeline']['status']
            }
            
        # User count changes
        da_users_change = current['da_users']['total_users'] - previous.get('da_users', {}).get('total_users', 0)
        if abs(da_users_change) > 0:
            changes['da_users'] = da_users_change
            
        # Poe status changes
        if current['poe_balance']['status'] != previous.get('poe_balance', {}).get('status'):
            changes['poe_status'] = {
                'from': previous.get('poe_balance', {}).get('status'),
                'to': current['poe_balance']['status']
            }
            
        return changes

    def save_metrics(self, metrics: Dict[str, Any]) -> None:
        """Save metrics to cache file."""
        with open(self.cache_file, 'w') as f:
            json.dump(metrics, f, indent=2)

    def run(self) -> Dict[str, Any]:
        """Main collection run."""
        # Load previous data for change detection
        previous_data = self.load_cached_data()
        
        # Collect fresh metrics
        current_data = self.collect_all_metrics()
        
        # Detect changes
        changes = self.detect_changes(current_data, previous_data)
        current_data['changes'] = changes
        
        # Save to cache
        self.save_metrics(current_data)
        
        return current_data


def main():
    """CLI interface for health collection."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Collect consolidated health metrics')
    parser.add_argument('--force', action='store_true', help='Force collection even if cache is valid')
    parser.add_argument('--json', action='store_true', help='Output JSON format')
    
    args = parser.parse_args()
    
    collector = HealthCollector()
    
    # Check if we need to collect
    if not args.force and collector.is_cache_valid():
        cached_data = collector.load_cached_data()
        if cached_data:
            if args.json:
                print(json.dumps(cached_data, indent=2))
            else:
                print(f"Using cached data from {cached_data['timestamp']}")
            return
    
    # Collect fresh data
    try:
        data = collector.run()
        if args.json:
            print(json.dumps(data, indent=2))
        else:
            print(f"✅ Health metrics collected at {data['timestamp']}")
            if data.get('changes'):
                print(f"📊 Changes detected: {list(data['changes'].keys())}")
    except Exception as e:
        print(f"❌ Collection failed: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()