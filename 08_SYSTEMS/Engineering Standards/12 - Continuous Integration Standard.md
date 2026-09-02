---
title: "12 - Continuous Integration Standard"
aliases: ["CI Standard", "Continuous Integration Standard", "Foundation Integrity", "Coherence Ratchet"]
tags: [systems, engineering, standards, ci, automation, coherence, integrity, alpha-proxima]
created: 2026-09-02
updated: 2026-09-02
status: active
version: "1.0.0"
authors: ["CLAUDE"]
artifact_type: engineering-standard
standard_id: "ES-12"
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "Claude"
dependencies: ["[[05 - Python Development Standard]]", "[[07 - Automation Standard]]", "[[09 - Git Standard]]", "[[03 - Folder Naming Convention]]"]
related_documents: ["[[ALPHA PROXIMA ENGINEERING HANDBOOK]]", "[[Alpha Proxima App Architecture v1]]", "[[Tool 013 - Alpha Proxima App]]", "[[Tool 012 - Founder OS State Engine]]", "[[Book III - Knowledge Integrity]]", "[[CN-001 Execution Tracker]]"]
related_research_programs: []
---

# 12 - Continuous Integration Standard

## Purpose

Define what the Foundation checks automatically on every change, and — more importantly — what it refuses to check.

This is the Foundation's first continuous integration. Before it, the toolkit's 79 tests and the coherence ratchet ran only when a person remembered to run them. A gate nobody pulls is not a gate.

---

## Scope

Applies to `.github/workflows/` and to any future automated check that gates a change to this repository.

---

## Context

### Why content is under test, not just code

Most repositories gate code. This one is a **Markdown vault with a small Python toolkit** — the institutional canon *is* the payload. A commit that adds one disconnected note damages the Foundation exactly as a broken function does: [[Book III - Knowledge Integrity]] and the Library Rule both require that knowledge connect, and a document connected to nothing cannot be found, inherited, or maintained.

So the workflow carries **no `paths` filter**. Notes and code are gated alike. This is the single most consequential decision in this standard, and the one most likely to be questioned by someone arriving from a conventional software repository.

### The two questions

| Job | Question | Cardinality |
|---|---|---|
| `verify` | Does the toolkit still work? | Once per supported Python version |
| `coherence` | Is the Foundation's knowledge coherent? | Once — content is not version-dependent |

Running the vault index three times would answer the same question three times. Running the tests on one Python would leave the toolkit exposed when a runner's default moves.

---

## Rules

### The ratchet

- Coherence defects are gated against `COHERENCE_CEILING`, declared in the workflow.
- **The ceiling ratchets down. It must never be raised to excuse defects introduced within the indexed corpus.** A Founder-ratified expansion of the corpus may reset the baseline once, provided the old and new corpus sizes and complete defect composition are recorded in the same change.
- Lowering it belongs in the same commit as the repairs that earned it, so the number is never left behind.
- The ceiling lives in the workflow rather than a config file so that every movement is a visible, reviewable edit.

### Check the instrument before raising the tolerance

**When a gated metric worsens sharply, the first hypothesis is that the measurement changed, not the Foundation.**

This rule was earned. On 2026-09-02 the ceiling was raised from 243 to 422 to accommodate what looked like a large increase in broken links after a corpus expansion. It was not. The indexer resolved only bare `[[Note]]` links and treated every valid `[[folder/Note]]` — a form Obsidian resolves natively — as broken. **260 of the 349 reported broken links did not exist**, and 30 documents were reported as orphans purely because their real inbound links went unrecognised. Correcting the resolver put the true figure at 135, *below* the pre-expansion baseline.

A ceiling raised to accommodate a measurement bug ratifies decay that was never there, and does it with a documented justification that reads entirely reasonable. That is the dangerous case: not a careless raise, but a well-argued one resting on a bad number.

So before any upward movement, and before accepting any sharp worsening:

- Sample the defects the tool reports and confirm by hand that they are real.
- Ask what the tool would have to believe for this number to be correct.
- Prefer fixing the instrument. A corrected instrument ratchets the ceiling *down*, which no amendment can.

A ceiling exists at all because a gate that can never pass is not a gate — it is noise, and teams learn to route around noise. The vault carries pre-existing defects owned by [[CN-001 Execution Tracker]]; failing on them from day one would have made this workflow permanently red and therefore ignored within a week.

### Report versus gate

- **Gated:** the two test suites, Founder state validity, both renderers, the coherence ceiling, and the absence of a dependency manifest.
- **Reported, never gated:** vault validation. It carries pre-existing errors that belong to CN-001. Its output appears in the run summary so it stays visible without blocking unrelated work.

Anything reported but not gated must say so explicitly in the summary. A number with no stated authority invites the reader to assume it has some.

### Zero dependencies

The toolkit is Python standard library only. The workflow **asserts** this by failing if `requirements.txt`, `pyproject.toml`, `setup.py`, or `package.json` appears.

