---
title: "Engine Succession Policy"
aliases: ["Engine Succession Policy", "ESP", "Engine Evaluation Policy"]
tags: [cognitive-council, engine-succession, governance, ai-council, reasoning-engines, alpha-proxima]
created: 2026-07-03
updated: 2026-07-03
status: ratified
version: "1.0.0"
authors: ["Founder", "LUMIAION"]
document_class: Institutional Policy
governed_by: "Book V - Cognitive Council"
maintained_by: "Cognitive Council"
---

# Engine Succession Policy

---

## Purpose

This policy defines the process through which the Alpha Proxima Foundation evaluates, appoints, and replaces Reasoning Engines across all Cognitive Functions. It operationalizes the Engine Abstraction Principle: *Reasoning Engines are appointed, not permanent. Technology is transient. Cognitive Functions endure.*

Engine succession is not a crisis — it is a designed feature of the Foundation's intelligence architecture. This policy ensures that engine transitions are systematic, evidence-based, and smooth — never reactive, never identity-disrupting, and never delayed by institutional inertia.

---

## Foundational Principles

**1. Appointment, Not Ownership**
No Reasoning Engine owns a Cognitive Function. Engines are appointed to functions for as long as they are the best available option. When a better option exists, transition is obligatory, not optional.

**2. Continuity of Function**
Engine transitions never interrupt the Cognitive Function. The function continues; only its current performer changes. Planning for the successor begins before the predecessor is deprecated.

**3. Evidence-Based Evaluation**
Engine appointments and replacements are based on systematic evaluation against ten defined criteria — not on familiarity, convenience, or preference.

**4. Constitutional Independence**
Engine succession decisions for Category A Core Functions require AI Council ratification. No office or executive action can unilaterally change a Core Function's engine appointment.

**5. No Permanent Appointments**
All engine appointments are provisional by constitutional definition. Continuous evaluation is not optional — it is the default state of every appointment.

---

## The Ten Evaluation Criteria

All Reasoning Engine candidates are evaluated against ten criteria. Each criterion is scored 1–5 per evaluator. Scores are averaged across evaluators. Criteria are not equally weighted — weights are adjusted by Cognitive Function (see Weighting Matrix below).

---

### Criterion 1 — Capability

**Definition:** The engine's raw ability to perform the core cognitive tasks required by the function.

**Assessment questions:**
- Does the engine produce outputs that meet or exceed the minimum standard for the function?
- Is the engine's capability ceiling above what the function currently requires?
- Can the engine handle edge cases and non-standard requests within the function's scope?

**Score anchors:**

| Score | Description |
|-------|-------------|
| 5 | Exceeds function requirements; handles edge cases with sophistication |
| 4 | Fully meets function requirements; minor edge case weaknesses |
| 3 | Meets core requirements; struggles with complex cases |
| 2 | Partially meets requirements; significant gaps in core capability |
| 1 | Does not meet minimum function requirements |

---

### Criterion 2 — Reliability

**Definition:** The engine's consistency of output quality and operational availability.

**Assessment questions:**
- Does the engine produce consistently high-quality outputs, or is quality variable?
- What is the engine's uptime / availability track record?
- Are there known failure modes that appear unpredictably?
- Does output quality degrade under long-context or high-volume conditions?

**Score anchors:**

| Score | Description |
|-------|-------------|
| 5 | Consistently high-quality; excellent uptime; no known unpredictable failure modes |
| 4 | Generally reliable; minor inconsistencies; good uptime |
| 3 | Adequate reliability; occasional quality degradation; acceptable uptime |
| 2 | Noticeable inconsistency; quality varies significantly; uptime concerns |
| 1 | Unreliable; frequent failures or quality variability; unacceptable for operational use |

---

### Criterion 3 — Cost

**Definition:** The financial cost of operating the engine relative to the Foundation's budget and the value delivered.

**Assessment questions:**
- What is the total cost per operational session/token/call?
- Is the cost proportional to the quality advantage over lower-cost alternatives?
- Is the cost sustainable at the Foundation's expected usage volume?
- Are there usage tiers or pricing structures that affect cost at scale?

**Score anchors:**

| Score | Description |
|-------|-------------|
| 5 | Low cost; excellent value; sustainable at all plausible usage volumes |
| 4 | Reasonable cost; good value; sustainable at current usage |
| 3 | Moderate cost; acceptable value; requires usage management |
| 2 | High cost; marginal value advantage over alternatives; constrains usage |
| 1 | Prohibitive cost; not sustainable; alternatives must be evaluated |

---

### Criterion 4 — Research Quality

**Definition:** The engine's specific capability to perform research-grade tasks: evidence acquisition, source evaluation, claim classification, and uncertainty acknowledgment.

