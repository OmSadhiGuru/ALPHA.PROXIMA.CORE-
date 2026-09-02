---
title: "Tool 005 - Dependency Analyzer"
aliases: ["Vault Dependency Analyzer", "Engineering Toolkit Tool 005"]
tags: [systems, engineering, toolkit, dependencies, graph, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: implementation-note
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["Python 3 standard library", "[[Tool 001 - Vault Validator]]"]
related_documents: ["[[Alpha Proxima Engineering Toolkit]]", "[[Vault Dependency Report]]"]
related_research_programs: []
---

# Tool 005 - Dependency Analyzer

## Purpose

Analyze wiki links and frontmatter dependencies, then generate a Vault Dependency Report.

## CLI Interface

```bash
python3 "08_SYSTEMS/Engineering Toolkit/dependency_analyzer.py" --force
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" dependency-map --force
```

## Usage Examples

Generate dependency report:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" dependency-map --vault . --force
```

## Extension Points

- Add graph export formats.
- Add dependency severity policies.
- Add disconnected-cluster allowlists.

## Future Improvements

- [ ] Export Graphviz or JSON.
- [ ] Add cycle review workflow.
- [ ] Add dependency health scoring.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial dependency analyzer |
