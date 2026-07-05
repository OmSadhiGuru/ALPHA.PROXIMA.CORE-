# Awaken the Inner Guru
## Reference Implementation Blueprint — OSG Academy Flagship

*This is the **reference implementation** of an OSG course — the institutional benchmark that every future OSG course is measured against. It applies the **OSG Learning Standard (OLS) v1.1** faithfully and does not modify it. It contains architecture only: no lesson scripts, no marketing, no worksheets, no meditations, no content.*

**Course:** Awaken the Inner Guru
**Document class:** Reference Implementation Blueprint (institutional benchmark)
**Governing standard:** OSG Learning Standard (OLS) v1.1 — immutable
**Status:** Living institutional reference (v1.1.0) — pending Gate-1 approval
**Purpose:** Defines the **minimum quality standard** for every OSG course. Not the only way to build a course — the floor, not the ceiling. Future courses may innovate beyond it but may never violate the OLS, and are reviewed against it before publication (§16).
**Owner:** Chief Learning Architect, OSG Academy
**Relationship to prior artifacts:** Incorporates the *Awaken the Inner Guru — Production Blueprint v1.1* (workbook/journal/community/instructor/production detail and the §11 Bilingual FR/EN Production Model) **by reference**, and extends it to reference grade with the Transformation Map, Learning Validation, Knowledge Library Integration, Personalization Layer, AI Integration, and Future Evolution layers.
**Languages:** French (source) → English (transcreated). See Production Blueprint §11.

**Labeling (OLS §2.4):** `[E]` Evidence-based · `[R]` Reflective practice · `[F]` Contemplative/Personal framework.

**Course philosophy (governing constraint):** *The course does not provide answers.* It cultivates the learner's own capacity to reflect, observe, integrate, and develop judgment. Transformation comes through structured reflection, deliberate practice, and community — never dependency. Every architectural decision below serves that end.

---

## Table of Contents
1. Executive Overview
2. Transformation Map
3. Course Roadmap
4. Weekly Blueprint (Week 0 → Week 8)
5. Lesson Inventory
6. Learning Validation
7. Knowledge Library Integration
8. Personalization Layer
9. Community Layer
10. Workbook Blueprint
11. Journal Blueprint
12. Production Pipeline
13. AI Integration (YUNA · LUMIAION · Axiom Nexus · Living Genome · Knowledge Library)
14. Future Evolution
15. Success Metric & Compliance
16. Reference Implementation Governance (living reference)

---

## 1. Executive Overview

**Mission.** To help each learner build a reliable, discerning relationship with their own inner wisdom — cultivating the *capacity* to reflect, observe, and judge for themselves, rather than delivering answers to be consumed.

**Vision.** A generation of people who consult their own inner guidance with discernment and humility — who have exchanged dependence on external authority for a grounded, examined inner authority. *Awaken the Inner Guru* is the reference course that proves OSG's method and sets the pattern every OSG course follows.

**Transformation promise.**
> In 8 weeks — and a 90-day integration — you move from second-guessing yourself and seeking answers outside → to a calm, discerning relationship with your own inner wisdom that you can consult, and trust, for the rest of your life.

**Ideal student.** A reflective adult (≈30–55) who is capable and self-aware yet chronically defers to external authority, over-researches decisions, or doubts their own knowing. Has likely done some inner work and now wants to *trust themselves* — with structure and discernment, not naïve "follow your gut" advice.
*Not for:* those seeking a quick fix or an authority to decide for them (the course does the opposite); anyone in acute mental-health crisis (stated plainly; referred out — OSG is education, not therapy).

**Prerequisites.** None. Openness to reflection and ~15 min/day of practice. Beginners welcome; prior practice deepens but is not required.

**Learning outcomes.** By completion the learner can: (1) quiet mental noise enough to perceive inner signal `[E][F]`; (2) observe thoughts/reactions without being run by them `[E][F]`; (3) discern genuine intuition from fear, impulse, conditioning `[E][F]`; (4) recognize and work with the resistance that blocks self-trust `[R][F]`; (5) use inner-guidance practices to consult wisdom deliberately `[F]`; (6) ground guidance in examined values `[E][R]`; (7) apply the integrated method under real-life pressure; (8) sustain a lifelong inner-guru practice independently.

**Course duration.** Week 0 (Orientation) + Weeks 1–8 (core) + Graduation + 90-Day Integration. Active course: 8 weeks. Full arc to autonomy: ~5 months.

**Weekly commitment.** ~2–3 hrs/week: lesson video(s) + workbook + daily practice (~15 min) + one community/live touchpoint.

**Completion criteria.** A learner completes when they have: (a) engaged all 8 weekly modules; (b) completed the daily practice at a defined consistency threshold (self-attested + logged); (c) completed the three Progress Reviews; (d) produced the "after" Inner Guru Map; (e) written a personal maintenance plan; (f) participated in community at a minimum threshold (≥1 post/week average). Completion is **evidence of engagement and behavioral practice**, not a passed exam — consistent with the philosophy.

---

## 2. Transformation Map

The complete learner transformation, mapped to the course arc. Each stage names the learner's state, what shifts, and where it happens.

```
BEGINNING STATE  → "I don't trust myself; the answers are out there."
      ↓            (Week 0 — honest baseline)
DISCOVERY        → "There is an inner signal beneath the noise — and I can perceive it."
      ↓            (Weeks 1–2 — quieting, witnessing)
REFLECTION       → "I can observe and question my own reactions, and discern their source."
      ↓            (Weeks 3–4 — discernment, resistance)
PRACTICE         → "I have repeatable ways to consult my inner wisdom."
      ↓            (Weeks 5 — the guidance practices)
INTEGRATION      → "My guidance is grounded in what I actually value."
      ↓            (Week 6 — values & inner authority)
APPLICATION      → "I act from inner authority under real pressure."
      ↓            (Week 7 — real-world application)
AUTONOMY         → "I have an ongoing relationship with my inner guru, and I sustain it myself."
                   (Week 8 + 90-Day Integration — lifelong practice)
```

