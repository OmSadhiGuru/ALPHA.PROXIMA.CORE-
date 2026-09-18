---
title: "PR47 Identity and State Safety Review"
aliases: []
tags: [proposal, engineering, identity, state, alpha-proxima]
created: 2026-09-17
updated: 2026-09-17
status: draft
version: "0.1.0"
authors: ["CODEX"]
artifact_type: proposal
institutional_owner: "Alpha Proxima Foundation"
dependencies: ["[[Agent and Subagent Registry]]", "[[Validation Debt Policy]]"]
related_documents: ["[[Tool 012 - Founder OS State Engine]]", "[[Tool 014 - Council Session Kernel]]", "[[12 - Continuous Integration Standard]]"]
related_research_programs: []
---

# PR47 Identity and State Safety Review

## Review status and provenance

**Proposal only. No identity mapping, appointment, migration or debt disposition is approved.**
Prepared from PR #46 commit `4c1669e6214689f02fbc89a400f5b6a03aaa50f0`.
At inspection PR #46 is still open/draft and main is PR #45's
`a02b025b6a5d5cf84ef4c4ee48b36532ceb8d6f4`. This follow-up is stacked on PR #46;
it must not claim to start from merged PR #46. Merge review remains the Founder's act.

Sources: `13_OPERATIONS/Founder OS/state/founder-state.json` and the
[[Agent and Subagent Registry]]. Council availability below is copied from that
registry, not inferred from Founder operational status or engine names.

## Identity evidence and proposed correspondence

Founder has 12 roster entries; Council has 16 roles. All twelve Founder IDs also
exist in Council, but shared string IDs do not prove shared identity. Only AGT-001
has an evident same-name/same-function counterpart, still not a ratified cross-store
mapping. “Candidate” below means a review suggestion, never an executable mapping.

| Founder ID and identity | Council meaning of the same ID | Candidate for Founder review | Evidence / boundary |
|---|---|---|---|
| AGT-001 LUMIAION | LUMIAION Orchestrator | AGT-001 | Name, orchestration function and owner align; preserve source provenance. |
| AGT-002 CLAUDE / Chief Knowledge Architect | Research Lead | Unresolved | An engine identity and an architecture function do not identify a unique Council role. |
| AGT-003 CODEX / Engineering | Comparative Lead | AGT-007 CODEX Engineering Lead | Name/office align; mapping is not approval to rewrite historical IDs. |
| AGT-004 PERPLEXITY / Research | Education Lead | AGT-002 Research Lead | Registry explicitly lists Perplexity and Research Intelligence Office. |
| AGT-005 COMET / Observatory | Computational Specialist | AGT-008 Observatory Lead | Registry explicitly lists Comet and Institutional Observatory. |
| AGT-006 JERANIUM / manual semantic routing | Executive Briefing Lead | Unresolved | AGT-015 carries JERANIUM's name but is blocked/owner pending; AGT-009 shares some memory functions but a different role. Do not choose by name or function alone. |
| AGT-007 ATHENA | CODEX Engineering Lead | AGT-012 ATHENA Domain Lead | Domain/name alignment; “available” does not mean a connected native integration. |
| AGT-008 SOHMA | Observatory Lead | AGT-014 SOHMA Domain Lead | Domain/name alignment; no new authority conferred. |
| AGT-009 VORTEX | Memory Steward | AGT-013 VORTEX Domain Lead | Domain/name alignment; no financial execution authority conferred. |
| AGT-010 ARTEMIS, proposed | Ethics Sentinel | None established | Proposed historical entry must not become an Ethics appointment. |
| AGT-011 POSTMANIUM, proposed | Strategic Intelligence Lead | None established | Both strings existing does not establish identity or authority. |
| AGT-012 SECRETARY-GENERAL, proposed | ATHENA Domain Lead | None established | Charter/privacy boundaries remain undefined; do not turn this into ATHENA. |

Council roles with no candidate above remain canonical Council roles; absence from
Founder state is not a reason to create another operational roster entry. Current
AGT-010 remains advisory-only, AGT-011/015/016 remain blocked, and owner-pending
roles receive no invented department.

## Historical run contract

The inspected Founder state contains one run: `RUN-001`, `agent_id: AGT-006`,
`task_id: TSK-007`, `handoff_id: FIR-001`, `result_id: RES-003`, route
`LUMIAION -> JERANIUM`, worker `vault_validator.validate`.

A global AGT-006 replacement would either misattribute it to Executive Briefing Lead
or imply that today's blocked JERANIUM Council role executed it. Neither follows
from the evidence. Proposed preservation contract:

1. Keep the original run and its original roster reference unchanged.
2. A future reference must carry a source namespace and revision before any join.
   Illustrative labels `founder-legacy` and `council-registry` are proposed namespaces,
   not new agents or committed state schema in this change.
