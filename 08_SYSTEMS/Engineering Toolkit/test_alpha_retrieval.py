#!/usr/bin/env python3
"""Tests for vault retrieval.

Most of these assert what the module refuses to claim. A retrieval layer that
overstates itself is worse than none, because a reader who trusts a null result
stops looking.

Run: python3 "08_SYSTEMS/Engineering Toolkit/test_alpha_retrieval.py"
"""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import alpha_retrieval as ret  # noqa: E402

NOTE = """---
title: "{title}"
aliases: [{aliases}]
tags: [{tags}]
artifact_type: {artifact_type}
---

# {title}

{body}
"""


def write(root: Path, relative: str, *, title: str, body: str = "Ordinary prose.",
          aliases: str = "", tags: str = "alpha-proxima",
          artifact_type: str = "policy") -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(NOTE.format(title=title, aliases=aliases, tags=tags,
                                artifact_type=artifact_type, body=body), encoding="utf-8")


def corpus(tmp: str) -> Path:
    root = Path(tmp)
    write(root, "00_CONSTITUTION/Charter.md", title="Charter",
          body="The founding rules. Refers to [[Ledger Standard]].")
    write(root, "08_SYSTEMS/Ledger Standard.md", title="Ledger Standard",
          tags="ledger append-only", body="An append-only ledger is never rewritten.")
    write(root, "08_SYSTEMS/Unrelated.md", title="Unrelated",
          body="Gardening, weather, and the price of tin.")
    return root


class TestItNeverClaimsToBeSemantic(unittest.TestCase):
    def test_the_module_declares_itself_lexical(self):
        self.assertFalse(ret.IS_SEMANTIC)
        self.assertEqual(ret.RETRIEVAL_KIND, "lexical+structural")

    def test_every_search_result_carries_the_declaration(self):
        with tempfile.TemporaryDirectory() as tmp:
            view = ret.search("ledger", ret.build_index(corpus(tmp)))
            self.assertFalse(view["is_semantic"])
            self.assertEqual(view["retrieval_kind"], "lexical+structural")

    def test_the_index_carries_it_too(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertFalse(ret.build_index(corpus(tmp))["is_semantic"])

    def test_an_empty_result_still_states_the_limits(self):
        """A null result must not read as 'the Foundation holds nothing on this'."""
        with tempfile.TemporaryDirectory() as tmp:
            view = ret.search("zzzznonexistentterm", ret.build_index(corpus(tmp)))
            self.assertEqual(view["results"], [])
            self.assertTrue(view["limits"])
            # Assert the two claims, not my phrasing of them: that the absence
            # of embeddings is named, and that an empty result is explicitly
            # not a statement about what the Foundation holds.
            limits = " ".join(view["limits"]).lower()
            self.assertIn("embedding", limits)
            self.assertIn("never that the foundation holds nothing", limits)

    def test_the_rendered_output_says_so_on_an_empty_result(self):
        with tempfile.TemporaryDirectory() as tmp:
            text = ret.render(ret.search("zzzznonexistent", ret.build_index(corpus(tmp))))
            self.assertIn("not an empty Foundation", text)

    def test_the_rendered_output_says_not_semantic(self):
        with tempfile.TemporaryDirectory() as tmp:
            text = ret.render(ret.search("ledger", ret.build_index(corpus(tmp))))
            self.assertIn("not semantic", text)

    def test_the_module_records_that_it_narrows_blk_002_rather_than_closing_it(self):
        source = Path(ret.__file__).read_text(encoding="utf-8")
        self.assertIn("narrowed by this module, not closed", source)


class TestLexicalRanking(unittest.TestCase):
    def test_a_term_in_the_title_outranks_the_same_term_in_prose(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "a/Ledger.md", title="Ledger", body="Nothing else here.")
            write(root, "b/Other.md", title="Other",
                  body="ledger ledger ledger ledger ledger ledger")
            hits = ret.lexical_search(ret.build_index(root), "ledger", limit=2)
            self.assertEqual(hits[0]["path"], "a/Ledger.md")

    def test_every_hit_names_the_terms_that_earned_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            hits = ret.lexical_search(ret.build_index(corpus(tmp)), "append-only ledger")
            self.assertTrue(hits)
            self.assertIn("ledger", hits[0]["matched_terms"])
            self.assertEqual(hits[0]["reached_by"], "term")

    def test_a_document_sharing_no_words_is_not_returned(self):
        """The honest failure, asserted so nobody mistakes it for a bug."""
        with tempfile.TemporaryDirectory() as tmp:
            hits = ret.lexical_search(ret.build_index(corpus(tmp)), "append-only ledger")
            self.assertNotIn("08_SYSTEMS/Unrelated.md", [h["path"] for h in hits])

    def test_stopwords_earn_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(ret.lexical_search(ret.build_index(corpus(tmp)), "the and of is"), [])

    def test_code_fences_are_not_indexed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "x/Fenced.md", title="Fenced",
                  body="Prose.\n\n```\nsecretfencedtoken\n```\n")
            self.assertEqual(ret.lexical_search(ret.build_index(root), "secretfencedtoken"), [])


