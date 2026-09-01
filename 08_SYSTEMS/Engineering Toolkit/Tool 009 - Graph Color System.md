---
title: "Tool 009 - Graph Color System"
aliases: ["Graph Color Tool", "Obsidian Graph Color Utility", "Engineering Toolkit Tool 009"]
tags: [systems, engineering, toolkit, obsidian, graph-view, color-system, alpha-proxima]
created: 2026-07-03
updated: 2026-07-03
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: implementation-note
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["Python 3 standard library", "[[Graph View Color System]]", "[[Tool 008 - Engineering CLI]]"]
related_documents: ["[[Alpha Proxima Engineering Toolkit]]", "[[Graph View Color System]]"]
related_research_programs: []
---

# Tool 009 - Graph Color System

## Purpose

Apply the official Alpha Proxima Obsidian Graph View color groups to `.obsidian/graph.json`.

## Scope

The utility updates only the `colorGroups` section and preserves unrelated graph settings. It creates a timestamped backup before writing.

## Boundary

Close Obsidian before running this script. Obsidian may overwrite `graph.json` while open.

Do not rely on `graph.json` hot reload. Obsidian UI remains the source of truth for active graph color settings.

## CLI Interface

```bash
python3 "08_SYSTEMS/Engineering Toolkit/apply_graph_colors.py" --vault .
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" graph-colors --vault .
```

Options:

| Option | Purpose |
|--------|---------|
| `--vault PATH` | Vault root. Defaults to current working directory. |
| `--graph-file PATH` | Graph config path. Defaults to `.obsidian/graph.json`. |
| `--dry-run` | Preview without writing. |

## Usage Examples

Preview the update:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" graph-colors --vault . --dry-run
```

Apply the official color groups:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" graph-colors --vault .
```

## Implementation Notes

The script writes the groups in the official priority order defined by [[Graph View Color System]]. More specific office and charter rules appear before generic folder rules.

The backup path uses:

```text
.obsidian/graph.backup-YYYYMMDD-HHMMSS.json
```

## Future Improvements

- [ ] Export/import named graph themes.
- [ ] Generate color groups from YAML node types.
- [ ] Add institute-specific graph modes.
- [ ] Add LUMIAION-centered graph view presets.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | [[CODEX]] | Initial graph color system utility |
