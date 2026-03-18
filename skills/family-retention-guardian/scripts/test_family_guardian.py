#!/usr/bin/env python3
"""
Test suite for Family Retention Guardian
"""

import json
import os
import sys
import unittest
from unittest.mock import patch, Mock
from datetime import datetime, timedelta

# Add the scripts directory to the path so we can import the main module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_family_health import FamilyRetentionGuardian

class TestFamilyRetentionGuardian(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment"""
        # Mock environment variable
        os.environ['HUB_API_KEY'] = 'test-key-123'
        self.guardian = FamilyRetentionGuardian()
    
    def tearDown(self):
        """Clean up after tests"""
        if 'HUB_API_KEY' in os.environ:
            del os.environ['HUB_API_KEY']
    
    def test_initialization_without_api_key(self):
        """Test that initialization fails without API key"""
        if 'HUB_API_KEY' in os.environ:
            del os.environ['HUB_API_KEY']
        if 'INGEST_API_KEY' in os.environ:
            del os.environ['INGEST_API_KEY']
            
        with self.assertRaises(ValueError):
            FamilyRetentionGuardian()
    
    def test_family_emails_loaded(self):
        """Test that family emails are properly loaded"""
        expected_emails = {
            'lhamer228@gmail.com',
            'rhamersunsetpartners@gmail.com', 
            'hamer.daniel@gmail.com',
            'mitch.p.hamer@gmail.com'
        }
        self.assertEqual(set(self.guardian.family_emails.keys()), expected_emails)
    
    def test_engagement_score_calculation(self):
        """Test engagement score calculation algorithm"""
        
        # Test case 1: Healthy user - recent activity, good vault, many drops
        user_data = {
            'last_drop': (datetime.now() - timedelta(days=1)).isoformat() + 'Z',
            'vault_count': 15,
            'total_drops': 20
        }
        score, risk_level = self.guardian.calculate_engagement_score(user_data)
        self.assertGreaterEqual(score, 80)
        self.assertEqual(risk_level, 'healthy')
        
        # Test case 2: At-risk user - moderate inactivity
        user_data = {
            'last_drop': (datetime.now() - timedelta(days=10)).isoformat() + 'Z',
            'vault_count': 5,
            'total_drops': 8
        }
        score, risk_level = self.guardian.calculate_engagement_score(user_data)
        self.assertLess(score, 60)
        self.assertIn(risk_level, ['at_risk', 'critical'])
        
        # Test case 3: Emergency user - no activity
        user_data = {
            'last_drop': None,
            'vault_count': 0,
            'total_drops': 0
        }
        score, risk_level = self.guardian.calculate_engagement_score(user_data)
        self.assertEqual(score, 0)
        self.assertEqual(risk_level, 'emergency')
    
    def test_last_activity_formatting(self):
        """Test human-readable last activity formatting"""
        
        # Test today
        today = datetime.now().isoformat() + 'Z'
        result = self.guardian.format_last_activity(today)
        self.assertEqual(result, 'Today')
        
        # Test yesterday  
        yesterday = (datetime.now() - timedelta(days=1)).isoformat() + 'Z'
        result = self.guardian.format_last_activity(yesterday)
        self.assertEqual(result, 'Yesterday')
        
        # Test several days ago
        week_ago = (datetime.now() - timedelta(days=7)).isoformat() + 'Z'
        result = self.guardian.format_last_activity(week_ago)
        self.assertEqual(result, '7 days ago')
        
        # Test never
        result = self.guardian.format_last_activity('')
        self.assertEqual(result, 'Never')
    
    @patch('check_family_health.requests.get')
    def test_get_user_activity_success(self, mock_get):
        """Test successful user activity retrieval"""
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = [
            {
                'email': 'lhamer228@gmail.com',
                'last_drop': '2026-03-17T10:00:00Z',
                'vault_count': 10,
                'total_drops': 15
            }
        ]
        mock_get.return_value = mock_response
        
        result = self.guardian.get_user_activity('lhamer228@gmail.com')
        self.assertIsNotNone(result)
        self.assertEqual(result['email'], 'lhamer228@gmail.com')
    
    @patch('check_family_health.requests.get')
    def test_get_user_activity_not_found(self, mock_get):
        """Test user not found case"""
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = []  # Empty user list
        mock_get.return_value = mock_response
        
        result = self.guardian.get_user_activity('unknown@example.com')
        self.assertIsNone(result)
    
    @patch.object(FamilyRetentionGuardian, 'get_user_activity')
    def test_check_family_member_healthy(self, mock_get_activity):
        """Test checking a healthy family member"""
        mock_get_activity.return_value = {
            'email': 'lhamer228@gmail.com',
            'last_drop': datetime.now().isoformat() + 'Z',
            'vault_count': 12,
            'total_drops': 25
        }
        
        result = self.guardian.check_family_member('lhamer228@gmail.com')
        self.assertEqual(result['email'], 'lhamer228@gmail.com')
        self.assertEqual(result['name'], 'Lisa Hamer')
        self.assertEqual(result['risk_level'], 'healthy')
        self.assertFalse(result['needs_action'])
    
    @patch.object(FamilyRetentionGuardian, 'get_user_activity')  
    def test_check_family_member_at_risk(self, mock_get_activity):
        """Test checking an at-risk family member"""
        mock_get_activity.return_value = {
            'email': 'hamer.daniel@gmail.com',
            'last_drop': (datetime.now() - timedelta(days=15)).isoformat() + 'Z',
            'vault_count': 2,
            'total_drops': 3
        }
        
        result = self.guardian.check_family_member('hamer.daniel@gmail.com')
        self.assertEqual(result['email'], 'hamer.daniel@gmail.com')
        self.assertEqual(result['name'], 'Daniel Hamer')
        self.assertIn(result['risk_level'], ['critical', 'emergency'])
        self.assertTrue(result['needs_action'])
        self.assertIn(result['action_type'], ['direct_outreach', 'emergency_alert'])
    
    @patch.object(FamilyRetentionGuardian, 'get_user_activity')
    def test_check_family_member_not_found(self, mock_get_activity):
        """Test checking a family member not found in system"""
        mock_get_activity.return_value = None
        
        result = self.guardian.check_family_member('lhamer228@gmail.com')
        self.assertEqual(result['status'], 'not_found')
        self.assertEqual(result['risk_level'], 'emergency')
        self.assertTrue(result['needs_action'])
        self.assertEqual(result['action_type'], 'manual_investigation')
    
    @patch.object(FamilyRetentionGuardian, 'check_family_member')
    def test_check_all_family(self, mock_check_member):
        """Test checking all family members"""
        # Mock responses for each family member
        mock_check_member.side_effect = [
            {'email': 'lhamer228@gmail.com', 'risk_level': 'healthy', 'needs_action': False},
            {'email': 'rhamersunsetpartners@gmail.com', 'risk_level': 'critical', 'needs_action': True},
            {'email': 'hamer.daniel@gmail.com', 'risk_level': 'emergency', 'needs_action': True},
            {'email': 'mitch.p.hamer@gmail.com', 'risk_level': 'watch', 'needs_action': False}
        ]
        
        results = self.guardian.check_all_family()
        self.assertEqual(len(results), 4)
        
        # Check that we called check_family_member for each family email
        self.assertEqual(mock_check_member.call_count, 4)
    
    def test_format_report_text(self):
        """Test text report formatting"""
        test_results = [
            {
                'email': 'lhamer228@gmail.com',
                'name': 'Lisa Hamer',
                'score': 85,
                'risk_level': 'healthy',
                'last_activity': 'Yesterday',
                'vault_count': 12,
                'total_drops': 25,
                'needs_action': False,
                'action_type': None
            },
            {
                'email': 'hamer.daniel@gmail.com', 
                'name': 'Daniel Hamer',
                'score': 15,
                'risk_level': 'emergency',
                'last_activity': 'Never',
                'vault_count': 0,
                'total_drops': 0,
                'needs_action': True,
                'action_type': 'emergency_alert'
            }
        ]
        
        report = self.guardian.format_report(test_results, 'text')
        self.assertIn('FAMILY RETENTION GUARDIAN REPORT', report)
        self.assertIn('Lisa Hamer', report)
        self.assertIn('Daniel Hamer', report)
        self.assertIn('emergency_alert', report)
    
    def test_format_report_json(self):
        """Test JSON report formatting"""
        test_results = [
            {
                'email': 'test@example.com',
                'score': 50,
                'risk_level': 'at_risk'
            }
        ]
        
        report = self.guardian.format_report(test_results, 'json')
        parsed = json.loads(report)
        self.assertEqual(len(parsed), 1)
        self.assertEqual(parsed[0]['email'], 'test@example.com')

class TestIntegration(unittest.TestCase):
    """Integration tests (require real API key)"""
    
    def setUp(self):
        """Only run if real API key is available"""
        self.api_key = os.getenv('HUB_API_KEY') or os.getenv('INGEST_API_KEY')
        if not self.api_key:
            self.skipTest("No real API key available for integration tests")
        
        self.guardian = FamilyRetentionGuardian()
    
    def test_real_api_connection(self):
        """Test actual connection to Hub API (if API key available)"""
        try:
            # Try to get user activity for a known family member
            result = self.guardian.get_user_activity('lhamer228@gmail.com')
            # Should either return data or None, not raise an exception
            self.assertIsInstance(result, (dict, type(None)))
        except Exception as e:
            self.fail(f"Real API connection failed: {e}")

def run_tests():
    """Run the test suite and return results"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestFamilyRetentionGuardian))
    
    # Add integration tests only if API key is available  
    if os.getenv('HUB_API_KEY') or os.getenv('INGEST_API_KEY'):
        suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
        print("🔗 Including integration tests (API key found)")
    else:
        print("⚠️  Skipping integration tests (no API key)")
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return True if all tests passed
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)