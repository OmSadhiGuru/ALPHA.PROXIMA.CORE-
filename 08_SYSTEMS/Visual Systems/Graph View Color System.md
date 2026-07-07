---
title: "Graph View Color System"
aliases: ["Obsidian Graph Color System", "Alpha Proxima Graph Colors"]
tags: [systems, visual-systems, obsidian, graph-view, color-system, alpha-proxima]
created: 2026-07-03
updated: 2026-07-07
status: active
version: "1.1.0"
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
| 1 | `path:09_OFFICES/LUMIAION OR file:LUMIAION` | LUMIAION Violet | `#7C3AED` | Central orchestration intelligence and primary institutional consciousness — the brain. This is the anchor color; every other rule below exists to keep everything *around* the brain identifiable so the brain itself stays visually distinct rather than lost in a field of uncolored nodes. |
| 2 | `path:"11_OPERATIONS/Executive Office"` | Executive Amber | `#D97706` | Executive coordination and strategic direction |
| 3 | `path:"03_AI_COUNCIL/Research Council"` | Research Emerald | `#059669` | Research intelligence and evidence intake |
| 4 | `path:"08_SYSTEMS/Engineering Toolkit" OR path:"08_SYSTEMS/Engineering Standards"` | Engineering Orange | `#EA580C` | Implementation, tooling, infrastructure, and automation |
| 5 | `path:"11_OPERATIONS/Institutional Observatory"` | Observatory Cyan | `#0891B2` | Monitoring, synthesis observation, and institutional awareness |
| 6 | `file:"Ethics Council Charter"` | Ethics Crimson | `#BE123C` | Ethics authority and moral review |
| 7 | `file:"SOHMA Charter"` | SOHMA Purple | `#9333EA` | Consciousness, meaning, and interiority |
| 8 | `file:"ATHENA Charter"` | ATHENA Blue | `#1D4ED8` | Knowledge, reasoning, and strategic intelligence |
| 9 | `file:"VORTEX Charter"` | VORTEX Green | `#65A30D` | Finance, economics, and strategic resource flow |
| 10 | `file:"JERANIUM Charter"` | JERANIUM Teal | `#0F766E` | Research intelligence and scientific integration |
| 11 | `path:00_CONSTITUTION` | Constitutional Gold | `#F59E0B` | Constitutional authority and foundational law |
| 12 | `path:07_RESEARCH` | Research Green | `#16A34A` | Research programs, evidence, synthesis, and knowledge development |
| 13 | `path:06_GOVERNANCE` | Governance Blue | `#0369A1` | Governance bodies, standards, and review authority |
| 14 | `path:08_SYSTEMS` | Systems Burnt Orange | `#C2410C` | Systems architecture, engineering standards, and infrastructure (catch-all for everything under 08_SYSTEMS not already caught by rule 4) |
| 15 | `path:03_AI_COUNCIL` | AI Council Teal | `#0D9488` | AI council, reasoning engines, and cognitive offices (catch-all for everything under 03_AI_COUNCIL not already caught by rule 3) |
| 16 | `path:04_DECISIONS` | Decision Rose | `#E11D48` | ADRs, decisions, and institutional commitments |
| 17 | `path:01_VISION OR path:02_STRATEGY` | Vision Magenta | `#C026D3` | Vision, strategy, long horizon direction |
| 18 | `path:10_TEMPLATES` | Template Slate | `#64748B` | Reusable scaffolds and document patterns |
| 19 | `path:99_ARCHIVE` | Archive Stone | `#57534E` | Preserved history, deprecated artifacts, and archived records |
| 20 | `path:05_PROPOSALS` | Proposal Indigo | `#4F46E5` | Concept Notes awaiting or undergoing Council deliberation |
| 21 | `path:06_PROJECTS` | Project Sky | `#0EA5E9` | Active project workspaces |
| 22 | `path:09_FUTURE` | Future Pink | `#EC4899` | Future proposals, technology watch, and ideas preserved until mature |
| 23 | `path:09_PEOPLE` | People Copper | `#92400E` | Participant profiles and roles |
| 24 | `path:11_OPERATIONS` | Operations Charcoal | `#1E293B` | The operational nervous system generally — catch-all for every 11_OPERATIONS subfolder not already caught by rules 2 or 5 (Office Registry, Workflow Registry, Dashboards, Review Cycles, and the rest) |
| 25 | `path:"ALPHA PROXIMA"` | Alpha Proxima Bronze | `#A16207` | Root-level cross-cutting Alpha Proxima meta-notes (Notion Command Center, vault-level indexes) that sit outside the numbered folder structure |
| 26 | `path:OSG_LAUNCH` | OSG Forest | `#14532D` | The OSG launch initiative — its own project namespace (courses, clients, media, academy), parallel to the numbered Alpha Proxima structure |

Rules 20-26 close gaps found during the 2026-07-07 audit: `09_OFFICES` never existed as a real folder (offices live under `11_OPERATIONS`), so rules 2-5 were pointing at dead paths and every 11_OPERATIONS subfolder — including [[LUMIAION - Operating Manual (LOOM)]]'s own home in Workflow Registry — rendered with no color at all. Rules 3 and 4 (Research Intelligence Office, Engineering Office) still lack a dedicated `11_OPERATIONS` subfolder the way Executive Office and Institutional Observatory have; they are pointed at the closest real institutional anchor for now (see Open Questions).

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
- [ ] Create dedicated `11_OPERATIONS/Research Intelligence Office/` and `11_OPERATIONS/Engineering Office/` subfolders (mirroring Executive Office and Institutional Observatory) so rules 3 and 4 can point at real operational homes instead of the closest available proxy.
- [ ] Re-audit this list any time a new top-level folder is added to the vault — a new folder with no matching rule falls through uncolored and dilutes the graph's readability around [[LUMIAION]].

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | [[CODEX]] | Initial Alpha Proxima Obsidian Graph View color system |
| 1.1.0 | 2026-07-07 | Founder / LUMIAION | Full audit: fixed rules 2-5, which pointed at a `09_OFFICES` path that never existed (every `11_OPERATIONS` subfolder was rendering uncolored). Added rules 20-26 for `05_PROPOSALS`, `06_PROJECTS`, `09_FUTURE`, `09_PEOPLE`, a generic `11_OPERATIONS` catch-all, `ALPHA PROXIMA`, and `OSG_LAUNCH` — every real top-level folder in the vault now resolves to a color group. `Tags/` and `copilot/` were left uncolored deliberately: they are Obsidian plugin data, not institutional content. |
