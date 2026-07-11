---
title: Ingestion Folder
id: apx-ingestion-readme
department: LUMIAION
domain: ingestion
type: readme
status: active
version: 1.0.0
created: 2026-07-10
updated: 2026-07-10
source: founder-request
tags: [ingestion, readme, knowledge-pipeline]
related: [source-record-standard.md, extraction-standard.md, evidence-classification-standard.md, founder-synthesis-standard.md, drive-ingestion-workflow.md, ingestion-approval-gates.md, ../AUTOMATIONS/drive-sync-spec.md, ../KNOWLEDGE/README.md]
owner: "Office of Knowledge (scope pending Founder ratification)"
---

# INGESTION

## Purpose

Hold the Knowledge Ingestion Engine — the institutional pipeline that will later transform `.My life unfolding.` (and, eventually, other raw source archives) into OSG Knowledge Objects. This is a **design sprint deliverable**: no ingestion has occurred, no raw source has been touched, and no file has been read from Google Drive as part of producing this folder.

## Scope

This folder defines standards and workflow only. It does not contain any ingested content — that belongs under `../KNOWLEDGE/<domain>/` once the pipeline actually runs.

## The Ingestion Lifecycle

```
RAW SOURCE → SOURCE RECORD → EXTRACTION → CLASSIFICATION → FOUNDER SYNTHESIS → OSG KNOWLEDGE OBJECT → KNOWLEDGE GRAPH
```

| Stage | Standard | Template | Gate |
|---|---|---|---|
| Raw Source | `../AUTOMATIONS/drive-sync-spec.md` (governs the archive boundary) | — | — |
| Source Record | `source-record-standard.md` | `../TEMPLATES/source-record.template.md` | G1 — none |
| Extraction | `extraction-standard.md` | `../TEMPLATES/extraction-note.template.md` | G2 — none |
| Classification | `evidence-classification-standard.md` | (annotation, no new document) | G3 — conditional, Ethics & Evidence Council |
| Founder Synthesis | `founder-synthesis-standard.md` | `../TEMPLATES/founder-synthesis.template.md` | G4 — Founder review recommended |
| OSG Knowledge Object | (existing) `../TEMPLATES/designed-knowledge-object.template.md` | — | G5 — Founder approval if public-candidate |
| Knowledge Graph | `../INDEX/master-index.md`, `../SCRIPTS/build-index.py` | — | — |
| *(Publication)* | *(OSGMETAPHYSICS, out of this repository's scope)* | — | G6 — Ethics & Evidence Council + Founder |

Full gate detail: `ingestion-approval-gates.md`.

## Relationship to Existing Pipelines

This lifecycle formalizes, and does not replace, two pipelines already present in this repository:
- `../AUTOMATIONS/drive-sync-spec.md`'s six transformation stages (raw identification → extraction → synthesis → perspective separation → application mapping → content ideation) — that document remains authoritative on what automation may do to Drive; this folder sequences the fuller workflow around it.
- `../KNOWLEDGE/README.md`'s six-stage Knowledge Object Lifecycle (Raw Source → Extraction → Synthesis → OSG Principle → Application → Content Output) — this folder's lifecycle is a more granular version of the same first three stages (adding Source Record as an explicit stage, and Classification as its own named step between Extraction and Synthesis).

## Safety Rules

Binding across every stage of this pipeline:

1. **Raw sources are never modified.** No process in this folder renames, edits, reorganizes, or deletes anything at its origin.
2. **Original author/source remains traceable.** Every derived document carries its Source ID back to a Source Record (`source-record-standard.md`).
3. **No plagiarism.** Extraction must distinguish quotation from paraphrase and attribute both (`extraction-standard.md`).
4. **No medical/health claim goes public without Ethics & Evidence review.** Enforced at Gate 3 (Clinical classification) and Gate 6 (publication) — `ingestion-approval-gates.md`.
5. **Uncertainty must be preserved.** Classification categories travel forward through Synthesis; authority (including the Founder's) does not upgrade a claim's evidentiary status (`evidence-classification-standard.md`, `founder-synthesis-standard.md`).
6. **Metaphysical/symbolic/experiential/scientific claims must remain separated.** Enforced by the seven-category classification set applied per extraction entry, never per source (`evidence-classification-standard.md`).

## Pilot Batch

Ingestion does not proceed against the full `.My life unfolding.` archive yet. A 3-5 item pilot batch is defined by policy in `drive-ingestion-workflow.md`; the actual items are not yet named (no Drive visibility in this design sprint).

## Unresolved Decisions

1. **Two knowledge-object templates now exist**: `../TEMPLATES/osg-knowledge-object.template.md` (referenced by `drive-sync-spec.md`) and `../TEMPLATES/designed-knowledge-object.template.md` (Sprint 1 Knowledge Design System). This pipeline points new work at the latter; the former is not retired. Needs a Founder or Codex decision.
2. **Evidence category provenance.** The seven-category classification set is used repository-wide (`../DESIGN/`) as if citing "Constitution Art. XI," but the constitutional package is not filed in this repository. Needs a filing decision (carried over from Sprint 1.5).
3. **Relationship to Book III's C/M/Q/E/S/P** (separate Vault repository) — treated as a probable, unconfirmed second axis (`evidence-classification-standard.md`). Not resolved here.
4. **Approval recording mechanism** — whether ingestion approvals should route through `../OPERATIONS/CPOS/APPROVAL_GATES.md`'s generic table or the interim frontmatter `approval_status` field this folder uses. Not resolved here.
5. **The Ethics & Evidence Council is not seated.** Gates 3 and 6 will stop and wait, not proceed on Founder approval alone, until it exists.
6. **Pilot batch items are unnamed.** Requires Drive access and Founder designation, per `drive-ingestion-workflow.md`.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-10 | Claude (Repository Architect / Knowledge Pipeline Designer) | Initial INGESTION folder, Sprint 3 — Knowledge Ingestion Engine design, no ingestion performed. |
