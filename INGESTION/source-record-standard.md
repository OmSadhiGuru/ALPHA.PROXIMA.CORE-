---
title: Source Record Standard
id: apx-ingestion-source-record-standard
department: LUMIAION
domain: ingestion
type: ingestion-standard
status: active
version: 1.0.0
created: 2026-07-10
updated: 2026-07-10
source: founder-request
tags: [ingestion, source-record, traceability]
related: [../AUTOMATIONS/drive-sync-spec.md, ../INDEX/source-index.md, ../TEMPLATES/source-record.template.md]
owner: "Office of Knowledge (scope pending Founder ratification)"
---

# Source Record Standard

## Purpose

Define the fixed structure of a **Source Record** — the first durable artifact created for any raw source entering the Knowledge Ingestion Engine, and the anchor every later stage (Extraction, Classification, Founder Synthesis, OSG Knowledge Object) must trace back to.

## Scope

Applies to every raw source considered for ingestion, starting with `.My life unfolding.` (Google Drive) per `../AUTOMATIONS/drive-sync-spec.md`, and to any future source archive (Notion export, physical notes, third-party research) admitted under the same pipeline.

## Relationship to Existing Standards

This does not replace `../AUTOMATIONS/drive-sync-spec.md`'s "Files Are Indexed" rule or `../INDEX/source-index.md`'s row structure — it is the standard for the full Source Record *document* that a `source-index.md` row points to. One Source Record document per source; one summary row per Source Record in the index.

## Required Fields

1. **Source ID** — stable identifier, matches the corresponding `../INDEX/source-index.md` row.
2. **Original Title / Filename** — exactly as it appears at origin, unmodified.
3. **Origin Location** — Drive path, file path, URL, or physical description. Never a copy of the content itself.
4. **File Type** — format of the raw source (document, audio, image, note, etc.).
5. **Author / Originator** — who created the source. If the Founder, state so explicitly. If a third party, this field is mandatory and drives the No-Plagiarism Rule (`README.md`, Safety Rules).
6. **Created / Observed Date** — when the source material originated, not when it was ingested.
7. **Intake Date** — when this Source Record was created.
8. **Processing Status** — one of the values defined in `../AUTOMATIONS/drive-sync-spec.md` (`unindexed`, `indexed`, `extracted`, `synthesized`, `converted`, `reviewed`, `archived-source`).
9. **Copyright / License Note** — what is known about rights over this material. If unknown, state `unknown` explicitly rather than omitting the field — this is load-bearing for the No-Plagiarism Rule.
10. **Derived Knowledge Object IDs** — populated as later stages produce output; empty at intake.
11. **Immutability Statement** — a fixed sentence confirming the raw source itself has not been altered: *"The source at Origin Location has not been renamed, edited, or removed by this Source Record or any process referencing it."*

## Rule

A Source Record is created before any Extraction work begins on that source (Extraction Standard, Prerequisite). No extraction, classification, or synthesis document may exist without a Source Record it traces back to by Source ID.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-10 | Claude (Repository Architect / Knowledge Pipeline Designer) | Initial Source Record Standard, Sprint 3. |
