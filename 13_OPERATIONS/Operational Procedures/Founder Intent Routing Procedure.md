---
title: "Founder Intent Routing Procedure"
aliases: ["Unified Founder Routing", "One-Inbox Routing", "FIR-001"]
tags: [operations, procedures, orchestration, routing, founder, lumiaion, alpha-proxima]
created: 2026-08-28
updated: 2026-09-03
status: active
version: "1.0.0"
authors: ["Founder", "LUMIAION", "CODEX"]
artifact_type: operational-procedure
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Orchestration"
reasoning_engine: "LUMIAION"
dependencies: ["[[The Orchestration Framework]]", "[[Decision Routing Protocol]]", "[[Knowledge Routing Protocol]]", "[[LUMIAION Charter]]"]
related_documents: ["[[Workflow Registry]]", "[[Operational Procedures Index]]", "[[Founder Reboot Control Center]]"]
related_research_programs: []
---

# Founder Intent Routing Procedure

## Purpose

Give the Founder one reliable intake surface. The Founder states an intent once; Alpha Proxima classifies it, loads relevant memory, assigns accountable execution, and returns one review-ready result.

This procedure removes manual department selection from the Founder's workload. A request received in the wrong project, department, tool, or session remains valid intake.

## Scope

FIR-001 governs operational intake and handoff. It does not change departmental authority, ratify agents, bypass approval gates, or permit one department to act outside its charter.

## Governing Rule

> The Founder communicates with one institution, not a collection of disconnected agents.

No receiving context may reject a valid Founder intent merely because another department owns execution. The receiving context must preserve the request, identify the domain owner, and create a complete handoff packet.

## Accountabilities

| Role | Accountability |
|---|---|
| Founder | States intent, supplies unavailable constraints, and approves gated outcomes |
| LUMIAION | Owns classification, priority, routing, conflict resolution, synthesis, and escalation |
| JERANIUM | Retrieves relevant institutional memory, structures context, checks duplication, and supports writeback |
| Domain department | Owns specialist execution within its ratified charter |
| CODEX or engineering delegate | Implements technical artifacts when the route requires engineering |

LUMIAION is the routing authority. JERANIUM strengthens the route with memory and knowledge infrastructure; it does not replace LUMIAION's orchestration authority.

## Intake Contract

The Founder may use natural language. The receiving context converts it into this minimum packet:

```yaml
handoff_id: FIR-YYYYMMDD-NNN
received_at: YYYY-MM-DDTHH:MM:SSZ
founder_intent: "Outcome requested in the Founder's language"
success_condition: "Observable completion condition"
primary_owner: "Ratified department or office"
supporting_roles: []
priority: critical | high | normal | low
decision_class: I | II | III | IV
context_sources: []
constraints: []
deliverables: []
approval_gate: none | founder_review | governance_review
writeback_destination: "Canonical Vault destination or session-only"
state: captured | routed | executing | review | approved | completed | blocked
next_action: "One executable action"
```

Unknown information is recorded as `unknown`; it is not invented. Clarification is requested only when the missing information materially changes safety, authority, cost, or the deliverable.

## Procedure

1. **Capture** — Preserve the Founder's original language and desired outcome.
2. **Classify** — LUMIAION identifies domain ownership, decision class, urgency, risk, and approval needs.
3. **Load** — JERANIUM retrieves the smallest sufficient context package from canonical memory.
4. **Route** — LUMIAION assigns one primary owner and names supporting roles only when necessary.
5. **Execute** — The primary owner produces the deliverable within charter boundaries.
6. **Synthesize** — LUMIAION reconciles contributions and returns one coherent result.
7. **Approve** — The Founder reviews only when the declared gate requires it.
8. **Write back** — JERANIUM routes durable knowledge to its canonical home and records the next action.

## Routing Rules

- Every request has exactly one primary owner.
- Cross-domain requests may have supporting roles, but never competing owners.
- A department receiving an out-of-domain request must hand it off; it must not silently absorb the work.
- The Founder is not asked to restate information already present in the packet or canonical memory.
- The system returns one result, one status, and one next action.
- Public publication, financial execution, medical decisions, constitutional changes, and destructive actions retain their existing approval requirements.
- A blocked route states the missing dependency and preserves the packet for resumption.

## State Model

| State | Meaning | Required exit condition |
|---|---|---|
| captured | Intent preserved | Primary domain classified |
| routed | Owner and context assigned | Owner accepts execution |
| executing | Work is active | Deliverable produced or blocker found |
| review | Result awaits an explicit gate | Approval or requested revision |
| approved | Gated result accepted | Writeback completed |
| completed | Deliverable and writeback finished | None |
| blocked | Required dependency unavailable | Dependency restored or Founder decision |

## Example — Workout Request Received in VORTEX

```yaml
handoff_id: FIR-20260828-001
founder_intent: "Generate tomorrow's workout and schedule my flexible weekly sessions"
success_condition: "Tomorrow's session and a rolling 6-workouts-on-8-days cycle are ready"
primary_owner: ATHENA
supporting_roles: [LUMIAION, JERANIUM]
priority: high
decision_class: IV
context_sources:
  - "ATHENA Charter"
  - "Founder's prior training cycle and performance goals"
constraints:
  - "Flexible schedule"
  - "Preserve shoulder mobility"
  - "Retain workout history instead of restarting"
deliverables:
  - "Next workout"
  - "Rolling eight-day schedule"
  - "Progression and completion record"
approval_gate: founder_review
writeback_destination: "ATHENA operational record"
state: routed
next_action: "ATHENA generates the first calendar-ready session"
```

VORTEX does not design the workout. It recognizes valid institutional intake, preserves the packet, and allows LUMIAION to route execution to ATHENA.

## Completion Standard

A routed request is complete only when:

- the requested deliverable exists;
- the Founder can understand its status without reading internal handoffs;
- any required approval is explicit;
- durable context has a declared writeback destination; and
- one next action is visible, or the work is closed.

## Implemented V1 Route

FIR-001 now has one executable route: repository health. The state engine
captures the Founder intent and success condition, records LUMIAION's routing
decision, assigns JERANIUM, runs the report-only Vault Validator, persists the
task/run/result/handoff chain, and regenerates Founder Console. The route stops
at `review`; it does not approve its own output.

```bash
AP='python3 "08_SYSTEMS/Engineering Toolkit/ap.py" founder'
$AP repository-health "Assess current repository health" \
  --success-condition "A persisted report is ready for Founder review" \
  --why "Founder needs current evidence before choosing a repair" \
  --vault . \
  --report "13_OPERATIONS/Operational Health/FIR-001 Repository Health Result.md"
```

This is intentionally not a general dispatcher. New domains and delivery
channels remain unimplemented until this route is reviewed and preserved.

## Failure Recovery

If a tool, engine, project, or session cannot reach the assigned owner:

1. preserve the handoff packet;
2. complete any safe, in-scope portion locally;
3. mark the exact unavailable dependency;
4. provide a resumable next action; and
5. never report a handoff as completed unless execution actually occurred.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-09-03 | Founder / LUMIAION / CODEX | Activated the first executable, persisted repository-health route |
| 0.1.0 | 2026-08-28 | Founder / LUMIAION / CODEX | Initial unified Founder-intent routing procedure submitted for review |
