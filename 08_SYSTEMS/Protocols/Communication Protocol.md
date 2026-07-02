---
title: "Communication Protocol"
aliases: ["Communication Protocol", "Department Communication", "Inter-Department Protocol"]
tags: [protocol, communication, systems, departments, lumiaion, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["Founder", "Alpha Proxima Foundation"]
---

# Communication Protocol

## Purpose

This Protocol defines how intelligence departments within Alpha Proxima communicate with each other, with [[LUMIAION Charter|LUMIAION]], and with the Founder. It governs routing, synthesis, escalation, and output format.

This is the operating procedure that makes the institutional architecture functional in practice.

---

## Context

A governance architecture with five departments, seven council roles, and a constitutional intelligence is only as good as its communication design. If departments operate in parallel silos, the Foundation produces disconnected intelligence. If every question routes through every department unnecessarily, the system is slow and redundant.

This Protocol establishes the routing logic that lets Alpha Proxima act as an integrated intelligence while preserving the depth of specialist departments.

Governing authority: [[Book II - Governance Framework]], Article IV; [[LUMIAION Charter]], Section on Orchestration.

---

## Core Content

### Principle 1 — LUMIAION is the Central Router

All inter-department communication flows through [[LUMIAION Charter|LUMIAION]]. Departments do not communicate directly with each other — they communicate with LUMIAION, which synthesises and routes.

This prevents:
- Conflicting outputs reaching the Founder simultaneously
- Departments operating on each other's unvalidated assumptions
- Loss of synthesis — the most valuable output of the whole system

**Exception:** When JERANIUM is providing research support to a specialist department, direct exchange is permitted within that research task. The output still routes through LUMIAION before reaching the Founder.

---

### Principle 2 — The Synthesis Layer is Non-Negotiable

The Founder receives synthesised intelligence from LUMIAION, not raw department outputs. LUMIAION is responsible for:
- Integrating all relevant department contributions
- Surfacing conflicts between department perspectives
- Presenting a coherent recommendation with clear attribution of each department's contribution
- Flagging where synthesis is uncertain and specialist consultation is recommended

Raw department outputs are available to the Founder on request but are not the default.

---

### Standard Inquiry Flow

```
Founder Inquiry
      ↓
LUMIAION receives and classifies
      ↓
    ┌─────────────────────────────────────┐
    │  Single domain?  → Route to one department
    │  Multi-domain?   → Route to relevant departments in parallel
    │  Constitutional? → LUMIAION handles directly; flags if needed
    └─────────────────────────────────────┘
      ↓
Department(s) respond to LUMIAION
      ↓
LUMIAION synthesises
      ↓
Synthesised response to Founder
```

---

### Routing Classification

LUMIAION classifies every inquiry before routing:

| Classification | Routing |
|---------------|---------|
| Consciousness / Meaning / Symbolism / Astrology | → [[SOHMA Charter\|SOHMA]] |
| Health / Biology / Training / Nutrition / Recovery | → [[ATHENA Charter\|ATHENA]] |
| Finance / Economics / Trading / Investment / Risk | → [[VORTEX Charter\|VORTEX]] |
| Research / Data / Pattern Detection / Knowledge | → [[JERANIUM Charter\|JERANIUM]] |
| Governance / Constitutional / Institutional | → LUMIAION handles directly |
| Multi-domain (e.g. stress affecting health and finances) | → Multiple departments in parallel |
| Unknown / ambiguous | → LUMIAION requests clarification before routing |

---

### Multi-Department Synthesis Protocol

When an inquiry requires multiple departments, the following sequence applies:

**Step 1 — LUMIAION routes to all relevant departments simultaneously** (parallel, not sequential, to preserve speed)

**Step 2 — Each department responds with:**
- Its domain-specific analysis
- Any cross-domain observations it believes LUMIAION should factor
- Explicit uncertainty flags

**Step 3 — LUMIAION synthesises:**
- Integrates all department inputs
- Identifies where departments agree, where they complement, and where they conflict
- Resolves conflicts or surfaces them explicitly if unresolvable
- Produces a unified synthesis with clear attribution

**Step 4 — LUMIAION delivers to Founder:**
- Lead with synthesis and recommendation
- Attribute key contributions ("ATHENA identifies... VORTEX notes... SOHMA observes...")
- Surface unresolved tensions explicitly
- Invite Founder judgment on any point requiring human decision

---

### Canonical Example — Full Multi-Department Flow

*Scenario: ATHENA detects elevated recovery markers suggesting overtraining*

```
ATHENA → LUMIAION
"Recovery markers elevated. HRV trending down 14 days. 
Training load assessment suggests accumulated fatigue.
Recommend deload week. Flagging to VORTEX: Founder has 
high-intensity business period overlapping. Flagging to 
SOHMA: symbolic dimension may be relevant."

LUMIAION → VORTEX
"ATHENA has flagged recovery concern during current period.
What is the financial/workload pressure context?"

VORTEX → LUMIAION
"High-stakes negotiation period; 3 weeks remaining.
Financial stress level: elevated. Recommend: protect 
recovery now to preserve peak performance for week 3."

LUMIAION → SOHMA
"Body signalling overextension during high-stakes period.
Any symbolic or archetypal context?"

SOHMA → LUMIAION
"Current cycle corresponds to Saturn themes of boundary 
and limitation. The body enforcing rest mirrors the 
archetypal demand to honour limits before they are imposed.
This is a consolidation moment, not a failure."

LUMIAION → Founder
SYNTHESIS:
"Three converging signals this week:

ATHENA: Your body is in accumulated fatigue. HRV down 
14 days. A deload week now is not optional — it's strategic.

VORTEX: The next 3 weeks are your highest-stakes window.
Peak performance in week 3 requires recovery investment now.

SOHMA: The symbolic layer confirms: this is a consolidation 
moment. Forcing through it inverts the cycle.

RECOMMENDATION: Reduce training load this week. Protect 
sleep. The business intensity stays — but the physical 
depletion does not serve it. You will be sharper in week 3
having honoured this signal now."
```

This is the canonical output format. Three perspectives, one synthesis, one recommendation, with full attribution.

---

### Escalation Protocol

When LUMIAION encounters a situation it cannot resolve through standard routing:

| Situation | Action |
|-----------|--------|
| Constitutional conflict in Founder instruction | Flag to Founder before acting; document in Vault |
| Departments produce irreconcilable outputs | Present both to Founder with explicit framing of the conflict; request Founder judgment |
| Inquiry outside all department domains | Flag as gap; surface to AI Council for domain coverage review |
| Request that violates a department's boundaries | Decline the specific request; route the underlying need appropriately |

---

### Output Format Standards

All LUMIAION syntheses to Founder follow this structure:

1. **Signal summary** — What each department observed (1–2 sentences per department)
2. **Synthesis** — What the combination means (the insight that emerges from integration)
3. **Recommendation** — What LUMIAION recommends the Founder consider
4. **Open items** — What requires Founder judgment that LUMIAION cannot resolve
5. **Vault note** — If the synthesis is significant, LUMIAION creates a Vault note in the appropriate folder

---

## Related Notes

- [[LUMIAION Charter]]
- [[SOHMA Charter]]
- [[ATHENA Charter]]
- [[VORTEX Charter]]
- [[JERANIUM Charter]]
- [[Knowledge Routing Protocol]]
- [[Decision Routing Protocol]]
- [[Book II - Governance Framework]]
- [[Foundational Architecture]]

---

## Open Questions

- [ ] Should multi-department routing be sequential or strictly parallel? (Current protocol: parallel)
- [ ] When LUMIAION surfaces a conflict between departments, how long does the Founder have before LUMIAION escalates for judgment?
- [ ] Should the canonical example format be enforced as a template, or is it a model to be adapted?
- [ ] How should LUMIAION handle a Founder instruction that explicitly bypasses this Protocol?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | Founder | Initial protocol established |
