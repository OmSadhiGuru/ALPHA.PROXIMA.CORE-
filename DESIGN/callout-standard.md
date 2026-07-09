---
title: Callout Standard
id: apx-design-callout-standard
department: LUMIAION
domain: design
type: design-standard
status: active
version: 1.0.0
created: 2026-07-08
updated: 2026-07-08
source: founder-request
tags: [design-system, callouts, obsidian]
related: [knowledge-design-system.md, color-system.md, obsidian-style-guide.md, document-layout-standard.md]
owner: Human Experience Lab (scope pending Founder ratification)
---

# Callout Standard

## Purpose

Define the fixed set of reusable callout types so every callout communicates function, not decoration (Design Principle 4). A reader who has never seen a document before should be able to infer a callout's purpose from its label alone.

## Format Rule

Callouts are written as Obsidian callout syntax (`> [!type] Title`) so they render natively in Obsidian, and degrade to a plain blockquote on GitHub — this satisfies the cross-platform constraint in `knowledge-design-system.md`. Platform-specific rendering notes live in `obsidian-style-guide.md`.

```markdown
> [!principle] Title
> Body text.
```

## Callout Types

### Principle
- **Purpose:** states a foundational, durable truth the document depends on.
- **Color:** Gold.
- **Icon suggestion:** compass or diamond.
- **When to use:** introducing a claim meant to outlast the document it appears in.
- **When not to use:** for anything time-bound, provisional, or specific to one instance — use Evidence or Application instead.

### Practice
- **Purpose:** an actionable, repeatable instruction.
- **Color:** Green.
- **Icon suggestion:** checkmark or open hand.
- **When to use:** telling the reader what to *do*.
- **When not to use:** for something that only informs, not instructs — use Principle or Evidence.

### Evidence
- **Purpose:** presents a claim tagged with its Intellectual Honesty category (Constitution Art. XI: Empirical, Clinical, Historical, Philosophical, Symbolic, Experiential, Speculative).
- **Color:** Steel blue.
- **Icon suggestion:** open book.
- **When to use:** any claim being asserted as more than opinion. The category tag is mandatory inside the callout body.
- **When not to use:** never omit the category tag — an Evidence callout without one is a defect, not a valid use.

### Reflection
- **Purpose:** marks first-person, interpretive, or synthesis-stage content.
- **Color:** Violet.
- **Icon suggestion:** open eye or spiral.
- **When to use:** Founder or contributor reflection distinct from raw evidence.
- **When not to use:** for content presented as fact — Reflection is explicitly subjective.

### Warning
- **Purpose:** flags a general risk, caveat, or limitation not specific to medical content.
- **Color:** Orange.
- **Icon suggestion:** triangle with exclamation mark.
- **When to use:** any non-medical caution (e.g., a methodology limitation, a data quality issue).
- **When not to use:** for health/medical content — use Medical Safety Note instead, which carries a distinct, stricter meaning.

### Founder Decision
- **Purpose:** marks a decision made or ratified by the Founder.
- **Color:** Gold (matches Principle — distinguish by icon, not color, since both mark durable authority).
- **Icon suggestion:** seal or crown.
- **When to use:** recording an actual ratification event, not a proposal.
- **When not to use:** for a proposed or pending decision — use Open Loop.

### Research Question
- **Purpose:** poses an open question driving inquiry.
- **Color:** Teal.
- **Icon suggestion:** question mark.
- **When to use:** framing what a study or research note is trying to answer.
- **When not to use:** for a question already answered — restate as Principle or Evidence instead.

### Open Loop
- **Purpose:** marks an unresolved thread requiring future attention.
- **Color:** Amber.
- **Icon suggestion:** unclosed circle or thread.
- **When to use:** anything pending a decision, a source, or a follow-up.
- **When not to use:** for a resolved item — remove or convert to Evidence/Principle once closed.

### Contradiction
- **Purpose:** flags two sources, claims, or documents that disagree.
- **Color:** Red.
- **Icon suggestion:** crossed arrows.
- **When to use:** any time synthesis reveals conflicting evidence or governance.
- **When not to use:** for mere uncertainty (no actual conflicting claim exists) — use Research Question or Open Loop.

### Application
- **Purpose:** shows how a principle or evidence translates into practical use.
- **Color:** Green (distinguish from Practice by content: Application connects an idea to a real use case; Practice is the instruction itself).
- **Icon suggestion:** target.
- **When to use:** coaching, teaching, or operational use-cases.
- **When not to use:** for the underlying instruction itself — use Practice.

### Public Content Candidate
- **Purpose:** flags content as a candidate for OSGMETAPHYSICS publication.
- **Color:** Teal.
- **Icon suggestion:** megaphone or globe.
- **When to use:** internal knowledge objects being considered for public release.
- **When not to use:** once actually published — replace with a status field, not this callout (see `document-layout-standard.md`, Approval Status).

### Medical Safety Note
- **Purpose:** a stricter, health-specific warning tied to the Office of Health's constitutional limit (Constitution Art. VI implementing text, Organizational Charter: "does not diagnose, prescribe, or substitute for licensed medical care").
- **Color:** Crimson.
- **Icon suggestion:** medical cross.
- **When to use:** any content in or adjacent to the Office of Health / Office of Nature Systems that could be mistaken for medical advice.
- **When not to use:** for general caution — use Warning. Do not downgrade a Medical Safety Note to a Warning to make content read more permissively.

### Ethics Review Required
- **Purpose:** marks content that must pass the Ethics & Evidence Council before publication.
- **Color:** Maroon.
- **Icon suggestion:** scales.
- **When to use:** any public-facing health, wellness, educational, or complementary-practice content, per Constitution Art. XIV.
- **When not to use:** once review is complete — replace with the resulting Approval Status (see `document-layout-standard.md`).

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-08 | Claude (Constitutional Secretary / Repository Architect) | Initial callout standard, thirteen types. |
