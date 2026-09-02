---
title: "08_SYSTEMS Draft Triage Register"
aliases: ["Systems Draft Triage", "08_SYSTEMS Triage Register"]
tags: [proposal, planning, engineering, triage, 08-systems, alpha-proxima, preparation]
created: 2026-07-18
updated: 2026-07-18
status: draft
version: "0.1.0"
authors: ["Claude Code — Vault Architect"]
artifact_type: triage-register
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Alpha Proxima Engineering Toolkit]]"]
related_documents: ["[[PHASE III INSTITUTIONAL READINESS MAP]]", "[[CN-0001 COUNCIL CLOSURE IMPLEMENTATION PLAN]]"]
related_research_programs: []
---

# 08_SYSTEMS Draft Triage Register

> **Classification-only.** No document status is changed by this register. Recommendations are proposals for the (future) Engineering Council + Codex to execute. Vocabulary: RATIFY · REVISE · MERGE · SUPERSEDE · ARCHIVE · DELETE · HOLD.

## Method & Evidence

Query: `grep -rl "^status: draft" 08_SYSTEMS/` → **32 documents** (2026-07-18). Dates via filesystem `stat`. No document was rewritten. Where a filename encodes a date or version, supersession is inferred from the newer sibling.

## Headline Finding

**The "32 drafts" number overstates unfinished work.** The overwhelming majority are **completed, dated, generated reports falsely left in `draft` status** (should be `active`/historical → ARCHIVE) plus **8 misplaced templates** that belong in `10_TEMPLATES`. Genuine in-progress design work is a small minority. *Do not read 32 drafts as 32 architectural gaps.*

Breakdown: 20 Engineering Toolkit reports · 3 Knowledge Graph registries · 8 Research Management templates (misplaced) · 1 delivery report.

---

## Triage Register (one row per draft)

Columns: **Rec** = recommendation · **Mat** = maturity (Complete/Partial/Stub) · **Arch** = architectural relevance to Phase III (H/M/L)

