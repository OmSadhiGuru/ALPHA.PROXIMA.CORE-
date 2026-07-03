---
title: "Graph View Color System"
aliases: ["Obsidian Graph Color System", "Alpha Proxima Graph Colors"]
tags: [systems, visual-systems, obsidian, graph-view, color-system, alpha-proxima]
created: 2026-07-03
updated: 2026-07-03
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: visual-system-standard
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Alpha Proxima Engineering Toolkit]]"]
related_documents: ["[[Tool 009 - Graph Color System]]", "[[Institutional Relationship Map]]"]
related_research_programs: []
---

# Graph View Color System

## Purpose

Define the official color language of the Alpha Proxima Obsidian graph.

The graph should visually represent the Foundation as a multi-consciousness neuronal pathway. Color is part of institutional readability, not decoration.

## Philosophy

Colors are not decoration.

Colors represent institutional functions.

The graph should make Alpha Proxima readable at a glance. A contributor should be able to open the graph and immediately distinguish constitutional authority, research, governance, systems, offices, councils, decisions, templates, and archives.

The graph is not only navigation. It is the visual nervous system of Alpha Proxima.

## Color Groups

Specific office and charter rules must appear before generic folder rules.

| Priority | Query | Color Name | Hex Code | Institutional Meaning |
|----------|-------|------------|----------|-----------------------|
| 1 | `path:09_OFFICES/LUMIAION OR file:LUMIAION` | LUMIAION Violet | `#7C3AED` | Central orchestration intelligence and primary institutional consciousness |
| 2 | `path:"09_OFFICES/Executive Office"` | Executive Amber | `#D97706` | Executive coordination and strategic direction |
| 3 | `path:"09_OFFICES/Research Intelligence Office"` | Research Emerald | `#059669` | Research intelligence and evidence intake |
| 4 | `path:"09_OFFICES/Engineering Office"` | Engineering Orange | `#EA580C` | Implementation, tooling, infrastructure, and automation |
| 5 | `path:"09_OFFICES/Institutional Observatory"` | Observatory Cyan | `#0891B2` | Monitoring, synthesis observation, and institutional awareness |
| 6 | `file:"Ethics Council Charter"` | Ethics Crimson | `#BE123C` | Ethics authority and moral review |
| 7 | `file:"SOHMA Charter"` | SOHMA Purple | `#9333EA` | Consciousness, meaning, and interiority |
| 8 | `file:"ATHENA Charter"` | ATHENA Blue | `#1D4ED8` | Knowledge, reasoning, and strategic intelligence |
| 9 | `file:"VORTEX Charter"` | VORTEX Green | `#65A30D` | Finance, economics, and strategic resource flow |
| 10 | `file:"JERANIUM Charter"` | JERANIUM Teal | `#0F766E` | Research intelligence and scientific integration |
| 11 | `path:00_CONSTITUTION` | Constitutional Gold | `#F59E0B` | Constitutional authority and foundational law |
| 12 | `path:07_RESEARCH` | Research Green | `#16A34A` | Research programs, evidence, synthesis, and knowledge development |
| 13 | `path:06_GOVERNANCE` | Governance Blue | `#0369A1` | Governance bodies, standards, and review authority |
| 14 | `path:08_SYSTEMS` | Systems Burnt Orange | `#C2410C` | Systems architecture, engineering standards, and infrastructure |
| 15 | `path:03_AI_COUNCIL` | AI Council Teal | `#0D9488` | AI council, reasoning engines, and cognitive offices |
| 16 | `path:04_DECISIONS` | Decision Rose | `#E11D48` | ADRs, decisions, and institutional commitments |
| 17 | `path:01_VISION OR path:02_STRATEGY` | Vision Magenta | `#C026D3` | Vision, strategy, long horizon direction |
| 18 | `path:10_TEMPLATES` | Template Slate | `#64748B` | Reusable scaffolds and document patterns |
| 19 | `path:99_ARCHIVE` | Archive Stone | `#57534E` | Preserved history, deprecated artifacts, and archived records |

## Layer Rules

Obsidian Graph View applies the first matching color group.

Specific office rules must appear above generic folder rules. For example, a LUMIAION office rule must appear before a broad systems or council rule if both could match the same note.

Rule order is part of the color system. Reordering groups changes the institutional visual language.

## Manual Setup Instructions

1. Open Obsidian.
2. Open Graph View.
3. Open the Graph View settings panel.
4. Expand the Groups or Color Groups section.
5. Add each color group in the exact priority order listed above.
6. For each group, paste the query exactly.
7. Set the color to the matching hex code.
8. Confirm that specific office and charter groups appear above generic folder groups.
9. Close and reopen Graph View if the visual layout does not refresh immediately.
10. Treat the Obsidian UI as the active source of truth for live graph color settings.

## Boundary

Do not rely on `graph.json` hot reload.

Obsidian may overwrite `.obsidian/graph.json` while open. Close Obsidian before applying automated graph color updates.

Obsidian UI remains the source of truth for active graph color settings.

## Implementation Notes

The engineering utility [[Tool 009 - Graph Color System]] can write these groups into `.obsidian/graph.json`, but the active visual state should still be verified through the Obsidian UI.

## Future Improvements

- [ ] Automated graph theme export/import.
- [ ] Node type colors from YAML.
- [ ] Institute-specific colors.
- [ ] Research Program gradients.
- [ ] LUMIAION-centered graph view.
- [ ] ATHENA/SOHMA/VORTEX/JERANIUM subgraphs.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | [[CODEX]] | Initial Alpha Proxima Obsidian Graph View color system |
