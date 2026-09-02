---
title: "Vault Note Generator"
aliases: ["Obsidian Note Generator", "Implementation Note Generator"]
tags: [systems, automation, obsidian, implementation, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "0.1.0"
authors: ["CODEX"]
dependencies: ["Python 3 standard library", "[[Implementation Note Template]]", "[[Vault Structure Convention]]"]
related_documents: ["[[Implementation Note Template]]", "[[Vault Structure Convention]]", "[[LUMIAION Architecture Spec v0.1]]"]
related_research_programs: []
---

# Vault Note Generator

## Purpose

This document describes the local note generator for the Alpha Proxima Obsidian Vault. The generator reduces repetitive Markdown setup by creating draft notes from approved templates while preserving human control over placement, meaning, and governance status.

---

## Dependencies

- Python 3 standard library
- [[Implementation Note Template]]
- [[Vault Structure Convention]]
- [[LUMIAION Architecture Spec v0.1]]

---

## Version

| Field | Value |
|-------|-------|
| **Version** | 0.1.0 |
| **Status** | active |
| **Last Updated** | 2026-07-02 |

---

## Author

[[CODEX]]

---

## Related Documents

- [[Implementation Note Template]]
- [[Vault Structure Convention]]
- [[LUMIAION Architecture Spec v0.1]]
- [[Decision Routing Protocol]]

---

## Related Research Programs

- N/A

---

## Implementation Notes

The generator lives at `08_SYSTEMS/Automation/vault_note.py`. It currently supports implementation notes and writes them to `08_SYSTEMS/Implementation Notes/` unless a specific output path is supplied.

Example:

```bash
python3 08_SYSTEMS/Automation/vault_note.py implementation "Local API Integration Plan" --author CODEX --purpose "Draft the implementation plan for a local API integration."
```

The tool creates parent folders when needed, refuses to overwrite existing files unless `--force` is supplied, and keeps generated notes in `draft` status.

---

## Future Improvements

- [ ] Add a dry-run mode that prints the target path and generated frontmatter without writing a file.
- [ ] Add validation for required frontmatter across the vault.
- [ ] Add support for additional approved templates after the template lifecycle is formalized.
- [ ] Add an index note for generated implementation notes if the folder grows beyond ten notes.

---

## Context

The vault already contains governance and research templates. Implementation work needs a lower-friction format for technical maintenance without turning every script or workflow into a governance artifact.

This generator is intentionally narrow. It scaffolds a draft note from explicit command input. It does not infer institutional status, ratify decisions, classify decision classes, or move files across governance folders.

---

## Core Content

### Supported Note Types

| Type | Template | Default Folder |
|------|----------|----------------|
| implementation | [[Implementation Note Template]] | `08_SYSTEMS/Implementation Notes/` |

### Operational Boundary

Automation may create draft scaffolds and reduce repeated formatting work. Automation may not decide whether a note is canonical, approved, constitutional, or binding.

### Maintenance Workflow

1. Confirm the note belongs in the vault and not inside an existing note.
2. Generate the draft note.
3. Review and complete all placeholder sections.
4. Link the note to relevant documents.
5. Update version history when the note becomes active.

---

## Open Questions

- [ ] Should implementation notes receive their own sequential identifier?
- [ ] Should generated notes be indexed automatically in a future `08_SYSTEMS/Implementation Notes Index`?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-07-02 | [[CODEX]] | Initial generator documentation |