| Stage | Learner state | Mechanism | Where |
|-------|--------------|-----------|-------|
| Beginning State | External-authority dependence; self-doubt | Honest baseline | Week 0 |
| Discovery | Realizes inner signal exists and is perceivable | Stillness + witnessing | Weeks 1–2 |
| Reflection | Observes and discerns own inner states | Discernment + shadow work | Weeks 3–4 |
| Practice | Repeatable access to inner guidance | The four practices | Week 5 |
| Integration | Guidance grounded in values | Values + inner authority | Week 6 |
| Application | Acts from inner authority in real life | Applied integrated method | Week 7 |
| Autonomy | Sustains the relationship independently | Maintenance rhythm + 90-day | Week 8 + Integration |

**Design note:** the arc deliberately ends in **Autonomy**, not completion. The 90-Day Integration exists because durable behavioral change and true autonomy form *after* the teaching ends. `[E — habit formation and durable change require post-instruction practice]`

---

## 3. Course Roadmap

Per OLS Course Architecture (§4), extended with Week 0 and the 90-Day Integration.

```
ORIENTATION (WEEK 0) — "Meeting the Inner Guru"
   baseline map · how to learn here · promise & boundary · first practice
        ↓
WEEK 1  The Noise and the Signal            (Discovery)
WEEK 2  The Inner Witness                   (Discovery → Reflection)
   ── Progress Review #1 ──
WEEK 3  Intuition & Discernment             (Reflection)
WEEK 4  Shadow & Resistance                 (Reflection → Practice)
   ── Progress Review #2 (midpoint) ──
WEEK 5  The Practices of Inner Guidance      (Practice)
WEEK 6  Values & Inner Authority             (Integration)
   ── Progress Review #3 ──
WEEK 7  Discernment in Action                (Application)
WEEK 8  Living from the Inner Guru           (Autonomy)
        ↓
GRADUATION — before/after map · maintenance plan · celebration · testimonial
        ↓
90-DAY INTEGRATION — structured monthly check-ins · community · practice sustainment
        ↓
NEXT LEARNING PATH → Coaching Container · Community tier · Advanced course
```

**90-Day Integration architecture:** three monthly milestones (Day 30 / 60 / 90), each with a self-review against the maintenance plan, a community re-engagement prompt, and a "guidance-in-the-wild" reflection (a real decision made from inner authority). Optional group integration calls. This is where Autonomy consolidates.

---

## 4. Weekly Blueprint (Week 0 → Week 8)

*For every week: purpose · transformation · knowledge / understanding / behavioral / reflection objectives · skills · required assets · estimated time · completion evidence · success criteria. Assets are named at type level; full asset production detail = Production Blueprint §9.*

---

### WEEK 0 — Orientation: "Meeting the Inner Guru"
- **Purpose:** Orient, install the first small win, take an honest baseline.
- **Transformation:** "I hope this works" → "I know how to work this, and I've begun."
- **Knowledge:** the course map; the OSG method; the evidence/framework promise.
- **Understanding:** that the course builds capacity, not dependency.
- **Behavioral:** completes setup; does first 5-min stillness.
- **Reflection:** names where self-trust stands today.
- **Skills:** how to reflect/journal/practice the OSG way.
- **Assets:** welcome video; orientation workbook section; baseline self-assessment (Inner Guru Map); first stillness audio; community intro prompt.
- **Time:** ~60–75 min.
- **Completion evidence:** baseline Map submitted; intro posted; first practice logged.
- **Success criteria:** learner can state their starting point and has completed one practice within 24h.

---

### WEEK 1 — The Noise and the Signal *(Discovery)*
- **Purpose:** Quiet mental noise enough to notice inner signal.
- **Transformation:** a mind too loud to hear itself → moments of genuine quiet.
- **Knowledge:** mental noise vs. signal `[F]`; attention is trainable `[E]`.
- **Understanding:** why stillness precedes listening.
- **Behavioral:** installs daily 10-min stillness.
- **Reflection:** recognizes habitual noise patterns.
- **Skills:** stillness practice; noticing inner-state texture.
- **Assets:** 2 lesson videos + practice video; stillness audio; workbook pages; journal prompts; community prompt.
- **Time:** ~2.5 hrs.
- **Completion evidence:** ≥5 days practice logged; noise inventory done.
- **Success criteria:** learner reports at least one experienced moment of inner quiet.

---

### WEEK 2 — The Inner Witness *(Discovery → Reflection)*
- **Purpose:** Observe thoughts/reactions without being swept by them.
- **Transformation:** inside every thought → watching thought from a steadier vantage.
- **Knowledge:** the Inner Witness `[F]`; metacognition `[E]`; the stimulus-response pause `[E]`.
- **Understanding:** "I notice anger" ≠ "I am angry."
- **Behavioral:** daily witnessing; one real-world pause.
- **Reflection:** distinguishes identification from observation.
- **Skills:** witnessing; affect labeling `[E]`.
- **Assets:** 2 lesson videos + practice video; witnessing audio; workbook; journal; community prompt; **Progress Review #1**.
- **Time:** ~2.5 hrs.
- **Completion evidence:** witness checkpoints logged; Progress Review #1 completed.
- **Success criteria:** learner can describe a moment they observed a reaction instead of enacting it.

---

### WEEK 3 — Intuition & Discernment *(Reflection)*
- **Purpose:** Distinguish genuine intuition from fear, impulse, conditioning.
- **Transformation:** "can't tell gut from anxiety" → working discernment.
- **Knowledge:** what intuition is/isn't — evidence and limits `[E]`; felt signatures `[F]`.
- **Understanding:** discernment is a skill, not a gift.
- **Behavioral:** applies a discernment protocol to a real prompt.
- **Reflection:** personal map of how fear vs. wisdom *feel*.
- **Skills:** discernment protocol; somatic noticing.
- **Assets:** 2 lesson videos + practice video; discernment worksheet; case study; workbook; journal; community prompt.
- **Time:** ~2.5–3 hrs.
- **Completion evidence:** discernment protocol applied and recorded.
- **Success criteria:** learner correctly distinguishes a fear-driven from a wisdom-driven prompt in their own life.

---

