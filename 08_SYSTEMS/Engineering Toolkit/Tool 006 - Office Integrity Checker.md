---
title: "Tool 006 - Office Integrity Checker"
aliases: ["Office Integrity Checker", "Engineering Toolkit Tool 006"]
tags: [systems, engineering, toolkit, operations, offices, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: implementation-note
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["Python 3 standard library", "[[Tool 001 - Vault Validator]]", "[[Office Registry]]"]
related_documents: ["[[Alpha Proxima Engineering Toolkit]]", "[[Office Integrity Report]]"]
related_research_programs: []
---

# Tool 006 - Office Integrity Checker

## Purpose

Verify whether office-related areas expose expected operational components: charter, authority, owner, relationships, standing orders, and active status.

## CLI Interface

```bash
python3 "08_SYSTEMS/Engineering Toolkit/office_integrity_checker.py" --force
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" office-check --force
```

## Usage Examples

Generate office integrity report:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" office-check --vault . --force
```

## Extension Points

- Replace text heuristics with a formal Office Registry schema.
- Add per-office required components.
- Add standing-order templates.

## Future Improvements

- [ ] Add office schema validation.
- [ ] Add registry-to-folder reconciliation.
- [ ] Add missing component scaffolds requiring human confirmation.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial office integrity checker |
