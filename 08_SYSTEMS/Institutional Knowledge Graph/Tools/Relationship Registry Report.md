---
title: "Relationship Registry Report"
aliases: ["Institutional Knowledge Graph Relationship Registry Report"]
tags: [systems, engineering, knowledge-graph, relationships, report, alpha-proxima]
created: 2026-09-04
updated: 2026-09-04
status: draft
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-report
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Tool 011 - Relationship Extractor]]", "[[Relationship Taxonomy]]", "[[Tool 010 - Node Registry Generator]]"]
related_documents: ["[[Engineering Program EP-001 - Institutional Knowledge Graph]]", "[[Relationship Taxonomy]]", "[[Node Registry Report]]"]
related_research_programs: []
---

# Relationship Registry Report

## Purpose

Summarize candidate graph relationships extracted by [[Tool 011 - Relationship Extractor]].

## Summary

- Vault: `/Users/Fred/Documents/Obsidian Vault`
- Generated: `2026-09-04T11:19:47-04:00`
- Total relationships discovered: `2652`
- Low-confidence relationships: `163`
- Broken or unresolved links: `735`

## Relationships by Type

| Relationship Type | Count |
|-------------------|-------|
| `REFERENCES` | `1598` |
| `RELATED_TO` | `483` |
| `REQUIRES` | `302` |
| `PART_OF` | `159` |
| `PRODUCED_BY` | `93` |
| `IMPLEMENTS` | `11` |
| `EXTENDS` | `2` |
| `SUPERSEDES` | `2` |
| `SUPPORTS` | `2` |

## Relationships by Source

| Source | Count |
|--------|-------|
| `wiki_link` | `1600` |
| `yaml_field` | `880` |
| `folder_inference` | `159` |
| `filename_inference` | `13` |

## Low-Confidence Relationships

