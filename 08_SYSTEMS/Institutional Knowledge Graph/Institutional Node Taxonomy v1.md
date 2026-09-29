---
title: "Institutional Node Taxonomy v1"
aliases: ["Node Taxonomy", "Entity Taxonomy", "KnowledgeNode Taxonomy", "Entity Registry"]
tags: [systems, knowledge-graph, taxonomy, entities, truth-kernel, alpha-proxima]
created: 2026-09-29
updated: 2026-09-29
status: active
version: "1.0.0"
authors: ["CLAUDE"]
artifact_type: architecture-specification
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Architecture"
reasoning_engine: "Claude"
dependencies: ["[[Cognitive Function Registry]]", "[[Office Registry]]", "[[Agent and Subagent Registry]]", "[[Book I - The Constitution]]"]
related_documents: ["[[Knowledge Graph Architecture v1.0]]", "[[Node Taxonomy]]", "[[Governance Model Crosswalk]]", "[[12 - Continuous Integration Standard]]", "[[Alpha Proxima App Architecture v1]]"]
related_research_programs: []
---

# Institutional Node Taxonomy v1

## Purpose

Establish what a node in the Institutional Knowledge Graph actually is, so the graph can distinguish a **document** from an **actor** — and stop reporting the Foundation's own Council as missing.

---

## Context

### The finding

The Institutional Knowledge Graph was built on a single assumption: *every node is a Markdown document.* On 2026-09-29 the Truth Kernel reported **750 unresolved relationships**. Sampling them showed only **51 distinct targets**, and the largest were not documents at all:

| Target | Occurrences | Source fields |
|---|---:|---|
| CODEX | 236 | `authors`, wiki-links |
| Alpha Proxima Foundation | 198 | `institutional_owner`, `authors` |
| LUMIAION | 113 | `authors`, wiki-links |
| OSG | 29 | `institutional_owner` |
| CODEX (CF-07) | 16 | `authors` |

**515 of the 750 were `OWNED_BY` or `PRODUCED_BY`** — relationships derived from `authors:`, `institutional_owner:` and `reasoning_engine:`. The graph was demanding a Markdown document for every actor the Foundation names.

That is not decay. It is a modelling gap, and it had a cost: the Founder saw a permanent **ATTENTION** status that no amount of repair could clear. A standing red nobody can clear is a red nobody reads — the failure mode [[12 - Continuous Integration Standard]] already names.

### What was rejected

- **Suppressing the findings.** That hides the gap instead of closing it.
- **Creating Markdown documents for CODEX, LUMIAION and the rest.** Hundreds of stub documents written to satisfy a resolver would be the Foundation lying to its own graph.
- **Lowering severity.** Severity is a consequence of semantics, not a substitute for them.

---

## Architecture

### The taxonomy

```
KnowledgeNode
│
├── DocumentNode      an institutional artifact, one Markdown file
│
└── EntityNode        an actor, named by a ratified registry
     ├── agent        cognitive functions and named agent roles
     ├── office       where institutional authority is housed
     ├── organization the Foundation and its ventures
     └── person       the Founder
```

`EventNode`, `SystemNode` and `ExternalResourceNode` are reserved for the live layer and are **not** implemented here. Implementing a type before something produces it would be modelling fiction.

### Two rules

**Derived, never authored.** Every entity comes from a registry the Foundation already ratified. Nothing in `entity_registry.py` invents an actor. A name absent from every registry does not resolve, and the graph keeps reporting it — that is the difference between modelling the institution and silencing it.

**Provenance is mandatory.** Every entity carries `canonical_source`, the document that confers its identity. An entity nobody ratified cannot exist.

### Canonical sources

| Source | Confers |
|---|---|
| [[Cognitive Function Registry]] | CF-01…CF-16 as `agent:cf-NN`. Canonical since Epoch V per [[Governance Model Crosswalk]]. |
| [[Office Registry]] | The offices as `office:*`. |
| [[Agent and Subagent Registry]] | AGT-001…AGT-016 as `agent:agt-NNN`. |
| [[Book I - The Constitution]] | `organization:alpha-proxima-foundation`, `organization:osg`, `person:founder`. |