class TestStructuralExpansion(unittest.TestCase):
    def relationships(self):
        return [{"relationship_type": "REFERENCES",
                 "source_path": "00_CONSTITUTION/Charter.md",
                 "target_path": "08_SYSTEMS/Ledger Standard.md",
                 "provenance": "body_wikilink"}]

    def test_a_neighbour_is_reached_and_marked_as_such(self):
        with tempfile.TemporaryDirectory() as tmp:
            index = ret.build_index(corpus(tmp))
            seeds = [{"path": "00_CONSTITUTION/Charter.md"}]
            found = ret.expand_structurally(seeds, self.relationships(), index)
            self.assertEqual(len(found), 1)
            self.assertEqual(found[0]["path"], "08_SYSTEMS/Ledger Standard.md")
            self.assertEqual(found[0]["reached_by"], "edge")

    def test_a_neighbour_names_the_seed_and_the_edge_that_reached_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            index = ret.build_index(corpus(tmp))
            found = ret.expand_structurally(
                [{"path": "00_CONSTITUTION/Charter.md"}], self.relationships(), index)
            self.assertEqual(found[0]["from_seed"], "00_CONSTITUTION/Charter.md")
            self.assertEqual(found[0]["edge_type"], "REFERENCES")
            self.assertEqual(found[0]["edge_provenance"], "body_wikilink")

    def test_the_hop_works_in_both_directions(self):
        with tempfile.TemporaryDirectory() as tmp:
            index = ret.build_index(corpus(tmp))
            found = ret.expand_structurally(
                [{"path": "08_SYSTEMS/Ledger Standard.md"}], self.relationships(), index)
            self.assertEqual(found[0]["path"], "00_CONSTITUTION/Charter.md")

    def test_a_seed_is_never_returned_as_its_own_neighbour(self):
        with tempfile.TemporaryDirectory() as tmp:
            index = ret.build_index(corpus(tmp))
            seeds = [{"path": "00_CONSTITUTION/Charter.md"},
                     {"path": "08_SYSTEMS/Ledger Standard.md"}]
            self.assertEqual(ret.expand_structurally(seeds, self.relationships(), index), [])

    def test_only_structural_relationship_types_expand(self):
        """Causal and temporal edges belong to the memory graph, not to retrieval."""
        for kind in ("CAUSED_BY", "PRECEDED_BY", "OWNED_BY"):
            self.assertNotIn(kind, ret.EXPAND_TYPES)

    def test_expansion_is_bounded(self):
        with tempfile.TemporaryDirectory() as tmp:
            index = ret.build_index(corpus(tmp))
            many = [{"relationship_type": "REFERENCES",
                     "source_path": "00_CONSTITUTION/Charter.md",
                     "target_path": path, "provenance": "x"}
                    for path in index["documents"] if path != "00_CONSTITUTION/Charter.md"]
            found = ret.expand_structurally(
                [{"path": "00_CONSTITUTION/Charter.md"}], many, index, limit=1)
            self.assertEqual(len(found), 1)


class TestItReadsAndNothingElse(unittest.TestCase):
    def test_the_module_writes_nothing(self):
        source = Path(ret.__file__).read_text(encoding="utf-8")
        for forbidden in (".write_text(", ".mkdir(", "shutil", "os.remove"):
            self.assertNotIn(forbidden, source)

    def test_the_module_opens_no_socket(self):
        source = Path(ret.__file__).read_text(encoding="utf-8")
        for forbidden in ("urllib.request", "http.client", "import socket", "requests"):
            self.assertNotIn(forbidden, source)

    def test_it_declares_no_dependency(self):
        source = Path(ret.__file__).read_text(encoding="utf-8")
        for forbidden in ("numpy", "sklearn", "sentence_transformers", "faiss", "torch"):
            self.assertNotIn(forbidden, source)


class TestTheShippedVault(unittest.TestCase):
    def test_the_real_vault_indexes(self):
        index = ret.build_index(ret.VAULT_ROOT)
        self.assertGreater(index["document_count"], 300)
        self.assertGreater(index["term_count"], 5000)

    def test_a_known_document_is_findable_by_its_own_subject(self):
        index = ret.build_index(ret.VAULT_ROOT)
        hits = ret.lexical_search(index, "coherence ceiling ratchet", limit=5)
        paths = [hit["path"] for hit in hits]
        self.assertTrue(any("Continuous Integration Standard" in p for p in paths),
                        f"ES-12 should rank for its own subject; got {paths}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
