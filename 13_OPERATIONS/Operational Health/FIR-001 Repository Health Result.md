---
title: "Vault Validation Report"
aliases: []
tags: [systems, engineering, validation, report, alpha-proxima]
created: 2026-09-03
updated: 2026-09-03
status: draft
version: "0.1.0"
authors: ["CODEX"]
artifact_type: engineering-report
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Tool 001 - Vault Validator]]"]
related_documents: ["[[Alpha Proxima Engineering Toolkit]]", "[[ALPHA PROXIMA ENGINEERING HANDBOOK]]"]
related_research_programs: []
---

# Vault Validation Report

## Purpose

Report engineering quality issues detected by [[Tool 001 - Vault Validator]].

## Summary

- Vault: `/private/tmp/alpha-fir-work.H0ZK1A`
- Generated: `2026-09-03T22:05:47-04:00`
- Markdown notes scanned: `368`
- Critical: `0`
- Errors: `23`
- Warnings: `998`
- Info: `38`

## Folder Classification

| Category | Top-Level Folder Count |
|----------|------------------------|
| institutional | `16` |
| legacy | `0` |
| tool-managed | `0` |
| hidden | `3` |
| temporary | `0` |
| unclassified | `5` |

Tool-managed and hidden folders are excluded from default institutional validation scans.

## Validation Results

### broken_wiki_link

| Severity | Path | Message |
|----------|------|---------|
| error | `00_CONSTITUTION/Book IV - Cognitive Architecture.md` | Missing wiki link target: \[\[Community Council Charter]] |
| error | `08_SYSTEMS/Engineering Standards/12 - Continuous Integration Standard.md` | Missing wiki link target: \[\[Note]] |
| error | `08_SYSTEMS/Engineering Standards/12 - Continuous Integration Standard.md` | Missing wiki link target: \[\[folder/Note]] |
| error | `08_SYSTEMS/Engineering Toolkit/Tool 013 - Alpha Proxima App.md` | Missing wiki link target: \[\[Note]] |
| error | `08_SYSTEMS/Engineering Toolkit/Tool 013 - Alpha Proxima App.md` | Missing wiki link target: \[\[folder/Note]] |

### duplicate_filename

| Severity | Path | Message |
|----------|------|---------|
| warning | `03_AI_COUNCIL/Departments/LUMIAION Charter.md` | Duplicate filename appears in 2 locations: LUMIAION Charter.md |
| warning | `07_RESEARCH/RP-001/ARCHIVE/ARCHIVE Philosophy.md` | Duplicate filename appears in 2 locations: ARCHIVE Philosophy.md |
| warning | `07_RESEARCH/RP-002/ARCHIVE/ARCHIVE Philosophy.md` | Duplicate filename appears in 2 locations: ARCHIVE Philosophy.md |
| warning | `08_SYSTEMS/Research Management Toolkit/Templates/Research Commission Template.md` | Duplicate filename appears in 2 locations: Research Commission Template.md |
| warning | `09_OFFICES/LUMIAION/LUMIAION Charter.md` | Duplicate filename appears in 2 locations: LUMIAION Charter.md |
| warning | `14_FUTURE/Templates/Research Commission Template.md` | Duplicate filename appears in 2 locations: Research Commission Template.md |

### incorrect_folder_placement

| Severity | Path | Message |
|----------|------|---------|
| warning | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Protocols should live under 08_SYSTEMS/Protocols/. |
| warning | `OSG_LAUNCH/09_TEMPLATES/Automation Spec Template.md` | Templates should live under 10_TEMPLATES/ or an approved office-local Templates/ folder. |
| warning | `OSG_LAUNCH/09_TEMPLATES/Client Template.md` | Templates should live under 10_TEMPLATES/ or an approved office-local Templates/ folder. |
| warning | `OSG_LAUNCH/09_TEMPLATES/Content Item Template.md` | Templates should live under 10_TEMPLATES/ or an approved office-local Templates/ folder. |
| warning | `OSG_LAUNCH/09_TEMPLATES/Course Template.md` | Templates should live under 10_TEMPLATES/ or an approved office-local Templates/ folder. |

### invalid_frontmatter

