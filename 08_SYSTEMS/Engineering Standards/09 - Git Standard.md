---
title: "09 - Git Standard"
aliases: ["GitHub Standard", "Repository Standard"]
tags: [systems, engineering, standards, git, github, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-standard
standard_id: "ES-09"
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[ALPHA PROXIMA ENGINEERING HANDBOOK]]"]
related_documents: ["[[Vault Structure Convention]]"]
related_research_programs: []
---

# 09 - Git Standard

## Purpose

Define Git and GitHub practices that preserve institutional memory, support review, and keep technical changes reversible.

---

## Scope

Applies to the Alpha Proxima Vault and related repositories used for engineering, automation, documentation, and local-first infrastructure.

---

## Rules

- Keep commits focused on one coherent change.
- Do not mix unrelated Obsidian workspace noise with intentional content changes.
- Use branches for substantial or risky changes.
- Use `codex/` prefix for CODEX implementation branches unless a different prefix is requested.
- Write commit messages in imperative mood.
- Include tests or validation notes for implementation changes.
- Use pull requests for reviewed changes when working through GitHub.
- Tag releases when a reusable tool, standard library, or package reaches a meaningful version.
- Prefer revert commits over history rewriting on shared branches.
- Never commit secrets.

### Branch Naming

| Branch Type | Pattern | Example |
|-------------|---------|---------|
| Feature | `codex/short-feature-name` | `codex/engineering-standards-library` |
| Fix | `codex/fix-short-description` | `codex/fix-note-generator-paths` |
| Docs | `codex/docs-short-description` | `codex/docs-python-standard` |
| Release | `release/vX.Y.Z` | `release/v1.0.0` |

### Commit Style

```text
Add engineering standards handbook

Create the initial standards library for Markdown, metadata,
folder naming, file naming, Python, CLI, automation, logging,
Git, and templates.
```

---

## Examples

### Pull Request Template

```markdown
## Purpose

## Changes

## Validation

## Governance Boundary

## Related Documents
```

### Version Tag

```text
engineering-standards-v1.0.0
```

### Rollback

```text
Use a revert commit that explains why the change was reversed.
Do not delete the historical record.
```

---

## Best Practices

- Review diffs before committing.
- Separate generated files from source changes when practical.
- Keep PR descriptions short but complete.
- Link related ADRs, concept notes, implementation notes, and standards.
- Use tags for stable milestones, not every minor edit.
- Keep repository roots clean and documented.

---

## Common Mistakes

- Committing editor state or workspace files by accident.
- Combining a standards change with unrelated content edits.
- Using vague commit messages such as `update` or `fix stuff`.
- Force-pushing shared branches without explicit agreement.
- Treating Git history as a replacement for decision records.

---

## Future Evolution

Future versions may define protected branch rules, required checks, release automation, changelog generation, and repository ownership. Any required review policy should align with Foundation governance.

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial Git standard |

---

## Related Standards

- [[03 - Folder Naming Convention]]
- [[04 - File Naming Convention]]
- [[05 - Python Development Standard]]
- [[07 - Automation Standard]]
- [[10 - Template Standard]]

