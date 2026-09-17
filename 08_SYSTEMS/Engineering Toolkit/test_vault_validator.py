"""Focused regression tests for Vault Validator validation-debt baselines."""
from __future__ import annotations
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
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

    def test_cli_gates_new_errors_without_hiding_inherited_debt(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            root = base / "vault"
            root.mkdir()
            (root / "old.md").write_text("Legacy note without metadata.")
            _, issues = validator.validate(root, False)
            baseline = base / "baseline.json"
            validator.write_baseline(baseline, issues)
            report = base / "report.md"
            args = ["--vault", str(root), "--output", str(report), "--force",
                    "--baseline", str(baseline), "--fail-on", "error"]
            with redirect_stdout(StringIO()) as output:
                self.assertEqual(validator.main(args), 0)
            self.assertIn("New issues: 0 critical, 0 errors", output.getvalue())
            self.assertIn("old.md", report.read_text())
            (root / "new.md").write_text("A new note without metadata.")
            with redirect_stdout(StringIO()) as output:
                self.assertEqual(validator.main(args), 1)
            self.assertIn("New issues: 0 critical, 1 errors", output.getvalue())
            self.assertIn("new.md", report.read_text())


class WikiLinkCodeTests(unittest.TestCase):
    def test_code_examples_do_not_hide_real_broken_links(self):
        cases = [
            "`[[example]]` [[missing]]",
            "``[[example]] `nested` `` [[missing]]",
            "`line one\n[[example]]` [[missing]]",
            "```md\n[[example]]\n```\n[[missing]]",
            "`[[missing]]",  # An unclosed delimiter is ordinary text.
            "``[[missing]]`",  # Different delimiter lengths do not form a span.
        ]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for source in cases:
                with self.subTest(source=source):
                    (root / "source.md").write_text(source)
                    issues = validator.validate_links(root, validator.load_notes(root, False))
                    broken = [i.message for i in issues if i.check == "broken_wiki_link"]
                    self.assertEqual(broken, ["Missing wiki link target: [[missing]]"])

    def test_code_examples_do_not_create_backlinks(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "source.md").write_text("`[[target]]`")
            (root / "target.md").write_text("Target")
            issues = validator.validate_links(root, validator.load_notes(root, False))
            self.assertTrue(any(i.check == "missing_backlinks" and i.path == "target.md"
                                for i in issues))
            (root / "source.md").write_text("[[target]]")
            issues = validator.validate_links(root, validator.load_notes(root, False))
            self.assertFalse(any(i.check == "missing_backlinks" and i.path == "target.md"
                                 for i in issues))


if __name__ == "__main__":
    unittest.main()
