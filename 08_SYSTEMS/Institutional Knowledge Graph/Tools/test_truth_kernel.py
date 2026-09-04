#!/usr/bin/env python3
"""Tests for the read-only Alpha Proxima Truth Kernel."""

from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import truth_kernel


NOTE = """---
title: "{title}"
aliases: [{aliases}]
tags: [alpha-proxima]
created: 2026-09-03
updated: 2026-09-03
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: {artifact_type}
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: Implementation
reasoning_engine: CODEX
dependencies: [{dependencies}]
related_documents: []
related_research_programs: []
{identity}
---

# {title}

{body}
"""


def write_note(root: Path, relative: str, *, title: str | None = None,
               artifact_type: str = "engineering-standard", identity: str = "",
               aliases: str = "", dependencies: str = "", body: str = "Content.") -> Path:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(NOTE.format(
        title=title or path.stem, artifact_type=artifact_type, identity=identity,
        aliases=aliases, dependencies=dependencies, body=body,
    ), encoding="utf-8")
    return path


def digest_tree(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*.md"))
    }


class TestNodeIdentity(unittest.TestCase):
    def test_explicit_taxonomy_identity_is_used(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_note(root, "08_SYSTEMS/Standard.md", identity="standard_id: ES-99")
            node = truth_kernel.node_registry.build_nodes(root)[0]
        self.assertEqual(node["node_id"], "apkg:standard:es-99")
        self.assertEqual(node["identity_stability"], "stable")

    def test_title_fallback_survives_a_file_move(self):
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            write_note(Path(first), "08_SYSTEMS/Old/Stable.md", title="Stable Identity")
            write_note(Path(second), "08_SYSTEMS/New/Stable.md", title="Stable Identity")
            before = truth_kernel.node_registry.build_nodes(Path(first))[0]
            after = truth_kernel.node_registry.build_nodes(Path(second))[0]
        self.assertEqual(before["node_id"], after["node_id"])
        self.assertEqual(before["identity_stability"], "provisional")

    def test_collisions_are_unique_and_visible(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_note(root, "08_SYSTEMS/A.md", title="Same")
            write_note(root, "08_SYSTEMS/B.md", title="Same")
            nodes = truth_kernel.node_registry.build_nodes(root)
        self.assertEqual(len({node["node_id"] for node in nodes}), 2)
        self.assertTrue(all(node["identity_stability"] == "collision_bound" for node in nodes))
        self.assertTrue(all(any(item["code"] == "identity_collision" for item in node["validation_findings"]) for node in nodes))


class TestSafetyAndValidation(unittest.TestCase):
    def test_local_omi_scaffolding_is_excluded(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_note(root, "08_SYSTEMS/Canonical.md", title="Canonical")
            write_note(root, "Omi/Local.md", title="Local")
            contract = truth_kernel.build(root)
        self.assertEqual(contract["counts"]["nodes"], 1)

    def test_missing_and_malformed_frontmatter_are_findings(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "Loose.md").write_text("# Loose\n\nContent.\n", encoding="utf-8")
            (root / "Broken.md").write_text("---\ntitle: Broken\nnot yaml\n---\n\n# Broken\n", encoding="utf-8")
            contract = truth_kernel.build(root)
        codes = {item["code"] for item in contract["validation"]["findings"]}
        self.assertIn("missing_frontmatter", codes)
        self.assertIn("malformed_frontmatter", codes)

    def test_unreadable_scan_failure_is_not_hidden(self):
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.object(
                truth_kernel.node_registry.vault_validator,
                "load_notes",
                side_effect=PermissionError("denied"),
            ):
                with self.assertRaises(PermissionError):
                    truth_kernel.node_registry.build_nodes(Path(tmp))

    def test_generation_never_changes_source_notes(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as out:
            root = Path(tmp)
            write_note(root, "08_SYSTEMS/A.md", title="A", dependencies='"[[B]]"')
            write_note(root, "08_SYSTEMS/B.md", title="B")
            before = digest_tree(root)
            result = truth_kernel.main(["--vault", str(root), "--output-dir", out, "--force"])
            after = digest_tree(root)
        self.assertEqual(result, 0)
        self.assertEqual(before, after)


class TestRelationships(unittest.TestCase):
    def test_ambiguous_alias_is_preserved_not_guessed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_note(root, "08_SYSTEMS/A.md", title="A", aliases='"Shared"')
            write_note(root, "08_SYSTEMS/B.md", title="B", aliases='"Shared"')
            write_note(root, "08_SYSTEMS/C.md", title="C", dependencies='"[[Shared]]"')
            contract = truth_kernel.build(root)
        ambiguous = [rel for rel in contract["unresolved_relationships"] if rel["target_raw"] == "[[Shared]]"]
        self.assertEqual(len(ambiguous), 1)
        self.assertEqual(ambiguous[0]["resolution_status"], "ambiguous")
        self.assertEqual(len(ambiguous[0]["candidate_node_ids"]), 2)


class TestContract(unittest.TestCase):
    def test_empty_vault_is_a_ready_empty_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            contract = truth_kernel.build(Path(tmp))
        self.assertEqual(contract["counts"]["nodes"], 0)
        self.assertEqual(contract["health"]["status"], "ready")

    def test_missing_vault_fails_explicitly(self):
        with self.assertRaises(FileNotFoundError):
            truth_kernel.build(Path("/nonexistent/alpha-proxima-vault"))

    def test_machine_contract_is_reproducible(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_note(root, "08_SYSTEMS/A.md", title="A", dependencies='"[[B]]"')
            write_note(root, "08_SYSTEMS/B.md", title="B")
            first = truth_kernel.build(root)
            second = truth_kernel.build(root)
        self.assertEqual(first, second)
        self.assertEqual(first["schema_version"], "1.0.0")
        self.assertEqual(first["mode"], "read_only")
        self.assertEqual(first["counts"]["nodes"], 2)
        self.assertEqual(first["counts"]["relationships"], 1)
        json.dumps(first)


if __name__ == "__main__":
    unittest.main(verbosity=2)
