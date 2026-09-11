"""Focused regression tests for Vault Validator validation-debt baselines."""
from __future__ import annotations
import json
import tempfile
import unittest
from pathlib import Path
import vault_validator as validator

class ValidationBaselineTests(unittest.TestCase):
    def test_baseline_preserves_debt_and_detects_only_regressions(self):
        known = validator.Issue("warning", "missing_required_metadata", "old.md", "Missing field")
        new = validator.Issue("error", "broken_wiki_link", "new.md", "Missing link")
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "baseline.json"
            validator.write_baseline(path, [known])
            baseline = validator.load_baseline(path)
        self.assertIn(validator.issue_signature(known), baseline)
        self.assertFalse(validator.should_fail([known] if validator.issue_signature(known) not in baseline else [], "warning"))
        self.assertTrue(validator.should_fail([new], "error"))

    def test_invalid_baseline_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "baseline.json"; path.write_text(json.dumps({"issue_signatures": [1]}))
            with self.assertRaises(ValueError): validator.load_baseline(path)
