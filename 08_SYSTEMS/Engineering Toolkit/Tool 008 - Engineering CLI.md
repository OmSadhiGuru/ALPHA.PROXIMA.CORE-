---
title: "Tool 008 - Engineering CLI"
aliases: ["Alpha Proxima CLI", "Engineering CLI", "ap CLI", "Engineering Toolkit Tool 008"]
tags: [systems, engineering, toolkit, cli, alpha-proxima]
created: 2026-07-02
updated: 2026-07-03
status: active
version: "1.0.2"
authors: ["CODEX"]
artifact_type: implementation-note
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["Python 3 standard library", "[[06 - CLI Standard]]"]
related_documents: ["[[Alpha Proxima Engineering Toolkit]]"]
related_research_programs: []
---

# Tool 008 - Engineering CLI

## Purpose

Provide one unified command interface for the Engineering Toolkit.

## CLI Interface

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" <command> [options]
```

## Commands

| Command | Tool |
|---------|------|
| `validate` | [[Tool 001 - Vault Validator]] |
| `yaml` | [[Tool 002 - YAML Validator]] |
| `migrate` | [[Tool 003 - Metadata Migration Utility]] |
| `stats` | [[Tool 004 - Vault Statistics Generator]] |
| `report` | Alias for `stats` |
| `dependency-map` | [[Tool 005 - Dependency Analyzer]] |
| `office-check` | [[Tool 006 - Office Integrity Checker]] |
| `research-check` | [[Tool 007 - Research Integrity Checker]] |
| `research-management` | [[Research Management Toolkit v1.0]] |
| `graph-colors` | [[Tool 009 - Graph Color System]] |
| `node-registry` | [[Tool 010 - Node Registry Generator]] |

## Usage Examples

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" validate --force
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" stats --force
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" dependency-map --force
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" research-management --force
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" graph-colors --vault . --dry-run
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" node-registry --vault . --force
```

## Extension Points

- Register future tools in `COMMANDS`.
- Add shell wrapper installation later.
- Add command aliases for daily engineering audits.

## Future Improvements

- [ ] Add `ap health`.
- [ ] Add `ap audit`.
- [ ] Add `ap export`.
- [ ] Add installable package metadata.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.2 | 2026-07-03 | [[CODEX]] | Added graph-colors and node-registry commands |
| 1.0.1 | 2026-07-02 | [[CODEX]] | Added research-management command for ES-004 |
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial unified Engineering CLI |
