---
title: Evidence Classification Standard
id: apx-ingestion-evidence-classification-standard
department: LUMIAION
domain: ingestion
type: ingestion-standard
status: active
version: 1.0.0
created: 2026-07-10
updated: 2026-07-10
source: founder-request
tags: [ingestion, evidence, classification]
related: [extraction-standard.md, ../DESIGN/research-note-standard.md, ../DESIGN/callout-standard.md]
owner: "Ethics & Evidence Council (not yet seated — see Unresolved Decisions in INGESTION/README.md)"
---

# Evidence Classification Standard

## Purpose

Define the third stage of the ingestion lifecycle: assigning every extracted item a classification before it is allowed into Founder Synthesis. This is the formal enforcement point for the repository-wide rule that metaphysical, symbolic, experiential, and scientific claims must remain separated (`README.md`, Safety Rules).

## Classification Set

Every extraction entry (`extraction-standard.md`) receives exactly one of the following categories, matching the vocabulary already in use in `../DESIGN/research-note-standard.md` and `../DESIGN/callout-standard.md`'s Evidence callout:

- **Empirical**
- **Clinical**
- **Historical**
- **Philosophical**
- **Symbolic**
- **Experiential**
- **Speculative**

**Source note, not yet resolved:** these seven categories are cited elsewhere in this repository as "Constitution Art. XI," but the constitutional package containing that Article is **not filed in this repository** (pending source — see `INGESTION/README.md`, Unresolved Decisions). This standard uses the same vocabulary for consistency with `../DESIGN/`, not as a citation to a document that exists here.

**Separate, unreconciled taxonomy:** a different six-class evidence system (Class C/M/Q/E/S/P — Consensus, Competing Models, Open Questions, Emerging Evidence, Speculative Hypotheses, Phenomenological Reports) exists in the separate Vault repository's `Book III - Knowledge Integrity`. The relationship between that system and this one (two orthogonal axes — confidence-status vs. claim-domain — is the working theory, not yet confirmed) is an open cross-repository question, not resolved by this standard.

## Classification Rule

1. Classification is assigned to the *extraction entry*, not the source as a whole — a single source (e.g., a journal entry) commonly contains extractions in more than one category.
2. Classification is never inferred silently. The classifier states, in one sentence, why an entry received its category.
3. **Symbolic and Experiential entries are not downgraded to Speculative by default**, and empirical/clinical entries are not upgraded to certainty they do not have. The category describes the *kind* of claim, not its perceived value.
4. Any entry classified **Clinical** is automatically flagged for Ethics & Evidence Council review before it may reach a public-facing Founder Synthesis or OSG Knowledge Object (`ingestion-approval-gates.md`).

## Output

A Classification pass annotates each entry in an Extraction Note with its category and one-sentence basis. No new document type is created at this stage — classification is metadata added to the Extraction Note, consumed by Founder Synthesis next.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-10 | Claude (Repository Architect / Knowledge Pipeline Designer) | Initial Evidence Classification Standard, Sprint 3. Constitution Art. XI citation marked pending source; Book III relationship flagged unresolved. |
