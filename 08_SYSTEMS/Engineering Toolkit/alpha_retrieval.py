#!/usr/bin/env python3
"""Vault retrieval — lexical and structural. Deliberately **not** semantic.

`BLK-002` records that the semantic memory layer does not exist, and states its
impact: *"LUMIAION cannot search the full Vault in-session; context loading
stays manual."* Those are two different problems wearing one label, and this
module solves the second without pretending to solve the first.

## What this is

Two retrieval strategies over the 390-odd canonical documents, combined:

**Lexical.** BM25 over each document's title, aliases, tags, artifact type,
cognitive function, headings and body. Ordinary term matching, tuned for a
corpus of institutional prose where the same vocabulary recurs constantly and
the discriminating words are rare.

**Structural.** The Institutional Knowledge Graph already holds 2,700-odd typed
relationships with provenance. After lexical seeding, one hop outward through
`dependencies`, `related_documents` and their inbound counterparts surfaces
documents that never used the query's words but are what the seeds point at.
That is often the document actually wanted: a query about coherence finds the
report, and the hop finds the standard the report enforces.

## What this is not, stated plainly because the blocker will be read later

**This is not semantic search and must never be described as such.** It has no
embeddings, no vectors, no model. It cannot match *"how does the Foundation
decide things"* to a document titled *"Governance Framework"* that shares none
of those words. A reader who believes otherwise will trust a null result, and a
null result here means "no shared vocabulary", never "nothing relevant exists".

That limitation is structural, not an omission. Embeddings require either a
vendored dependency — which the CI gate refuses, by design, because the
toolkit's zero-dependency property is an architectural decision rather than a
build detail — or a hosted model, which requires a credential this repository
does not hold and an approved egress this Foundation has not granted.

So **`BLK-002` is narrowed by this module, not closed.** The manual-search half
is answered. The semantic half stays open, and the decision it waits on is the
Founder's: accept a dependency, accept a credential, or appoint the Chief
Memory Architect the Engine Registry still lists as unfilled. A partial remedy
that closed the blocker would cost the Foundation the memory of what it still
lacks.

## Every result says why it is a result

A retrieval layer that returns a ranked list and no reasons teaches its reader
to accept the ranking. Each hit here carries the terms it matched, or the edge
it was reached by and from which seed, so a wrong answer can be diagnosed
instead of merely distrusted.

Standard library only.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

TOOLKIT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT_DIR.parent.parent

SCHEMA_VERSION = "1.0.0"

# What this layer is, in a field, so no consumer has to infer it from the name.
RETRIEVAL_KIND = "lexical+structural"
IS_SEMANTIC = False


def _load_sibling(filename: str, name: str):
    import importlib.util
    path = (TOOLKIT_DIR / filename).resolve()
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load toolkit module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


vault_validator = _load_sibling("vault_validator.py", "retrieval_vault_validator")

TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9\-_/]*")
FENCE_RE = re.compile(r"```.*?```", re.S)
HEADING_RE = re.compile(r"^#{1,6}\s+(.+)$", re.M)

# Words that appear in nearly every institutional document and therefore
# discriminate nothing. BM25 already discounts them by document frequency; this
# keeps them out of the index entirely so the postings stay small and a reader
# inspecting a match is not shown "the" as evidence.
STOPWORDS = frozenset("""
a an and are as at be been but by for from has have how in into is it its of on
or that the their this to was were what when which who why will with not no
alpha proxima foundation document note md
""".split())

# Fields whose words say what a document *is*, weighted above prose because a
# term in a title is a claim about the whole document and a term in paragraph
# nine is a mention.
FIELD_WEIGHTS = (
    ("title", 6),
    ("aliases", 4),
    ("tags", 3),
    ("artifact_type", 3),
    ("cognitive_function", 2),
    ("headings", 2),
    ("body", 1),
)

# Relationship types worth one hop outward. Structural, stated by a document
# about itself — never inferred.
EXPAND_TYPES = ("DEPENDS_ON", "RELATED_TO", "REFERENCES")

# BM25, standard parameters. k1 controls how fast term frequency saturates; b
# how much a long document is penalised for length.
BM25_K1 = 1.4
BM25_B = 0.72


class RetrievalError(Exception):
    """Raised when the vault cannot be indexed."""


def tokenize(text: str) -> list[str]:
    """Lowercase terms, code fences removed, stopwords dropped."""
    cleaned = FENCE_RE.sub(" ", text.lower())
    return [t for t in TOKEN_RE.findall(cleaned) if t not in STOPWORDS and len(t) > 1]


def _as_text(value: Any) -> str:
    if isinstance(value, list):
        return " ".join(str(item) for item in value)
    return "" if value is None else str(value)


def document_fields(note: Any) -> dict[str, str]:
    """The weighted surfaces of one document."""
    fm = note.frontmatter or {}
    return {
        "title": _as_text(fm.get("title")) or Path(note.relative_path).stem,
        "aliases": _as_text(fm.get("aliases")),
        "tags": _as_text(fm.get("tags")),
        "artifact_type": _as_text(fm.get("artifact_type")),
        "cognitive_function": _as_text(fm.get("cognitive_function")),
        "headings": " ".join(HEADING_RE.findall(note.body or "")),
        "body": note.body or "",
    }


def build_index(root: Path | str = VAULT_ROOT) -> dict[str, Any]:
    """Index every canonical document once. Pure read; writes nothing."""
    root = Path(root)
    if not root.exists():
        raise RetrievalError(f"Vault root does not exist: {root}")
    notes = vault_validator.load_notes(root, include_hidden=False)
    if not notes:
        raise RetrievalError(f"No Markdown documents found under {root}")

    documents: dict[str, dict[str, Any]] = {}
    postings: dict[str, dict[str, int]] = defaultdict(dict)
    lengths: dict[str, int] = {}

    for note in notes:
        path = note.relative_path
        fields = document_fields(note)
        weighted: Counter[str] = Counter()
        for field, weight in FIELD_WEIGHTS:
            for term in tokenize(fields[field]):
                weighted[term] += weight
        if not weighted:
            continue
        documents[path] = {
            "path": path,
            "title": fields["title"],
            "artifact_type": fields["artifact_type"],
            "tags": fields["tags"].split() if fields["tags"] else [],
        }
        lengths[path] = sum(weighted.values())
        for term, count in weighted.items():
            postings[term][path] = count

    total = len(documents) or 1
    return {
        "schema_version": SCHEMA_VERSION,
        "retrieval_kind": RETRIEVAL_KIND,
        "is_semantic": IS_SEMANTIC,
        "root": str(root),
        "documents": documents,
        "postings": dict(postings),
        "lengths": lengths,
        "document_count": len(documents),
        "term_count": len(postings),
        "average_length": sum(lengths.values()) / total,
    }


def lexical_search(index: dict[str, Any], query: str, limit: int = 10) -> list[dict[str, Any]]:
    """BM25. Returns hits carrying the terms that earned them."""
    terms = tokenize(query)
    if not terms:
        return []

    total = index["document_count"] or 1
    average = index["average_length"] or 1.0
    scores: dict[str, float] = defaultdict(float)
    matched: dict[str, list[str]] = defaultdict(list)

    for term in set(terms):
        posting = index["postings"].get(term)
        if not posting:
            continue
        # +0.5/+0.5 smoothing keeps a term present in every document from going
        # negative, which would make a common word actively demote a match.
        idf = math.log(1 + (total - len(posting) + 0.5) / (len(posting) + 0.5))
        for path, frequency in posting.items():
            length = index["lengths"].get(path, 1)
            denominator = frequency + BM25_K1 * (1 - BM25_B + BM25_B * length / average)
            scores[path] += idf * frequency * (BM25_K1 + 1) / denominator
            matched[path].append(term)

    ranked = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
    hits = []
    for path, score in ranked[:limit]:
        document = index["documents"][path]
        hits.append({
            "path": path,
            "title": document["title"],
            "artifact_type": document["artifact_type"],
            "score": round(score, 4),
            "reached_by": "term",
            "matched_terms": sorted(set(matched[path])),
            "from_seed": None,
        })
    return hits


def load_relationships(contract: dict[str, Any] | None) -> list[dict[str, Any]]:
    if not contract:
        return []
    return [r for r in contract.get("relationships", [])
            if r.get("relationship_type") in EXPAND_TYPES]


def expand_structurally(seeds: Iterable[dict[str, Any]], relationships: list[dict[str, Any]],
                        index: dict[str, Any], limit: int = 5) -> list[dict[str, Any]]:
    """One hop from the seeds, in either direction, marked as such.

    Kept to one hop on purpose. Two hops in a graph this dense reaches most of
    the vault, and a result set that contains everything has told the reader
    nothing.
    """
    seed_paths = {hit["path"] for hit in seeds}
    if not seed_paths:
        return []

    neighbours: dict[str, dict[str, Any]] = {}
    for relationship in relationships:
        source = relationship.get("source_path")
        target = relationship.get("target_path")
        for origin, reached in ((source, target), (target, source)):
            if origin in seed_paths and reached and reached not in seed_paths:
                if reached in index["documents"] and reached not in neighbours:
                    document = index["documents"][reached]
                    neighbours[reached] = {
                        "path": reached,
                        "title": document["title"],
                        "artifact_type": document["artifact_type"],
                        "score": 0.0,
                        "reached_by": "edge",
                        "matched_terms": [],
                        "from_seed": origin,
                        "edge_type": relationship.get("relationship_type"),
                        "edge_provenance": relationship.get("provenance"),
                    }
    return sorted(neighbours.values(), key=lambda hit: hit["path"])[:limit]


def search(query: str, index: dict[str, Any], contract: dict[str, Any] | None = None,
           limit: int = 10, expand: int = 5) -> dict[str, Any]:
    """The composed read model for one query."""
    lexical = lexical_search(index, query, limit=limit)
    structural = expand_structurally(lexical, load_relationships(contract), index, limit=expand)
    return {
        "schema_version": SCHEMA_VERSION,
        "query": query,
        "retrieval_kind": RETRIEVAL_KIND,
        "is_semantic": IS_SEMANTIC,
        # Carried in every result so a null result is never read as "nothing
        # relevant exists" when it means "no shared vocabulary".
        "limits": [
            "No embeddings: a document sharing no words with the query is not found.",
            "An empty result means no lexical or structural match, never that the "
            "Foundation holds nothing on the subject.",
        ],
        "counts": {
            "lexical": len(lexical),
            "structural": len(structural),
            "indexed_documents": index["document_count"],
            "indexed_terms": index["term_count"],
        },
        "results": lexical + structural,
    }


def render(view: dict[str, Any]) -> str:
    lines = [f"QUERY  {view['query']!r}",
             f"  {view['retrieval_kind']} over {view['counts']['indexed_documents']} documents "
             f"({view['counts']['indexed_terms']} terms) — not semantic",
             ""]
    if not view["results"]:
        lines.append("  No match. That means no shared vocabulary, not an empty Foundation.")
        return "\n".join(lines)

    for hit in view["results"]:
        if hit["reached_by"] == "term":
            why = "terms: " + ", ".join(hit["matched_terms"][:6])
            lines.append(f"  {hit['score']:7.3f}  {hit['path']}")
        else:
            why = f"{hit.get('edge_type', 'edge')} from {hit['from_seed']}"
            lines.append(f"     edge  {hit['path']}")
        lines.append(f"            {hit['title']}")
        lines.append(f"            {why}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ap.py retrieve", description=__doc__)
    parser.add_argument("query", nargs="*", help="Words to search for.")
    parser.add_argument("--root", default=str(VAULT_ROOT), help="Vault root to index.")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--expand", type=int, default=5,
                        help="Structural neighbours to add. 0 disables the hop.")
    parser.add_argument("--json", action="store_true", help="Print the read model.")
    parser.add_argument("--no-graph", action="store_true",
                        help="Skip the Knowledge Graph; lexical only.")
    args = parser.parse_args(argv)

    root = Path(args.root)
    try:
        index = build_index(root)
    except RetrievalError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if not args.query:
        print(json.dumps({
            "schema_version": SCHEMA_VERSION,
            "retrieval_kind": RETRIEVAL_KIND,
            "is_semantic": IS_SEMANTIC,
            "indexed_documents": index["document_count"],
            "indexed_terms": index["term_count"],
            "expand_types": list(EXPAND_TYPES),
            "narrows_but_does_not_close": "BLK-002",
        }, indent=2))
        return 0

    contract = None
    if not args.no_graph and args.expand > 0:
        truth_kernel = _load_sibling(
            "../Institutional Knowledge Graph/Tools/truth_kernel.py", "retrieval_truth_kernel")
        contract = truth_kernel.build(root)

    view = search(" ".join(args.query), index, contract,
                  limit=args.limit, expand=args.expand)
    print(json.dumps(view, indent=2, ensure_ascii=False) if args.json else render(view))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
