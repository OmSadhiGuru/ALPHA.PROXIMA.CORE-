---
title: "10 - Template Standard"
aliases: ["Template Standard", "Template Lifecycle Standard", "Reusable Template Standard"]
tags: [systems, engineering, standards, templates, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-standard
standard_id: "ES-10"
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[ALPHA PROXIMA ENGINEERING HANDBOOK]]"]
related_documents: ["[[Implementation Note Template]]", "[[ADR Template]]", "[[Concept Note Template]]", "[[Research Note Template]]"]
related_research_programs: []
---

# 10 - Template Standard

## Purpose

Define how Alpha Proxima templates are created, versioned, evolved, deprecated, and reused so repeated work becomes consistent without freezing institutional learning.

---

## Scope

Applies to all reusable Markdown templates, code templates, workflow templates, PR templates, issue templates, automation templates, and future prompt or MCP templates.

---

## Rules

- Store canonical Markdown templates in `10_TEMPLATES/`.
- Every template must include frontmatter.
- Every template must include purpose, scope or usage context, required sections, related standards, and version history.
- Use placeholders consistently: `{{PLACEHOLDER_NAME}}`.
- Mark the beginning and end of copyable template content when the file includes explanatory material.
- Version templates with semantic versioning.
- Do not make breaking template changes silently.
- Deprecate templates before removing them from active use.
- Link templates to the standards that govern them.
- Use automation to scaffold templates, not to approve their institutional use.

### Template Lifecycle

| Stage | Meaning |
|-------|---------|
| draft | Being designed |
| active | Approved for use |
| deprecated | Still available but discouraged |
| superseded | Replaced by a newer template |
| archived | Preserved, not maintained |

### Versioning

| Change | Version Increment |
|--------|-------------------|
| Correct typo or clarify wording | Patch |
| Add optional section or example | Minor |
| Change required structure or meaning | Major |

---

## Examples

### Placeholder

```markdown
# {{TITLE}}

## Purpose

{{PURPOSE}}
```

### Template Boundary

```markdown
> TEMPLATE BEGINS BELOW THIS LINE

---
title: "{{TITLE}}"
---

# {{TITLE}}

> TEMPLATE ENDS ABOVE THIS LINE
```

### Deprecation Note

```markdown
status: deprecated
superseded_by: "[[Implementation Note Template]]"
```

---

## Best Practices

- Design templates from repeated real use, not speculation.
- Keep required sections stable across related templates.
- Include examples that show correct use.
- Keep placeholders obvious and searchable.
- Separate explanatory guidance from copyable template content.
- Add generator support only after the template structure has stabilized.

---

## Common Mistakes

- Creating a template for a one-off document.
- Changing required fields without updating version history.
- Mixing multiple artifact types into one template.
- Leaving placeholders ambiguous.
- Letting generated templates imply approval or canonical status.
- Failing to link the template to relevant standards.

---

## Future Evolution

Future versions may define template inheritance, reusable section libraries, validation schemas, and template generators. Governance-sensitive templates should receive explicit approval before being treated as canonical.

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial template standard |

---

## Related Standards

- [[01 - Markdown Style Guide]]
- [[02 - YAML Frontmatter Standard]]
- [[03 - Folder Naming Convention]]
- [[04 - File Naming Convention]]
- [[07 - Automation Standard]]
