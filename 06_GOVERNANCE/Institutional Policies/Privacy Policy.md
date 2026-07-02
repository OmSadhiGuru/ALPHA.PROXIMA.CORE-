---
title: "Privacy Policy"
aliases: ["Privacy Policy", "Data Privacy Policy", "Foundation Privacy Policy"]
tags: [policy, privacy, data, governance, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: ratified
version: "1.0.0"
authors: ["Founder", "LUMIAION"]
document_class: Institutional Policy
governed_by: "Book I - The Constitution"
---

# Privacy Policy

---

## Purpose

This policy defines how the Alpha Proxima Foundation handles personal data, sensitive institutional information, and privacy across its knowledge systems, research programs, and operations. It establishes the constitutional position of privacy as a foundational value — not a compliance checkbox.

---

## Governing Principle

**Privacy is a precondition of trust. Trust is a precondition of institutional integrity.**

The Foundation does not collect, retain, or process personal data beyond what is necessary for its mission. When personal data enters Foundation systems, it is handled with the minimum footprint necessary and protected from unauthorized access, publication, or retention.

---

## Scope

This policy applies to:

- All information stored in the Obsidian Vault
- All information stored in or transmitted through the GitHub repository
- All information processed by reasoning engines in the execution of Foundation cognitive functions
- All information shared with, processed by, or stored in third-party AI providers
- All information about people participating in, researching with, or collaborating with the Foundation

This policy does not apply to:
- Published external documents (papers, books, articles) used as research sources
- Publicly available institutional information about organizations or public figures

---

## Categories of Information

### Category A — Institutional Information (Non-Personal)

Constitutional documents, governance frameworks, research programs, engineering systems, decision records, and all other Foundation knowledge assets. No privacy concern in the institutional information layer.

**Handling:** Stored in Vault and GitHub repository. Committed, versioned, and visible to all institutional participants.

### Category B — Participant Information (Personal)

Names, roles, contact information, and contributions of human participants in the Foundation.

**Handling:**
- Stored only in `09_PEOPLE/` (when this folder is created)
- Not published publicly without explicit participant consent
- Minimum necessary information only: role, institutional contributions, contact method for institutional use
- No biometric, financial, health, or personal history data without explicit informed consent and a documented legitimate purpose

### Category C — Sensitive Institutional Information

Strategic plans, unreleased research findings, unpublished proposals, and information shared in confidence by external collaborators.

**Handling:**
- Stored in Vault; not committed to public GitHub repository while sensitive
- Clearly marked in frontmatter: `sensitivity: confidential`
- Access restricted to designated institutional participants
- Review at each quarter whether sensitivity classification remains appropriate

### Category D — Third-Party Personal Data (Research Subjects)

Data about individuals that enters the Foundation through research programs (e.g., case studies, interview data, referenced personal accounts).

**Handling:**
- Anonymized before Vault commitment wherever possible
- If identifiable, stored only in a designated restricted ARCHIVE subfolder
- Not published in Canonical Syntheses without anonymization or explicit consent
- Ethics Council review required for research programs that involve identifiable personal data

---

## Third-Party AI Providers

The Foundation uses external reasoning engines (currently Anthropic Claude, Perplexity, DeepSeek, Comet) to execute its cognitive functions. In doing so:

1. **Assume all inputs may be stored or used for training** by the provider, unless the provider's terms explicitly state otherwise and those terms have been verified.
2. **Do not send Category B, C, or D information to external AI providers** without:
   - A documented legitimate need
   - The relevant participant's knowledge (for Category B)
   - Anonymization where possible (for Category D)
3. **Do not use external AI providers as repositories of sensitive information.** The Vault is the institutional memory. AI provider context windows are transient.
4. **API usage without persistent storage** is preferred. Session-based API calls that do not persist user data are lower risk than platform interfaces that may retain conversations.

As the Foundation moves toward Phase 2 and Phase 3 infrastructure (per the [[Engineering Office Charter]]), the use of locally-operated models will reduce third-party data exposure. Until then, minimum necessary data principle applies to all provider interactions.

---

## Data Minimization

The Foundation collects and retains the minimum information necessary for institutional operation. This means:

- Do not add biographical information about a person to the Vault unless it is relevant to their institutional role
- Do not log individual session content unless the session produced an institutional artifact that belongs in the Vault
- Do not retain drafts, working notes, or intermediate outputs beyond the session in which they were produced, unless they have independent institutional value
- When in doubt about whether information belongs in the Vault, ask: *Would this information serve the Foundation's mission if read by a future participant ten years from now?* If no, do not commit it.

---

## Vault as Institutional Memory, Not Personal History

The Vault is institutional memory. It documents what the Foundation knows, decides, and builds — not the personal history of individuals involved. When a person contributes to the Foundation, their contribution is recorded (as part of a document's `authors` field or in a relevant ADR). Their personal circumstances, private communications, or off-topic activities are not recorded.

---

## Breach and Disclosure Protocol

If sensitive institutional or personal information is inadvertently committed to the public GitHub repository:

1. Notify the Founder immediately
2. Remove the information from the repository (git history scrub may be required)
3. Assess whether affected parties (if Category B or D) need to be notified
4. Document the incident in the Engineering Debt Register with corrective measures
5. Review the process that allowed the breach and update procedures to prevent recurrence

---

## Privacy Review

The Ethics Council is responsible for reviewing this policy annually and for reviewing any research program that involves Category D data before that program commences.

LUMIAION flags any Vault document that appears to contain personal information inconsistent with this policy during its quarterly Vault integrity review.

---

## Related Notes

- [[Book I - The Constitution]]
- [[Ethics Council Charter]]
- [[Engineering Office Charter]]
- [[Source Attribution Policy]]
- [[Research Intelligence Office Charter]]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | Founder + LUMIAION | Initial ratification; four data categories; third-party AI provider protocol; data minimization principle; Vault as institutional not personal memory; breach protocol; Ethics Council review mandate |
