---
title: Founder Synthesis Template
id: apx-template-founder-synthesis
department: LUMIAION
domain: templates
type: template
status: active
version: 1.0.0
created: 2026-07-10
updated: 2026-07-10
source: founder-request
tags: [template, founder-synthesis, ingestion]
related: [../INGESTION/founder-synthesis-standard.md, ../INGESTION/ingestion-approval-gates.md, ../DESIGN/callout-standard.md]
owner: LUMIAION
---

# Founder Synthesis Template

Use this template to turn one or more classified Extraction Notes into a durable, OSG-native principle (`../INGESTION/founder-synthesis-standard.md`). Copy the block below as the new document's live frontmatter, then fill in every field.

```yaml
---
title:
id: apx-synthesis-
department:
domain: ingestion
type: founder-synthesis
status: draft
version: 0.1.0
created:
updated:
source: drive-ingestion
extraction_note_ids: []   # every Extraction Note this synthesis draws on
contains_clinical_classification: false  # true routes this to Gate 3, Ethics & Evidence Council
approval_status: draft    # draft | internal-reviewed | ethics-reviewed | public-approved | archived
tags: [founder-synthesis]
related: []
owner:
---
```

# Synthesis Title

## Contributing Extractions

| Extraction Note ID | Classification(s) Represented |
|---|---|
| | |

## Founder Synthesis

> [!reflection] or [!founder-decision]
> The durable principle itself — interpretive, attributed, and reusable outside the original source context. This is not a restatement of the extracted material; it is what the institution now understands as a result of it.

## Classification Carried Forward

State which classification(s) from the contributing extractions this synthesis rests on, and whether the synthesis itself introduces a new claim beyond what was extracted (if so, that new claim needs its own classification, stated here explicitly).

## Ethics Gate Check

> [!ethics-review-required] (only if contains_clinical_classification is true, or the synthesis is health/wellness/education/complementary-practice adjacent)
> State explicitly whether this synthesis requires Ethics & Evidence Council review before proceeding to an OSG Knowledge Object (Gate 3 or Gate 6, `../INGESTION/ingestion-approval-gates.md`). If not applicable, state why.

## Next Stage

Whether this synthesis is ready to become an OSG Knowledge Object (`../TEMPLATES/designed-knowledge-object.template.md`), and any gate it must clear first.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 0.1.0 | | | |

## Template Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-10 | Claude (Repository Architect / Knowledge Pipeline Designer) | Initial template, Sprint 3. |
