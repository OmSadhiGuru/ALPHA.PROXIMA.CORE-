# Claude Code inside Obsidian — Setup Guide

*Run Claude Code (or Codex / Gemini CLI) as an internal worker inside your Obsidian vault, via the **Agent Client Protocol (ACP)**. Your vault becomes the agent's working directory: it can read, write, search, and run multi-step work on your notes.*

**Reproducible & shareable.** This guide is written to be followed cold by anyone. Tested on macOS/Linux; Windows notes included.

---

## What you're building

```
Obsidian
   └── Agent Client plugin  (speaks ACP)
          └── claude-agent-acp   (the ACP ↔ Claude Code bridge)   ← needs Node.js
                 └── Claude Code   (the actual agent/worker)
                        └── your vault  (its working directory)
```

Three command-line pieces sit under the Obsidian plugin: **Node.js**, the **Claude Code** CLI, and the **`claude-agent-acp`** adapter that lets them speak ACP.

---

## Prerequisites

- **Obsidian** desktop (this is desktop-only; it will not work on mobile).
- **Node.js v18+** (v20 LTS or newer recommended). *Required* — both the adapter and Claude Code are Node tools.
- An **Anthropic account** (for Claude Code login).
- Terminal access (Terminal on macOS/Linux; PowerShell + WSL on Windows).

---

## Step 1 — Install Node.js

**macOS:** `brew install node` (or download from [nodejs.org](https://nodejs.org))
**Linux:** your package manager, or [nodejs.org](https://nodejs.org)
**Windows:** installer from [nodejs.org](https://nodejs.org) — but see the Windows note below (use WSL).

Verify:
```bash
node --version     # v18+ (v20+ ideal)
npm --version
```

## Step 2 — Install Claude Code (the worker) and log in

```bash
curl -fsSL https://claude.ai/install.sh | bash
```
Then launch it once to authenticate (opens a browser login):
```bash
claude
```
Log in with your Anthropic account. Once logged in via the CLI, you won't need to paste an API key into Obsidian.

Verify:
```bash
claude --version
```

## Step 3 — Install the ACP adapter (the bridge)

This provides the `claude-agent-acp` binary the plugin launches:
```bash
npm install -g @agentclientprotocol/claude-agent-acp
```
Verify:
```bash
claude-agent-acp --help     # should respond, not "command not found"
```

## Step 4 — Get the paths you'll paste into Obsidian

```bash
which node               # e.g. /opt/homebrew/bin/node  or  /usr/local/bin/node
which claude-agent-acp   # e.g. /usr/local/bin/claude-agent-acp
```
Windows: use `where node` / `where claude-agent-acp`.

Keep these two paths handy for the next step.

## Step 5 — Install & configure the Obsidian plugin

1. Obsidian → **Settings → Community plugins → Browse** → search **"Agent Client"** → Install → Enable.
   *(Author: RAIT-09. Alternative: "Claudian" by YishenTu does the same job — pick one, not both.)*
2. Open **Settings → Agent Client** and set:
   - **Node.js path** → the `which node` result. *(Can be left blank only if `node` is on your system PATH; setting it explicitly avoids the most common failure.)*
   - **Claude Code path** (the `claude-agent-acp` binary) → the `which claude-agent-acp` result.
   - **API key** → leave empty (you logged in via the CLI in Step 2).
   - **Default agent** → Claude Code.
3. Open the Agent Client view (right sidebar tab, or the floating chat button), select **Claude Code**, and start a message.

That's it — Claude Code now runs with your **vault as its working directory**.

---

## Verify it works

In the Agent Client chat, ask something that requires touching files, e.g.:
> "List the top-level folders in this vault and summarize the README."

If it reads your files and answers, the full chain (Obsidian → ACP → adapter → Claude Code → vault) is live.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `command not found: claude-agent-acp` | Step 3 didn't complete, or npm's global bin isn't on PATH. Run `npm bin -g` and add that dir to PATH, or paste the full path into the plugin. |
| Plugin says it can't find Node | Set the **Node.js path** explicitly (Step 5) to your `which node` output. GUI apps often don't inherit your shell PATH. |
| Works in terminal, not in Obsidian | Almost always PATH: Obsidian (a GUI app) has a minimal PATH. Fill in **both** explicit paths in plugin settings. |
| Auth errors | Re-run `claude` in a terminal and confirm you're logged in; leave the plugin API key blank. |
| Nothing happens on send | Restart Obsidian after setting the paths; check the plugin's debug mode. |
| Node version errors | Upgrade to Node 20 LTS. |

---

## Windows note

Claude Code runs best on Windows via **WSL** (Windows Subsystem for Linux):
1. Install WSL + a Linux distro.
2. Run Steps 1–3 **inside WSL**.
3. In the Agent Client settings, enable **WSL mode** (`windowsWslMode`) and point the paths at the WSL binaries.

On macOS/Linux, ignore this section.

---

## Security note (read once)

The Agent Client plugin has an **`autoAllowPermissions`** setting.
- **On** = the agent reads/writes/runs commands in your vault **without asking** each time. Convenient; genuinely "internal worker."
- **Off** = you approve actions the first while.

For a trusted personal vault, "on" is reasonable. But the agent can modify **anything** in the vault folder unattended — if your vault holds sensitive or important work, start with it **off** until you trust the flow, then turn it on. Also: the agent's reach is your vault folder, so keep secrets/credentials out of the vault.

---

## Switching or adding agents

The same plugin can run **Codex** and **Gemini CLI** too — install their CLIs + ACP adapters and select them from the agent dropdown. Claude Code, Codex, and Gemini can each be an internal worker; switch per task.

---

## Reference: what each piece is

| Piece | What it is | Install |
|-------|-----------|---------|
| **Node.js** | JS runtime the tools run on | `brew install node` / nodejs.org |
| **Claude Code** | The agent (reads/writes/runs, multi-step) | `curl -fsSL https://claude.ai/install.sh \| bash` |
| **claude-agent-acp** | ACP adapter bridging Obsidian ↔ Claude Code | `npm i -g @agentclientprotocol/claude-agent-acp` |
| **Agent Client** | Obsidian plugin (ACP client UI) | Community plugins → "Agent Client" |

---

## Sources

- [Agent Client plugin (RAIT-09)](https://github.com/RAIT-09/obsidian-agent-client) · [docs](https://rait-09.github.io/obsidian-agent-client/)
- [Zed ACP — Obsidian editor](https://zed.dev/acp/editor/obsidian)
- [Claudian (YishenTu)](https://github.com/YishenTu/claudian)
- [Agent Client Protocol](https://agentclientprotocol.com)

---

*Last updated: 2026-07-04. If a command changes upstream, verify the package name with `npm view @agentclientprotocol/claude-agent-acp` and the install script at claude.ai/install.sh.*
