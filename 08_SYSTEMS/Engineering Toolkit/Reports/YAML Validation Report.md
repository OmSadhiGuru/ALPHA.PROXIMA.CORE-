---
title: "YAML Validation Report"
aliases: []
tags: [systems, engineering, validation, yaml, report, alpha-proxima]
created: 2026-09-29
updated: 2026-09-29
status: draft
version: "0.1.0"
authors: ["CODEX"]
artifact_type: engineering-report
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Tool 002 - YAML Validator]]"]
related_documents: ["[[Alpha Proxima Engineering Toolkit]]", "[[02 - YAML Frontmatter Standard]]"]
related_research_programs: []
---

# YAML Validation Report

## Purpose

Report frontmatter quality issues detected by [[Tool 002 - YAML Validator]].

## Summary

- Vault: `/home/user/ALPHA.PROXIMA.CORE-`
- Generated: `2026-09-29T16:57:39+00:00`
- Markdown notes scanned: `391`
- Critical: `0`
- Errors: `16`
- Warnings: `977`
- Info: `387`

## Validation Results

### deprecated_field

| Severity | Path | Message |
|----------|------|---------|
| warning | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Deprecated field `owner`; use `institutional_owner`. |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Deprecated field `owner`; use `institutional_owner`. |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Deprecated field `owner`; use `institutional_owner`. |

### invalid_status

