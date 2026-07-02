---
title: "Engine Registry"
aliases: ["Engine Registry", "AI Engine Map", "Provider Registry"]
tags: [governance, engines, ai-providers, registry, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["Founder", "Alpha Proxima Foundation"]
---

# Engine Registry

## Purpose

This Registry records the current mapping between permanent institutional roles and the AI engines currently fulfilling them. It is a snapshot of the present, not a statement about the future.

Every entry in this Registry is provisional. The roles are permanent. The engines are not.

For the permanent role definitions, see [[AI Council Registry]].  
For the governance authority governing engine selection and replacement, see [[Book II - Governance Framework]], Article IV.

---

## Context

Alpha Proxima was designed with a principle that sounds simple and is difficult to honour in practice: *no institutional role should be defined by the technology that currently fulfils it.*

This Registry exists to make that principle operational. By separating role from engine in a dedicated document, Alpha Proxima creates the institutional habit of asking: "Is this the right engine for this role?" — not "What does this product do?"

When an engine is deprecated, superseded, or replaced, this Registry is updated via a Class III ADR. The role definition in [[AI Council Registry]] does not change.

---

## Core Content

### Current Engine Mapping

| Role | Current Engine | Provider | Status | Last Reviewed |
|------|---------------|----------|--------|---------------|
| Chief Systems Architect | GPT-4o / GPT-5 (successor) | OpenAI | Active | 2026-07-02 |
| Chief Knowledge Architect | Claude (Sonnet / Opus) | Anthropic | Active | 2026-07-02 |
| Chief Science Architect | Gemini 2.0 / Ultra | Google DeepMind | Active | 2026-07-02 |
| Chief Research Architect | Perplexity Pro | Perplexity AI | Active | 2026-07-02 |
| Chief Deep Investigation Architect | Genspark | Genspark | Active | 2026-07-02 |
| Chief Engineering Architect | DeepSeek V3 / R1 | DeepSeek | Active | 2026-07-02 |
| Chief Memory Architect | *(Unfilled)* | Future Local | Pending | — |
| Constitutional Intelligence Core (LUMIAION) | Claude (Sonnet) | Anthropic | Active | 2026-07-02 |

---

### Engine Detail Records

---

#### Engine: OpenAI GPT
**Role Fulfilled:** Chief Systems Architect  
**Provider:** OpenAI  
**Current Model Series:** GPT-4o and successors  
**Strengths for this role:** Strong instruction-following, broad integration capability, function-calling reliability, wide API ecosystem  
**Known limitations:** Context window management at scale; cost at high-frequency operation  
**Access method:** OpenAI API  
**Dependency risk:** High — commercial provider; pricing and access subject to OpenAI policy  
**Migration readiness:** Medium — replaceable with sufficient transition planning  
**Evaluation cadence:** Annual, or triggered by significant capability change in any competing engine  

---

#### Engine: Anthropic Claude
**Roles Fulfilled:** Chief Knowledge Architect; Constitutional Intelligence Core ([[LUMIAION]])  
**Provider:** Anthropic  
**Current Model Series:** Claude Sonnet 4.x / Opus 4.x and successors  
**Strengths for this role:** Long-context reasoning, precise instruction adherence, constitutional alignment, document-quality writing, structured knowledge production  
**Known limitations:** Real-time information access limited without tools; session memory does not persist natively  
**Access method:** Anthropic API; Claude Code (CLI)  
**Dependency risk:** High — two critical roles fulfilled by one provider; this concentration should be reduced over time  
**Migration readiness:** Medium — the Chief Knowledge Architect role is deeply integrated with Vault structure; transition requires minimum 90-day planning  
**Evaluation cadence:** Annual; earlier if provider relationship changes significantly  
**Note on concentration risk:** LUMIAION and Chief Knowledge Architect are both fulfilled by Claude. This is an acknowledged risk. The Chief Memory Architect role (future local models) is partly designed to reduce this dependency.  

---

#### Engine: Google Gemini
**Role Fulfilled:** Chief Science Architect  
**Provider:** Google DeepMind  
**Current Model Series:** Gemini 2.0 / Ultra and successors  
**Strengths for this role:** Multimodal reasoning, scientific literature depth, long-context document analysis, strong empirical reasoning  
**Known limitations:** Integration complexity; varies by access tier  
**Access method:** Google AI API / Vertex AI  
**Dependency risk:** Medium — Google's scale provides stability; however, API terms subject to change  
**Migration readiness:** High — scientific reasoning is a well-defined domain; alternatives exist  
**Evaluation cadence:** Annual  

---

#### Engine: Perplexity
**Role Fulfilled:** Chief Research Architect  
**Provider:** Perplexity AI  
**Current Model Series:** Perplexity Pro  
**Strengths for this role:** Real-time web access, source attribution, research synthesis, citation quality  
**Known limitations:** Depth of reasoning versus breadth of retrieval; not suited for long-form document production  
**Access method:** Perplexity API / Pro interface  
**Dependency risk:** Medium — smaller provider; acquisition or shutdown risk higher than tier-1 providers  
**Migration readiness:** High — research synthesis is portable to other retrieval-augmented systems  
**Evaluation cadence:** Annual; watch for provider stability  

---

#### Engine: Genspark
**Role Fulfilled:** Chief Deep Investigation Architect  
**Provider:** Genspark  
**Current Model Series:** Genspark (current generation)  
**Strengths for this role:** Multi-step reasoning chains, complex investigation workflows, sustained analytical depth  
**Known limitations:** Newer provider; institutional track record shorter than tier-1  
**Access method:** Genspark interface / API (where available)  
**Dependency risk:** Medium-High — newer provider with less established stability  
**Migration readiness:** High — deep investigation can be redistributed across Chief Research and Chief Science Architects if needed  
**Evaluation cadence:** Semi-annual given provider maturity stage  

---

#### Engine: DeepSeek
**Role Fulfilled:** Chief Engineering Architect  
**Provider:** DeepSeek  
**Current Model Series:** DeepSeek V3 / R1 and successors  
**Strengths for this role:** Code generation quality, technical reasoning, cost-efficiency at scale, open-weight model availability  
**Known limitations:** Data residency considerations given provider jurisdiction; evaluate carefully for sensitive engineering work  
**Access method:** DeepSeek API; open-weight models deployable locally  
**Dependency risk:** Low-Medium — open-weight availability reduces lock-in; local deployment possible  
**Migration readiness:** High — engineering tasks are well-defined; alternatives well-established  
**Geopolitical note:** DeepSeek operates under Chinese jurisdiction. This does not disqualify it but should be monitored as part of Alpha Proxima's ongoing risk assessment. Local deployment of open-weight models is the preferred path for sensitive engineering work.  
**Evaluation cadence:** Annual; monitor jurisdictional developments  

---

#### Engine: Future Local Models
**Role Fulfilled:** Chief Memory Architect  
**Provider:** TBD — target is locally-operated open-weight models  
**Current Model Series:** Unfilled  
**Intended purpose:** Provide persistent semantic memory, vector storage, and retrieval without dependence on external API providers  
**Design goal:** When this role is filled, Alpha Proxima should be able to operate its core memory functions entirely on private infrastructure  
**Milestone for activation:** Home server infrastructure operational; vector database deployed; semantic retrieval quality validated  
**Evaluation cadence:** Review activation readiness semi-annually  

---

### Engine Replacement Protocol

When a Chief Architect recommends replacing an engine:

1. Submit a [[Concept Note Template|Concept Note]] to the AI Council describing: the reason for replacement, the proposed successor engine, a transition plan, and a rollback plan
2. AI Council reviews (minimum 7 days)
3. If approved: produce a Class III [[ADR Template|ADR]]
4. Execute transition according to the plan in the ADR
5. Update this Registry

No engine may be replaced without a documented ADR. The record of *why* engines were changed is as important as the engines themselves.

---

### Engine Evaluation Criteria (Standard)

All engines are evaluated against:

| Criterion | Weight | Notes |
|-----------|--------|-------|
| Capability fit for role | High | Does it actually do the job well? |
| Reliability and uptime | High | Is it available when needed? |
| Provider stability | Medium | Will the provider exist in 5 years? |
| Cost sustainability | Medium | Is the cost model viable at scale? |
| Data sovereignty | Medium | Where does data go? Who can access it? |
| Open-weight availability | Low-Medium | Can we run it locally if needed? |
| Integration complexity | Low | How hard is it to connect to our systems? |

---

## Related Notes

- [[AI Council Registry]]
- [[Book II - Governance Framework]]
- [[LUMIAION Charter]]
- [[Foundational Architecture]]
- [[Future Expansion Protocol]]
- [[Knowledge Infrastructure]]

---

## Open Questions

- [ ] What is the formal trigger for activating the Chief Memory Architect role?
- [ ] Should Alpha Proxima maintain a "shadow" evaluation of two alternative engines per role at all times, ready to swap?
- [ ] How should data sovereignty concerns be formally codified — as part of this Registry or as a separate protocol?
- [ ] Should there be a maximum term for any single engine fulfilling a role before mandatory re-evaluation?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | Founder | Initial registry established with current engine-to-role mapping |