| # | Title | Subsystem | Purpose | Conflicts/Dupes | Updated | Mat | Arch | **Rec** | Next action | Owner | Risk if ignored |
|---|-------|-----------|---------|-----------------|---------|-----|------|--------|-------------|-------|-----------------|
| 1 | Constitutional Engineering Audit v1.0 | Eng Toolkit/Reports | Master audit | Supersedes older individual reports | 07-04 | Complete | **H** | **RATIFY** | Set active; make canonical audit | Eng Council | Loss of newest authoritative audit |
| 2 | …Audit - Dashboard | Eng Toolkit/Reports | Audit view | child of #1 | 07-04 | Complete | M | **HOLD** | Keep as #1 appendix | Eng Council | — |
| 3 | …Audit - Dependency Map | Eng Toolkit/Reports | Audit view | child of #1; dup of #16 | 07-04 | Complete | M | **MERGE** | Fold into #1 | Codex | Dup dependency data |
| 4 | …Audit - Office Integrity | Eng Toolkit/Reports | Audit view | supersedes #12 | 07-04 | Complete | M | **SUPERSEDE** | Replace #12 | Codex | Two office-integrity truths |
| 5 | …Audit - Research Integrity | Eng Toolkit/Reports | Audit view | supersedes #13 | 07-04 | Complete | M | **SUPERSEDE** | Replace #13 | Codex | Two research-integrity truths |
| 6 | …Audit - Vault Validation | Eng Toolkit/Reports | Audit view | supersedes #14,#15 | 07-04 | Complete | M | **SUPERSEDE** | Replace dated validations | Codex | Stale validation cited |
| 7 | …Audit - YAML Validation | Eng Toolkit/Reports | Audit view | supersedes #19,#20 | 07-04 | Complete | M | **SUPERSEDE** | Replace dated YAML reports | Codex | Stale YAML cited |
| 8 | ES-001 - Orphan Document Classification | Eng Toolkit/Reports | Orphan scan | — | 07-02 | Complete | **H** | **REVISE** | Re-run vs current vault; feeds Vault Health | Eng Council | Orphans persist into Phase III |
| 9 | ES-001 - SanaLab Root File Assessment | Eng Toolkit/Reports | One-off assessment | — | 07-02 | Complete | L | **ARCHIVE** | Historical record | Codex | Clutter |
| 10 | Engineering Dashboard Report | Eng Toolkit/Reports | Dashboard snapshot | dup of #2 | 07-02 | Complete | L | **ARCHIVE** | Superseded by #1 set | Codex | Dup dashboards |
| 11 | Engineering Health Report v1.1 | Eng Toolkit/Reports | Health snapshot | — | 07-02 | Complete | L | **ARCHIVE** | Historical | Codex | Stale health cited |
| 12 | Office Integrity Report | Eng Toolkit/Reports | Office scan | superseded by #4 | 07-02 | Complete | L | **ARCHIVE** | Historical | Codex | Two truths |
| 13 | Research Integrity Report | Eng Toolkit/Reports | Research scan | superseded by #5 | 07-02 | Complete | L | **ARCHIVE** | Historical | Codex | Two truths |
| 14 | Vault Validation Report - 2026-07-02 | Eng Toolkit/Reports | Validation | superseded by #15,#6 | 07-02 | Complete | L | **ARCHIVE** | Oldest of chain | Codex | Stale cited |
| 15 | Vault Validation Report - 2026-07-03 | Eng Toolkit/Reports | Validation | superseded by #6 | 07-03 | Complete | L | **ARCHIVE** | Historical | Codex | Stale cited |
| 16 | Vault Dependency Report | Eng Toolkit/Reports | Dependency scan | dup of #3 | 07-02 | Complete | M | **ARCHIVE** | Superseded by #1 set | Codex | Dup |
| 17 | Metadata Migration Plan v1.0 | Eng Toolkit/Reports | Migration plan | superseded by #18 | 07-02 | Complete | L | **SUPERSEDE** | Replaced by v1.1 | Codex | Executing old plan |
| 18 | Metadata Migration Report v1.1 | Eng Toolkit/Reports | Migration result | — | 07-02 | Complete | L | **ARCHIVE** | Historical record | Codex | — |
| 19 | YAML Validation Report - 2026-07-02 | Eng Toolkit/Reports | YAML scan | superseded by #20,#7 | 07-02 | Complete | L | **ARCHIVE** | Oldest | Codex | Stale cited |
| 20 | YAML Validation Report - 2026-07-03 | Eng Toolkit/Reports | YAML scan | superseded by #7 | 07-03 | Complete | L | **ARCHIVE** | Historical | Codex | Stale cited |
| 21 | Graph Readiness Assessment | Inst. Knowledge Graph | KG readiness | — | 07-03 | Partial | **H** | **REVISE** | Update; feeds Phase III KG | Eng Council | Phase III KG unvalidated |
| 22 | Node Registry Report | Inst. KG/Tools | Generated registry | regenerable | 07-03 | Complete | M | **HOLD** | Regenerate on demand | Codex | Stale counts |
| 23 | Relationship Registry Report | Inst. KG/Tools | Generated registry | regenerable | 07-03 | Complete | M | **HOLD** | Regenerate on demand | Codex | Stale counts |
| 24 | ES-004 - Research Mgmt Toolkit Delivery Report | Research Mgmt/Reports | Delivery record | — | 07-02 | Complete | L | **ARCHIVE** | Historical | Codex | Clutter |
| 25 | Canonical Synthesis Template | Research Mgmt/Templates | Template | **misplaced** (→10_TEMPLATES) | 07-02 | Complete | M | **RATIFY** | Ratify + relocate to `10_TEMPLATES` | Research Council | Templates unusable/lost |
| 26 | Evidence Registry Template | Research Mgmt/Templates | Template | misplaced | 07-02 | Complete | M | **RATIFY** | Ratify + relocate | Research Council | " |
| 27 | Future Research Template | Research Mgmt/Templates | Template | misplaced | 07-02 | Complete | M | **RATIFY** | Ratify + relocate | Research Council | " |
| 28 | Open Questions Template | Research Mgmt/Templates | Template | misplaced | 07-02 | Complete | M | **RATIFY** | Ratify + relocate | Research Council | " |
| 29 | Research Artifact Template | Research Mgmt/Templates | Template | misplaced | 07-02 | Complete | M | **RATIFY** | Ratify + relocate | Research Council | " |
| 30 | Research Commission Template | Research Mgmt/Templates | Template | misplaced | 07-02 | Complete | M | **RATIFY** | Ratify + relocate | Research Council | " |
| 31 | Research Program Template | Research Mgmt/Templates | Template | misplaced; used by RP-002..006 | 07-02 | Complete | **H** | **RATIFY** | Ratify + relocate (RP stubs depend on it) | Research Council | RP scaffolds unanchored |
| 32 | Research Timeline Template | Research Mgmt/Templates | Template | misplaced | 07-02 | Complete | M | **RATIFY** | Ratify + relocate | Research Council | " |