### WEEK 4 — Shadow & Resistance *(Reflection → Practice)*
- **Purpose:** Recognize and work with the resistance blocking self-trust.
- **Transformation:** unconsciously run by blocks → meeting them consciously.
- **Knowledge:** resistance/self-sabotage `[R]`; shadow as framework `[F]`.
- **Understanding:** self-trust is courage, not certainty.
- **Behavioral:** names and works with one core block.
- **Reflection:** identifies the learner's central self-trust block.
- **Skills:** resistance-mapping; compassionate self-inquiry `[E — self-compassion]`.
- **Assets:** 2 lesson videos + practice video; resistance worksheet; contemplation audio; workbook; journal; community prompt; **Progress Review #2**. **Boundary callout:** not therapy; refer out.
- **Time:** ~3 hrs.
- **Completion evidence:** resistance map done; Progress Review #2 completed.
- **Success criteria:** learner can name their core block and one compassionate response to it.

---

### WEEK 5 — The Practices of Inner Guidance *(Practice)*
- **Purpose:** Deliberately consult inner wisdom via defined practices.
- **Transformation:** hoping for insight → a repeatable method for accessing it.
- **Knowledge:** four practices — stillness, written inquiry, contemplative sitting, symbolic/imaginal inquiry `[F]`; journaling as thinking `[E]`.
- **Understanding:** guidance is accessed by asking and listening, not forcing.
- **Behavioral:** takes a real question through the full process.
- **Reflection:** discovers which practice fits best.
- **Skills:** inner dialogue; contemplative & symbolic inquiry.
- **Assets:** 2–3 lesson videos + practice video; guided inquiry audio; inner-dialogue worksheet; templates; workbook; journal; community prompt.
- **Time:** ~3 hrs.
- **Completion evidence:** one full inner-guidance session recorded.
- **Success criteria:** learner completes a guidance session and can name what surfaced.

---

### WEEK 6 — Values & Inner Authority *(Integration)*
- **Purpose:** Ground guidance in examined values so trust is discerning, not impulsive.
- **Transformation:** "trust yourself" as slogan → inner authority grounded in values.
- **Knowledge:** values clarification `[E]`; inner authority vs. self-will `[F]`.
- **Understanding:** intuition + discernment + values = grounded authority.
- **Behavioral:** makes a real decision via the full integrated method.
- **Reflection:** clarifies deep vs. borrowed values.
- **Skills:** values-based decision practice; integration.
- **Assets:** 2 lesson videos + practice video; values worksheet; integration template; workbook; journal; community prompt; **Progress Review #3**.
- **Time:** ~2.5–3 hrs.
- **Completion evidence:** integrated decision recorded; values clarified.
- **Success criteria:** learner makes one decision they can trace to intuition + discernment + values.

---

### WEEK 7 — Discernment in Action *(Application)*
- **Purpose:** Apply the integrated method under real-life pressure and complexity.
- **Transformation:** practicing in calm → applying under real stakes.
- **Knowledge:** applying the full method (stillness → witness → discern → consult → values-check → act) in hard, ambiguous situations.
- **Understanding:** autonomy means using the method *when it's difficult*.
- **Behavioral:** applies the method to a genuinely consequential real decision.
- **Reflection:** notices where the method held and where old patterns pulled.
- **Skills:** applied integration; self-correction under pressure.
- **Assets:** 2 lesson videos + practice video; application worksheet; case study; workbook; journal; community prompt.
- **Time:** ~2.5–3 hrs.
- **Completion evidence:** a real, higher-stakes application documented.
- **Success criteria:** learner applies the full method to a consequential decision and reflects on the result.

---

### WEEK 8 — Living from the Inner Guru *(Autonomy)*
- **Purpose:** Assemble a sustainable lifelong system and mark the transformation.
- **Transformation:** "I took a course" → "I have an ongoing relationship with my inner guru."
- **Knowledge:** personal daily/weekly/quarterly rhythm; habit design `[E]`; relapse-recovery; the inner guru as lifelong relationship `[F]`.
- **Understanding:** autonomy is sustained by rhythm, not motivation.
- **Behavioral:** writes and begins a personal maintenance plan.
- **Reflection:** completes the "after" Inner Guru Map beside the "before."
- **Skills:** designing a maintenance rhythm; quarterly self-review.
- **Assets:** 2 lesson videos; maintenance-plan template; before/after map; graduation video; testimonial prompt; Next Path overview.
- **Time:** ~2–2.5 hrs.
- **Completion evidence:** maintenance plan written; after-Map completed; graduation share posted.
- **Success criteria:** learner has a documented, personal, sustainable practice and can articulate their transformation.

---

## 5. Lesson Inventory

*Every lesson follows the OLS 12-part Lesson Blueprint in production. Below: the lesson-specific architecture, plus two reference-grade fields — **Knowledge Library Concepts** (canonical IDs from §7) and **Future AI Opportunities** (how AI may later support this lesson, §13). No scripts.*

**Legend:** Obj = objective · Dur · PE = practice · M = meditation/contemplation · J = journal · C = community · HW = homework · KL = Knowledge nodes · AI = future AI opportunity.

---

**Week 0 — Orientation**

**L0.1 Welcome & How This Works** — Obj: understand structure & method · Dur 15m · PE: set up practice space · J: "Why am I here?" · M: — · C: intro post · HW: complete setup · KL: KL-000 (OSG Method), KL-025 (Learner Sovereignty) · AI: AI onboarding concierge answers "how does this work" questions.

**L0.2 Meeting Your Inner Guru (Baseline)** — Obj: define inner guru; baseline self-trust `[F]` · Dur 30m · PE: baseline Inner Guru Map · J: "Where do I look for answers, and why?" · M: 5-min stillness `[F]` · C: "One question for my inner guru by Week 8" · HW: repeat stillness · KL: KL-024 (The Inner Guru), KL-001 (Attention/Noise) · AI: AI captures baseline into the learner's Living Genome profile (future).

---

**Week 1 — The Noise and the Signal**

**L1.1 Why You Can't Hear Yourself** — Obj: understand noise vs. signal `[E][F]` · Dur 25m · PE: noise inventory · J: "What does my noise sound like?" · M: 10-min stillness · C: "Your loudest noise" · HW: daily stillness · KL: KL-001 (Attention/Noise, Core), KL-002 (Stillness, Core) · AI: AI practice-reminder + noise-pattern reflection.

**L1.2 The Practice of Stillness** — Obj: install daily stillness `[E][F]` · Dur 25m · PE: design practice slot · J: "What did the quiet show me?" · M: 10-min stillness · C: "A moment of quiet" · HW: stillness daily · KL: KL-002 (Stillness), KL-004 (Metacognition, supporting) · AI: AI consistency tracking + gentle nudge.