[[Engine Registry]] is **superseded** and is not read as authority.

### Alias precedence

One alias resolves to at most one entity. Where registries overlap, three rules decide, in order:

1. **An explicit CF code wins.** `LUMIAION (CF-01)` is CF-01, whatever `LUMIAION` alone resolves to.
2. **A registry's own label beats a name it merely cites.** `LUMIAION` is an office by name; CF-09 merely runs on it. Engines move between functions; labels do not.
3. **Earlier sources win**, so the canonical Cognitive Function model precedes what it superseded.

Collisions are recorded, not hidden — `ap.py entities check` prints them.

### What a wiki-link never becomes

A wiki-link in prose is **always** a document reference. `[[CODEX]]` in a sentence asks for a document about CODEX; it is not reclassified as the actor. Only the three entity-bearing frontmatter fields — `authors`, `institutional_owner`, `reasoning_engine` — produce entity edges.

This matters: it is the line that stops entity resolution from quietly absorbing genuine broken links.

---

## Severity semantics

| Severity | Meaning | Examples |
|---|---|---|
| **error** | Integrity failure. Drives `attention`. | missing wiki-link target, identity collision, duplicate node id, empty document |
| **warning** | A real issue that does not invalidate graph integrity. | provisional identity, missing owner, unknown node type, ambiguous target |
| **info** | Expected, non-actionable state. | template placeholder such as `authors: ["<AUTHOR>"]` |

**Health follows errors only.** A template that ships `<AUTHOR>` is doing its job; counting it against the Foundation measures the template.

---

## The two instruments are independent

The App's coherence ratchet and the Truth Kernel answer different questions. They are **not** expected to agree on a number, and forcing them to would destroy information.

| | App coherence | Truth Kernel |
|---|---|---|
| **Question** | Is every document connected and described? | Is the typed graph internally consistent? |
| **Unit** | Documents | Nodes, entities, typed relationships |
| **Gate** | `COHERENCE_CEILING`, ratchets down | Errors only |
| **Owns** | Document-level hygiene | Graph integrity |

The system must always be able to say *App coherence: 123 defects* and *Truth graph: 20 errors, 985 warnings, 12 informational* without a single ambiguous global red.

---

## Verification

Measured on the shipped vault, 2026-09-29:

| Signal | Before | After |
|---|---:|---:|
| Unresolved relationships | 750 | **246** |
| Entity relationships (typed, with provenance) | — | **492** |
| Template placeholders (informational) | — | **12** |
| Total findings | 1509 | **1017** |
| Warnings | 1489 | **985** |
| **Errors** | **20** | **20** |
| App coherence defects | 123 | **123** |

**Errors are unchanged, and that is the point.** Entity resolution removed no genuine defect — the 4 empty documents, 6 identity collisions and 10 missing document references all survive, asserted by `test_real_errors_survive_entity_resolution`.

---

## Future Improvements

1. **`EventNode`** when the live layer produces events; `actor_id` on an AlphaEvent should resolve against this model.
2. **Constitutional entity table.** `organization:*` and `person:founder` are declared in code with constitutional provenance because the Constitution defines them in prose. A ratified table would replace the declaration without changing a consumer.
3. **Unregistered authors.** Names such as `Claude Code — Vault Architect` remain unresolved by design. Either register them or correct the documents; do not widen the resolver to swallow them.
4. **`missing_owner` (180) and `provisional_identity` (373)** are genuine and unaddressed. Both are document hygiene, not modelling gaps.

---

## Open Questions

- Should `agent:agt-NNN` and `agent:cf-NN` remain distinct, or should an agent role resolve through to the function it serves?
- Does an office author documents in its own right, or always through a cognitive function?
- Should unregistered authors block ratification of a document?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-09-29 | CLAUDE | First taxonomy: DocumentNode / EntityNode split, derived-never-authored rule, alias precedence, severity semantics, instrument independence |
