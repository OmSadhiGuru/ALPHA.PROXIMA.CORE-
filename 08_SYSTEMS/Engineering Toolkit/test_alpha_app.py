#!/usr/bin/env python3
"""Tests for the Alpha Proxima App.

Run: python3 "08_SYSTEMS/Engineering Toolkit/test_alpha_app.py"
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import alpha_app as app  # noqa: E402
import founder_os as fos  # noqa: E402


NOTE = """---
title: "{title}"
tags: [{tags}]
status: {status}
version: "1.0.0"
artifact_type: {artifact_type}
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: Governance
reasoning_engine: Claude
authors: ["CLAUDE"]
updated: 2026-09-01
dependencies: []
related_documents: [{related}]
---

# {title}

{body}
"""


def write_note(root: Path, relative: str, *, title: str | None = None,
               status: str = "active", artifact_type: str = "policy",
               tags: str = "alpha-proxima", related: str = "", body: str = "Content.") -> Path:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        NOTE.format(title=title or path.stem, tags=tags, status=status,
                    artifact_type=artifact_type, related=related, body=body),
        encoding="utf-8",
    )
    return path


def vault(tmp: str) -> Path:
    """A miniature Foundation: two connected documents and one isolated one."""
    root = Path(tmp)
    write_note(root, "00_CONSTITUTION/Book I.md", title="Book I",
               artifact_type="constitution", related='"[[Book II]]"')
    write_note(root, "00_CONSTITUTION/Book II.md", title="Book II",
               artifact_type="governance-framework", body="Refers back to [[Book I]].")
    write_note(root, "07_RESEARCH/RP-001 Index.md", title="RP-001 Index",
               artifact_type="research-index", body="No links here.")
    return root


class TestVaultIndex(unittest.TestCase):
    def test_indexes_every_note(self):
        with tempfile.TemporaryDirectory() as tmp:
            index = app.build_vault_index(vault(tmp))
        self.assertEqual(index["note_count"], 3)
        self.assertEqual({e["title"] for e in index["entries"]},
                         {"Book I", "Book II", "RP-001 Index"})

    def test_entry_carries_metadata_but_never_the_body(self):
        """The index describes a document; it must never become a copy of it."""
        with tempfile.TemporaryDirectory() as tmp:
            index = app.build_vault_index(vault(tmp))
        entry = next(e for e in index["entries"] if e["title"] == "Book I")
        self.assertEqual(entry["type"], "constitution")
        self.assertEqual(entry["status"], "active")
        self.assertEqual(entry["owner"], "Alpha Proxima Foundation")
        self.assertEqual(entry["function"], "Governance")
        self.assertNotIn("body", entry)
        self.assertNotIn("text", entry)
        for value in entry.values():
            self.assertNotIn("Content.", json.dumps(value))

    def test_domains_are_ordered_constitutionally(self):
        with tempfile.TemporaryDirectory() as tmp:
            index = app.build_vault_index(vault(tmp))
        self.assertEqual([d["id"] for d in index["domains"]],
                         ["00_CONSTITUTION", "07_RESEARCH"])

    def test_uncanonical_folders_are_flagged_not_hidden(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = vault(tmp)
            write_note(root, "OSG_LAUNCH/Plan.md", title="Plan")
            index = app.build_vault_index(root)
        loose = next(d for d in index["domains"] if d["id"] == "OSG_LAUNCH")
        self.assertIn("Not yet placed", loose["question"])

    def test_scaffolding_is_excluded(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = vault(tmp)
            write_note(root, "copilot/Prompt.md", title="Prompt")
            write_note(root, "Tags/Tag.md", title="Tag")
            index = app.build_vault_index(root)
        self.assertEqual(index["note_count"], 3)

    def test_missing_root_raises(self):
        with self.assertRaises(app.AppError):
            app.build_vault_index(Path("/nonexistent/vault"))


class TestRelationships(unittest.TestCase):
    def test_links_resolve_to_entry_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            index = app.build_vault_index(vault(tmp))
        by_title = {e["title"]: e for e in index["entries"]}
        self.assertIn(by_title["Book II"]["id"], by_title["Book I"]["links"])

    def test_frontmatter_and_body_links_both_count(self):
        """A dependency declared in YAML is as real a relationship as a wiki-link."""
        with tempfile.TemporaryDirectory() as tmp:
            index = app.build_vault_index(vault(tmp))
        by_title = {e["title"]: e for e in index["entries"]}
        self.assertIn(by_title["Book I"]["id"], by_title["Book II"]["links"])

    def test_unresolved_links_are_reported_not_dropped(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = vault(tmp)
            write_note(root, "00_CONSTITUTION/Book IV.md", title="Book IV",
                       body="Points at [[A Document That Does Not Exist]].")
            index = app.build_vault_index(root)
        entry = next(e for e in index["entries"] if e["title"] == "Book IV")
        self.assertEqual(entry["unresolved"], ["A Document That Does Not Exist"])

    def test_links_inside_code_fences_are_not_relationships(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = vault(tmp)
            write_note(root, "10_TEMPLATES/Guide.md", title="Guide",
                       body="```\n[[Book I]]\n```")
            index = app.build_vault_index(root)
        entry = next(e for e in index["entries"] if e["title"] == "Guide")
        self.assertEqual(entry["links"], [])

    def test_links_inside_inline_code_are_not_relationships(self):
        """A link quoted in backticks is documentation about links, not a link."""
        with tempfile.TemporaryDirectory() as tmp:
            root = vault(tmp)
            write_note(root, "08_SYSTEMS/Standard.md", title="Standard",
                       body="Write a wiki-link as `[[Book I]]` in your notes.")
            index = app.build_vault_index(root)
        entry = next(e for e in index["entries"] if e["title"] == "Standard")
        self.assertEqual(entry["links"], [])
        self.assertEqual(entry["unresolved"], [])

    def test_inline_code_does_not_hide_a_real_neighbouring_link(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = vault(tmp)
            write_note(root, "08_SYSTEMS/Mixed.md", title="Mixed",
                       body="Use `[[Placeholder]]` when referring to [[Book II]].")
            index = app.build_vault_index(root)
        by_title = {e["title"]: e for e in index["entries"]}
        self.assertEqual(by_title["Mixed"]["links"], [by_title["Book II"]["id"]])
        self.assertEqual(by_title["Mixed"]["unresolved"], [])

    def test_self_links_are_ignored(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = vault(tmp)
            write_note(root, "01_VISION/Vision.md", title="Vision",
                       body="See [[Vision]] itself.")
            index = app.build_vault_index(root)
        entry = next(e for e in index["entries"] if e["title"] == "Vision")
        self.assertEqual(entry["links"], [])

    def test_backlinks_are_counted(self):
        with tempfile.TemporaryDirectory() as tmp:
            index = app.build_vault_index(vault(tmp))
        by_title = {e["title"]: e for e in index["entries"]}
        self.assertEqual(by_title["Book II"]["backlinks"], 1)
        self.assertEqual(by_title["RP-001 Index"]["backlinks"], 0)


class TestCoherence(unittest.TestCase):
    """The Library Rule -- 'never create isolated information' -- as a measurement."""

    def test_isolated_documents_are_named(self):
        with tempfile.TemporaryDirectory() as tmp:
            index = app.build_vault_index(vault(tmp))
        orphans = index["coherence"]["orphans"]
        self.assertEqual([o["title"] for o in orphans], ["RP-001 Index"])

    def test_connectedness_is_a_ratio_of_connected_documents(self):
        with tempfile.TemporaryDirectory() as tmp:
            coherence = app.build_vault_index(vault(tmp))["coherence"]
        self.assertEqual(coherence["connected"], 2)
        self.assertEqual(coherence["note_count"], 3)
        self.assertAlmostEqual(coherence["connectedness"], 2 / 3, places=3)

    def test_notes_without_frontmatter_are_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = vault(tmp)
            (root / "04_DECISIONS").mkdir(parents=True)
            (root / "04_DECISIONS" / "Loose.md").write_text("# Loose\n\nNo metadata.\n")
            coherence = app.build_vault_index(root)["coherence"]
        self.assertEqual([n["title"] for n in coherence["missing_frontmatter"]], ["Loose"])

    def test_broken_links_are_reported_with_their_targets(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = vault(tmp)
            write_note(root, "05_PROPOSALS/Note.md", title="Note", body="[[Missing Thing]]")
            coherence = app.build_vault_index(root)["coherence"]
        broken = next(b for b in coherence["broken_links"] if b["title"] == "Note")
        self.assertEqual(broken["targets"], ["Missing Thing"])
        self.assertEqual(coherence["counts"]["broken_links"], 1)

    def test_a_fully_connected_vault_reports_no_defects(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_note(root, "00_CONSTITUTION/A.md", title="A", related='"[[B]]"')
            write_note(root, "00_CONSTITUTION/B.md", title="B", related='"[[A]]"')
            coherence = app.build_vault_index(root)["coherence"]
        self.assertEqual(sum(coherence["counts"].values()), 0)
        self.assertEqual(coherence["connectedness"], 1.0)


class TestAppView(unittest.TestCase):
    def test_view_composes_both_halves(self):
        with tempfile.TemporaryDirectory() as tmp:
            view = app.build_app_view(fos.empty_state(), vault(tmp))
        self.assertIn("operate", view)
        self.assertIn("know", view)
        self.assertEqual([h["id"] for h in view["halves"]], ["operate", "know"])

    def test_operate_half_is_the_founder_os_read_model(self):
        """The app must consume the existing read model, never re-derive it."""
        state = fos.empty_state()
        fos.set_mission(state, "Prove the routing lane")
        with tempfile.TemporaryDirectory() as tmp:
            view = app.build_app_view(state, vault(tmp))
        self.assertEqual(view["operate"]["mission"]["mission"], "Prove the routing lane")
        self.assertEqual(set(fos.build_view(state)), set(view["operate"]))

    def test_view_is_json_serialisable(self):
        with tempfile.TemporaryDirectory() as tmp:
            view = app.build_app_view(fos.empty_state(), vault(tmp))
        json.loads(json.dumps(view))


class TestRenderer(unittest.TestCase):
    TEMPLATE = "<html><body><script>var V=" + app.VIEW_PLACEHOLDER + ";</script></body></html>"

    def test_render_inlines_the_view(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            template = root / "app.template.html"
            template.write_text(self.TEMPLATE, encoding="utf-8")
            view = app.build_app_view(fos.empty_state(), vault(tmp))
            html = app.render_app(view, template)
        self.assertNotIn(app.VIEW_PLACEHOLDER, html)
        self.assertIn('"app_version"', html)

    def test_render_escapes_closing_script_tags(self):
        """A note titled with a closing tag must not be able to break out of the script."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_note(root, "00_CONSTITUTION/X.md", title="</script><b>injected")
            template = root / "app.template.html"
            template.write_text(self.TEMPLATE, encoding="utf-8")
            html = app.render_app(app.build_app_view(fos.empty_state(), root), template)
        self.assertNotIn("</script><b>injected", html)
        self.assertIn("<\\/script>", html)

    def test_missing_template_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            view = app.build_app_view(fos.empty_state(), vault(tmp))
            with self.assertRaises(app.AppError):
                app.render_app(view, Path(tmp) / "absent.html")

    def test_template_without_placeholder_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            template = root / "bad.html"
            template.write_text("<html></html>", encoding="utf-8")
            view = app.build_app_view(fos.empty_state(), vault(tmp))
            with self.assertRaises(app.AppError):
                app.render_app(view, template)

    def test_write_outputs_produces_both_artifacts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            template = root / "app.template.html"
            template.write_text(self.TEMPLATE, encoding="utf-8")
            view = app.build_app_view(fos.empty_state(), vault(tmp))
            written = app.write_outputs(view, template, root / "out" / "app.html",
                                        root / "out" / "vault-index.json")
            self.assertEqual(len(written), 2)
            self.assertTrue(all(p.exists() for p in written))
            self.assertIn("note_count",
                          json.loads((root / "out" / "vault-index.json").read_text()))


