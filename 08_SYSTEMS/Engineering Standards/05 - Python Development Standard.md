---
title: "05 - Python Development Standard"
aliases: ["Python Standard", "Python Engineering Standard"]
tags: [systems, engineering, standards, python, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-standard
standard_id: "ES-05"
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[ALPHA PROXIMA ENGINEERING HANDBOOK]]"]
related_documents: ["[[Vault Note Generator]]"]
related_research_programs: []
---

# 05 - Python Development Standard

## Purpose

Define how Alpha Proxima Python utilities should be structured, written, tested, and maintained so local-first automation stays reliable over time.

---

## Scope

Applies to Python scripts, CLI utilities, local services, indexing jobs, workflow helpers, and automation pipelines maintained inside or alongside the vault.

---

## Rules

- Use Python 3 standard library when it is sufficient.
- Prefer small modules with explicit responsibilities.
- Use lowercase snake_case for files, functions, variables, and modules.
- Use `PascalCase` for classes.
- Add type hints for public functions and non-obvious internal functions.
- Use `argparse` for standard-library CLIs.
- Keep side effects inside `main()` or clearly named orchestration functions.
- Use `pathlib.Path` for filesystem paths.
- Raise specific exceptions or return explicit exit codes.
- Do not hardcode user-specific absolute paths unless the script is explicitly local and documented.
- Do not store secrets in source files, frontmatter, logs, or examples.

### Directory Layout

For small vault utilities:

```text
08_SYSTEMS/Automation/
  vault_note.py
  Vault Note Generator.md
```

For larger packages:

```text
project-name/
  src/project_name/
  tests/
  pyproject.toml
  README.md
```

---

## Examples

### Imports

```python
from __future__ import annotations

import argparse
import logging
from pathlib import Path
```

### Function Shape

```python
def build_output_path(root: Path, title: str) -> Path:
    """Return the destination path for a generated note."""
    return root / f"{title}.md"
```

### Error Handling

```python
if destination.exists() and not force:
    raise FileExistsError(f"Refusing to overwrite existing file: {destination}")
```

### CLI Entry Point

```python
def main(argv: list[str]) -> int:
    args = parse_args(argv)
    run(args)
    return 0
```

---

## Best Practices

- Keep scripts boring, inspectable, and easy to run locally.
- Separate parsing, transformation, and writing.
- Write tests for parsing, path generation, and failure cases.
- Use dependency files only when external packages are necessary.
- Prefer configuration files or environment variables for values that change by machine.
- Log operational events; print final user-facing results.

---

## Common Mistakes

- Mixing CLI parsing with business logic.
- Writing files during import.
- Catching every exception and hiding the failure.
- Adding dependencies for simple standard-library tasks.
- Using comments to explain confusing code instead of simplifying the code.
- Letting generated paths escape the intended workspace.

---

## Future Evolution

Future versions may define packaging, test coverage, linting, type checking, local server, and vector database standards. Those should be added when the vault contains enough Python surface area to justify the overhead.

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial Python development standard |

---

## Related Standards

- [[04 - File Naming Convention]]
- [[06 - CLI Standard]]
- [[07 - Automation Standard]]
- [[08 - Logging Standard]]
- [[09 - Git Standard]]