3. If approved, store the crosswalk in one governance-owned document and derive
   read models from it; do not create a second independently maintained state map.
4. Missing or unapproved mappings stay unresolved and cannot authorize execution.
5. Any future migration requires a dry-run reference inventory, reversible snapshot,
   semantic before/after validation and explicit Founder approval of the exact diff.

## Sixteen debt decisions prepared

The individual paths and source evidence remain in [[Validation Debt Policy]];
this groups the decisions without changing their C classification or baseline.

| Items | Count | Proposed disposition for review | Decision still required |
|---|---:|---|---|
| Empty production-folder note, Sans titre, Sans titre 1, Vault | 4 | Retain untouched until purpose is confirmed; then explicitly choose fill or archive | Founder must choose per file; no automatic deletion or invented metadata |
| OSG launch package 00–07 | 8 | Keep as unapproved business working material | Confirm actual author/owner, lifecycle and adoption; “ready to publish” is not approval |
| Omi/Memories export | 1 | Preserve personal provenance and keep out of new identity joins | Founder decides retention and institutional classification; do not copy personal details into proposals |
| LUMIAION constitutional charter and README | 2 | Review together against the existing hierarchy notice | Approve authoritative summary and metadata ownership without a fresh constitutional claim |
| Claude-Code-in-Obsidian setup guide | 1 | Propose Engineering maintenance review | Confirm owner, adoption status and ongoing maintenance responsibility |

Two OSG documents already repaired in PR #46 expose additional Truth Kernel identity
questions: which canonical entity, if any, represents Chief Learning Architect / OSG
Academy, and which LUMIAION is intended as author. Preserve the literal attributions
until resolved; do not fabricate nodes to remove warnings.

## First technical lane implemented: atomic publication

The existing Founder and Council writers now serialize and validate before publishing
one complete JSON snapshot. A temporary sibling file is written, flushed and fsynced,
then atomically replaces the canonical file. Existing file permissions are retained;
new files are private (0600). A symlinked state path continues to update its target.
Pre-replacement failures leave the old file intact and remove temporary scratch files.
The helper is not a new state owner, store, execution path or migration.

**Limits:** this protects against partial-file visibility, not concurrent lost updates.
The containing directory is not fsynced, so power-loss durability of the rename is not
promised. Existing per-file ownership/ACLs beyond permission bits and hard-link identity
are not a preservation guarantee of replacement. Current canonical inputs are ordinary
Git-tracked JSON files. No production mutation was performed to test this lane.

## Next technical lane, specified but not implemented

Protect the entire load/validate/mutate/save transaction, not just the save call.
Use a stable sibling lock (not the replaced inode), a bounded lock wait and a content
revision check. This lock is synchronization metadata, never canonical institutional
state. Read-only views need no write lock because replacement is atomic.

Council `run` has saves before and after an external process. Do not hold a global lock
across an LLM call: reserve an assignment under lock, release it during work, then reload
and verify the reservation/revision before committing the result under lock. A stale
completion must be rejected visibly, never overwrite a Founder decision. `init` must
also atomically refuse an existing state. These semantics need a separately reviewed
implementation, not an assertion that atomic replacement already solves concurrency.

Acceptance tests for that next lane: two process writers retain both valid changes;
a stale revision is rejected; lock timeout changes no state; crash before replacement
leaves valid old JSON; crash after replacement leaves valid new JSON; failed external
work does not erase concurrent decisions; recovery never silently rolls back governance.
No test should invoke a live provider.

## Concrete Founder review choices

Recommended next approval: **approve source-scoped references and preservation of
historical runs, while keeping every candidate mapping and debt disposition unapproved**.
This would authorize a narrowly scoped reference contract, not a roster migration.

Alternative: review and approve selected candidate mappings individually before changing
any reference contract. In either case, CLAUDE, JERANIUM and all proposed Founder seats
remain unresolved until explicitly decided. No decision has been written into Founder
or Council state by this work.


## Verification of this first increment

168 Toolkit tests and 11 Truth Kernel tests pass. Vault validation remains 16 inherited
errors, 983 warnings and 36 informational findings, with zero new findings. Coherence
remains 123 against ceiling 123. Founder/Council/Registry bytes match PR #46. All
existing App, Founder, Council, Office, Galaxy and Truth Kernel render/check paths pass.
Six new tests cover atomic visibility, failure before replacement, serialization
failure, symlink preservation, permissions and integration with both state owners.

The new proposal adds three visible Truth Kernel warnings: CODEX author resolution is
ambiguous, Alpha Proxima Foundation ownership lacks a resolved node, and this draft
uses a provisional title-based node identity. Totals are 1504 findings (1484 warnings,
20 errors), versus PR #46's 1501 (1481 warnings, 20 errors). These are disclosed graph
limitations of this draft; no durable institutional ID or replacement entity is invented.
