#!/usr/bin/env python3
"""
Test suite for Family Retention Guardian

Tests the family monitoring and re-engagement logic.
"""

import unittest
import sys
import os
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock

# Add the scripts directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the module under test
import check_family

class TestFamilyRetentionGuardian(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_users = [
            {
                "email": "lhamer228@gmail.com",
                "user_id": "920d4d339900efd5",
                "last_drop": "2026-03-04T00:00:00Z",
                "vault_count": 5,
                "digest_enabled": True
            },
            {
                "email": "rhamersunsetpartners@gmail.com", 
                "user_id": "abc123",
                "last_drop": "2026-03-07T00:00:00Z",
                "vault_count": 3,
                "digest_enabled": True
            },
            {
                "email": "hamer.daniel@gmail.com",
                "user_id": "def456", 
                "last_drop": None,
                "vault_count": 0,
                "digest_enabled": True
            },
            {
                "email": "notfamily@example.com",
                "user_id": "xyz789",
                "last_drop": "2026-03-17T00:00:00Z",
                "vault_count": 10,
                "digest_enabled": True
            }
        ]
    
    def test_identify_family_members(self):
        """Test family member identification."""
        family = check_family.identify_family_members(self.mock_users)
        
        # Should find 3 family members
        self.assertEqual(len(family), 3)
        
        # Should include all Hamer family emails
        family_emails = [user["email"] for user in family]
        self.assertIn("lhamer228@gmail.com", family_emails)
        self.assertIn("rhamersunsetpartners@gmail.com", family_emails) 
        self.assertIn("hamer.daniel@gmail.com", family_emails)
        
        # Should not include non-family
        self.assertNotIn("notfamily@example.com", family_emails)
    
    def test_calculate_engagement_score(self):
        """Test engagement score calculation."""
        # Test user with recent activity
        recent_user = {
            "last_drop": "2026-03-17T00:00:00Z",
            "vault_count": 10
        }
        score = check_family.calculate_engagement_score(recent_user)
        self.assertGreater(score, 80)  # Should be high score
        
        # Test user with old activity
        old_user = {
            "last_drop": "2026-03-01T00:00:00Z",
            "vault_count": 2
        }
        score = check_family.calculate_engagement_score(old_user)
        self.assertLess(score, 50)  # Should be lower score
        
        # Test user with no activity
        inactive_user = {
            "last_drop": None,
            "vault_count": 0
        }
        score = check_family.calculate_engagement_score(inactive_user)
        self.assertEqual(score, 0)  # Should be zero
    
    def test_assess_risk_level(self):
        """Test risk level assessment."""
        # Test healthy user
        healthy_user = {
            "last_drop": datetime.now().isoformat() + "Z"
        }
        risk = check_family.assess_risk_level(healthy_user, 90)
        self.assertEqual(risk, "HEALTHY")
        
        # Test at-risk user  
        at_risk_user = {
            "last_drop": (datetime.now() - timedelta(days=10)).isoformat() + "Z"
        }
        risk = check_family.assess_risk_level(at_risk_user, 40)
        self.assertIn(risk, ["AT_RISK", "HEALTHY"])  # Could be either based on exact timing
        
        # Test critical user
        critical_user = {
            "last_drop": (datetime.now() - timedelta(days=35)).isoformat() + "Z"
        }
        risk = check_family.assess_risk_level(critical_user, 20)
        self.assertEqual(risk, "CRITICAL")
        
        # Test abandoned user
        abandoned_user = {
            "last_drop": None
        }
        risk = check_family.assess_risk_level(abandoned_user, 0)
        self.assertEqual(risk, "ABANDONED")
    
    def test_create_reengagement_task(self):
        """Test re-engagement task creation."""
        test_user = {
            "email": "test@example.com",
            "user_id": "test123"
        }
        
        # Test healthy user (should not create task)
        task = check_family.create_reengagement_task(test_user, "HEALTHY")
        self.assertIsNone(task)
        
        # Test at-risk user (should create task)
        task = check_family.create_reengagement_task(test_user, "AT_RISK")
        self.assertIsNotNone(task)
        self.assertEqual(task["type"], "family_reengagement")
        self.assertEqual(task["target_email"], "test@example.com")
        self.assertEqual(task["risk_level"], "AT_RISK")
        self.assertIn("drops", task["suggested_message"].lower())
        
        # Test critical user
        task = check_family.create_reengagement_task(test_user, "CRITICAL")
        self.assertIsNotNone(task)
        self.assertEqual(task["priority"], "high")
    
    @patch('check_family.requests.get')
    def test_get_user_data_success(self, mock_get):
        """Test successful user data fetch."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.mock_users
        mock_get.return_value = mock_response
        
        result = check_family.get_user_data()
        self.assertEqual(result, self.mock_users)
    
    @patch('check_family.requests.get') 
    def test_get_user_data_failure(self, mock_get):
        """Test failed user data fetch."""
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_get.return_value = mock_response
        
        result = check_family.get_user_data()
        self.assertEqual(result, [])
    
    def test_family_patterns(self):
        """Test that family patterns are correctly defined."""
        patterns = check_family.FAMILY_PATTERNS
        
        # Should include known family emails
        self.assertIn("lhamer228@gmail.com", patterns)
        self.assertIn("rhamersunsetpartners@gmail.com", patterns)
        self.assertIn("hamer.daniel@gmail.com", patterns)
    
    def test_risk_thresholds(self):
        """Test that risk thresholds are reasonable."""
        thresholds = check_family.RISK_THRESHOLDS
        
        # Should have all risk levels
        self.assertIn("HEALTHY", thresholds)
        self.assertIn("AT_RISK", thresholds)
        self.assertIn("CRITICAL", thresholds)
        self.assertIn("ABANDONED", thresholds)
        
        # Thresholds should be progressive
        self.assertLess(thresholds["HEALTHY"]["days"], thresholds["AT_RISK"]["days"])
        self.assertLess(thresholds["AT_RISK"]["days"], thresholds["CRITICAL"]["days"])
        self.assertLess(thresholds["CRITICAL"]["days"], thresholds["ABANDONED"]["days"])

def run_tests():
    """Run all tests and return results."""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFamilyRetentionGuardian)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Summary
    total_tests = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    passed = total_tests - failures - errors
    
    print(f"\n{'='*50}")
    print(f"FAMILY GUARDIAN TEST SUMMARY")
    print(f"{'='*50}")
    print(f"✅ Passed: {passed}/{total_tests}")
    print(f"❌ Failed: {failures}")
    print(f"💥 Errors: {errors}")
    
    if failures > 0 or errors > 0:
        print(f"\n❌ TESTS FAILED - Fix issues before deploying")
        return False
    else:
        print(f"\n✅ ALL TESTS PASSED - Skill ready to deploy")
        return True

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)