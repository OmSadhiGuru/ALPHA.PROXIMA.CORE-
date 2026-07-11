---
title: Extraction Standard
id: apx-ingestion-extraction-standard
department: LUMIAION
domain: ingestion
type: ingestion-standard
status: active
version: 1.0.0
created: 2026-07-10
updated: 2026-07-10
source: founder-request
tags: [ingestion, extraction]
related: [source-record-standard.md, evidence-classification-standard.md, ../DESIGN/research-note-standard.md, ../TEMPLATES/extraction-note.template.md]
owner: "Office of Research (scope pending Founder ratification)"
---

# Extraction Standard

## Purpose

Define how claims, themes, and observations are pulled out of a raw source, per `../KNOWLEDGE/README.md`'s Extraction stage rule: *"separate extracted material from interpretation."* This is the second stage of the ingestion lifecycle (`README.md`) and the first stage where content leaves the source's own words.

## Prerequisite

A completed Source Record (`source-record-standard.md`) must exist for the source being extracted from. Extraction never begins on an un-recorded source.

## Extraction Rules

1. **Quotation vs. paraphrase is marked explicitly.** A direct quotation is wrapped in quotation marks and attributed to the exact location in the source (page, timestamp, or section). A paraphrase is marked as such and never presented typographically as a quotation.
2. **One extracted item, one entry.** Do not merge multiple claims or observations into a single extraction entry — later Classification and Synthesis stages depend on items being separable.
3. **No interpretation at this stage.** An extraction records *what the source says or shows*, not what the extractor believes it means. Interpretation belongs to Founder Synthesis (`founder-synthesis-standard.md`).
4. **Attribution travels with the extract.** Every extraction entry carries its Source ID (from the Source Record) and a precise locator within that source.
5. **No plagiarism.** Extracted material that will appear in any public-facing output must be either a clearly attributed direct quotation or a substantive paraphrase in the extractor's own structure and wording — never a near-verbatim rewording presented as original. This applies regardless of the source's copyright status; attribution is an intellectual honesty rule, not only a legal one (`README.md`, Safety Rules).

## Extraction Entry Fields

1. Source ID (from Source Record).
2. Locator (page/timestamp/section).
3. Extract type: quotation | paraphrase | observation | data-point.
4. Extract content.
5. Extractor.
6. Extraction date.
7. Preliminary theme tag (informal, not yet the formal classification — see `evidence-classification-standard.md`).

## Output

One or more Extraction Notes (`../TEMPLATES/extraction-note.template.md`) per source, each containing multiple extraction entries. Extraction Notes feed Classification, never Founder Synthesis directly.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-10 | Claude (Repository Architect / Knowledge Pipeline Designer) | Initial Extraction Standard, Sprint 3. |
