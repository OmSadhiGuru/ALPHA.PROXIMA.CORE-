---
title: "Metadata Migration Plan v1.0"
aliases: ["Metadata Migration Plan", "Frontmatter Migration Plan"]
tags: [systems, engineering, metadata, migration, validation, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: draft
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-plan
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Tool 001 - Vault Validator]]", "[[Tool 002 - YAML Validator]]", "[[02 - YAML Frontmatter Standard]]"]
related_documents: ["[[ALPHA PROXIMA ENGINEERING HANDBOOK]]", "[[Alpha Proxima Engineering Toolkit]]", "[[01 - Markdown Style Guide]]", "[[02 - YAML Frontmatter Standard]]"]
related_research_programs: []
---

# Metadata Migration Plan v1.0

## Purpose

Define a reusable strategy for migrating legacy vault metadata toward the Engineering Handbook standard without manually editing hundreds of documents or automating institutional judgment.

## Dependencies

- [[Tool 001 - Vault Validator]]
- [[Tool 002 - YAML Validator]]
- [[02 - YAML Frontmatter Standard]]
- [[03 - Folder Naming Convention]]
- [[04 - File Naming Convention]]

## Version

| Field | Value |
|-------|-------|
| Version | 1.0.0 |
| Status | draft |
| Date | 2026-07-02 |

## Author

[[CODEX]]

## Related Documents

- [[ALPHA PROXIMA ENGINEERING HANDBOOK]]
- [[Alpha Proxima Engineering Toolkit]]
- [[Tool 001 - Vault Validator]]
- [[Tool 002 - YAML Validator]]

## Related Research Programs

- N/A

## Migration Principles

- Preserve institutional continuity.
- Prefer reusable tooling over repetitive edits.
- Never infer institutional authority when metadata is ambiguous.
- Default generated or modified metadata to `draft` unless an existing status is already clear.
- Separate legacy debt from new validation regressions.
- Require human review for ownership, canonical status, governance status, and research claims.

## Migration Phases

| Phase | Scope | Objective | Automation Level |
|-------|-------|-----------|------------------|
| Phase 0 | Baseline | Capture current validation debt as a dated baseline | Automated report |
| Phase 1 | Engineering-owned documents | Bring Engineering Toolkit, reports, and standards into full compliance | Safe automation with review |
| Phase 2 | Templates | Normalize template metadata while preserving placeholders | Safe automation with template schema |
| Phase 3 | Research scaffolds | Add missing structural fields to RP indexes and scaffolds | Assisted automation with human review |
| Phase 4 | Governance and constitutional documents | Add metadata only where ownership and authority are explicit | Human-reviewed |
| Phase 5 | Legacy archive | Classify legacy files as historical, migrated, duplicate, or archive-only | Human-reviewed |
| Phase 6 | Root notes and orphan stubs | Route, archive, or remove root-level and empty artifacts | Human decision required |

## Priority Order

1. Remove active errors that block clean validation.
2. Make validators schema-aware so reports reflect real debt.
3. Migrate Engineering Office documents first because Engineering owns the tooling.
4. Migrate templates before content because templates prevent future debt.
5. Migrate research scaffolds with explicit RP identifiers.
6. Migrate governance and constitutional materials only with careful review.
7. Migrate or archive legacy documents after canonical equivalents are confirmed.

## Automation Opportunities

| Opportunity | Tooling Recommendation | Human Review Required |
|-------------|------------------------|-----------------------|
| Add missing list fields as empty lists | Metadata migration utility | No, if field is purely structural |
| Add `artifact_type` from folder and filename pattern | Metadata migration utility with preview | Yes |
| Add `institutional_owner` from folder policy | Metadata migration utility with preview | Yes |
| Normalize date formats | YAML Validator autofix suggestion mode | No, if original date is unambiguous |
| Normalize aliases | Template Generator expansion | Yes |
| Separate baseline debt from new debt | Validator baseline file | No |
| Produce per-folder migration reports | Engineering Report Generator | No |

## Validation Checkpoints

| Checkpoint | Required Evidence |
|------------|-------------------|
| Before migration | Dated Vault Validation Report and YAML Validation Report |
| After tool changes | Validator test run with no new tool errors |
| After each phase | Phase-specific report stored under Engineering Toolkit Reports |
| Before applying bulk edits | Preview report listing every target file and proposed metadata |
| After applying bulk edits | Full validation suite and diff review |
| Before closing migration | Engineering Health Report summarizing remaining debt |

## Rollback Strategy

- Use version control as the primary rollback mechanism.
- Do not run bulk metadata changes without first producing a preview report.
- Keep every phase small enough to review.
- Commit or snapshot after each accepted phase.
- If a migration introduces ambiguity, stop that phase and record a recommendation rather than applying inferred metadata.
- Never overwrite user changes or canonical documents without explicit confirmation.

## Implementation Notes

The next reusable utility should be a metadata migration planner, not an autofixer. It should read validator output, classify missing fields by file group, and generate proposed frontmatter changes for review.

Bulk edits should not begin until the planner can distinguish safe structural fields from fields that require institutional judgment.

## Future Improvements

- [ ] Add `ap metadata plan` to the future Alpha Proxima CLI.
- [ ] Add validation baselines for pre-handbook debt.
- [ ] Add per-artifact metadata schemas.
- [ ] Add dry-run frontmatter patch generation.
- [ ] Add a reviewed migration ledger.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial metadata migration strategy for ES-001 |