---

**Week 2 — The Inner Witness**

**L2.1 The One Who Watches** — Obj: access the witnessing stance `[E][F]` · Dur 30m · PE: 3 daily witness checkpoints · J: "A thought I watched" · M: witnessing meditation `[F]` · C: "What did stepping back show?" · HW: witness daily · KL: KL-003 (Inner Witness, Core), KL-004 (Metacognition, Core) · AI: AI reflective questioner deepens witnessing journal.

**L2.2 Labeling and the Pause** — Obj: use labeling to create the pause `[E]` · Dur 25m · PE: label states 3×/day · J: "A moment I paused" · M: short witnessing sit · C: "Where a pause helped" · HW: practice the pause · KL: KL-005 (Stimulus-Response Pause, Supporting), KL-006 (Affect Labeling, Supporting) · AI: AI surfaces the learner's pause-vs-react patterns over time.

---

**Week 3 — Intuition & Discernment**

**L3.1 What Intuition Actually Is** — Obj: understand intuition accurately `[E]` · Dur 30m · PE: intuition audit · J: "Right vs. wrong intuition" · M: body-listening `[F]` · C: "An intuition story" · HW: notice prompts without acting · KL: KL-007 (Intuition, Core), KL-021 (Intuition research limits, Future Research) · AI: AI helps categorize past-decision audit.

**L3.2 Fear, Impulse, or Wisdom?** — Obj: discern wisdom from fear/impulse `[E][F]` · Dur 30m · PE: apply discernment protocol · J: "How fear vs. wisdom feels" · M: discernment contemplation `[F]` · C: "Your tell for fear-as-intuition" · HW: run one decision through discernment · KL: KL-008 (Discernment, Core), KL-009 (Fear/Impulse/Wisdom, Core) · AI: AI discernment-companion walks the protocol interactively (future).

---

**Week 4 — Shadow & Resistance**

**L4.1 Why You Don't Trust Yourself** — Obj: identify resistance blocking self-trust `[R][F]` · Dur 30m · PE: resistance map · J: "When did I learn not to trust myself?" · M: compassionate self-inquiry `[F]` · C: "Name one block" · HW: observe the block · KL: KL-010 (Resistance, Supporting), KL-011 (Shadow, Advanced) · AI: AI reflects patterns back non-judgmentally; refers out on distress signals.

**L4.2 Meeting the Block** — Obj: work with a core block compassionately `[R][F]` · Dur 30m · PE: compassion practice · J: "What does my resistance protect/cost?" · M: contemplation `[F]` · C: mid-course turning-point share · HW: one compassionate act · KL: KL-011 (Shadow), KL-012 (Self-Compassion, Supporting), KL-022 (Reconsolidation link, Future Alpha Proxima) · AI: **boundary-aware** support only; escalates to human/professional on risk.

---

**Week 5 — The Practices of Inner Guidance**

**L5.1 Four Ways to Ask Within** — Obj: learn four guidance practices `[F][E]` · Dur 35m · PE: try all four · J: "Which met me most?" · M: guided inner-inquiry `[F]` · C: "Which practice calls you?" · HW: pick one; daily · KL: KL-013 (Inner Guidance Practices, Core), KL-014 (Contemplative Inquiry, Advanced), KL-015 (Symbolic Inquiry, Advanced), KL-016 (Journaling-as-thinking, Supporting) · AI: AI journaling partner scaffolds written inquiry.

**L5.2 Asking a Real Question** — Obj: full guidance process on a real question `[F]` · Dur 30m · PE: full session · J: structured inner dialogue · M: extended guided inquiry `[F]` · C: "What surfaced (opt-in)" · HW: repeat with a 2nd question · KL: KL-013, KL-016 · AI: AI helps frame the question and capture the response (never generates the answer).

---

**Week 6 — Values & Inner Authority**

**L6.1 What You Actually Value** — Obj: clarify core values `[E][R]` · Dur 30m · PE: values clarification · J: "Mine vs. inherited values" · M: values contemplation `[F]` · C: "A value you're reclaiming" · HW: notice aligned/violating choices · KL: KL-017 (Values Clarification, Core) · AI: AI values-sorter reflects patterns; learner decides.

**L6.2 Standing in Inner Authority** — Obj: integrate into grounded authority `[E][F]` · Dur 30m · PE: full integrated method · J: "A decision from inner authority" · M: contemplation `[F]` · C: "Where you stood in authority" · HW: live one decision from authority · KL: KL-018 (Inner Authority, Core), KL-019 (Integrated Decision Method, Core) · AI: AI decision-companion runs the integrated method as a guided flow (future).

---

**Week 7 — Discernment in Action**

**L7.1 Under Pressure** — Obj: apply the method in a hard, ambiguous situation · Dur 30m · PE: applied case · J: "Where the method held / old patterns pulled" · M: grounding sit `[F]` · C: "A real application this week" · HW: apply to a live situation · KL: KL-019 (Integrated Decision Method), KL-009 · AI: AI scenario-rehearsal partner for pressure-testing (future).

**L7.2 A Real Decision** — Obj: apply the full method to a consequential decision · Dur 30m · PE: full applied decision · J: "The decision & its result" · M: contemplation `[F]` · C: share the application · HW: complete & reflect · KL: KL-019, KL-018 · AI: AI after-action reflection to consolidate learning.

---

**Week 8 — Living from the Inner Guru**

**L8.1 Your Inner Operating Rhythm** — Obj: assemble a sustainable rhythm `[E][F]` · Dur 30m · PE: write maintenance plan · J: "What rhythm will I keep?" · M: integrative sit `[F]` · C: "Your plan in one line" · HW: run the rhythm · KL: KL-020 (Habit Design/Maintenance, Supporting), KL-023 (Quarterly Self-Review, Supporting) · AI: AI maintenance-rhythm reminders + quarterly-review prompts.

**L8.2 Living from the Inner Guru (Graduation)** — Obj: mark transformation; step into lifelong practice `[F]` · Dur 30m · PE: after Inner Guru Map · J: "Who was I; who am I now?" · M: closing contemplation `[F]` · C: graduation + testimonial · HW: begin maintenance; choose Next Path · KL: KL-024 (Inner Guru), KL-025 (Learner Sovereignty) · AI: AI graduation summary from the learner's own journey data; hands off to 90-day integration cadence.

