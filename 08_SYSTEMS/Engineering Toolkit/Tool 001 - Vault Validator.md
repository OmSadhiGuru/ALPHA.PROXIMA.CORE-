---
title: "Tool 001 - Vault Validator"
aliases: ["Vault Validator", "Engineering Toolkit Tool 001"]
tags: [systems, engineering, toolkit, validation, obsidian, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "0.1.0"
authors: ["CODEX"]
artifact_type: implementation-note
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["Python 3 standard library", "[[ALPHA PROXIMA ENGINEERING HANDBOOK]]"]
related_documents: ["[[Alpha Proxima Engineering Toolkit]]", "[[02 - YAML Frontmatter Standard]]", "[[03 - Folder Naming Convention]]", "[[04 - File Naming Convention]]", "[[06 - CLI Standard]]", "[[07 - Automation Standard]]"]
related_research_programs: []
---

# Tool 001 - Vault Validator

## Purpose

The Vault Validator scans the Obsidian Vault for engineering quality issues and generates a Markdown validation report.

It checks for missing YAML, invalid frontmatter, missing required metadata, broken wiki links, missing backlinks, duplicate filenames, and likely incorrect folder placement.

---

## Dependencies

- Python 3 standard library
- [[02 - YAML Frontmatter Standard]]
- [[03 - Folder Naming Convention]]
- [[04 - File Naming Convention]]
- [[06 - CLI Standard]]
- [[07 - Automation Standard]]

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

- [[Alpha Proxima Engineering Toolkit]]
- [[ALPHA PROXIMA ENGINEERING HANDBOOK]]
- [[02 - YAML Frontmatter Standard]]
- [[03 - Folder Naming Convention]]
- [[04 - File Naming Convention]]
- [[07 - Automation Standard]]
- [[08 - Logging Standard]]

---

## Related Research Programs

- N/A

---

## Implementation Notes

The CLI lives at `08_SYSTEMS/Engineering Toolkit/vault_validator.py`.

The validator is intentionally report-only. It does not edit notes, move files, approve metadata, or resolve governance questions.

---

## CLI Interface

```bash
python3 "08_SYSTEMS/Engineering Toolkit/vault_validator.py" [options]
```

Options:

| Option | Purpose |
|--------|---------|
| `--vault PATH` | Vault root. Defaults to the current working directory. |
| `--output PATH` | Report output path. Defaults to `08_SYSTEMS/Engineering Toolkit/Reports/Vault Validation Report.md`. |
| `--format markdown` | Report format. Markdown is currently supported. |
| `--include-hidden` | Include hidden folders. Hidden folders are skipped by default. |
| `--fail-on LEVEL` | Return exit code `1` when issues exist at or above `warning` or `error`. |

Exit codes:

| Code | Meaning |
|------|---------|
| 0 | Report generated successfully and fail threshold was not met |
| 1 | Report generated and fail threshold was met |
| 2 | Invalid arguments or unreadable vault |

---

## Usage Examples

Generate the default report:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/vault_validator.py"
```

Write a report to a temporary file:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/vault_validator.py" --output /private/tmp/vault-validation.md
```

Use in an automation check:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/vault_validator.py" --fail-on error
```

---

## Future Improvements

- [ ] Add JSON output for downstream automation.
- [ ] Add severity configuration.
- [ ] Add stricter YAML parsing when a dependency policy is approved.
- [ ] Add reusable scanner modules for Tool 004 and Tool 005.
- [ ] Add baseline support so legacy debt can be tracked separately from new issues.

---

## Context

The vault is expected to grow from hundreds to tens of thousands of notes. Manual validation will not scale. The Vault Validator creates an engineering feedback loop while preserving human control over what changes are made.

---

## Core Content

### Checks

| Check | Description |
|-------|-------------|
| Missing YAML | Markdown note does not begin with frontmatter |
| Invalid frontmatter | Frontmatter is missing a closing delimiter or contains unsupported top-level structure |
| Missing required metadata | Required fields from [[02 - YAML Frontmatter Standard]] are absent |
| Broken wiki links | `[[Target]]` does not resolve to a note filename or frontmatter title |
| Missing backlinks | Markdown note has no incoming wiki links |
| Duplicate filenames | Same file name appears in more than one location |
| Incorrect folder placement | Known artifact naming pattern appears in the wrong canonical folder |

### Operational Boundary

The validator reports likely issues. A human or approved governance process decides what to change.

---

## Open Questions

- [ ] Should root-level index notes be exempt from missing backlink warnings?
- [ ] Should legacy notes created before the Engineering Handbook be tracked in a baseline file?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-07-02 | [[CODEX]] | Initial Vault Validator tool documented and implemented |

