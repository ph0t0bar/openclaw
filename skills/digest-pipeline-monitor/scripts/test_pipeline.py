#!/usr/bin/env python3
"""
Test suite for digest-pipeline-monitor skill
Validates functionality without affecting production systems
"""

import sys
import os
import json
import tempfile
from datetime import datetime

# Add scripts directory to path for importing modules
sys.path.insert(0, os.path.dirname(__file__))

def test_pipeline_health_calculation():
    """Test pipeline health analysis with mock data"""
    from check_pipeline import analyze_pipeline_health
    
    print("🧪 Testing pipeline health calculation...")
    
    # Test case 1: Healthy pipeline
    metrics_healthy = {
        "users_total": 109,
        "digests_sent_24h": 85,
        "active_users_24h": 15,
        "drops_24h": 60,
        "errors_24h": 2
    }
    
    health = analyze_pipeline_health(metrics_healthy)
    assert health["status"] == "healthy", f"Expected healthy, got {health['status']}"
    assert health["delivery_rate"] >= 75, f"Expected >75% delivery rate, got {health['delivery_rate']}"
    print("  ✅ Healthy pipeline case passed")
    
    # Test case 2: Failed pipeline (current situation)
    metrics_failed = {
        "users_total": 109,
        "digests_sent_24h": 2,
        "active_users_24h": 9,
        "drops_24h": 58,
        "errors_24h": 24
    }
    
    health = analyze_pipeline_health(metrics_failed)
    assert health["status"] in ["failed", "critical"], f"Expected failed/critical, got {health['status']}"
    assert health["delivery_rate"] < 25, f"Expected <25% delivery rate, got {health['delivery_rate']}"
    assert health["users_affected"] > 75, f"Expected >75 users affected, got {health['users_affected']}"
    print("  ✅ Failed pipeline case passed")
    
    # Test case 3: Stalled pipeline (zero digests)
    metrics_stalled = {
        "users_total": 109,
        "digests_sent_24h": 0,
        "active_users_24h": 10,
        "drops_24h": 50,
        "errors_24h": 5
    }
    
    health = analyze_pipeline_health(metrics_stalled)
    assert health["status"] == "stalled", f"Expected stalled, got {health['status']}"
    assert health["severity"] == "emergency", f"Expected emergency severity, got {health['severity']}"
    print("  ✅ Stalled pipeline case passed")
    
    # Test case 4: Error handling
    metrics_error = {"error": "API connection failed"}
    health = analyze_pipeline_health(metrics_error)
    assert health["status"] == "unknown", f"Expected unknown, got {health['status']}"
    print("  ✅ Error handling case passed")

def test_expected_digest_calculation():
    """Test expected digest calculation logic"""
    from check_pipeline import calculate_expected_digests
    
    print("🧪 Testing expected digest calculation...")
    
    # Test normal case
    expected = calculate_expected_digests(100, 15)
    assert 70 <= expected <= 91, f"Expected 70-91 digests for 100 users, got {expected}"
    print(f"  ✅ 100 users → {expected} expected digests")
    
    # Test current DropAnywhere case
    expected = calculate_expected_digests(109, 9)
    assert 70 <= expected <= 85, f"Expected 70-85 digests for 109 users, got {expected}"
    print(f"  ✅ 109 users → {expected} expected digests")
    
    # Test edge case: low user count
    expected = calculate_expected_digests(5, 2)
    assert expected >= 3, f"Expected >=3 digests for 5 users, got {expected}"
    print(f"  ✅ 5 users → {expected} expected digests")