**Totals:** 18 lessons (Week 0: 2 · Weeks 1–8: 16) · 9 module themes across the transformation arc.

---

## 6. Learning Validation

*For every week: what students should KNOW · UNDERSTAND · PRACTICE · which BEHAVIORS change · and the OBSERVABLE EVIDENCE of successful learning. This is the assessment architecture — behavioral and reflective, never an exam.*

| Week | Should KNOW | Should UNDERSTAND | Should PRACTICE | BEHAVIOR change | OBSERVABLE EVIDENCE |
|------|------------|-------------------|-----------------|-----------------|---------------------|
| 0 | The method & promise | It builds capacity, not dependency | Setup + first stillness | Begins engaging | Baseline Map + intro post + 1 practice logged |
| 1 | Noise vs. signal; attention is trainable | Stillness precedes listening | Daily stillness | Starts a daily practice | ≥5 practice logs; noise inventory |
| 2 | The Witness; the pause | Observation ≠ identification | Witnessing + labeling | Pauses before some reactions | Witness logs; a described real pause; Review #1 |
| 3 | What intuition is/isn't | Discernment is a skill | Discernment protocol | Tests prompts before acting | A recorded discernment of a real prompt |
| 4 | Resistance & shadow (framework) | Self-trust is courage, not certainty | Compassionate self-inquiry | Meets a block consciously | Resistance map; a compassionate response; Review #2 |
| 5 | The four practices | Guidance is asked for, not forced | A full guidance session | Consults inner wisdom deliberately | A recorded full inner-guidance session |
| 6 | Values clarification; inner authority | Authority = intuition+discernment+values | Integrated decision | Decides from grounded authority | An integrated decision traced to values; Review #3 |
| 7 | Applying the method under pressure | Autonomy = using it when hard | Applied method, real stakes | Acts from authority under pressure | A documented consequential application |
| 8 | Rhythm & maintenance | Autonomy is sustained by rhythm | Designing the maintenance plan | Commits to ongoing practice | Maintenance plan; after-Map; graduation share |

**Validation principle:** evidence is **behavioral and self-authored** (logs, maps, documented real decisions, community shares), never a test score — because the capacity being built is internal. The three Progress Reviews (Weeks 2/4/6) are structured self-assessments against the transformation promise.

---

## 7. Knowledge Library Integration

Every concept the course teaches becomes a canonical **Knowledge Node** in the OSG Knowledge Library, with a stable ID reusable across all future courses. IDs are permanent; classification may evolve.

**Classification:** **Core** (central to the course) · **Supporting** (enabling) · **Advanced** (deeper/optional) · **Future Research** (open questions OSG may investigate) · **Future Alpha Proxima** (bridges to the Alpha Proxima research institute — consciousness/memory/learning programs).

| ID | Concept | Class | Tag | Cross-links |
|----|---------|-------|-----|-------------|
| KL-000 | The OSG Method (Transformation Path) | Core | — | All courses |
| KL-001 | Attention / Mental Noise | Core | `[E][F]` | — |
| KL-002 | Stillness Practice | Core | `[F]` | — |
| KL-003 | The Inner Witness | Core | `[F]` | KL-004 |
| KL-004 | Metacognition | Core | `[E]` | **Future Alpha Proxima → RP-001 (Consciousness)** |
| KL-005 | Stimulus–Response Pause | Supporting | `[E]` | KL-006 |
| KL-006 | Affect Labeling | Supporting | `[E]` | — |
| KL-007 | Intuition | Core | `[E][F]` | KL-021 |
| KL-008 | Discernment | Core | `[F]` | KL-009 |
| KL-009 | Fear / Impulse / Wisdom Distinction | Core | `[F]` | KL-008 |
| KL-010 | Resistance / Self-Sabotage | Supporting | `[R]` | KL-011 |
| KL-011 | Shadow (framework) | Advanced | `[F]` | — |
| KL-012 | Self-Compassion | Supporting | `[E]` | — |
| KL-013 | Inner Guidance Practices | Core | `[F]` | KL-014, KL-015, KL-016 |
| KL-014 | Contemplative Inquiry | Advanced | `[F]` | — |
| KL-015 | Symbolic / Imaginal Inquiry | Advanced | `[F]` | — |
| KL-016 | Journaling as Thinking | Supporting | `[E]` | — |
| KL-017 | Values Clarification | Core | `[E]` | — |
| KL-018 | Inner Authority | Core | `[F]` | KL-019 |
| KL-019 | Integrated Decision Method | Core | `[E][F]` | KL-007, KL-008, KL-017 |
| KL-020 | Habit Design / Maintenance | Supporting | `[E]` | KL-023 |
| KL-021 | Intuition — Research Limits | Future Research | `[E]` | KL-007 |
| KL-022 | Memory Reconsolidation & Inner Change | Future Alpha Proxima | `[E]` | **→ RP-002 (Memory)** |
| KL-023 | Quarterly Self-Review | Supporting | `[R]` | KL-020 |
| KL-024 | The Inner Guru (framework) | Core | `[F]` | — |
| KL-025 | Learner Sovereignty | Core | `[F]` | KL-000 |
| KL-026 | Structured Reflection & Durable Change | Future Alpha Proxima | `[E]` | **→ RP-003 (Learning)** |

**Institutional value:** because concepts carry stable IDs, (a) future courses reuse nodes instead of re-teaching from scratch; (b) the Knowledge Library becomes a cross-course graph; (c) the *Future Alpha Proxima* nodes are the deliberate bridges where OSG's applied teaching connects to the research institute's programs — kept clearly labeled and separate, never conflated.

---

## 8. Personalization Layer

Every activity can be delivered in alternative formats **without changing the learning objective.** Only the *experience* adapts; the *outcome* is identical. This makes the course accessible across learning preferences, accessibility needs, and (later) AI-personalized delivery.