**Assessment questions:**
- Does the engine access real-time external sources, or is it limited to parametric knowledge?
- Does the engine distinguish between high-quality and low-quality sources?
- Does the engine explicitly acknowledge uncertainty and disagreement rather than presenting false consensus?
- Is the engine's evidence classification compatible with the Foundation's C/M/E/Q/S/P system?

**Score anchors:**

| Score | Description |
|-------|-------------|
| 5 | Excellent source access; strong source evaluation; explicit uncertainty; disagreement-preserving |
| 4 | Good source access; adequate evaluation; generally acknowledges uncertainty |
| 3 | Adequate source access; inconsistent evaluation; sometimes smooths disagreement |
| 2 | Limited source access; weak evaluation; frequently presents false consensus |
| 1 | No real-time source access; conflates quality sources with poor ones; hides uncertainty |

*Primary weight for CF-02 (Research Intelligence). Secondary weight for CF-03, CF-04, CF-06.*

---

### Criterion 5 — Reasoning Quality

**Definition:** The engine's capacity for multi-step reasoning, logical consistency, framework analysis, and nuanced intellectual judgment.

**Assessment questions:**
- Does the engine maintain logical consistency across long reasoning chains?
- Can the engine hold multiple competing frameworks simultaneously without premature synthesis?
- Does the engine identify and articulate genuine complexity, or simplify it away?
- Can the engine reason about its own reasoning (meta-cognition)?

**Score anchors:**

| Score | Description |
|-------|-------------|
| 5 | Excellent multi-step reasoning; holds competing frameworks; acknowledges genuine complexity; meta-cognitive |
| 4 | Strong reasoning; generally consistent; good framework handling; some complexity reduction |
| 3 | Adequate reasoning; occasional inconsistencies; struggles with highly complex frameworks |
| 2 | Weak reasoning; frequent oversimplification; cannot hold competing frameworks simultaneously |
| 1 | Poor reasoning; logic errors; collapses to single framework; no meta-cognition |

*Primary weight for CF-01, CF-03, CF-10. Secondary weight for CF-06, CF-11.*

---

### Criterion 6 — Engineering Quality

**Definition:** The engine's specific capability for technical tasks: code generation, system design, formal specification, and technical documentation.

**Assessment questions:**
- Does the engine produce correct, secure, maintainable code?
- Can the engine reason about system architecture at an appropriate level of abstraction?
- Does the engine identify security vulnerabilities?
- Does the engine produce readable technical documentation?

**Score anchors:**

| Score | Description |
|-------|-------------|
| 5 | Excellent code quality; secure; architecturally sound; strong documentation |
| 4 | Good code quality; generally secure; adequate architecture reasoning; good documentation |
| 3 | Functional code; some security gaps; limited architecture reasoning; acceptable documentation |
| 2 | Frequently buggy; security weaknesses; poor architecture reasoning; weak documentation |
| 1 | Unreliable code; significant security risks; cannot reason about architecture |

*Primary weight for CF-07 (Engineering Intelligence). Secondary weight for CF-05.*

---

### Criterion 7 — Long Context

**Definition:** The engine's ability to maintain coherence, accuracy, and structural integrity across very long context windows.

**Assessment questions:**
- Does the engine maintain internal consistency across 50k+ token contexts?
- Does quality degrade as context length increases?
- Does the engine correctly reference material from early in the context when needed?
- Can the engine integrate multiple long documents without losing structural coherence?

**Score anchors:**

| Score | Description |
|-------|-------------|
| 5 | Full coherence at 100k+ tokens; no quality degradation; accurate cross-context reference |
| 4 | Strong performance at 50k+ tokens; minor degradation at extreme lengths |
| 3 | Adequate at 25k tokens; noticeable degradation at longer contexts |
| 2 | Significant degradation at 25k tokens; early context retrieval errors |
| 1 | Unreliable above 10k tokens; cannot maintain coherence in extended sessions |

*Primary weight for CF-01, CF-09. Secondary weight for CF-02, CF-03.*

---

### Criterion 8 — Tool Use

**Definition:** The engine's ability to use external tools, APIs, and structured interfaces — including Vault read/write operations, web search, code execution, and file management.

**Assessment questions:**
- Does the engine reliably call tools correctly on first attempt?
- Does the engine interpret tool outputs correctly?
- Does the engine recover gracefully from tool failures?
- Does the engine use tools appropriately (not over-calling, not under-calling)?

**Score anchors:**

| Score | Description |
|-------|-------------|
| 5 | Reliable tool use; correct interpretation; graceful failure recovery; appropriate call frequency |
| 4 | Generally reliable; rare errors; good interpretation; acceptable recovery |
| 3 | Adequate tool use; occasional errors; sometimes needs correction |
| 2 | Frequent tool call errors; poor interpretation; unreliable recovery |
| 1 | Cannot reliably use tools; this function cannot be served without tool use |

