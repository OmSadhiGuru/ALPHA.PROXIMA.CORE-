---
title: "Validation Debt Policy"
aliases: ["Vault Validation Baseline", "Validation Debt"]
tags: [systems, engineering, validation, debt, alpha-proxima]
created: 2026-09-05
updated: 2026-09-17
status: active
version: "1.1.0"
authors: ["Founder", "CODEX (CF-07)"]
artifact_type: engineering-policy
institutional_owner: "Engineering Office"
cognitive_function: "Engineering Intelligence"
reasoning_engine: "CODEX"
dependencies: ["[[Tool 001 - Vault Validator]]"]
related_documents: ["[[Engineering Office Charter]]"]
related_research_programs: []
---

# Validation Debt Policy

The Vault Validator reports all issues. A reviewed baseline records inherited debt so CI fails only on regressions. The baseline is evidence, not an exclusion list: reports always show total debt and new issues separately.

Use `--write-baseline` only after review. Use `--baseline ... --fail-on error` for operational CI. Remove signatures from the baseline only when the underlying document is repaired; never add a new defect merely to make CI pass.


## Post-PR-45 review — PR #46

Measured on main `a02b025b6a5d5cf84ef4c4ee48b36532ceb8d6f4` before edits:
151 Toolkit tests and 11 Truth Kernel tests passed; 18 inherited errors, zero new
errors, 990 total warnings (7 new), 38 total informational findings (1 new).
Coherence was 128 (22 orphans, 17 missing frontmatter, 85 broken links, 4 empty notes), ceiling 129.
The PR #45 baseline was reproduced without discrepancy. The validator scans 385
notes; the app indexes 384 because the app explicitly excludes the imported `Omi/Memories.md`; the validator
retains that export in its scan.

### Every inherited error classified

All 18 are `missing_yaml`, not broken links or parser false positives.
A = mechanical repair; B = instrument defect; C = governance decision required;
D = explicitly authorized retained debt. This review found **A: 2, B: 0, C: 16,
D: 0**. Baseline membership permits reporting without failing CI; it does not
supply missing institutional authority and is not itself a D classification.

| Document path | Class | Evidence and disposition |
|---|---|---|
| `Awaken the Inner Guru Production Folder.md` | C | Empty placeholder. Founder must decide purpose, ownership and retain/archive disposition; do not invent a document. |
| `OSG_BUSINESS/00 OSG Business Foundation — Overview.md` | C | Explicit working assumptions and launch package; approved owner/status and admission into institutional metadata are not established. Founder/OSG must decide. |
| `OSG_BUSINESS/01 Flagship Course.md` | C | Working title and proposed course; Founder/OSG must confirm ownership and approval state. |
| `OSG_BUSINESS/02 Coaching Offers.md` | C | Recommended offers/prices do not establish approved ownership/status. Founder/OSG decision required. |
| `OSG_BUSINESS/03 Website Copy.md` | C | Publication-ready wording and placeholders are not publication approval. Founder/OSG must confirm owner/status. |
| `OSG_BUSINESS/04 Client Journey & Onboarding.md` | C | Proposed operating journey; accountable owner and approval status require Founder/OSG confirmation. |
| `OSG_BUSINESS/05 Email Sequences.md` | C | Copy templates with personalization placeholders; author/owner and adoption status are unproven. Founder/OSG decision required. |
| `OSG_BUSINESS/06 Community Onboarding.md` | C | Recommended community structure, not an appointment or adoption record. Founder/OSG must confirm owner/status. |
| `OSG_BUSINESS/07 30-Day Launch Checklist.md` | C | Unchecked decisions and launch tasks; do not infer approval. Founder/OSG must confirm owner/status. |
| `OSG_BUSINESS/OSG_ACADEMY/Awaken the Inner Guru — Production Blueprint.md` | A | Added metadata from its explicit owner, Gate-1-pending status, version and dated author history. `draft` preserves pending approval; no approval granted. Body unchanged. |
| `OSG_BUSINESS/OSG_ACADEMY/OSG Learning Standard (OLS) v1.0.md` | A | Transcribed the document's own ratified status, owner, version and dated author history. No new ratification or constitutional wording. Body unchanged. |
| `Omi/Memories.md` | C | Imported personal-memory export, not an institutional record. Founder must decide retention, classification and ownership. |
| `Sans titre 1.md` | C | Empty placeholder; Founder disposition and purpose required. |
| `Sans titre.md` | C | Empty placeholder; Founder disposition and purpose required. |
| `Vault.md` | C | Empty placeholder; Founder disposition and purpose required. |
| `docs/constitution/LUMIAION_CONSTITUTION.md` | C | Historical charter has a Book-I subordination notice; metadata ownership and historical/current authority require governance review together with its README. No constitutional rewrite. |
| `docs/constitution/README.md` | C | Still describes the charter as supreme, unlike the charter's hierarchy notice. Governance must approve the reconciled summary and metadata. |
| `docs/setup/Claude-Code-in-Obsidian.md` | C | Technical setup prose supplies no accountable institutional owner/status. Founder/Engineering must decide adoption and maintenance responsibility. |

