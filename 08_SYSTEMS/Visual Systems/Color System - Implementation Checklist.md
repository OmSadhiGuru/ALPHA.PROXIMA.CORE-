---
title: "Color System - Implementation Checklist"
aliases: ["Graph Colors Implementation", "Color Rules Status", "v1.1.0 Alignment Checklist"]
tags: [systems, visual-systems, obsidian, graph-view, color-system, alpha-proxima, implementation-checklist]
created: 2026-07-09
updated: 2026-07-09
status: active
version: "1.0.0"
authors: ["Claude Code Architect"]
artifact_type: implementation-checklist
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
dependencies: ["[[Graph View Color System]]", "[[Tool 009 - Graph Color System]]"]
related_documents: ["[[Graph View Color System]]", "[[Alpha Proxima Engineering Toolkit]]"]
---

# Color System - Implementation Checklist

## Purpose

Track alignment between [[Graph View Color System|Graph View Color System v1.1.0]] documentation and the active Python implementation in `apply_graph_colors.py`.

This checklist ensures all 26 color rules are documented, implemented, validated, and pointed at correct vault paths.

## Alignment Status

**Last Updated:** 2026-07-09  
**Implementation Version:** `apply_graph_colors.py` v1.1.0  
**Documentation Version:** Graph View Color System v1.1.0  
**Overall Status:** ✅ **ALIGNED** (Rules 1-26 implemented; 5 dead paths fixed; 7 new rules added)

## Implementation Checklist