| Severity | Path | Message |
|----------|------|---------|
| warning | `04_DECISIONS/ADR-0002 - Reconciling the Four Institutional Taxonomies.md` | Invalid status value: proposed |
| warning | `05_PROPOSALS/Live Layer Reconciliation - PR51 vs PR52-53.md` | Invalid status value: adopted |
| warning | `07_RESEARCH/RP-002/06 Source - Illustrated/RP-002 Source Note - Illustrated.md` | Invalid status value: pending |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-C RP-002 Illustrated.md` | Invalid status value: pending |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Invalid status value: living-reference |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Invalid status value: ready-for-recording |

### invalid_version

| Severity | Path | Message |
|----------|------|---------|
| warning | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Version should use semantic versioning: 1.0 |

### missing_required_metadata

| Severity | Path | Message |
|----------|------|---------|
| warning | `00_CONSTITUTION/Constitutional Hierarchy Statement.md` | Missing required field: artifact_type |
| warning | `00_CONSTITUTION/Constitutional Hierarchy Statement.md` | Missing required field: dependencies |
| warning | `00_CONSTITUTION/Constitutional Hierarchy Statement.md` | Missing required field: institutional_owner |
| warning | `00_CONSTITUTION/Constitutional Hierarchy Statement.md` | Missing required field: related_documents |
| warning | `00_CONSTITUTION/Constitutional Hierarchy Statement.md` | Missing required field: related_research_programs |
| warning | `00_CONSTITUTION/Founding Principles of Alpha Proxima.md` | Missing required field: artifact_type |
| warning | `00_CONSTITUTION/Founding Principles of Alpha Proxima.md` | Missing required field: dependencies |
| warning | `00_CONSTITUTION/Founding Principles of Alpha Proxima.md` | Missing required field: institutional_owner |
| warning | `00_CONSTITUTION/Founding Principles of Alpha Proxima.md` | Missing required field: related_documents |
| warning | `00_CONSTITUTION/Founding Principles of Alpha Proxima.md` | Missing required field: related_research_programs |
| warning | `01_VISION/Alpha Proxima — 10 Year Vision.md` | Missing required field: artifact_type |
| warning | `01_VISION/Alpha Proxima — 10 Year Vision.md` | Missing required field: dependencies |
| warning | `01_VISION/Alpha Proxima — 10 Year Vision.md` | Missing required field: institutional_owner |
| warning | `01_VISION/Alpha Proxima — 10 Year Vision.md` | Missing required field: related_documents |
| warning | `01_VISION/Alpha Proxima — 10 Year Vision.md` | Missing required field: related_research_programs |
| warning | `03_AI_COUNCIL/AI Council Registry.md` | Missing required field: artifact_type |
| warning | `03_AI_COUNCIL/AI Council Registry.md` | Missing required field: dependencies |
| warning | `03_AI_COUNCIL/AI Council Registry.md` | Missing required field: institutional_owner |
| warning | `03_AI_COUNCIL/AI Council Registry.md` | Missing required field: related_documents |
| warning | `03_AI_COUNCIL/AI Council Registry.md` | Missing required field: related_research_programs |
| warning | `03_AI_COUNCIL/Alpha Council.md` | Missing required field: artifact_type |
| warning | `03_AI_COUNCIL/Alpha Council.md` | Missing required field: dependencies |
| warning | `03_AI_COUNCIL/Alpha Council.md` | Missing required field: institutional_owner |
| warning | `03_AI_COUNCIL/Alpha Council.md` | Missing required field: related_documents |
| warning | `03_AI_COUNCIL/Alpha Council.md` | Missing required field: related_research_programs |
| warning | `03_AI_COUNCIL/Cognitive Council Charter.md` | Missing required field: artifact_type |
| warning | `03_AI_COUNCIL/Cognitive Council Charter.md` | Missing required field: dependencies |
| warning | `03_AI_COUNCIL/Cognitive Council Charter.md` | Missing required field: institutional_owner |
| warning | `03_AI_COUNCIL/Cognitive Council Charter.md` | Missing required field: related_documents |
| warning | `03_AI_COUNCIL/Cognitive Council Charter.md` | Missing required field: related_research_programs |
| warning | `03_AI_COUNCIL/Cognitive Function Matrix.md` | Missing required field: artifact_type |
| warning | `03_AI_COUNCIL/Cognitive Function Matrix.md` | Missing required field: dependencies |
| warning | `03_AI_COUNCIL/Cognitive Function Matrix.md` | Missing required field: institutional_owner |
| warning | `03_AI_COUNCIL/Cognitive Function Matrix.md` | Missing required field: related_documents |
| warning | `03_AI_COUNCIL/Cognitive Function Matrix.md` | Missing required field: related_research_programs |
| warning | `03_AI_COUNCIL/Cognitive Function Registry.md` | Missing required field: artifact_type |
| warning | `03_AI_COUNCIL/Cognitive Function Registry.md` | Missing required field: dependencies |
| warning | `03_AI_COUNCIL/Cognitive Function Registry.md` | Missing required field: institutional_owner |
| warning | `03_AI_COUNCIL/Cognitive Function Registry.md` | Missing required field: related_documents |
| warning | `03_AI_COUNCIL/Cognitive Function Registry.md` | Missing required field: related_research_programs |
| warning | `03_AI_COUNCIL/Departments/ATHENA Charter.md` | Missing required field: artifact_type |
| warning | `03_AI_COUNCIL/Departments/ATHENA Charter.md` | Missing required field: dependencies |
| warning | `03_AI_COUNCIL/Departments/ATHENA Charter.md` | Missing required field: institutional_owner |
| warning | `03_AI_COUNCIL/Departments/ATHENA Charter.md` | Missing required field: related_documents |
| warning | `03_AI_COUNCIL/Departments/ATHENA Charter.md` | Missing required field: related_research_programs |
| warning | `03_AI_COUNCIL/Departments/JERANIUM Charter.md` | Missing required field: artifact_type |
| warning | `03_AI_COUNCIL/Departments/JERANIUM Charter.md` | Missing required field: dependencies |
| warning | `03_AI_COUNCIL/Departments/JERANIUM Charter.md` | Missing required field: institutional_owner |
| warning | `03_AI_COUNCIL/Departments/JERANIUM Charter.md` | Missing required field: related_documents |
| warning | `03_AI_COUNCIL/Departments/JERANIUM Charter.md` | Missing required field: related_research_programs |
| warning | `03_AI_COUNCIL/Departments/LUMIAION Charter.md` | Missing required field: artifact_type |
| warning | `03_AI_COUNCIL/Departments/LUMIAION Charter.md` | Missing required field: dependencies |
| warning | `03_AI_COUNCIL/Departments/LUMIAION Charter.md` | Missing required field: institutional_owner |
| warning | `03_AI_COUNCIL/Departments/LUMIAION Charter.md` | Missing required field: related_documents |
| warning | `03_AI_COUNCIL/Departments/LUMIAION Charter.md` | Missing required field: related_research_programs |
| warning | `03_AI_COUNCIL/Departments/SOHMA Charter.md` | Missing required field: artifact_type |
| warning | `03_AI_COUNCIL/Departments/SOHMA Charter.md` | Missing required field: dependencies |
| warning | `03_AI_COUNCIL/Departments/SOHMA Charter.md` | Missing required field: institutional_owner |
| warning | `03_AI_COUNCIL/Departments/SOHMA Charter.md` | Missing required field: related_documents |
| warning | `03_AI_COUNCIL/Departments/SOHMA Charter.md` | Missing required field: related_research_programs |
| warning | `03_AI_COUNCIL/Departments/VORTEX Charter.md` | Missing required field: artifact_type |
| warning | `03_AI_COUNCIL/Departments/VORTEX Charter.md` | Missing required field: dependencies |
| warning | `03_AI_COUNCIL/Departments/VORTEX Charter.md` | Missing required field: institutional_owner |
| warning | `03_AI_COUNCIL/Departments/VORTEX Charter.md` | Missing required field: related_documents |
| warning | `03_AI_COUNCIL/Departments/VORTEX Charter.md` | Missing required field: related_research_programs |
| warning | `03_AI_COUNCIL/Engine Registry.md` | Missing required field: artifact_type |
| warning | `03_AI_COUNCIL/Engine Registry.md` | Missing required field: dependencies |
| warning | `03_AI_COUNCIL/Engine Registry.md` | Missing required field: institutional_owner |
| warning | `03_AI_COUNCIL/Engine Registry.md` | Missing required field: related_documents |
| warning | `03_AI_COUNCIL/Engine Registry.md` | Missing required field: related_research_programs |
| warning | `03_AI_COUNCIL/Engine Succession Policy.md` | Missing required field: artifact_type |
| warning | `03_AI_COUNCIL/Engine Succession Policy.md` | Missing required field: dependencies |
| warning | `03_AI_COUNCIL/Engine Succession Policy.md` | Missing required field: institutional_owner |
| warning | `03_AI_COUNCIL/Engine Succession Policy.md` | Missing required field: related_documents |
| warning | `03_AI_COUNCIL/Engine Succession Policy.md` | Missing required field: related_research_programs |
| warning | `03_AI_COUNCIL/Institutional Registry.md` | Missing required field: artifact_type |
| warning | `03_AI_COUNCIL/Institutional Registry.md` | Missing required field: dependencies |
| warning | `03_AI_COUNCIL/Institutional Registry.md` | Missing required field: institutional_owner |
| warning | `03_AI_COUNCIL/Institutional Registry.md` | Missing required field: related_documents |
| warning | `03_AI_COUNCIL/Institutional Registry.md` | Missing required field: related_research_programs |
| warning | `03_AI_COUNCIL/YUNA Charter.md` | Missing required field: artifact_type |
| warning | `03_AI_COUNCIL/YUNA Charter.md` | Missing required field: dependencies |
| warning | `03_AI_COUNCIL/YUNA Charter.md` | Missing required field: institutional_owner |
| warning | `03_AI_COUNCIL/YUNA Charter.md` | Missing required field: related_documents |
| warning | `03_AI_COUNCIL/YUNA Charter.md` | Missing required field: related_research_programs |
| warning | `04_DECISIONS/ADR-0001 - The Founding Decision.md` | Missing required field: artifact_type |
| warning | `04_DECISIONS/ADR-0001 - The Founding Decision.md` | Missing required field: dependencies |
| warning | `04_DECISIONS/ADR-0001 - The Founding Decision.md` | Missing required field: institutional_owner |
| warning | `04_DECISIONS/ADR-0001 - The Founding Decision.md` | Missing required field: related_documents |
| warning | `04_DECISIONS/ADR-0001 - The Founding Decision.md` | Missing required field: related_research_programs |
| warning | `04_DECISIONS/ADR-0002 - Reconciling the Four Institutional Taxonomies.md` | Missing required field: artifact_type |
| warning | `04_DECISIONS/ADR-0002 - Reconciling the Four Institutional Taxonomies.md` | Missing required field: dependencies |
| warning | `04_DECISIONS/ADR-0002 - Reconciling the Four Institutional Taxonomies.md` | Missing required field: institutional_owner |
| warning | `04_DECISIONS/ADR-0002 - Reconciling the Four Institutional Taxonomies.md` | Missing required field: related_documents |
| warning | `04_DECISIONS/ADR-0002 - Reconciling the Four Institutional Taxonomies.md` | Missing required field: related_research_programs |
| warning | `05_PROPOSALS/CN-0001 - Constitutional Alignment Gap Report.md` | Missing required field: artifact_type |
| warning | `05_PROPOSALS/CN-0001 - Constitutional Alignment Gap Report.md` | Missing required field: dependencies |
| warning | `05_PROPOSALS/CN-0001 - Constitutional Alignment Gap Report.md` | Missing required field: institutional_owner |
| warning | `05_PROPOSALS/CN-0001 - Constitutional Alignment Gap Report.md` | Missing required field: related_documents |
| warning | `05_PROPOSALS/CN-0001 - Constitutional Alignment Gap Report.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Canonical Terminology/Canonical Terminology Register.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Canonical Terminology/Canonical Terminology Register.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Canonical Terminology/Canonical Terminology Register.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Canonical Terminology/Canonical Terminology Register.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Canonical Terminology/Canonical Terminology Register.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Constitutional Audit/CAR-001 Constitutional Audit Report.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Constitutional Audit/CAR-001 Constitutional Audit Report.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Constitutional Audit/CAR-001 Constitutional Audit Report.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Constitutional Audit/CAR-001 Constitutional Audit Report.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Constitutional Audit/CAR-001 Constitutional Audit Report.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-001 Epoch III Constitutional Refactoring.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-001 Epoch III Constitutional Refactoring.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-001 Epoch III Constitutional Refactoring.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-001 Epoch III Constitutional Refactoring.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-001 Epoch III Constitutional Refactoring.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-002 Institutional Completeness Review.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-002 Institutional Completeness Review.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-002 Institutional Completeness Review.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-002 Institutional Completeness Review.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-002 Institutional Completeness Review.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Directive Governance Framework/Directive Governance Framework.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Directive Governance Framework/Directive Governance Framework.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Directive Governance Framework/Directive Governance Framework.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Directive Governance Framework/Directive Governance Framework.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Directive Governance Framework/Directive Governance Framework.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Epoch V/Governance Model Crosswalk.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Epoch V/Governance Model Crosswalk.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Epoch V/Governance Model Crosswalk.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Epoch V/Governance Model Crosswalk.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Epoch V/Governance Model Crosswalk.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Epoch V/Interim Authority Instrument.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Epoch V/Interim Authority Instrument.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Epoch V/Interim Authority Instrument.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Epoch V/Interim Authority Instrument.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Epoch V/Interim Authority Instrument.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Foundation Gap Report/FGR-001 Epoch II Stewardship Audit.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Foundation Gap Report/FGR-001 Epoch II Stewardship Audit.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Foundation Gap Report/FGR-001 Epoch II Stewardship Audit.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Foundation Gap Report/FGR-001 Epoch II Stewardship Audit.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Foundation Gap Report/FGR-001 Epoch II Stewardship Audit.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Founder Directives/Founder Directives Register.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Founder Directives/Founder Directives Register.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Founder Directives/Founder Directives Register.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Founder Directives/Founder Directives Register.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Founder Directives/Founder Directives Register.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Institutional Glossary & Acronym Register.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Institutional Glossary & Acronym Register.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Institutional Glossary & Acronym Register.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Institutional Glossary & Acronym Register.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Institutional Glossary & Acronym Register.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Institutional Open Questions Register.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Institutional Open Questions Register.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Institutional Open Questions Register.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Institutional Open Questions Register.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Institutional Open Questions Register.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Institutional Policies/Citation Policy.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Institutional Policies/Citation Policy.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Institutional Policies/Citation Policy.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Institutional Policies/Citation Policy.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Institutional Policies/Citation Policy.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Institutional Policies/Metadata Policy.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Institutional Policies/Metadata Policy.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Institutional Policies/Metadata Policy.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Institutional Policies/Metadata Policy.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Institutional Policies/Metadata Policy.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Institutional Policies/Naming Policy.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Institutional Policies/Naming Policy.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Institutional Policies/Naming Policy.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Institutional Policies/Naming Policy.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Institutional Policies/Naming Policy.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Institutional Policies/Privacy Policy.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Institutional Policies/Privacy Policy.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Institutional Policies/Privacy Policy.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Institutional Policies/Privacy Policy.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Institutional Policies/Privacy Policy.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Institutional Policies/Source Attribution Policy.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Institutional Policies/Source Attribution Policy.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Institutional Policies/Source Attribution Policy.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Institutional Policies/Source Attribution Policy.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Institutional Policies/Source Attribution Policy.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Institutional Policies/Versioning Policy.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Institutional Policies/Versioning Policy.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Institutional Policies/Versioning Policy.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Institutional Policies/Versioning Policy.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Institutional Policies/Versioning Policy.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Institutional Timeline.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Institutional Timeline.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Institutional Timeline.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Institutional Timeline.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Institutional Timeline.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Research Debt Register/Research Debt Register.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Research Debt Register/Research Debt Register.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Research Debt Register/Research Debt Register.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Research Debt Register/Research Debt Register.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Research Debt Register/Research Debt Register.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Research Framework/Institutional Intelligence Translation Framework v1.0.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Research Framework/Institutional Intelligence Translation Framework v1.0.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Research Framework/Institutional Intelligence Translation Framework v1.0.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Research Framework/Institutional Intelligence Translation Framework v1.0.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Research Framework/Institutional Intelligence Translation Framework v1.0.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Research Framework/Research Integration Framework.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Research Framework/Research Integration Framework.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Research Framework/Research Integration Framework.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Research Framework/Research Integration Framework.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Research Framework/Research Integration Framework.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Research Framework/Research Program Playbook v1.0.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Research Framework/Research Program Playbook v1.0.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Research Framework/Research Program Playbook v1.0.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Research Framework/Research Program Playbook v1.0.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Research Framework/Research Program Playbook v1.0.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Research Framework/Translation Checklist.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Research Framework/Translation Checklist.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Research Framework/Translation Checklist.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Research Framework/Translation Checklist.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Research Framework/Translation Checklist.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Research Framework/Translation Decision Matrix.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Research Framework/Translation Decision Matrix.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Research Framework/Translation Decision Matrix.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Research Framework/Translation Decision Matrix.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Research Framework/Translation Decision Matrix.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Research Framework/Translation Review Process.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Research Framework/Translation Review Process.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Research Framework/Translation Review Process.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Research Framework/Translation Review Process.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Research Framework/Translation Review Process.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Research Methodology/Alpha Proxima Research Methodology v1.0.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Research Methodology/Alpha Proxima Research Methodology v1.0.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Research Methodology/Alpha Proxima Research Methodology v1.0.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Research Methodology/Alpha Proxima Research Methodology v1.0.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Research Methodology/Alpha Proxima Research Methodology v1.0.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Standards Council/Standards Council Evaluation.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Standards Council/Standards Council Evaluation.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Standards Council/Standards Council Evaluation.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Standards Council/Standards Council Evaluation.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Standards Council/Standards Council Evaluation.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Missing required field: authors |
| warning | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Missing required field: related_research_programs |
| warning | `06_GOVERNANCE/Standing Orders/Standing Orders Register.md` | Missing required field: artifact_type |
| warning | `06_GOVERNANCE/Standing Orders/Standing Orders Register.md` | Missing required field: dependencies |
| warning | `06_GOVERNANCE/Standing Orders/Standing Orders Register.md` | Missing required field: institutional_owner |
| warning | `06_GOVERNANCE/Standing Orders/Standing Orders Register.md` | Missing required field: related_documents |
| warning | `06_GOVERNANCE/Standing Orders/Standing Orders Register.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/01 Research Question/RP-001 Research Question.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/01 Research Question/RP-001 Research Question.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/01 Research Question/RP-001 Research Question.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/01 Research Question/RP-001 Research Question.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/01 Research Question/RP-001 Research Question.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/02 Objectives/RP-001 Objectives.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/02 Objectives/RP-001 Objectives.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/02 Objectives/RP-001 Objectives.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/02 Objectives/RP-001 Objectives.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/02 Objectives/RP-001 Objectives.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/03 Source Registry/RP-001 Source Registry.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/03 Source Registry/RP-001 Source Registry.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/03 Source Registry/RP-001 Source Registry.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/03 Source Registry/RP-001 Source Registry.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/03 Source Registry/RP-001 Source Registry.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/04 Source - Perplexity/RP-001 Source Note - Perplexity.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/04 Source - Perplexity/RP-001 Source Note - Perplexity.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/04 Source - Perplexity/RP-001 Source Note - Perplexity.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/04 Source - Perplexity/RP-001 Source Note - Perplexity.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/04 Source - Perplexity/RP-001 Source Note - Perplexity.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/05 Source - Gemini/RP-001 Source Note - Gemini.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/05 Source - Gemini/RP-001 Source Note - Gemini.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/05 Source - Gemini/RP-001 Source Note - Gemini.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/05 Source - Gemini/RP-001 Source Note - Gemini.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/05 Source - Gemini/RP-001 Source Note - Gemini.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/06 Source - SanaLab/RP-001 Source Note - SanaLab.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/06 Source - SanaLab/RP-001 Source Note - SanaLab.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/06 Source - SanaLab/RP-001 Source Note - SanaLab.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/06 Source - SanaLab/RP-001 Source Note - SanaLab.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/06 Source - SanaLab/RP-001 Source Note - SanaLab.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/07 Future Sources/RP-001 Future Sources.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/07 Future Sources/RP-001 Future Sources.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/07 Future Sources/RP-001 Future Sources.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/07 Future Sources/RP-001 Future Sources.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/07 Future Sources/RP-001 Future Sources.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/08 Comparative Framework/RP-001 Comparative Framework.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/08 Comparative Framework/RP-001 Comparative Framework.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/08 Comparative Framework/RP-001 Comparative Framework.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/08 Comparative Framework/RP-001 Comparative Framework.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/08 Comparative Framework/RP-001 Comparative Framework.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/10 Theory Matrix/RP-001 Theory Matrix.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/10 Theory Matrix/RP-001 Theory Matrix.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/10 Theory Matrix/RP-001 Theory Matrix.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/10 Theory Matrix/RP-001 Theory Matrix.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/10 Theory Matrix/RP-001 Theory Matrix.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/11 Canonical Glossary/RP-001 Canonical Glossary.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/11 Canonical Glossary/RP-001 Canonical Glossary.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/11 Canonical Glossary/RP-001 Canonical Glossary.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/11 Canonical Glossary/RP-001 Canonical Glossary.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/11 Canonical Glossary/RP-001 Canonical Glossary.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Attention Schema Theory.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Attention Schema Theory.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Attention Schema Theory.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Attention Schema Theory.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Attention Schema Theory.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Attention Schema Theory.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Attention Schema Theory.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Attention Schema Theory.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Higher-Order Thought Theory.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Higher-Order Thought Theory.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Higher-Order Thought Theory.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Higher-Order Thought Theory.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Higher-Order Thought Theory.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Higher-Order Thought Theory.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Higher-Order Thought Theory.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Higher-Order Thought Theory.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Illusionism.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Illusionism.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Illusionism.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Illusionism.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Illusionism.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Illusionism.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Illusionism.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Illusionism.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Meta Awareness.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Meta Awareness.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Meta Awareness.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Meta Awareness.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Meta Awareness.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Meta Awareness.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Meta Awareness.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Meta Awareness.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/RP-001 Research Graph.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/RP-001 Research Graph.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/RP-001 Research Graph.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/RP-001 Research Graph.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/RP-001 Research Graph.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/14 Open Questions/RP-001 Open Questions.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/14 Open Questions/RP-001 Open Questions.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/14 Open Questions/RP-001 Open Questions.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/14 Open Questions/RP-001 Open Questions.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/14 Open Questions/RP-001 Open Questions.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/15 Future Experiments/RP-001 Future Research Opportunities.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/15 Future Experiments/RP-001 Future Research Opportunities.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/15 Future Experiments/RP-001 Future Research Opportunities.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/15 Future Experiments/RP-001 Future Research Opportunities.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/15 Future Experiments/RP-001 Future Research Opportunities.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/16 Visual Knowledge/RP-001 Visual Knowledge Index.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/16 Visual Knowledge/RP-001 Visual Knowledge Index.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/16 Visual Knowledge/RP-001 Visual Knowledge Index.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/16 Visual Knowledge/RP-001 Visual Knowledge Index.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/16 Visual Knowledge/RP-001 Visual Knowledge Index.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/17 NotebookLM Package/RP-001 NotebookLM Source Pack.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/17 NotebookLM Package/RP-001 NotebookLM Source Pack.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/17 NotebookLM Package/RP-001 NotebookLM Source Pack.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/17 NotebookLM Package/RP-001 NotebookLM Source Pack.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/17 NotebookLM Package/RP-001 NotebookLM Source Pack.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/18 Related Constitution/RP-001 Constitutional Links.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/18 Related Constitution/RP-001 Constitutional Links.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/18 Related Constitution/RP-001 Constitutional Links.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/18 Related Constitution/RP-001 Constitutional Links.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/18 Related Constitution/RP-001 Constitutional Links.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/19 Related Laws/RP-001 Governing Provisions.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/19 Related Laws/RP-001 Governing Provisions.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/19 Related Laws/RP-001 Governing Provisions.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/19 Related Laws/RP-001 Governing Provisions.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/19 Related Laws/RP-001 Governing Provisions.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/20 Related ADRs/RP-001 ADR Links.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/20 Related ADRs/RP-001 ADR Links.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/20 Related ADRs/RP-001 ADR Links.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/20 Related ADRs/RP-001 ADR Links.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/20 Related ADRs/RP-001 ADR Links.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/21 Version History/RP-001 Version History.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/21 Version History/RP-001 Version History.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/21 Version History/RP-001 Version History.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/21 Version History/RP-001 Version History.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/21 Version History/RP-001 Version History.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/ARCHIVE/ARCHIVE Philosophy.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/ARCHIVE/ARCHIVE Philosophy.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/ARCHIVE/ARCHIVE Philosophy.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/ARCHIVE/ARCHIVE Philosophy.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/ARCHIVE/ARCHIVE Philosophy.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/00 Executive Summary/RP-002 Executive Summary.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/00 Executive Summary/RP-002 Executive Summary.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/00 Executive Summary/RP-002 Executive Summary.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/00 Executive Summary/RP-002 Executive Summary.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/00 Executive Summary/RP-002 Executive Summary.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/01 Research Question/RP-002 Research Question.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/01 Research Question/RP-002 Research Question.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/01 Research Question/RP-002 Research Question.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/01 Research Question/RP-002 Research Question.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/01 Research Question/RP-002 Research Question.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/02 Objectives/RP-002 Objectives.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/02 Objectives/RP-002 Objectives.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/02 Objectives/RP-002 Objectives.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/02 Objectives/RP-002 Objectives.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/02 Objectives/RP-002 Objectives.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/03 Source Registry/RP-002 Source Registry.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/03 Source Registry/RP-002 Source Registry.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/03 Source Registry/RP-002 Source Registry.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/03 Source Registry/RP-002 Source Registry.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/03 Source Registry/RP-002 Source Registry.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/04 Source - CORE-002/RP-002 Source Note - CORE-002.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/04 Source - CORE-002/RP-002 Source Note - CORE-002.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/04 Source - CORE-002/RP-002 Source Note - CORE-002.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/04 Source - CORE-002/RP-002 Source Note - CORE-002.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/04 Source - CORE-002/RP-002 Source Note - CORE-002.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/05 Source - SanaLab/RP-002 Source Note - SanaLab.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/05 Source - SanaLab/RP-002 Source Note - SanaLab.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/05 Source - SanaLab/RP-002 Source Note - SanaLab.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/05 Source - SanaLab/RP-002 Source Note - SanaLab.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/05 Source - SanaLab/RP-002 Source Note - SanaLab.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/06 Source - Illustrated/RP-002 Source Note - Illustrated.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/06 Source - Illustrated/RP-002 Source Note - Illustrated.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/06 Source - Illustrated/RP-002 Source Note - Illustrated.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/06 Source - Illustrated/RP-002 Source Note - Illustrated.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/06 Source - Illustrated/RP-002 Source Note - Illustrated.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/07 Future Sources/RP-002 Future Sources.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/07 Future Sources/RP-002 Future Sources.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/07 Future Sources/RP-002 Future Sources.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/07 Future Sources/RP-002 Future Sources.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/07 Future Sources/RP-002 Future Sources.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/08 Comparative Framework/RP-002 Comparative Framework.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/08 Comparative Framework/RP-002 Comparative Framework.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/08 Comparative Framework/RP-002 Comparative Framework.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/08 Comparative Framework/RP-002 Comparative Framework.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/08 Comparative Framework/RP-002 Comparative Framework.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/09 Canonical Synthesis/RP-002 Canonical Synthesis.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/09 Canonical Synthesis/RP-002 Canonical Synthesis.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/09 Canonical Synthesis/RP-002 Canonical Synthesis.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/09 Canonical Synthesis/RP-002 Canonical Synthesis.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/09 Canonical Synthesis/RP-002 Canonical Synthesis.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/10 Theory Matrix/RP-002 Theory Matrix.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/10 Theory Matrix/RP-002 Theory Matrix.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/10 Theory Matrix/RP-002 Theory Matrix.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/10 Theory Matrix/RP-002 Theory Matrix.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/10 Theory Matrix/RP-002 Theory Matrix.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/11 Canonical Glossary/RP-002 Canonical Glossary.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/11 Canonical Glossary/RP-002 Canonical Glossary.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/11 Canonical Glossary/RP-002 Canonical Glossary.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/11 Canonical Glossary/RP-002 Canonical Glossary.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/11 Canonical Glossary/RP-002 Canonical Glossary.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/12 Evidence Registry/RP-002 Evidence Registry.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/12 Evidence Registry/RP-002 Evidence Registry.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/12 Evidence Registry/RP-002 Evidence Registry.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/12 Evidence Registry/RP-002 Evidence Registry.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/12 Evidence Registry/RP-002 Evidence Registry.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Collective Memory.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Collective Memory.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Collective Memory.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Collective Memory.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Collective Memory.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Collective Memory.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Collective Memory.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Collective Memory.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Contemplative Memory.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Contemplative Memory.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Contemplative Memory.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Contemplative Memory.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Contemplative Memory.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Contemplative Memory.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Contemplative Memory.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Contemplative Memory.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Engram.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Engram.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Engram.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Engram.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Engram.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Engram.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Engram.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Engram.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Hippocampus.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Hippocampus.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Hippocampus.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Hippocampus.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Hippocampus.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Hippocampus.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Hippocampus.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Hippocampus.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/LTP - Synaptic Plasticity.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/LTP - Synaptic Plasticity.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/LTP - Synaptic Plasticity.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/LTP - Synaptic Plasticity.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/LTP - Synaptic Plasticity.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/LTP - Synaptic Plasticity.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/LTP - Synaptic Plasticity.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/LTP - Synaptic Plasticity.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Memory.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Memory.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Memory.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Memory.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Memory.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Memory.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Memory.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Memory.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Pattern Separation and Completion.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Pattern Separation and Completion.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Pattern Separation and Completion.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Pattern Separation and Completion.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Pattern Separation and Completion.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Pattern Separation and Completion.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Pattern Separation and Completion.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Pattern Separation and Completion.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Reconsolidation.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Reconsolidation.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Reconsolidation.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Reconsolidation.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Reconsolidation.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Reconsolidation.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Reconsolidation.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Reconsolidation.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Trauma Memory.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Trauma Memory.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Trauma Memory.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Trauma Memory.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Trauma Memory.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Trauma Memory.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Trauma Memory.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Trauma Memory.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Working Memory.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Working Memory.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Working Memory.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Working Memory.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Working Memory.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Working Memory.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Working Memory.md` | Missing required field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Working Memory.md` | Missing required field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/RP-002 Research Graph.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/RP-002 Research Graph.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/RP-002 Research Graph.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/RP-002 Research Graph.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/RP-002 Research Graph.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/14 Open Questions/RP-002 Open Questions.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/14 Open Questions/RP-002 Open Questions.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/14 Open Questions/RP-002 Open Questions.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/14 Open Questions/RP-002 Open Questions.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/14 Open Questions/RP-002 Open Questions.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/15 Future Experiments/RP-002 Future Research Opportunities.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/15 Future Experiments/RP-002 Future Research Opportunities.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/15 Future Experiments/RP-002 Future Research Opportunities.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/15 Future Experiments/RP-002 Future Research Opportunities.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/15 Future Experiments/RP-002 Future Research Opportunities.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/16 Visual Knowledge/RP-002 Visual Knowledge Index.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/16 Visual Knowledge/RP-002 Visual Knowledge Index.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/16 Visual Knowledge/RP-002 Visual Knowledge Index.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/16 Visual Knowledge/RP-002 Visual Knowledge Index.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/16 Visual Knowledge/RP-002 Visual Knowledge Index.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/17 NotebookLM Package/RP-002 NotebookLM Source Pack.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/17 NotebookLM Package/RP-002 NotebookLM Source Pack.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/17 NotebookLM Package/RP-002 NotebookLM Source Pack.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/17 NotebookLM Package/RP-002 NotebookLM Source Pack.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/17 NotebookLM Package/RP-002 NotebookLM Source Pack.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/18 Related Constitution/RP-002 Constitutional Links.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/18 Related Constitution/RP-002 Constitutional Links.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/18 Related Constitution/RP-002 Constitutional Links.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/18 Related Constitution/RP-002 Constitutional Links.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/18 Related Constitution/RP-002 Constitutional Links.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/19 Related Laws/RP-002 Governing Provisions.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/19 Related Laws/RP-002 Governing Provisions.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/19 Related Laws/RP-002 Governing Provisions.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/19 Related Laws/RP-002 Governing Provisions.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/19 Related Laws/RP-002 Governing Provisions.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/20 Related ADRs/RP-002 ADR Links.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/20 Related ADRs/RP-002 ADR Links.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/20 Related ADRs/RP-002 ADR Links.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/20 Related ADRs/RP-002 ADR Links.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/20 Related ADRs/RP-002 ADR Links.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/21 Version History/RP-002 Version History.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/21 Version History/RP-002 Version History.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/21 Version History/RP-002 Version History.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/21 Version History/RP-002 Version History.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/21 Version History/RP-002 Version History.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/ARCHIVE/ARCHIVE Philosophy.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/ARCHIVE/ARCHIVE Philosophy.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/ARCHIVE/ARCHIVE Philosophy.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/ARCHIVE/ARCHIVE Philosophy.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/ARCHIVE/ARCHIVE Philosophy.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-A Architecture Systemique Memoire Humaine.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-A Architecture Systemique Memoire Humaine.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-A Architecture Systemique Memoire Humaine.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-A Architecture Systemique Memoire Humaine.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-A Architecture Systemique Memoire Humaine.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-A Architecture Systemique Memoire Humaine.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-B Interdisciplinary Comparative Framework Memory.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-B Interdisciplinary Comparative Framework Memory.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-B Interdisciplinary Comparative Framework Memory.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-B Interdisciplinary Comparative Framework Memory.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-B Interdisciplinary Comparative Framework Memory.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-B Interdisciplinary Comparative Framework Memory.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-C RP-002 Illustrated.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-C RP-002 Illustrated.md` | Missing required field: authors |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-C RP-002 Illustrated.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-C RP-002 Illustrated.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-C RP-002 Illustrated.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-C RP-002 Illustrated.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Canonical Synthesis.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Canonical Synthesis.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Canonical Synthesis.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Canonical Synthesis.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Canonical Synthesis.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Institutional Synthesis Report.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Institutional Synthesis Report.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Institutional Synthesis Report.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Institutional Synthesis Report.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Institutional Synthesis Report.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Knowledge Graph Update Recommendations.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Knowledge Graph Update Recommendations.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Knowledge Graph Update Recommendations.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Knowledge Graph Update Recommendations.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Knowledge Graph Update Recommendations.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-003/RP-003 Master Index.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-003/RP-003 Master Index.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-003/RP-003 Master Index.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-003/RP-003 Master Index.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-003/RP-003 Master Index.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-004/RP-004 Master Index.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-004/RP-004 Master Index.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-004/RP-004 Master Index.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-004/RP-004 Master Index.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-004/RP-004 Master Index.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-005/RP-005 Master Index.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-005/RP-005 Master Index.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-005/RP-005 Master Index.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-005/RP-005 Master Index.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-005/RP-005 Master Index.md` | Missing required field: related_research_programs |
| warning | `07_RESEARCH/RP-006/RP-006 Master Index.md` | Missing required field: artifact_type |
| warning | `07_RESEARCH/RP-006/RP-006 Master Index.md` | Missing required field: dependencies |
| warning | `07_RESEARCH/RP-006/RP-006 Master Index.md` | Missing required field: institutional_owner |
| warning | `07_RESEARCH/RP-006/RP-006 Master Index.md` | Missing required field: related_documents |
| warning | `07_RESEARCH/RP-006/RP-006 Master Index.md` | Missing required field: related_research_programs |
| warning | `08_SYSTEMS/Alpha Proxima Operating Model v1.0.md` | Missing required field: artifact_type |
| warning | `08_SYSTEMS/Alpha Proxima Operating Model v1.0.md` | Missing required field: dependencies |
| warning | `08_SYSTEMS/Alpha Proxima Operating Model v1.0.md` | Missing required field: institutional_owner |
| warning | `08_SYSTEMS/Alpha Proxima Operating Model v1.0.md` | Missing required field: related_documents |
| warning | `08_SYSTEMS/Alpha Proxima Operating Model v1.0.md` | Missing required field: related_research_programs |
| warning | `08_SYSTEMS/Automation/Vault Note Generator.md` | Missing required field: artifact_type |
| warning | `08_SYSTEMS/Automation/Vault Note Generator.md` | Missing required field: institutional_owner |
| warning | `08_SYSTEMS/Foundational Architecture.md` | Missing required field: artifact_type |
| warning | `08_SYSTEMS/Foundational Architecture.md` | Missing required field: dependencies |
| warning | `08_SYSTEMS/Foundational Architecture.md` | Missing required field: institutional_owner |
| warning | `08_SYSTEMS/Foundational Architecture.md` | Missing required field: related_documents |
| warning | `08_SYSTEMS/Foundational Architecture.md` | Missing required field: related_research_programs |
| warning | `08_SYSTEMS/Institutional Relationship Map.md` | Missing required field: artifact_type |
| warning | `08_SYSTEMS/Institutional Relationship Map.md` | Missing required field: dependencies |
| warning | `08_SYSTEMS/Institutional Relationship Map.md` | Missing required field: institutional_owner |
| warning | `08_SYSTEMS/Institutional Relationship Map.md` | Missing required field: related_documents |
| warning | `08_SYSTEMS/Institutional Relationship Map.md` | Missing required field: related_research_programs |
| warning | `08_SYSTEMS/LUMIAION Architecture Spec v0.1.md` | Missing required field: artifact_type |
| warning | `08_SYSTEMS/LUMIAION Architecture Spec v0.1.md` | Missing required field: dependencies |
| warning | `08_SYSTEMS/LUMIAION Architecture Spec v0.1.md` | Missing required field: institutional_owner |
| warning | `08_SYSTEMS/LUMIAION Architecture Spec v0.1.md` | Missing required field: related_documents |
| warning | `08_SYSTEMS/LUMIAION Architecture Spec v0.1.md` | Missing required field: related_research_programs |
| warning | `08_SYSTEMS/Protocols/Communication Protocol.md` | Missing required field: artifact_type |
| warning | `08_SYSTEMS/Protocols/Communication Protocol.md` | Missing required field: dependencies |
| warning | `08_SYSTEMS/Protocols/Communication Protocol.md` | Missing required field: institutional_owner |
| warning | `08_SYSTEMS/Protocols/Communication Protocol.md` | Missing required field: related_documents |
| warning | `08_SYSTEMS/Protocols/Communication Protocol.md` | Missing required field: related_research_programs |
| warning | `08_SYSTEMS/Protocols/Decision Routing Protocol.md` | Missing required field: artifact_type |
| warning | `08_SYSTEMS/Protocols/Decision Routing Protocol.md` | Missing required field: dependencies |
| warning | `08_SYSTEMS/Protocols/Decision Routing Protocol.md` | Missing required field: institutional_owner |
| warning | `08_SYSTEMS/Protocols/Decision Routing Protocol.md` | Missing required field: related_documents |
| warning | `08_SYSTEMS/Protocols/Decision Routing Protocol.md` | Missing required field: related_research_programs |
| warning | `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` | Missing required field: artifact_type |
| warning | `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` | Missing required field: dependencies |
| warning | `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` | Missing required field: institutional_owner |
| warning | `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` | Missing required field: related_documents |
| warning | `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` | Missing required field: related_research_programs |
| warning | `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` | Missing required field: artifact_type |
| warning | `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` | Missing required field: dependencies |
| warning | `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` | Missing required field: institutional_owner |
| warning | `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` | Missing required field: related_documents |
| warning | `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` | Missing required field: related_research_programs |
| warning | `08_SYSTEMS/Protocols/Research Governance Protocol.md` | Missing required field: artifact_type |
| warning | `08_SYSTEMS/Protocols/Research Governance Protocol.md` | Missing required field: dependencies |
| warning | `08_SYSTEMS/Protocols/Research Governance Protocol.md` | Missing required field: institutional_owner |
| warning | `08_SYSTEMS/Protocols/Research Governance Protocol.md` | Missing required field: related_documents |
| warning | `08_SYSTEMS/Protocols/Research Governance Protocol.md` | Missing required field: related_research_programs |
| warning | `08_SYSTEMS/The Orchestration Framework.md` | Missing required field: artifact_type |
| warning | `08_SYSTEMS/The Orchestration Framework.md` | Missing required field: dependencies |
| warning | `08_SYSTEMS/The Orchestration Framework.md` | Missing required field: institutional_owner |
| warning | `08_SYSTEMS/The Orchestration Framework.md` | Missing required field: related_documents |
| warning | `08_SYSTEMS/The Orchestration Framework.md` | Missing required field: related_research_programs |
| warning | `08_SYSTEMS/Visual Systems/Color System - Implementation Checklist.md` | Missing required field: related_research_programs |
| warning | `09_OFFICES/Engineering Office/Engineering Office Charter.md` | Missing required field: artifact_type |
| warning | `09_OFFICES/Engineering Office/Engineering Office Charter.md` | Missing required field: dependencies |
| warning | `09_OFFICES/Engineering Office/Engineering Office Charter.md` | Missing required field: institutional_owner |
| warning | `09_OFFICES/Engineering Office/Engineering Office Charter.md` | Missing required field: related_documents |
| warning | `09_OFFICES/Engineering Office/Engineering Office Charter.md` | Missing required field: related_research_programs |
| warning | `09_OFFICES/Ethics Council/Ethics Council Charter.md` | Missing required field: artifact_type |
| warning | `09_OFFICES/Ethics Council/Ethics Council Charter.md` | Missing required field: dependencies |
| warning | `09_OFFICES/Ethics Council/Ethics Council Charter.md` | Missing required field: institutional_owner |
| warning | `09_OFFICES/Ethics Council/Ethics Council Charter.md` | Missing required field: related_documents |
| warning | `09_OFFICES/Ethics Council/Ethics Council Charter.md` | Missing required field: related_research_programs |
| warning | `09_OFFICES/Executive Office/Executive Office Charter.md` | Missing required field: artifact_type |
| warning | `09_OFFICES/Executive Office/Executive Office Charter.md` | Missing required field: dependencies |
| warning | `09_OFFICES/Executive Office/Executive Office Charter.md` | Missing required field: institutional_owner |
| warning | `09_OFFICES/Executive Office/Executive Office Charter.md` | Missing required field: related_documents |
| warning | `09_OFFICES/Executive Office/Executive Office Charter.md` | Missing required field: related_research_programs |
| warning | `09_OFFICES/Institutional Observatory/Institutional Observatory Charter.md` | Missing required field: artifact_type |
| warning | `09_OFFICES/Institutional Observatory/Institutional Observatory Charter.md` | Missing required field: dependencies |
| warning | `09_OFFICES/Institutional Observatory/Institutional Observatory Charter.md` | Missing required field: institutional_owner |
| warning | `09_OFFICES/Institutional Observatory/Institutional Observatory Charter.md` | Missing required field: related_documents |
| warning | `09_OFFICES/Institutional Observatory/Institutional Observatory Charter.md` | Missing required field: related_research_programs |
| warning | `09_OFFICES/LUMIAION/LUMIAION Charter.md` | Missing required field: artifact_type |
| warning | `09_OFFICES/LUMIAION/LUMIAION Charter.md` | Missing required field: dependencies |
| warning | `09_OFFICES/LUMIAION/LUMIAION Charter.md` | Missing required field: institutional_owner |
| warning | `09_OFFICES/LUMIAION/LUMIAION Charter.md` | Missing required field: related_documents |
| warning | `09_OFFICES/LUMIAION/LUMIAION Charter.md` | Missing required field: related_research_programs |
| warning | `09_OFFICES/Research Intelligence Office/Research Intelligence Office Charter.md` | Missing required field: artifact_type |
| warning | `09_OFFICES/Research Intelligence Office/Research Intelligence Office Charter.md` | Missing required field: dependencies |
| warning | `09_OFFICES/Research Intelligence Office/Research Intelligence Office Charter.md` | Missing required field: institutional_owner |
| warning | `09_OFFICES/Research Intelligence Office/Research Intelligence Office Charter.md` | Missing required field: related_documents |
| warning | `09_OFFICES/Research Intelligence Office/Research Intelligence Office Charter.md` | Missing required field: related_research_programs |
| warning | `09_OFFICES/Research Intelligence Office/Research Office Matrix.md` | Missing required field: artifact_type |
| warning | `09_OFFICES/Research Intelligence Office/Research Office Matrix.md` | Missing required field: dependencies |
| warning | `09_OFFICES/Research Intelligence Office/Research Office Matrix.md` | Missing required field: institutional_owner |
| warning | `09_OFFICES/Research Intelligence Office/Research Office Matrix.md` | Missing required field: related_documents |
| warning | `09_OFFICES/Research Intelligence Office/Research Office Matrix.md` | Missing required field: related_research_programs |
| warning | `10_TEMPLATES/ADR Template.md` | Missing required field: artifact_type |
| warning | `10_TEMPLATES/ADR Template.md` | Missing required field: dependencies |
| warning | `10_TEMPLATES/ADR Template.md` | Missing required field: institutional_owner |
| warning | `10_TEMPLATES/ADR Template.md` | Missing required field: related_documents |
| warning | `10_TEMPLATES/ADR Template.md` | Missing required field: related_research_programs |
| warning | `10_TEMPLATES/Concept Note Template.md` | Missing required field: artifact_type |
| warning | `10_TEMPLATES/Concept Note Template.md` | Missing required field: dependencies |
| warning | `10_TEMPLATES/Concept Note Template.md` | Missing required field: institutional_owner |
| warning | `10_TEMPLATES/Concept Note Template.md` | Missing required field: related_documents |
| warning | `10_TEMPLATES/Concept Note Template.md` | Missing required field: related_research_programs |
| warning | `10_TEMPLATES/Implementation Note Template.md` | Missing required field: artifact_type |
| warning | `10_TEMPLATES/Implementation Note Template.md` | Missing required field: dependencies |
| warning | `10_TEMPLATES/Implementation Note Template.md` | Missing required field: institutional_owner |
| warning | `10_TEMPLATES/Institutional Translation Template v1.0.md` | Missing required field: artifact_type |
| warning | `10_TEMPLATES/Institutional Translation Template v1.0.md` | Missing required field: dependencies |
| warning | `10_TEMPLATES/Institutional Translation Template v1.0.md` | Missing required field: institutional_owner |
| warning | `10_TEMPLATES/Institutional Translation Template v1.0.md` | Missing required field: related_documents |
| warning | `10_TEMPLATES/Institutional Translation Template v1.0.md` | Missing required field: related_research_programs |
| warning | `10_TEMPLATES/Research Commission Template v2.0.md` | Missing required field: artifact_type |
| warning | `10_TEMPLATES/Research Commission Template v2.0.md` | Missing required field: dependencies |
| warning | `10_TEMPLATES/Research Commission Template v2.0.md` | Missing required field: institutional_owner |
| warning | `10_TEMPLATES/Research Commission Template v2.0.md` | Missing required field: related_documents |
| warning | `10_TEMPLATES/Research Commission Template v2.0.md` | Missing required field: related_research_programs |
| warning | `10_TEMPLATES/Research Note Template.md` | Missing required field: artifact_type |
| warning | `10_TEMPLATES/Research Note Template.md` | Missing required field: dependencies |
| warning | `10_TEMPLATES/Research Note Template.md` | Missing required field: institutional_owner |
| warning | `10_TEMPLATES/Research Note Template.md` | Missing required field: related_documents |
| warning | `10_TEMPLATES/Research Note Template.md` | Missing required field: related_research_programs |
| warning | `10_TEMPLATES/Research Program Template/Research Program Methodology.md` | Missing required field: artifact_type |
| warning | `10_TEMPLATES/Research Program Template/Research Program Methodology.md` | Missing required field: dependencies |
| warning | `10_TEMPLATES/Research Program Template/Research Program Methodology.md` | Missing required field: institutional_owner |
| warning | `10_TEMPLATES/Research Program Template/Research Program Methodology.md` | Missing required field: related_documents |
| warning | `10_TEMPLATES/Research Program Template/Research Program Methodology.md` | Missing required field: related_research_programs |
| warning | `10_TEMPLATES/Vault Structure Convention.md` | Missing required field: artifact_type |
| warning | `10_TEMPLATES/Vault Structure Convention.md` | Missing required field: dependencies |
| warning | `10_TEMPLATES/Vault Structure Convention.md` | Missing required field: institutional_owner |
| warning | `10_TEMPLATES/Vault Structure Convention.md` | Missing required field: related_documents |
| warning | `10_TEMPLATES/Vault Structure Convention.md` | Missing required field: related_research_programs |
| warning | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Missing required field: aliases |
| warning | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Missing required field: artifact_type |
| warning | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Missing required field: authors |
| warning | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Missing required field: dependencies |
| warning | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Missing required field: institutional_owner |
| warning | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Missing required field: related_documents |
| warning | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Missing required field: related_research_programs |
| warning | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Missing required field: updated |
| warning | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Missing required field: version |
| warning | `Alpha Proxima Core.md` | Missing required field: artifact_type |
| warning | `Alpha Proxima Core.md` | Missing required field: dependencies |
| warning | `Alpha Proxima Core.md` | Missing required field: institutional_owner |
| warning | `Alpha Proxima Core.md` | Missing required field: related_documents |
| warning | `Alpha Proxima Core.md` | Missing required field: related_research_programs |
| warning | `LUMIAION.md` | Missing required field: artifact_type |
| warning | `LUMIAION.md` | Missing required field: dependencies |
| warning | `LUMIAION.md` | Missing required field: institutional_owner |
| warning | `LUMIAION.md` | Missing required field: related_documents |
| warning | `LUMIAION.md` | Missing required field: related_research_programs |
| warning | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Missing required field: aliases |
| warning | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Missing required field: artifact_type |
| warning | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Missing required field: authors |
| warning | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Missing required field: created |
| warning | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Missing required field: dependencies |
| warning | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Missing required field: institutional_owner |
| warning | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Missing required field: related_documents |
| warning | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Missing required field: related_research_programs |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Missing required field: artifact_type |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Missing required field: dependencies |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Missing required field: institutional_owner |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Missing required field: related_documents |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Missing required field: related_research_programs |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Missing required field: aliases |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Missing required field: artifact_type |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Missing required field: authors |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Missing required field: created |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Missing required field: dependencies |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Missing required field: institutional_owner |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Missing required field: related_documents |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Missing required field: related_research_programs |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Missing required field: title |
| warning | `OSG_LAUNCH/00_REPOSITORY/GitHub Best Practices.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/00_REPOSITORY/GitHub Best Practices.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/00_REPOSITORY/OSG Academy Engineering Review.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/00_REPOSITORY/OSG Academy Engineering Review.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/00_REPOSITORY/README.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/00_REPOSITORY/README.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/00_REPOSITORY/Repository Structure.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/00_REPOSITORY/Repository Structure.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/01_NOTION_WORKSPACE/Notion Workspace Architecture.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/01_NOTION_WORKSPACE/Notion Workspace Architecture.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/01_NOTION_WORKSPACE/README.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/01_NOTION_WORKSPACE/README.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/02_COURSES/Course Folder Hierarchy.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/02_COURSES/Course Folder Hierarchy.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/02_COURSES/README.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/02_COURSES/README.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/03_MEDIA/README.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/03_MEDIA/README.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/04_CLIENTS/Client Folder Hierarchy.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/04_CLIENTS/Client Folder Hierarchy.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/04_CLIENTS/README.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/04_CLIENTS/README.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/05_CONTENT/Content Workflow.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/05_CONTENT/Content Workflow.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/05_CONTENT/README.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/05_CONTENT/README.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/06_AUTOMATION/Automation Opportunities.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/06_AUTOMATION/Automation Opportunities.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/06_AUTOMATION/README.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/06_AUTOMATION/README.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/07_OPERATIONS/Launch Operations Model.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/07_OPERATIONS/Launch Operations Model.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/07_OPERATIONS/README.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/07_OPERATIONS/README.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/08_ROADMAP/30 Day Implementation Roadmap.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/08_ROADMAP/30 Day Implementation Roadmap.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/08_ROADMAP/README.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/08_ROADMAP/README.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/09_TEMPLATES/Automation Spec Template.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/09_TEMPLATES/Automation Spec Template.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/09_TEMPLATES/Client Template.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/09_TEMPLATES/Client Template.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/09_TEMPLATES/Content Item Template.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/09_TEMPLATES/Content Item Template.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/09_TEMPLATES/Course Template.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/09_TEMPLATES/Course Template.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/09_TEMPLATES/Naming Conventions.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/09_TEMPLATES/Naming Conventions.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/09_TEMPLATES/README.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/09_TEMPLATES/README.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/10_ACADEMY/AIG/Awaken the Inner Guru Recording Start Guide.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/10_ACADEMY/AIG/README.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/10_ACADEMY/README.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/10_ACADEMY/README.md` | Missing required field: authors |
| warning | `OSG_LAUNCH/README.md` | Missing required field: aliases |
| warning | `OSG_LAUNCH/README.md` | Missing required field: authors |
| warning | `PROJECT_GENOME/Genome Constitution v1.0.md` | Missing required field: artifact_type |
| warning | `PROJECT_GENOME/Genome Constitution v1.0.md` | Missing required field: dependencies |
| warning | `PROJECT_GENOME/Genome Constitution v1.0.md` | Missing required field: institutional_owner |
| warning | `PROJECT_GENOME/Genome Constitution v1.0.md` | Missing required field: related_documents |
| warning | `PROJECT_GENOME/Genome Constitution v1.0.md` | Missing required field: related_research_programs |
| warning | `PROJECT_GENOME/Project Genome Master Index.md` | Missing required field: artifact_type |
| warning | `PROJECT_GENOME/Project Genome Master Index.md` | Missing required field: dependencies |
| warning | `PROJECT_GENOME/Project Genome Master Index.md` | Missing required field: institutional_owner |
| warning | `PROJECT_GENOME/Project Genome Master Index.md` | Missing required field: related_documents |
| warning | `PROJECT_GENOME/Project Genome Master Index.md` | Missing required field: related_research_programs |

### missing_yaml

| Severity | Path | Message |
|----------|------|---------|
| error | `Awaken the Inner Guru Production Folder.md` | Markdown note does not start with YAML frontmatter. |
| error | `OSG_BUSINESS/00 OSG Business Foundation — Overview.md` | Markdown note does not start with YAML frontmatter. |
| error | `OSG_BUSINESS/01 Flagship Course.md` | Markdown note does not start with YAML frontmatter. |
| error | `OSG_BUSINESS/02 Coaching Offers.md` | Markdown note does not start with YAML frontmatter. |
| error | `OSG_BUSINESS/03 Website Copy.md` | Markdown note does not start with YAML frontmatter. |
| error | `OSG_BUSINESS/04 Client Journey & Onboarding.md` | Markdown note does not start with YAML frontmatter. |
| error | `OSG_BUSINESS/05 Email Sequences.md` | Markdown note does not start with YAML frontmatter. |
| error | `OSG_BUSINESS/06 Community Onboarding.md` | Markdown note does not start with YAML frontmatter. |
| error | `OSG_BUSINESS/07 30-Day Launch Checklist.md` | Markdown note does not start with YAML frontmatter. |
| error | `Omi/Memories.md` | Markdown note does not start with YAML frontmatter. |
| error | `Sans titre 1.md` | Markdown note does not start with YAML frontmatter. |
| error | `Sans titre.md` | Markdown note does not start with YAML frontmatter. |
| error | `Vault.md` | Markdown note does not start with YAML frontmatter. |
| error | `docs/constitution/LUMIAION_CONSTITUTION.md` | Markdown note does not start with YAML frontmatter. |
| error | `docs/constitution/README.md` | Markdown note does not start with YAML frontmatter. |
| error | `docs/setup/Claude-Code-in-Obsidian.md` | Markdown note does not start with YAML frontmatter. |

### title_mismatch

| Severity | Path | Message |
|----------|------|---------|
| info | `00_CONSTITUTION/Book I - The Constitution.md` | Frontmatter title `Book I - The Constitution` does not match H1 `Book I — The Constitution of Alpha Proxima Core`. |
| info | `00_CONSTITUTION/Book II - Governance Framework.md` | Frontmatter title `Book II - Governance Framework` does not match H1 `Book II — Governance Framework of the Alpha Proxima Foundation`. |
| info | `00_CONSTITUTION/Book III - Knowledge Integrity.md` | Frontmatter title `Book III - Knowledge Integrity` does not match H1 `Book III — Knowledge Integrity`. |
| info | `00_CONSTITUTION/Book IV - Cognitive Architecture.md` | Frontmatter title `Book IV - Cognitive Architecture` does not match H1 `Book IV — Cognitive Architecture of the Alpha Proxima Foundation`. |
| info | `00_CONSTITUTION/Book V - Cognitive Council.md` | Frontmatter title `Book V - Cognitive Council` does not match H1 `Book V — The Cognitive Council of the Alpha Proxima Foundation`. |
| info | `03_AI_COUNCIL/Departments/ATHENA Charter.md` | Frontmatter title `ATHENA Charter` does not match H1 `ATHENA Charter — Department of Health and Human Performance`. |
| info | `03_AI_COUNCIL/Departments/JERANIUM Charter.md` | Frontmatter title `JERANIUM Charter` does not match H1 `JERANIUM Charter — Department of Knowledge and Institutional Intelligence`. |
| info | `03_AI_COUNCIL/Departments/LUMIAION Charter.md` | Frontmatter title `LUMIAION Charter` does not match H1 `LUMIAION Charter — Living Intelligence Core (v1.0.0 — Archived)`. |
| info | `03_AI_COUNCIL/Departments/SOHMA Charter.md` | Frontmatter title `SOHMA Charter` does not match H1 `SOHMA Charter — Department of Consciousness and Meaning`. |
| info | `03_AI_COUNCIL/Departments/VORTEX Charter.md` | Frontmatter title `VORTEX Charter` does not match H1 `VORTEX Charter — Department of Finance and Economic Strategy`. |
| info | `03_AI_COUNCIL/YUNA Charter.md` | Frontmatter title `YUNA Charter` does not match H1 `YUNA Charter — Universal Synthesis, Education & Wisdom Mapping`. |
| info | `04_DECISIONS/ADR-0001 - The Founding Decision.md` | Frontmatter title `ADR-0001 - The Founding Decision` does not match H1 `ADR-0001 — The Founding Decision`. |
| info | `04_DECISIONS/ADR-0002 - Reconciling the Four Institutional Taxonomies.md` | Frontmatter title `ADR-0002 - Reconciling the Four Institutional Taxonomies` does not match H1 `ADR-0002 — Reconciling the Four Institutional Taxonomies`. |
| info | `04_DECISIONS/ADR-0003 - PR47 Source-Scoped Reference Contract.md` | Frontmatter title `ADR-0003 - PR47 Source-Scoped Reference Contract` does not match H1 `ADR-0003 — PR47 Source-Scoped Reference Contract`. |
| info | `05_PROPOSALS/CN-0001 - Constitutional Alignment Gap Report.md` | Frontmatter title `CN-0001 - Constitutional Alignment Gap Report` does not match H1 `CN-0001 — Constitutional Alignment Gap Report`. |
| info | `05_PROPOSALS/CN-001 Execution Tracker.md` | Frontmatter title `CN-001 Execution Tracker` does not match H1 `CN-001 — Execution Tracker & Attribution Ledger`. |
| info | `05_PROPOSALS/Live Layer Reconciliation - PR51 vs PR52-53.md` | Frontmatter title `Live Layer Reconciliation - PR51 vs PR52-53` does not match H1 `Live Layer Reconciliation — PR #51 vs PR #52/#53`. |
| info | `06_GOVERNANCE/Constitutional Audit/CAR-001 Constitutional Audit Report.md` | Frontmatter title `CAR-001 Constitutional Audit Report` does not match H1 `CAR-001 — Constitutional Audit Report`. |
| info | `06_GOVERNANCE/Constitutional Impact Report/CIR-001 Epoch III Constitutional Refactoring.md` | Frontmatter title `CIR-001 — Epoch III Constitutional Refactoring` does not match H1 `CIR-001 — Constitutional Impact Report`. |
| info | `06_GOVERNANCE/Constitutional Impact Report/CIR-003 Epoch V Constitutional Coherence.md` | Frontmatter title `CIR-003 Epoch V — Constitutional Coherence` does not match H1 `CIR-003 — Epoch V: Constitutional Coherence`. |
| info | `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | Frontmatter title `RP-001 Executive Summary` does not match H1 `RP-001 — Executive Summary`. |
| info | `07_RESEARCH/RP-001/01 Research Question/RP-001 Research Question.md` | Frontmatter title `RP-001 Research Question` does not match H1 `RP-001 — Research Question`. |
| info | `07_RESEARCH/RP-001/02 Objectives/RP-001 Objectives.md` | Frontmatter title `RP-001 Objectives` does not match H1 `RP-001 — Objectives`. |
| info | `07_RESEARCH/RP-001/03 Source Registry/RP-001 Source Registry.md` | Frontmatter title `RP-001 Source Registry` does not match H1 `RP-001 — Source Registry`. |
| info | `07_RESEARCH/RP-001/04 Source - Perplexity/RP-001 Source Note - Perplexity.md` | Frontmatter title `RP-001 Source Note — Perplexity` does not match H1 `RP-001 — Source Note: Perplexity (DOC-001)`. |
| info | `07_RESEARCH/RP-001/05 Source - Gemini/RP-001 Source Note - Gemini.md` | Frontmatter title `RP-001 Source Note — Gemini` does not match H1 `RP-001 — Source Note: Gemini (DOC-002)`. |
| info | `07_RESEARCH/RP-001/06 Source - SanaLab/RP-001 Source Note - SanaLab.md` | Frontmatter title `RP-001 Source Note — SanaLab` does not match H1 `RP-001 — Source Note: SanaLab (DOC-003, DOC-004)`. |
| info | `07_RESEARCH/RP-001/07 Future Sources/RP-001 Future Sources.md` | Frontmatter title `RP-001 Future Sources` does not match H1 `RP-001 — Future Sources`. |
| info | `07_RESEARCH/RP-001/08 Comparative Framework/RP-001 Comparative Framework.md` | Frontmatter title `RP-001 Comparative Framework` does not match H1 `RP-001 — Comparative Framework`. |
| info | `07_RESEARCH/RP-001/09 Canonical Synthesis/RP-001 Canonical Synthesis.md` | Frontmatter title `RP-001 Canonical Synthesis` does not match H1 `RP-001 — Canonical Synthesis`. |
| info | `07_RESEARCH/RP-001/10 Theory Matrix/RP-001 Theory Matrix.md` | Frontmatter title `RP-001 Consciousness Theory Matrix` does not match H1 `RP-001 — Consciousness Theory Matrix`. |
| info | `07_RESEARCH/RP-001/11 Canonical Glossary/RP-001 Canonical Glossary.md` | Frontmatter title `RP-001 Canonical Glossary` does not match H1 `RP-001 — Canonical Glossary`. |
| info | `07_RESEARCH/RP-001/12 Evidence Registry/RP-001 Evidence Registry.md` | Frontmatter title `RP-001 Evidence Registry` does not match H1 `RP-001 — Evidence Registry`. |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | Frontmatter title `4E Cognition` does not match H1 `4E Cognition (Embodied / Embedded / Enacted / Extended)`. |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | Frontmatter title `Active Inference` does not match H1 `Active Inference (Free Energy Principle)`. |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Attention Schema Theory.md` | Frontmatter title `Attention Schema Theory` does not match H1 `Attention Schema Theory (AST)`. |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network.md` | Frontmatter title `Default Mode Network` does not match H1 `Default Mode Network (DMN)`. |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | Frontmatter title `Global Neuronal Workspace Theory` does not match H1 `Global Neuronal Workspace Theory (GNWT)`. |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Higher-Order Thought Theory.md` | Frontmatter title `Higher-Order Thought Theory` does not match H1 `Higher-Order Thought Theory (HOT)`. |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | Frontmatter title `Integrated Information Theory` does not match H1 `Integrated Information Theory (IIT)`. |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | Frontmatter title `Neural Correlates of Consciousness` does not match H1 `Neural Correlates of Consciousness (NCCs)`. |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | Frontmatter title `Orchestrated Objective Reduction` does not match H1 `Orchestrated Objective Reduction (Orch OR)`. |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | Frontmatter title `Panpsychism` does not match H1 `Panpsychism / Cosmopsychism`. |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | Frontmatter title `Predictive Processing` does not match H1 `Predictive Processing (PP)`. |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | Frontmatter title `Recurrent Processing Theory` does not match H1 `Recurrent Processing Theory (RPT)`. |
| info | `07_RESEARCH/RP-001/13 Research Graph/RP-001 Research Graph.md` | Frontmatter title `RP-001 Research Graph` does not match H1 `RP-001 — Research Graph`. |
| info | `07_RESEARCH/RP-001/14 Open Questions/RP-001 Open Questions.md` | Frontmatter title `RP-001 Open Questions` does not match H1 `RP-001 — Open Questions`. |
| info | `07_RESEARCH/RP-001/15 Future Experiments/RP-001 Future Research Opportunities.md` | Frontmatter title `RP-001 Future Research Opportunities` does not match H1 `RP-001 — Future Research Opportunities`. |
| info | `07_RESEARCH/RP-001/16 Visual Knowledge/RP-001 Visual Knowledge Index.md` | Frontmatter title `RP-001 Visual Knowledge Index` does not match H1 `RP-001 — Visual Knowledge Index`. |
| info | `07_RESEARCH/RP-001/17 NotebookLM Package/RP-001 NotebookLM Source Pack.md` | Frontmatter title `RP-001 NotebookLM Source Pack` does not match H1 `RP-001 — NotebookLM Source Pack`. |
| info | `07_RESEARCH/RP-001/18 Related Constitution/RP-001 Constitutional Links.md` | Frontmatter title `RP-001 Constitutional Links` does not match H1 `RP-001 — Related Constitutional Documents`. |
| info | `07_RESEARCH/RP-001/19 Related Laws/RP-001 Governing Provisions.md` | Frontmatter title `RP-001 Governing Provisions` does not match H1 `RP-001 — Governing Provisions and Operational Laws`. |
| info | `07_RESEARCH/RP-001/20 Related ADRs/RP-001 ADR Links.md` | Frontmatter title `RP-001 ADR Links` does not match H1 `RP-001 — Related Architectural Decision Records`. |
| info | `07_RESEARCH/RP-001/21 Version History/RP-001 Version History.md` | Frontmatter title `RP-001 Version History` does not match H1 `RP-001 — Program Version History`. |
| info | `07_RESEARCH/RP-001/ARCHIVE/ARCHIVE Philosophy.md` | Frontmatter title `ARCHIVE Philosophy — RP-001` does not match H1 `ARCHIVE — Philosophy and Governance`. |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Frontmatter title `DOC-001 — Architecture of Human Consciousness: A Comprehensive Literature Review` does not match H1 `DOC-001 — Architecture of Human Consciousness`. |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Frontmatter title `DOC-003 — Comparative Framework: Major Theories of Consciousness (SanaLab)` does not match H1 `DOC-003 — Comparative Framework: Major Theories of Consciousness`. |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Frontmatter title `DOC-004 — Theoretical Deep Dive: GNWT vs. IIT (SanaLab)` does not match H1 `DOC-004 — Theoretical Deep Dive: GNWT vs. IIT`. |
| info | `07_RESEARCH/RP-001/RP-001 Master Index.md` | Frontmatter title `RP-001 Master Index` does not match H1 `RP-001 — Atlas of Human Consciousness`. |
| info | `07_RESEARCH/RP-002/00 Executive Summary/RP-002 Executive Summary.md` | Frontmatter title `RP-002 Executive Summary — Atlas of Human Memory` does not match H1 `RP-002 — Executive Summary: Atlas of Human Memory`. |
| info | `07_RESEARCH/RP-002/01 Research Question/RP-002 Research Question.md` | Frontmatter title `RP-002 Research Question` does not match H1 `RP-002 — Research Question`. |
| info | `07_RESEARCH/RP-002/02 Objectives/RP-002 Objectives.md` | Frontmatter title `RP-002 Objectives` does not match H1 `RP-002 — Objectives`. |
| info | `07_RESEARCH/RP-002/03 Source Registry/RP-002 Source Registry.md` | Frontmatter title `RP-002 Source Registry` does not match H1 `RP-002 — Source Registry`. |
| info | `07_RESEARCH/RP-002/04 Source - CORE-002/RP-002 Source Note - CORE-002.md` | Frontmatter title `RP-002 Source Note — CORE-002 (Genspark)` does not match H1 `RP-002 — Source Note: CORE-002 / Genspark (DOC-A)`. |
| info | `07_RESEARCH/RP-002/05 Source - SanaLab/RP-002 Source Note - SanaLab.md` | Frontmatter title `RP-002 Source Note — SanaLab (DOC-B)` does not match H1 `RP-002 — Source Note: SanaLab / DOC-B`. |
| info | `07_RESEARCH/RP-002/06 Source - Illustrated/RP-002 Source Note - Illustrated.md` | Frontmatter title `RP-002 Source Note — Illustrated (DOC-C)` does not match H1 `RP-002 — Source Note: Illustrated / DOC-C`. |
| info | `07_RESEARCH/RP-002/07 Future Sources/RP-002 Future Sources.md` | Frontmatter title `RP-002 Future Sources` does not match H1 `RP-002 — Future Sources`. |
| info | `07_RESEARCH/RP-002/08 Comparative Framework/RP-002 Comparative Framework.md` | Frontmatter title `RP-002 Comparative Framework` does not match H1 `RP-002 — Comparative Framework`. |
| info | `07_RESEARCH/RP-002/09 Canonical Synthesis/RP-002 Canonical Synthesis.md` | Frontmatter title `RP-002 Canonical Synthesis — Atlas of Human Memory` does not match H1 `RP-002 — Canonical Synthesis: Atlas of Human Memory`. |
| info | `07_RESEARCH/RP-002/10 Theory Matrix/RP-002 Theory Matrix.md` | Frontmatter title `RP-002 Theory Matrix` does not match H1 `RP-002 — Theory Matrix`. |
| info | `07_RESEARCH/RP-002/11 Canonical Glossary/RP-002 Canonical Glossary.md` | Frontmatter title `RP-002 Canonical Glossary` does not match H1 `RP-002 — Canonical Glossary`. |
| info | `07_RESEARCH/RP-002/12 Evidence Registry/RP-002 Evidence Registry.md` | Frontmatter title `RP-002 Evidence Registry` does not match H1 `RP-002 — Evidence Registry`. |
| info | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Collective Memory.md` | Frontmatter title `Concept — Collective Memory` does not match H1 `Concept Note — Collective Memory`. |
| info | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Contemplative Memory.md` | Frontmatter title `Concept — Contemplative Memory` does not match H1 `Concept Note — Contemplative Memory`. |
| info | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Engram.md` | Frontmatter title `Concept — Engram` does not match H1 `Concept Note — Engram`. |
| info | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Hippocampus.md` | Frontmatter title `Concept — Hippocampus` does not match H1 `Concept Note — Hippocampus`. |
| info | `07_RESEARCH/RP-002/13 Research Graph/Concepts/LTP - Synaptic Plasticity.md` | Frontmatter title `Concept — LTP and Synaptic Plasticity` does not match H1 `Concept Note — LTP and Synaptic Plasticity`. |
| info | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Memory.md` | Frontmatter title `Concept — Memory` does not match H1 `Concept Note — Memory`. |
| info | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Pattern Separation and Completion.md` | Frontmatter title `Concept — Pattern Separation and Completion` does not match H1 `Concept Note — Pattern Separation and Completion`. |
| info | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Reconsolidation.md` | Frontmatter title `Concept — Reconsolidation` does not match H1 `Concept Note — Reconsolidation`. |
| info | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Trauma Memory.md` | Frontmatter title `Concept — Trauma Memory` does not match H1 `Concept Note — Trauma Memory`. |
| info | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Working Memory.md` | Frontmatter title `Concept — Working Memory` does not match H1 `Concept Note — Working Memory`. |
| info | `07_RESEARCH/RP-002/13 Research Graph/RP-002 Research Graph.md` | Frontmatter title `RP-002 Research Graph` does not match H1 `RP-002 — Research Graph`. |
| info | `07_RESEARCH/RP-002/14 Open Questions/RP-002 Open Questions.md` | Frontmatter title `RP-002 Open Questions` does not match H1 `RP-002 — Open Questions`. |
| info | `07_RESEARCH/RP-002/15 Future Experiments/RP-002 Future Research Opportunities.md` | Frontmatter title `RP-002 Future Research Opportunities` does not match H1 `RP-002 — Future Research Opportunities`. |
| info | `07_RESEARCH/RP-002/16 Visual Knowledge/RP-002 Visual Knowledge Index.md` | Frontmatter title `RP-002 Visual Knowledge Index` does not match H1 `RP-002 — Visual Knowledge Index`. |
| info | `07_RESEARCH/RP-002/17 NotebookLM Package/RP-002 NotebookLM Source Pack.md` | Frontmatter title `RP-002 NotebookLM Source Pack` does not match H1 `RP-002 — NotebookLM Source Pack`. |
| info | `07_RESEARCH/RP-002/18 Related Constitution/RP-002 Constitutional Links.md` | Frontmatter title `RP-002 Constitutional Links` does not match H1 `RP-002 — Constitutional Links`. |
| info | `07_RESEARCH/RP-002/19 Related Laws/RP-002 Governing Provisions.md` | Frontmatter title `RP-002 Governing Provisions` does not match H1 `RP-002 — Governing Provisions`. |
| info | `07_RESEARCH/RP-002/20 Related ADRs/RP-002 ADR Links.md` | Frontmatter title `RP-002 ADR Links` does not match H1 `RP-002 — ADR Links`. |
| info | `07_RESEARCH/RP-002/21 Version History/RP-002 Version History.md` | Frontmatter title `RP-002 Version History` does not match H1 `RP-002 — Version History`. |
| info | `07_RESEARCH/RP-002/ARCHIVE/ARCHIVE Philosophy.md` | Frontmatter title `RP-002 ARCHIVE Philosophy` does not match H1 `RP-002 — ARCHIVE Philosophy`. |
| info | `07_RESEARCH/RP-002/ARCHIVE/DOC-A Architecture Systemique Memoire Humaine.md` | Frontmatter title `DOC-A — Architecture Systémique de la Mémoire Humaine (CORE-002)` does not match H1 `DOC-A — Architecture Systémique de la Mémoire Humaine`. |
| info | `07_RESEARCH/RP-002/ARCHIVE/DOC-B Interdisciplinary Comparative Framework Memory.md` | Frontmatter title `DOC-B — Interdisciplinary Comparative Framework: Memory (SanaLab)` does not match H1 `DOC-B — Interdisciplinary Comparative Framework: Memory`. |
| info | `07_RESEARCH/RP-002/ARCHIVE/DOC-C RP-002 Illustrated.md` | Frontmatter title `DOC-C — RP-002 Illustrated (Genspark)` does not match H1 `DOC-C — RP-002 Illustrated`. |
| info | `07_RESEARCH/RP-002/RP-002 Master Index.md` | Frontmatter title `RP-002 Master Index — Atlas of Human Memory` does not match H1 `RP-002 — Master Index: Atlas of Human Memory`. |
| info | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Canonical Synthesis.md` | Frontmatter title `ISR-001 Canonical Synthesis — The Consciousness-Memory Architecture` does not match H1 `ISR-001 — Canonical Synthesis`. |
| info | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Institutional Synthesis Report.md` | Frontmatter title `ISR-001 — Institutional Synthesis Report: RP-001 and RP-002` does not match H1 `ISR-001 — Institutional Synthesis Report`. |
| info | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Knowledge Graph Update Recommendations.md` | Frontmatter title `ISR-001 Knowledge Graph Update Recommendations` does not match H1 `ISR-001 — Knowledge Graph Update Recommendations`. |
| info | `07_RESEARCH/RP-003/RP-003 Master Index.md` | Frontmatter title `RP-003 Master Index` does not match H1 `RP-003 — Atlas of Human Learning`. |
| info | `07_RESEARCH/RP-004/RP-004 Master Index.md` | Frontmatter title `RP-004 Master Index` does not match H1 `RP-004 — Atlas of Human Decision Making`. |
| info | `07_RESEARCH/RP-005/RP-005 Master Index.md` | Frontmatter title `RP-005 Master Index` does not match H1 `RP-005 — Atlas of Human Intelligence`. |
| info | `07_RESEARCH/RP-006/RP-006 Master Index.md` | Frontmatter title `RP-006 Master Index` does not match H1 `RP-006 — Atlas of Human Wisdom`. |
| info | `08_SYSTEMS/Engineering Toolkit/Alpha Proxima Engineering Toolkit.md` | Frontmatter title `Alpha Proxima Engineering Toolkit` does not match H1 `Alpha Proxima Engineering Toolkit v1.0`. |
| info | `08_SYSTEMS/The Orchestration Framework.md` | Frontmatter title `The Orchestration Framework` does not match H1 `THE ORCHESTRATION FRAMEWORK`. |
| info | `09_OFFICES/LUMIAION/LUMIAION Charter.md` | Frontmatter title `LUMIAION Charter — Permanent Constitutional Definition` does not match H1 `LUMIAION — Permanent Constitutional Charter`. |
| info | `10_TEMPLATES/ADR Template.md` | Frontmatter title `ADR Template` does not match H1 `ADR Template — Architecture Decision Record`. |
| info | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Frontmatter title `Legacy ALPHA PROXIMA — Archive Provenance` does not match H1 `Legacy ALPHA PROXIMA — Archived (Epoch V)`. |
| info | `OSG_BUSINESS/OSG_ACADEMY/Awaken the Inner Guru — Production Blueprint.md` | Frontmatter title `Awaken the Inner Guru — Production Blueprint` does not match H1 `Awaken the Inner Guru`. |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Frontmatter title `RI-001 — Awaken the Inner Guru — Reference Implementation Blueprint` does not match H1 `Awaken the Inner Guru`. |
| info | `OSG_LAUNCH/09_TEMPLATES/Automation Spec Template.md` | Frontmatter title `OSG Automation Spec Template` does not match H1 `<Automation Name>`. |
| info | `OSG_LAUNCH/09_TEMPLATES/Client Template.md` | Frontmatter title `OSG Client Template` does not match H1 `<Client Code>`. |
| info | `OSG_LAUNCH/09_TEMPLATES/Content Item Template.md` | Frontmatter title `OSG Content Item Template` does not match H1 `<Content Title>`. |
| info | `OSG_LAUNCH/09_TEMPLATES/Course Template.md` | Frontmatter title `OSG Course Template` does not match H1 `<Course Name>`. |
| info | `PROJECT_GENOME/Genome Constitution v1.0.md` | Frontmatter title `The Genome Constitution v1.0` does not match H1 `THE GENOME CONSTITUTION`. |
| info | `PROJECT_GENOME/Project Genome Master Index.md` | Frontmatter title `Project Genome Master Index` does not match H1 `PROJECT GENOME — Master Index`. |
| info | `README.md` | Frontmatter title `ALPHA.PROXIMA.CORE- README` does not match H1 `ALPHA.PROXIMA.CORE-`. |

