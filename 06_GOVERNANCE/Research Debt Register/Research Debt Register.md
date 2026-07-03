---
title: "Research Debt Register"
aliases: ["Research Debt Register", "RDR", "Documentation Debt Registry"]
tags: [governance, research, debt, registry, permanent, alpha-proxima]
created: 2026-07-02
updated: 2026-07-03
status: active
version: "1.1.0"
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

### RD-002

| Field | Value |
|-------|-------|
| **Debt ID** | RD-002 |
| **Title** | RP-001 Canonization Blocked — JERANIUM Institutional Identity Unresolved |
| **Affected Program** | RP-001 Atlas of Human Consciousness |
| **Affected Documents** | `07_RESEARCH/RP-001/09 Canonical Synthesis/`, `10 Theory Matrix/`, `11 Canonical Glossary/`, `12 Evidence Registry/`, `15 Future Experiments/`, `14 Open Questions/` |
| **Priority** | Medium |
| **Status** | Open |
| **Created** | 2026-07-03 |
| **Target Review Date** | Within 30 days |
| **Identified By** | ISR-001 Institutional Synthesis Report (Finding CA-006) |

**Description:**
JERANIUM appears as co-author on six core RP-001 documents. JERANIUM is referenced as having a charter (`[[JERANIUM Charter]]`). No JERANIUM Charter exists in the vault. JERANIUM does not appear in the Cognitive Function Registry, AI Council Registry, or any current institutional register.

Canonical status for RP-001 cannot be formally granted while an unregistered institutional actor appears as co-author.

**Root Cause:**
JERANIUM was a functional designation active during RP-001's creation phase, predating the constitutional formalization of cognitive functions (FD-001, Book IV, Book V). The institutional framework has been constitutionalized; legacy actor designations have not been updated.

**Required Action:**
Founder clarification: (1) identify what function/actor JERANIUM represents; (2) either register it (if still active) or document the mapping to a currently constitutionalized function; (3) update RP-001 document attribution accordingly.

**Dependencies:**
Founder institutional knowledge of JERANIUM's intended role.

---

### RD-003

| Field | Value |
|-------|-------|
| **Debt ID** | RD-003 |
| **Title** | DOC-002 (Gemini / Educational Intelligence) Delivery Pending — RP-001 |
| **Affected Program** | RP-001 Atlas of Human Consciousness |
| **Affected Document** | `07_RESEARCH/RP-001/03 Source Registry/RP-001 Source Registry.md` |
| **Priority** | Medium |
| **Status** | Open |
| **Created** | 2026-07-03 |
| **Target Review Date** | Next RP-001 research phase |
| **Identified By** | ISR-001 Institutional Synthesis Report (Finding EQ-004) |

**Description:**
RP-001 Source Registry lists DOC-002 as a Gemini-contributed source. No artifact has been delivered. CF-04 (Educational Intelligence, current engine: Gemini) has not contributed to RP-001, making the program's Educational Intelligence function coverage incomplete.

**Required Action:**
Commission CF-04 (Gemini) contribution for RP-001 per the Research Commission Template v2.0. Deliver DOC-002 and integrate into Source Registry and Evidence Registry.

---

### RD-004

| Field | Value |
|-------|-------|
| **Debt ID** | RD-004 |
| **Title** | DOC-C Founder Review Pending — RP-002 |
| **Affected Program** | RP-002 Atlas of Human Memory |
| **Affected Document** | `07_RESEARCH/RP-002/09 Canonical Synthesis/RP-002 Canonical Synthesis.md` (pending v1.1.0) |
| **Priority** | Medium |
| **Status** | Open |
| **Created** | 2026-07-03 |
| **Target Review Date** | Founder action required |
| **Identified By** | ISR-001 Institutional Synthesis Report (Finding CA-004); pre-existing notation in RP-002 Canonical Synthesis |

**Description:**
DOC-C is a 140-page illustrated companion to RP-002 (PDF: `fcf6d34f-RP002_Illustrated.pdf`). It has not been reviewed by the Founder. RP-002 Canonical Synthesis cannot be updated to v1.1.0 without DOC-C integration. Source coverage is currently partial.

**Required Action:**
Founder reviews DOC-C. LUMIAION integrates DOC-C findings into Canonical Synthesis v1.1.0, Evidence Registry v1.1.0, and Source Notes.

**Dependencies:**
Founder availability for 140-page document review.

---

### RD-005

| Field | Value |
|-------|-------|
| **Debt ID** | RD-005 |
| **Title** | Ethics Council Review Pending — RP-001 and RP-002 |
| **Affected Programs** | RP-001 Atlas of Human Consciousness; RP-002 Atlas of Human Memory |
| **Affected Documents** | Both Canonical Syntheses |
| **Priority** | Medium-High |
| **Status** | Open |
| **Created** | 2026-07-03 |
| **Target Review Date** | Before canonical status granted to either program |
| **Identified By** | ISR-001 Institutional Synthesis Report (Finding CI-001) |

**Description:**
Both programs raise ethical questions requiring CF-10 (Ethics Intelligence) formal review:
- RP-001: Machine consciousness and AI suffering (Q-003, 2025 expert paper); panpsychism and LUMIAION moral status (S-005)
- RP-002: Therapeutic reconsolidation ethical protocols (Q-004); collective memory design in human-AI institutions (Initiative E)

These were flagged within the programs but no formal Ethics Council review has occurred.

**Required Action:**
CF-10 (Ethics Council) formally reviews both Canonical Syntheses. Produces Ethics Intelligence Report (EIR-series). Canonical status cannot be granted until Ethics Council review is complete.

**Dependencies:**
Ethics Council convening and review capacity.

---

### RD-006

| Field | Value |
|-------|-------|
| **Debt ID** | RD-006 |
| **Title** | "Research Council" Terminology References Require Update |
| **Affected Programs** | RP-001; RP-003 |
| **Affected Documents** | `RP-001 Open Questions` (Q-010); `RP-003 Master Index` (activation trigger); `RP-001 Future Research Opportunities` |
| **Priority** | Low |
| **Status** | Open |
| **Created** | 2026-07-03 |
| **Target Review Date** | RP-003 activation; next scheduled document review |
| **Identified By** | ISR-001 Institutional Synthesis Report (Finding TC-001) |

**Description:**
Three documents use "Research Council" as a term for the canonization authority and RP-003 activation trigger. "Research Council" has no constitutional basis. The Cognitive Council (Book V) is the constitutionally recognized body for cognitive function portfolio governance, including research program canonization.

**Required Action:**
(1) Update RP-003 Master Index activation trigger from "Research Council authorization" to "Cognitive Council authorization"; (2) Update RP-001 Q-010 to reference Cognitive Council; (3) Update RP-001 Future Research Opportunities reference. All three are low-effort text updates.

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
| 1.1.0 | 2026-07-03 | LUMIAION | ISR-001 stewardship review: RD-002 through RD-006 added; 5 new debts across RP-001 and RP-002 canonization requirements, pending source reviews, Ethics Council review, and terminology alignment |