| Core activity | Visual | Audio | Reading | Writing | Conversation | Kinesthetic | Reflection |
|---------------|--------|-------|---------|---------|--------------|-------------|-----------|
| **Teaching** | Diagram/animation of the model | Audio lesson | Transcript/essay | Note-taking template | Discuss in community/AI | Walk-and-listen | Post-teaching reflection prompt |
| **Stillness** | Visual anchor/candle | Guided audio | Written instructions | Practice log | Group sit | Body-scan/breath | "What did the quiet show?" |
| **Witnessing** | Visual metaphor | Guided audio | Reading on metacognition | Witness journal | Buddy debrief | Movement-based noticing | Checkpoint reflection |
| **Discernment** | Fear/wisdom map graphic | Audio walkthrough | Case study text | Discernment worksheet | Talk it through | Somatic/felt-sense scan | Felt-difference reflection |
| **Guidance practice** | Symbolic imagery | Guided inquiry audio | Written inquiry method | Inner-dialogue writing | Spoken inner dialogue | Walking contemplation | "Which practice met me?" |
| **Values** | Values card-sort visual | Audio contemplation | Values reading | Values worksheet | Values conversation | Embodied values exercise | Deep/borrowed reflection |
| **Integration/Decision** | Decision-flow diagram | Audio guide | Method reading | Integration template | Decision dialogue | Enact/roleplay the decision | Post-decision reflection |

**Rule (OLS-aligned):** the **learning objective and the Transformation-Path stage are invariant** across formats. Personalization changes modality, never the destination. At launch, offer 2–3 formats per activity (typically audio + reading + writing); AI-driven per-learner adaptation is a future upgrade (§13) that requires no redesign because objectives are already format-independent.

---

## 9. Community Layer

Per OLS §10 and Production Blueprint §7 (full weekly table there). Architecture:

- **Weekly discussion** — one transcreated prompt per week, per language space (Production Blueprint §11.6).
- **Peer accountability** — buddy pairing within language; weekly practice check-in threads.
- **Live session objectives** — per week (welcome/orient → teach stillness → witnessing → discernment → shadow-held-safely → group inquiry → integration → graduation), FR/EN sessions.
- **Celebration** — shared bilingual Wins space; mid-course turning-point share (Week 4); public small-win recognition.
- **Graduation** — Week 8 graduation share + testimonial; celebrated community-wide.
- **90-Day Integration** — monthly re-engagement prompts and optional integration calls sustain community past graduation.

Community rules (OLS-wide): confidentiality; support-don't-fix; first post in 48h; personal welcome; celebrate publicly/correct privately; refer crises to professionals.

---

## 10. Workbook Blueprint (structure only)

Architecture per Production Blueprint §5 (full detail there). Reference structure: front matter (how-to + evidence/framework key + baseline Inner Guru Map) → per-week sections (objective, lesson worksheets, reflection pages, practical exercise scaffolds, weekly review) → recurring instruments (Discernment, Inner-Dialogue, Values, Integrated-Decision, Maintenance-Plan templates) → progress tracking (daily practice log ×8 weeks, 3 Progress Reviews, before/after Map) → **90-day integration section** (Day 30/60/90 review pages) → bilingual glossary appendix. Separate full FR and EN editions, shared design system (Production Blueprint §11.4). *No content — structure only.*

---

## 11. Journal Blueprint (structure only)

Architecture per Production Blueprint §6. Reference structure: daily prompts (sequenced by weekly theme) → weekly deep prompts → milestone reflections (Weeks 2/4/6) → **Week-7 application reflection** → end-of-course reflection → **90-day integration entries (Day 30/60/90)** → free inner-dialogue overflow pages. FR/EN editions, prompts transcreated (Production Blueprint §11). *No content — architecture only.*

---

## 12. Production Pipeline

Everything required before any recording (OLS §14; full checklist in Production Blueprint §9). Reference-grade readiness set:

- **Instructional:** approved blueprint (this doc); 18 lesson scripts to the 12-part Lesson Blueprint; instructor stories; research references for every `[E]` node.
- **Slides & graphics:** Transformation Path; Noise-vs-Signal; Witness/Pause; Fear-Impulse-Wisdom map; Four Practices; Integrated Decision flow; Rhythm graphic; per-lesson title/objective slides.
- **Visuals & animations:** model animations (Transformation Path, decision flow); the personalization visual variants (§8).
- **Research:** compiled reference list; every `[E]` claim sourced; every `[F]` claim labeled.
- **Examples & stories:** 1–2 per week (Production Blueprint §8).
- **Audio:** native FR + EN meditations/contemplations (per lesson M); audio teaching versions.
- **Downloads:** workbook, journal (both editions), templates, quick-start, practice-setup guide, resource library.
- **Graphics/assets:** bilingual subtitle files per video; termbase-locked terminology.
- **Systems:** course platform (week-gated); community spaces; progress instruments; onboarding emails; **Knowledge Node IDs registered in the Knowledge Library**; **language metadata populated** (Production Blueprint §11.8).

**Gate rule:** nothing is recorded until the full readiness set exists and Gate-1 (blueprint) is approved. Per-lesson Gate-2 (OLS Compliance QC + translation-accuracy QC) precedes filming each lesson.

---

## 13. AI Integration (future compatibility without redesign)

The blueprint is architected so the following systems can plug in **later without any redesign**, because the course already exposes the structured surfaces they need: stable Knowledge Node IDs (§7), format-independent objectives (§8), behavioral evidence data (§6), and language metadata (Production Blueprint §11.8).

| System | Role with this course | Why no redesign is needed |
|--------|----------------------|---------------------------|
| **LUMIAION** | Cognitive orchestrator: routes learner questions, coordinates AI tutors, maintains context across the course | The course already emits structured events (lessons, KL nodes, progress evidence) LUMIAION can orchestrate over |
| **YUNA** | Personal learning companion: reflection prompting, journaling support, practice reminders, personalized recommendations — within OLS §13 AI boundaries (support, never replace, never decide) | Personalization Layer (§8) already makes objectives format-independent; YUNA adapts modality per learner without touching objectives |
| **Axiom Nexus** | User-facing interface layer where the learner experiences course + AI + community | Course assets carry consistent naming/metadata; Axiom Nexus renders them without bespoke wiring |
| **Living Genome** | The learner's evolving knowledge/inner-development record: baseline map, reflections, decisions, and growth captured as the learner's own genome | Baseline Map + reflections + KL nodes are already structured artifacts a Living Genome can ingest (with consent) |
| **Knowledge Library** | The canonical concept graph (§7 nodes) shared across all OSG courses and bridged (clearly labeled) to Alpha Proxima research | KL IDs are assigned now; the library is populated at production, not retrofitted |