class TestCli(unittest.TestCase):
    """`check` is a ratchet: it fails above an agreed ceiling, not on principle."""

    def run_check(self, root: Path, *extra: str) -> int:
        state_path = root / "founder-state.json"
        fos.save_state(fos.empty_state(), state_path)
        argv = ["--root", str(root), "--state", str(state_path), "check", *extra]
        stdout, sys.stdout = sys.stdout, open("/dev/null", "w")
        try:
            return app.main(argv)
        finally:
            sys.stdout.close()
            sys.stdout = stdout

    def test_check_fails_above_the_ceiling(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(self.run_check(vault(tmp)), 1)

    def test_check_passes_within_an_agreed_ceiling(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(self.run_check(vault(tmp), "--max-defects", "50"), 0)

    def test_check_passes_on_a_coherent_vault(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_note(root, "00_CONSTITUTION/A.md", title="A", related='"[[B]]"')
            write_note(root, "00_CONSTITUTION/B.md", title="B", related='"[[A]]"')
            self.assertEqual(self.run_check(root), 0)


class TestShippedApp(unittest.TestCase):
    """What is committed to the Vault must always build, render, and stay honest."""

    def test_shipped_template_carries_the_placeholder(self):
        if not app.DEFAULT_TEMPLATE.exists():
            self.skipTest("no shipped template yet")
        self.assertIn(app.VIEW_PLACEHOLDER,
                      app.DEFAULT_TEMPLATE.read_text(encoding="utf-8"))

    def test_the_real_vault_builds_and_renders(self):
        if not (app.DEFAULT_TEMPLATE.exists() and fos.DEFAULT_STATE.exists()):
            self.skipTest("no shipped template or state yet")
        state = fos.load_state(fos.DEFAULT_STATE)
        view = app.build_app_view(state, app.VAULT_ROOT)
        html = app.render_app(view, app.DEFAULT_TEMPLATE)
        self.assertGreater(view["know"]["note_count"], 100)
        self.assertIn("Alpha Proxima", html)

    def test_the_app_makes_no_network_call(self):
        """FD-002: the page is local-only. It must reference no remote resource."""
        if not app.DEFAULT_TEMPLATE.exists():
            self.skipTest("no shipped template yet")
        template = app.DEFAULT_TEMPLATE.read_text(encoding="utf-8")
        for forbidden in ("http://", "https://", "//cdn", "fetch(", "XMLHttpRequest",
                          "WebSocket", "<link", "@import"):
            self.assertNotIn(forbidden, template, f"template must not contain {forbidden!r}")

    def test_the_app_never_writes_state(self):
        """One writer per source of truth. This module is not it."""
        source = Path(app.__file__).read_text(encoding="utf-8")
        for forbidden in ("save_state", "set_mission", "add_task", "add_priority",
                          "resolve_decision"):
            self.assertNotIn(f"founder_os.{forbidden}", source)


if __name__ == "__main__":
    unittest.main(verbosity=2)