| Severity | Path | Message |
|----------|------|---------|
| warning | `04_DECISIONS/ADR-0002 - Reconciling the Four Institutional Taxonomies.md` | Invalid status value: proposed |
| warning | `07_RESEARCH/RP-002/06 Source - Illustrated/RP-002 Source Note - Illustrated.md` | Invalid status value: pending |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-C RP-002 Illustrated.md` | Invalid status value: pending |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Invalid status value: living-reference |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Invalid status value: ready-for-recording |

### missing_backlinks

| Severity | Path | Message |
|----------|------|---------|
| info | `06_GOVERNANCE/Institutional Open Questions Register.md` | No incoming wiki links found. |
| info | `06_GOVERNANCE/Institutional Policies/Privacy Policy.md` | No incoming wiki links found. |
| info | `06_GOVERNANCE/Standards Council/Standards Council Evaluation.md` | No incoming wiki links found. |
| info | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | No incoming wiki links found. |
| info | `07_RESEARCH/RP-001/05 Source - Gemini/RP-001 Source Note - Gemini.md` | No incoming wiki links found. |
| info | `07_RESEARCH/RP-001/07 Future Sources/RP-001 Future Sources.md` | No incoming wiki links found. |
| info | `07_RESEARCH/RP-001/16 Visual Knowledge/RP-001 Visual Knowledge Index.md` | No incoming wiki links found. |
| info | `07_RESEARCH/RP-001/19 Related Laws/RP-001 Governing Provisions.md` | No incoming wiki links found. |
| info | `07_RESEARCH/RP-001/20 Related ADRs/RP-001 ADR Links.md` | No incoming wiki links found. |
| info | `07_RESEARCH/RP-002/07 Future Sources/RP-002 Future Sources.md` | No incoming wiki links found. |
| info | `07_RESEARCH/RP-002/13 Research Graph/RP-002 Research Graph.md` | No incoming wiki links found. |
| info | `07_RESEARCH/RP-002/16 Visual Knowledge/RP-002 Visual Knowledge Index.md` | No incoming wiki links found. |
| info | `07_RESEARCH/RP-002/ARCHIVE/ARCHIVE Philosophy.md` | No incoming wiki links found. |
| info | `08_SYSTEMS/Engineering Toolkit/OSG Reading Color CSS Guide.md` | No incoming wiki links found. |
| info | `08_SYSTEMS/Institutional Knowledge Graph/Tools/Relationship Registry Report.md` | No incoming wiki links found. |
| info | `08_SYSTEMS/Research Management Toolkit/Reports/ES-004 - Research Management Toolkit Delivery Report.md` | No incoming wiki links found. |
| info | `14_FUTURE/Templates/Research Commission Template.md` | No incoming wiki links found. |
| info | `99_ARCHIVE/Legacy ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/Building achitecture/LUMIAION VAULT.md` | No incoming wiki links found. |
| info | `Building Milestone.md` | No incoming wiki links found. |
| info | `LUMIAION.md` | No incoming wiki links found. |
| info | `OSG_BUSINESS/00 OSG Business Foundation — Overview.md` | No incoming wiki links found. |
| info | `OSG_BUSINESS/01 Flagship Course.md` | No incoming wiki links found. |
| info | `OSG_BUSINESS/02 Coaching Offers.md` | No incoming wiki links found. |
| info | `OSG_BUSINESS/03 Website Copy.md` | No incoming wiki links found. |
| info | `OSG_BUSINESS/04 Client Journey & Onboarding.md` | No incoming wiki links found. |
| info | `OSG_BUSINESS/05 Email Sequences.md` | No incoming wiki links found. |
| info | `OSG_BUSINESS/06 Community Onboarding.md` | No incoming wiki links found. |
| info | `OSG_BUSINESS/07 30-Day Launch Checklist.md` | No incoming wiki links found. |
| info | `OSG_BUSINESS/OSG_ACADEMY/Awaken the Inner Guru — Production Blueprint.md` | No incoming wiki links found. |
| info | `OSG_BUSINESS/OSG_ACADEMY/OSG Learning Standard (OLS) v1.0.md` | No incoming wiki links found. |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | No incoming wiki links found. |
| info | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | No incoming wiki links found. |
| info | `Omi/Memories.md` | No incoming wiki links found. |
| info | `PROJECT_GENOME/Project Genome Master Index.md` | No incoming wiki links found. |
| info | `Sans titre 1.md` | No incoming wiki links found. |
| info | `Sans titre.md` | No incoming wiki links found. |
| info | `Vault.md` | No incoming wiki links found. |
| info | `docs/setup/Claude-Code-in-Obsidian.md` | No incoming wiki links found. |

### missing_required_metadata

| Severity | Path | Message |
|----------|------|---------|
| warning | `00_CONSTITUTION/Book IV - Cognitive Architecture.md` | Missing required frontmatter field: artifact_type |
| warning | `00_CONSTITUTION/Book IV - Cognitive Architecture.md` | Missing required frontmatter field: dependencies |
| warning | `00_CONSTITUTION/Book IV - Cognitive Architecture.md` | Missing required frontmatter field: institutional_owner |
| warning | `00_CONSTITUTION/Book IV - Cognitive Architecture.md` | Missing required frontmatter field: related_documents |
| warning | `00_CONSTITUTION/Book IV - Cognitive Architecture.md` | Missing required frontmatter field: related_research_programs |
| warning | `00_CONSTITUTION/Book V - Cognitive Council.md` | Missing required frontmatter field: artifact_type |
| warning | `00_CONSTITUTION/Book V - Cognitive Council.md` | Missing required frontmatter field: dependencies |
| warning | `00_CONSTITUTION/Book V - Cognitive Council.md` | Missing required frontmatter field: institutional_owner |
| warning | `00_CONSTITUTION/Book V - Cognitive Council.md` | Missing required frontmatter field: related_documents |
| warning | `00_CONSTITUTION/Book V - Cognitive Council.md` | Missing required frontmatter field: related_research_programs |
| warning | `00_CONSTITUTION/Constitutional Hierarchy Statement.md` | Missing required frontmatter field: artifact_type |
| warning | `00_CONSTITUTION/Constitutional Hierarchy Statement.md` | Missing required frontmatter field: dependencies |
| warning | `00_CONSTITUTION/Constitutional Hierarchy Statement.md` | Missing required frontmatter field: institutional_owner |
| warning | `00_CONSTITUTION/Constitutional Hierarchy Statement.md` | Missing required frontmatter field: related_documents |
| warning | `00_CONSTITUTION/Constitutional Hierarchy Statement.md` | Missing required frontmatter field: related_research_programs |
| warning | `00_CONSTITUTION/Founding Principles of Alpha Proxima.md` | Missing required frontmatter field: artifact_type |
| warning | `00_CONSTITUTION/Founding Principles of Alpha Proxima.md` | Missing required frontmatter field: dependencies |
| warning | `00_CONSTITUTION/Founding Principles of Alpha Proxima.md` | Missing required frontmatter field: institutional_owner |
| warning | `00_CONSTITUTION/Founding Principles of Alpha Proxima.md` | Missing required frontmatter field: related_documents |
| warning | `00_CONSTITUTION/Founding Principles of Alpha Proxima.md` | Missing required frontmatter field: related_research_programs |
| warning | `01_VISION/Alpha Proxima — 10 Year Vision.md` | Missing required frontmatter field: artifact_type |
| warning | `01_VISION/Alpha Proxima — 10 Year Vision.md` | Missing required frontmatter field: dependencies |
| warning | `01_VISION/Alpha Proxima — 10 Year Vision.md` | Missing required frontmatter field: institutional_owner |
| warning | `01_VISION/Alpha Proxima — 10 Year Vision.md` | Missing required frontmatter field: related_documents |
| warning | `01_VISION/Alpha Proxima — 10 Year Vision.md` | Missing required frontmatter field: related_research_programs |
| warning | `03_AI_COUNCIL/AI Council Registry.md` | Missing required frontmatter field: artifact_type |
| warning | `03_AI_COUNCIL/AI Council Registry.md` | Missing required frontmatter field: dependencies |
| warning | `03_AI_COUNCIL/AI Council Registry.md` | Missing required frontmatter field: institutional_owner |
| warning | `03_AI_COUNCIL/AI Council Registry.md` | Missing required frontmatter field: related_documents |
| warning | `03_AI_COUNCIL/AI Council Registry.md` | Missing required frontmatter field: related_research_programs |
| warning | `03_AI_COUNCIL/Alpha Council.md` | Missing required frontmatter field: artifact_type |
| warning | `03_AI_COUNCIL/Alpha Council.md` | Missing required frontmatter field: dependencies |
| warning | `03_AI_COUNCIL/Alpha Council.md` | Missing required frontmatter field: institutional_owner |
| warning | `03_AI_COUNCIL/Alpha Council.md` | Missing required frontmatter field: related_documents |
| warning | `03_AI_COUNCIL/Alpha Council.md` | Missing required frontmatter field: related_research_programs |
| warning | `03_AI_COUNCIL/Cognitive Council Charter.md` | Missing required frontmatter field: artifact_type |
| warning | `03_AI_COUNCIL/Cognitive Council Charter.md` | Missing required frontmatter field: dependencies |
| warning | `03_AI_COUNCIL/Cognitive Council Charter.md` | Missing required frontmatter field: institutional_owner |
| warning | `03_AI_COUNCIL/Cognitive Council Charter.md` | Missing required frontmatter field: related_documents |
| warning | `03_AI_COUNCIL/Cognitive Council Charter.md` | Missing required frontmatter field: related_research_programs |
| warning | `03_AI_COUNCIL/Cognitive Function Matrix.md` | Missing required frontmatter field: artifact_type |
| warning | `03_AI_COUNCIL/Cognitive Function Matrix.md` | Missing required frontmatter field: dependencies |
| warning | `03_AI_COUNCIL/Cognitive Function Matrix.md` | Missing required frontmatter field: institutional_owner |
| warning | `03_AI_COUNCIL/Cognitive Function Matrix.md` | Missing required frontmatter field: related_documents |
| warning | `03_AI_COUNCIL/Cognitive Function Matrix.md` | Missing required frontmatter field: related_research_programs |
| warning | `03_AI_COUNCIL/Cognitive Function Registry.md` | Missing required frontmatter field: artifact_type |
| warning | `03_AI_COUNCIL/Cognitive Function Registry.md` | Missing required frontmatter field: dependencies |
| warning | `03_AI_COUNCIL/Cognitive Function Registry.md` | Missing required frontmatter field: institutional_owner |
| warning | `03_AI_COUNCIL/Cognitive Function Registry.md` | Missing required frontmatter field: related_documents |
| warning | `03_AI_COUNCIL/Cognitive Function Registry.md` | Missing required frontmatter field: related_research_programs |
| warning | `03_AI_COUNCIL/Departments/ATHENA Charter.md` | Missing required frontmatter field: artifact_type |
| warning | `03_AI_COUNCIL/Departments/ATHENA Charter.md` | Missing required frontmatter field: dependencies |
| warning | `03_AI_COUNCIL/Departments/ATHENA Charter.md` | Missing required frontmatter field: institutional_owner |
| warning | `03_AI_COUNCIL/Departments/ATHENA Charter.md` | Missing required frontmatter field: related_documents |
| warning | `03_AI_COUNCIL/Departments/ATHENA Charter.md` | Missing required frontmatter field: related_research_programs |
| warning | `03_AI_COUNCIL/Departments/JERANIUM Charter.md` | Missing required frontmatter field: artifact_type |
| warning | `03_AI_COUNCIL/Departments/JERANIUM Charter.md` | Missing required frontmatter field: dependencies |
| warning | `03_AI_COUNCIL/Departments/JERANIUM Charter.md` | Missing required frontmatter field: institutional_owner |
| warning | `03_AI_COUNCIL/Departments/JERANIUM Charter.md` | Missing required frontmatter field: related_documents |
| warning | `03_AI_COUNCIL/Departments/JERANIUM Charter.md` | Missing required frontmatter field: related_research_programs |
| warning | `03_AI_COUNCIL/Departments/LUMIAION Charter.md` | Missing required frontmatter field: artifact_type |
| warning | `03_AI_COUNCIL/Departments/LUMIAION Charter.md` | Missing required frontmatter field: dependencies |
| warning | `03_AI_COUNCIL/Departments/LUMIAION Charter.md` | Missing required frontmatter field: institutional_owner |
| warning | `03_AI_COUNCIL/Departments/LUMIAION Charter.md` | Missing required frontmatter field: related_documents |
| warning | `03_AI_COUNCIL/Departments/LUMIAION Charter.md` | Missing required frontmatter field: related_research_programs |
| warning | `03_AI_COUNCIL/Departments/SOHMA Charter.md` | Missing required frontmatter field: artifact_type |
| warning | `03_AI_COUNCIL/Departments/SOHMA Charter.md` | Missing required frontmatter field: dependencies |
| warning | `03_AI_COUNCIL/Departments/SOHMA Charter.md` | Missing required frontmatter field: institutional_owner |
| warning | `03_AI_COUNCIL/Departments/SOHMA Charter.md` | Missing required frontmatter field: related_documents |
| warning | `03_AI_COUNCIL/Departments/SOHMA Charter.md` | Missing required frontmatter field: related_research_programs |
| warning | `03_AI_COUNCIL/Departments/VORTEX Charter.md` | Missing required frontmatter field: artifact_type |
| warning | `03_AI_COUNCIL/Departments/VORTEX Charter.md` | Missing required frontmatter field: dependencies |
| warning | `03_AI_COUNCIL/Departments/VORTEX Charter.md` | Missing required frontmatter field: institutional_owner |
| warning | `03_AI_COUNCIL/Departments/VORTEX Charter.md` | Missing required frontmatter field: related_documents |
| warning | `03_AI_COUNCIL/Departments/VORTEX Charter.md` | Missing required frontmatter field: related_research_programs |
| warning | `03_AI_COUNCIL/Engine Registry.md` | Missing required frontmatter field: artifact_type |
| warning | `03_AI_COUNCIL/Engine Registry.md` | Missing required frontmatter field: dependencies |
| warning | `03_AI_COUNCIL/Engine Registry.md` | Missing required frontmatter field: institutional_owner |
| warning | `03_AI_COUNCIL/Engine Registry.md` | Missing required frontmatter field: related_documents |
| warning | `03_AI_COUNCIL/Engine Registry.md` | Missing required frontmatter field: related_research_programs |
| warning | `03_AI_COUNCIL/Engine Succession Policy.md` | Missing required frontmatter field: artifact_type |
| warning | `03_AI_COUNCIL/Engine Succession Policy.md` | Missing required frontmatter field: dependencies |
| warning | `03_AI_COUNCIL/Engine Succession Policy.md` | Missing required frontmatter field: institutional_owner |
| warning | `03_AI_COUNCIL/Engine Succession Policy.md` | Missing required frontmatter field: related_documents |
| warning | `03_AI_COUNCIL/Engine Succession Policy.md` | Missing required frontmatter field: related_research_programs |
| warning | `03_AI_COUNCIL/Institutional Registry.md` | Missing required frontmatter field: artifact_type |
| warning | `03_AI_COUNCIL/Institutional Registry.md` | Missing required frontmatter field: dependencies |
| warning | `03_AI_COUNCIL/Institutional Registry.md` | Missing required frontmatter field: institutional_owner |
| warning | `03_AI_COUNCIL/Institutional Registry.md` | Missing required frontmatter field: related_documents |
| warning | `03_AI_COUNCIL/Institutional Registry.md` | Missing required frontmatter field: related_research_programs |
| warning | `03_AI_COUNCIL/YUNA Charter.md` | Missing required frontmatter field: artifact_type |
| warning | `03_AI_COUNCIL/YUNA Charter.md` | Missing required frontmatter field: dependencies |
| warning | `03_AI_COUNCIL/YUNA Charter.md` | Missing required frontmatter field: institutional_owner |
| warning | `03_AI_COUNCIL/YUNA Charter.md` | Missing required frontmatter field: related_documents |
| warning | `03_AI_COUNCIL/YUNA Charter.md` | Missing required frontmatter field: related_research_programs |
| warning | `04_DECISIONS/ADR-0001 - The Founding Decision.md` | Missing required frontmatter field: artifact_type |
| warning | `04_DECISIONS/ADR-0001 - The Founding Decision.md` | Missing required frontmatter field: dependencies |
| warning | `04_DECISIONS/ADR-0001 - The Founding Decision.md` | Missing required frontmatter field: institutional_owner |
| warning | `04_DECISIONS/ADR-0001 - The Founding Decision.md` | Missing required frontmatter field: related_documents |
| warning | `04_DECISIONS/ADR-0001 - The Founding Decision.md` | Missing required frontmatter field: related_research_programs |
| warning | `04_DECISIONS/ADR-0002 - Reconciling the Four Institutional Taxonomies.md` | Missing required frontmatter field: artifact_type |
| warning | `04_DECISIONS/ADR-0002 - Reconciling the Four Institutional Taxonomies.md` | Missing required frontmatter field: dependencies |
| warning | `04_DECISIONS/ADR-0002 - Reconciling the Four Institutional Taxonomies.md` | Missing required frontmatter field: institutional_owner |
| warning | `04_DECISIONS/ADR-0002 - Reconciling the Four Institutional Taxonomies.md` | Missing required frontmatter field: related_documents |
| warning | `04_DECISIONS/ADR-0002 - Reconciling the Four Institutional Taxonomies.md` | Missing required frontmatter field: related_research_programs |
| warning | `05_PROPOSALS/CN-0001 - Constitutional Alignment Gap Report.md` | Missing required frontmatter field: artifact_type |
| warning | `05_PROPOSALS/CN-0001 - Constitutional Alignment Gap Report.md` | Missing required frontmatter field: dependencies |
| warning | `05_PROPOSALS/CN-0001 - Constitutional Alignment Gap Report.md` | Missing required frontmatter field: institutional_owner |
| warning | `05_PROPOSALS/CN-0001 - Constitutional Alignment Gap Report.md` | Missing required frontmatter field: related_documents |
| warning | `05_PROPOSALS/CN-0001 - Constitutional Alignment Gap Report.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Canonical Terminology/Canonical Terminology Register.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Canonical Terminology/Canonical Terminology Register.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Canonical Terminology/Canonical Terminology Register.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Canonical Terminology/Canonical Terminology Register.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Canonical Terminology/Canonical Terminology Register.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Constitutional Audit/CAR-001 Constitutional Audit Report.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Constitutional Audit/CAR-001 Constitutional Audit Report.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Constitutional Audit/CAR-001 Constitutional Audit Report.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Constitutional Audit/CAR-001 Constitutional Audit Report.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Constitutional Audit/CAR-001 Constitutional Audit Report.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-001 Epoch III Constitutional Refactoring.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-001 Epoch III Constitutional Refactoring.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-001 Epoch III Constitutional Refactoring.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-001 Epoch III Constitutional Refactoring.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-001 Epoch III Constitutional Refactoring.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-002 Institutional Completeness Review.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-002 Institutional Completeness Review.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-002 Institutional Completeness Review.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-002 Institutional Completeness Review.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-002 Institutional Completeness Review.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-003 Epoch V Constitutional Coherence.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-003 Epoch V Constitutional Coherence.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-003 Epoch V Constitutional Coherence.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-003 Epoch V Constitutional Coherence.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Constitutional Impact Report/CIR-003 Epoch V Constitutional Coherence.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Directive Governance Framework/Directive Governance Framework.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Directive Governance Framework/Directive Governance Framework.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Directive Governance Framework/Directive Governance Framework.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Directive Governance Framework/Directive Governance Framework.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Directive Governance Framework/Directive Governance Framework.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Epoch V/Governance Model Crosswalk.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Epoch V/Governance Model Crosswalk.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Epoch V/Governance Model Crosswalk.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Epoch V/Governance Model Crosswalk.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Epoch V/Governance Model Crosswalk.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Epoch V/Interim Authority Instrument.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Epoch V/Interim Authority Instrument.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Epoch V/Interim Authority Instrument.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Epoch V/Interim Authority Instrument.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Epoch V/Interim Authority Instrument.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Foundation Gap Report/FGR-001 Epoch II Stewardship Audit.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Foundation Gap Report/FGR-001 Epoch II Stewardship Audit.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Foundation Gap Report/FGR-001 Epoch II Stewardship Audit.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Foundation Gap Report/FGR-001 Epoch II Stewardship Audit.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Foundation Gap Report/FGR-001 Epoch II Stewardship Audit.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Founder Directives/Founder Directives Register.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Founder Directives/Founder Directives Register.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Founder Directives/Founder Directives Register.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Founder Directives/Founder Directives Register.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Founder Directives/Founder Directives Register.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Institutional Glossary & Acronym Register.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Institutional Glossary & Acronym Register.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Institutional Glossary & Acronym Register.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Institutional Glossary & Acronym Register.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Institutional Glossary & Acronym Register.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Institutional Open Questions Register.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Institutional Open Questions Register.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Institutional Open Questions Register.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Institutional Open Questions Register.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Institutional Open Questions Register.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Institutional Policies/Citation Policy.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Institutional Policies/Citation Policy.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Institutional Policies/Citation Policy.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Institutional Policies/Citation Policy.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Institutional Policies/Citation Policy.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Institutional Policies/Metadata Policy.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Institutional Policies/Metadata Policy.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Institutional Policies/Metadata Policy.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Institutional Policies/Metadata Policy.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Institutional Policies/Metadata Policy.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Institutional Policies/Naming Policy.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Institutional Policies/Naming Policy.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Institutional Policies/Naming Policy.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Institutional Policies/Naming Policy.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Institutional Policies/Naming Policy.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Institutional Policies/Privacy Policy.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Institutional Policies/Privacy Policy.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Institutional Policies/Privacy Policy.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Institutional Policies/Privacy Policy.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Institutional Policies/Privacy Policy.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Institutional Policies/Source Attribution Policy.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Institutional Policies/Source Attribution Policy.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Institutional Policies/Source Attribution Policy.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Institutional Policies/Source Attribution Policy.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Institutional Policies/Source Attribution Policy.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Institutional Policies/Versioning Policy.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Institutional Policies/Versioning Policy.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Institutional Policies/Versioning Policy.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Institutional Policies/Versioning Policy.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Institutional Policies/Versioning Policy.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Institutional Timeline.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Institutional Timeline.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Institutional Timeline.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Institutional Timeline.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Institutional Timeline.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Research Debt Register/Research Debt Register.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Research Debt Register/Research Debt Register.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Research Debt Register/Research Debt Register.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Research Debt Register/Research Debt Register.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Research Debt Register/Research Debt Register.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Research Framework/Institutional Intelligence Translation Framework v1.0.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Research Framework/Institutional Intelligence Translation Framework v1.0.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Research Framework/Institutional Intelligence Translation Framework v1.0.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Research Framework/Institutional Intelligence Translation Framework v1.0.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Research Framework/Institutional Intelligence Translation Framework v1.0.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Research Framework/Research Integration Framework.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Research Framework/Research Integration Framework.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Research Framework/Research Integration Framework.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Research Framework/Research Integration Framework.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Research Framework/Research Integration Framework.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Research Framework/Research Program Playbook v1.0.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Research Framework/Research Program Playbook v1.0.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Research Framework/Research Program Playbook v1.0.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Research Framework/Research Program Playbook v1.0.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Research Framework/Research Program Playbook v1.0.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Research Framework/Translation Checklist.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Research Framework/Translation Checklist.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Research Framework/Translation Checklist.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Research Framework/Translation Checklist.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Research Framework/Translation Checklist.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Research Framework/Translation Decision Matrix.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Research Framework/Translation Decision Matrix.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Research Framework/Translation Decision Matrix.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Research Framework/Translation Decision Matrix.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Research Framework/Translation Decision Matrix.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Research Framework/Translation Review Process.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Research Framework/Translation Review Process.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Research Framework/Translation Review Process.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Research Framework/Translation Review Process.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Research Framework/Translation Review Process.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Research Methodology/Alpha Proxima Research Methodology v1.0.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Research Methodology/Alpha Proxima Research Methodology v1.0.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Research Methodology/Alpha Proxima Research Methodology v1.0.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Research Methodology/Alpha Proxima Research Methodology v1.0.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Research Methodology/Alpha Proxima Research Methodology v1.0.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Standards Council/Standards Council Evaluation.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Standards Council/Standards Council Evaluation.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Standards Council/Standards Council Evaluation.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Standards Council/Standards Council Evaluation.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Standards Council/Standards Council Evaluation.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Missing required frontmatter field: authors |
| warning | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Standing Orders/SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` | Missing required frontmatter field: related_research_programs |
| warning | `06_GOVERNANCE/Standing Orders/Standing Orders Register.md` | Missing required frontmatter field: artifact_type |
| warning | `06_GOVERNANCE/Standing Orders/Standing Orders Register.md` | Missing required frontmatter field: dependencies |
| warning | `06_GOVERNANCE/Standing Orders/Standing Orders Register.md` | Missing required frontmatter field: institutional_owner |
| warning | `06_GOVERNANCE/Standing Orders/Standing Orders Register.md` | Missing required frontmatter field: related_documents |
| warning | `06_GOVERNANCE/Standing Orders/Standing Orders Register.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/00 Executive Summary/RP-001 Executive Summary.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/01 Research Question/RP-001 Research Question.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/01 Research Question/RP-001 Research Question.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/01 Research Question/RP-001 Research Question.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/01 Research Question/RP-001 Research Question.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/01 Research Question/RP-001 Research Question.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/02 Objectives/RP-001 Objectives.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/02 Objectives/RP-001 Objectives.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/02 Objectives/RP-001 Objectives.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/02 Objectives/RP-001 Objectives.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/02 Objectives/RP-001 Objectives.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/03 Source Registry/RP-001 Source Registry.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/03 Source Registry/RP-001 Source Registry.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/03 Source Registry/RP-001 Source Registry.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/03 Source Registry/RP-001 Source Registry.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/03 Source Registry/RP-001 Source Registry.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/04 Source - Perplexity/RP-001 Source Note - Perplexity.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/04 Source - Perplexity/RP-001 Source Note - Perplexity.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/04 Source - Perplexity/RP-001 Source Note - Perplexity.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/04 Source - Perplexity/RP-001 Source Note - Perplexity.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/04 Source - Perplexity/RP-001 Source Note - Perplexity.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/05 Source - Gemini/RP-001 Source Note - Gemini.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/05 Source - Gemini/RP-001 Source Note - Gemini.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/05 Source - Gemini/RP-001 Source Note - Gemini.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/05 Source - Gemini/RP-001 Source Note - Gemini.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/05 Source - Gemini/RP-001 Source Note - Gemini.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/06 Source - SanaLab/RP-001 Source Note - SanaLab.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/06 Source - SanaLab/RP-001 Source Note - SanaLab.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/06 Source - SanaLab/RP-001 Source Note - SanaLab.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/06 Source - SanaLab/RP-001 Source Note - SanaLab.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/06 Source - SanaLab/RP-001 Source Note - SanaLab.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/07 Future Sources/RP-001 Future Sources.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/07 Future Sources/RP-001 Future Sources.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/07 Future Sources/RP-001 Future Sources.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/07 Future Sources/RP-001 Future Sources.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/07 Future Sources/RP-001 Future Sources.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/08 Comparative Framework/RP-001 Comparative Framework.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/08 Comparative Framework/RP-001 Comparative Framework.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/08 Comparative Framework/RP-001 Comparative Framework.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/08 Comparative Framework/RP-001 Comparative Framework.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/08 Comparative Framework/RP-001 Comparative Framework.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/10 Theory Matrix/RP-001 Theory Matrix.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/10 Theory Matrix/RP-001 Theory Matrix.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/10 Theory Matrix/RP-001 Theory Matrix.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/10 Theory Matrix/RP-001 Theory Matrix.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/10 Theory Matrix/RP-001 Theory Matrix.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/11 Canonical Glossary/RP-001 Canonical Glossary.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/11 Canonical Glossary/RP-001 Canonical Glossary.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/11 Canonical Glossary/RP-001 Canonical Glossary.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/11 Canonical Glossary/RP-001 Canonical Glossary.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/11 Canonical Glossary/RP-001 Canonical Glossary.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/4E Cognition.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Active Inference.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Attention Schema Theory.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Attention Schema Theory.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Attention Schema Theory.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Attention Schema Theory.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Attention Schema Theory.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Attention Schema Theory.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Attention Schema Theory.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Attention Schema Theory.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Higher-Order Thought Theory.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Higher-Order Thought Theory.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Higher-Order Thought Theory.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Higher-Order Thought Theory.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Higher-Order Thought Theory.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Higher-Order Thought Theory.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Higher-Order Thought Theory.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Higher-Order Thought Theory.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Illusionism.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Illusionism.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Illusionism.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Illusionism.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Illusionism.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Illusionism.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Illusionism.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Illusionism.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Integrated Information Theory.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Meta Awareness.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Meta Awareness.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Meta Awareness.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Meta Awareness.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Meta Awareness.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Meta Awareness.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Meta Awareness.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Meta Awareness.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Neural Correlates of Consciousness.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Orchestrated Objective Reduction.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Panpsychism.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-001/13 Research Graph/Concepts/Recurrent Processing Theory.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-001/13 Research Graph/RP-001 Research Graph.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/13 Research Graph/RP-001 Research Graph.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/13 Research Graph/RP-001 Research Graph.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/13 Research Graph/RP-001 Research Graph.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/13 Research Graph/RP-001 Research Graph.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/14 Open Questions/RP-001 Open Questions.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/14 Open Questions/RP-001 Open Questions.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/14 Open Questions/RP-001 Open Questions.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/14 Open Questions/RP-001 Open Questions.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/14 Open Questions/RP-001 Open Questions.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/15 Future Experiments/RP-001 Future Research Opportunities.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/15 Future Experiments/RP-001 Future Research Opportunities.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/15 Future Experiments/RP-001 Future Research Opportunities.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/15 Future Experiments/RP-001 Future Research Opportunities.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/15 Future Experiments/RP-001 Future Research Opportunities.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/16 Visual Knowledge/RP-001 Visual Knowledge Index.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/16 Visual Knowledge/RP-001 Visual Knowledge Index.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/16 Visual Knowledge/RP-001 Visual Knowledge Index.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/16 Visual Knowledge/RP-001 Visual Knowledge Index.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/16 Visual Knowledge/RP-001 Visual Knowledge Index.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/17 NotebookLM Package/RP-001 NotebookLM Source Pack.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/17 NotebookLM Package/RP-001 NotebookLM Source Pack.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/17 NotebookLM Package/RP-001 NotebookLM Source Pack.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/17 NotebookLM Package/RP-001 NotebookLM Source Pack.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/17 NotebookLM Package/RP-001 NotebookLM Source Pack.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/18 Related Constitution/RP-001 Constitutional Links.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/18 Related Constitution/RP-001 Constitutional Links.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/18 Related Constitution/RP-001 Constitutional Links.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/18 Related Constitution/RP-001 Constitutional Links.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/18 Related Constitution/RP-001 Constitutional Links.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/19 Related Laws/RP-001 Governing Provisions.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/19 Related Laws/RP-001 Governing Provisions.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/19 Related Laws/RP-001 Governing Provisions.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/19 Related Laws/RP-001 Governing Provisions.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/19 Related Laws/RP-001 Governing Provisions.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/20 Related ADRs/RP-001 ADR Links.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/20 Related ADRs/RP-001 ADR Links.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/20 Related ADRs/RP-001 ADR Links.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/20 Related ADRs/RP-001 ADR Links.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/20 Related ADRs/RP-001 ADR Links.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/21 Version History/RP-001 Version History.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/21 Version History/RP-001 Version History.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/21 Version History/RP-001 Version History.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/21 Version History/RP-001 Version History.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/21 Version History/RP-001 Version History.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/ARCHIVE/ARCHIVE Philosophy.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/ARCHIVE/ARCHIVE Philosophy.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/ARCHIVE/ARCHIVE Philosophy.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/ARCHIVE/ARCHIVE Philosophy.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/ARCHIVE/ARCHIVE Philosophy.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-001 Architecture of Human Consciousness.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-003 Comparative Framework - SanaLab.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-001/ARCHIVE/DOC-004 GNWT vs IIT Deep Dive - SanaLab.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/00 Executive Summary/RP-002 Executive Summary.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/00 Executive Summary/RP-002 Executive Summary.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/00 Executive Summary/RP-002 Executive Summary.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/00 Executive Summary/RP-002 Executive Summary.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/00 Executive Summary/RP-002 Executive Summary.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/01 Research Question/RP-002 Research Question.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/01 Research Question/RP-002 Research Question.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/01 Research Question/RP-002 Research Question.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/01 Research Question/RP-002 Research Question.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/01 Research Question/RP-002 Research Question.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/02 Objectives/RP-002 Objectives.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/02 Objectives/RP-002 Objectives.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/02 Objectives/RP-002 Objectives.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/02 Objectives/RP-002 Objectives.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/02 Objectives/RP-002 Objectives.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/03 Source Registry/RP-002 Source Registry.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/03 Source Registry/RP-002 Source Registry.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/03 Source Registry/RP-002 Source Registry.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/03 Source Registry/RP-002 Source Registry.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/03 Source Registry/RP-002 Source Registry.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/04 Source - CORE-002/RP-002 Source Note - CORE-002.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/04 Source - CORE-002/RP-002 Source Note - CORE-002.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/04 Source - CORE-002/RP-002 Source Note - CORE-002.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/04 Source - CORE-002/RP-002 Source Note - CORE-002.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/04 Source - CORE-002/RP-002 Source Note - CORE-002.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/05 Source - SanaLab/RP-002 Source Note - SanaLab.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/05 Source - SanaLab/RP-002 Source Note - SanaLab.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/05 Source - SanaLab/RP-002 Source Note - SanaLab.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/05 Source - SanaLab/RP-002 Source Note - SanaLab.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/05 Source - SanaLab/RP-002 Source Note - SanaLab.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/06 Source - Illustrated/RP-002 Source Note - Illustrated.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/06 Source - Illustrated/RP-002 Source Note - Illustrated.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/06 Source - Illustrated/RP-002 Source Note - Illustrated.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/06 Source - Illustrated/RP-002 Source Note - Illustrated.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/06 Source - Illustrated/RP-002 Source Note - Illustrated.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/07 Future Sources/RP-002 Future Sources.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/07 Future Sources/RP-002 Future Sources.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/07 Future Sources/RP-002 Future Sources.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/07 Future Sources/RP-002 Future Sources.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/07 Future Sources/RP-002 Future Sources.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/08 Comparative Framework/RP-002 Comparative Framework.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/08 Comparative Framework/RP-002 Comparative Framework.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/08 Comparative Framework/RP-002 Comparative Framework.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/08 Comparative Framework/RP-002 Comparative Framework.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/08 Comparative Framework/RP-002 Comparative Framework.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/09 Canonical Synthesis/RP-002 Canonical Synthesis.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/09 Canonical Synthesis/RP-002 Canonical Synthesis.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/09 Canonical Synthesis/RP-002 Canonical Synthesis.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/09 Canonical Synthesis/RP-002 Canonical Synthesis.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/09 Canonical Synthesis/RP-002 Canonical Synthesis.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/10 Theory Matrix/RP-002 Theory Matrix.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/10 Theory Matrix/RP-002 Theory Matrix.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/10 Theory Matrix/RP-002 Theory Matrix.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/10 Theory Matrix/RP-002 Theory Matrix.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/10 Theory Matrix/RP-002 Theory Matrix.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/11 Canonical Glossary/RP-002 Canonical Glossary.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/11 Canonical Glossary/RP-002 Canonical Glossary.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/11 Canonical Glossary/RP-002 Canonical Glossary.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/11 Canonical Glossary/RP-002 Canonical Glossary.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/11 Canonical Glossary/RP-002 Canonical Glossary.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/12 Evidence Registry/RP-002 Evidence Registry.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/12 Evidence Registry/RP-002 Evidence Registry.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/12 Evidence Registry/RP-002 Evidence Registry.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/12 Evidence Registry/RP-002 Evidence Registry.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/12 Evidence Registry/RP-002 Evidence Registry.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Collective Memory.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Collective Memory.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Collective Memory.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Collective Memory.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Collective Memory.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Collective Memory.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Collective Memory.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Collective Memory.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Contemplative Memory.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Contemplative Memory.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Contemplative Memory.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Contemplative Memory.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Contemplative Memory.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Contemplative Memory.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Contemplative Memory.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Contemplative Memory.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Engram.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Engram.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Engram.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Engram.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Engram.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Engram.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Engram.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Engram.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Hippocampus.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Hippocampus.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Hippocampus.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Hippocampus.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Hippocampus.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Hippocampus.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Hippocampus.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Hippocampus.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/LTP - Synaptic Plasticity.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/LTP - Synaptic Plasticity.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/LTP - Synaptic Plasticity.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/LTP - Synaptic Plasticity.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/LTP - Synaptic Plasticity.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/LTP - Synaptic Plasticity.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/LTP - Synaptic Plasticity.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/LTP - Synaptic Plasticity.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Memory.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Memory.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Memory.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Memory.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Memory.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Memory.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Memory.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Memory.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Pattern Separation and Completion.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Pattern Separation and Completion.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Pattern Separation and Completion.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Pattern Separation and Completion.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Pattern Separation and Completion.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Pattern Separation and Completion.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Pattern Separation and Completion.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Pattern Separation and Completion.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Reconsolidation.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Reconsolidation.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Reconsolidation.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Reconsolidation.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Reconsolidation.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Reconsolidation.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Reconsolidation.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Reconsolidation.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Trauma Memory.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Trauma Memory.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Trauma Memory.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Trauma Memory.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Trauma Memory.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Trauma Memory.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Trauma Memory.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Trauma Memory.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Working Memory.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Working Memory.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Working Memory.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Working Memory.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Working Memory.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Working Memory.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Working Memory.md` | Missing required frontmatter field: status |
| warning | `07_RESEARCH/RP-002/13 Research Graph/Concepts/Working Memory.md` | Missing required frontmatter field: version |
| warning | `07_RESEARCH/RP-002/13 Research Graph/RP-002 Research Graph.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/13 Research Graph/RP-002 Research Graph.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/13 Research Graph/RP-002 Research Graph.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/13 Research Graph/RP-002 Research Graph.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/13 Research Graph/RP-002 Research Graph.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/14 Open Questions/RP-002 Open Questions.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/14 Open Questions/RP-002 Open Questions.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/14 Open Questions/RP-002 Open Questions.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/14 Open Questions/RP-002 Open Questions.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/14 Open Questions/RP-002 Open Questions.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/15 Future Experiments/RP-002 Future Research Opportunities.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/15 Future Experiments/RP-002 Future Research Opportunities.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/15 Future Experiments/RP-002 Future Research Opportunities.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/15 Future Experiments/RP-002 Future Research Opportunities.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/15 Future Experiments/RP-002 Future Research Opportunities.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/16 Visual Knowledge/RP-002 Visual Knowledge Index.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/16 Visual Knowledge/RP-002 Visual Knowledge Index.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/16 Visual Knowledge/RP-002 Visual Knowledge Index.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/16 Visual Knowledge/RP-002 Visual Knowledge Index.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/16 Visual Knowledge/RP-002 Visual Knowledge Index.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/17 NotebookLM Package/RP-002 NotebookLM Source Pack.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/17 NotebookLM Package/RP-002 NotebookLM Source Pack.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/17 NotebookLM Package/RP-002 NotebookLM Source Pack.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/17 NotebookLM Package/RP-002 NotebookLM Source Pack.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/17 NotebookLM Package/RP-002 NotebookLM Source Pack.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/18 Related Constitution/RP-002 Constitutional Links.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/18 Related Constitution/RP-002 Constitutional Links.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/18 Related Constitution/RP-002 Constitutional Links.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/18 Related Constitution/RP-002 Constitutional Links.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/18 Related Constitution/RP-002 Constitutional Links.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/19 Related Laws/RP-002 Governing Provisions.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/19 Related Laws/RP-002 Governing Provisions.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/19 Related Laws/RP-002 Governing Provisions.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/19 Related Laws/RP-002 Governing Provisions.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/19 Related Laws/RP-002 Governing Provisions.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/20 Related ADRs/RP-002 ADR Links.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/20 Related ADRs/RP-002 ADR Links.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/20 Related ADRs/RP-002 ADR Links.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/20 Related ADRs/RP-002 ADR Links.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/20 Related ADRs/RP-002 ADR Links.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/21 Version History/RP-002 Version History.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/21 Version History/RP-002 Version History.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/21 Version History/RP-002 Version History.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/21 Version History/RP-002 Version History.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/21 Version History/RP-002 Version History.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/ARCHIVE/ARCHIVE Philosophy.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/ARCHIVE/ARCHIVE Philosophy.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/ARCHIVE/ARCHIVE Philosophy.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/ARCHIVE/ARCHIVE Philosophy.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/ARCHIVE/ARCHIVE Philosophy.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-A Architecture Systemique Memoire Humaine.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-A Architecture Systemique Memoire Humaine.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-A Architecture Systemique Memoire Humaine.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-A Architecture Systemique Memoire Humaine.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-A Architecture Systemique Memoire Humaine.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-A Architecture Systemique Memoire Humaine.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-B Interdisciplinary Comparative Framework Memory.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-B Interdisciplinary Comparative Framework Memory.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-B Interdisciplinary Comparative Framework Memory.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-B Interdisciplinary Comparative Framework Memory.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-B Interdisciplinary Comparative Framework Memory.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-B Interdisciplinary Comparative Framework Memory.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-C RP-002 Illustrated.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-C RP-002 Illustrated.md` | Missing required frontmatter field: authors |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-C RP-002 Illustrated.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-C RP-002 Illustrated.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-C RP-002 Illustrated.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-002/ARCHIVE/DOC-C RP-002 Illustrated.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Canonical Synthesis.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Canonical Synthesis.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Canonical Synthesis.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Canonical Synthesis.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Canonical Synthesis.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Institutional Synthesis Report.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Institutional Synthesis Report.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Institutional Synthesis Report.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Institutional Synthesis Report.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Institutional Synthesis Report.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Knowledge Graph Update Recommendations.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Knowledge Graph Update Recommendations.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Knowledge Graph Update Recommendations.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Knowledge Graph Update Recommendations.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-003/00 Institutional Stewardship Review/ISR-001 Knowledge Graph Update Recommendations.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-003/RP-003 Master Index.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-003/RP-003 Master Index.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-003/RP-003 Master Index.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-003/RP-003 Master Index.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-003/RP-003 Master Index.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-004/RP-004 Master Index.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-004/RP-004 Master Index.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-004/RP-004 Master Index.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-004/RP-004 Master Index.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-004/RP-004 Master Index.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-005/RP-005 Master Index.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-005/RP-005 Master Index.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-005/RP-005 Master Index.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-005/RP-005 Master Index.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-005/RP-005 Master Index.md` | Missing required frontmatter field: related_research_programs |
| warning | `07_RESEARCH/RP-006/RP-006 Master Index.md` | Missing required frontmatter field: artifact_type |
| warning | `07_RESEARCH/RP-006/RP-006 Master Index.md` | Missing required frontmatter field: dependencies |
| warning | `07_RESEARCH/RP-006/RP-006 Master Index.md` | Missing required frontmatter field: institutional_owner |
| warning | `07_RESEARCH/RP-006/RP-006 Master Index.md` | Missing required frontmatter field: related_documents |
| warning | `07_RESEARCH/RP-006/RP-006 Master Index.md` | Missing required frontmatter field: related_research_programs |
| warning | `08_SYSTEMS/Alpha Proxima Operating Model v1.0.md` | Missing required frontmatter field: artifact_type |
| warning | `08_SYSTEMS/Alpha Proxima Operating Model v1.0.md` | Missing required frontmatter field: dependencies |
| warning | `08_SYSTEMS/Alpha Proxima Operating Model v1.0.md` | Missing required frontmatter field: institutional_owner |
| warning | `08_SYSTEMS/Alpha Proxima Operating Model v1.0.md` | Missing required frontmatter field: related_documents |
| warning | `08_SYSTEMS/Alpha Proxima Operating Model v1.0.md` | Missing required frontmatter field: related_research_programs |
| warning | `08_SYSTEMS/Automation/Vault Note Generator.md` | Missing required frontmatter field: artifact_type |
| warning | `08_SYSTEMS/Automation/Vault Note Generator.md` | Missing required frontmatter field: institutional_owner |
| warning | `08_SYSTEMS/Foundational Architecture.md` | Missing required frontmatter field: artifact_type |
| warning | `08_SYSTEMS/Foundational Architecture.md` | Missing required frontmatter field: dependencies |
| warning | `08_SYSTEMS/Foundational Architecture.md` | Missing required frontmatter field: institutional_owner |
| warning | `08_SYSTEMS/Foundational Architecture.md` | Missing required frontmatter field: related_documents |
| warning | `08_SYSTEMS/Foundational Architecture.md` | Missing required frontmatter field: related_research_programs |
| warning | `08_SYSTEMS/Institutional Relationship Map.md` | Missing required frontmatter field: artifact_type |
| warning | `08_SYSTEMS/Institutional Relationship Map.md` | Missing required frontmatter field: dependencies |
| warning | `08_SYSTEMS/Institutional Relationship Map.md` | Missing required frontmatter field: institutional_owner |
| warning | `08_SYSTEMS/Institutional Relationship Map.md` | Missing required frontmatter field: related_documents |
| warning | `08_SYSTEMS/Institutional Relationship Map.md` | Missing required frontmatter field: related_research_programs |
| warning | `08_SYSTEMS/LUMIAION Architecture Spec v0.1.md` | Missing required frontmatter field: artifact_type |
| warning | `08_SYSTEMS/LUMIAION Architecture Spec v0.1.md` | Missing required frontmatter field: dependencies |
| warning | `08_SYSTEMS/LUMIAION Architecture Spec v0.1.md` | Missing required frontmatter field: institutional_owner |
| warning | `08_SYSTEMS/LUMIAION Architecture Spec v0.1.md` | Missing required frontmatter field: related_documents |
| warning | `08_SYSTEMS/LUMIAION Architecture Spec v0.1.md` | Missing required frontmatter field: related_research_programs |
| warning | `08_SYSTEMS/Protocols/Communication Protocol.md` | Missing required frontmatter field: artifact_type |
| warning | `08_SYSTEMS/Protocols/Communication Protocol.md` | Missing required frontmatter field: dependencies |
| warning | `08_SYSTEMS/Protocols/Communication Protocol.md` | Missing required frontmatter field: institutional_owner |
| warning | `08_SYSTEMS/Protocols/Communication Protocol.md` | Missing required frontmatter field: related_documents |
| warning | `08_SYSTEMS/Protocols/Communication Protocol.md` | Missing required frontmatter field: related_research_programs |
| warning | `08_SYSTEMS/Protocols/Decision Routing Protocol.md` | Missing required frontmatter field: artifact_type |
| warning | `08_SYSTEMS/Protocols/Decision Routing Protocol.md` | Missing required frontmatter field: dependencies |
| warning | `08_SYSTEMS/Protocols/Decision Routing Protocol.md` | Missing required frontmatter field: institutional_owner |
| warning | `08_SYSTEMS/Protocols/Decision Routing Protocol.md` | Missing required frontmatter field: related_documents |
| warning | `08_SYSTEMS/Protocols/Decision Routing Protocol.md` | Missing required frontmatter field: related_research_programs |
| warning | `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` | Missing required frontmatter field: artifact_type |
| warning | `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` | Missing required frontmatter field: dependencies |
| warning | `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` | Missing required frontmatter field: institutional_owner |
| warning | `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` | Missing required frontmatter field: related_documents |
| warning | `08_SYSTEMS/Protocols/Knowledge Ownership Protocol.md` | Missing required frontmatter field: related_research_programs |
| warning | `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` | Missing required frontmatter field: artifact_type |
| warning | `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` | Missing required frontmatter field: dependencies |
| warning | `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` | Missing required frontmatter field: institutional_owner |
| warning | `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` | Missing required frontmatter field: related_documents |
| warning | `08_SYSTEMS/Protocols/Knowledge Routing Protocol.md` | Missing required frontmatter field: related_research_programs |
| warning | `08_SYSTEMS/Protocols/Research Governance Protocol.md` | Missing required frontmatter field: artifact_type |
| warning | `08_SYSTEMS/Protocols/Research Governance Protocol.md` | Missing required frontmatter field: dependencies |
| warning | `08_SYSTEMS/Protocols/Research Governance Protocol.md` | Missing required frontmatter field: institutional_owner |
| warning | `08_SYSTEMS/Protocols/Research Governance Protocol.md` | Missing required frontmatter field: related_documents |
| warning | `08_SYSTEMS/Protocols/Research Governance Protocol.md` | Missing required frontmatter field: related_research_programs |
| warning | `08_SYSTEMS/The Orchestration Framework.md` | Missing required frontmatter field: artifact_type |
| warning | `08_SYSTEMS/The Orchestration Framework.md` | Missing required frontmatter field: dependencies |
| warning | `08_SYSTEMS/The Orchestration Framework.md` | Missing required frontmatter field: institutional_owner |
| warning | `08_SYSTEMS/The Orchestration Framework.md` | Missing required frontmatter field: related_documents |
| warning | `08_SYSTEMS/The Orchestration Framework.md` | Missing required frontmatter field: related_research_programs |
| warning | `08_SYSTEMS/Visual Systems/Color System - Implementation Checklist.md` | Missing required frontmatter field: related_research_programs |
| warning | `09_OFFICES/Engineering Office/Engineering Office Charter.md` | Missing required frontmatter field: artifact_type |
| warning | `09_OFFICES/Engineering Office/Engineering Office Charter.md` | Missing required frontmatter field: dependencies |
| warning | `09_OFFICES/Engineering Office/Engineering Office Charter.md` | Missing required frontmatter field: institutional_owner |
| warning | `09_OFFICES/Engineering Office/Engineering Office Charter.md` | Missing required frontmatter field: related_documents |
| warning | `09_OFFICES/Engineering Office/Engineering Office Charter.md` | Missing required frontmatter field: related_research_programs |
| warning | `09_OFFICES/Ethics Council/Ethics Council Charter.md` | Missing required frontmatter field: artifact_type |
| warning | `09_OFFICES/Ethics Council/Ethics Council Charter.md` | Missing required frontmatter field: dependencies |
| warning | `09_OFFICES/Ethics Council/Ethics Council Charter.md` | Missing required frontmatter field: institutional_owner |
| warning | `09_OFFICES/Ethics Council/Ethics Council Charter.md` | Missing required frontmatter field: related_documents |
| warning | `09_OFFICES/Ethics Council/Ethics Council Charter.md` | Missing required frontmatter field: related_research_programs |
| warning | `09_OFFICES/Executive Office/Executive Office Charter.md` | Missing required frontmatter field: artifact_type |
| warning | `09_OFFICES/Executive Office/Executive Office Charter.md` | Missing required frontmatter field: dependencies |
| warning | `09_OFFICES/Executive Office/Executive Office Charter.md` | Missing required frontmatter field: institutional_owner |
| warning | `09_OFFICES/Executive Office/Executive Office Charter.md` | Missing required frontmatter field: related_documents |
| warning | `09_OFFICES/Executive Office/Executive Office Charter.md` | Missing required frontmatter field: related_research_programs |
| warning | `09_OFFICES/Institutional Observatory/Institutional Observatory Charter.md` | Missing required frontmatter field: artifact_type |
| warning | `09_OFFICES/Institutional Observatory/Institutional Observatory Charter.md` | Missing required frontmatter field: dependencies |
| warning | `09_OFFICES/Institutional Observatory/Institutional Observatory Charter.md` | Missing required frontmatter field: institutional_owner |
| warning | `09_OFFICES/Institutional Observatory/Institutional Observatory Charter.md` | Missing required frontmatter field: related_documents |
| warning | `09_OFFICES/Institutional Observatory/Institutional Observatory Charter.md` | Missing required frontmatter field: related_research_programs |
| warning | `09_OFFICES/LUMIAION/LUMIAION Charter.md` | Missing required frontmatter field: artifact_type |
| warning | `09_OFFICES/LUMIAION/LUMIAION Charter.md` | Missing required frontmatter field: dependencies |
| warning | `09_OFFICES/LUMIAION/LUMIAION Charter.md` | Missing required frontmatter field: institutional_owner |
| warning | `09_OFFICES/LUMIAION/LUMIAION Charter.md` | Missing required frontmatter field: related_documents |
| warning | `09_OFFICES/LUMIAION/LUMIAION Charter.md` | Missing required frontmatter field: related_research_programs |
| warning | `09_OFFICES/Research Intelligence Office/Research Intelligence Office Charter.md` | Missing required frontmatter field: artifact_type |
| warning | `09_OFFICES/Research Intelligence Office/Research Intelligence Office Charter.md` | Missing required frontmatter field: dependencies |
| warning | `09_OFFICES/Research Intelligence Office/Research Intelligence Office Charter.md` | Missing required frontmatter field: institutional_owner |
| warning | `09_OFFICES/Research Intelligence Office/Research Intelligence Office Charter.md` | Missing required frontmatter field: related_documents |
| warning | `09_OFFICES/Research Intelligence Office/Research Intelligence Office Charter.md` | Missing required frontmatter field: related_research_programs |
| warning | `09_OFFICES/Research Intelligence Office/Research Office Matrix.md` | Missing required frontmatter field: artifact_type |
| warning | `09_OFFICES/Research Intelligence Office/Research Office Matrix.md` | Missing required frontmatter field: dependencies |
| warning | `09_OFFICES/Research Intelligence Office/Research Office Matrix.md` | Missing required frontmatter field: institutional_owner |
| warning | `09_OFFICES/Research Intelligence Office/Research Office Matrix.md` | Missing required frontmatter field: related_documents |
| warning | `09_OFFICES/Research Intelligence Office/Research Office Matrix.md` | Missing required frontmatter field: related_research_programs |
| warning | `10_TEMPLATES/ADR Template.md` | Missing required frontmatter field: artifact_type |
| warning | `10_TEMPLATES/ADR Template.md` | Missing required frontmatter field: dependencies |
| warning | `10_TEMPLATES/ADR Template.md` | Missing required frontmatter field: institutional_owner |
| warning | `10_TEMPLATES/ADR Template.md` | Missing required frontmatter field: related_documents |
| warning | `10_TEMPLATES/ADR Template.md` | Missing required frontmatter field: related_research_programs |
| warning | `10_TEMPLATES/Concept Note Template.md` | Missing required frontmatter field: artifact_type |
| warning | `10_TEMPLATES/Concept Note Template.md` | Missing required frontmatter field: dependencies |
| warning | `10_TEMPLATES/Concept Note Template.md` | Missing required frontmatter field: institutional_owner |
| warning | `10_TEMPLATES/Concept Note Template.md` | Missing required frontmatter field: related_documents |
| warning | `10_TEMPLATES/Concept Note Template.md` | Missing required frontmatter field: related_research_programs |
| warning | `10_TEMPLATES/Implementation Note Template.md` | Missing required frontmatter field: artifact_type |
| warning | `10_TEMPLATES/Implementation Note Template.md` | Missing required frontmatter field: dependencies |
| warning | `10_TEMPLATES/Implementation Note Template.md` | Missing required frontmatter field: institutional_owner |
| warning | `10_TEMPLATES/Institutional Translation Template v1.0.md` | Missing required frontmatter field: artifact_type |
| warning | `10_TEMPLATES/Institutional Translation Template v1.0.md` | Missing required frontmatter field: dependencies |
| warning | `10_TEMPLATES/Institutional Translation Template v1.0.md` | Missing required frontmatter field: institutional_owner |
| warning | `10_TEMPLATES/Institutional Translation Template v1.0.md` | Missing required frontmatter field: related_documents |
| warning | `10_TEMPLATES/Institutional Translation Template v1.0.md` | Missing required frontmatter field: related_research_programs |
| warning | `10_TEMPLATES/Research Commission Template v2.0.md` | Missing required frontmatter field: artifact_type |
| warning | `10_TEMPLATES/Research Commission Template v2.0.md` | Missing required frontmatter field: dependencies |
| warning | `10_TEMPLATES/Research Commission Template v2.0.md` | Missing required frontmatter field: institutional_owner |
| warning | `10_TEMPLATES/Research Commission Template v2.0.md` | Missing required frontmatter field: related_documents |
| warning | `10_TEMPLATES/Research Commission Template v2.0.md` | Missing required frontmatter field: related_research_programs |
| warning | `10_TEMPLATES/Research Note Template.md` | Missing required frontmatter field: artifact_type |
| warning | `10_TEMPLATES/Research Note Template.md` | Missing required frontmatter field: dependencies |
| warning | `10_TEMPLATES/Research Note Template.md` | Missing required frontmatter field: institutional_owner |
| warning | `10_TEMPLATES/Research Note Template.md` | Missing required frontmatter field: related_documents |
| warning | `10_TEMPLATES/Research Note Template.md` | Missing required frontmatter field: related_research_programs |
| warning | `10_TEMPLATES/Research Program Template/Research Program Methodology.md` | Missing required frontmatter field: artifact_type |
| warning | `10_TEMPLATES/Research Program Template/Research Program Methodology.md` | Missing required frontmatter field: dependencies |
| warning | `10_TEMPLATES/Research Program Template/Research Program Methodology.md` | Missing required frontmatter field: institutional_owner |
| warning | `10_TEMPLATES/Research Program Template/Research Program Methodology.md` | Missing required frontmatter field: related_documents |
| warning | `10_TEMPLATES/Research Program Template/Research Program Methodology.md` | Missing required frontmatter field: related_research_programs |
| warning | `10_TEMPLATES/Vault Structure Convention.md` | Missing required frontmatter field: artifact_type |
| warning | `10_TEMPLATES/Vault Structure Convention.md` | Missing required frontmatter field: dependencies |
| warning | `10_TEMPLATES/Vault Structure Convention.md` | Missing required frontmatter field: institutional_owner |
| warning | `10_TEMPLATES/Vault Structure Convention.md` | Missing required frontmatter field: related_documents |
| warning | `10_TEMPLATES/Vault Structure Convention.md` | Missing required frontmatter field: related_research_programs |
| warning | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Missing required frontmatter field: aliases |
| warning | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Missing required frontmatter field: artifact_type |
| warning | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Missing required frontmatter field: authors |
| warning | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Missing required frontmatter field: dependencies |
| warning | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Missing required frontmatter field: institutional_owner |
| warning | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Missing required frontmatter field: related_documents |
| warning | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Missing required frontmatter field: related_research_programs |
| warning | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Missing required frontmatter field: updated |
| warning | `99_ARCHIVE/Legacy ALPHA PROXIMA/README.md` | Missing required frontmatter field: version |
| warning | `Alpha Proxima Core.md` | Missing required frontmatter field: artifact_type |
| warning | `Alpha Proxima Core.md` | Missing required frontmatter field: dependencies |
| warning | `Alpha Proxima Core.md` | Missing required frontmatter field: institutional_owner |
| warning | `Alpha Proxima Core.md` | Missing required frontmatter field: related_documents |
| warning | `Alpha Proxima Core.md` | Missing required frontmatter field: related_research_programs |
| warning | `LUMIAION.md` | Missing required frontmatter field: artifact_type |
| warning | `LUMIAION.md` | Missing required frontmatter field: dependencies |
| warning | `LUMIAION.md` | Missing required frontmatter field: institutional_owner |
| warning | `LUMIAION.md` | Missing required frontmatter field: related_documents |
| warning | `LUMIAION.md` | Missing required frontmatter field: related_research_programs |
| warning | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Missing required frontmatter field: aliases |
| warning | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Missing required frontmatter field: artifact_type |
| warning | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Missing required frontmatter field: authors |
| warning | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Missing required frontmatter field: created |
| warning | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Missing required frontmatter field: dependencies |
| warning | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Missing required frontmatter field: institutional_owner |
| warning | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Missing required frontmatter field: related_documents |
| warning | `OSG_BUSINESS/OSG_ACADEMY/README.md` | Missing required frontmatter field: related_research_programs |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Missing required frontmatter field: artifact_type |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Missing required frontmatter field: dependencies |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Missing required frontmatter field: institutional_owner |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Missing required frontmatter field: related_documents |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Missing required frontmatter field: related_research_programs |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Missing required frontmatter field: aliases |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Missing required frontmatter field: artifact_type |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Missing required frontmatter field: authors |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Missing required frontmatter field: created |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Missing required frontmatter field: dependencies |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Missing required frontmatter field: institutional_owner |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Missing required frontmatter field: related_documents |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Missing required frontmatter field: related_research_programs |
| warning | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Production/Module 0 - Orientation/Module 0 — Orientation — Production Package.md` | Missing required frontmatter field: title |
| warning | `OSG_LAUNCH/00_REPOSITORY/GitHub Best Practices.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/00_REPOSITORY/GitHub Best Practices.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/00_REPOSITORY/OSG Academy Engineering Review.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/00_REPOSITORY/OSG Academy Engineering Review.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/00_REPOSITORY/README.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/00_REPOSITORY/README.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/00_REPOSITORY/Repository Structure.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/00_REPOSITORY/Repository Structure.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/01_NOTION_WORKSPACE/Notion Workspace Architecture.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/01_NOTION_WORKSPACE/Notion Workspace Architecture.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/01_NOTION_WORKSPACE/README.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/01_NOTION_WORKSPACE/README.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/02_COURSES/Course Folder Hierarchy.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/02_COURSES/Course Folder Hierarchy.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/02_COURSES/README.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/02_COURSES/README.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/03_MEDIA/README.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/03_MEDIA/README.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/04_CLIENTS/Client Folder Hierarchy.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/04_CLIENTS/Client Folder Hierarchy.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/04_CLIENTS/README.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/04_CLIENTS/README.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/05_CONTENT/Content Workflow.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/05_CONTENT/Content Workflow.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/05_CONTENT/README.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/05_CONTENT/README.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/06_AUTOMATION/Automation Opportunities.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/06_AUTOMATION/Automation Opportunities.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/06_AUTOMATION/README.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/06_AUTOMATION/README.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/07_OPERATIONS/Launch Operations Model.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/07_OPERATIONS/Launch Operations Model.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/07_OPERATIONS/README.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/07_OPERATIONS/README.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/08_ROADMAP/30 Day Implementation Roadmap.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/08_ROADMAP/30 Day Implementation Roadmap.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/08_ROADMAP/README.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/08_ROADMAP/README.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/09_TEMPLATES/Automation Spec Template.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/09_TEMPLATES/Automation Spec Template.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/09_TEMPLATES/Client Template.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/09_TEMPLATES/Client Template.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/09_TEMPLATES/Content Item Template.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/09_TEMPLATES/Content Item Template.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/09_TEMPLATES/Course Template.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/09_TEMPLATES/Course Template.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/09_TEMPLATES/Naming Conventions.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/09_TEMPLATES/Naming Conventions.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/09_TEMPLATES/README.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/09_TEMPLATES/README.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/10_ACADEMY/AIG/Awaken the Inner Guru Recording Start Guide.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/10_ACADEMY/AIG/README.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/10_ACADEMY/README.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/10_ACADEMY/README.md` | Missing required frontmatter field: authors |
| warning | `OSG_LAUNCH/README.md` | Missing required frontmatter field: aliases |
| warning | `OSG_LAUNCH/README.md` | Missing required frontmatter field: authors |
| warning | `PROJECT_GENOME/Genome Constitution v1.0.md` | Missing required frontmatter field: artifact_type |
| warning | `PROJECT_GENOME/Genome Constitution v1.0.md` | Missing required frontmatter field: dependencies |
| warning | `PROJECT_GENOME/Genome Constitution v1.0.md` | Missing required frontmatter field: institutional_owner |
| warning | `PROJECT_GENOME/Genome Constitution v1.0.md` | Missing required frontmatter field: related_documents |
| warning | `PROJECT_GENOME/Genome Constitution v1.0.md` | Missing required frontmatter field: related_research_programs |
| warning | `PROJECT_GENOME/Project Genome Master Index.md` | Missing required frontmatter field: artifact_type |
| warning | `PROJECT_GENOME/Project Genome Master Index.md` | Missing required frontmatter field: dependencies |
| warning | `PROJECT_GENOME/Project Genome Master Index.md` | Missing required frontmatter field: institutional_owner |
| warning | `PROJECT_GENOME/Project Genome Master Index.md` | Missing required frontmatter field: related_documents |
| warning | `PROJECT_GENOME/Project Genome Master Index.md` | Missing required frontmatter field: related_research_programs |

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
| error | `OSG_BUSINESS/OSG_ACADEMY/Awaken the Inner Guru — Production Blueprint.md` | Markdown note does not start with YAML frontmatter. |
| error | `OSG_BUSINESS/OSG_ACADEMY/OSG Learning Standard (OLS) v1.0.md` | Markdown note does not start with YAML frontmatter. |
| error | `Omi/Memories.md` | Markdown note does not start with YAML frontmatter. |
| error | `Sans titre 1.md` | Markdown note does not start with YAML frontmatter. |
| error | `Sans titre.md` | Markdown note does not start with YAML frontmatter. |
| error | `Vault.md` | Markdown note does not start with YAML frontmatter. |
| error | `docs/constitution/LUMIAION_CONSTITUTION.md` | Markdown note does not start with YAML frontmatter. |
| error | `docs/constitution/README.md` | Markdown note does not start with YAML frontmatter. |
| error | `docs/setup/Claude-Code-in-Obsidian.md` | Markdown note does not start with YAML frontmatter. |

## Implementation Notes

This report is diagnostic. It does not approve, reject, move, or modify institutional documents.

## Future Improvements

- [ ] Add baseline support for legacy validation debt.
- [ ] Add JSON output for downstream automation.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-09-03 | [[CODEX]] | Validation report generated |