### unknown_field

| Severity | Path | Message |
|----------|------|---------|
| info | `00_CONSTITUTION/Book I - The Constitution.md` | Field is not defined in the current standard: ratification_state |
| info | `00_CONSTITUTION/Book II - Governance Framework.md` | Field is not defined in the current standard: ratification_state |
| info | `00_CONSTITUTION/Book III - Knowledge Integrity.md` | Field is not defined in the current standard: constitutional_rank |
| info | `00_CONSTITUTION/Book III - Knowledge Integrity.md` | Field is not defined in the current standard: ratification_state |
| info | `00_CONSTITUTION/Book IV - Cognitive Architecture.md` | Field is not defined in the current standard: constitutional_rank |
| info | `00_CONSTITUTION/Book IV - Cognitive Architecture.md` | Field is not defined in the current standard: ratification_state |
| info | `00_CONSTITUTION/Book V - Cognitive Council.md` | Field is not defined in the current standard: constitutional_rank |
| info | `00_CONSTITUTION/Book V - Cognitive Council.md` | Field is not defined in the current standard: ratification_state |
| info | `00_CONSTITUTION/Constitutional Hierarchy Statement.md` | Field is not defined in the current standard: document_class |
| info | `00_CONSTITUTION/Constitutional Hierarchy Statement.md` | Field is not defined in the current standard: initiative |
| info | `00_CONSTITUTION/Constitutional Hierarchy Statement.md` | Field is not defined in the current standard: resolves |
| info | `00_CONSTITUTION/Founding Principles of Alpha Proxima.md` | Field is not defined in the current standard: document_class |
| info | `03_AI_COUNCIL/Cognitive Council Charter.md` | Field is not defined in the current standard: document_class |
| info | `03_AI_COUNCIL/Cognitive Council Charter.md` | Field is not defined in the current standard: governed_by |
| info | `03_AI_COUNCIL/Cognitive Council Charter.md` | Field is not defined in the current standard: maintained_by |
| info | `03_AI_COUNCIL/Cognitive Function Matrix.md` | Field is not defined in the current standard: document_class |
| info | `03_AI_COUNCIL/Cognitive Function Matrix.md` | Field is not defined in the current standard: governed_by |
| info | `03_AI_COUNCIL/Cognitive Function Matrix.md` | Field is not defined in the current standard: maintained_by |
| info | `03_AI_COUNCIL/Cognitive Function Registry.md` | Field is not defined in the current standard: document_class |
| info | `03_AI_COUNCIL/Cognitive Function Registry.md` | Field is not defined in the current standard: governed_by |
| info | `03_AI_COUNCIL/Cognitive Function Registry.md` | Field is not defined in the current standard: maintained_by |
| info | `03_AI_COUNCIL/Cognitive Function Registry.md` | Field is not defined in the current standard: reviewed_by |
| info | `03_AI_COUNCIL/Council Node Architecture.md` | Field is not defined in the current standard: initiative |
| info | `03_AI_COUNCIL/Departments/LUMIAION Charter.md` | Field is not defined in the current standard: superseded_date |
| info | `03_AI_COUNCIL/Engine Succession Policy.md` | Field is not defined in the current standard: document_class |
| info | `03_AI_COUNCIL/Engine Succession Policy.md` | Field is not defined in the current standard: governed_by |
| info | `03_AI_COUNCIL/Engine Succession Policy.md` | Field is not defined in the current standard: maintained_by |
| info | `03_AI_COUNCIL/YUNA Charter.md` | Field is not defined in the current standard: document_class |
| info | `03_AI_COUNCIL/YUNA Charter.md` | Field is not defined in the current standard: initiative |
| info | `03_AI_COUNCIL/YUNA Charter.md` | Field is not defined in the current standard: proposed_cf_code |
| info | `03_AI_COUNCIL/YUNA Charter.md` | Field is not defined in the current standard: resolves |
| info | `04_DECISIONS/ADR-0001 - The Founding Decision.md` | Field is not defined in the current standard: decision_class |
| info | `04_DECISIONS/ADR-0001 - The Founding Decision.md` | Field is not defined in the current standard: ratification_date |
| info | `04_DECISIONS/ADR-0001 - The Founding Decision.md` | Field is not defined in the current standard: ratified_by |
| info | `04_DECISIONS/ADR-0002 - Reconciling the Four Institutional Taxonomies.md` | Field is not defined in the current standard: decision_class |
| info | `04_DECISIONS/ADR-0002 - Reconciling the Four Institutional Taxonomies.md` | Field is not defined in the current standard: ratification_date |
| info | `04_DECISIONS/ADR-0002 - Reconciling the Four Institutional Taxonomies.md` | Field is not defined in the current standard: ratified_by |
| info | `04_DECISIONS/ADR-0003 - PR47 Source-Scoped Reference Contract.md` | Field is not defined in the current standard: adr_code |
| info | `04_DECISIONS/ADR-0003 - PR47 Source-Scoped Reference Contract.md` | Field is not defined in the current standard: decision_class |
| info | `04_DECISIONS/ADR-0003 - PR47 Source-Scoped Reference Contract.md` | Field is not defined in the current standard: decision_status |
| info | `04_DECISIONS/ADR-0003 - PR47 Source-Scoped Reference Contract.md` | Field is not defined in the current standard: document_class |
| info | `04_DECISIONS/ADR-0003 - PR47 Source-Scoped Reference Contract.md` | Field is not defined in the current standard: ratification_date |
| info | `04_DECISIONS/ADR-0003 - PR47 Source-Scoped Reference Contract.md` | Field is not defined in the current standard: ratified_by |
| info | `05_PROPOSALS/CN-0001 - Constitutional Alignment Gap Report.md` | Field is not defined in the current standard: cn_number |
| info | `05_PROPOSALS/CN-0001 - Constitutional Alignment Gap Report.md` | Field is not defined in the current standard: decision_class |
| info | `05_PROPOSALS/CN-0001 - Constitutional Alignment Gap Report.md` | Field is not defined in the current standard: outcome |
| info | `05_PROPOSALS/CN-0001 - Constitutional Alignment Gap Report.md` | Field is not defined in the current standard: submitted_to |
| info | `05_PROPOSALS/Constitution v2.0 Ratification Draft.md` | Field is not defined in the current standard: basis_ratification |
| info | `05_PROPOSALS/Constitution v2.0 Ratification Draft.md` | Field is not defined in the current standard: initiative |
| info | `06_GOVERNANCE/Canonical Terminology/Canonical Terminology Register.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Constitutional Audit/CAR-001 Constitutional Audit Report.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Constitutional Audit/CAR-001 Constitutional Audit Report.md` | Field is not defined in the current standard: governed_by |
| info | `06_GOVERNANCE/Constitutional Audit/CAR-001 Constitutional Audit Report.md` | Field is not defined in the current standard: review_scope |
| info | `06_GOVERNANCE/Constitutional Impact Report/CIR-001 Epoch III Constitutional Refactoring.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Constitutional Impact Report/CIR-001 Epoch III Constitutional Refactoring.md` | Field is not defined in the current standard: initiative |
| info | `06_GOVERNANCE/Constitutional Impact Report/CIR-002 Institutional Completeness Review.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Constitutional Impact Report/CIR-002 Institutional Completeness Review.md` | Field is not defined in the current standard: initiative |
| info | `06_GOVERNANCE/Constitutional Impact Report/CIR-003 Epoch V Constitutional Coherence.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Constitutional Impact Report/CIR-003 Epoch V Constitutional Coherence.md` | Field is not defined in the current standard: initiative |
| info | `06_GOVERNANCE/Constitutional Impact Report/CIR-003 Epoch V Constitutional Coherence.md` | Field is not defined in the current standard: resolves |
| info | `06_GOVERNANCE/Constitutional Impact Report/CIR-003 Epoch V Constitutional Coherence.md` | Field is not defined in the current standard: supersedes_claim |
| info | `06_GOVERNANCE/Directive Governance Framework/Directive Governance Framework.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Directive Governance Framework/Directive Governance Framework.md` | Field is not defined in the current standard: governed_by |
| info | `06_GOVERNANCE/Epoch V/Book II Amendment — Council Topology.md` | Field is not defined in the current standard: initiative |
| info | `06_GOVERNANCE/Epoch V/Book II Amendment — Council Topology.md` | Field is not defined in the current standard: resolves |
| info | `06_GOVERNANCE/Epoch V/Consolidated Ethics Framework.md` | Field is not defined in the current standard: initiative |
| info | `06_GOVERNANCE/Epoch V/Consolidated Ethics Framework.md` | Field is not defined in the current standard: resolves |
| info | `06_GOVERNANCE/Epoch V/Governance Model Crosswalk.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Epoch V/Governance Model Crosswalk.md` | Field is not defined in the current standard: initiative |
| info | `06_GOVERNANCE/Epoch V/Governance Model Crosswalk.md` | Field is not defined in the current standard: resolves |
| info | `06_GOVERNANCE/Epoch V/Interim Authority Instrument.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Epoch V/Interim Authority Instrument.md` | Field is not defined in the current standard: initiative |
| info | `06_GOVERNANCE/Epoch V/Interim Authority Instrument.md` | Field is not defined in the current standard: resolves |
| info | `06_GOVERNANCE/Foundation Gap Report/FGR-001 Epoch II Stewardship Audit.md` | Field is not defined in the current standard: report_id |
| info | `06_GOVERNANCE/Foundation Gap Report/FGR-001 Epoch II Stewardship Audit.md` | Field is not defined in the current standard: report_type |
| info | `06_GOVERNANCE/Foundation Gap Report/FGR-001 Epoch II Stewardship Audit.md` | Field is not defined in the current standard: scope |
| info | `06_GOVERNANCE/Founder Directives/Founder Directives Register.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Founder Directives/Founder Directives Register.md` | Field is not defined in the current standard: governed_by |
| info | `06_GOVERNANCE/Institutional Glossary & Acronym Register.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Institutional Glossary & Acronym Register.md` | Field is not defined in the current standard: initiative |
| info | `06_GOVERNANCE/Institutional Glossary & Acronym Register.md` | Field is not defined in the current standard: resolves |
| info | `06_GOVERNANCE/Institutional Open Questions Register.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Institutional Open Questions Register.md` | Field is not defined in the current standard: initiative |
| info | `06_GOVERNANCE/Institutional Open Questions Register.md` | Field is not defined in the current standard: resolves |
| info | `06_GOVERNANCE/Institutional Policies/Citation Policy.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Institutional Policies/Citation Policy.md` | Field is not defined in the current standard: governed_by |
| info | `06_GOVERNANCE/Institutional Policies/Metadata Policy.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Institutional Policies/Metadata Policy.md` | Field is not defined in the current standard: governed_by |
| info | `06_GOVERNANCE/Institutional Policies/Naming Policy.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Institutional Policies/Naming Policy.md` | Field is not defined in the current standard: governed_by |
| info | `06_GOVERNANCE/Institutional Policies/Privacy Policy.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Institutional Policies/Privacy Policy.md` | Field is not defined in the current standard: governed_by |
| info | `06_GOVERNANCE/Institutional Policies/Source Attribution Policy.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Institutional Policies/Source Attribution Policy.md` | Field is not defined in the current standard: governed_by |
| info | `06_GOVERNANCE/Institutional Policies/Versioning Policy.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Institutional Policies/Versioning Policy.md` | Field is not defined in the current standard: governed_by |
| info | `06_GOVERNANCE/Institutional Timeline.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Institutional Timeline.md` | Field is not defined in the current standard: initiative |
| info | `06_GOVERNANCE/Institutional Timeline.md` | Field is not defined in the current standard: resolves |
| info | `06_GOVERNANCE/Research Debt Register/Research Debt Register.md` | Field is not defined in the current standard: registry_type |
| info | `06_GOVERNANCE/Research Framework/Institutional Intelligence Translation Framework v1.0.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Research Framework/Institutional Intelligence Translation Framework v1.0.md` | Field is not defined in the current standard: governed_by |
| info | `06_GOVERNANCE/Research Framework/Institutional Intelligence Translation Framework v1.0.md` | Field is not defined in the current standard: initiative |
| info | `06_GOVERNANCE/Research Framework/Research Integration Framework.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Research Framework/Research Integration Framework.md` | Field is not defined in the current standard: governed_by |
| info | `06_GOVERNANCE/Research Framework/Research Integration Framework.md` | Field is not defined in the current standard: initiative |
| info | `06_GOVERNANCE/Research Framework/Research Program Playbook v1.0.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Research Framework/Research Program Playbook v1.0.md` | Field is not defined in the current standard: governed_by |
| info | `06_GOVERNANCE/Research Framework/Research Program Playbook v1.0.md` | Field is not defined in the current standard: initiative |
| info | `06_GOVERNANCE/Research Framework/Translation Checklist.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Research Framework/Translation Checklist.md` | Field is not defined in the current standard: governed_by |
| info | `06_GOVERNANCE/Research Framework/Translation Checklist.md` | Field is not defined in the current standard: initiative |
| info | `06_GOVERNANCE/Research Framework/Translation Decision Matrix.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Research Framework/Translation Decision Matrix.md` | Field is not defined in the current standard: governed_by |
| info | `06_GOVERNANCE/Research Framework/Translation Decision Matrix.md` | Field is not defined in the current standard: initiative |
| info | `06_GOVERNANCE/Research Framework/Translation Review Process.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Research Framework/Translation Review Process.md` | Field is not defined in the current standard: governed_by |
| info | `06_GOVERNANCE/Research Framework/Translation Review Process.md` | Field is not defined in the current standard: initiative |
| info | `06_GOVERNANCE/Research Methodology/Alpha Proxima Research Methodology v1.0.md` | Field is not defined in the current standard: derived_from |
| info | `06_GOVERNANCE/Research Methodology/Alpha Proxima Research Methodology v1.0.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Research Methodology/Alpha Proxima Research Methodology v1.0.md` | Field is not defined in the current standard: governing_body |
| info | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Field is not defined in the current standard: directive_code |
| info | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Field is not defined in the current standard: effective_date |
| info | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Field is not defined in the current standard: issuing_authority |
| info | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Field is not defined in the current standard: target_office |
| info | `06_GOVERNANCE/Standing Orders/Standing Orders Register.md` | Field is not defined in the current standard: document_class |
| info | `06_GOVERNANCE/Standing Orders/Standing Orders Register.md` | Field is not defined in the current standard: governed_by |
| info | `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | Field is not defined in the current standard: canon_status |
| info | `07_RESEARCH/RP-001/04 Source - Perplexity/RP-001 Source Note - Perplexity.md` | Field is not defined in the current standard: document_id |
| info | `07_RESEARCH/RP-001/05 Source - Gemini/RP-001 Source Note - Gemini.md` | Field is not defined in the current standard: document_id |
| info | `07_RESEARCH/RP-001/06 Source - SanaLab/RP-001 Source Note - SanaLab.md` | Field is not defined in the current standard: document_ids |
| info | `07_RESEARCH/RP-001/08 Comparative Framework/RP-001 Comparative Framework.md` | Field is not defined in the current standard: canon_status |
| info | `07_RESEARCH/RP-001/09 Canonical Synthesis/RP-001 Canonical Synthesis.md` | Field is not defined in the current standard: canon_status |
| info | `07_RESEARCH/RP-001/09 Canonical Synthesis/RP-001 Canonical Synthesis.md` | Field is not defined in the current standard: contributor |
| info | `07_RESEARCH/RP-001/09 Canonical Synthesis/RP-001 Canonical Synthesis.md` | Field is not defined in the current standard: intake_date |
| info | `07_RESEARCH/RP-001/09 Canonical Synthesis/RP-001 Canonical Synthesis.md` | Field is not defined in the current standard: sources |
| info | `07_RESEARCH/RP-001/10 Theory Matrix/RP-001 Theory Matrix.md` | Field is not defined in the current standard: canon_status |
| info | `07_RESEARCH/RP-001/11 Canonical Glossary/RP-001 Canonical Glossary.md` | Field is not defined in the current standard: canon_status |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | Field is not defined in the current standard: key_theorists |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | Field is not defined in the current standard: key_theorists |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Attention Schema Theory.md` | Field is not defined in the current standard: key_theorists |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | Field is not defined in the current standard: key_theorists |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Higher-Order Thought Theory.md` | Field is not defined in the current standard: key_theorists |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Illusionism.md` | Field is not defined in the current standard: key_theorists |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | Field is not defined in the current standard: key_theorists |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | Field is not defined in the current standard: key_theorists |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | Field is not defined in the current standard: key_theorists |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | Field is not defined in the current standard: key_theorists |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | Field is not defined in the current standard: key_theorists |
| info | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | Field is not defined in the current standard: key_theorists |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Field is not defined in the current standard: canon_status |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Field is not defined in the current standard: contributor |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Field is not defined in the current standard: contributor_type |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Field is not defined in the current standard: deposit_date |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Field is not defined in the current standard: document_id |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Field is not defined in the current standard: file_size_kb |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Field is not defined in the current standard: format |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Field is not defined in the current standard: immutable |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Field is not defined in the current standard: original_date |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Field is not defined in the current standard: page_count |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Field is not defined in the current standard: canon_status |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Field is not defined in the current standard: commissioned_by |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Field is not defined in the current standard: contributor |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Field is not defined in the current standard: contributor_agent |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Field is not defined in the current standard: contributor_type |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Field is not defined in the current standard: deposit_date |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Field is not defined in the current standard: document_id |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Field is not defined in the current standard: file_size_kb |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Field is not defined in the current standard: format |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Field is not defined in the current standard: immutable |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Field is not defined in the current standard: original_date |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Field is not defined in the current standard: page_count |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Field is not defined in the current standard: canon_status |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Field is not defined in the current standard: contributor |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Field is not defined in the current standard: contributor_role |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Field is not defined in the current standard: contributor_type |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Field is not defined in the current standard: deposit_date |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Field is not defined in the current standard: document_id |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Field is not defined in the current standard: file_size_kb |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Field is not defined in the current standard: format |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Field is not defined in the current standard: immutable |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Field is not defined in the current standard: original_date |
| info | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Field is not defined in the current standard: page_count |
| info | `07_RESEARCH/RP-001/RP-001 Master Index.md` | Field is not defined in the current standard: canon_status |
| info | `07_RESEARCH/RP-002/04 Source - CORE-002/RP-002 Source Note - CORE-002.md` | Field is not defined in the current standard: document_id |
| info | `07_RESEARCH/RP-002/05 Source - SanaLab/RP-002 Source Note - SanaLab.md` | Field is not defined in the current standard: document_id |
| info | `07_RESEARCH/RP-002/06 Source - Illustrated/RP-002 Source Note - Illustrated.md` | Field is not defined in the current standard: document_id |
| info | `07_RESEARCH/RP-002/08 Comparative Framework/RP-002 Comparative Framework.md` | Field is not defined in the current standard: source |
| info | `07_RESEARCH/RP-002/09 Canonical Synthesis/RP-002 Canonical Synthesis.md` | Field is not defined in the current standard: evidence_sources |
| info | `07_RESEARCH/RP-002/09 Canonical Synthesis/RP-002 Canonical Synthesis.md` | Field is not defined in the current standard: pending_sources |
| info | `07_RESEARCH/RP-002/ARCHIVE/ARCHIVE Philosophy.md` | Field is not defined in the current standard: immutable |
| info | `07_RESEARCH/RP-002/ARCHIVE/DOC-A Architecture Systemique Memoire Humaine.md` | Field is not defined in the current standard: document_id |
| info | `07_RESEARCH/RP-002/ARCHIVE/DOC-A Architecture Systemique Memoire Humaine.md` | Field is not defined in the current standard: immutable |
| info | `07_RESEARCH/RP-002/ARCHIVE/DOC-B Interdisciplinary Comparative Framework Memory.md` | Field is not defined in the current standard: document_id |
| info | `07_RESEARCH/RP-002/ARCHIVE/DOC-B Interdisciplinary Comparative Framework Memory.md` | Field is not defined in the current standard: immutable |
| info | `07_RESEARCH/RP-002/ARCHIVE/DOC-C RP-002 Illustrated.md` | Field is not defined in the current standard: document_id |
| info | `07_RESEARCH/RP-002/ARCHIVE/DOC-C RP-002 Illustrated.md` | Field is not defined in the current standard: immutable |
| info | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Canonical Synthesis.md` | Field is not defined in the current standard: canon_review_required |
| info | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Canonical Synthesis.md` | Field is not defined in the current standard: document_class |
| info | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Canonical Synthesis.md` | Field is not defined in the current standard: governed_by |
| info | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Canonical Synthesis.md` | Field is not defined in the current standard: review_scope |
| info | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Institutional Synthesis Report.md` | Field is not defined in the current standard: commissioned_by |
| info | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Institutional Synthesis Report.md` | Field is not defined in the current standard: document_class |
| info | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Institutional Synthesis Report.md` | Field is not defined in the current standard: review_scope |
| info | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Knowledge Graph Update Recommendations.md` | Field is not defined in the current standard: commissioned_by |
| info | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Knowledge Graph Update Recommendations.md` | Field is not defined in the current standard: document_class |
| info | `08_SYSTEMS/ALPHAPROXIMA Enterprise Knowledge Architecture v1.0.md` | Field is not defined in the current standard: document_type |
| info | `08_SYSTEMS/Alpha Proxima Operating Model v1.0.md` | Field is not defined in the current standard: document_class |
| info | `08_SYSTEMS/Institutional Knowledge Graph/Tools/Tool 014 - Truth Kernel.md` | Field is not defined in the current standard: tool_id |
| info | `08_SYSTEMS/Knowledge Architecture Specification.md` | Field is not defined in the current standard: initiative |
| info | `08_SYSTEMS/Knowledge Architecture Specification.md` | Field is not defined in the current standard: resolves |
| info | `08_SYSTEMS/LUMIAION Architecture Spec v0.1.md` | Field is not defined in the current standard: generated_by |
| info | `08_SYSTEMS/The Orchestration Framework.md` | Field is not defined in the current standard: document_type |
| info | `09_OFFICES/Engineering Office/Engineering Office Charter.md` | Field is not defined in the current standard: current_reasoning_engine |
| info | `09_OFFICES/Engineering Office/Engineering Office Charter.md` | Field is not defined in the current standard: document_class |
| info | `09_OFFICES/Executive Office/Executive Office Charter.md` | Field is not defined in the current standard: document_class |
| info | `09_OFFICES/Institutional Observatory/Institutional Observatory Charter.md` | Field is not defined in the current standard: current_reasoning_engine |
| info | `09_OFFICES/Institutional Observatory/Institutional Observatory Charter.md` | Field is not defined in the current standard: document_class |
| info | `09_OFFICES/LUMIAION/LUMIAION Charter.md` | Field is not defined in the current standard: constitutional_rank |
| info | `09_OFFICES/LUMIAION/LUMIAION Charter.md` | Field is not defined in the current standard: document_class |
| info | `09_OFFICES/Research Intelligence Office/Research Intelligence Office Charter.md` | Field is not defined in the current standard: current_reasoning_engine |
| info | `09_OFFICES/Research Intelligence Office/Research Intelligence Office Charter.md` | Field is not defined in the current standard: document_class |
| info | `09_OFFICES/Research Intelligence Office/Research Office Matrix.md` | Field is not defined in the current standard: document_class |
| info | `09_OFFICES/Research Intelligence Office/Research Office Matrix.md` | Field is not defined in the current standard: governed_by |
| info | `09_OFFICES/Research Intelligence Office/Research Office Matrix.md` | Field is not defined in the current standard: initiative |
| info | `10_TEMPLATES/Institutional Translation Template v1.0.md` | Field is not defined in the current standard: document_class |
| info | `10_TEMPLATES/Institutional Translation Template v1.0.md` | Field is not defined in the current standard: governed_by |
| info | `10_TEMPLATES/Institutional Translation Template v1.0.md` | Field is not defined in the current standard: initiative |
| info | `10_TEMPLATES/Research Commission Template v2.0.md` | Field is not defined in the current standard: document_class |
| info | `10_TEMPLATES/Research Commission Template v2.0.md` | Field is not defined in the current standard: governed_by |
| info | `10_TEMPLATES/Research Commission Template v2.0.md` | Field is not defined in the current standard: initiative |
| info | `10_TEMPLATES/Research Note Template.md` | Field is not defined in the current standard: canon_status |
| info | `10_TEMPLATES/Research Note Template.md` | Field is not defined in the current standard: contributor |
| info | `10_TEMPLATES/Research Note Template.md` | Field is not defined in the current standard: intake_date |
| info | `10_TEMPLATES/Research Note Template.md` | Field is not defined in the current standard: sources |
| info | `10_TEMPLATES/Research Program Template/Research Program Methodology.md` | Field is not defined in the current standard: derived_from |
| info | `11_OPERATIONS/Weekly Execution Plans/2026-09-03 - Truth Kernel Execution Plan.md` | Field is not defined in the current standard: approval_state |
| info | `11_OPERATIONS/Weekly Execution Plans/2026-09-03 - Truth Kernel Execution Plan.md` | Field is not defined in the current standard: execution_window |
| info | `Alpha Proxima Core.md` | Field is not defined in the current standard: note_type |
| info | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Field is not defined in the current standard: document_class |
| info | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Field is not defined in the current standard: document_id |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Field is not defined in the current standard: canonical_path |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Field is not defined in the current standard: course |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Field is not defined in the current standard: document_class |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Field is not defined in the current standard: document_id |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Field is not defined in the current standard: engineering_review |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Field is not defined in the current standard: governing_standard |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Field is not defined in the current standard: incorporates_by_reference |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Field is not defined in the current standard: ols_version |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Field is not defined in the current standard: reference_id |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Field is not defined in the current standard: review_role |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Field is not defined in the current standard: course |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Field is not defined in the current standard: document_class |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Field is not defined in the current standard: document_id |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Field is not defined in the current standard: language |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Field is not defined in the current standard: module |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Field is not defined in the current standard: reference_id |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Field is not defined in the current standard: source_language |
| info | `OSG_LAUNCH/00_REPOSITORY/OSG Academy Engineering Review.md` | Field is not defined in the current standard: core_question |
| info | `OSG_LAUNCH/10_ACADEMY/AIG/Awaken the Inner Guru Recording Start Guide.md` | Field is not defined in the current standard: core_question |
| info | `OSG_LAUNCH/10_ACADEMY/AIG/README.md` | Field is not defined in the current standard: core_question |
| info | `OSG_LAUNCH/10_ACADEMY/README.md` | Field is not defined in the current standard: core_question |
| info | `PROJECT_GENOME/Genome Constitution v1.0.md` | Field is not defined in the current standard: classification |
| info | `PROJECT_GENOME/Genome Constitution v1.0.md` | Field is not defined in the current standard: document_class |
| info | `PROJECT_GENOME/Genome Constitution v1.0.md` | Field is not defined in the current standard: governed_by |
| info | `PROJECT_GENOME/Genome Constitution v1.0.md` | Field is not defined in the current standard: initiative |
| info | `PROJECT_GENOME/Genome Constitution v1.0.md` | Field is not defined in the current standard: project |
| info | `PROJECT_GENOME/Project Genome Master Index.md` | Field is not defined in the current standard: document_class |
| info | `PROJECT_GENOME/Project Genome Master Index.md` | Field is not defined in the current standard: project |

## Implementation Notes

This report is diagnostic. It does not approve, reject, move, or modify institutional documents.

## Future Improvements

- [ ] Add per-artifact schemas.
- [ ] Add JSON output for automation.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-09-29 | [[CODEX]] | YAML validation report generated |
