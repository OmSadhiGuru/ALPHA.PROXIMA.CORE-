---
title: "Tool 007 - Research Integrity Checker"
aliases: ["Research Integrity Checker", "Engineering Toolkit Tool 007"]
tags: [systems, engineering, toolkit, research, integrity, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: implementation-note
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["Python 3 standard library", "[[Tool 001 - Vault Validator]]", "[[Research Governance Protocol]]"]
related_documents: ["[[Alpha Proxima Engineering Toolkit]]", "[[Research Integrity Report]]"]
related_research_programs: []
---

# Tool 007 - Research Integrity Checker

## Purpose

Verify whether research program folders contain expected structural artifacts: master index, canonical synthesis, evidence registry, source notes, source registry, and cross links.

## CLI Interface

```bash
python3 "08_SYSTEMS/Engineering Toolkit/research_integrity_checker.py" --force
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" research-check --force
```

## Usage Examples

Generate research integrity report:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" research-check --vault . --force
```

## Extension Points

- Add research phase schemas.
- Add source-to-claim traceability scoring.
- Add RP artifact generation hooks.

## Future Improvements

- [ ] Add phase-aware validation.
- [ ] Add missing component preview generation.
- [ ] Integrate with Research Artifact Creator.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial research integrity checker |
