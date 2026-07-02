---
title: "Research Debt Register"
aliases: ["Research Debt Register", "RDR", "Documentation Debt Registry"]
tags: [governance, research, debt, registry, permanent, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["LUMIAION"]
registry_type: Research Debt
---

# Research Debt Register

---

## Purpose

The Research Debt Register is the permanent institutional record of all known documentation debts in the Alpha Proxima Foundation's research programs. It operationalizes the following institutional principle:

> **The Foundation distinguishes between architectural blockers and documentation debt. Only architectural blockers stop progress. Documentation debt is tracked, prioritized, and resolved through scheduled review.**

A research debt is not a failure. It is a visible, intentional deferral — the recognition that a specific documentation gap exists, that it is understood, that it is insufficient to block institutional progress, and that it will be resolved on a defined schedule.

An unregistered gap is more dangerous than a registered one. Registration transforms an invisible risk into a managed obligation.

---

## Institutional Principle

**Architectural Blocker vs. Documentation Debt:**

| Type | Definition | Effect on Progress |
|------|-----------|-------------------|
| Architectural Blocker | A gap that prevents correct institutional operation, introduces structural ambiguity, or makes downstream work unreliable | Must be resolved before progress continues |
| Documentation Debt | A known incompleteness that does not prevent correct institutional operation; current state is sufficient but not final | Tracked, prioritized, resolved through scheduled review — does not block progress |

---

## Active Register

### RD-001

| Field | Value |
|-------|-------|
| **Debt ID** | RD-001 |
| **Title** | Page-Level Citations Incomplete — RP-002 Evidence Registry |
| **Affected Program** | RP-002 Atlas of Human Memory |
| **Affected Document** | `07_RESEARCH/RP-002/12 Evidence Registry/RP-002 Evidence Registry.md` |
| **Priority** | Medium |
| **Status** | Open |
| **Created** | 2026-07-02 |
| **Target Review Date** | During Source Verification Pass (date TBD) |
| **Reclassified From** | GAP-003 (FGR-001 Epoch II Stewardship Audit) |

**Description:**
RP-002's Evidence Registry classifies 31 claims across six evidence categories but does not include source page citations for any claim. Claims reference the source document (DOC-A or DOC-B) but not the specific page from which the claim is drawn.

RP-001's Evidence Registry includes page citations in a `Page` column (e.g., "DOC-003 | p.3"). This level of traceability is the stated standard.

**Root Cause:**
DOC-A (French PDF, 12 pages) and DOC-B (English PDF, 14 pages) were reviewed via in-session PDF rendering in which page numbers were not consistently visible in the structured extraction output. Page citations were omitted rather than guessed.

**Impact:**
Low for institutional development. The claim content, evidence classification, and source attribution are all correct. A reader verifying a specific claim cannot immediately locate it in the source PDF without searching the full document.

High for long-term traceability. As the Foundation builds on RP-002 claims, the absence of page citations makes verification slower than it should be.

**Why Deferred:**
Current evidence traceability is sufficient for institutional development in Epoch II. Page-level verification requires physical document review with visible pagination. This should be combined with the pending DOC-C Founder review.

**Required Action:**
During the Source Verification Pass: (1) Re-review DOC-A and DOC-B with visible page numbers; (2) Add page citations to all 31 Evidence Registry entries; (3) Note page ranges for key DOC-C claims once DOC-C is reviewed; (4) Bump Evidence Registry to v1.1.0.

**Dependencies:**
- DOC-C Founder review (PDF: `fcf6d34f-RP002_Illustrated.pdf`)
- Source Verification Pass scheduling

---

## Closed Register

*No closed debts yet.*

---

## Research Debt Policy

### How a Debt Is Registered

1. A gap is identified (through audit, Founder review, or LUMIAION discovery)
2. It is assessed: architectural blocker or documentation debt?
3. If documentation debt: assign RD-ID, complete all fields, add to Active Register
4. Record the reclassification in the originating document (Gap Report, if applicable)

### How a Debt Is Resolved

1. The required action is completed
2. The affected document is updated and versioned
3. The debt entry is moved from Active → Closed with resolution date and summary
4. The registry version is bumped

### How a Debt Is Escalated

If circumstances change — if downstream work begins relying on the incomplete information in ways that introduce error — a documentation debt may be escalated to an architectural blocker. This requires a Founder decision and creates an immediate work stoppage on the affected program.

### Debt Priority Scale

| Priority | Definition |
|---------|-----------|
| High | Gap will affect downstream decisions if not resolved soon; review within 30 days |
| Medium | Gap is visible but not affecting current work; review within 90 days |
| Low | Cosmetic or minor; resolve during next scheduled review |

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | LUMIAION | Initial registry; RD-001 registered (reclassified from GAP-003); institutional principle established |
