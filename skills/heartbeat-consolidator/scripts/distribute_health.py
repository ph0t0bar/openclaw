#!/usr/bin/env python3
"""
Intelligent distribution of cached health metrics to agents.
Filters metrics by agent needs and prevents duplicate alerts.
"""

import json
import os
import sys
from typing import Dict, Any, List, Optional

class HealthDistributor:
    def __init__(self):
        self.cache_file = '/root/.openclaw/workspace/skills/heartbeat-consolidator/data/health_cache.json'
        self.config_file = '/root/.openclaw/workspace/skills/heartbeat-consolidator/config/heartbeat.json'
        self.agent_state_file = '/root/.openclaw/workspace/skills/heartbeat-consolidator/data/agent_state.json'
        
        # Ensure data directory exists
        os.makedirs(os.path.dirname(self.agent_state_file), exist_ok=True)

    def load_config(self) -> Dict[str, Any]:
        """Load configuration with agent filter definitions."""
        default_config = {
            'agent_filters': {
                'chief-of-staff': {
                    'metrics': ['digest_pipeline', 'family_users', 'ci_status', 'poe_balance'],
                    'alert_keywords': ['critical', 'failed', 'family'],
                    'format': 'status_summary'
                },
                'ops-monitor': {
                    'metrics': ['da_users', 'bha_users', 'poe_balance', 'stripe', 'errors'],
                    'alert_keywords': ['degraded', 'error'],
                    'format': 'metrics_table'
                },
                'user-health': {
                    'metrics': ['da_users', 'family_users', 'digest_pipeline'],
                    'alert_keywords': ['family', 'engagement'],
                    'format': 'user_focus'
                },
                'patrol': {
                    'metrics': ['da_users', 'bha_users', 'poe_balance', 'errors'],
                    'alert_keywords': ['critical', 'down'],
                    'format': 'alert_focus'
                }
            }
        }
        
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                # Merge with defaults
                default_config.update(config)
                return default_config
        
        return default_config

    def load_health_data(self) -> Optional[Dict[str, Any]]:
        """Load cached health data."""
        if not os.path.exists(self.cache_file):
            return None
            
        try:
            with open(self.cache_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return None

    def load_agent_state(self) -> Dict[str, Any]:
        """Load agent state for change tracking."""
        if os.path.exists(self.agent_state_file):
            try:
                with open(self.agent_state_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        return {}

    def save_agent_state(self, state: Dict[str, Any]) -> None:
        """Save agent state for change tracking."""
        with open(self.agent_state_file, 'w') as f:
            json.dump(state, f, indent=2)

    def filter_metrics_for_agent(self, agent_name: str, health_data: Dict[str, Any]) -> Dict[str, Any]:
        """Filter health data for specific agent needs."""
        config = self.load_config()
        agent_config = config['agent_filters'].get(agent_name, {})
        
        if not agent_config:
            # Return basic metrics for unknown agents
            return {
                'timestamp': health_data['timestamp'],
                'status': 'filtered',
                'da_users': health_data['da_users'],
                'poe_balance': health_data['poe_balance']
            }
        
        # Filter by agent's metric interests
        filtered_data = {
            'timestamp': health_data['timestamp'],
            'collection_time': health_data['collection_time'],
            'agent': agent_name,
            'filtered_for': agent_config['metrics']
        }
        
        for metric_key in agent_config['metrics']:
            if metric_key in health_data:
                filtered_data[metric_key] = health_data[metric_key]
        
        # Include changes if any affect this agent's metrics
        if 'changes' in health_data:
            agent_changes = {}
            for change_key, change_data in health_data['changes'].items():
                # Check if this change affects agent's metrics
                for metric_key in agent_config['metrics']:
                    if metric_key in change_key or change_key in metric_key:
                        agent_changes[change_key] = change_data
            
            if agent_changes:
                filtered_data['changes'] = agent_changes
        
        return filtered_data

    def format_for_agent(self, agent_name: str, filtered_data: Dict[str, Any]) -> str:
        """Format filtered data according to agent preferences."""
        config = self.load_config()
        agent_config = config['agent_filters'].get(agent_name, {})
        format_type = agent_config.get('format', 'json')
        
        if format_type == 'status_summary':
            return self.format_status_summary(filtered_data)
        elif format_type == 'metrics_table':
            return self.format_metrics_table(filtered_data)
        elif format_type == 'user_focus':
            return self.format_user_focus(filtered_data)
        elif format_type == 'alert_focus':
            return self.format_alert_focus(filtered_data)
        else:
            return json.dumps(filtered_data, indent=2)

    def format_status_summary(self, data: Dict[str, Any]) -> str:
        """Format as status summary (Chief of Staff style)."""
        lines = [f"🔄 Health Check — {data['timestamp'][:16]} UTC"]
        
        # Digest pipeline status
        if 'digest_pipeline' in data:
            dp = data['digest_pipeline']
            status_emoji = {'healthy': '✅', 'degraded': '🟡', 'critical': '🔴'}.get(dp['status'], '❓')
            lines.append(f"{status_emoji} DIGEST PIPELINE: {dp['digests_sent_24h']}/{dp['total_users']} sent ({dp['delivery_rate']:.1%})")
        
        # Family users
        if 'family_users' in data:
            fu = data['family_users']
            if fu['at_risk_count'] > 0:
                lines.append(f"🔴 FAMILY AT RISK: {fu['at_risk_count']}/3 members")
            else:
                lines.append(f"✅ FAMILY: {fu['family_count']} members healthy")
        
        # Poe balance
        if 'poe_balance' in data:
            pb = data['poe_balance']
            status_emoji = {'healthy': '✅', 'warning': '🟡', 'critical': '🔴'}.get(pb['status'], '❓')
            lines.append(f"{status_emoji} POE: {pb['balance']:,} points ({pb['runway_hours']:.1f}h runway)")
        
        # Changes
        if 'changes' in data and data['changes']:
            lines.append("📊 CHANGES:")
            for key, value in data['changes'].items():
                lines.append(f"  • {key}: {value}")
        
        return '\n'.join(lines)

    def format_metrics_table(self, data: Dict[str, Any]) -> str:
        """Format as metrics table (Ops Monitor style)."""
        lines = [f"📊 System Metrics — {data['timestamp'][:16]} UTC"]
        
        # DA metrics
        if 'da_users' in data:
            da = data['da_users']
            lines.append(f"**DropAnywhere:** {da['total_users']} users / {da['active_24h']} active / {da['drops_24h']} drops (24h)")
        
        # BHA metrics  
        if 'bha_users' in data:
            bha = data['bha_users']
            lines.append(f"**BHA:** {bha['total_users']} users / {bha['active_7d']} active (7d) / {bha['new_24h']} new (24h)")
        
        # Poe
        if 'poe_balance' in data:
            pb = data['poe_balance']
            lines.append(f"**Poe:** {pb['balance']:,} balance / {pb['burn_6h']:,} burn (6h)")
        
        # Stripe
        if 'stripe' in data:
            st = data['stripe']
            lines.append(f"**Stripe:** {st['succeeded_4h']} succeeded / {st['failed_4h']} failed / ${st['revenue_4h']:.2f} revenue (4h)")
        
        # Errors
        if 'errors' in data:
            er = data['errors']
            if er['errors_24h'] > 0:
                lines.append(f"**Errors:** {er['errors_24h']} (24h)")
        
        return '\n'.join(lines)

    def format_user_focus(self, data: Dict[str, Any]) -> str:
        """Format with user focus (UserHealth style)."""
        lines = [f"👥 User Health — {data['timestamp'][:16]} UTC"]
        
        if 'da_users' in data:
            da = data['da_users']
            lines.append(f"**Total Users:** {da['total_users']} ({da['premium_users']} premium)")
            lines.append(f"**Active:** {da['active_24h']} (24h) | {da['active_7d']} (7d)")
        
        if 'family_users' in data:
            fu = data['family_users']
            if fu['at_risk_count'] > 0:
                lines.append(f"🚨 **FAMILY AT RISK:** {fu['at_risk_count']}/3 members")
                if fu['engagement_issues']:
                    lines.append(f"  • Issues: {', '.join(fu['engagement_issues'])}")
        
        if 'digest_pipeline' in data:
            dp = data['digest_pipeline']
            lines.append(f"**Digest Delivery:** {dp['digests_sent_24h']}/{dp['total_users']} ({dp['delivery_rate']:.1%})")
        
        return '\n'.join(lines)

    def format_alert_focus(self, data: Dict[str, Any]) -> str:
        """Format with alert focus (Patrol style)."""
        alerts = []
        
        # Check for critical conditions
        if 'digest_pipeline' in data and data['digest_pipeline']['status'] == 'critical':
            alerts.append(f"🔴 DIGEST CRITICAL: {data['digest_pipeline']['delivery_rate']:.1%} delivery rate")
        
        if 'poe_balance' in data and data['poe_balance']['status'] == 'critical':
            alerts.append(f"🔴 POE CRITICAL: {data['poe_balance']['balance']:,} points remaining")
        
        if 'family_users' in data and data['family_users']['at_risk_count'] > 0:
            alerts.append(f"🔴 FAMILY RISK: {data['family_users']['at_risk_count']} members at risk")
        
        if 'errors' in data and data['errors']['errors_24h'] > 50:
            alerts.append(f"🟡 HIGH ERRORS: {data['errors']['errors_24h']} in 24h")
        
        if alerts:
            return f"🚨 ALERTS — {data['timestamp'][:16]} UTC\n" + '\n'.join(alerts)
        else:
            return f"✅ ALL CLEAR — {data['timestamp'][:16]} UTC"

    def get_changes_only(self, agent_name: str) -> Optional[Dict[str, Any]]:
        """Get only metrics that changed since agent's last check."""
        health_data = self.load_health_data()
        if not health_data:
            return None
            
        agent_state = self.load_agent_state()
        agent_last_check = agent_state.get(agent_name, {}).get('last_check', 0)
        
        if health_data['collection_time'] <= agent_last_check:
            return None  # No new data
        
        # Filter for this agent
        filtered_data = self.filter_metrics_for_agent(agent_name, health_data)
        
        # Update agent state
        agent_state[agent_name] = {
            'last_check': health_data['collection_time'],
            'last_data': filtered_data
        }
        self.save_agent_state(agent_state)
        
        return filtered_data

    def distribute(self, agent_name: str, changes_only: bool = False, format_output: bool = True) -> Optional[str]:
        """Main distribution method."""
        if changes_only:
            filtered_data = self.get_changes_only(agent_name)
        else:
            health_data = self.load_health_data()
            if not health_data:
                return None
            filtered_data = self.filter_metrics_for_agent(agent_name, health_data)
        
        if not filtered_data:
            return None
            
        if format_output:
            return self.format_for_agent(agent_name, filtered_data)
        else:
            return json.dumps(filtered_data, indent=2)


def main():
    """CLI interface for health distribution."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Distribute health metrics to agents')
    parser.add_argument('--agent', required=True, help='Agent name (chief-of-staff, ops-monitor, etc.)')
    parser.add_argument('--changes-only', action='store_true', help='Return only changed metrics')
    parser.add_argument('--raw-json', action='store_true', help='Output raw JSON instead of formatted')
    parser.add_argument('--list-metrics', action='store_true', help='List available metrics')
    
    args = parser.parse_args()
    
    distributor = HealthDistributor()
    
    if args.list_metrics:
        health_data = distributor.load_health_data()
        if health_data:
            print("Available metrics:")
            for key in sorted(health_data.keys()):
                if key not in ['timestamp', 'collection_time']:
                    print(f"  - {key}")
        else:
            print("No cached health data available. Run collect_health.py first.")
        return
    
    try:
        result = distributor.distribute(
            agent_name=args.agent,
            changes_only=args.changes_only,
            format_output=not args.raw_json
        )
        
        if result:
            print(result)
        else:
            if args.changes_only:
                print(f"No new changes for {args.agent}")
            else:
                print(f"No health data available for {args.agent}")
    
    except Exception as e:
        print(f"❌ Distribution failed: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()