---
title: Founder Synthesis Standard
id: apx-ingestion-founder-synthesis-standard
department: LUMIAION
domain: ingestion
type: ingestion-standard
status: active
version: 1.0.0
created: 2026-07-10
updated: 2026-07-10
source: founder-request
tags: [ingestion, founder-synthesis]
related: [evidence-classification-standard.md, ../DESIGN/document-layout-standard.md, ../DESIGN/callout-standard.md, ../TEMPLATES/founder-synthesis.template.md]
owner: LUMIAION
---

# Founder Synthesis Standard

## Purpose

Define the fourth stage of the ingestion lifecycle: turning classified extractions into a durable, OSG-native principle, explicitly attributed to and authored by the Founder's own interpretive act — distinct from the raw evidence beneath it.

## Prerequisite

Every extraction entry feeding a Founder Synthesis must already carry a classification (`evidence-classification-standard.md`). A synthesis may draw on entries from more than one category, but must state which category each contributing entry belongs to.

## Rule

1. **Synthesis is not extraction.** A Founder Synthesis is explicitly interpretive — it is where the institution's own understanding is formed, not a restatement of the source.
2. **Synthesis is attributed.** Every Founder Synthesis document is marked `[!reflection]` or `[!founder-decision]` (`../DESIGN/callout-standard.md`) and records who performed the synthesis. If not the Founder personally, this must be stated — the standard is named for the constitutional role this stage answers to, not a claim that every instance is Founder-authored.
3. **Uncertainty is preserved, not resolved by authority.** A synthesis may state a confident conclusion, but it may not present a Speculative or Symbolic-derived claim as Empirical or Clinical simply because the Founder wrote it. Classification categories from the contributing extractions carry forward into the synthesis.
4. **Clinical-derived syntheses are gated.** Any synthesis drawing on a Clinical-classified extraction is automatically routed to Ethics & Evidence Council review before it may proceed to a public-facing OSG Knowledge Object (`ingestion-approval-gates.md`).
5. **The synthesis becomes the durable principle**, in the sense already established by `../KNOWLEDGE/README.md`'s OSG Principle stage: *"the principle must be reusable outside the original source context."* A Founder Synthesis that only restates the source in different words has not yet reached this bar.

## Output

A Founder Synthesis document (`../TEMPLATES/founder-synthesis.template.md`), which becomes the direct input to the OSG Knowledge Object stage — using `../TEMPLATES/designed-knowledge-object.template.md` (Sprint 1, Knowledge Design System) as the target format going forward. `../TEMPLATES/osg-knowledge-object.template.md` remains referenced by `../AUTOMATIONS/drive-sync-spec.md` as the original target format; reconciling the two templates is an unresolved decision (`INGESTION/README.md`).

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-10 | Claude (Repository Architect / Knowledge Pipeline Designer) | Initial Founder Synthesis Standard, Sprint 3. |
