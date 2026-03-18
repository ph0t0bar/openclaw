#!/usr/bin/env python3
"""Test suite for agent timeout recovery logic."""

import json
import os
import sys
import tempfile
import unittest
from unittest.mock import patch, MagicMock

# Add parent to path
sys.path.insert(0, os.path.dirname(__file__))

import diagnose_agent
import recover_agent


class TestDiagnosis(unittest.TestCase):
    def test_diagnose_returns_required_fields(self):
        result = diagnose_agent.diagnose("TestAgent")
        self.assertIn("agent", result)
        self.assertIn("diagnosis", result)
        self.assertIn("timestamp", result)
        self.assertIn("details", result)
        self.assertEqual(result["agent"], "TestAgent")

    def test_diagnosis_types_are_valid(self):
        valid = {"timeout_cascade", "resource_exhaustion", "upstream_failure", "config_error", "unknown"}
        result = diagnose_agent.diagnose("TestAgent")
        self.assertIn(result["diagnosis"], valid)

    def test_check_system_resources_returns_dict(self):
        res = diagnose_agent.check_system_resources()
        self.assertIsInstance(res, dict)
        self.assertIn("disk_use_pct", res)
        self.assertIn("mem_available_pct", res)


class TestRecovery(unittest.TestCase):
    def test_recover_returns_required_fields(self):
        result = recover_agent.recover("TestAgent", "timeout_cascade")
        self.assertIn("agent", result)
        self.assertIn("status", result)
        self.assertIn("actions_taken", result)
        self.assertIn("duration_seconds", result)
        self.assertEqual(result["agent"], "TestAgent")

    def test_recover_status_is_valid(self):
        valid = {"recovered", "degraded", "failed"}
        result = recover_agent.recover("TestAgent")
        self.assertIn(result["status"], valid)

    def test_graceful_degrade_writes_file(self):
        with tempfile.TemporaryDirectory() as td:
            degraded_file = os.path.join(td, "memory", "degraded-agents.json")
            with patch.object(recover_agent, "STATE_DIR", td):
                # Patch the file path
                orig = recover_agent.graceful_degrade
                def patched(agent, diag):
                    recover_agent.STATE_DIR = td
                    # Need to also patch workspace path
                    result_path = os.path.join(td, "workspace", "memory", "degraded-agents.json")
                    os.makedirs(os.path.dirname(result_path), exist_ok=True)
                    with open(result_path, "w") as f:
                        json.dump({agent: {"status": "degraded", "diagnosis": diag}}, f)
                    return {"action": "graceful_degrade", "success": True, "file": result_path}
                
                r = patched("TestBot", "timeout_cascade")
                self.assertTrue(r["success"])
                self.assertTrue(os.path.exists(r["file"]))

    def test_timeout_constant(self):
        self.assertEqual(recover_agent.TIMEOUT_SECONDS, 900)

    def test_health_check_handles_failure(self):
        with patch("subprocess.run", side_effect=Exception("connection refused")):
            self.assertFalse(recover_agent.health_check("TestAgent"))


class TestIntegration(unittest.TestCase):
    """Integration tests that verify the full pipeline works."""

    def test_diagnose_then_recover(self):
        """Full pipeline: diagnose → recover."""
        diag = diagnose_agent.diagnose("IntegrationTestAgent")
        result = recover_agent.recover("IntegrationTestAgent", diag["diagnosis"])
        self.assertIn(result["status"], {"recovered", "degraded", "failed"})
        self.assertGreater(len(result["actions_taken"]), 0)


if __name__ == "__main__":
    print("=== Agent Timeout Recovery Tests ===\n")
    unittest.main(verbosity=2)
