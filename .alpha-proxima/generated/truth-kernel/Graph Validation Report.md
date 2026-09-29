---
title: "Truth Kernel Graph Validation Report"
tags: [systems, engineering, truth-kernel, validation, alpha-proxima]
created: 2026-09-29
updated: 2026-09-29
status: draft
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-report
institutional_owner: "Alpha Proxima Foundation"
dependencies: ["[[Truth Kernel Node Contract v0.1]]", "[[Tool 010 - Node Registry Generator]]", "[[Tool 011 - Relationship Extractor]]"]
---

# Truth Kernel Graph Validation Report

## Verification boundary

This report describes a derived, read-only scan. Findings are not canonical decisions and source notes were not modified by the generator.

## Summary

- Generated: `2026-09-29T16:48:06+00:00`
- Source fingerprint: `2eebfea8dc87238b6d0535fe6410497364b6b054b7ea1162851f821c6803db6e`
- Contract fingerprint: `7ae4d557f9fd538847afe5d4af60dd419269fed5b8b125193af9d249c6856303`
- Document nodes: `390`
- Entity nodes: `42`
- Document relationships: `2736`
- Entity relationships: `498`
- Template placeholders: `12`
- Unresolved relationships: `265`
- Errors: `20`
- Warnings: `1011`
- Informational: `12`
- Health: `attention`

Health follows **errors only**. A warning is a real issue that does not
invalidate graph integrity; an informational finding is an expected state.
This scan measures *typed graph integrity* and is deliberately independent
of the App's document-level coherence ratchet — the two answer different
questions and are not expected to agree on a number.

## Findings

