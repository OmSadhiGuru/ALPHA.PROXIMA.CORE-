---
title: "Node Taxonomy"
aliases: ["Institutional Knowledge Graph Node Taxonomy", "KG Node Types"]
tags: [systems, engineering, knowledge-graph, taxonomy, nodes, alpha-proxima]
created: 2026-07-03
updated: 2026-07-03
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-standard
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Knowledge Graph Architecture v1.0]]"]
related_documents: ["[[Relationship Taxonomy]]", "[[Knowledge Graph Conventions]]"]
related_research_programs: []
---

# Node Taxonomy

## Purpose

Define the approved node types for the Institutional Knowledge Graph v1.0.

## Node Type Rules

- Node types use lowercase snake_case in machine-readable form.
- Human labels may use title case.
- Every node type must have an owner, lifecycle, and minimum properties.
- New node types require Engineering Office schema update and architectural review if they imply new institutional categories.

## Core Node Types

| Node Type | Human Label | Purpose | Typical Source |
|-----------|-------------|---------|----------------|
| `research_program` | Research Program | Durable research program identity | RP master index |
| `research_commission` | Research Commission | Commissioned research request | Commission document |
| `research_artifact` | Research Artifact | Delivered source or research output | Archive/source note |
| `canonical_synthesis` | Canonical Synthesis | Reviewed institutional synthesis | Synthesis document |
| `evidence_claim` | Evidence Claim | Claim with evidence classification | Evidence registry |
| `open_question` | Open Question | Unresolved research or institutional question | Open questions note |
| `future_research` | Future Research | Research opportunity not yet commissioned | Future research note |
| `concept` | Concept | Reusable knowledge concept | Concept note |
| `theory` | Theory | Structured explanatory framework | Research graph or synthesis |
| `person` | Person | Human contributor or subject | People profile |
| `organization` | Organization | External or internal organization | Registry/source note |
| `publication` | Publication | Paper, book, report, or source publication | Source registry |
| `standard` | Standard | Engineering or institutional standard | Engineering standards |
| `office` | Office | Institutional office or operating unit | Office registry |
| `cognitive_function` | Cognitive Function | Institutional reasoning function | AI Council/operations registry |
| `engineering_tool` | Engineering Tool | Reusable implementation capability | Engineering Toolkit |
| `policy` | Policy | Binding or operational policy | Governance/protocol docs |
| `charter` | Charter | Authority-defining office/council artifact | Charter docs |
| `standing_order` | Standing Order | Durable operational instruction | Operations procedures |
| `founder_directive` | Founder Directive | Founder-originated directive | Directive/proposal record |

## Minimum Properties by Node Type

| Node Type | Required Additional Properties |
|-----------|--------------------------------|
| `research_program` | `research_program_id`, `phase`, `review_status` |
| `research_commission` | `commission_id`, `origin`, `assigned_to`, `due_date` |
| `research_artifact` | `artifact_id`, `format`, `contributor`, `received_date` |
| `canonical_synthesis` | `research_program_id`, `canon_status`, `review_authority` |
| `evidence_claim` | `claim_id`, `evidence_class`, `source_artifact`, `review_status` |
| `open_question` | `question_id`, `priority`, `origin`, `next_action` |
| `future_research` | `future_id`, `priority`, `dependencies`, `review_date` |
| `concept` | `concept_id`, `domain`, `definition_status` |
| `theory` | `theory_id`, `domain`, `evidence_status` |
| `person` | `person_id`, `role`, `affiliation` |
| `organization` | `organization_id`, `organization_type` |
| `publication` | `publication_id`, `citation`, `source_quality` |
| `standard` | `standard_id`, `domain`, `compliance_status` |
| `office` | `office_id`, `authority`, `review_cycle` |
| `cognitive_function` | `function_id`, `preferred_engine`, `responsibilities` |
| `engineering_tool` | `tool_id`, `cli_command`, `owner` |
| `policy` | `policy_id`, `authority`, `effective_date` |
| `charter` | `charter_id`, `office`, `authority_scope` |
| `standing_order` | `order_id`, `owner`, `review_cycle` |
| `founder_directive` | `directive_id`, `origin_date`, `status` |

## Implementation Notes

This taxonomy maps current vault artifacts to graph-ready node identities. It intentionally starts with broad institutional types before adding domain-specific subtypes.

## Future Improvements

- [ ] Add machine-readable node schema JSON.
- [ ] Add examples from each current vault folder.
- [ ] Add subtype hierarchy after node registry exists.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | [[CODEX]] | Initial Institutional Knowledge Graph node taxonomy |