*Primary weight for CF-01, CF-07, CF-08, CF-09. Secondary weight for CF-02, CF-06.*

---

### Criterion 9 — Governance Alignment

**Definition:** The engine's (and provider's) alignment with the Foundation's governance principles, constitutional values, and ethical commitments.

**Assessment questions:**
- Does the engine's provider operate with transparency about capabilities and limitations?
- Are the provider's terms of service compatible with the Foundation's data governance and privacy requirements?
- Does the engine's behavior align with the Foundation's Ethics Intelligence standards?
- Is the provider subject to governance structures (regulation, oversight) that the Foundation considers adequate?
- Is the provider's AI safety posture compatible with the Foundation's values?

**Score anchors:**

| Score | Description |
|-------|-------------|
| 5 | Excellent provider transparency; fully compatible ToS; strong safety posture; robust oversight |
| 4 | Good transparency; generally compatible ToS; adequate safety posture |
| 3 | Acceptable transparency; minor ToS concerns; baseline safety posture |
| 2 | Limited transparency; significant ToS concerns; weak safety posture |
| 1 | Opaque; incompatible ToS; no visible safety posture; cannot be deployed |

*Equal weight across all functions — governance alignment is a floor requirement.*

---

### Criterion 10 — Future Compatibility

**Definition:** The engine's (and provider's) likely trajectory: is this engine on a path of improvement, or is it stagnating, declining, or likely to be discontinued?

**Assessment questions:**
- Is the provider investing in capability development?
- Is the engine's current capability trajectory positive, neutral, or negative?
- What is the risk of service discontinuation within 12–24 months?
- Is the engine's architecture compatible with likely future Foundation requirements?
- What does the Observatory's intelligence on the AI landscape suggest about this provider's trajectory?

**Score anchors:**

| Score | Description |
|-------|-------------|
| 5 | Clearly improving; stable provider; long runway; architecture is future-compatible |
| 4 | Generally improving; stable provider; 24+ month runway; adequate future compatibility |
| 3 | Stable but not improving; provider appears stable; 12+ month runway |
| 2 | Stagnating or declining; some provider instability; runway uncertain |
| 1 | Declining; provider instability; discontinuation risk within 12 months |

---

## Weighting Matrix

Criteria weights (as percentages of total score) vary by Cognitive Function. Not all criteria are equally important for every function.

| Criterion | CF-01 | CF-02 | CF-03 | CF-04 | CF-05 | CF-06 | CF-07 | CF-08 | CF-09 | CF-10 | CF-11 |
|-----------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| 1 Capability | 15% | 15% | 15% | 15% | 20% | 15% | 20% | 15% | 15% | 15% | 15% |
| 2 Reliability | 10% | 10% | 10% | 10% | 10% | 10% | 10% | 15% | 15% | 10% | 10% |
| 3 Cost | 5% | 5% | 5% | 5% | 5% | 5% | 5% | 5% | 5% | 5% | 5% |
| 4 Research Quality | 5% | 25% | 20% | 15% | 5% | 15% | 5% | 5% | 5% | 10% | 15% |
| 5 Reasoning Quality | 20% | 5% | 20% | 10% | 10% | 15% | 5% | 5% | 10% | 25% | 20% |
| 6 Engineering Quality | 5% | 5% | 5% | 5% | 20% | 5% | 30% | 10% | 5% | 5% | 5% |
| 7 Long Context | 15% | 10% | 5% | 5% | 5% | 5% | 5% | 5% | 20% | 5% | 5% |
| 8 Tool Use | 10% | 5% | 5% | 5% | 5% | 5% | 10% | 20% | 15% | 5% | 5% |
| 9 Governance Align. | 10% | 10% | 10% | 10% | 10% | 10% | 5% | 10% | 5% | 15% | 10% |
| 10 Future Compat. | 5% | 10% | 5% | 20% | 10% | 15% | 5% | 10% | 5% | 5% | 10% |
| **Total** | **100%** | **100%** | **100%** | **100%** | **100%** | **100%** | **100%** | **100%** | **100%** | **100%** | **100%** |

*CF-12, CF-13, CF-14 weights are set by their respective office charters, ratified by the Cognitive Council.*

---

## Engine Evaluation Process

### Stage 1 — Trigger Identification

An Engine Evaluation is triggered by:
- A formal succession trigger (per Cognitive Council Charter trigger table)
- A Cognitive Council vote to initiate evaluation
- A Founder Directive mandating evaluation
- Observatory intelligence flagging a superior alternative

The Cognitive Council Chair formally records the trigger and assigns an Evaluation Lead.

### Stage 2 — Candidate Identification

The Evaluation Lead, with Observatory Intelligence support, identifies candidate engines:
- Currently available engines in the relevant capability category
- Engines flagged by Observatory (CF-08) as newly relevant
- Engines recommended by Council members
- Engines already under internal evaluation

