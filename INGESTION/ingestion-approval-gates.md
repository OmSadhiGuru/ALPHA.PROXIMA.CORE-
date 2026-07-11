---
title: Ingestion Approval Gates
id: apx-ingestion-approval-gates
department: LUMIAION
domain: ingestion
type: ingestion-standard
status: active
version: 1.0.0
created: 2026-07-10
updated: 2026-07-10
source: founder-request
tags: [ingestion, approval, ethics, gates]
related: [../GOVERNANCE/approval-policy.md, ../OPERATIONS/CPOS/APPROVAL_GATES.md, evidence-classification-standard.md, founder-synthesis-standard.md]
owner: "Ethics & Evidence Council (not yet seated) / LUMIAION"
---

# Ingestion Approval Gates

## Purpose

Specialize `../GOVERNANCE/approval-policy.md` for the ingestion lifecycle specifically, and define exactly where the pipeline stops for review rather than proceeding automatically.

## Gate Table

| Gate | Lifecycle Stage | Approval Required | Trigger |
|---|---|---|---|
| G1 | Source Record | None | Matches approval-policy.md's "index updates" / "non-destructive file organization." |
| G2 | Extraction | None | Matches "research summaries." |
| G3 | Classification | **Ethics & Evidence Council** — conditional | Any entry classified **Clinical** (`evidence-classification-standard.md`). Non-Clinical classification requires no gate. |
| G4 | Founder Synthesis | **Founder review** — recommended, not blocking | This is the first stage where interpretation is added; the Founder should see it before it hardens into an OSG Knowledge Object, but may delegate initial review. |
| G5 | Conversion to OSG Knowledge Object | **Founder approval** — required only if the object is marked `[!public-content-candidate]` (`../DESIGN/callout-standard.md`) | Internal-only knowledge objects may proceed without this gate; anything flagged as a public candidate stops here. |
| G6 | Publication (OSGMETAPHYSICS) | **Ethics & Evidence Council + Founder** — both required | Matches approval-policy.md's "external publication." No health, wellness, educational, or complementary-practice content passes this gate without Council review, per the Council's constitutional purpose. |

## Rule

A gate that requires approval halts the pipeline at that stage — the item does not proceed to the next stage, and does not get marked with the next `AUTOMATIONS/drive-sync-spec.md` processing status, until the required approval is recorded.

## Recording Approvals

Until `OPERATIONS/CPOS/APPROVAL_GATES.md`'s generic Open Approval Gates table is confirmed as the shared mechanism for this purpose (unresolved — see `INGESTION/README.md`), record ingestion-specific approvals directly in the relevant Founder Synthesis or Knowledge Object document's frontmatter (`approval_status` field, per `../DESIGN/document-layout-standard.md`) as the interim mechanism.

## Standing Gap

The Ethics & Evidence Council named at G3 and G6 is established in principle (constitutional package, pending source — not filed in this repository) but has no seated members and no defined review procedure yet. Until it is seated, any item reaching G3 or G6 stops and waits — it does not default to Founder-only approval as a substitute, since the Council's review is a distinct check the Founder's own approval does not satisfy.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-10 | Claude (Repository Architect / Knowledge Pipeline Designer) | Initial Ingestion Approval Gates, Sprint 3. Standing gap on the unseated Ethics & Evidence Council recorded explicitly rather than routed around. |