| Severity | Code | Source path | Message |
|---|---|---|---|
| error | `empty_note` | `Awaken the Inner Guru Production Folder.md` | Markdown note body is empty. |
| error | `empty_note` | `Sans titre 1.md` | Markdown note body is empty. |
| error | `empty_note` | `Sans titre.md` | Markdown note body is empty. |
| error | `empty_note` | `Vault.md` | Markdown note body is empty. |
| error | `identity_collision` | `10_TEMPLATES/Concept Note Template.md` | Identity candidate collides across 2 notes; path suffix applied. |
| error | `identity_collision` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 2/CONCEPT NOTE TEMPLATE.md` | Identity candidate collides across 2 notes; path suffix applied. |
| error | `identity_collision` | `Awaken the Inner Guru Production Folder.md` | Identity candidate collides across 2 notes; path suffix applied. |
| error | `identity_collision` | `LUMIAION.md` | Identity candidate collides across 2 notes; path suffix applied. |
| error | `identity_collision` | `OSG_LAUNCH/10_ACADEMY/AIG/README.md` | Identity candidate collides across 2 notes; path suffix applied. |
| error | `identity_collision` | `docs/constitution/LUMIAION_CONSTITUTION.md` | Identity candidate collides across 2 notes; path suffix applied. |
| error | `missing_relationship` | `03_AI_COUNCIL/AI Council Registry.md` | REFERENCES target: 10_TEMPLATES/ |
| error | `missing_relationship` | `06_GOVERNANCE/Canonical Terminology/Canonical Terminology Register.md` | REFERENCES target: 08_SYSTEMS/Protocols/ |
| error | `missing_relationship` | `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | REFERENCES target: 04 Source - Perplexity |
| error | `missing_relationship` | `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | REFERENCES target: 05 Source - Gemini |
| error | `missing_relationship` | `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | REFERENCES target: 13 Research Graph/Concepts |
| error | `missing_relationship` | `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | REFERENCES target: ARCHIVE |
| error | `missing_relationship` | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | REFERENCES target: 13 Research Graph/Concepts |
| error | `missing_relationship` | `07_RESEARCH/RP-002/09 Canonical Synthesis/RP-002 Canonical Synthesis.md` | REFERENCES target: 13 Research Graph/Concepts/ |
| error | `missing_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Engineering Program EP-001 - Institutional Knowledge Graph.md` | REFERENCES target: Vault Dependency Report |
| error | `missing_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/Building achitecture/LUMIAION VAULT.md` | REFERENCES target: ALPHA_PROXIMA_VAULT.canvas |
| warning | `ambiguous_relationship` | `00_CONSTITUTION/Book I - The Constitution.md` | REFERENCES target: Concept Note Template |
| warning | `ambiguous_relationship` | `00_CONSTITUTION/Book I - The Constitution.md` | REFERENCES target: LUMIAION |
| warning | `ambiguous_relationship` | `00_CONSTITUTION/Book II - Governance Framework.md` | REFERENCES target: LUMIAION |
| warning | `ambiguous_relationship` | `00_CONSTITUTION/Book II - Governance Framework.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `00_CONSTITUTION/Book III - Knowledge Integrity.md` | REFERENCES target: LUMIAION |
| warning | `ambiguous_relationship` | `00_CONSTITUTION/Book III - Knowledge Integrity.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `00_CONSTITUTION/Book IV - Cognitive Architecture.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `01_VISION/Alpha Proxima — 10 Year Vision.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `03_AI_COUNCIL/AI Council Registry.md` | REFERENCES target: LUMIAION |
| warning | `ambiguous_relationship` | `03_AI_COUNCIL/AI Council Registry.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `03_AI_COUNCIL/Alpha Council.md` | REFERENCES target: Concept Note Template |
| warning | `ambiguous_relationship` | `03_AI_COUNCIL/Alpha Council.md` | REFERENCES target: LUMIAION |
| warning | `ambiguous_relationship` | `03_AI_COUNCIL/Cognitive Council Charter.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `03_AI_COUNCIL/Departments/ATHENA Charter.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `03_AI_COUNCIL/Departments/JERANIUM Charter.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `03_AI_COUNCIL/Departments/LUMIAION Charter.md` | REFERENCES target: LUMIAION |
| warning | `ambiguous_relationship` | `03_AI_COUNCIL/Departments/SOHMA Charter.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `03_AI_COUNCIL/Departments/VORTEX Charter.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `03_AI_COUNCIL/Engine Registry.md` | REFERENCES target: Concept Note Template |
| warning | `ambiguous_relationship` | `03_AI_COUNCIL/Engine Registry.md` | REFERENCES target: LUMIAION |
| warning | `ambiguous_relationship` | `03_AI_COUNCIL/Engine Registry.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `03_AI_COUNCIL/Institutional Registry.md` | REFERENCES target: Concept Note Template |
| warning | `ambiguous_relationship` | `03_AI_COUNCIL/Institutional Registry.md` | REFERENCES target: LUMIAION |
| warning | `ambiguous_relationship` | `03_AI_COUNCIL/Research Council.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `04_DECISIONS/ADR-0001 - The Founding Decision.md` | REFERENCES target: LUMIAION |
| warning | `ambiguous_relationship` | `04_DECISIONS/ADR-0001 - The Founding Decision.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `06_GOVERNANCE/Canonical Terminology/Canonical Terminology Register.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `06_GOVERNANCE/Constitutional Impact Report/CIR-002 Institutional Completeness Review.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `06_GOVERNANCE/Directive Governance Framework/Directive Governance Framework.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `06_GOVERNANCE/Research Framework/Research Integration Framework.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `07_RESEARCH/RP-001/05 Source - Gemini/RP-001 Source Note - Gemini.md` | REFERENCES target: ARCHIVE/ARCHIVE Philosophy |
| warning | `ambiguous_relationship` | `07_RESEARCH/RP-001/07 Future Sources/RP-001 Future Sources.md` | REFERENCES target: ARCHIVE/ARCHIVE Philosophy |
| warning | `ambiguous_relationship` | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | REFERENCES target: Active Inference |
| warning | `ambiguous_relationship` | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness.md` | REFERENCES target: Active Inference |
| warning | `ambiguous_relationship` | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | REFERENCES target: Active Inference |
| warning | `ambiguous_relationship` | `07_RESEARCH/RP-001/19 Related Laws/RP-001 Governing Provisions.md` | REFERENCES target: ARCHIVE/ARCHIVE Philosophy |
| warning | `ambiguous_relationship` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | REFERENCES target: 13 Research Graph/Concepts/Active Inference |
| warning | `ambiguous_relationship` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | REFERENCES target: ARCHIVE/ARCHIVE Philosophy |
| warning | `ambiguous_relationship` | `07_RESEARCH/RP-001/RP-001 Master Index.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `07_RESEARCH/RP-002/03 Source Registry/RP-002 Source Registry.md` | REFERENCES target: ARCHIVE/ARCHIVE Philosophy |
| warning | `ambiguous_relationship` | `07_RESEARCH/RP-002/19 Related Laws/RP-002 Governing Provisions.md` | REFERENCES target: ARCHIVE/ARCHIVE Philosophy |
| warning | `ambiguous_relationship` | `07_RESEARCH/RP-002/RP-002 Master Index.md` | REFERENCES target: ARCHIVE/ARCHIVE Philosophy |
| warning | `ambiguous_relationship` | `08_SYSTEMS/ALPHAPROXIMA Enterprise Knowledge Architecture v1.0.md` | REFERENCES target: Node Taxonomy |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Alpha Proxima Operating Model v1.0.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Automation/Vault Note Generator.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Standards/01 - Markdown Style Guide.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Standards/02 - YAML Frontmatter Standard.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Standards/03 - Folder Naming Convention.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Standards/06 - CLI Standard.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Standards/07 - Automation Standard.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Standards/08 - Logging Standard.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Standards/09 - Git Standard.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Standards/10 - Template Standard.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Standards/10 - Template Standard.md` | RELATED_TO target: [[Concept Note Template]] |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Standards/11 - One Question Document Standard.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Standards/ALPHA PROXIMA ENGINEERING HANDBOOK.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Toolkit/Alpha Proxima Engineering Toolkit.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Toolkit/Tool 001 - Vault Validator.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Toolkit/Tool 002 - YAML Validator.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Toolkit/Tool 003 - Metadata Migration Utility.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Toolkit/Tool 004 - Vault Statistics Generator.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Toolkit/Tool 005 - Dependency Analyzer.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Toolkit/Tool 006 - Office Integrity Checker.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Toolkit/Tool 007 - Research Integrity Checker.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Toolkit/Tool 008 - Engineering CLI.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Toolkit/Tool 009 - Graph Color System.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Engineering Toolkit/Tool 012 - Founder OS State Engine.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/EP-001 Engineering Roadmap.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Engineering Program EP-001 - Institutional Knowledge Graph.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Engineering Program EP-001 - Institutional Knowledge Graph.md` | REFERENCES target: Node Taxonomy |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Engineering Program EP-001 - Institutional Knowledge Graph.md` | RELATED_TO target: [[Node Taxonomy]] |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Graph Readiness Assessment.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Institutional Node Taxonomy v1.md` | RELATED_TO target: [[Node Taxonomy]] |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Knowledge Graph Architecture v1.0.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Knowledge Graph Architecture v1.0.md` | REFERENCES target: Node Taxonomy |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Knowledge Graph Architecture v1.0.md` | RELATED_TO target: [[Node Taxonomy]] |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Knowledge Graph Conventions.md` | DEPENDS_ON target: [[Node Taxonomy]] |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Knowledge Graph Conventions.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Node Taxonomy.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Relationship Taxonomy.md` | DEPENDS_ON target: [[Node Taxonomy]] |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Relationship Taxonomy.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Tools/Node Registry Report.md` | DEPENDS_ON target: [[Node Taxonomy]] |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Tools/Node Registry Report.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Tools/Node Registry Report.md` | REFERENCES target: Node Taxonomy |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Tools/Relationship Registry Report.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Tools/Tool 010 - Node Registry Generator.md` | DEPENDS_ON target: [[Node Taxonomy]] |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Tools/Tool 010 - Node Registry Generator.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Tools/Tool 010 - Node Registry Generator.md` | REFERENCES target: Node Taxonomy |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Tools/Tool 011 - Relationship Extractor.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Tools/Tool 011 - Relationship Extractor.md` | RELATED_TO target: [[Node Taxonomy]] |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Truth Kernel Node Contract v0.1.md` | DEPENDS_ON target: [[Node Taxonomy]] |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Knowledge Graph/Truth Kernel Node Contract v0.1.md` | REFERENCES target: Node Taxonomy |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Institutional Relationship Map.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Knowledge Architecture Specification.md` | REFERENCES target: Node Taxonomy |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Knowledge Architecture Specification.md` | RELATED_TO target: [[Node Taxonomy]] |
| warning | `ambiguous_relationship` | `08_SYSTEMS/LUMIAION Architecture Spec v0.1.md` | REFERENCES target: LUMIAION |
| warning | `ambiguous_relationship` | `08_SYSTEMS/LUMIAION Architecture Spec v0.1.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Protocols/Communication Protocol.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Protocols/Decision Routing Protocol.md` | REFERENCES target: Concept Note Template |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Protocols/Decision Routing Protocol.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Protocols/Future Expansion Protocol.md` | DEPENDS_ON target: [[Concept Note Template]] |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Protocols/Future Expansion Protocol.md` | REFERENCES target: Concept Note Template |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Protocols/Future Expansion Protocol.md` | RELATED_TO target: [[Concept Note Template]] |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Research Management Toolkit/Reports/ES-004 - Research Management Toolkit Delivery Report.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Research Management Toolkit/Research Dashboard.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Research Management Toolkit/Research Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Research Management Toolkit/Research Lifecycle Diagram.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Research Management Toolkit/Research Management Toolkit v1.0.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Research Management Toolkit/Research Management Toolkit v1.0.md` | REFERENCES target: Research Commission Template |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Research Management Toolkit/Templates/Research Program Template.md` | REFERENCES target: Research Commission Template |
| warning | `ambiguous_relationship` | `08_SYSTEMS/The Orchestration Framework.md` | REFERENCES target: ARCHIVE Philosophy |
| warning | `ambiguous_relationship` | `08_SYSTEMS/The Orchestration Framework.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Visual Systems/Graph View Color System.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `08_SYSTEMS/Visual Systems/Graph View Color System.md` | REFERENCES target: LUMIAION |
| warning | `ambiguous_relationship` | `09_OFFICES/Engineering Office/Engineering Office Charter.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `09_OFFICES/Ethics Council/Ethics Council Charter.md` | REFERENCES target: Concept Note Template |
| warning | `ambiguous_relationship` | `09_OFFICES/Ethics Council/Ethics Council Charter.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `09_OFFICES/Executive Office/Executive Office Charter.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `09_OFFICES/Research Intelligence Office/Research Intelligence Office Charter.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `09_OFFICES/Research Intelligence Office/Research Office Matrix.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `10_TEMPLATES/ADR Template.md` | REFERENCES target: Concept Note Template |
| warning | `ambiguous_relationship` | `10_TEMPLATES/ADR Template.md` | REFERENCES target: LUMIAION |
| warning | `ambiguous_relationship` | `10_TEMPLATES/Concept Note Template.md` | REFERENCES target: LUMIAION |
| warning | `ambiguous_relationship` | `10_TEMPLATES/Implementation Note Template.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `10_TEMPLATES/Implementation Note Template.md` | REFERENCES target: Concept Note Template |
| warning | `ambiguous_relationship` | `10_TEMPLATES/Vault Structure Convention.md` | REFERENCES target: Concept Note Template |
| warning | `ambiguous_relationship` | `10_TEMPLATES/Vault Structure Convention.md` | REFERENCES target: LUMIAION |
| warning | `ambiguous_relationship` | `12_PEOPLE/CODEX.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `12_PEOPLE/Frederick Belizaire Gunville.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/AI Council/AI Council Operations Registry.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/AI Council/AI Council Operations Registry.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `13_OPERATIONS/AI Council/AI Council Operations Registry.md` | RELATED_TO target: [[CODEX]] |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Annual Reviews/Annual Reviews Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Artifact Registry/Artifact Registry.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Automation Queue/Automation Queue Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Daily Operations/Daily Operations Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Dashboards/Dashboards Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Decision Pipelines/Decision Pipelines Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Decision Pipelines/Decision Pipelines Index.md` | REFERENCES target: Concept Note Template |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Executive Office/Executive Office Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Institutional Observatory/Institutional Observatory Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Metrics/Metrics Registry.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Monthly Operations/Monthly Operations Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Office Registry/Office Registry.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Office Registry/Office Registry.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Operational Health/FIR-001 Repository Health Result.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Operational Health/Operational Health Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Operational Procedures/Founder Intent Routing Procedure.md` | DEPENDS_ON target: [[LUMIAION Charter]] |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Operational Procedures/Operational Procedures Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Quarterly Reviews/Quarterly Reviews Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/README.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Review Cycles/Review Cycles Registry.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Version History/Operations Version History.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Weekly Operations/Weekly Operations Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `13_OPERATIONS/Workflow Registry/Workflow Registry.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `14_FUTURE/AI Recommendations/AI Recommendations Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `14_FUTURE/Architectural Proposals/Architectural Proposals Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `14_FUTURE/Archive/Future Archive Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `14_FUTURE/Decision Log/Decision Log Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `14_FUTURE/Feature Requests/Feature Requests Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `14_FUTURE/Founder Ideas/Founder Ideas Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `14_FUTURE/Future Cognitive Functions/Future Cognitive Functions Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `14_FUTURE/Future Institutes/Future Institutes Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `14_FUTURE/Implementation Proposals/Implementation Proposals Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `14_FUTURE/README.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `14_FUTURE/README.md` | REFERENCES target: Concept Note Template |
| warning | `ambiguous_relationship` | `14_FUTURE/Research Commissions/Research Commissions Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `14_FUTURE/Research Commissions/Research Commissions Index.md` | REFERENCES target: Research Commission Template |
| warning | `ambiguous_relationship` | `14_FUTURE/Review Queue/Review Queue Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `14_FUTURE/Roadmap/Roadmap Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `14_FUTURE/Technology Watch/Technology Watch Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `14_FUTURE/Templates/Future Templates Index.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `14_FUTURE/Templates/Future Templates Index.md` | REFERENCES target: Research Commission Template |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Engineering Cleanup/ES-002 Metadata Migration Phase 1/06 Source - SanaLab.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/Building achitecture/ALPHA PROXIMA ROLES/AI COUNCIL/AI COUNCIL.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/Building achitecture/ALPHA PROXIMA ROLES/ARCHITECTURE MAP.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/Building achitecture/LUMIAION VAULT.md` | REFERENCES target: BUILDING MILESTONE |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/Building achitecture/LUMIAION VAULT.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/Building achitecture/LUMIAION VAULT.md` | RELATED_TO target: [[BUILDING MILESTONE]] |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/Phase 1/PHASE 1 - FOUNDATION.md` | RELATED_TO target: [[Building Milestone]] |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 2/CONCEPT NOTE TEMPLATE.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 2/CONCEPT NOTE TEMPLATE.md` | RELATED_TO target: [[Concept Note Template]] |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 2/CORE FOLDER.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 2/NAMING RULES.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 2/PHASE 2 - KNOWLEDGE.md` | REFERENCES target: CONCEPT NOTE TEMPLATE |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 2/PHASE 2 - KNOWLEDGE.md` | RELATED_TO target: [[CONCEPT NOTE TEMPLATE]] |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 2/SOURCE NOTE TEMPLATE.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 2/TAG TAXONOMY.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 3/COST TIERS.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 3/MEMORY RULES.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 3/PHASE 3 - INTELLIGENCE.md` | REFERENCES target: AI COUNCIL |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 3/PHASE 3 - INTELLIGENCE.md` | RELATED_TO target: [[AI Council]] |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 3/ROUTING RULES.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 4/AUTOMATION PLAN.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 4/GITHUB REPO STRUCTURE.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 4/HOSTING OPTIONS.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 4/MVP SPECIFICATION.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 5/CONTRACTION FINDER.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 5/DAILY REVIEW LOOP.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 5/IMPROVEMENT LOG.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/building milestone/phase 5/LEGACY ROADMAP.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/NOTION COMMAND CENTER.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `99_ARCHIVE/Legacy ALPHA PROXIMA/OBSIDIAN VAULT.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `Alpha Proxima Core.md` | REFERENCES target: LUMIAION Charter |
| warning | `ambiguous_relationship` | `Building Milestone.md` | REFERENCES target: CODEX |
| warning | `ambiguous_relationship` | `Building Milestone.md` | RELATED_TO target: [[BUILDING MILESTONE]] |
| warning | `ambiguous_relationship` | `LUMIAION.md` | REFERENCES target: Concept Note Template |
| warning | `ambiguous_relationship` | `OSG_LAUNCH/10_ACADEMY/AIG/Awaken the Inner Guru Recording Start Guide.md` | DEPENDS_ON target: [[Awaken the Inner Guru Production Folder]] |
| warning | `ambiguous_relationship` | `OSG_LAUNCH/10_ACADEMY/README.md` | RELATED_TO target: [[Awaken the Inner Guru Production Folder]] |
| warning | `missing_frontmatter` | `Awaken the Inner Guru Production Folder.md` | Markdown note has no frontmatter. |
| warning | `missing_frontmatter` | `OSG_BUSINESS/00 OSG Business Foundation — Overview.md` | Markdown note has no frontmatter. |
| warning | `missing_frontmatter` | `OSG_BUSINESS/01 Flagship Course.md` | Markdown note has no frontmatter. |
| warning | `missing_frontmatter` | `OSG_BUSINESS/02 Coaching Offers.md` | Markdown note has no frontmatter. |
| warning | `missing_frontmatter` | `OSG_BUSINESS/03 Website Copy.md` | Markdown note has no frontmatter. |
| warning | `missing_frontmatter` | `OSG_BUSINESS/04 Client Journey & Onboarding.md` | Markdown note has no frontmatter. |
| warning | `missing_frontmatter` | `OSG_BUSINESS/05 Email Sequences.md` | Markdown note has no frontmatter. |
| warning | `missing_frontmatter` | `OSG_BUSINESS/06 Community Onboarding.md` | Markdown note has no frontmatter. |
| warning | `missing_frontmatter` | `OSG_BUSINESS/07 30-Day Launch Checklist.md` | Markdown note has no frontmatter. |
| warning | `missing_frontmatter` | `Sans titre 1.md` | Markdown note has no frontmatter. |
| warning | `missing_frontmatter` | `Sans titre.md` | Markdown note has no frontmatter. |
| warning | `missing_frontmatter` | `Vault.md` | Markdown note has no frontmatter. |
| warning | `missing_frontmatter` | `docs/constitution/LUMIAION_CONSTITUTION.md` | Markdown note has no frontmatter. |
| warning | `missing_frontmatter` | `docs/constitution/README.md` | Markdown note has no frontmatter. |
| warning | `missing_frontmatter` | `docs/setup/Claude-Code-in-Obsidian.md` | Markdown note has no frontmatter. |
| warning | `missing_owner` | `00_CONSTITUTION/Constitutional Hierarchy Statement.md` | No canonical owner is declared. |
| warning | `missing_owner` | `00_CONSTITUTION/Founding Principles of Alpha Proxima.md` | No canonical owner is declared. |
| warning | `missing_owner` | `01_VISION/Alpha Proxima — 10 Year Vision.md` | No canonical owner is declared. |
| warning | `missing_owner` | `03_AI_COUNCIL/AI Council Registry.md` | No canonical owner is declared. |
| warning | `missing_owner` | `03_AI_COUNCIL/Alpha Council.md` | No canonical owner is declared. |
| warning | `missing_owner` | `03_AI_COUNCIL/Cognitive Council Charter.md` | No canonical owner is declared. |
| warning | `missing_owner` | `03_AI_COUNCIL/Cognitive Function Matrix.md` | No canonical owner is declared. |
| warning | `missing_owner` | `03_AI_COUNCIL/Cognitive Function Registry.md` | No canonical owner is declared. |
| warning | `missing_owner` | `03_AI_COUNCIL/Departments/ATHENA Charter.md` | No canonical owner is declared. |
| warning | `missing_owner` | `03_AI_COUNCIL/Departments/JERANIUM Charter.md` | No canonical owner is declared. |
| warning | `missing_owner` | `03_AI_COUNCIL/Departments/LUMIAION Charter.md` | No canonical owner is declared. |
| warning | `missing_owner` | `03_AI_COUNCIL/Departments/SOHMA Charter.md` | No canonical owner is declared. |
| warning | `missing_owner` | `03_AI_COUNCIL/Departments/VORTEX Charter.md` | No canonical owner is declared. |
| warning | `missing_owner` | `03_AI_COUNCIL/Engine Registry.md` | No canonical owner is declared. |
| warning | `missing_owner` | `03_AI_COUNCIL/Engine Succession Policy.md` | No canonical owner is declared. |
| warning | `missing_owner` | `03_AI_COUNCIL/Institutional Registry.md` | No canonical owner is declared. |
| warning | `missing_owner` | `03_AI_COUNCIL/YUNA Charter.md` | No canonical owner is declared. |
| warning | `missing_owner` | `04_DECISIONS/ADR-0001 - The Founding Decision.md` | No canonical owner is declared. |
| warning | `missing_owner` | `04_DECISIONS/ADR-0002 - Reconciling the Four Institutional Taxonomies.md` | No canonical owner is declared. |
| warning | `missing_owner` | `05_PROPOSALS/CN-0001 - Constitutional Alignment Gap Report.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Canonical Terminology/Canonical Terminology Register.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Constitutional Audit/CAR-001 Constitutional Audit Report.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Constitutional Impact Report/CIR-001 Epoch III Constitutional Refactoring.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Constitutional Impact Report/CIR-002 Institutional Completeness Review.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Directive Governance Framework/Directive Governance Framework.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Epoch V/Governance Model Crosswalk.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Epoch V/Interim Authority Instrument.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Foundation Gap Report/FGR-001 Epoch II Stewardship Audit.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Founder Directives/Founder Directives Register.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Institutional Glossary & Acronym Register.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Institutional Open Questions Register.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Institutional Policies/Citation Policy.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Institutional Policies/Metadata Policy.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Institutional Policies/Naming Policy.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Institutional Policies/Privacy Policy.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Institutional Policies/Source Attribution Policy.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Institutional Policies/Versioning Policy.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Institutional Timeline.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Research Debt Register/Research Debt Register.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Research Framework/Institutional Intelligence Translation Framework v1.0.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Research Framework/Research Integration Framework.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Research Framework/Research Program Playbook v1.0.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Research Framework/Translation Checklist.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Research Framework/Translation Decision Matrix.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Research Framework/Translation Review Process.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Research Methodology/Alpha Proxima Research Methodology v1.0.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Standards Council/Standards Council Evaluation.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | No canonical owner is declared. |
| warning | `missing_owner` | `06_GOVERNANCE/Standing Orders/Standing Orders Register.md` | No canonical owner is declared. |
| warning | `missing_owner` | `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | No canonical owner is declared. |
| warning | `missing_owner` | `07_RESEARCH/RP-001/01 Research Question/RP-001 Research Question.md` | No canonical owner is declared. |
| warning | `missing_owner` | `07_RESEARCH/RP-001/02 Objectives/RP-001 Objectives.md` | No canonical owner is declared. |

## Reproduction

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" truth-kernel --vault . --output-dir /tmp/alpha-proxima-truth-kernel --force
```

The machine-readable outputs are deterministic: two runs over unchanged source content must be byte-identical.
