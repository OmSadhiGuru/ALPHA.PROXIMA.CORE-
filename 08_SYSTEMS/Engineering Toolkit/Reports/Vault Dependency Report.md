---
title: "Vault Dependency Report"
aliases: ["Dependency Analyzer Report"]
tags: [systems, engineering, dependencies, graph, report, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
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
- Generated: `2026-07-02T15:03:43-04:00`
- Notes analyzed: `178`
- Directed dependency edges: `1066`
- Broken references: `23`
- Circular references found: `50`
- Disconnected single-note clusters: `5`
- Connected clusters: `6`

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
| `99_ARCHIVE/Engineering Cleanup/ES-002 Metadata Migration Phase 1/06 Source - SanaLab.md` | `[[ES-001 - SanaLab Root File Assessment]]` |
| `ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/Building achitecture/LUMIAION VAULT.md` | `[[ALPHA_PROXIMA_VAULT.canvas]]` |
| `ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/Building achitecture/LUMIAION VAULT.md` | `[[ALPHA_PROXIMA_VAULT.canvas]]` |

## Circular References

| Cycle |
|-------|
| `00_CONSTITUTION/Book I - The Constitution.md` -> `10_TEMPLATES/Concept Note Template.md` -> `00_CONSTITUTION/Book I - The Constitution.md` |
| `00_CONSTITUTION/Book I - The Constitution.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `00_CONSTITUTION/Book I - The Constitution.md` |
| `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `10_TEMPLATES/Concept Note Template.md` |
| `00_CONSTITUTION/Book I - The Constitution.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `00_CONSTITUTION/Book I - The Constitution.md` |
| `00_CONSTITUTION/Book I - The Constitution.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `00_CONSTITUTION/Book I - The Constitution.md` |
| `00_CONSTITUTION/Book I - The Constitution.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `11_OPERATIONS/README.md` -> `00_CONSTITUTION/Book I - The Constitution.md` |
| `00_CONSTITUTION/Book I - The Constitution.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `11_OPERATIONS/README.md` -> `11_OPERATIONS/Office Registry/Office Registry.md` -> `03_AI_COUNCIL/AI Council Registry.md` -> `00_CONSTITUTION/Book I - The Constitution.md` |
| `00_CONSTITUTION/Book I - The Constitution.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `11_OPERATIONS/README.md` -> `11_OPERATIONS/Office Registry/Office Registry.md` -> `03_AI_COUNCIL/AI Council Registry.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `00_CONSTITUTION/Book I - The Constitution.md` |
| `03_AI_COUNCIL/AI Council Registry.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `03_AI_COUNCIL/AI Council Registry.md` |
| `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` |
| `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` |
| `03_AI_COUNCIL/AI Council Registry.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `03_AI_COUNCIL/AI Council Registry.md` |
| `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` |
| `00_CONSTITUTION/Book I - The Constitution.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `11_OPERATIONS/README.md` -> `11_OPERATIONS/Office Registry/Office Registry.md` -> `03_AI_COUNCIL/AI Council Registry.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `00_CONSTITUTION/Book I - The Constitution.md` |
| `00_CONSTITUTION/Book I - The Constitution.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `11_OPERATIONS/README.md` -> `11_OPERATIONS/Office Registry/Office Registry.md` -> `03_AI_COUNCIL/AI Council Registry.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book I - The Constitution.md` |
| `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` |
| `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` |
| `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `11_OPERATIONS/README.md` -> `11_OPERATIONS/Office Registry/Office Registry.md` -> `03_AI_COUNCIL/AI Council Registry.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `10_TEMPLATES/Concept Note Template.md` |
| `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` |
| `00_CONSTITUTION/Book I - The Constitution.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `11_OPERATIONS/README.md` -> `11_OPERATIONS/Office Registry/Office Registry.md` -> `03_AI_COUNCIL/AI Council Registry.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `00_CONSTITUTION/Book I - The Constitution.md` |
| `03_AI_COUNCIL/AI Council Registry.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `03_AI_COUNCIL/AI Council Registry.md` |
| `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` |
| `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` |
| `00_CONSTITUTION/Book I - The Constitution.md` -> `10_TEMPLATES/Concept Note Template.md` -> `03_AI_COUNCIL/Institutional Registry.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `11_OPERATIONS/README.md` -> `11_OPERATIONS/Office Registry/Office Registry.md` -> `03_AI_COUNCIL/AI Council Registry.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `00_CONSTITUTION/Book I - The Constitution.md` |
| `03_AI_COUNCIL/AI Council Registry.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `03_AI_COUNCIL/AI Council Registry.md` |
| `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` |
| `03_AI_COUNCIL/Institutional Registry.md` -> `03_AI_COUNCIL/Alpha Council.md` -> `10_TEMPLATES/Vault Structure Convention.md` -> `11_OPERATIONS/README.md` -> `11_OPERATIONS/Office Registry/Office Registry.md` -> `03_AI_COUNCIL/AI Council Registry.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `03_AI_COUNCIL/Institutional Registry.md` |
| `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` |
| `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` |
| `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` |
| `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` |
| `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` -> `03_AI_COUNCIL/Departments/ATHENA Charter.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` |
| `03_AI_COUNCIL/AI Council Registry.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` -> `03_AI_COUNCIL/Departments/ATHENA Charter.md` -> `03_AI_COUNCIL/AI Council Registry.md` |
| `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` -> `03_AI_COUNCIL/Departments/ATHENA Charter.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` |
| `08_SYSTEMS/Protocols/Communication Protocol.md` -> `03_AI_COUNCIL/Departments/ATHENA Charter.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` |
| `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` -> `03_AI_COUNCIL/Departments/ATHENA Charter.md` -> `03_AI_COUNCIL/Departments/VORTEX Charter.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` |
| `03_AI_COUNCIL/AI Council Registry.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` -> `03_AI_COUNCIL/Departments/ATHENA Charter.md` -> `03_AI_COUNCIL/Departments/VORTEX Charter.md` -> `03_AI_COUNCIL/AI Council Registry.md` |
| `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` -> `03_AI_COUNCIL/Departments/ATHENA Charter.md` -> `03_AI_COUNCIL/Departments/VORTEX Charter.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` |
| `08_SYSTEMS/Protocols/Communication Protocol.md` -> `03_AI_COUNCIL/Departments/ATHENA Charter.md` -> `03_AI_COUNCIL/Departments/VORTEX Charter.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` |
| `03_AI_COUNCIL/Departments/ATHENA Charter.md` -> `03_AI_COUNCIL/Departments/VORTEX Charter.md` -> `03_AI_COUNCIL/Departments/ATHENA Charter.md` |
| `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` -> `03_AI_COUNCIL/Departments/ATHENA Charter.md` -> `03_AI_COUNCIL/Departments/VORTEX Charter.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` |
| `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` -> `03_AI_COUNCIL/Departments/ATHENA Charter.md` -> `03_AI_COUNCIL/Departments/VORTEX Charter.md` -> `03_AI_COUNCIL/Departments/JERANIUM Charter.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` |
| `03_AI_COUNCIL/AI Council Registry.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` -> `03_AI_COUNCIL/Departments/ATHENA Charter.md` -> `03_AI_COUNCIL/Departments/VORTEX Charter.md` -> `03_AI_COUNCIL/Departments/JERANIUM Charter.md` -> `03_AI_COUNCIL/AI Council Registry.md` |
| `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` -> `03_AI_COUNCIL/Departments/ATHENA Charter.md` -> `03_AI_COUNCIL/Departments/VORTEX Charter.md` -> `03_AI_COUNCIL/Departments/JERANIUM Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` |
| `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` -> `03_AI_COUNCIL/Departments/ATHENA Charter.md` -> `03_AI_COUNCIL/Departments/VORTEX Charter.md` -> `03_AI_COUNCIL/Departments/JERANIUM Charter.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` |
| `08_SYSTEMS/Protocols/Communication Protocol.md` -> `03_AI_COUNCIL/Departments/ATHENA Charter.md` -> `03_AI_COUNCIL/Departments/VORTEX Charter.md` -> `03_AI_COUNCIL/Departments/JERANIUM Charter.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` |
| `03_AI_COUNCIL/Departments/ATHENA Charter.md` -> `03_AI_COUNCIL/Departments/VORTEX Charter.md` -> `03_AI_COUNCIL/Departments/JERANIUM Charter.md` -> `03_AI_COUNCIL/Departments/ATHENA Charter.md` |
| `03_AI_COUNCIL/Departments/VORTEX Charter.md` -> `03_AI_COUNCIL/Departments/JERANIUM Charter.md` -> `03_AI_COUNCIL/Departments/VORTEX Charter.md` |
| `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` -> `03_AI_COUNCIL/Departments/ATHENA Charter.md` -> `03_AI_COUNCIL/Departments/VORTEX Charter.md` -> `03_AI_COUNCIL/Departments/JERANIUM Charter.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` |
| `03_AI_COUNCIL/Departments/LUMIAION Charter.md` -> `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` -> `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` -> `08_SYSTEMS/Protocols/Decision Routing Protocol.md` -> `00_CONSTITUTION/Book II - Governance Framework.md` -> `08_SYSTEMS/Institutional Relationship Map.md` -> `08_SYSTEMS/Protocols/Communication Protocol.md` -> `03_AI_COUNCIL/Departments/ATHENA Charter.md` -> `03_AI_COUNCIL/Departments/VORTEX Charter.md` -> `03_AI_COUNCIL/Departments/JERANIUM Charter.md` -> `03_AI_COUNCIL/Departments/SOHMA Charter.md` -> `03_AI_COUNCIL/Departments/LUMIAION Charter.md` |

## Largest Clusters

| Size | Example Notes |
|------|---------------|
| `173` | `00_CONSTITUTION/Book I - The Constitution.md`<br>`00_CONSTITUTION/Book II - Governance Framework.md`<br>`00_CONSTITUTION/Book III - Knowledge Integrity.md`<br>`01_VISION/Alpha Proxima — 10 Year Vision.md`<br>`03_AI_COUNCIL/AI Council Registry.md` |
| `1` | `07_RESEARCH/RP-003/RP-003 Master Index.md` |
| `1` | `07_RESEARCH/RP-004/RP-004 Master Index.md` |
| `1` | `07_RESEARCH/RP-005/RP-005 Master Index.md` |
| `1` | `07_RESEARCH/RP-006/RP-006 Master Index.md` |
| `1` | `Vault.md` |

## Implementation Notes

Circular references are not automatically errors. They identify dependency loops that may need human review.

## Future Improvements

- [ ] Add graph export formats.
- [ ] Add dependency severity rules.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Dependency report generated |
