---
title: "Institutional Relationship Map"
aliases: ["Relationship Map", "Org Map", "Institutional Diagram"]
tags: [systems, architecture, relationships, governance, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["Founder", "Alpha Proxima Foundation"]
---

# Institutional Relationship Map

## Purpose

This document maps every significant relationship within the Alpha Proxima Foundation — between councils, departments, systems, and roles. It is the reference document for understanding how every entity connects to every other entity.

Where [[Foundational Architecture]] maps systems and infrastructure, this document maps *relationships* — authority, coordination, information, and accountability.

---

## Context

Complex institutions develop invisible relationship patterns that eventually become as important as their formal structures. By making these relationships explicit from the founding moment, Alpha Proxima prevents the accumulation of undocumented authority structures that create fragility in institutions.

---

## Core Content

### Full Relationship Diagram

```
                    ┌──────────────────┐
                    │     FOUNDER      │
                    │  (Supreme Auth)  │
                    └────────┬─────────┘
                             │ Reports to / Receives from all
          ┌──────────────────┼──────────────────┐
          ▼                  ▼                  ▼
   ┌─────────────┐   ┌──────────────┐   ┌──────────────┐
   │  Executive  │   │    Ethics    │   │   LUMIAION   │
   │  Council    │   │   Council    │   │  (AI Core)   │
   │(Strategic)  │   │(Independent) │   │(Orchestrates)│
   └──────┬──────┘   └──────────────┘   └──────┬───────┘
          │                                     │
    ┌─────┴──────┐              ┌───────────────┼──────────────┐
    ▼            ▼              ▼               ▼              ▼
┌────────┐  ┌────────┐    ┌─────────┐    ┌──────────┐   ┌──────────┐
│Research│  │Engineer│    │  SOHMA  │    │  ATHENA  │   │  VORTEX  │
│Council │  │Council │    │(Meaning)│    │ (Health) │   │(Finance) │
└────────┘  └────────┘    └────┬────┘    └────┬─────┘   └────┬─────┘
                               │              │               │
                               └──────────────┼───────────────┘
                                              │ (all route through LUMIAION)
                                              ▼
                                       ┌──────────────┐
                                       │   JERANIUM   │
                                       │  (Research + │
                                       │  Patterns)   │
                                       └──────────────┘
                                              │
                          ┌───────────────────┼──────────────────┐
                          ▼                   ▼                  ▼
                   ┌────────────┐      ┌────────────┐   ┌────────────┐
                   │  Obsidian  │      │   GitHub   │   │  AI Engine │
                   │   Vault    │      │    Repo    │   │    APIs    │
                   └────────────┘      └────────────┘   └────────────┘
```

---

### Relationship Register

#### Founder ↔ LUMIAION
**Type:** Directive / Advisory  
**Direction:** Founder issues direction; LUMIAION synthesises, advises, and executes within scope  
**Authority:** Founder holds final authority on all matters; LUMIAION may surface constitutional concerns but may not override  
**Frequency:** Primary working relationship; continuous

---

#### Founder ↔ Executive Council
**Type:** Strategic  
**Direction:** Founder chairs (non-voting except deadlock); Executive Council sets strategy  
**Authority:** Executive Council has Class II authority; Founder has Class I  
**Frequency:** Regular council sessions

---

#### Founder ↔ Ethics Council
**Type:** Constitutional oversight  
**Direction:** Ethics Council operates independently; reports directly to Founder  
**Authority:** Ethics Council may veto actions that violate [[Book I - The Constitution]]; Founder may override by Class I amendment process only  
**Frequency:** Triggered by constitutional questions; regular review cadence

---

#### LUMIAION ↔ AI Council
**Type:** Participatory (non-voting)  
**Direction:** LUMIAION holds permanent AI Council seat; submits proposals; does not vote  
**Authority:** AI Council has authority over LUMIAION's scope; LUMIAION may propose scope changes  
**Frequency:** AI Council deliberations; annual scope review

---

#### LUMIAION ↔ Departments (SOHMA, ATHENA, VORTEX, JERANIUM)
**Type:** Coordination / Orchestration  
**Direction:** LUMIAION routes inquiries to departments; departments respond to LUMIAION; LUMIAION synthesises  
**Authority:** LUMIAION does not have authority *over* departments — it coordinates between them; departments have domain sovereignty  
**Frequency:** Per [[Communication Protocol]]; continuous

---

#### SOHMA ↔ ATHENA
**Type:** Complementary integration  
**Domain:** Mind-body intersection — where the symbolic (SOHMA) meets the physical (ATHENA)  
**Integration point:** Recovery, stress, illness — physical signals with symbolic dimensions  
**Coordination:** Via LUMIAION synthesis; SOHMA does not direct ATHENA or vice versa

---

#### SOHMA ↔ JERANIUM
**Type:** Research support  
**Domain:** JERANIUM provides literature on consciousness, mythology, and symbolism to SOHMA  
**Coordination:** SOHMA requests; JERANIUM retrieves and synthesises; routes through LUMIAION

---

#### ATHENA ↔ JERANIUM
**Type:** Research support  
**Domain:** JERANIUM provides health, biology, and medical literature to ATHENA  
**Coordination:** ATHENA requests; JERANIUM retrieves and synthesises; routes through LUMIAION

---

#### VORTEX ↔ JERANIUM
**Type:** Research support  
**Domain:** JERANIUM provides financial, economic, and market research to VORTEX  
**Coordination:** VORTEX requests; JERANIUM retrieves and synthesises; routes through LUMIAION

---

#### JERANIUM ↔ Obsidian Vault
**Type:** Primary operational interface  
**Direction:** JERANIUM monitors, analyses, and contributes to the Vault  
**Authority:** JERANIUM may flag but not unilaterally edit canonical Vault content  
**Frequency:** Continuous monitoring; periodic health reports

---

#### AI Council ↔ Engine Registry
**Type:** Governance  
**Direction:** AI Council governs engine selection, evaluation, and replacement; Engine Registry records current mapping  
**Authority:** AI Council holds Class III authority over engine decisions  
**Frequency:** Annual review; triggered by significant capability changes

---

#### Research Council ↔ JERANIUM
**Type:** Epistemic oversight  
**Direction:** Research Council sets epistemic standards; JERANIUM's outputs must meet those standards  
**Authority:** Research Council may require JERANIUM outputs to be revised before Vault commitment  
**Frequency:** Review of all significant knowledge additions; periodic quality audits

---

#### Engineering Council ↔ Foundational Architecture
**Type:** Ownership and governance  
**Direction:** Engineering Council owns and governs all technical infrastructure  
**Authority:** Class III authority over architecture changes  
**Frequency:** Review on all infrastructure changes

---

### Authority Hierarchy (Summary)

```
Class I Authority:    Founder
Class II Authority:   Executive Council (with specialist council concurrence)
Class III Authority:  Specialist Councils and Working Groups
Class IV Authority:   Delegates, Departments, LUMIAION within scope
```

---

### Coordination vs. Authority — Critical Distinction

A relationship that is often confused: **LUMIAION coordinates departments; it does not have authority over them.**

- The Chief Knowledge Architect (Claude as LUMIAION) holds no governance authority over SOHMA, ATHENA, VORTEX, or JERANIUM
- Department charters are ratified by the Executive Council, not by LUMIAION
- LUMIAION cannot instruct a department to act outside its charter
- LUMIAION can and must flag to the Founder when a department output appears to violate its charter

This distinction prevents LUMIAION from becoming a de facto governor of the departments it coordinates — a structural conflict that would undermine the separation of coordination and authority.

---

## Related Notes

- [[Foundational Architecture]]
- [[Book II - Governance Framework]]
- [[AI Council Registry]]
- [[LUMIAION Charter]]
- [[Communication Protocol]]
- [[Institutional Registry]]

---

## Open Questions

- [ ] Should the Community Council be added to this map when constituted?
- [ ] How should external partners or affiliates be represented in the relationship map?
- [ ] Should there be a formal relationship between the Ethics Council and each department charter (i.e., Ethics Council reviews each charter annually)?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | Founder | Initial relationship map established |