This is not pedantry. A dependency is a maintenance obligation that outlives whoever added it, and a vault meant to remain readable for a century cannot afford a tree of transitive packages that stop resolving. Adding one is an architectural decision requiring a Founder decision, not a build fix applied under deadline pressure.

The workflow itself uses only `actions/checkout` and `actions/setup-python`, both first-party.

### Keeping the runner honest

Actions are pinned to a **major version**, and the major must be one whose runtime GitHub still supports. `checkout@v5` and `setup-python@v6` are the Node 24 majors; the previous pair targeted Node 20, which GitHub removed in September 2026.

A deprecation warning in a green run is still a finding. This one was caught by reading the first run's log rather than trusting the green tick — a check that passes today while warning about its own runtime is a check with an expiry date on it. Read the log of a workflow's first run, and of any run after a runner image changes.

### Permissions and secrets

- `permissions: contents: read`. The workflow validates; it never writes to the repository, publishes an artifact, or touches a credential.
- **The Foundation has no secrets, and this file must not become the reason it needs one.** Any future check requiring a credential is a Founder decision, and inherits the boundary recorded in `FD-002`.

### Generated artifacts

CI does **not** assert that committed generated files (`app.html`, `vault-index.json`, `console.html`, [[Founder Console]]) are byte-identical to a fresh render. It cannot: every render embeds the current date, and the Console legitimately changes what it displays when the Mission of the Day goes stale.

Instead CI proves the **renderers work end to end on real data** — they exit cleanly, the template placeholder is replaced, and the index parses. That catches the real risks (a broken placeholder, invalid state, a renderer crash) without a check that would start failing at midnight for no reason.

Generated files are still never edited by hand. That rule is enforced by convention and by the banner each carries, not by CI.

### Writing a new check

- Every gate must name a repair, not a trend. "Connect this document" is a check; "documentation velocity" is not.
- Prefer putting an assertion in a test suite over putting it in workflow YAML. Tests can be run locally by a contributor; YAML cannot. The workflow should stay thin enough to read in one screen per job.
- A step that pipes to `tee` must set `pipefail` or capture `PIPESTATUS`, or a crash will be masked by the exit code of `tee`.
- Global CLI options precede the subcommand: `ap.py app --app X render`, never `ap.py app render --app X`. See [[06 - CLI Standard]].

---

## Examples

Good — a gate that names a repair:

```yaml
- name: Coherence ratchet
  run: python3 "$AP" app check --max-defects "$COHERENCE_CEILING"
```

Bad — a gate that can never pass, and will be ignored within a week:

```yaml
- name: Vault must be perfect
  run: python3 "$AP" validate --fail-on error   # 17 pre-existing errors
```

Bad — raising the ceiling to make a change land:

```yaml
COHERENCE_CEILING: "245"   # was 243; new note is an orphan
```

Worse — raising it on a number nobody checked:

```yaml
COHERENCE_CEILING: "422"   # was 243; broken links "jumped" after an import
```

The second is more dangerous than the first: it is well argued, and wrong. 260 of those links resolved perfectly well in Obsidian.

---

## Verification

The workflow was simulated against a clean clone before it was committed, executing each `run:` step under `bash -e` exactly as the GitHub runner does.

| Check | Result |
|---|---|
| All steps, clean checkout | Pass |
| Coherence ratchet with one orphan note added | **Fails, exit 1**, with `::error::` annotations |
| Run summary rendered | Both on success and on failure (`if: always()`) |

A gate never observed failing is not a verified gate. The negative case was tested deliberately.

---

## Related Documents

- [[ALPHA PROXIMA ENGINEERING HANDBOOK]] — the standards library
- [[Alpha Proxima App Architecture v1]] — where the ratchet and its ceiling are defined
- [[Tool 013 - Alpha Proxima App]] — the tool CI invokes
- [[Tool 012 - Founder OS State Engine]] — the state CI validates
- [[09 - Git Standard]] — branches, commits, and reviews this workflow runs against
- [[CN-001 Execution Tracker]] — owner of every defect the ratchet counts

---

## Future Improvements

1. **Lower the ceiling** with each repaired batch until it reaches zero, then delete `--max-defects` entirely.
2. **A browser smoke test** for the app interface. Deliberately omitted from v1: it needs a browser on the runner, and the failure it would catch is better covered by an assertion inside `test_alpha_app.py`, which a contributor can also run locally.
3. **Gate vault validation** once CN-001 closes the 17 errors, converting it from report to gate.
4. **A release workflow**, if the Foundation ever publishes a versioned artifact. It does not today.

---

## Open Questions

- Should the ceiling live in a committed file that CI reads, so lowering it is a one-line diff rather than a workflow edit? The current choice favours visibility over convenience.
- Should a pull request that raises `COHERENCE_CEILING` be blocked mechanically, rather than by this standard's prohibition?
- Does the Foundation want CI to run on a schedule as well as on change, to catch decay in a repository that sits idle?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-09-02 | CLAUDE | First CI standard: the two jobs, the ratchet, report-versus-gate, zero dependencies, and the no-`paths`-filter decision |
