---
title: Source Record Template
id: apx-template-source-record
department: LUMIAION
domain: templates
type: template
status: active
version: 1.0.0
created: 2026-07-10
updated: 2026-07-10
source: founder-request
tags: [template, source-record, ingestion]
related: [../INGESTION/source-record-standard.md, ../INDEX/source-index.md]
owner: "Office of Knowledge (scope pending Founder ratification)"
---

# Source Record Template

Use this template for every raw source entering the Knowledge Ingestion Engine (`../INGESTION/source-record-standard.md`). Copy the block below as the new document's live frontmatter, then fill in every field. This document is created **before** any extraction work begins.

```yaml
---
title:
id: apx-source-
department:
domain: ingestion
type: source-record
status: draft
version: 0.1.0
created:
updated:
source: drive-ingestion
processing_status: unindexed  # unindexed | indexed | extracted | synthesized | converted | reviewed | archived-source
tags: [source-record]
related: []
owner:
---
```

# Source Title

## Source Record

| Field | Value |
|---|---|
| Source ID | |
| Original Title / Filename | |
| Origin Location | |
| File Type | |
| Author / Originator | |
| Created / Observed Date | |
| Intake Date | |
| Processing Status | |
| Copyright / License Note | *(state `unknown` explicitly if not known — do not leave blank)* |
| Derived Knowledge Object IDs | *(empty at intake)* |

## Immutability Statement

The source at Origin Location has not been renamed, edited, or removed by this Source Record or any process referencing it.

## Notes

Any context needed to understand this source that does not belong in the fields above.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 0.1.0 | | | |

## Template Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-10 | Claude (Repository Architect / Knowledge Pipeline Designer) | Initial template, Sprint 3. |
