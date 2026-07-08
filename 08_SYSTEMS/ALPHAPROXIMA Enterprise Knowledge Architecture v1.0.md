---
title: "ALPHAPROXIMA Enterprise Knowledge Architecture v1.0"
aliases: ["Enterprise Knowledge Architecture", "AEKA", "Master Reference", "Institutional Master Reference"]
tags: [systems, architecture, governance, master-reference, alpha-proxima, lumiaion, knowledge-graph]
created: 2026-07-07
updated: 2026-07-07
status: active
version: "1.0.0"
authors: ["Founder", "LUMIAION"]
document_type: canonical-master-reference
artifact_type: master-reference
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Orchestration"
reasoning_engine: "LUMIAION"
dependencies: ["[[Book I - The Constitution]]", "[[Foundational Architecture]]", "[[Office Registry]]", "[[Engine Registry]]", "[[Knowledge Graph Architecture v1.0]]", "[[Vault Structure Convention]]"]
related_documents: ["[[Alpha Proxima Core]]", "[[The Orchestration Framework]]", "[[Institutional Relationship Map]]", "[[ADR-0002 - Reconciling the Four Institutional Taxonomies]]", "[[LUMIAION - Operating Manual (LOOM)]]"]
related_research_programs: []
---

# ALPHAPROXIMA Enterprise Knowledge Architecture v1.0

## Purpose

This document is the **institutional master reference** for the Alpha Proxima / OSG ecosystem. It does not replace, rewrite, or re-rank any existing canon. It is the executive architecture layer that references and orchestrates the documents that already govern each domain, closes the specific gaps named in the Founder's brief (repository standards, self-search architecture, compatibility layer, RAG strategy, automation architecture, interoperability standards), and records the one genuine cross-cutting inconsistency found during compilation as [[ADR-0002 - Reconciling the Four Institutional Taxonomies]] rather than silently editing the documents in conflict.

Every section below states explicitly: **Canonical Source(s)** (existing, authoritative, unchanged), **New Material** (introduced here because nothing else covers it), **Dependencies**, **Related Systems**, and **Future Extension Points**. Where a section's canonical source is complete and sufficient, this document adds no new material and says so — padding an already-solved problem is itself a form of duplication.

---

## Context

Commissioned 2026-07-07 as the "Institutional Master Reference" that unifies existing canon under a single-source-of-truth principle, rather than a new constitution. Compiled by inventorying the vault's actual current state (00_CONSTITUTION through 99_ARCHIVE, `03_AI_COUNCIL`, `08_SYSTEMS`, `11_OPERATIONS`, and the live GitHub repository at `github.com/OmSadhiGuru/ALPHA.PROXIMA.CORE-`) rather than drafting from the brief alone. This follows directly from the [[LUMIAION - Operating Manual (LOOM)]] integration (2026-07-07), where a first-draft document contradicted already-ratified canon (Office Registry) and had to be reconciled — the same risk this document was explicitly commissioned to avoid at a much larger scale.

---

## 0. Canonical Dependency Map

```
ALPHAPROXIMA
│
├── Book I - The Constitution  [00_CONSTITUTION, ratified, Class I]
│   ├── Book II - Governance Framework  [councils, decision classes I-IV, role→engine table]
│   └── Book III - Knowledge Integrity  [evidence classes C/M/Q/E/S/P, revision policy]
│
├── Foundational Architecture  [08_SYSTEMS, System Registry: Vault + GitHub + AI APIs, Phase 1-3 roadmap]
│   ├── The Orchestration Framework  [component map, routing tree, Intelligence Tiers 1-5, session lifecycle]
│   │   └── LUMIAION Architecture Spec v0.1  [LUMIAION's own memory model, 3 layers, evolution path v0.1→v1.0]
│   └── Institutional Relationship Map  [pairwise relationship register — "LUMIAION coordinates, does not command"]
│
├── AI Council Registry + Engine Registry  [03_AI_COUNCIL — 7 Chief Architect roles ↔ current engines]
│
├── Office Registry + Workflow Registry  [11_OPERATIONS — production-function offices, workflows, dashboards]
│   └── LUMIAION - Operating Manual (LOOM)  [end-to-end idea→published-asset pipeline, reconciled to Office Registry]
│
├── Department Charters  [03_AI_COUNCIL/Departments — SOHMA, ATHENA, VORTEX, JERANIUM: subject-matter jurisdiction]
│
├── Institutional Knowledge Graph  [08_SYSTEMS — Node Taxonomy (19 types), Relationship Taxonomy (14 types),
│   Knowledge Graph Architecture v1.0, EP-001 roadmap, generated registries: 204 nodes / 1,985 relationships]
│
├── Repository Standards  [= the vault's own folder structure, Vault Structure Convention; ES-01..ES-11
│   Engineering Standards; live repo github.com/OmSadhiGuru/ALPHA.PROXIMA.CORE-]
│
├── Automation Standards  [08_SYSTEMS/Engineering Standards/07 - Automation Standard; Automation Queue Index —
│   all candidates currently status: planned]
│
└── AI Department Specifications  [each Department Charter's "Preferred AI Engine" section;
    Engine Registry's per-engine Detail Records]
```

