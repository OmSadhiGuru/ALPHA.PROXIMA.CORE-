---
title: "Tool 014 - Council Session Kernel"
aliases: ["Council Kernel", "council_kernel", "Engineering Toolkit Tool 014", "ap council"]
tags: [systems, engineering, toolkit, council, governance, state, alpha-proxima]
created: 2026-09-04
updated: 2026-09-04
status: draft
version: "0.1.0"
authors: ["Founder", "CODEX (CF-07)"]
artifact_type: implementation-note
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Engineering Intelligence"
reasoning_engine: "CODEX"
dependencies: ["Python 3 standard library", "[[Tool 008 - Engineering CLI]]", "[[Minimum Viable Council Procedure]]", "[[Agent and Subagent Registry]]"]
related_documents: ["[[Council Node Architecture]]", "[[Founder Intent Routing Procedure]]", "[[Interim Authority Instrument]]"]
related_research_programs: []
---

# Tool 014 - Council Session Kernel

## Purpose

Make the Minimum Viable Council procedure executable as a local, auditable session record. The kernel owns one JSON state document and can render a single decision packet for Founder review.

It is a **control plane**, not an autonomous multi-agent runtime: it does not call model providers, confer authority, appoint people or engines, or claim that a Council has voted.

## CLI

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" council <command> [options]
```

| Command | Effect |
|---|---|
| `init` | Create the empty Council state document. |
| `open` | Preserve Founder intent, class, authority basis, accountable role, and Ethics trigger. |
| `assign` | Create one bounded agent, subagent, or challenger deliverable. |
| `output` | Attach a concise, durable output summary to that assignment. |
| `synthesize` | Record recommendation and dissent; move the session to Founder review. |
| `decide` | Record an explicit Founder decision and, where permitted, execution owner. |
| `render` | Print or write the self-contained Founder decision packet. |
| `dashboard` / `serve [--port]` | Render or serve the read-only local Council Console and JSON read model. |
| `list` / `check` | Show sessions or validate the canonical state. |

## Gates

- Only the Founder may record an interim decision.
- Class I and II proposals require `ratify`; `approve` is intentionally rejected.
- AGT-010 is advisory-only; AGT-011, AGT-015, and AGT-016 are rejected as blocked pending appointment.
- An `formal-review-required` Ethics trigger blocks work; the kernel never substitutes an Ethics Council finding.
- Each session has exactly one accountable available Agent Role. Assignments carry one bounded deliverable and cannot move a blocked session forward.

## State and outputs

The default state path is `13_OPERATIONS/AI Council/state/council-state.json`. It is created only by `council init`; no sample or live session is committed by this tool. Decision packets are explicitly rendered to stdout or a user-selected path.

`serve` binds only to `127.0.0.1` (default port `8788`) and exposes `/`, `/api/view`, and `/api/state`. It is intentionally read-only; session changes still go through explicit Kernel commands.

## Verification

```bash
python3 -m unittest discover -s "08_SYSTEMS/Engineering Toolkit" -p "test_council_kernel.py"
python3 -m compileall -q "08_SYSTEMS/Engineering Toolkit"
```

## Status boundary

This proposed implementation is stacked on the activation packet in PR #28. It becomes operational only when its exact reviewed commit is explicitly approved and merged after that prerequisite. Until then it is a testable draft implementation, not a live Council system.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 0.1.0 | 2026-09-04 | Founder + CODEX (CF-07) | First runnable local session kernel with role, authority, and Ethics gates. |
