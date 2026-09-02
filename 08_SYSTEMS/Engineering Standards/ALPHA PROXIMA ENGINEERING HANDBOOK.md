---
title: "ALPHA PROXIMA ENGINEERING HANDBOOK"
aliases: ["Engineering Handbook", "Alpha Proxima Engineering Standards Library"]
tags: [systems, engineering, standards, handbook, alpha-proxima]
created: 2026-07-02
updated: 2026-07-05
status: active
version: "1.1.0"
authors: ["CODEX"]
artifact_type: handbook
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Vault Structure Convention]]", "[[Book I - The Constitution]]"]
related_documents: ["[[Vault Structure Convention]]", "[[Implementation Note Template]]"]
related_research_programs: []
---

# ALPHA PROXIMA ENGINEERING HANDBOOK

## Purpose

This handbook is the entry point for Alpha Proxima engineering standards. It defines how technical contributors, reasoning engines, and automation systems should create durable work that feels like it came from the same institution.

The handbook does not redefine the Foundation. It translates existing institutional architecture into reusable engineering practice.

---

## Scope

This handbook governs Markdown, metadata, folder structure, file naming, Python utilities, CLI tools, automation, logging, Git practice, and template lifecycle work inside the Alpha Proxima Vault and related local-first repositories.

---

## Standards Library

| Standard | Canonical Document | Primary Use |
|----------|--------------------|-------------|
| 01 | [[01 - Markdown Style Guide]] | Document structure and formatting |
| 02 | [[02 - YAML Frontmatter Standard]] | Metadata consistency |
| 03 | [[03 - Folder Naming Convention]] | Durable vault hierarchy |
| 04 | [[04 - File Naming Convention]] | Human-readable file names |
| 05 | [[05 - Python Development Standard]] | Python utilities and services |
| 06 | [[06 - CLI Standard]] | Command-line interfaces |
| 07 | [[07 - Automation Standard]] | Automation boundaries and reliability |
| 08 | [[08 - Logging Standard]] | Event, audit, and debug logs |
| 09 | [[09 - Git Standard]] | Branches, commits, reviews, releases |
| 10 | [[10 - Template Standard]] | Template creation and evolution |
| 11 | [[11 - One Question Document Standard]] | Single-purpose documents and AI-friendly modularity |

---

## Rules

- Prefer consistency over cleverness.
- Prefer simple durable conventions over tool-specific optimizations.
- Keep human judgment outside automation.
- Use Obsidian-compatible Markdown and Git-friendly plain text.
- Every standard must be versioned, cross-linked, and understandable without private context.
- Engineering standards may recommend governance action, but must not make constitutional decisions.

---

## Examples

A new contributor implementing an automation should read:

1. [[02 - YAML Frontmatter Standard]]
2. [[04 - File Naming Convention]]
3. [[05 - Python Development Standard]]
4. [[06 - CLI Standard]]
5. [[07 - Automation Standard]]
6. [[08 - Logging Standard]]
7. [[09 - Git Standard]]

A contributor creating a new reusable document should read:

1. [[01 - Markdown Style Guide]]
2. [[02 - YAML Frontmatter Standard]]
3. [[10 - Template Standard]]
4. [[11 - One Question Document Standard]]

---

## Best Practices

- Start from the narrowest applicable standard.
- Link standards from implementation notes when they constrain the work.
- Keep examples small enough to copy and adapt.
- Record deviations explicitly in implementation notes or ADRs.
- Review standards when repeated confusion appears in implementation work.

---

## Common Mistakes

- Treating standards as suggestions when automation depends on them.
- Creating technology-specific folder names that become obsolete.
- Using metadata fields inconsistently across similar notes.
- Automating approval, canonization, or governance classification.
- Updating a template without updating its version history.

---

## Future Evolution

Future versions may add standards for APIs, local services, vector databases, MCP servers, n8n workflows, security, data retention, and release engineering.

Any standard that changes institutional authority or governance process must be proposed through the Foundation governance process before adoption.

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-05 | [[CODEX]] | Added one-question document standard |
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial engineering standards handbook created |

---

## Related Standards

- [[01 - Markdown Style Guide]]
- [[02 - YAML Frontmatter Standard]]
- [[03 - Folder Naming Convention]]
- [[04 - File Naming Convention]]
- [[05 - Python Development Standard]]
- [[06 - CLI Standard]]
- [[07 - Automation Standard]]
- [[08 - Logging Standard]]
- [[09 - Git Standard]]
- [[10 - Template Standard]]
- [[11 - One Question Document Standard]]
