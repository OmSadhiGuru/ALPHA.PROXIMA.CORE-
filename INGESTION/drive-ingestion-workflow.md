---
title: Drive Ingestion Workflow
id: apx-ingestion-drive-ingestion-workflow
department: LUMIAION
domain: ingestion
type: ingestion-workflow
status: active
version: 1.0.0
created: 2026-07-10
updated: 2026-07-10
source: founder-request
tags: [ingestion, drive, workflow, pilot-batch]
related: [../AUTOMATIONS/drive-sync-spec.md, source-record-standard.md, extraction-standard.md, evidence-classification-standard.md, founder-synthesis-standard.md, ingestion-approval-gates.md]
owner: "Office of Knowledge (scope pending Founder ratification)"
---

# Drive Ingestion Workflow

## Purpose

Apply the ingestion lifecycle (`README.md`) specifically to Google Drive folder `.My life unfolding.`, governed at the automation-boundary level by `../AUTOMATIONS/drive-sync-spec.md`. That document remains authoritative on what automation may and may not do to Drive; this document sequences the human/LUMIAION workflow steps that use it.

## Workflow, Step by Step

1. **Select** — a source (single file or tightly-scoped subfolder) is chosen from `.My life unfolding.`, limited to the current pilot batch (see below).
2. **Record** — a Source Record is created (`source-record-standard.md`, `../TEMPLATES/source-record.template.md`), and a corresponding row is added to `../INDEX/source-index.md`. Processing status: `indexed`.
3. **Extract** — an Extraction Note is created (`extraction-standard.md`, `../TEMPLATES/extraction-note.template.md`). Processing status: `extracted`.
4. **Classify** — every extraction entry receives a category (`evidence-classification-standard.md`). No new document; the Extraction Note is annotated.
5. **Synthesize** — a Founder Synthesis document is created (`founder-synthesis-standard.md`, `../TEMPLATES/founder-synthesis.template.md`). Processing status: `synthesized`.
6. **Gate** — the synthesis passes through the applicable approval gate(s) (`ingestion-approval-gates.md`) before proceeding.
7. **Convert** — an OSG Knowledge Object is created under `../KNOWLEDGE/<domain>/`, per `../AUTOMATIONS/drive-sync-spec.md`'s storage rule. Processing status: `converted`, then `reviewed` once checked.
8. **Index** — `../INDEX/master-index.md` and `../INDEX/source-index.md` are updated with the new object's ID and its Source ID, closing the traceability loop back to the raw source.

At every step, the raw Drive source itself is untouched — this workflow only ever creates new documents inside `ALPHAPROXIMA/`, per `../AUTOMATIONS/drive-sync-spec.md`'s Non-Goals.

## Pilot Batch — Selection Policy

Per instruction, ingestion does not proceed against the whole of `.My life unfolding.` yet. A pilot batch of **3 to 5 documents or tightly-scoped folders** is used to test this workflow end to end before wider processing begins.

**Selection criteria** (for whoever — Founder or LUMIAION — designates the actual pilot items):
1. Prefer items that are self-contained (a single entry, a single theme) over long-running or multi-year material, so the pilot exercises the full lifecycle without stalling on scope.
2. Include at least one item likely to classify as **Symbolic or Experiential** and at least one likely to classify as **Empirical or Historical**, so the pilot tests the classification separation rule (`evidence-classification-standard.md`) rather than only one register.
3. Exclude, for this pilot, any item likely to require **Clinical** classification — the Ethics & Evidence Council gate (`ingestion-approval-gates.md`) should be tested deliberately, not accidentally, on the first pass.
4. Exclude anything time-sensitive or already slated for near-term publication — the pilot is a pipeline test, not a production release.

**This document does not name the actual pilot items.** Doing so requires visibility into `.My life unfolding.`'s actual contents, which this design sprint does not have and is not authorized to browse or mutate. The pilot batch's specific item names are an open field, to be filled in by whoever next has Drive access and Founder authorization to designate them (see `README.md`, Unresolved Decisions).

## Pilot Batch Record (to be completed before pilot begins)

| # | Item (Drive path or title) | Expected Classification | Status |
|---|---|---|---|
| 1 | *pending selection* | | not started |
| 2 | *pending selection* | | not started |
| 3 | *pending selection* | | not started |
| 4 (optional) | *pending selection* | | not started |
| 5 (optional) | *pending selection* | | not started |

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-10 | Claude (Repository Architect / Knowledge Pipeline Designer) | Initial Drive Ingestion Workflow and pilot batch policy, Sprint 3. Pilot items intentionally left unnamed — no Drive visibility. |
