---
title: Change Control Workflow
id: apx-governance-change-control-workflow
department: LUMIAION
domain: governance
type: policy
status: active
version: 1.0.0
created: 2026-07-11
updated: 2026-07-11
source: founder-request
tags: [governance, change-control, workflow]
related: [approval-authority-matrix.md, ../OPERATIONS/loom-command-center-spec.md]
owner: LUMIAION
---

# Change Control Workflow

## Purpose

Define the one permanent path a major institutional change must follow, end to end, so no change reaches the canonical repository without passing every check that applies to it.

## The Workflow

```
Founder Intent
  → LUMIAION Strategic Framing
    → Claude Constitutional or Architectural Draft
      → Codex Technical Verification
        → Ethics & Evidence Review (where applicable — see approval-authority-matrix.md)
          → Founder Approval
            → Commit
              → Index Update
                → LOOM Executive Record
```

## Step Definitions

| Step | Input | Output | Actor |
|---|---|---|---|
| Founder Intent | Vision, priority, or problem statement | A framed request | Founder |
| LUMIAION Strategic Framing | Founder Intent | Scoped objective, routed to the right Office/AI Worker | LUMIAION |
| Claude Constitutional or Architectural Draft | Scoped objective | Draft document(s), marked `draft` | Claude Code |
| Codex Technical Verification | Draft document(s) | Pass/fail report — metadata, links, IDs, status vocabulary | Codex |
| Ethics & Evidence Review | Draft + verification report, where the content touches health/wellness/education/complementary-practice or publication | Review verdict (Standing Gap applies — `approval-authority-matrix.md`) | Ethics & Evidence Council |
| Founder Approval | Verified (and, where applicable, reviewed) draft | Ratification decision, recorded per `../OPERATIONS/canonical-approval-record.md` | Founder |
| Commit | Approved draft | Git commit | Codex or Claude, per repository convention |
| Index Update | Committed change | Updated `../INDEX/master-index.md` and related indexes | Codex or the owning Office |
| LOOM Executive Record | Completed change | Entry in the Founder Command Center (`../OPERATIONS/loom-command-center-spec.md`) | LUMIAION |

## Rule

**No major institutional change may bypass this workflow.** "Major" is any change in scope for `approval-authority-matrix.md`'s Founder-approval row (strategy, brand, architecture, cost, legal/privacy/safety, irreversible action) or anything gated to the Ethics & Evidence Council. Minor changes (documentation formatting, metadata correction, index update) may skip the Founder Approval and Ethics Review steps, consistent with `approval-policy.md`, but still pass through Codex verification and land in the LOOM record.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-11 | Claude (Constitutional Secretary / Institutional Architect) | Initial Change Control Workflow, Phase II Sprint 2. |