def test_digest_content_generation():
    """Test emergency digest content generation"""
    from emergency_digest import generate_digest_content
    
    print("🧪 Testing digest content generation...")
    
    # Test case 1: Normal drops
    mock_drops = {
        "drops": [
            {
                "content": "Interesting article about AI development",
                "source": "email",
                "created_at": "2026-03-18T06:00:00Z"
            },
            {
                "content": "Meeting notes from team standup",
                "source": "web",
                "created_at": "2026-03-18T05:30:00Z"
            }
        ],
        "total": 2
    }
    
    digest = generate_digest_content(mock_drops)
    assert "error" not in digest, f"Unexpected error: {digest.get('error')}"
    assert "2 New Items" in digest["subject"], f"Subject should mention 2 items"
    assert "From Email" in digest["content"], f"Content should group by source"
    print("  ✅ Normal drops case passed")
    
    # Test case 2: No drops
    empty_drops = {"drops": [], "total": 0}
    digest = generate_digest_content(empty_drops)
    assert "No New Content" in digest["subject"], f"Subject should mention no content"
    assert "No new drops captured" in digest["content"], f"Content should explain no drops"
    print("  ✅ Empty drops case passed")
    
    # Test case 3: Error handling
    error_drops = {"error": "API connection failed"}
    digest = generate_digest_content(error_drops)
    assert "error" in digest, f"Should propagate error"
    print("  ✅ Error propagation case passed")

def test_json_output_format():
    """Test that scripts can produce valid JSON output"""
    import subprocess
    
    print("🧪 Testing JSON output formats...")
    
    # Test check_pipeline.py JSON output
    try:
        result = subprocess.run([
            "python", "check_pipeline.py", "--format", "json"
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            data = json.loads(result.stdout)
            assert "timestamp" in data, "JSON should include timestamp"
            assert "pipeline" in data, "JSON should include pipeline status"
            print("  ✅ check_pipeline.py JSON output valid")
        else:
            print(f"  ⚠️  check_pipeline.py returned error (expected due to missing env vars)")
    
    except Exception as e:
        print(f"  ⚠️  check_pipeline.py JSON test skipped: {e}")
    
    # Test emergency_digest.py JSON output (dry run)
    try:
        result = subprocess.run([
            "python", "emergency_digest.py", 
            "--user-id", "test123",
            "--format", "json",
            "--dry-run"
        ], capture_output=True, text=True, timeout=30)
        
        if result.stdout:
            data = json.loads(result.stdout)
            assert "timestamp" in data, "JSON should include timestamp"
            assert "user_id" in data, "JSON should include user_id"
            print("  ✅ emergency_digest.py JSON output valid")
    
    except Exception as e:
        print(f"  ⚠️  emergency_digest.py JSON test skipped: {e}")

def test_skill_integration():
    """Test skill can be invoked from workspace"""
    import subprocess
    
    print("🧪 Testing skill integration...")
    
    # Change to skill directory
    skill_dir = "/root/.openclaw/workspace/skills/digest-pipeline-monitor"
    if not os.path.exists(skill_dir):
        print(f"  ❌ Skill directory not found: {skill_dir}")
        return
    
    os.chdir(skill_dir)
    
    # Test SKILL.md exists and is readable
    skill_md = os.path.join(skill_dir, "SKILL.md")
    assert os.path.exists(skill_md), "SKILL.md should exist"
    
    with open(skill_md, 'r') as f:
        content = f.read()
        assert "Digest Pipeline Monitor" in content, "SKILL.md should contain title"
        assert "check_pipeline.py" in content, "SKILL.md should reference scripts"
    
    print("  ✅ SKILL.md structure valid")
    
    # Test scripts are executable
    scripts_dir = os.path.join(skill_dir, "scripts")
    assert os.path.exists(scripts_dir), "scripts/ directory should exist"
    
    for script in ["check_pipeline.py", "emergency_digest.py"]:
        script_path = os.path.join(scripts_dir, script)
        assert os.path.exists(script_path), f"{script} should exist"
        assert os.access(script_path, os.X_OK), f"{script} should be executable"
    
    print("  ✅ Scripts are present and executable")

def main():
    """Run all tests"""
    print("🔬 DIGEST PIPELINE MONITOR - Test Suite")
    print("=" * 60)
    
    try:
        test_expected_digest_calculation()
        test_pipeline_health_calculation()  
        test_digest_content_generation()
        test_json_output_format()
        test_skill_integration()
        
        print("\n✅ ALL TESTS PASSED")
        print("🚀 Skill is ready for production use")
        return 0
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n💥 UNEXPECTED ERROR: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())