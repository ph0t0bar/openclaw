#!/usr/bin/env python3
"""
Simple test for Family Retention Guardian core functionality
Tests the engagement scoring and formatting functions without requiring external APIs
"""

import sys
import os
from datetime import datetime, timedelta

# Add the scripts directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that we can import the main module"""
    try:
        from check_family_health import FamilyRetentionGuardian
        print("✅ Import successful")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def test_scoring_algorithm():
    """Test the engagement scoring algorithm"""
    try:
        # Mock the API key for testing
        os.environ['HUB_API_KEY'] = 'test-key'
        from check_family_health import FamilyRetentionGuardian
        
        guardian = FamilyRetentionGuardian()
        
        # Test Case 1: Healthy user
        user_data = {
            'last_drop': datetime.now().isoformat() + 'Z',
            'vault_count': 15,
            'total_drops': 20
        }
        score, risk_level = guardian.calculate_engagement_score(user_data)
        assert score >= 70, f"Expected high score for healthy user, got {score}"
        assert risk_level in ['healthy', 'watch'], f"Expected healthy/watch level, got {risk_level}"
        print(f"✅ Healthy user test: {score}/100 ({risk_level})")
        
        # Test Case 2: At-risk user
        user_data = {
            'last_drop': (datetime.now() - timedelta(days=10)).isoformat() + 'Z',
            'vault_count': 3,
            'total_drops': 5
        }
        score, risk_level = guardian.calculate_engagement_score(user_data)
        assert score < 60, f"Expected lower score for at-risk user, got {score}"
        print(f"✅ At-risk user test: {score}/100 ({risk_level})")
        
        # Test Case 3: Emergency user
        user_data = {
            'last_drop': None,
            'vault_count': 0,
            'total_drops': 0
        }
        score, risk_level = guardian.calculate_engagement_score(user_data)
        assert score == 0, f"Expected 0 score for emergency user, got {score}"
        assert risk_level == 'emergency', f"Expected emergency level, got {risk_level}"
        print(f"✅ Emergency user test: {score}/100 ({risk_level})")
        
        return True
    except Exception as e:
        print(f"❌ Scoring test failed: {e}")
        return False

def test_activity_formatting():
    """Test last activity formatting"""
    try:
        os.environ['HUB_API_KEY'] = 'test-key'
        from check_family_health import FamilyRetentionGuardian
        
        guardian = FamilyRetentionGuardian()
        
        # Test today
        today = datetime.now().isoformat() + 'Z'
        result = guardian.format_last_activity(today)
        assert result == 'Today', f"Expected 'Today', got '{result}'"
        print("✅ Today formatting test")
        
        # Test yesterday
        yesterday = (datetime.now() - timedelta(days=1)).isoformat() + 'Z'
        result = guardian.format_last_activity(yesterday)
        assert result == 'Yesterday', f"Expected 'Yesterday', got '{result}'"
        print("✅ Yesterday formatting test")
        
        # Test several days ago
        week_ago = (datetime.now() - timedelta(days=7)).isoformat() + 'Z'
        result = guardian.format_last_activity(week_ago)
        assert result == '7 days ago', f"Expected '7 days ago', got '{result}'"
        print("✅ Days ago formatting test")
        
        # Test never
        result = guardian.format_last_activity('')
        assert result == 'Never', f"Expected 'Never', got '{result}'"
        print("✅ Never formatting test")
        
        return True
    except Exception as e:
        print(f"❌ Formatting test failed: {e}")
        return False

def test_family_emails():
    """Test that family emails are loaded correctly"""
    try:
        os.environ['HUB_API_KEY'] = 'test-key'
        from check_family_health import FamilyRetentionGuardian
        
        guardian = FamilyRetentionGuardian()
        
        expected_emails = {
            'lhamer228@gmail.com',
            'rhamersunsetpartners@gmail.com',
            'hamer.daniel@gmail.com',
            'mitch.p.hamer@gmail.com'
        }
        
        actual_emails = set(guardian.family_emails.keys())
        assert actual_emails == expected_emails, f"Family emails mismatch. Expected {expected_emails}, got {actual_emails}"
        
        print(f"✅ Family emails loaded: {len(actual_emails)} members")
        for email, name in guardian.family_emails.items():
            print(f"   - {name} ({email})")
        
        return True
    except Exception as e:
        print(f"❌ Family emails test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=== Family Retention Guardian - Simple Tests ===\n")
    
    tests = [
        ("Import Test", test_imports),
        ("Family Emails Test", test_family_emails),
        ("Scoring Algorithm Test", test_scoring_algorithm),
        ("Activity Formatting Test", test_activity_formatting),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"Running {test_name}...")
        if test_func():
            passed += 1
        print()
    
    print(f"=== Test Results: {passed}/{total} passed ===")
    
    if passed == total:
        print("🎉 All tests passed! Skill is ready for use.")
        return 0
    else:
        print("❌ Some tests failed. Check the output above.")
        return 1

if __name__ == '__main__':
    sys.exit(main())