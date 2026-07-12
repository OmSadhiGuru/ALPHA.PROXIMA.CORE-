---
title: Worker Handoff Template
id: apx-template-worker-handoff
department: LUMIAION
domain: templates
type: template
status: active
version: 1.0.0
created: 2026-07-11
updated: 2026-07-11
source: founder-request
tags: [template, handoff, ai-workers]
related: [../GOVERNANCE/ai-worker-jurisdiction.md, ../OPERATIONS/CPOS/HANDOFF_LOG.md]
owner: "Office of Operations (scope pending Founder ratification)"
---

# Worker Handoff Template

Standalone version of the handoff entry format already used inline in `../OPERATIONS/CPOS/HANDOFF_LOG.md` — same fields, usable outside CPOS for any AI-worker-to-AI-worker or AI-worker-to-Founder handoff (`../GOVERNANCE/ai-worker-jurisdiction.md`).

```yaml
---
title: "Handoff — "
id: apx-handoff-
department:
domain: operations
type: worker-handoff
status: draft
version: 0.1.0
created:
updated:
source: founder-request
tags: [worker-handoff]
related: []
owner:
---
```

# Handoff — Task / Date

| Field | Value |
|---|---|
| From (Worker) | |
| To (Worker or Office) | |
| Source Queue / Context | |
| Destination Queue / Context | |
| Git Reference | |
| Status | *(Done / Review / Blocked / Waiting Approval / Published — matches `../OPERATIONS/CPOS/HANDOFF_LOG.md`)* |
| What Entered | |
| What Left | |
| Quality Criteria Met | |
| Verification | |
| Dependencies Created | |
| Blockers Opened / Resolved | |
| Approval Gates Opened / Resolved | |
| Next Eligible Task | |

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 0.1.0 | | | |

## Template Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-11 | Claude (Constitutional Secretary / Institutional Architect) | Initial template, Phase II Sprint 2, extracted from CPOS's inline format for repository-wide reuse. |