**Reconciliation note:** "Subminds/Departments" (this brief's term) and "Offices" (Office Registry's term) are two different, both-valid axes — see [[ADR-0002 - Reconciling the Four Institutional Taxonomies]]. This document uses "Subminds" only where quoting the Founder's brief; everywhere else it names the specific axis (Domain Department vs. Production Office vs. Chief Architect Role vs. Council).

---

## 1. Executive Architecture Overview

**Canonical Source:** [[Book I - The Constitution]] Art. I (identity), [[ADR-0001 - The Founding Decision]] §5/§9 (LUMIAION and the four departments formally constituted), [[LUMIAION Architecture Spec v0.1]] (LUMIAION's operating model), the four Department Charters.
**New Material:** none — this section is a pointer, not a redefinition.

- **ALPHAPROXIMA** (`ALPHA.PROXIMA.CORE-`) — the Foundation itself. Supreme instrument: [[Book I - The Constitution]]. The trailing dash is constitutional, not typographic: it declares the work permanently incomplete (Book I, Art. I).
- **LUMIAION** — the Constitutional Intelligence Core, formally established by ADR-0001 §5. Permanent role, replaceable engine (currently Claude). Coordinates departments; per [[Institutional Relationship Map]] it explicitly **does not have authority over them**.
- **Subminds (Domain Departments)** — SOHMA (consciousness, metaphysics, symbolism, meaning), ATHENA (health, biology, training, longevity), VORTEX (finance, economics, trading, strategy), JERANIUM (knowledge architecture, research, data, pattern detection). Each governed by its own Charter; jurisdiction, not authority, is what distinguishes them (see Section 3).
- Additional departments (per the brief's "may be proposed only if structurally justified") follow the same route every department followed: a Concept Note in `05_PROPOSALS/`, Executive Council review, ADR ratification (Class II, per [[Decision Routing Protocol]]). No department has ever been created any other way, and this document does not create an exception.

**Dependencies:** Book I, ADR-0001, four Charters.
**Related Systems:** AI Council Registry (engine axis), Office Registry (function axis).
**Future Extension Points:** a fifth department requires a Concept Note, not an edit to this section.

---

## 2. System Map

**Canonical Source:** [[ADR-0001 - The Founding Decision]] §9 (departments), [[Vault Structure Convention]] (folder structure), [[Artifact Registry]] (14 output/artifact types), department Charters (knowledge domains).
**New Material:** the explicit "Projects" and "Outputs" tiers below, since no existing document draws the full ALPHAPROXIMA → Outputs chain in one place.

```
ALPHAPROXIMA
 └─ LUMIAION (orchestration)
     └─ Subminds / Domain Departments
         ├─ SOHMA    → knowledge domain: consciousness, metaphysics, symbolism
         ├─ ATHENA   → knowledge domain: health, biology, training, longevity
         ├─ VORTEX   → knowledge domain: finance, economics, trading
         └─ JERANIUM → knowledge domain: knowledge architecture, research, data
             └─ Projects
                 ├─ 06_PROJECTS/         (Alpha Proxima internal projects — currently empty, .gitkeep only)
                 ├─ 07_RESEARCH/RP-001/  (Research Programs — e.g. "Atlas of Human Consciousness," SOHMA-adjacent)
                 └─ OSG_LAUNCH/          (a SEPARATE, explicitly isolated business namespace —
                                          not a child of Alpha Proxima governance; see Section 7)
                     └─ Outputs (per Artifact Registry's 14 types)
                         Constitution · Law · ADR · Concept Note · Research Commission · Research Package ·
                         Canonical Synthesis · Engineering Standard · Future Proposal · Strategic Review ·
                         Operational Procedure · Implementation Note · Engineering Report · Operational Health Report
```

**Dependencies:** Artifact Registry, Vault Structure Convention.
**Related Systems:** Office Registry (who produces each output type), Workflow Registry (how an output moves stage to stage).
**Future Extension Points:** `06_PROJECTS/` is real but empty — the first Alpha Proxima-internal project (as opposed to research program or OSG business work) will establish the pattern others follow.

---

## 3. Department Standard

**Canonical Source:** [[SOHMA Charter]], [[ATHENA Charter]], [[VORTEX Charter]], [[JERANIUM Charter]] — mission, jurisdiction, and Preferred AI Engine are authoritative there. **Databases, Automation Needs, and Human Approval Points are new material**, added here because the Charters do not yet define them in this shape; they are additive, not corrections.

| Field | SOHMA | ATHENA | VORTEX | JERANIUM |
|---|---|---|---|---|
| **Mission** | Consciousness, metaphysics, symbolism, astrology, dreams, meditation, Reiki, meaning-construction | Health, biology, training, nutrition, performance, recovery, longevity, medical knowledge | Finance, economics, trading, business strategy, investments, risk analysis | Knowledge architecture, research, data, pattern detection, knowledge graph development, institutional intelligence |
| **Jurisdiction** | Interiority and symbolic frameworks | Body intelligence and health-sensitive data | Financial data and market intelligence | Cross-department knowledge routing and the Knowledge Graph itself |
| **AI Model Responsibilities** *(Charter, "Preferred AI Engine")* | Claude (primary), GPT (supplementary, broad symbolic databases) | Gemini (primary, scientific literature), Claude (synthesis/communication) | GPT (primary, quantitative modelling), Claude (strategy synthesis) | Perplexity (primary, retrieval), Genspark (deep investigation), Claude (synthesis/writing) |
| **Inputs** *(new)* | Founder reflections, symbolic/astrological queries | Health data, training logs, medical literature requests | Market data, financial questions, strategy briefs | Research commissions, cross-department knowledge requests, vault state |
| **Outputs** *(new)* | Interpretive notes, symbolic frameworks (Class P/S evidence per Book III) | Evidence-based health syntheses (Class C/E per Book III) | Financial models, strategic recommendations | Canonical syntheses, knowledge graph updates, routing decisions |
| **Databases** *(new — none exist yet)* | None. No dedicated store; notes live in `07_RESEARCH/` or department-tagged vault notes. | None. | None. | The Institutional Knowledge Graph itself (`node_registry.json`, `relationship_registry.json`) is JERANIUM's natural home once formally assigned. |
| **Tools** *(new)* | None automated | None automated | None automated | `ap.py node-registry`, `ap.py relationship-extract`, `ap.py dependency-map` (Engineering Toolkit) |
| **Knowledge Formats** | Book III evidence classes P (phenomenological) and S (speculative) predominate | Book III evidence classes C (consensus) and E (emerging) predominate | Book III evidence class M (competing models) predominate (market theories) | All six Book III classes — JERANIUM is the routing layer, not a domain restricted to one class |
| **Automation Needs** *(new)* | None identified | None identified | None identified | Node/Relationship registry regeneration (already built, not yet scheduled — see Section 9) |
| **Human Approval Points** | Ethics Council Research/Publication Review Protocol for any public-facing symbolic-framework claim | Ethics Council Research Review Protocol mandatory given health-sensitivity (per Charter's own data-handling note) | Ethics Council Research Review Protocol mandatory given financial-data sensitivity | Founder/LUMIAION per Knowledge Routing Protocol Rule 5 ("Route research to JERANIUM"); canonization requires Research Council per Research Governance Protocol Stage 5 (see gap below) |

**Known gap inherited, not created, by this table:** Research Governance Protocol Stage 5 (Canonisation) names the Research Council as reviewing authority, but [[Research Council]] is `status: placeholder` — tracked in `CN-0001 - Constitutional Alignment Gap Report`, not resolved here.

**Dependencies:** four Charters, Book III (evidence classes), Ethics Council Charter (five Review Protocols).
**Related Systems:** Office Registry's Research Intelligence Office (function axis, not domain axis — see ADR-0002).
**Future Extension Points:** if a department is ever given a real database (e.g., ATHENA wiring to a health-data store), the Compatibility Layer (Section 7) and Automation Standard's approval boundary govern how, not this table.

---

## 4. Knowledge Object Schema

**Canonical Source:** [[Node Taxonomy]] (19 node types), [[Relationship Taxonomy]] (14 relationship types), [[Vault Structure Convention]] (required frontmatter, required six sections), [[Research Note Template]].
**New Material:** four fields the Founder's brief requires that do not exist in any current template (`domain`, `department_owner`, `osg_interpretation`, `application`, `last_reviewed`) — added as an **optional extension block**, not a replacement of the existing frontmatter standard.

The Founder's brief specifies 13 fields. Each is mapped below to what already exists rather than issuing a fifth competing schema:

| Requested Field | Status | Resolution |
|---|---|---|
| Title | Exists | `title` — universal frontmatter (Vault Structure Convention) |
| Domain | **New** | Add `domain:` frontmatter field — one of the four Department jurisdictions, or `cross-domain` |
| Department Owner | **New** | Add `department_owner:` frontmatter field (distinct from `authors:`, which names the drafting engine/person) |
| Source Type | Partial | Research-class notes already have `contributor` + `source_quality` ([[Research Note Template]]); non-research notes get a new `source_type:` field (`primary`, `synthesis`, `AI-generated`, `founder-directive`) |
| Summary | Exists | The `## Purpose` section, required by Vault Structure Convention, already serves this role — no new field |
| Key Concepts | Exists | Node Taxonomy's `concept` node type + wiki-links already capture this; use `## Related Notes` |
| **OSG Interpretation** | **New** | No existing field captures the Foundation's own synthesis/take on a source, as distinct from the source's content. Add a `## OSG Interpretation` body section for any node type that ingests external material (`research_artifact`, `evidence_claim`, `theory`) |
| Related Nodes | Exists | [[Relationship Taxonomy]]'s 14 types (`REFERENCES`, `SUPPORTS`, `CONTRADICTS`, etc.) already formalize this beyond a flat list — use relationship-typed wiki-links, not a new field |
| **Application** | **New** | No field captures practical/operational use of a knowledge item. Add `## Application` body section — how a department or project actually uses this node |
| Status | Exists | `status:` — universal frontmatter |
| Version | Exists | `version:` — universal frontmatter, semantic versioning per Vault Structure Convention |
| **Last Reviewed** | **New** | Currently only `updated:` exists, which conflates edits with reviews. Add `last_reviewed:` (date of the most recent human/Council review, independent of content edits) |
| Next Action | Partial | `## Open Questions` (required section) already captures this at the document level; for a single scannable field, add `next_action:` as an optional one-line frontmatter summary that must point back to a specific Open Questions checkbox, not duplicate it |

**Resulting extension block** (append to the Vault Structure Convention's required frontmatter for any node participating in the Knowledge Graph as a `concept`, `theory`, `evidence_claim`, `research_artifact`, or `canonical_synthesis` type):

```yaml
domain: "SOHMA | ATHENA | VORTEX | JERANIUM | cross-domain"
department_owner: "[[Department Name]]"
source_type: "primary | synthesis | AI-generated | founder-directive"
last_reviewed: YYYY-MM-DD
next_action: "one line, must reference an Open Questions item"
```

Plus two new required body sections where applicable: `## OSG Interpretation`, `## Application`.

**Dependencies:** Node Taxonomy, Relationship Taxonomy, Vault Structure Convention.
**Related Systems:** Institutional Knowledge Graph tools (Node Registry Generator would need a minor update to extract the new fields — see Section 9, Phase 4).
**Future Extension Points:** this extension block is additive and versioned independently; it does not require reissuing the base Vault Structure Convention.

---

## 5. Repository Architecture

**Canonical Source:** [[Vault Structure Convention]] (the folder structure *is* the repository architecture — this vault is the GitHub repo, live at `github.com/OmSadhiGuru/ALPHA.PROXIMA.CORE-`), [[Foundational Architecture]] (System 2: GitHub Repo).
**New Material:** the mapping table below (brief's generic categories → real folders) and the explicit naming of two genuine gaps (Agents, Prompts).

The brief requests a GitHub layout using generic categories. Rather than propose a second, competing folder tree, each category is mapped to the real, already-live structure:

| Brief Category | Real Location | Status |
|---|---|---|
| Governance | `00_CONSTITUTION/`, `04_DECISIONS/`, `05_PROPOSALS/`, `06_GOVERNANCE/` | Live |
| Architecture | `08_SYSTEMS/` | Live |
| Departments | `03_AI_COUNCIL/Departments/` | Live |
| **Agents** | **No dedicated folder exists.** `03_AI_COUNCIL/` holds role/engine registries, not per-agent operational configs (system prompts, tool permissions — those live outside the vault, e.g. in `~/.claude/agents/`). | **Gap** |
| Projects | `06_PROJECTS/` (empty, Alpha Proxima-internal) — distinct from `OSG_LAUNCH/` (separate business namespace, see Section 7) | Live but empty |
| **Prompts** | **No dedicated folder exists.** Closest fit is `10_TEMPLATES/`, which already governs "reusable note formats." | **Gap** |
| Research | `07_RESEARCH/` | Live |
| Templates | `10_TEMPLATES/` | Live |
| Automations | `08_SYSTEMS/Automation/`, `08_SYSTEMS/Engineering Toolkit/` (11 tools, `ap.py` CLI), `11_OPERATIONS/Automation Queue/` | Live |
| Logs | **No dedicated top-level folder.** Closest fit: `08_SYSTEMS/Engineering Toolkit/Reports/` (generated reports) + per-note `Version History` tables + git commit history itself (`git log`, auto-committed as "vault backup" snapshots) | Covered, differently named |
| Archive | `99_ARCHIVE/` | Live |

**Recommended resolution for the two real gaps** (Agents, Prompts): add as subfolders of existing numbered folders, not new top-level numbers — `03_AI_COUNCIL/Agents/` (an index of which agent configs exist and what role/engine they map to, not the configs themselves) and `10_TEMPLATES/Prompts/`. Both changes are additive to the Vault Structure Convention and, per that document's own rule ("never modify a template without an ADR"), require a Concept Note before creation — not created unilaterally here.

**Additional finding:** no `LICENSE` file and no `.github/` (no CI, no PR workflow) exist anywhere in the repository. Git is currently used purely as an Obsidian-Git auto-backup mechanism ("vault backup: <timestamp>" commits), not as a review pipeline. This is consistent with Foundational Architecture's Phase 1 scope but is worth naming as a boundary: there is currently no automated check preventing a bad commit from reaching `main`.

**Dependencies:** Vault Structure Convention, Foundational Architecture.
**Related Systems:** Automation Standard (governs whether a future CI check counts as "automating judgment," which it would).
**Future Extension Points:** Agents/, Prompts/ subfolders; optional `.github/` CI once Phase 2 orchestration begins (Section 9).

---

## 6. Self-Search Architecture

**Canonical Source:** [[Knowledge Graph Architecture v1.0]], [[Node Taxonomy]], [[Relationship Taxonomy]], [[Graph Readiness Assessment]], `EP-001 Engineering Roadmap`, Tool 010 (Node Registry Generator), Tool 011 (Relationship Extractor), [[Graph View Color System]].
**New Material:** concrete, runnable search commands (none were previously assembled in one place) and an explicit statement of exactly which unbuilt step blocks RAG.

**Current state (accurate, not aspirational):** there is no live vector search or RAG in this system. What exists is a **Markdown-to-registry graph prototype** — a deterministic extractor that reads YAML frontmatter, wiki-links, and folder structure to produce `node_registry.json` (204 nodes, last generated 2026-07-03) and `relationship_registry.json` (1,985 relationships, 199 unresolved). This is explicitly staged as the precursor to, not a substitute for, a future graph database or vector store.

**Metadata strategy:** the required frontmatter block (Vault Structure Convention) plus the Knowledge Object Schema extension (Section 4) plus the 19 Node Taxonomy types plus the 14 Relationship Taxonomy types together are the entire metadata strategy. No fifth metadata system is introduced.

**Tags:** kebab-case, always including the primary domain tag and relevant institution tag, per Vault Structure Convention — already sufficient, unchanged.

**Index files:** `Alpha Proxima Core.md` (root MOC), each folder's own index note (e.g. `11_OPERATIONS/README.md`, `09_FUTURE/README.md`), and the two generated reports (`Node Registry Report.md`, `Relationship Registry Report.md`) function as the current index layer.

**README structure:** every governed folder should carry a README or index note following the same six required sections as any other note (Vault Structure Convention) — most already do (`11_OPERATIONS/README.md`, `OSG_LAUNCH/README.md`); the root `README.md` is currently a one-line stub and is the weakest link in this chain.

**Search commands, as they exist today:**

| Interface | Command / Query |
|---|---|
| Obsidian Quick Switcher | `Cmd+O`, fuzzy filename match |
| Obsidian search operators | `path:"03_AI_COUNCIL/Departments"`, `tag:#alpha-proxima`, `file:"SOHMA Charter"` — the same query language already used by [[Graph View Color System]] |
| Shell / grep | `grep -rn "term" --include="*.md" .` from vault root |
| Engineering CLI | `ap.py node-registry` (regenerate node index), `ap.py relationship-extract` (regenerate relationship index), `ap.py dependency-map`, `ap.py office-check`, `ap.py research-check` |
| Structured query | `python3 -c "import json; ..."` against `node_registry.json` / `relationship_registry.json` directly for anything the CLI reports don't already surface |

**Vector search / future RAG compatibility:** the roadmap already exists and is not being replaced — [[Graph Readiness Assessment]]'s 7-phase migration and `EP-001`'s tool sequence (ES-007 Graph Builder → ES-008 Graph Validator → ES-009 Dashboard → ES-010 Future Graph Connector, the last of which explicitly targets Neo4j/RDF/GraphRAG/vector-store adapters). **The single blocking step today is ES-007 (Graph Builder)** — it does not exist yet, and every later step in the roadmap depends on it. This document does not add a competing roadmap; it names the one concrete next step.

**Notion / GitHub compatibility:** see Section 7 (Compatibility Layer) — not duplicated here.

**Dependencies:** all Knowledge Graph documents listed above.
**Related Systems:** Engineering Toolkit (the CLI that runs all of this), Compatibility Layer (Section 7).
**Future Extension Points:** ES-007 Graph Builder is the critical path; everything else in this section is either already built or explicitly downstream of it.

---

## 7. Compatibility Layer

**Canonical Source:** [[Foundational Architecture]] (System Registry, Phase 1-3), [[Engine Registry]] (per-engine access method and dependency risk), [[The Orchestration Framework]] Ch. V (API Integration Roadmap).
**New Material:** the honest current-status table below — no prior document lists all ten integration surfaces side by side with implementation status.

| System | Status | Detail |
|---|---|---|
| **Local folders (the Vault)** | Live — canonical | System 1 per Foundational Architecture. Source of truth for everything. |
| **GitHub** | Live | `github.com/OmSadhiGuru/ALPHA.PROXIMA.CORE-`, synced via Obsidian Git plugin (auto-pull ~5 min). No CI, no LICENSE, no branch protection (Section 5). |
| **Claude** | Live | Current engine for LUMIAION (Constitutional Intelligence Core) and Chief Knowledge Architect, via Claude Code CLI + API. |
| **Codex — naming ambiguity, flagged not resolved:** | Unclear | "CODEX" is used throughout `11_OPERATIONS`/Engineering Toolkit as an **author persona** for Engineering-Office-produced documents (i.e., Claude operating in an engineering posture) — it is not a separate connected product. Separately, "Codex" in the Founder's LOOM brief and in general industry usage refers to OpenAI's code-focused model. Engine Registry's Chief Engineering Architect is currently **DeepSeek**, not OpenAI Codex. This document does not guess which is meant going forward — it is named here as an open item (see Open Questions). |
| **ChatGPT / GPT** | Manual invocation only | Chief Systems Architect (Engine Registry). Orchestration Framework Ch. V Phase 1 = manual invocation; Phase 2 (programmatic) not started. |
| **Gemini** | Manual invocation only | Chief Science Architect; ATHENA's primary engine. Same Phase 1 constraint. |
| **Perplexity** | Manual invocation only | Chief Research Architect; JERANIUM's primary engine; also Research Intelligence Office (function axis) and LOOM's Research stage owner. |
| **n8n** | Not implemented | Appears only as a forward-looking TODO in `OSG_LAUNCH/06_AUTOMATION/Automation Opportunities.md` and as a scope note in the Automation Standard. No workflow, no owner, no folder. |
| **Supabase** | Not implemented — zero references anywhere in the vault prior to this document | New integration surface. If adopted, note that Supabase (via `pgvector`) is a concrete candidate to fill the "Vector Database" placeholder already planned for Phase 2 in Foundational Architecture and the Knowledge Routing Protocol — this document does not decide that; it names the option. Requires a Concept Note before adoption per the Automation Standard's approval boundary. |
| **Google Drive** | Not implemented — zero references anywhere in the vault | No canonical owner, no planned phase. |
| **Notion** | Not implemented for Alpha Proxima | `ALPHA PROXIMA/NOTION COMMAND CENTER.md` and `OBSIDIAN VAULT.md` are both explicit `status: placeholder` legacy notes. Foundational Architecture lists Notion as "Planned — Phase 2" (Mission Control). **Separately**, `OSG_LAUNCH/01_NOTION_WORKSPACE/` has a real (early-stage) Notion architecture for OSG's own business operations — this is outside Alpha Proxima governance per OSG_LAUNCH's own README ("intentionally isolated"). Do not conflate the two. |

**Dependencies:** Foundational Architecture, Engine Registry, Automation Standard.
**Related Systems:** Self-Search Architecture (Section 6, Supabase/vector overlap), Governance System (Section 8, approval gate for any new integration).
**Future Extension Points:** resolve the Codex naming ambiguity; decide Supabase-as-vector-DB when Phase 2 begins; assign an owner if Drive or n8n integration is ever commissioned.

---

## 8. Governance System

**Canonical Source:** [[Vault Structure Convention]] (naming, versioning, documentation), [[Decision Routing Protocol]] (approval), [[Book III - Knowledge Integrity]] Art. IV + [[Artifact Registry]] (archive/lifecycle), [[Review Cycles Registry]] (update cycle), [[ADR Template]] + [[ADR-0001 - The Founding Decision]] + [[ADR-0002 - Reconciling the Four Institutional Taxonomies]] (decision record format, with two worked examples).
**New Material:** none. This is the most mature layer in the entire ecosystem — every mechanic the brief asks for already has a ratified, active canonical source. Restating it would itself violate the single-source-of-truth objective this document serves.

| Mechanic | Canonical Source | Status |
|---|---|---|
| Naming conventions | Vault Structure Convention (file naming table); `08_SYSTEMS/Engineering Standards/04 - File Naming Convention.md` | Active |
| Versioning rules | Vault Structure Convention (semantic versioning: Major/Minor/Patch); Artifact Registry (per-type versioning column) | Active |
| Documentation rules | Vault Structure Convention (required frontmatter, six required sections) | Active |
| Approval rules | Decision Routing Protocol (Class I-IV routing trees); Automation Standard (approval boundary); Ethics Council Charter (five Review Protocols) | Active |
| Archive rules | Vault Structure Convention ("never delete, archive instead"); Book III Art. IV (Revision Policy) | Active |
| Update cycle | Review Cycles Registry (Daily/Weekly/Monthly/Quarterly/Annual, each with owner + inputs + outputs) | Active |
| Decision record format | ADR Template; two worked examples now exist: ADR-0001 (Class I, founding) and ADR-0002 (Class II, this document's own taxonomy finding) | Active |

**One genuine gap surfaced, not fixed here:** Artifact Registry's 14 artifact types do not include a "Master Reference" type — this document's own `artifact_type: master-reference` (frontmatter, above) is new and not yet registered. Adding it is a Class III change to the Artifact Registry (its own governed document) and is logged as an Open Question, not performed unilaterally.

**Dependencies:** all sources in the table above.
**Related Systems:** every other section of this document depends on this one.
**Future Extension Points:** register the `master-reference` artifact type in Artifact Registry.

---

## 9. Implementation Roadmap

**Canonical Source:** Foundational Architecture's Phase 1-3, LUMIAION Architecture Spec's v0.1→v1.0 evolution path, Orchestration Framework Ch. V (API roadmap), EP-001's tool sequence — all of which already define a phased future. **New Material:** mapping the brief's Phase 0-7 labels onto actual current status (done / partial / not started) rather than treating all seven as future work.

| Phase | Brief's Label | Actual Status | What Remains |
|---|---|---|---|
| 0 | Foundation | **Done** | Book I-III ratified; ADR-0001 founding act complete. |
| 1 | Repository creation | **Done** | Vault = live GitHub repo, Vault Structure Convention enforced. Remaining: LICENSE, `.github/` CI (Section 5). |
| 2 | Knowledge schema | **Mostly done** | Node/Relationship Taxonomy ratified; Research Note/ADR/Concept Note/Implementation Note templates live. Remaining: adopt Section 4's extension block (`domain`, `department_owner`, `osg_interpretation`, `application`, `last_reviewed`). |
| 3 | Department setup | **Done** | SOHMA, ATHENA, VORTEX, JERANIUM chartered and engine-assigned (ADR-0001 §9). Remaining: Databases column in Section 3 is entirely unbuilt — none of the four departments has a dedicated data store yet. |
| 4 | Search/indexing | **Partial — current frontier** | Node Registry + Relationship Extractor built and run once (2026-07-03 snapshot, now stale — regenerate per Section 6). ES-007 Graph Builder is the next concrete step; ES-008/009/010 depend on it and are not started. |
| 5 | Automation | **Not started, but designed** | Automation Standard (ES-07) defines the approval boundary; Automation Queue Index lists 4 candidates, all `status: planned`. Zero scheduled jobs, zero n8n workflows, zero cron. |
| 6 | AI agent integration | **Manual only** | Orchestration Framework Phase 1 (manual invocation) is where every engine sits today. Phase 2 (programmatic orchestration) requires the four "Required" protocols the Orchestration Framework itself names as not yet formalized: Session Initiation Protocol, Session Closure Protocol, API Failure Recovery Protocol, Conflict Resolution Protocol. |
| 7 | Institutional publishing | **Not started for Alpha Proxima** | No public-facing publishing pipeline exists. `OSG_LAUNCH` has the closest analog (its own `00_REPOSITORY`, `03_MEDIA`, `05_CONTENT`), but is explicitly a separate, isolated business namespace — Alpha Proxima's own institutional publishing (e.g. a public Book I/II summary, a public Knowledge Graph explorer) has no owner or plan yet. |

**Sequencing rule, consistent with the Sprint System already defined in [[LUMIAION - Operating Manual (LOOM)]]:** one active phase-priority at a time. Given the table above, **Phase 4 (ES-007 Graph Builder) is the single highest-leverage next action** — every later phase either depends on it (5, 6) or is independent of it and can wait (7).

**Dependencies:** Foundational Architecture, LUMIAION Architecture Spec, Orchestration Framework, EP-001, Automation Queue Index.
**Related Systems:** Section 6 (Self-Search), Section 7 (Compatibility).
**Future Extension Points:** the four "Required" protocols named under Phase 6 are the concrete next documents to draft, in the same reconciled style as this one.

---

## Related Notes

- [[Alpha Proxima Core]]
- [[Book I - The Constitution]]
- [[Foundational Architecture]]
- [[The Orchestration Framework]]
- [[LUMIAION Architecture Spec v0.1]]
- [[Institutional Relationship Map]]
- [[Office Registry]]
- [[Engine Registry]]
- [[AI Council Registry]]
- [[Knowledge Graph Architecture v1.0]]
- [[Vault Structure Convention]]
- [[LUMIAION - Operating Manual (LOOM)]]
- [[ADR-0002 - Reconciling the Four Institutional Taxonomies]]

---

## Open Questions

- [ ] Resolve the Codex naming ambiguity (Section 7): is "Codex" ever intended to mean OpenAI's product, or should the vault rename the Engineering-Office author persona to avoid the collision?
- [ ] Register `master-reference` as a 15th Artifact Registry type (Section 8).
- [ ] Should Supabase (`pgvector`) be formally proposed as the Phase 2 Vector Database, or should that remain an open evaluation against other candidates?
- [ ] Draft the four "Required" protocols the Orchestration Framework names but does not yet contain: Session Initiation, Session Closure, API Failure Recovery, Conflict Resolution.
- [ ] Assign a real owner and folder to ES-007 (Graph Builder) so Phase 4 has a tracked next action rather than a named intention.
- [ ] Should `03_AI_COUNCIL/Agents/` and `10_TEMPLATES/Prompts/` be created via Concept Note (Section 5)?
- [ ] Resolve the [[Research Council]] placeholder gap via `CN-0001` (referenced, not owned, by this document).

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-07 | Founder / LUMIAION | Initial compilation as the Institutional Master Reference, consolidating existing canon per the Founder's explicit architecture principles; filed alongside [[ADR-0002 - Reconciling the Four Institutional Taxonomies]] to record the one cross-cutting inconsistency found rather than silently resolving it. |
