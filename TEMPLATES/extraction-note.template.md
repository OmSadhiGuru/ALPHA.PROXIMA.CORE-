---
title: Extraction Note Template
id: apx-template-extraction-note
department: LUMIAION
domain: templates
type: template
status: active
version: 1.0.0
created: 2026-07-10
updated: 2026-07-10
source: founder-request
tags: [template, extraction-note, ingestion]
related: [../INGESTION/extraction-standard.md, ../INGESTION/evidence-classification-standard.md]
owner: "Office of Research (scope pending Founder ratification)"
---

# Extraction Note Template

Use this template to record extracted claims, themes, and observations from a single Source Record (`../INGESTION/extraction-standard.md`). Copy the block below as the new document's live frontmatter, then fill in every field.

```yaml
---
title:
id: apx-extraction-
department:
domain: ingestion
type: extraction-note
status: draft
version: 0.1.0
created:
updated:
source: drive-ingestion
source_record_id:  # the Source ID this extraction traces back to
tags: [extraction-note]
related: []
owner:
---
```

# Extraction Note — Source Title

Traces back to Source ID: *(from the Source Record)*.

## Extraction Entries

| # | Locator | Type | Extract | Classification | Basis for Classification |
|---|---|---|---|---|---|
| 1 | | quotation / paraphrase / observation / data-point | | *(filled during Classification — see `../INGESTION/evidence-classification-standard.md`)* | |
| 2 | | | | | |

Add rows as needed. One extracted item per row — do not merge multiple claims into one entry.

## Extractor

Who performed this extraction, and when.

## Notes

Anything about the extraction process itself worth recording — ambiguity in the source, items considered but excluded, etc. This section is not for interpretation of what the extracts mean; that belongs to Founder Synthesis.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 0.1.0 | | | |

## Template Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-10 | Claude (Repository Architect / Knowledge Pipeline Designer) | Initial template, Sprint 3. |
