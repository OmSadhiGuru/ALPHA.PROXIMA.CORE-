---
title: "Vault Dependency Report"
aliases: ["Dependency Analyzer Report"]
tags: [systems, engineering, dependencies, graph, report, alpha-proxima]
created: 2026-07-04
updated: 2026-07-04
status: draft
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-report
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Tool 005 - Dependency Analyzer]]"]
related_documents: ["[[Alpha Proxima Engineering Toolkit]]"]
related_research_programs: []
---

# Vault Dependency Report

## Purpose

Analyze wiki links and frontmatter dependencies for graph health.

## Summary

- Vault: `/Users/Fred/Documents/Obsidian Vault`
- Generated: `2026-07-04T01:43:36-04:00`
- Notes analyzed: `205`
- Directed dependency edges: `1216`
- Broken references: `40`
- Circular references found: `50`
- Disconnected single-note clusters: `2`
- Connected clusters: `3`

## Broken References

| Source | Missing Target |
|--------|----------------|
| `03_AI_COUNCIL/AI Council Registry.md` | `[[10_TEMPLATES/]]` |
| `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | `[[ARCHIVE]]` |
| `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | `[[13 Research Graph/Concepts]]` |
| `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | `[[04 Source - Perplexity]]` |
| `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | `[[05 Source - Gemini]]` |
| `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | `[[13 Research Graph/Concepts]]` |
| `08_SYSTEMS/Automation/Vault Note Generator.md` | `[[Python 3 standard library]]` |
| `08_SYSTEMS/Engineering Toolkit/Tool 001 - Vault Validator.md` | `[[Python 3 standard library]]` |
| `08_SYSTEMS/Engineering Toolkit/Tool 002 - YAML Validator.md` | `[[Python 3 standard library]]` |
| `08_SYSTEMS/Engineering Toolkit/Tool 003 - Metadata Migration Utility.md` | `[[Metadata Migration Plan v1.0]]` |
| `08_SYSTEMS/Engineering Toolkit/Tool 003 - Metadata Migration Utility.md` | `[[Python 3 standard library]]` |
| `08_SYSTEMS/Engineering Toolkit/Tool 004 - Vault Statistics Generator.md` | `[[Engineering Dashboard Report]]` |
| `08_SYSTEMS/Engineering Toolkit/Tool 004 - Vault Statistics Generator.md` | `[[Python 3 standard library]]` |
| `08_SYSTEMS/Engineering Toolkit/Tool 005 - Dependency Analyzer.md` | `[[Vault Dependency Report]]` |
| `08_SYSTEMS/Engineering Toolkit/Tool 005 - Dependency Analyzer.md` | `[[Python 3 standard library]]` |
| `08_SYSTEMS/Engineering Toolkit/Tool 006 - Office Integrity Checker.md` | `[[Office Integrity Report]]` |
| `08_SYSTEMS/Engineering Toolkit/Tool 006 - Office Integrity Checker.md` | `[[Python 3 standard library]]` |
| `08_SYSTEMS/Engineering Toolkit/Tool 007 - Research Integrity Checker.md` | `[[Research Integrity Report]]` |
| `08_SYSTEMS/Engineering Toolkit/Tool 007 - Research Integrity Checker.md` | `[[Python 3 standard library]]` |
| `08_SYSTEMS/Engineering Toolkit/Tool 008 - Engineering CLI.md` | `[[Python 3 standard library]]` |
| `08_SYSTEMS/Engineering Toolkit/Tool 009 - Graph Color System.md` | `[[Python 3 standard library]]` |
| `08_SYSTEMS/Institutional Knowledge Graph/Engineering Program EP-001 - Institutional Knowledge Graph.md` | `[[Vault Dependency Report]]` |
| `08_SYSTEMS/Institutional Knowledge Graph/Graph Readiness Assessment.md` | `[[Vault Dependency Report]]` |
| `08_SYSTEMS/Institutional Knowledge Graph/Graph Readiness Assessment.md` | `[[Engineering Dashboard Report]]` |
| `08_SYSTEMS/Institutional Knowledge Graph/Graph Readiness Assessment.md` | `[[Vault Dependency Report]]` |
| `08_SYSTEMS/Institutional Knowledge Graph/Graph Readiness Assessment.md` | `[[Engineering Dashboard Report]]` |
| `08_SYSTEMS/Institutional Knowledge Graph/Tools/Relationship Registry Report.md` | `[[Metadata Migration Plan v1.0]]` |
| `08_SYSTEMS/Institutional Knowledge Graph/Tools/Relationship Registry Report.md` | `[[Engineering Dashboard Report]]` |
| `08_SYSTEMS/Institutional Knowledge Graph/Tools/Relationship Registry Report.md` | `[[Vault Dependency Report]]` |
| `08_SYSTEMS/Institutional Knowledge Graph/Tools/Relationship Registry Report.md` | `[[Office Integrity Report]]` |
| `08_SYSTEMS/Institutional Knowledge Graph/Tools/Relationship Registry Report.md` | `[[Research Integrity Report]]` |
| `08_SYSTEMS/Institutional Knowledge Graph/Tools/Relationship Registry Report.md` | `[[Vault Dependency Report]]` |
| `08_SYSTEMS/Institutional Knowledge Graph/Tools/Relationship Registry Report.md` | `[[Engineering Dashboard Report]]` |
| `08_SYSTEMS/Institutional Knowledge Graph/Tools/Relationship Registry Report.md` | `[[node_registry.json]]` |
| `08_SYSTEMS/Institutional Knowledge Graph/Tools/Tool 010 - Node Registry Generator.md` | `[[node_registry.json]]` |
| `08_SYSTEMS/Institutional Knowledge Graph/Tools/Tool 010 - Node Registry Generator.md` | `[[Python 3 standard library]]` |
| `08_SYSTEMS/Institutional Knowledge Graph/Tools/Tool 011 - Relationship Extractor.md` | `[[Python 3 standard library]]` |
| `99_ARCHIVE/Engineering Cleanup/ES-002 Metadata Migration Phase 1/06 Source - SanaLab.md` | `[[ES-001 - SanaLab Root File Assessment]]` |
| `ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/Building achitecture/LUMIAION VAULT.md` | `[[ALPHA_PROXIMA_VAULT.canvas]]` |
| `ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/Building achitecture/LUMIAION VAULT.md` | `[[ALPHA_PROXIMA_VAULT.canvas]]` |

## Circular References

| Cycle |
|-------|
| `00_CONSTITUTION/Book I - The Constitution.md` -> `LUMIAION.md` -> `00_CONSTITUTION/Book I - The Constitution.md` |
| `LUMIAION.md` -> `10_TEMPLATES/Concept Note Template.md` -> `LUMIAION.md` |
| `00_CONSTITUTION/Book I - The Constitution.md` -> `LUMIAION.md` -> `10_TEMPLATES/Concept Note Template.md` -> `00_CONSTITUTION/Book I - The Constitution.md` |
| `LUMIAION.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `LUMIAION.md` |
| `00_CONSTITUTION/Book I - The Constitution.md` -> `LUMIAION.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `00_CONSTITUTION/Book I - The Constitution.md` |
| `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `10_TEMPLATES/Concept Note Template.md` |
| `LUMIAION.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `Alpha Proxima Core.md` -> `LUMIAION.md` |
| `00_CONSTITUTION/Book I - The Constitution.md` -> `LUMIAION.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `Alpha Proxima Core.md` -> `00_CONSTITUTION/Book I - The Constitution.md` |
| `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `Alpha Proxima Core.md` -> `10_TEMPLATES/Concept Note Template.md` |
| `LUMIAION.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `Alpha Proxima Core.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `LUMIAION.md` |
| `00_CONSTITUTION/Book I - The Constitution.md` -> `LUMIAION.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `Alpha Proxima Core.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `00_CONSTITUTION/Book I - The Constitution.md` |
| `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `Alpha Proxima Core.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `10_TEMPLATES/Concept Note Template.md` |
| `03_AI_COUNCIL/Institutional Registry.md` -> `Alpha Proxima Core.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `03_AI_COUNCIL/Institutional Registry.md` |
| `Alpha Proxima Core.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `Alpha Proxima Core.md` |
| `LUMIAION.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `Alpha Proxima Core.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `LUMIAION.md` |
| `00_CONSTITUTION/Book I - The Constitution.md` -> `LUMIAION.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `Alpha Proxima Core.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `00_CONSTITUTION/Book I - The Constitution.md` |
| `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `Alpha Proxima Core.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `10_TEMPLATES/Concept Note Template.md` |
| `10_TEMPLATES/Vault Structure Convention.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `10_TEMPLATES/Vault Structure Convention.md` |
| `03_AI_COUNCIL/Institutional Registry.md` -> `Alpha Proxima Core.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `03_AI_COUNCIL/Institutional Registry.md` |
| `Alpha Proxima Core.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `Alpha Proxima Core.md` |
| `03_AI_COUNCIL/Alpha Council.md` -> `03_AI_COUNCIL/Alpha Council.md` |
| `LUMIAION.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `Alpha Proxima Core.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `10_TEMPLATES/ADR Template.md` -> `LUMIAION.md` |
| `00_CONSTITUTION/Book I - The Constitution.md` -> `LUMIAION.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `Alpha Proxima Core.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `10_TEMPLATES/ADR Template.md` -> `00_CONSTITUTION/Book I - The Constitution.md` |
| `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `Alpha Proxima Core.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `10_TEMPLATES/ADR Template.md` -> `10_TEMPLATES/Concept Note Template.md` |
| `03_AI_COUNCIL/Institutional Registry.md` -> `Alpha Proxima Core.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `10_TEMPLATES/ADR Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` |
| `Alpha Proxima Core.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `10_TEMPLATES/ADR Template.md` -> `Alpha Proxima Core.md` |
| `03_AI_COUNCIL/Alpha Council.md` -> `10_TEMPLATES/ADR Template.md` -> `03_AI_COUNCIL/Alpha Council.md` |
| `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` -> `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` -> `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` |
| `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` -> `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` -> `08_SYSTEMS/Engineering Standards/01 - Markdown Style Guide.md` -> `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` |
| `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` -> `08_SYSTEMS/Engineering Standards/01 - Markdown Style Guide.md` -> `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` |
| `10_TEMPLATES/Vault Structure Convention.md` -> `11_OPERATIONS/README.md` -> `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` -> `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` -> `08_SYSTEMS/Engineering Standards/01 - Markdown Style Guide.md` -> `10_TEMPLATES/Vault Structure Convention.md` |
| `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` -> `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` -> `08_SYSTEMS/Engineering Standards/01 - Markdown Style Guide.md` -> `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` -> `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` |
| `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` -> `08_SYSTEMS/Engineering Standards/01 - Markdown Style Guide.md` -> `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` -> `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` |
| `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` -> `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` -> `08_SYSTEMS/Engineering Standards/01 - Markdown Style Guide.md` -> `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` -> `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` -> `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` |
| `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` -> `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` -> `08_SYSTEMS/Engineering Standards/01 - Markdown Style Guide.md` -> `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` -> `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` -> `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` -> `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` |
| `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` -> `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` -> `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` |
| `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` -> `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` -> `08_SYSTEMS/Engineering Standards/01 - Markdown Style Guide.md` -> `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` -> `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` -> `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` -> `08_SYSTEMS/Engineering Standards/08 - Logging Standard.md` -> `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` |
| `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` -> `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` -> `08_SYSTEMS/Engineering Standards/08 - Logging Standard.md` -> `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` |
| `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` -> `08_SYSTEMS/Engineering Standards/08 - Logging Standard.md` -> `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` |
| `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` -> `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` -> `08_SYSTEMS/Engineering Standards/01 - Markdown Style Guide.md` -> `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` -> `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` -> `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` -> `08_SYSTEMS/Engineering Standards/08 - Logging Standard.md` -> `08_SYSTEMS/Engineering Standards/09 - Git Standard.md` -> `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` |
| `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` -> `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` -> `08_SYSTEMS/Engineering Standards/08 - Logging Standard.md` -> `08_SYSTEMS/Engineering Standards/09 - Git Standard.md` -> `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` |
| `10_TEMPLATES/Vault Structure Convention.md` -> `11_OPERATIONS/README.md` -> `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` -> `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` -> `08_SYSTEMS/Engineering Standards/01 - Markdown Style Guide.md` -> `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` -> `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` -> `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` -> `08_SYSTEMS/Engineering Standards/08 - Logging Standard.md` -> `08_SYSTEMS/Engineering Standards/09 - Git Standard.md` -> `10_TEMPLATES/Vault Structure Convention.md` |
| `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` -> `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` -> `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` -> `08_SYSTEMS/Engineering Standards/08 - Logging Standard.md` -> `08_SYSTEMS/Engineering Standards/09 - Git Standard.md` -> `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` |
| `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` -> `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` -> `08_SYSTEMS/Engineering Standards/01 - Markdown Style Guide.md` -> `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` -> `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` -> `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` -> `08_SYSTEMS/Engineering Standards/08 - Logging Standard.md` -> `08_SYSTEMS/Engineering Standards/09 - Git Standard.md` -> `08_SYSTEMS/Engineering Standards/10 - Template Standard.md` -> `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` |
| `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` -> `08_SYSTEMS/Engineering Standards/01 - Markdown Style Guide.md` -> `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` -> `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` -> `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` -> `08_SYSTEMS/Engineering Standards/08 - Logging Standard.md` -> `08_SYSTEMS/Engineering Standards/09 - Git Standard.md` -> `08_SYSTEMS/Engineering Standards/10 - Template Standard.md` -> `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` |
| `08_SYSTEMS/Engineering Standards/01 - Markdown Style Guide.md` -> `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` -> `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` -> `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` -> `08_SYSTEMS/Engineering Standards/08 - Logging Standard.md` -> `08_SYSTEMS/Engineering Standards/09 - Git Standard.md` -> `08_SYSTEMS/Engineering Standards/10 - Template Standard.md` -> `08_SYSTEMS/Engineering Standards/01 - Markdown Style Guide.md` |
| `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `Alpha Proxima Core.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `11_OPERATIONS/README.md` -> `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` -> `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` -> `08_SYSTEMS/Engineering Standards/01 - Markdown Style Guide.md` -> `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` -> `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` -> `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` -> `08_SYSTEMS/Engineering Standards/08 - Logging Standard.md` -> `08_SYSTEMS/Engineering Standards/09 - Git Standard.md` -> `08_SYSTEMS/Engineering Standards/10 - Template Standard.md` -> `10_TEMPLATES/Concept Note Template.md` |
| `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` -> `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` -> `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` -> `08_SYSTEMS/Engineering Standards/08 - Logging Standard.md` -> `08_SYSTEMS/Engineering Standards/09 - Git Standard.md` -> `08_SYSTEMS/Engineering Standards/10 - Template Standard.md` -> `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` |
| `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` -> `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` -> `08_SYSTEMS/Engineering Standards/01 - Markdown Style Guide.md` -> `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` -> `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` -> `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` -> `08_SYSTEMS/Engineering Standards/08 - Logging Standard.md` -> `08_SYSTEMS/Engineering Standards/09 - Git Standard.md` -> `08_SYSTEMS/Engineering Standards/10 - Template Standard.md` -> `08_SYSTEMS/Engineering Standards/03 - Folder Naming Convention.md` -> `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` |
| `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` -> `08_SYSTEMS/Engineering Standards/01 - Markdown Style Guide.md` -> `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` -> `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` -> `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` -> `08_SYSTEMS/Engineering Standards/08 - Logging Standard.md` -> `08_SYSTEMS/Engineering Standards/09 - Git Standard.md` -> `08_SYSTEMS/Engineering Standards/10 - Template Standard.md` -> `08_SYSTEMS/Engineering Standards/03 - Folder Naming Convention.md` -> `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` |

## Largest Clusters

| Size | Example Notes |
|------|---------------|
| `203` | `00_CONSTITUTION/Book I - The Constitution.md`<br>`00_CONSTITUTION/Book II - Governance Framework.md`<br>`00_CONSTITUTION/Book III - Knowledge Integrity.md`<br>`01_VISION/Alpha Proxima — 10 Year Vision.md`<br>`03_AI_COUNCIL/AI Council Registry.md` |
| `1` | `Sans titre.md` |
| `1` | `Vault.md` |

## Implementation Notes

Circular references are not automatically errors. They identify dependency loops that may need human review.

## Future Improvements

- [ ] Add graph export formats.
- [ ] Add dependency severity rules.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-04 | [[CODEX]] | Dependency report generated |
