---
title: "Tool 003 - Metadata Migration Utility"
aliases: ["Metadata Migration Utility", "Engineering Toolkit Tool 003"]
tags: [systems, engineering, toolkit, metadata, migration, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: implementation-note
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["Python 3 standard library", "[[Tool 001 - Vault Validator]]", "[[Tool 002 - YAML Validator]]"]
related_documents: ["[[Alpha Proxima Engineering Toolkit]]", "[[Metadata Migration Plan v1.0]]", "[[02 - YAML Frontmatter Standard]]"]
related_research_programs: []
---

# Tool 003 - Metadata Migration Utility

## Purpose

Plan and apply frontmatter metadata migrations to explicitly selected notes.

## Scope

This tool supports dry runs, preview reports, interactive confirmation, batch mode, rollback files, and progress reporting. It never selects migration targets implicitly.

## CLI Interface

```bash
python3 "08_SYSTEMS/Engineering Toolkit/metadata_migrator.py" --paths "path/to/note.md" --fill-required
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" migrate --paths "path/to/note.md" --fill-required
```

## Usage Examples

Dry-run preview:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" migrate --paths "Alpha Proxima Core.md" --fill-required --force
```

Apply in batch mode:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" migrate --paths-file targets.txt --fill-required --apply --batch --yes
```

Restore rollback:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" migrate --restore-rollback "08_SYSTEMS/Engineering Toolkit/Reports/metadata_migration_rollback.json"
```

## Extension Points

- Add migration profiles for artifact-specific defaults.
- Add preview diff rendering.
- Add approved field policy files.
- Add integration with future `ap metadata plan`.

## Future Improvements

- [ ] Add JSON report output.
- [ ] Add conflict detection when a file changes after preview.
- [ ] Add per-artifact metadata schemas.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial reusable metadata migration utility |