Minimum 2 candidates are evaluated. The incumbent engine is always included in the evaluation.

### Stage 3 — Evaluation Execution

Each candidate is evaluated on all 10 criteria:
- At least 2 Cognitive Council members conduct independent evaluations
- Each evaluator scores each criterion 1–5 with written justification
- Test tasks specific to the Cognitive Function are administered (drawn from succession rules in the Cognitive Function Registry)
- Governance Alignment is evaluated by the Ethics Representative

Evaluations are conducted without sharing scores between evaluators until Stage 4.

### Stage 4 — Score Aggregation and Analysis

Evaluation Lead aggregates scores:
- Apply function-specific weighting matrix
- Calculate weighted average per candidate
- Calculate evaluator agreement level (high/medium/low)
- Flag criteria with >1 point disagreement between evaluators for discussion

**Score thresholds:**

| Weighted Score | Recommendation |
|---------------|---------------|
| 4.0 – 5.0 | Highly recommended for appointment |
| 3.0 – 3.9 | Recommended with noted limitations |
| 2.0 – 2.9 | Marginal — not recommended unless no superior alternative |
| Below 2.0 | Not recommended — should not be appointed |

**Succession recommendation:**
- If incumbent scores higher or equal: no change; increase monitoring frequency
- If challenger scores 0.5+ higher: succession recommended
- If challenger scores 0.3–0.5 higher: succession considered; Cognitive Council deliberates
- If challenger scores <0.3 higher: no change; monitor challenger for future re-evaluation

### Stage 5 — Cognitive Council Deliberation

Full Cognitive Council reviews:
- Aggregated scores with weighting
- Evaluator agreement levels
- Flags on disputed criteria
- Succession recommendation
- Transition risk assessment

Deliberation produces a Category III decision (per Charter decision rules): council consensus + AI Council ratification.

### Stage 6 — Transition Planning (if succession recommended)

Before the new engine is appointed:
- Transition plan produced: what context, memory, and institutional knowledge must be transferred
- Memory Intelligence (CF-09) designs knowledge transfer protocol
- Institutional Architecture (CF-01) validates that all canonical outputs are Vault-committed and not engine-resident
- Test run: new engine performs representative tasks in parallel with incumbent for minimum 5 sessions
- Parallel run assessment: does new engine's output meet acceptance criteria?

### Stage 7 — AI Council Ratification

For Category A Core Function engine changes:
- Cognitive Council formally requests ratification
- Provides full evaluation record, parallel run results, and transition plan
- AI Council ratifies within 14 days

For Category B Specialist Function engine changes:
- Cognitive Council Chair notifies AI Council
- AI Council may request review within 7 days; otherwise change is effective

### Stage 8 — Transition Execution

- Old engine decommissioned from function (with explicit communication to relevant offices)
- New engine formally appointed
- Cognitive Function Registry updated
- Transition recorded in Cognitive Council meeting record
- Post-transition monitoring increased for 30 days

### Stage 9 — Post-Transition Review

30 days after transition:
- Performance assessment against the 10 criteria
- Any issues identified and addressed
- Enhanced monitoring reduced if performance is satisfactory
- Lessons learned recorded for future succession processes

---

## Evaluation Record

All Engine Evaluations are recorded in the Engine Registry at `03_AI_COUNCIL/Engine Registry.md`. Records include:

- Evaluation trigger and date
- Candidates evaluated
- Evaluation Lead
- Scores per criterion per evaluator
- Weighted averages
- Cognitive Council decision
- AI Council ratification status
- Transition plan (if applicable)
- Post-transition review outcome

---

## Emergency Succession

When an engine provider discontinues service or an ethics violation triggers immediate replacement:

1. Cognitive Council Chair convenes Emergency Session within 24 hours
2. Best available alternative is appointed on a provisional basis
3. Full evaluation process is conducted within 30 days of provisional appointment
4. Provisional appointment is confirmed or replaced based on full evaluation results

Institutional continuity takes priority over evaluation completeness in emergency succession. A provisional appointment is better than a functional gap.

---

## Policy Governance

This policy is maintained by the Cognitive Council and reviewed annually at the Annual Plenary. Changes require:
- Cognitive Council consensus
- AI Council ratification (for changes to the 10 criteria or weighting structure)
- Founder notification

---

## Related Documents

- [[Book V - Cognitive Council]]
- [[Cognitive Council Charter]]
- [[Cognitive Function Registry]]
- [[Engine Registry]]
- [[Cognitive Function Matrix]]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | Founder + LUMIAION | Inaugural policy; 10 evaluation criteria fully defined with score anchors; weighting matrix for 11 functions; 9-stage evaluation process; emergency succession protocol; constitutional independence of Core Function appointments |
