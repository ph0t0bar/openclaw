#!/usr/bin/env python3
"""
Test suite for Poe Balance Guardian
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.check_balance import calculate_runway


def test_calculate_runway():
    """Test runway calculations."""
    # Test healthy status
    result = calculate_runway(150000, 30000)
    assert result["status"] == "healthy", f"Expected healthy, got {result['status']}"
    assert result["burn_rate_per_hour"] == 5000.0
    print("✅ Healthy status test passed")
    
    # Test caution status
    result = calculate_runway(75000, 30000)
    assert result["status"] == "caution", f"Expected caution, got {result['status']}"
    print("✅ Caution status test passed")
    
    # Test warning status
    result = calculate_runway(35000, 30000)
    assert result["status"] == "warning", f"Expected warning, got {result['status']}"
    print("✅ Warning status test passed")
    
    # Test critical status
    result = calculate_runway(15000, 30000)
    assert result["status"] == "critical", f"Expected critical, got {result['status']}"
    print("✅ Critical status test passed")
    
    # Test emergency status
    result = calculate_runway(5000, 30000)
    assert result["status"] == "emergency", f"Expected emergency, got {result['status']}"
    print("✅ Emergency status test passed")
    
    # Test zero usage
    result = calculate_runway(100000, 0)
    assert result["status"] == "unknown"
    assert result["hours_remaining"] == float('inf')
    print("✅ Zero usage test passed")
    
    print("\n🎉 All tests passed!")


if __name__ == "__main__":
    test_calculate_runway()
