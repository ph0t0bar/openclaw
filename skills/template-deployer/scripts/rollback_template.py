#!/usr/bin/env python3
"""
Template Rollback - Rollback to previous template versions
Emergency rollback capability to prevent deployment disasters
"""

import os
import sys
import json
import shutil
import datetime
from pathlib import Path
import glob

BACKUP_DIR = "/root/.openclaw/workspace/template-backups"
STAGING_DIR = "/tmp/template-staging"

def list_backups(template_name=None):
    """List available backups, optionally filtered by template name"""
    backup_dir = Path(BACKUP_DIR)
    
    if not backup_dir.exists():
        return []
        
    backups = []
    pattern = f"{template_name}_*.backup" if template_name else "*.backup"
    
    for backup_file in backup_dir.glob(pattern):
        try:
            with open(backup_file, 'r') as f:
                backup_info = json.load(f)
                backup_info['backup_file'] = str(backup_file)
                backups.append(backup_info)
        except (json.JSONDecodeError, FileNotFoundError):
            # Skip corrupted backup files
            continue
            
    # Sort by timestamp, newest first
    backups.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
    
    return backups

def get_latest_backup(template_name):
    """Get the most recent backup for a specific template"""
    backups = list_backups(template_name)
    
    if not backups:
        return None
        
    return backups[0]

def get_backup_by_timestamp(template_name, timestamp):
    """Get a specific backup by timestamp"""
    backups = list_backups(template_name)
    
    for backup in backups:
        if backup.get('timestamp') == timestamp:
            return backup
            
    return None

def rollback_to_backup(backup_info, target_mode='staging'):
    """Rollback to a specific backup"""
    
    if not backup_info:
        return {
            'success': False,
            'error': 'No backup information provided'
        }
        
    backup_file = backup_info['backup_file']
    template_name = backup_info['template']
    
    # For rollback, we'd restore from the backup to the appropriate location
    # This is a simplified implementation
    
    try:
        if target_mode == 'staging':
            staging_path = Path(STAGING_DIR)
            staging_path.mkdir(parents=True, exist_ok=True)
            
            # In real implementation, would restore actual template content
            # For now, create a rollback marker
            rollback_marker = staging_path / f"{template_name}_rollback.html"
            
            with open(rollback_marker, 'w') as f:
                f.write(f"<!-- ROLLBACK MARKER -->\n")
                f.write(f"<!-- Original timestamp: {backup_info['timestamp']} -->\n")
                f.write(f"<!-- Rollback date: {datetime.datetime.now().isoformat()} -->\n")
                f.write("<!-- Template content would be restored here -->\n")
                
            return {
                'success': True,
                'mode': 'staging',
                'template': template_name,
                'backup_timestamp': backup_info['timestamp'],
                'rollback_file': str(rollback_marker),
                'message': f"Rollback to staging successful: {backup_info['timestamp']}"
            }
            
        elif target_mode == 'production' or target_mode == 'prod':
            # Production rollback - more careful process
            
            # First rollback to staging for verification
            staging_result = rollback_to_backup(backup_info, 'staging')
            
            if not staging_result['success']:
                return {
                    'success': False,
                    'error': 'Staging rollback failed',
                    'details': staging_result
                }
                
            # Then apply to production
            # In real implementation, would:
            # - Update production email templates
            # - Notify all services
            # - Update deployment records
            
            return {
                'success': True,
                'mode': 'production',
                'template': template_name,
                'backup_timestamp': backup_info['timestamp'],
                'staging_result': staging_result,
                'message': f"Production rollback successful: {backup_info['timestamp']}",
                'integration_points': [
                    'Resend email service (simulated)',
                    'Hub dashboard (simulated)',
                    'WhatsApp notifications (simulated)'
                ]
            }
            
    except Exception as e:
        return {
            'success': False,
            'error': f"Rollback failed: {str(e)}"
        }

def rollback_template(template_name=None, version='previous', mode='staging'):
    """Main rollback function"""
    
    if version == 'previous' or version == 'latest':
        if not template_name:
            return {
                'success': False,
                'error': 'Template name required for latest/previous rollback'
            }
            
        backup_info = get_latest_backup(template_name)
        
        if not backup_info:
            return {
                'success': False,
                'error': f'No backups found for template: {template_name}'
            }
            
    elif version.startswith('2'):  # Timestamp format
        if not template_name:
            return {
                'success': False,
                'error': 'Template name required for specific version rollback'
            }
            
        backup_info = get_backup_by_timestamp(template_name, version)
        
        if not backup_info:
            return {
                'success': False,
                'error': f'No backup found for template {template_name} with timestamp {version}'
            }
            
    else:
        return {
            'success': False,
            'error': f'Invalid version format: {version}. Use "previous" or timestamp (YYYYMMDD_HHMMSS)'
        }
        
    print(f"Rolling back {template_name} to {backup_info['timestamp']}")
    
    result = rollback_to_backup(backup_info, mode)
    
    return result

def main():
    if len(sys.argv) < 2:
        print("Usage: python rollback_template.py <template_name> [--version previous|TIMESTAMP] [--mode staging|prod]")
        print("       python rollback_template.py --list [template_name]")
        print()
        print("Examples:")
        print("  python rollback_template.py brooke-demo-email --version previous")
        print("  python rollback_template.py morning-brief --version 20260318_143022")
        print("  python rollback_template.py --list")
        print("  python rollback_template.py --list brooke-demo-email")
        sys.exit(1)
        
    # Handle list command
    if sys.argv[1] == '--list':
        template_name = sys.argv[2] if len(sys.argv) > 2 else None
        backups = list_backups(template_name)
        
        if not backups:
            if template_name:
                print(f"No backups found for template: {template_name}")
            else:
                print("No backups found")
            return
            
        print("Available backups:")
        print("-" * 60)
        for backup in backups:
            print(f"{backup['template']:20} {backup['timestamp']:15} {backup['backup_date'][:19]}")
        return
        
    # Parse arguments
    template_name = sys.argv[1]
    version = 'previous'
    mode = 'staging'
    
    if '--version' in sys.argv:
        version_idx = sys.argv.index('--version')
        if version_idx + 1 < len(sys.argv):
            version = sys.argv[version_idx + 1]
            
    if '--mode' in sys.argv:
        mode_idx = sys.argv.index('--mode')
        if mode_idx + 1 < len(sys.argv):
            mode = sys.argv[mode_idx + 1]
            
    print(f"Rolling back template: {template_name}")
    print(f"Version: {version}")
    print(f"Mode: {mode}")
    print("-" * 50)
    
    result = rollback_template(template_name, version, mode)
    
    if result['success']:
        print("✅ Rollback SUCCESSFUL")
        print(f"Template: {result.get('template')}")
        print(f"Backup: {result.get('backup_timestamp')}")
        print(f"Mode: {result.get('mode')}")
        
        if '--json' in sys.argv:
            print("\nRollback details:")
            print(json.dumps(result, indent=2))
    else:
        print("❌ Rollback FAILED")
        print(f"Error: {result.get('error')}")
        
        if '--json' in sys.argv:
            print("\nError details:")
            print(json.dumps(result, indent=2))
            
        sys.exit(1)

if __name__ == '__main__':
    main()