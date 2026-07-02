---
title: "Tool 002 - YAML Validator"
aliases: ["YAML Validator", "Frontmatter Validator", "Engineering Toolkit Tool 002"]
tags: [systems, engineering, toolkit, validation, yaml, frontmatter, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "0.1.1"
authors: ["CODEX"]
artifact_type: implementation-note
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["Python 3 standard library", "[[02 - YAML Frontmatter Standard]]", "[[Tool 001 - Vault Validator]]"]
related_documents: ["[[Alpha Proxima Engineering Toolkit]]", "[[02 - YAML Frontmatter Standard]]", "[[06 - CLI Standard]]", "[[07 - Automation Standard]]"]
related_research_programs: []
---

# Tool 002 - YAML Validator

## Purpose

The YAML Validator scans Markdown notes for frontmatter compliance with [[02 - YAML Frontmatter Standard]] and generates a draft metadata validation report.

It is narrower than [[Tool 001 - Vault Validator]]. It focuses only on metadata quality.

Template files are template-aware: approved placeholders such as `YYYY-MM-DD`, `<TITLE>`, `<AUTHOR>`, and `{{value}}` are accepted in template contexts without weakening validation for operational documents.

---

## Dependencies

- Python 3 standard library
- [[02 - YAML Frontmatter Standard]]
- [[Tool 001 - Vault Validator]]

---

## Version

| Field | Value |
|-------|-------|
| **Version** | 0.1.1 |
| **Status** | active |
| **Last Updated** | 2026-07-02 |

---

## Author

[[CODEX]]

---

## Related Documents

- [[Alpha Proxima Engineering Toolkit]]
- [[02 - YAML Frontmatter Standard]]
- [[06 - CLI Standard]]
- [[07 - Automation Standard]]

---

## Related Research Programs

- N/A

---

## Implementation Notes

The CLI lives at `08_SYSTEMS/Engineering Toolkit/yaml_validator.py`.

The validator is report-only. It does not edit frontmatter, approve metadata, or determine canonical status.

Template awareness applies only to notes stored in approved template locations, files named `* Template.md`, or notes identified as templates through frontmatter. Operational documents remain subject to normal date, status, version, and title checks.

---

## CLI Interface

```bash
python3 "08_SYSTEMS/Engineering Toolkit/yaml_validator.py" [options]
```

Options:

| Option | Purpose |
|--------|---------|
| `--vault PATH` | Vault root. Defaults to the current working directory. |
| `--output PATH` | Report output path. Defaults to `08_SYSTEMS/Engineering Toolkit/Reports/YAML Validation Report.md`. |
| `--include-hidden` | Include hidden folders. Hidden folders are skipped by default. |
| `--fail-on LEVEL` | Return exit code `1` when issues exist at or above `warning` or `error`. |
| `--force` | Overwrite an existing report after explicit confirmation by command flag. |

Exit codes:

| Code | Meaning |
|------|---------|
| 0 | Report generated successfully and fail threshold was not met |
| 1 | Report generated and fail threshold was met |
| 2 | Invalid arguments or unreadable vault |
| 4 | Refused to overwrite an existing report |

---

## Usage Examples

Generate the default report:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/yaml_validator.py"
```

Write a dated report:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/yaml_validator.py" --output "08_SYSTEMS/Engineering Toolkit/Reports/YAML Validation Report - 2026-07-02.md"
```

Use in an automation check:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/yaml_validator.py" --fail-on error
```

Overwrite an existing report only after review:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/yaml_validator.py" --force
```

---

## Future Improvements

- [ ] Add JSON output for downstream automation.
- [ ] Add configurable legacy baseline support.
- [ ] Add per-artifact schemas for templates, research notes, ADRs, and Future Office proposals.
- [ ] Add autofix suggestions without applying changes automatically.

---

## Context

Consistent frontmatter is the foundation for search, indexing, dashboards, validation, and automation. The YAML Validator creates a focused metadata quality loop before broader vault checks run.

---

## Core Content

### Checks

| Check | Description |
|-------|-------------|
| Missing YAML | Note does not begin with frontmatter |
| Invalid frontmatter | Unsupported frontmatter structure or invalid field names |
| Missing required metadata | Required Engineering Handbook fields are absent |
| Invalid status | Status is outside the approved values |
| Invalid date | `created`, `updated`, or `review_date` is not `YYYY-MM-DD` |
| Invalid version | `version` is not semantic versioning |
| Invalid list field | Field that should be a list is not a list |
| Deprecated field | Legacy field name should be replaced |
| Title mismatch | Frontmatter title does not match the H1 |

### Operational Boundary

The validator reports metadata quality issues. Humans or approved automation decide what to change.

---

## Open Questions

- [ ] Should legacy notes created before Engineering Handbook v1.0 use a baseline until migrated?
- [ ] Should template placeholder frontmatter be validated under a separate template schema?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.1.1 | 2026-07-02 | [[CODEX]] | Added template-aware placeholder validation without weakening operational document validation |
| 0.1.0 | 2026-07-02 | [[CODEX]] | Initial YAML Validator tool documented and implemented |