Only the two repaired `missing_yaml` signatures were removed from the baseline.
No signatures were added, no baseline was regenerated, no rules were weakened.
Empty optional relationship lists assert no new governance relationship. OSG creation
dates/authors/versions come from the existing 2026-07-04 version histories; the update
date records this metadata edit. The OLS relationship is already explicit in the blueprint.

### All eight new findings investigated

All concern `13_OPERATIONS/AI Council/spatial/Galaxy Prototype Concept.md`.

| Finding | Classification | Repair |
|---|---|---|
| Missing `aliases` | Legitimate documentation debt | Empty aliases list; no invented synonym. |
| Missing `dependencies` | Legitimate documentation debt | Link to the existing Agent and Subagent Registry consumed by the prototype. |
| Missing `related_documents` | Legitimate documentation debt | Link to the existing Council Kernel implementation note. |
| Missing `related_research_programs` | Legitimate documentation debt | Empty list; no research affiliation invented. |
| Missing `tags` | Legitimate documentation debt | Descriptive systems/council/prototype tags. |
| Missing `updated` | Legitimate documentation debt | Date of this edit. |
| Missing `version` | Legitimate documentation debt | Initial metadata version 0.1.0; draft status preserved. |
| No incoming link | Legitimate documentation debt | Council Kernel note links to the concept while explaining read-only boundaries. |

These are integration documentation omissions, not false positives or grounds for
suppressions. Governance-dependent roster identity conflicts are separate from these
eight findings; see [[Tool 014 - Council Session Kernel]].

### Remaining boundary and next review

The Agent/Subagent Registry remains canonical for Council roles. Founder OS has a
historical operational roster with colliding AGT IDs. No automatic cross-store join,
renaming, appointment or migration is authorized by this cleanup. PR #47 should first
obtain a Founder-approved identity crosswalk, including preservation of historical
run references, and dispositions for the 16 C items above. It should separately bound
state-write atomicity/concurrency work: existing Founder and Council writers remain
non-atomic, and this PR does not claim simultaneous-writer safety. Any interface work
must consume the established read models and retain the prototype boundary. This is
a recommended scope for review, not authorization to start PR #47.


### Truth Kernel measurement consequence

The OSG metadata repairs make existing attribution machine-readable. The Truth
Kernel consequently exposes six unresolved relationships: on each of the two OSG
notes, `OWNED_BY: Chief Learning Architect, OSG Academy` and `PRODUCED_BY: Chief
Learning Architect` have no unique canonical node, while `PRODUCED_BY: LUMIAION`
is ambiguous. Four prior missing-owner/frontmatter warnings disappear. Thus total
Truth Kernel findings move from 1499 to 1501 (net +2 warnings); error count is
unchanged. This is newly measured pre-existing identity debt, not new appointments.
Do not create agents/nodes or guess which LUMIAION to select to hide it. Founder/OSG
must confirm the canonical identity mapping as part of the PR #47 review.

Final vault validation: 16 inherited errors, 983 warnings, 36 informational findings;
zero new findings of any severity. Coherence: 123 (19 orphans, 15 missing frontmatter,
85 broken links, 4 empty notes), ratcheted from ceiling 129 to 123 under ES-12.