| Type | Source Path | Target | Confidence | Relationship Source |
|------|-------------|--------|------------|---------------------|
| `EXTENDS` | `07_RESEARCH/RP-002/21 Version History/RP-002 Version History.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.45` | `filename_inference` |
| `EXTENDS` | `07_RESEARCH/RP-001/21 Version History/RP-001 Version History.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.45` | `filename_inference` |
| `PART_OF` | `13_OPERATIONS/Weekly Operations/Weekly Operations Index.md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Collective Memory.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/13 Research Graph/RP-002 Research Graph.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `08_SYSTEMS/Research Management Toolkit/Templates/Research Timeline Template.md` | `08_SYSTEMS/Research Management Toolkit/Research Management Toolkit v1.0.md` | `0.55` | `folder_inference` |
| `PART_OF` | `08_SYSTEMS/Engineering Toolkit/Tool 004 - Vault Statistics Generator.md` | `08_SYSTEMS/Engineering Toolkit/Alpha Proxima Engineering Toolkit.md` | `0.55` | `folder_inference` |
| `PART_OF` | `13_OPERATIONS/Alpha Proxima App/README.md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `14_FUTURE/Templates/Upgrade Proposal Template.md` | `14_FUTURE/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `13_OPERATIONS/Workflow Registry/Workflow Registry.md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `14_FUTURE/Templates/Future Templates Index.md` | `14_FUTURE/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `14_FUTURE/Technology Watch/Technology Watch Index.md` | `14_FUTURE/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `08_SYSTEMS/Engineering Toolkit/Tool 012 - Founder OS State Engine.md` | `08_SYSTEMS/Engineering Toolkit/Alpha Proxima Engineering Toolkit.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/11 Canonical Glossary/RP-001 Canonical Glossary.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `08_SYSTEMS/Research Management Toolkit/Templates/Canonical Synthesis Template.md` | `08_SYSTEMS/Research Management Toolkit/Research Management Toolkit v1.0.md` | `0.55` | `folder_inference` |
| `PART_OF` | `08_SYSTEMS/Engineering Toolkit/OSG Reading Color CSS Guide.md` | `08_SYSTEMS/Engineering Toolkit/Alpha Proxima Engineering Toolkit.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/08 Comparative Framework/RP-001 Comparative Framework.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `08_SYSTEMS/Research Management Toolkit/Templates/Evidence Registry Template.md` | `08_SYSTEMS/Research Management Toolkit/Research Management Toolkit v1.0.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/20 Related ADRs/RP-001 ADR Links.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/11 Canonical Glossary/RP-002 Canonical Glossary.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/ARCHIVE/DOC-C RP-002 Illustrated.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/12 Evidence Registry/RP-001 Evidence Registry.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `08_SYSTEMS/Engineering Toolkit/Tool 008 - Engineering CLI.md` | `08_SYSTEMS/Engineering Toolkit/Alpha Proxima Engineering Toolkit.md` | `0.55` | `folder_inference` |
| `PART_OF` | `08_SYSTEMS/Research Management Toolkit/Templates/Research Program Template.md` | `08_SYSTEMS/Research Management Toolkit/Research Management Toolkit v1.0.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/13 Research Graph/Concepts/LTP - Synaptic Plasticity.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Contemplative Memory.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `14_FUTURE/Templates/Technology Watch Template.md` | `14_FUTURE/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `14_FUTURE/Feature Requests/Feature Requests Index.md` | `14_FUTURE/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `13_OPERATIONS/Office Registry/Office Registry.md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/05 Source - SanaLab/RP-002 Source Note - SanaLab.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `14_FUTURE/AI Recommendations/AI Recommendations Index.md` | `14_FUTURE/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `13_OPERATIONS/Operational Procedures/Minimum Viable Council Procedure.md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `09_OFFICES/Research Intelligence Office/Research Office Matrix.md` | `09_OFFICES/Research Intelligence Office/Research Intelligence Office Charter.md` | `0.55` | `folder_inference` |
| `PART_OF` | `13_OPERATIONS/Artifact Registry/Artifact Registry.md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `13_OPERATIONS/AI Council/Agent and Subagent Registry.md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `13_OPERATIONS/Automation Queue/Automation Queue Index.md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/00 Executive Summary/RP-002 Executive Summary.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `14_FUTURE/Archive/Future Archive Index.md` | `14_FUTURE/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `13_OPERATIONS/Alpha Proxima App/Alpha Proxima App Architecture v1.md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/18 Related Constitution/RP-001 Constitutional Links.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `08_SYSTEMS/Research Management Toolkit/Reports/ES-004 - Research Management Toolkit Delivery Report.md` | `08_SYSTEMS/Research Management Toolkit/Research Management Toolkit v1.0.md` | `0.55` | `folder_inference` |
| `PART_OF` | `14_FUTURE/Research Commissions/Research Commissions Index.md` | `14_FUTURE/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `14_FUTURE/Future Cognitive Functions/Future Cognitive Functions Index.md` | `14_FUTURE/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/03 Source Registry/RP-001 Source Registry.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `13_OPERATIONS/Metrics/Metrics Registry.md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `14_FUTURE/Templates/Future Proposal Template.md` | `14_FUTURE/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/19 Related Laws/RP-002 Governing Provisions.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `14_FUTURE/Roadmap/Roadmap Index.md` | `14_FUTURE/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `08_SYSTEMS/Engineering Toolkit/Tool 009 - Graph Color System.md` | `08_SYSTEMS/Engineering Toolkit/Alpha Proxima Engineering Toolkit.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/02 Objectives/RP-002 Objectives.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `08_SYSTEMS/Research Management Toolkit/Templates/Future Research Template.md` | `08_SYSTEMS/Research Management Toolkit/Research Management Toolkit v1.0.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/04 Source - Perplexity/RP-001 Source Note - Perplexity.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `14_FUTURE/Templates/Research Commission Template.md` | `14_FUTURE/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Canonical Synthesis.md` | `07_RESEARCH/RP-003/RP-003 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `13_OPERATIONS/Operational Procedures/Operational Procedures Index.md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `13_OPERATIONS/Annual Reviews/Annual Reviews Index.md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `13_OPERATIONS/Workflow Registry/LUMIAION - Operating Manual (LOOM).md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `14_FUTURE/Architectural Proposals/Architectural Proposals Index.md` | `14_FUTURE/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `08_SYSTEMS/Engineering Toolkit/Tool 013 - Alpha Proxima App.md` | `08_SYSTEMS/Engineering Toolkit/Alpha Proxima Engineering Toolkit.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/21 Version History/RP-001 Version History.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/14 Open Questions/RP-001 Open Questions.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/07 Future Sources/RP-001 Future Sources.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/07 Future Sources/RP-002 Future Sources.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/08 Comparative Framework/RP-002 Comparative Framework.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/12 Evidence Registry/RP-002 Evidence Registry.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/16 Visual Knowledge/RP-001 Visual Knowledge Index.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `13_OPERATIONS/Monthly Operations/Monthly Operations Index.md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/ARCHIVE/DOC-B Interdisciplinary Comparative Framework Memory.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Memory.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/21 Version History/RP-002 Version History.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/13 Research Graph/RP-001 Research Graph.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `08_SYSTEMS/Research Management Toolkit/Research Lifecycle Diagram.md` | `08_SYSTEMS/Research Management Toolkit/Research Management Toolkit v1.0.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/01 Research Question/RP-002 Research Question.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/01 Research Question/RP-001 Research Question.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `13_OPERATIONS/Founder OS/README.md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/06 Source - SanaLab/RP-001 Source Note - SanaLab.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `13_OPERATIONS/Review Cycles/Review Cycles Registry.md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/14 Open Questions/RP-002 Open Questions.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/ARCHIVE/ARCHIVE Philosophy.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `08_SYSTEMS/Research Management Toolkit/Templates/Open Questions Template.md` | `08_SYSTEMS/Research Management Toolkit/Research Management Toolkit v1.0.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Hippocampus.md` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `13_OPERATIONS/AI Council/MVC-001 Council Activation Record.md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `14_FUTURE/Decision Log/Decision Log Index.md` | `14_FUTURE/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `13_OPERATIONS/Operational Health/FIR-001 Repository Health Result.md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Illusionism.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `13_OPERATIONS/Operational Procedures/Founder Intent Routing Procedure.md` | `13_OPERATIONS/README.md` | `0.55` | `folder_inference` |
| `PART_OF` | `08_SYSTEMS/Research Management Toolkit/Research Index.md` | `08_SYSTEMS/Research Management Toolkit/Research Management Toolkit v1.0.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/09 Canonical Synthesis/RP-001 Canonical Synthesis.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |
| `PART_OF` | `08_SYSTEMS/Engineering Toolkit/Tool 005 - Dependency Analyzer.md` | `08_SYSTEMS/Engineering Toolkit/Alpha Proxima Engineering Toolkit.md` | `0.55` | `folder_inference` |
| `PART_OF` | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness.md` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | `0.55` | `folder_inference` |