**Binding constraint (OLS §13):** any AI here *supports* reflection, practice, and personalization — it never thinks for the learner, never decides, never creates dependency, always labels evidence vs. framework, and refers distress to human/professional care. The course philosophy (capacity, not answers) is the same principle that governs its AI.

---

## 14. Future Evolution

How this single reference blueprint scales — because it is architecture, not content:

| Scale | What stays constant | What is added |
|-------|--------------------|---------------|
| **10 courses** | OLS, the 12-part lesson, Transformation Path, Knowledge Library IDs, this reference pattern | New courses instantiate the same blueprint template; reuse KL nodes; share the community & production pipeline |
| **50 courses** | Same standard & benchmark | Knowledge Library becomes a rich cross-course graph; learning paths chain courses; shared asset/design system amortizes production |
| **100 courses** | Same governance (Gate-1/Gate-2, OLS compliance) | Curriculum architecture (tracks, specializations); Knowledge Library as the institutional memory of OSG Academy |
| **Multiple instructors** | The reference blueprint + OLS = no one invents methodology | Instructor certification to OLS; per-instructor voice within one standard; QC ensures consistency |
| **Multiple languages** | FR-source → transcreation model (Production Blueprint §11) | ES, then AR (RTL); multi-column termbase & RTL-aware design built from day one |
| **AI tutors** | Format-independent objectives + KL nodes + OLS §13 boundaries | YUNA per-learner personalization; AI reflection/journaling partners; AI progress summaries |
| **Global community** | OLS §10 community rules | Language-spaced communities with shared celebration; regional live sessions; cross-cultural adaptation |

**The scaling guarantee:** every one of these grows by **adding instances to a fixed architecture**, never by redesigning it. That is the definition of a reference implementation.

---

## 15. Success Metric & Compliance

**Success metric.** *A new instructor can build a fully OSG-compliant course using this blueprint as the pattern — without inventing their own methodology.* If an instructor must invent method, the reference has failed; if they only need to instantiate it, it has succeeded.

**Compliance.** This course passes OLS Gate-1 (blueprint approval) and per-lesson Gate-2 (OLS Compliance QC §10 of the Production Blueprint + translation-accuracy QC §11.9) before filming. Core and Design Principles (OLS §3, §15) are non-waivable; structural deviations require a documented, approved waiver.

**Standing role.** Once approved, this document is the **reference implementation** every future OSG course is patterned on and measured against. It is versioned; changes follow MAJOR.MINOR.PATCH under the Chief Learning Architect.

---

## 16. Reference Implementation Governance (living reference)

*This section makes the Reference Implementation Blueprint a **living institutional reference**, not a static document. It records why the design is as it is, what it does not yet do, how it will improve, what production teaches us, and how it relates to future versions of the OLS.*

### 16.1 — Standing & Authority of This Document

This document is the **canonical reference implementation** of the OSG Learning Standard. Its authority is deliberately bounded:

- **It defines the minimum quality standard**, not the only permitted design. It is a floor, not a ceiling.
- **Future courses may innovate beyond it** — new formats, structures, pedagogies, subjects — **but may never violate the OSG Learning Standard (OLS).** The OLS is the law; this document is the worked example of meeting it well.
- **Every future course is reviewed against this Reference Implementation before publication** (the Reference Review, §16.2), in addition to OLS Gate-1/Gate-2.
- Where a future course's innovation and this reference disagree, and the innovation still fully honors the OLS, **the OLS prevails and the innovation is permitted** — and, if broadly useful, is folded back into a future version of this reference (§16.6).

### 16.2 — The Reference Review (pre-publication)

Before any OSG course is published, it passes a **Reference Review** answering three questions:

1. **Does it meet the OLS?** (Non-negotiable — OLS Gate-1/Gate-2.)
2. **Does it meet or exceed the minimum quality bar this reference sets?** (Transformation-Path traversal, learning validation, Knowledge Library integration, personalization options, community integration, production readiness.)
3. **If it deviates from the reference pattern, is the deviation an innovation that still honors the OLS — or a shortfall?** Innovations are documented and considered for §16.6; shortfalls are corrected before publication.

The Reference Review is owned by the Chief Learning Architect and recorded per course.

### 16.3 — Rationale for Major Design Decisions

*Why the reference is built the way it is — so future architects understand the intent, not just the shape.*

| Decision | Rationale |
|----------|-----------|
| **8 content weeks (not 6)** | The transformation arc requires a distinct **Application** stage (Week 7) and **Autonomy** stage (Week 8). Compressing them collapses "learned it" into "can do it under pressure" — the exact failure mode the course exists to prevent. |
| **Arc ends in Autonomy + a 90-Day Integration** | Durable behavioral change and true independence consolidate *after* instruction ends. `[E]` Ending at "graduation" would optimize for completion, not transformation — violating OSG Design Principle "Transformation before completion." |
| **Behavioral/self-authored validation, not exams** | The capacity being built (discernment, self-trust) is internal and cannot be measured by a test. Observable evidence (logs, maps, documented real decisions) is the honest proxy. |
| **Canonical Knowledge Library IDs assigned now** | Stable IDs let future courses reuse concepts and let the library become a cross-course graph. Assigning them at reference time (not retrofitting) is what makes 50–100 courses coherent. |
| **"Future Alpha Proxima" node class** | Keeps the bridge between OSG's applied teaching and the research institute **explicit and labeled**, so the two are connected without ever being conflated (protecting the evidence/framework line). |
| **Personalization via format-independent objectives** | Making objectives invariant across modality is what allows AI personalization *later without redesign*. The architecture pays for a capability it doesn't yet use. |
| **French as source language** | The OSG voice — especially contemplative `[F]` register — must be composed, not converted. Transcreation into English yields a better English course than translation. (Production Blueprint §11.) |
| **AI integration specified but not required** | The course must ship and transform with zero AI. AI is designed as an *additive* layer bound by OLS §13 — never a dependency, never a decider. |
| **Reference incorporates the Production Blueprint by reference** | Avoids a second source of truth for workbook/journal/production/bilingual detail. One canonical place per concern. |

### 16.4 — Known Limitations

*Stated honestly, in the OSG spirit of disclosing uncertainty.*

