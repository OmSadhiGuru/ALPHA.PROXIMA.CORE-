---
title: "Vault Retrieval Architecture v1"
aliases: ["Vault Retrieval", "Lexical Retrieval", "BLK-002 Narrowing"]
tags: [systems, retrieval, memory, search, knowledge-graph, alpha-proxima]
created: 2026-09-29
updated: 2026-09-29
status: active
version: "1.0.0"
authors: ["CLAUDE"]
artifact_type: architecture-specification
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Architecture"
reasoning_engine: "Claude"
dependencies: ["[[Knowledge Graph Architecture v1.0]]", "[[Alpha Proxima Engineering Toolkit]]"]
related_documents: ["[[Alpha Proxima App Architecture v1]]", "[[Book III - Knowledge Integrity]]", "[[12 - Continuous Integration Standard]]", "[[Founder OS Architecture v1]]"]
related_research_programs: []
---

# Vault Retrieval Architecture v1

## Purpose

Answer the half of `BLK-002` that can be answered, and record precisely which half cannot — so that the blocker is **narrowed rather than closed**, and the Foundation keeps the memory of what it still lacks.

## Mission

Make finding a document in 394 of them a question rather than a chore, without once claiming a capability the Foundation does not have.

---

## Definitions

| Term | Meaning here |
|---|---|
| **Lexical retrieval** | Ranking by shared words. BM25 over weighted document surfaces. No model, no vectors. |
| **Structural retrieval** | Reaching a document through a relationship another document states about itself. |
| **Semantic retrieval** | Ranking by meaning, via embeddings. **Not implemented. Not approximated.** |
| **Narrowing a blocker** | Resolving part of a blocker's stated impact while leaving the blocker open, because the rest is unresolved. |

---

## Context

`BLK-002` reads:

> **Semantic memory layer (Layer 3) does not exist.**
> Impact: *LUMIAION cannot search the full Vault in-session; context loading stays manual.*

Those are two problems wearing one label.

The **title** names a mechanism — embeddings. The **impact** names a cost — search is manual. The cost can be paid down substantially without the mechanism, and conflating them has kept the whole blocker at a standstill: nobody could build the vector store, so nobody built anything.

`INT-006` says the same thing from the other side: *"Engine Registry lists the Chief Memory Architect role as unfilled."* A structural vacancy became a reason for zero retrieval rather than a reason for partial retrieval.

---

## Architecture

Two strategies, combined, with provenance on every result.

### Lexical

BM25 over each document's weighted surfaces:

| Surface | Weight | Why |
|---|---:|---|
| `title` | 6 | A term in a title is a claim about the whole document |
| `aliases` | 4 | The names a document answers to |
| `tags` | 3 | The Foundation's own classification |
| `artifact_type` | 3 | What kind of thing it is |
| `cognitive_function` | 2 | Which function owns it |
| headings | 2 | Structure the author chose |
| body | 1 | A term here is a mention |

Code fences are excluded: a token inside an example is not a subject of the document. Stopwords are dropped before indexing, including Foundation-ubiquitous words — `alpha`, `proxima`, `foundation` discriminate nothing in this corpus.

**394 documents, 14,811 terms, 0.38 seconds.**

### Structural

The Institutional Knowledge Graph already holds ~2,700 typed relationships with provenance. After lexical seeding, **one hop** outward through `DEPENDS_ON`, `RELATED_TO` and `REFERENCES`, in either direction.

One hop, not two, on purpose: this graph is dense enough that two hops reach most of the vault, and a result set containing everything has told the reader nothing.

This is where retrieval earns its keep. A query for *"coherence ceiling ratchet"* ranks `12 - Continuous Integration Standard` first — correct, it owns the rule — and the hop surfaces `Book III - Knowledge Integrity`, which shares almost none of those words and is the constitutional basis a reader wants next.

**Causal and temporal edges are deliberately excluded.** Those belong to `alpha_memory.py`, which is the only module permitted to emit them. Retrieval witnesses structure; it does not witness occurrence.

### Every result says why it is a result

A ranked list with no reasons teaches its reader to accept the ranking. Each hit carries either the terms it matched, or the edge type, provenance and seed it was reached by. A wrong answer can then be diagnosed rather than merely distrusted.

---

## What this is not

**This is not semantic search and must never be described as such.**

It has no embeddings, no vectors, no model. It cannot match *"how does the Foundation decide things"* to a document titled *"Governance Framework"* that shares none of those words. Asked *"who is allowed to overrule a ratified choice"*, it returns the ADR Template — matched incidentally on `choice` and `ratified`, not because it understood the question.

