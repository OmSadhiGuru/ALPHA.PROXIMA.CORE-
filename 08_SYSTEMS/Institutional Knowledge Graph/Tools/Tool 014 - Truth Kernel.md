---
title: "Tool 014 - Truth Kernel"
aliases: ["Truth Kernel", "Truth Kernel Builder"]
tags: [systems, engineering, truth-kernel, knowledge-graph, tool, alpha-proxima]
created: 2026-09-03
updated: 2026-09-03
status: draft
version: "0.1.0"
authors: ["CODEX"]
artifact_type: implementation-note
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["Python 3 standard library", "[[Truth Kernel Node Contract v0.1]]", "[[Tool 010 - Node Registry Generator]]", "[[Tool 011 - Relationship Extractor]]"]
related_documents: ["[[Alpha Proxima App Architecture v1]]", "[[Graph Readiness Assessment]]"]
related_research_programs: []
tool_id: "TOOL-014"
---

# Tool 014 - Truth Kernel

## Purpose

Build one deterministic, read-only contract over Alpha Proxima nodes, relationships, unresolved targets, health, and validation findings.

## CLI

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" truth-kernel \
  --vault . \
  --output-dir /tmp/alpha-proxima-truth-kernel \
  --force
```

## Outputs

- `node_registry.json`
- `relationship_registry.json`
- `truth-kernel.json`
- `Graph Validation Report.md`

The default output is `.alpha-proxima/generated/truth-kernel`, which is excluded by the standard hidden-directory scan rule. Passing a temporary output directory is recommended for verification.

## Interface contract

The Alpha Proxima App includes the Truth Kernel summary in `/api/app` and exposes:

- `/api/v1/truth-kernel`
- `/api/v1/nodes`
- `/api/v1/relationships`
- `/api/v1/validation`
- `/api/v1/health`

All endpoints are read-only and remain loopback-only under FD-002.

## Verification

Run:

```bash
python3 "08_SYSTEMS/Institutional Knowledge Graph/Tools/test_truth_kernel.py"
python3 "08_SYSTEMS/Engineering Toolkit/test_alpha_app.py"
```

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 0.1.0 | 2026-09-03 | CODEX | First integrated read-only Truth Kernel builder and interface contract |
