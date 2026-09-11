---
title: "Validation Debt Policy"
aliases: ["Vault Validation Baseline", "Validation Debt"]
tags: [systems, engineering, validation, debt, alpha-proxima]
created: 2026-09-05
updated: 2026-09-05
status: active
version: "1.0.0"
authors: ["Founder", "CODEX (CF-07)"]
artifact_type: engineering-policy
institutional_owner: "Engineering Office"
cognitive_function: "Engineering Intelligence"
reasoning_engine: "CODEX"
dependencies: ["[[Tool 001 - Vault Validator]]"]
related_documents: ["[[Engineering Office Charter]]"]
related_research_programs: []
---

# Validation Debt Policy

The Vault Validator reports all issues. A reviewed baseline records inherited debt so CI fails only on regressions. The baseline is evidence, not an exclusion list: reports always show total debt and new issues separately.

Use `--write-baseline` only after review. Use `--baseline ... --fail-on error` for operational CI. Remove signatures from the baseline only when the underlying document is repaired; never add a new defect merely to make CI pass.