> "Referenced by" and exhaustive conflict pairs were sampled, not fully link-traced (would require opening all 32 + inbound-link scan). Flagged as **inference** where marked dup/supersede.

---

## Required Lists

### Top 10 Highest-Risk Drafts
1. #1 Constitutional Engineering Audit v1.0 — newest authoritative audit stuck in draft.
2. #31 Research Program Template — RP-002…006 stubs depend on an unratified template.
3. #21 Graph Readiness Assessment — Phase III KG work rests on it; only partial.
4. #8 ES-001 Orphan Classification — orphans block a clean Phase III base.
5. #4 / #12 Office Integrity — two conflicting "truths" active simultaneously.
6. #5 / #13 Research Integrity — same double-truth risk.
7. #6 / #14 / #15 Vault Validation chain — stale validation may be cited as current.
8. #7 / #19 / #20 YAML Validation chain — same.
9. #25–#32 Templates — misplaced in 08_SYSTEMS, invisible to `10_TEMPLATES` users.
10. #17 Metadata Migration Plan v1.0 — risk of executing a superseded plan.

### Top 10 Fastest Closures (low-risk, mechanical)
#9, #10, #11, #16, #18, #24 → **ARCHIVE** · #14, #19 → **ARCHIVE** (oldest of chain) · #22, #23 → **HOLD** (regenerable). All are complete, uncontested, and need only a status flip once Engineering Council/Codex sign off.

### Drafts relevant to AxiomNexus
**None directly.** No draft references Axiom Nexus/AXN. Closest infrastructure relevance: #21 Graph Readiness, #1 Audit (would inform any future AXN control-plane). *Inference.*

### Drafts relevant to LUMIAION
#21 Graph Readiness Assessment (KG is LUMIAION's substrate); #1/#3/#16 dependency + audit data (LUMIAION orchestration reads these). No charter-level LUMIAION drafts here.

### Drafts relevant to CNS-002
**None identifiable** — CNS-002 is undefined in-vault (see Readiness Map). Cannot map relevance until the Founder defines it. **Open question.**

### Documents that MUST NOT survive into Phase III (as active/draft)
- All superseded chain members left in `draft`: #12, #13, #14, #15, #16, #17, #19, #20 — they create competing "current" truths.
- Misplaced templates #25–#32 must be **relocated** (not deleted) before Phase III, or `10_TEMPLATES` remains falsely incomplete.

## DELETE recommendations
**Zero.** Nothing warrants deletion; dated reports are historical evidence (ARCHIVE), templates are assets (RATIFY+relocate). Consistent with "prefer reduction/consolidation over destruction, but preserve evidence."

## Codex Review Criteria
1. Confirm each SUPERSEDE pair by opening both docs (verify newer fully covers older).
2. Confirm the 8 templates are not inbound-linked from `08_SYSTEMS`-relative paths before relocating (avoid breaking links → coordinate with Vault Health Register).
3. No status flips until Engineering Council exists **or** Founder authorises interim Class III action.

## Version History
| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-07-18 | Claude Code — Vault Architect | Classified all 32 drafts; supersession chains + misplaced-template finding; zero deletions. |