## Unresolved by Type

| Relationship Type | Count |
|-------------------|-------|
| `PRODUCED_BY` | `302` |
| `OWNED_BY` | `199` |
| `REFERENCES` | `193` |
| `DEPENDS_ON` | `21` |
| `RELATED_TO` | `18` |
| `SUPERSEDES` | `2` |

## Broken or Unresolved Links

| Type | Source Path | Target | Relationship Source | Source Detail |
|------|-------------|--------|---------------------|---------------|
| `DEPENDS_ON` | `08_SYSTEMS/Automation/Vault Note Generator.md` | `Python 3 standard library` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `08_SYSTEMS/Engineering Toolkit/Tool 014 - Council Session Kernel.md` | `Python 3 standard library` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `08_SYSTEMS/Protocols/Future Expansion Protocol.md` | `[[Concept Note Template]]` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `08_SYSTEMS/Institutional Knowledge Graph/Graph Readiness Assessment.md` | `[[Vault Dependency Report]]` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `08_SYSTEMS/Engineering Toolkit/Tool 004 - Vault Statistics Generator.md` | `Python 3 standard library` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `08_SYSTEMS/Engineering Toolkit/Tool 006 - Office Integrity Checker.md` | `Python 3 standard library` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `08_SYSTEMS/Engineering Toolkit/Tool 009 - Graph Color System.md` | `Python 3 standard library` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `08_SYSTEMS/Institutional Knowledge Graph/Tools/Tool 011 - Relationship Extractor.md` | `Python 3 standard library` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `OSG_LAUNCH/10_ACADEMY/AIG/Awaken the Inner Guru Recording Start Guide.md` | `[[Awaken the Inner Guru Production Folder]]` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `08_SYSTEMS/Engineering Toolkit/Tool 003 - Metadata Migration Utility.md` | `Python 3 standard library` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `08_SYSTEMS/Institutional Knowledge Graph/Tools/Tool 014 - Truth Kernel.md` | `Python 3 standard library` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `08_SYSTEMS/Institutional Knowledge Graph/Tools/Tool 010 - Node Registry Generator.md` | `Python 3 standard library` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `08_SYSTEMS/Engineering Toolkit/Tool 002 - YAML Validator.md` | `Python 3 standard library` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `08_SYSTEMS/Engineering Toolkit/Tool 012 - Founder OS State Engine.md` | `Python 3 standard library` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `08_SYSTEMS/Engineering Toolkit/Tool 013 - Alpha Proxima App.md` | `Python 3 standard library` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `08_SYSTEMS/Engineering Toolkit/Tool 005 - Dependency Analyzer.md` | `Python 3 standard library` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `13_OPERATIONS/Operational Procedures/Founder Intent Routing Procedure.md` | `[[LUMIAION Charter]]` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `08_SYSTEMS/Engineering Toolkit/Tool 001 - Vault Validator.md` | `Python 3 standard library` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `08_SYSTEMS/Engineering Toolkit/Tool 007 - Research Integrity Checker.md` | `Python 3 standard library` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `08_SYSTEMS/Institutional Knowledge Graph/Graph Readiness Assessment.md` | `[[Engineering Dashboard Report]]` | `yaml_field` | `dependencies` |
| `DEPENDS_ON` | `08_SYSTEMS/Engineering Toolkit/Tool 008 - Engineering CLI.md` | `Python 3 standard library` | `yaml_field` | `dependencies` |
| `OWNED_BY` | `05_PROPOSALS/Phase III Preparation/PHASE III INSTITUTIONAL READINESS MAP.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Operational Procedures/Minimum Viable Council Procedure.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Metrics/Metrics Registry.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `14_FUTURE/Technology Watch/Technology Watch Index.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/06_AUTOMATION/README.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/04_CLIENTS/Client Folder Hierarchy.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Quarterly Reviews/Quarterly Reviews Index.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `11_OPERATIONS/Weekly Execution Plans/2026-09-03 - Truth Kernel Execution Plan.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Founder OS/Founder OS Architecture v1.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Reboot/Repository Reboot Audit - 2026-08-23.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `06_GOVERNANCE/Constitutional Impact Report/CIR-003 Epoch V Constitutional Coherence.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Protocols/Future Expansion Protocol.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Institutional Observatory/Institutional Observatory Index.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Visual Systems/Color System - Implementation Checklist.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Research Management Toolkit/Templates/Evidence Registry Template.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 2/TAG TAXONOMY.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/07_OPERATIONS/README.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Engineering Toolkit/Tool 003 - Metadata Migration Utility.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `14_FUTURE/Templates/Upgrade Proposal Template.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Office Registry/Office Registry.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Operational Health/Operational Health Index.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `12_PEOPLE/CODEX.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Annual Reviews/Annual Reviews Index.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 2/PHASE 2 - KNOWLEDGE.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `00_CONSTITUTION/Book IV - Cognitive Architecture.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 2/NAMING RULES.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 4/HOSTING OPTIONS.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Engineering Standards/03 - Folder Naming Convention.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Institutional Knowledge Graph/Tools/Node Registry Report.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Operational Health/FIR-001 Repository Health Result.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Institutional Knowledge Graph/Engineering Program EP-001 - Institutional Knowledge Graph.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `14_FUTURE/Review Queue/Review Queue Index.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `14_FUTURE/Templates/Founder Idea Template.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/10_ACADEMY/AIG/README.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `03_AI_COUNCIL/Council Node Architecture.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `00_CONSTITUTION/Book I - The Constitution.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `14_FUTURE/Roadmap/Roadmap Index.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Engineering Toolkit/Tool 002 - YAML Validator.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/09_TEMPLATES/Naming Conventions.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 3/MEMORY RULES.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/09_TEMPLATES/README.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 2/SOURCE NOTE TEMPLATE.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/09_TEMPLATES/Content Item Template.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `05_PROPOSALS/Phase III Preparation/02_STRATEGY ARCHITECTURE BLUEPRINT.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `14_FUTURE/Archive/Future Archive Index.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `11_OPERATIONS/Weekly Execution Plans/Truth Kernel Weekly QA Report - 2026-09-03.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/10_ACADEMY/README.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/08_ROADMAP/30 Day Implementation Roadmap.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Research Management Toolkit/Templates/Canonical Synthesis Template.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/ALPHAPROXIMA Enterprise Knowledge Architecture v1.0.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/AI Council/MVC-001 Council Activation Record.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Engineering Toolkit/Tool 005 - Dependency Analyzer.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/Building achitecture/ALPHA PROXIMA ROLES/ARCHITECTURE MAP.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Engineering Toolkit/Tool 012 - Founder OS State Engine.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Engineering Toolkit/OSG Reading Color CSS Guide.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/AI Council/AI Council Operations Registry.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `05_PROPOSALS/Phase III Preparation/08_SYSTEMS DRAFT TRIAGE REGISTER.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/03_MEDIA/README.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Research Management Toolkit/Templates/Future Research Template.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/README.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Executive Office/Executive Office Index.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/BUILDING MILESTONE.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Version History/Operations Version History.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `14_FUTURE/Templates/Future Proposal Template.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `06_GOVERNANCE/Epoch V/Book II Amendment — Council Topology.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 2/CONCEPT NOTE TEMPLATE.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/00_REPOSITORY/GitHub Best Practices.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Dashboards/Dashboards Index.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Institutional Knowledge Graph/Truth Kernel Node Contract v0.1.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `14_FUTURE/AI Recommendations/AI Recommendations Index.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Engineering Toolkit/Tool 009 - Graph Color System.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `12_PEOPLE/Frederick Belizaire Gunville.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 5/DAILY REVIEW LOOP.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Engineering Standards/08 - Logging Standard.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `06_GOVERNANCE/Epoch V/Consolidated Ethics Framework.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Institutional Knowledge Graph/Knowledge Graph Conventions.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/02_COURSES/Course Folder Hierarchy.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `05_PROPOSALS/Phase III Preparation/CN-0001 COUNCIL CLOSURE IMPLEMENTATION PLAN.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Operational Procedures/Founder Intent Routing Procedure.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `14_FUTURE/Architectural Proposals/Architectural Proposals Index.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `05_PROPOSALS/Constitution v2.0 Ratification Draft.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `Building Milestone.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Institutional Knowledge Graph/Tools/Tool 014 - Truth Kernel.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 3/COST TIERS.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Institutional Knowledge Graph/Tools/Tool 010 - Node Registry Generator.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `00_CONSTITUTION/Book II - Governance Framework.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/07_OPERATIONS/Launch Operations Model.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 4/MVP SPECIFICATION.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Decision Pipelines/Decision Pipelines Index.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/00_REPOSITORY/README.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Founder OS/README.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Operational Procedures/Operational Procedures Index.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Institutional Knowledge Graph/Relationship Taxonomy.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/Phase 1/PHASE 1 - FOUNDATION.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Engineering Standards/10 - Template Standard.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/README.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Founder OS/Founder Console.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Institutional Knowledge Graph/Tools/Tool 011 - Relationship Extractor.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `14_FUTURE/Templates/Technology Watch Template.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Review Cycles/Review Cycles Registry.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Research Management Toolkit/Templates/Research Program Template.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/09_TEMPLATES/Course Template.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `05_PROPOSALS/Phase III Preparation/ALPHA PROXIMA META-LAYER DECISION MEMO.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Research Management Toolkit/Research Index.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `README.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 3/PHASE 3 - INTELLIGENCE.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Research Management Toolkit/Research Lifecycle Diagram.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/05_CONTENT/Content Workflow.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Engineering Standards/07 - Automation Standard.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/09_TEMPLATES/Client Template.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Engineering Toolkit/Tool 007 - Research Integrity Checker.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `00_CONSTITUTION/Book III - Knowledge Integrity.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Engineering Toolkit/Tool 004 - Vault Statistics Generator.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/00_REPOSITORY/OSG Academy Engineering Review.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `14_FUTURE/Implementation Proposals/Implementation Proposals Index.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Research Management Toolkit/Templates/Research Timeline Template.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Engineering Toolkit/Tool 001 - Vault Validator.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `08_SYSTEMS/Research Management Toolkit/Research Dashboard.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `00_CONSTITUTION/Book V - Cognitive Council.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 4/PHASE 4 - EXECUTION.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/Building achitecture/ALPHA PROXIMA ROLES/AI COUNCIL/AI COUNCIL.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Workflow Registry/Workflow Registry.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `99_ARCHIVE/Engineering Cleanup/ES-002 Metadata Migration Phase 1/06 Source - SanaLab.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `OSG_LAUNCH/09_TEMPLATES/Automation Spec Template.md` | `OSG` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `14_FUTURE/Founder Ideas/Founder Ideas Index.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |
| `OWNED_BY` | `13_OPERATIONS/Artifact Registry/Artifact Registry.md` | `Alpha Proxima Foundation` | `yaml_field` | `institutional_owner` |

## High-Value Cleanup Recommendations

- Add or correct notes for frequently unresolved dependency targets.
- Convert directory-like wiki links into explicit index note links.
- Add stable node IDs after Node Registry review.
- Review low-confidence `PART_OF`, `SUPPORTS`, and ownership relationships before downstream use.

## Recommendations for ES-007

- Build a graph builder that joins `node_registry.json` and `relationship_registry.json`.
- Export graph data to a technology-neutral JSONL format.
- Add graph validation for missing targets, duplicate relationship IDs, and invalid type pairs.
- Keep all generated relationships in draft/inferred state until reviewed.

## Implementation Notes

This report is generated from a read-only scan. Relationships are candidates for institutional graph construction, not canonical claims.

## Future Improvements

- [ ] Add configurable relationship rules.
- [ ] Add inverse relationship generation.
- [ ] Add relationship type source-target validation matrix.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-09-04 | [[CODEX]] | Relationship registry report generated |
