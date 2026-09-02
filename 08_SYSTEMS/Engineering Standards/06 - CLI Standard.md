---
title: "06 - CLI Standard"
aliases: ["Command Line Interface Standard", "Command Standard"]
tags: [systems, engineering, standards, cli, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-standard
standard_id: "ES-06"
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[ALPHA PROXIMA ENGINEERING HANDBOOK]]"]
related_documents: ["[[Vault Note Generator]]"]
related_research_programs: []
---

# 06 - CLI Standard

## Purpose

Define predictable command-line interfaces for Alpha Proxima tools so contributors can run, automate, debug, and document utilities consistently.

---

## Scope

Applies to scripts and tools invoked from a terminal, GitHub workflow, local scheduler, n8n node, MCP integration, or automation pipeline.

---

## Rules

- Use lowercase kebab-case for installed command names.
- Use subcommands for distinct actions.
- Use positional arguments only for required primary inputs.
- Use flags for optional behavior.
- Provide `--help` for every command and subcommand.
- Use `--dry-run` when a command can write, delete, move, publish, or send.
- Use `--force` only for explicit override behavior.
- Print machine-readable output only when requested through a flag such as `--json`.
- Write errors to stderr.
- Return meaningful exit codes.

### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | General failure |
| 2 | Invalid arguments or configuration |
| 3 | Missing input |
| 4 | Refused unsafe operation |
| 5 | External dependency failure |

---

## Examples

### Command Shape

```bash
vault-note create implementation "Local API Integration Plan" \
  --author CODEX \
  --purpose "Draft a local API integration plan."
```

### Help Output

```text
usage: vault-note create implementation TITLE --purpose PURPOSE [options]

Create a draft implementation note from an approved template.

options:
  --author NAME       Author or role to record in frontmatter
  --output PATH       Optional path relative to the vault root
  --dry-run           Show intended output without writing
  --force             Overwrite an existing target file
```

### Error Message

```text
error: refusing to overwrite existing file: 08_SYSTEMS/Implementation Notes/Plan.md
hint: pass --force only after reviewing the existing file
```

---

## Best Practices

- Make the safe path the default.
- Use verbs that describe user intent: `create`, `validate`, `index`, `export`, `sync`.
- Keep command output short unless verbosity is requested.
- Include the target path after successful file creation.
- Design commands so they can run non-interactively.
- Keep examples copyable.

---

## Common Mistakes

- Using hidden defaults that write to unexpected locations.
- Requiring interactive prompts for automation workflows.
- Printing stack traces for ordinary user errors.
- Using ambiguous flags such as `--do-it`.
- Returning success when a requested write did not happen.

---

## Future Evolution

Future versions may define standard JSON output schemas, shell completion, progress output, and command discovery for MCP or n8n integration.

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial CLI standard |

---

## Related Standards

- [[05 - Python Development Standard]]
- [[07 - Automation Standard]]
- [[08 - Logging Standard]]
- [[09 - Git Standard]]

