---
title: "Implementation Note Template"
aliases: ["Technical Implementation Template", "Automation Note Template"]
tags: [template, systems, implementation, automation, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["CODEX"]
template_type: Implementation Note
related_documents: ["[[Vault Structure Convention]]", "[[LUMIAION Architecture Spec v0.1]]"]
related_research_programs: []
---

# Implementation Note Template

## Purpose

This template is the standard format for implementation notes within [[Alpha Proxima Core]]. Implementation notes document technical work that supports the institution: automation, scripts, APIs, local infrastructure, integrations, developer tooling, and maintenance workflows.

Implementation notes are not governance decisions. If the work changes authority, institutional structure, or binding process, it must be routed through [[Concept Note Template]] and [[ADR Template]] instead.

---

## Dependencies

- [[Vault Structure Convention]]
- [[LUMIAION Architecture Spec v0.1]]
- [[Decision Routing Protocol]]

---

## Version

| Field | Value |
|-------|-------|
| **Template Version** | 1.0.0 |
| **Maintainer** | [[CODEX]] |
| **Status** | active |

---

## Author

[[CODEX]]

---

## Related Documents

- [[Vault Structure Convention]]
- [[LUMIAION Architecture Spec v0.1]]
- [[Decision Routing Protocol]]
- [[ADR Template]]
- [[Concept Note Template]]

---

## Related Research Programs

- N/A

---

## Implementation Notes

Use this template when the artifact is primarily executable, operational, or technical. Examples include:

- Python utilities
- Local server infrastructure
- Obsidian automation
- n8n workflows
- MCP integration notes
- GitHub workflow documentation
- Vector database indexing notes
- API integration notes

Do not use this template to ratify decisions, alter governance, or define institutional architecture.

---

## Future Improvements

- [ ] Add specialized subtemplates for API integrations, local services, and workflow automation if implementation volume increases.
- [ ] Add generator support for additional template types after governance approval.

---

## Core Content

---

> **TEMPLATE BEGINS BELOW THIS LINE**
> Delete everything above this line in actual implementation notes. Fill in every section. Do not leave sections blank; write "N/A" with a brief explanation if a section truly does not apply.

---

---
title: "{{TITLE}}"
aliases: []
tags: [systems, implementation, alpha-proxima]
created: {{DATE}}
updated: {{DATE}}
status: draft
version: "0.1.0"
authors: ["{{AUTHOR}}"]
implementation_type: "{{IMPLEMENTATION_TYPE}}"
dependencies: []
related_documents: []
related_research_programs: []
---

# {{TITLE}}

## Purpose

{{PURPOSE}}

---

## Dependencies

{{DEPENDENCIES}}

---

## Version

| Field | Value |
|-------|-------|
| **Version** | 0.1.0 |
| **Status** | draft |
| **Last Updated** | {{DATE}} |

---

## Author

[[{{AUTHOR}}]]

---

## Related Documents

{{RELATED_DOCUMENTS}}

---

## Related Research Programs

{{RELATED_RESEARCH_PROGRAMS}}

---

## Implementation Notes

{{IMPLEMENTATION_NOTES}}

---

## Future Improvements

{{FUTURE_IMPROVEMENTS}}

---

## Context

[What background does a maintainer need to understand why this implementation exists?]

---

## Core Content

[Document the implementation, workflow, commands, interfaces, configuration, or maintenance process.]

---

## Operational Boundary

This implementation automates repetitive technical work only. It does not make governance decisions, approve institutional changes, alter constitutional documents, or replace human review where judgment is required.

---

## Open Questions

- [ ] [Question]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.1.0 | {{DATE}} | [[{{AUTHOR}}]] | Initial draft |

---

> **TEMPLATE ENDS ABOVE THIS LINE**