1. **Unvalidated by a live cohort.** This is a design; its effectiveness is a hypothesis until a cohort runs. Several `[E]`-labeled learning claims are supported by general research, not by outcome data from *this* course.
2. **Instructor-dependence at launch.** The reference assumes a bilingual, contemplatively-fluent instructor. Until instructor certification (§14) exists, quality depends heavily on one person.
3. **Self-reported evidence.** Learning validation relies on self-attestation (logs, self-assessment). This is appropriate for internal-capacity work but is not externally verifiable; it can be gamed by a learner (mostly to their own loss).
4. **Personalization is specified, not built.** At launch only 2–3 formats per activity are realistic; full per-learner adaptation awaits the AI layer.
5. **Knowledge Library is IDs-on-paper.** The nodes are assigned but the actual cross-course graph/tooling does not yet exist.
6. **90-Day Integration depends on sustained engagement** — historically the hardest retention window. The design mitigates but does not solve post-course drop-off.
7. **Sensitive material (Module/Week 4).** Shadow/resistance work sits near clinical territory; the therapy boundary is stated, but real-time risk detection depends on human moderation until AI boundary-tooling matures.
8. **Cultural transferability untested.** The contemplative framing is designed in a French/Western register; ES/AR expansion (Production Blueprint §11.10) may surface adaptation needs not yet visible.

### 16.5 — Future Improvements

*Sequenced, and revised as production teaches us.*

- **After Cohort 1:** replace general `[E]` claims with course-specific outcome data where possible; capture real Lessons Learned (§16.7); tune week pacing and drop-off nudges.
- **Templates:** extract a **fillable Course Blueprint + Lesson Blueprint template pair** from this reference (OLS roadmap v1.1) so new courses instantiate, not reinvent.
- **Instructor certification** to OLS + this reference (enables multi-instructor scale).
- **Knowledge Library tooling** — make the KL nodes a real graph; wire cross-course reuse.
- **Personalization build-out** — implement AI-driven modality adaptation on the format-independent objectives.
- **Assessment depth** — richer mastery rubrics; optional peer or coach validation to supplement self-report.
- **Boundary tooling** — AI distress-detection with human escalation for Week 4.
- **Localization** — prove ES, then AR (RTL) against this reference.

### 16.6 — Handling Innovation Beyond the Reference

When a future course does something this reference does not:

1. If it **violates the OLS** → not permitted; corrected before publication.
2. If it **honors the OLS but diverges from this reference** → permitted; recorded in the course's Reference Review as an *innovation*.
3. Innovations that prove broadly valuable across multiple courses are **promoted into a future version of this reference** (a MINOR or MAJOR bump, §16.8) so the whole Academy benefits. This is the mechanism by which the reference *learns* from the courses it governs.

### 16.7 — Lessons Learned During Production

*A living log. Seeded with design-phase lessons; extended after each production milestone and cohort. Empty rows are intentional — they will be filled, not guessed.*

| Date | Phase | Lesson | Action taken / reference change |
|------|-------|--------|-------------------------------|
| 2026-07-04 | Design | Distinguishing a separate **Application** week (7) from **Integration** (6) clarified the arc; earlier drafts blurred them | Added Week 7 as its own transformation stage |
| 2026-07-04 | Design | The course risked implying it "gives answers"; explicit philosophy guardrail was needed at the top of the blueprint | Added the governing philosophy constraint to the header and §1 |
| 2026-07-04 | Design | Knowledge nodes needed a way to connect to Alpha Proxima **without conflating** applied and research work | Introduced the labeled "Future Alpha Proxima" node class |
| *(pending)* | Scripting | — | — |
| *(pending)* | Cohort 1 | — | — |

### 16.8 — Compatibility Notes with Future OLS Versions

This reference implements **OLS v1.1**. Forward-compatibility intent:

| OLS change type | Effect on this reference |
|-----------------|--------------------------|
| **OLS PATCH** (clarifications, typos) | No change required; reference remains valid. |
| **OLS MINOR** (new optional elements, added templates) | Reference reviewed; adopts new elements at next MINOR bump; existing courses remain compliant. |
| **OLS MAJOR** (change to Core/Design Principles or the Lesson Blueprint) | Reference **must** be re-reviewed and re-aligned; a new MAJOR version of this reference is issued; existing courses are re-certified against the new OLS on a defined transition schedule. |

**Standing commitments regardless of OLS version:**
- This reference will always implement the *current ratified* OLS; it never lags a MAJOR change without an explicit, dated transition plan recorded here.
- The **Transformation Path** and the **evidence/framework distinction** are expected to persist across OLS versions; if a future OLS altered them, that would be a MAJOR event requiring a full reference rebuild.
- Version alignment is recorded in the Change Log (§16.9): every reference version names the OLS version it implements.

### 16.9 — Change Log

*Fine-grained record of what changed and why. Distinct from the Version History table below (which is a coarse per-release summary).*

| Date | Ref. Version | OLS Version | Change | Reason |
|------|--------------|-------------|--------|--------|
| 2026-07-04 | 1.0.0 | 1.1 | Initial Reference Implementation Blueprint created | Establish the Academy's benchmark course |
| 2026-07-04 | 1.1.0 | 1.1 | Added §16 Reference Implementation Governance (standing, review process, rationale, known limitations, future improvements, innovation handling, lessons-learned log, OLS compatibility, this change log) | Convert the reference from a static blueprint into a living institutional reference |

---

## Version History

| Version | Date | Author | OLS | Summary |
|---------|------|--------|-----|---------|
| 1.0.0 | 2026-07-04 | Chief Learning Architect + LUMIAION | v1.1 | Reference Implementation Blueprint for *Awaken the Inner Guru*: executive overview, transformation map, Week 0→8 roadmap + 90-day integration, weekly blueprint, 18-lesson inventory (with Knowledge Library concepts + future AI opportunities), learning validation, Knowledge Library integration (canonical KL IDs + classification + Alpha Proxima bridges), personalization layer, community layer, workbook/journal/production architecture (by reference), AI integration, future-evolution scaling, success metric. OLS v1.1 unchanged. |
| 1.1.0 | 2026-07-04 | Chief Learning Architect + LUMIAION | v1.1 | Added §16 Reference Implementation Governance — making this a living institutional reference: standing & authority (minimum standard, innovate-beyond-but-never-violate-OLS), pre-publication Reference Review, rationale for major design decisions, known limitations, future improvements, innovation-handling, lessons-learned log, OLS forward-compatibility notes, and a fine-grained change log. |