**An empty result means no shared vocabulary. It never means the Foundation holds nothing on the subject.** That sentence travels in the `limits` field of every response and is printed on every empty render, because the failure mode that matters is a reader who trusts a null.

`is_semantic: false` is a field in the read model, not a caveat in a footnote.

---

## Why the semantic half stays blocked

Embeddings require one of three things, and each is a decision the Founder owns:

| Path | What it costs |
|---|---|
| **A vendored dependency** | The toolkit's zero-dependency property is an architectural decision enforced by CI, not a build detail. Breaking it is an amendment, not a fix. |
| **A hosted model** | A credential this repository does not hold, and an approved egress this Foundation has not granted. |
| **Appointing the Chief Memory Architect** | `INT-006` names this vacancy as the blocker's root. It is an institutional act, not an engineering task. |

A partial remedy that closed `BLK-002` would cost the Foundation the memory of what it still lacks. So:

> **`BLK-002` is narrowed, not closed.** Its stated impact — *"context loading stays manual"* — is substantially answered. Its title — *"the semantic memory layer does not exist"* — remains true.

`founder_os.py` is the single writer of Founder state, and `BLK-002` carries `needs_founder: true`. This document does not amend the record; the Founder does.

---

## Dependencies

| Dependency | Nature |
|---|---|
| Python 3 standard library | Runtime. Nothing else. |
| `vault_validator.py` | Markdown discovery and frontmatter parsing. Shared, not reimplemented. |
| `truth_kernel.py` | The relationship graph the structural hop traverses. Read-only. |
| The vault's Markdown notes | Canonical knowledge. Read-only to this module. |

---

## Related Documents

- [[Knowledge Graph Architecture v1.0]] — the graph the structural hop reads
- [[Book III - Knowledge Integrity]] — the constitutional basis for treating retrieval honesty as integrity
- [[Alpha Proxima Engineering Toolkit]] — `ap retrieve` registration
- [[Founder OS Architecture v1]] — owner of `BLK-002` and the single writer of its record
- [[12 - Continuous Integration Standard]] — the zero-dependency gate that shapes what retrieval may be

---

## Examples

```bash
AP='python3 "08_SYSTEMS/Engineering Toolkit/ap.py" retrieve'

$AP coherence ceiling ratchet        # lexical, then one structural hop
$AP --no-graph presence expiry       # lexical only, 0.38s
$AP --json --limit 20 event ledger   # the read model, for a consumer
$AP                                  # the contract: what this is and is not
```

---

## Verification

| Check | Result |
|---|---|
| `test_alpha_retrieval.py` | **23 passed** |
| Full toolkit regression | **656 across 15 suites** |
| Real vault indexes | 394 documents, 14,811 terms |
| A known document ranks for its own subject | asserted (ES-12 for the ceiling) |
| A title term outranks the same term repeated in prose | asserted |
| Code-fence tokens are not indexed | asserted |
| A document sharing no words is **not** returned | asserted — the honest failure, locked in |
| Empty result states its limits | asserted, in the read model and the render |
| Structural hop is marked, bounded, and names its seed | asserted |
| Causal and temporal edges excluded from expansion | asserted |
| Module writes nothing, opens no socket, declares no dependency | asserted |
| App coherence | **123 / 123** |

---

## Future Improvements

1. **Cache the index.** Rebuilt on every invocation today. 0.38s is cheap enough that caching would be premature, and a stale index is a worse failure than a slow one.
2. **Weight by recency or status.** A `superseded` document and an `active` one currently rank alike on vocabulary. The frontmatter to fix this already exists.
3. **Query expansion from the alias graph.** The entity registry knows `CODEX` and `CF-07` are one actor; retrieval does not. This is the nearest thing to semantics reachable without a model, because the synonyms would be the Foundation's own ratified ones rather than a model's guesses.

---

## Open Questions

- Which of the three paths to embeddings does the Founder intend? The answer determines whether `alpha_retrieval` stays the retrieval layer or becomes the lexical half of a hybrid one.
- Should retrieval be exposed through `/api/v1/` so the App can search, or stay a CLI capability for agents at session start?
- Does an `ap retrieve` call belong in a session-start hook, so context loading is automatic rather than merely possible?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-09-29 | CLAUDE | Lexical BM25 plus one structural hop over the Knowledge Graph; narrows `BLK-002` without closing it, and states in the read model that it is not semantic |