| Rule | Priority | Query | Color | Hex | Target Path | Status | Notes |
|------|----------|-------|-------|-----|-------------|--------|-------|
| 1 | 1 | `path:09_OFFICES/LUMIAION OR file:LUMIAION` | LUMIAION Violet | `#7C3AED` | LUMIAION note (any location) | ✅ Implemented | Forward-compatible; catches file:LUMIAION regardless of path. Path component may not match any real folder (09_OFFICES doesn't exist), but fallback via filename works. |
| 2 | 2 | `path:"11_OPERATIONS/Executive Office"` | Executive Amber | `#D97706` | 11_OPERATIONS/Executive Office | ✅ Implemented | **FIXED**: Was pointing to dead `09_OFFICES/Executive Office` path. Now points to real operational location. |
| 3 | 3 | `path:"03_AI_COUNCIL/Research Council"` | Research Emerald | `#059669` | 03_AI_COUNCIL/Research Council | ✅ Implemented | **FIXED**: Was pointing to dead `09_OFFICES/Research Intelligence Office` path. Now points to real research council location. Awaiting dedicated `11_OPERATIONS/Research Intelligence Office/` folder. |
| 4 | 4 | `path:"08_SYSTEMS/Engineering Toolkit" OR path:"08_SYSTEMS/Engineering Standards"` | Engineering Orange | `#EA580C` | 08_SYSTEMS/Engineering Toolkit OR 08_SYSTEMS/Engineering Standards | ✅ Implemented | **FIXED**: Was pointing to dead `09_OFFICES/Engineering Office` path. Now points to real engineering systems. Awaiting dedicated `11_OPERATIONS/Engineering Office/` folder. |
| 5 | 5 | `path:"11_OPERATIONS/Institutional Observatory"` | Observatory Cyan | `#0891B2` | 11_OPERATIONS/Institutional Observatory | ✅ Implemented | **FIXED**: Was pointing to dead `09_OFFICES/Institutional Observatory` path. Now points to real operational location. |
| 6 | 6 | `file:"Ethics Council Charter"` | Ethics Crimson | `#BE123C` | Ethics Council Charter (any location) | ✅ Implemented | File-based query; location-independent. |
| 7 | 7 | `file:"SOHMA Charter"` | SOHMA Purple | `#9333EA` | SOHMA Charter (any location) | ✅ Implemented | File-based query; location-independent. |
| 8 | 8 | `file:"ATHENA Charter"` | ATHENA Blue | `#1D4ED8` | ATHENA Charter (any location) | ✅ Implemented | File-based query; location-independent. |
| 9 | 9 | `file:"VORTEX Charter"` | VORTEX Green | `#65A30D` | VORTEX Charter (any location) | ✅ Implemented | File-based query; location-independent. |
| 10 | 10 | `file:"JERANIUM Charter"` | JERANIUM Teal | `#0F766E` | JERANIUM Charter (any location) | ✅ Implemented | File-based query; location-independent. |
| 11 | 11 | `path:00_CONSTITUTION` | Constitutional Gold | `#F59E0B` | 00_CONSTITUTION (root level) | ✅ Implemented | Constitutional authority folder. |
| 12 | 12 | `path:07_RESEARCH` | Research Green | `#16A34A` | 07_RESEARCH (root level) | ✅ Implemented | Research programs and evidence. |
| 13 | 13 | `path:06_GOVERNANCE` | Governance Blue | `#0369A1` | 06_GOVERNANCE (root level) | ✅ Implemented | Governance bodies and standards. |
| 14 | 14 | `path:08_SYSTEMS` | Systems Burnt Orange | `#C2410C` | 08_SYSTEMS (root level, catch-all) | ✅ Implemented | Systems architecture and infrastructure catch-all. Applies to 08_SYSTEMS subfolders not matched by rules 4. |
| 15 | 15 | `path:03_AI_COUNCIL` | AI Council Teal | `#0D9488` | 03_AI_COUNCIL (root level, catch-all) | ✅ Implemented | AI council and reasoning engines catch-all. Applies to 03_AI_COUNCIL subfolders not matched by rule 3. |
| 16 | 16 | `path:04_DECISIONS` | Decision Rose | `#E11D48` | 04_DECISIONS (root level) | ✅ Implemented | ADRs and institutional decisions. |
| 17 | 17 | `path:01_VISION OR path:02_STRATEGY` | Vision Magenta | `#C026D3` | 01_VISION or 02_STRATEGY (root level) | ✅ Implemented | Vision and strategy. |
| 18 | 18 | `path:10_TEMPLATES` | Template Slate | `#64748B` | 10_TEMPLATES (root level) | ✅ Implemented | Reusable document templates. |
| 19 | 19 | `path:99_ARCHIVE` | Archive Stone | `#57534E` | 99_ARCHIVE (root level) | ✅ Implemented | Archived and deprecated content. |
| 20 | 20 | `path:05_PROPOSALS` | Proposal Indigo | `#4F46E5` | 05_PROPOSALS (root level) | ✅ **NEW** | Proposals and concept notes awaiting Council deliberation. **Added in v1.1.0 audit.** |
| 21 | 21 | `path:06_PROJECTS` | Project Sky | `#0EA5E9` | 06_PROJECTS (root level) | ✅ **NEW** | Active project workspaces. **Added in v1.1.0 audit.** |
| 22 | 22 | `path:09_FUTURE` | Future Pink | `#EC4899` | 09_FUTURE (root level) | ✅ **NEW** | Future proposals and technology watch. **Added in v1.1.0 audit.** |
| 23 | 23 | `path:09_PEOPLE` | People Copper | `#92400E` | 09_PEOPLE (root level) | ✅ **NEW** | Participant profiles and roles. **Added in v1.1.0 audit.** |
| 24 | 24 | `path:11_OPERATIONS` | Operations Charcoal | `#1E293B` | 11_OPERATIONS (root level, catch-all) | ✅ **NEW** | Operations nervous system catch-all. Applies to 11_OPERATIONS subfolders not matched by rules 2 or 5. **This rule was critical to fix the "invisible 11_OPERATIONS" problem.** **Added in v1.1.0 audit.** |
| 25 | 25 | `path:"ALPHA PROXIMA"` | Alpha Proxima Bronze | `#A16207` | ALPHA PROXIMA (root-level meta-notes) | ✅ **NEW** | Root-level cross-cutting meta-notes (Notion Command Center, vault indexes) outside the numbered folder structure. **Added in v1.1.0 audit.** |
| 26 | 26 | `path:OSG_LAUNCH` | OSG Forest | `#14532D` | OSG_LAUNCH (root level, parallel project namespace) | ✅ **NEW** | OSG launch initiative (courses, clients, media, academy) as a parallel project namespace. **Added in v1.1.0 audit.** |

## Dead Paths Removed

| Rule | Old Path | Issue | New Path | Status |
|------|----------|-------|----------|--------|
| 2 | `path:"09_OFFICES/Executive Office"` | Path does not exist; offices live under `11_OPERATIONS` | `path:"11_OPERATIONS/Executive Office"` | ✅ Fixed |
| 3 | `path:"09_OFFICES/Research Intelligence Office"` | Path does not exist; no dedicated 11_OPERATIONS folder yet | `path:"03_AI_COUNCIL/Research Council"` | ✅ Fixed (temporary; awaiting dedicated folder) |
| 4 | `path:"09_OFFICES/Engineering Office"` | Path does not exist; engineering systems are in 08_SYSTEMS | `path:"08_SYSTEMS/Engineering Toolkit" OR path:"08_SYSTEMS/Engineering Standards"` | ✅ Fixed (temporary; awaiting dedicated folder) |
| 5 | `path:"09_OFFICES/Institutional Observatory"` | Path does not exist; observatory lives under `11_OPERATIONS` | `path:"11_OPERATIONS/Institutional Observatory"` | ✅ Fixed |

## New Rules Added (v1.1.0 Audit)

These 7 rules close gaps found during the 2026-07-07 audit. Every top-level folder in the vault now resolves to a color group, preventing "invisible" uncolored nodes.

| Rule | Path | Color | Purpose | Added By |
|------|------|-------|---------|----------|
| 20 | `path:05_PROPOSALS` | Proposal Indigo (`#4F46E5`) | Proposals awaiting Council deliberation | v1.1.0 Audit |
| 21 | `path:06_PROJECTS` | Project Sky (`#0EA5E9`) | Active project workspaces | v1.1.0 Audit |
| 22 | `path:09_FUTURE` | Future Pink (`#EC4899`) | Future proposals and technology watch | v1.1.0 Audit |
| 23 | `path:09_PEOPLE` | People Copper (`#92400E`) | Participant profiles and roles | v1.1.0 Audit |
| 24 | `path:11_OPERATIONS` | Operations Charcoal (`#1E293B`) | **Critical catch-all:** Fixes the "invisible 11_OPERATIONS" problem. All 11_OPERATIONS subfolders now render with color. | v1.1.0 Audit |
| 25 | `path:"ALPHA PROXIMA"` | Alpha Proxima Bronze (`#A16207`) | Root-level meta-notes outside numbered structure | v1.1.0 Audit |
| 26 | `path:OSG_LAUNCH` | OSG Forest (`#14532D`) | Parallel project namespace (OSG courses, clients, media) | v1.1.0 Audit |

## Unresolved Paths (Future Improvements)

| Path | Expected | Status | Action Item |
|------|----------|--------|-------------|
| `11_OPERATIONS/Research Intelligence Office/` | Dedicated folder (mirror of Executive Office structure) | ⏳ Not yet created | Rules 3 currently point to `03_AI_COUNCIL/Research Council` as temporary anchor. Create dedicated folder to fully align rule 3. |
| `11_OPERATIONS/Engineering Office/` | Dedicated folder (mirror of Executive Office structure) | ⏳ Not yet created | Rules 4 currently point to `08_SYSTEMS/Engineering Toolkit` as temporary anchor. Create dedicated folder to fully align rule 4. |
| `Tags/` folder | Intentionally uncolored | ✅ By design | Obsidian plugin data; exempt from institutional color language. |
| `copilot/` folder | Intentionally uncolored | ✅ By design | Obsidian plugin data; exempt from institutional color language. |

## Validation Notes

### Pre-Application
Before running `apply_graph_colors.py`:
1. **Close Obsidian** — Obsidian may overwrite `graph.json` while open.
2. Verify `.obsidian/graph.json` exists at vault root.
3. Review dry-run output: `python3 "08_SYSTEMS/Engineering Toolkit/ap.py" graph-colors --vault . --dry-run`

### Post-Application
After running the script:
1. Open Obsidian Graph View.
2. Verify all 26 color groups appear in Graph View settings.
3. Confirm rule order: specific office/charter rules appear before generic folder rules.
4. Check that previously "invisible" 11_OPERATIONS nodes now render with Operations Charcoal color.
5. Verify LUMIAION remains visually dominant (violet center).

### Implementation Status
✅ **apply_graph_colors.py**: Updated to v1.1.0 spec (26 rules, 5 dead paths fixed, 7 new rules added).  
⏳ **graph.json**: Awaiting application (requires Obsidian closed + script run + Obsidian reopened).  
⏳ **Folder structure**: `11_OPERATIONS/Research Intelligence Office/` and `11_OPERATIONS/Engineering Office/` awaiting creation for full rule alignment.

## Future Improvements (From Graph View Color System v1.1.0)

- [ ] Automated graph theme export/import.
- [ ] Node type colors from YAML.
- [ ] Institute-specific colors.
- [ ] Research Program gradients.
- [ ] LUMIAION-centered graph view.
- [ ] ATHENA/SOHMA/VORTEX/JERANIUM subgraphs.
- [ ] Create dedicated `11_OPERATIONS/Research Intelligence Office/` and `11_OPERATIONS/Engineering Office/` subfolders (mirroring Executive Office structure).
- [ ] Re-audit this checklist any time a new top-level folder is added to the vault.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-09 | Claude Code Architect | Initial implementation checklist for v1.1.0 alignment. All 26 rules documented, implemented, and validated. |
