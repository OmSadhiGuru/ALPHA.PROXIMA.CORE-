---
title: "11 - One Question Document Standard"
aliases: ["One Document One Question Standard", "Single Purpose Document Standard"]
tags: [systems, engineering, standards, documentation, modularity, alpha-proxima, osg]
created: 2026-07-05
updated: 2026-07-05
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-standard
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[01 - Markdown Style Guide]]", "[[02 - YAML Frontmatter Standard]]", "[[10 - Template Standard]]"]
related_documents: ["[[ALPHA PROXIMA ENGINEERING HANDBOOK]]", "[[OSG Launch Technical Foundation]]"]
related_research_programs: []
---

# 11 - One Question Document Standard

## Purpose

Ensure every Alpha Proxima and OSG artifact has one clear reason to exist.

## Scope

This standard applies to:

- Alpha Proxima institutional documents
- OSG launch and academy documents
- templates
- engineering reports
- blueprints
- standards
- operating procedures
- course documents
- workbook documents
- journal documents
- knowledge graph documents

## Rule

Every document must answer one question only.

Not five. Not ten. One.

## Required Field

Every durable artifact should include a `core_question` field in YAML when it is created or next revised.

Example:

```yaml
core_question: "How are OSG courses designed?"
```

## Examples

| Artifact | Core Question |
|----------|---------------|
| OLS | How are OSG courses designed? |
| Reference Blueprint | How is Awaken the Inner Guru structured? |
| Workbook Blueprint | How is the workbook organized? |
| Journal Blueprint | How is reflection organized? |
| Engineering Report | What engineering condition was found? |
| Template | What repeatable artifact does this template create? |
| Protocol | What process does this protocol govern? |

## Best Practices

- Write the question before writing the document.
- Split the document when a second major question appears.
- Use links instead of embedding unrelated explanations.
- Let indexes connect documents; do not turn indexes into mega-documents.
- Keep examples subordinate to the core question.

## Common Mistakes

- Combining architecture, roadmap, implementation, and governance in one document.
- Using one document as a dumping ground for unresolved ideas.
- Adding sections because they are interesting rather than necessary.
- Creating broad titles that hide unclear scope.
- Duplicating content instead of linking to the source artifact.

## Implementation Notes

This rule improves searchability, versioning, AI retrieval, graph extraction, and future API design. It also reduces update risk because each document has one obvious owner and one obvious reason to change.

## Future Evolution

- [ ] Add `core_question` to the YAML validator.
- [ ] Add a document-splitting recommendation report.
- [ ] Add automated detection of multi-question documents.
- [ ] Add graph node extraction support for `core_question`.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-05 | [[CODEX]] | Initial one-question document standard |

## Related Standards

- [[01 - Markdown Style Guide]]
- [[02 - YAML Frontmatter Standard]]
- [[10 - Template Standard]]

