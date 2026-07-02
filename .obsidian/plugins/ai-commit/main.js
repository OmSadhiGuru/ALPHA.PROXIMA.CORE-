"use strict";
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// main.ts
var main_exports = {};
__export(main_exports, {
  default: () => AICommitPlugin
});
module.exports = __toCommonJS(main_exports);
var import_obsidian = require("obsidian");
var import_child_process = require("child_process");
var DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions";
var DEFAULT_MODEL = "deepseek-v4-flash";
var RETRIES = 3;
var MODEL_OPTIONS = {
  "deepseek-v4-flash": "DeepSeek V4 Flash",
  "deepseek-v4-pro": "DeepSeek V4 Pro"
};
var SYSTEM_PROMPT = [
  "You are an expert at writing git commit messages.",
  "Write a short, descriptive commit message in plain language.",
  'Do NOT use Conventional Commits format (no "type:" or "type(scope):" prefixes).',
  "Write ONLY the commit message \u2014 no explanations, no markdown fences, no quotes.",
  "Output a complete sentence. Do not truncate mid-word.",
  "Focus on WHAT changed and WHY, not HOW."
].join("\n");
var DEFAULT_SETTINGS = {
  apiKey: "",
  model: DEFAULT_MODEL,
  customPrompt: "",
  timeout: 3e4
};
function cleanMessage(raw) {
  return raw.replace(/^```[a-z]*\n?/im, "").replace(/\n?```$/m, "").replace(/^["']|["']$/g, "").replace(/^commit message:\s*/im, "").replace(/^\w+(\([^)]*\))?!?:\s*/i, "").trim();
}
function isError(e) {
  return e instanceof Error;
}
function isAbortError(e) {
  return isError(e) && e.name === "AbortError";
}
function errorMessage(e) {
  if (isError(e)) {
    return e.message;
  }
  if (typeof e === "string") {
    return e;
  }
  return "Unknown error";
}
function timeoutPromise(ms) {
  return new Promise(
    (_, reject) => window.setTimeout(() => reject(new DOMException("Request timed out", "AbortError")), ms)
  );
}
var AICommitSettingTab = class extends import_obsidian.PluginSettingTab {
  plugin;
  constructor(app, plugin) {
    super(app, plugin);
    this.plugin = plugin;
  }
  display() {
    const { containerEl } = this;
    containerEl.empty();
    new import_obsidian.Setting(containerEl).setName("DeepSeek API key").setDesc("DeepSeek API key").addText((text) => {
      text.setPlaceholder("Sk-\u2026").setValue(this.plugin.settings.apiKey).onChange(async (value) => {
        this.plugin.settings.apiKey = value.trim();
        await this.plugin.saveSettings();
      });
      text.inputEl.type = "password";
    });
    new import_obsidian.Setting(containerEl).setName("Model").setDesc("DeepSeek model for commit message generation").addDropdown((dropdown) => {
      for (const key of Object.keys(MODEL_OPTIONS)) {
        dropdown.addOption(key, MODEL_OPTIONS[key]);
      }
      dropdown.setValue(this.plugin.settings.model);
      dropdown.onChange(async (value) => {
        this.plugin.settings.model = value;
        await this.plugin.saveSettings();
      });
    });
    new import_obsidian.Setting(containerEl).setName("Timeout").setDesc("API request timeout in seconds").addSlider((slider) => {
      slider.setLimits(10, 120, 5).setValue(this.plugin.settings.timeout / 1e3).onChange(async (value) => {
        this.plugin.settings.timeout = value * 1e3;
        await this.plugin.saveSettings();
      });
    });
    new import_obsidian.Setting(containerEl).setName("Custom instructions").setDesc("Appended to the system prompt (language, style, extra rules)").addTextArea((text) => {
      text.setPlaceholder("Write concise commit messages").setValue(this.plugin.settings.customPrompt).onChange(async (value) => {
        this.plugin.settings.customPrompt = value.trim();
        await this.plugin.saveSettings();
      });
      text.inputEl.rows = 3;
    });
  }
};
var AICommitPlugin = class extends import_obsidian.Plugin {
  async onload() {
    await this.loadSettings();
    this.addSettingTab(new AICommitSettingTab(this.app, this));
    this.addCommand({
      id: "generate-commit-message",
      name: "Generate commit message",
      callback: () => {
        void this.generateAndFill();
      }
    });
    this.registerEvent(
      this.app.workspace.on("layout-change", () => {
        this.injectButton();
      })
    );
    this.app.workspace.onLayoutReady(() => {
      this.injectButton();
      this.observeGitView();
    });
  }
  injectButton() {
    const leaves = this.app.workspace.getLeavesOfType("git-view");
    const plugin = this;
    const doc = window.activeDocument;
    for (const leaf of leaves) {
      const container = leaf.view.containerEl.querySelector(".nav-buttons-container");
      if (!container || container.querySelector("#ai-commit-btn")) continue;
      const btn = doc.createElement("div");
      btn.id = "ai-commit-btn";
      btn.className = "clickable-icon nav-action-button ai-commit-btn";
      btn.setAttribute("aria-label", "Generate commit message");
      (0, import_obsidian.setIcon)(btn, "sparkles");
      btn.addEventListener("click", () => {
        void plugin.generateAndFill();
      });
      const commitBtn = container.querySelector("#commit-btn");
      if (commitBtn) {
        commitBtn.before(btn);
      } else {
        container.appendChild(btn);
      }
    }
  }
  observeGitView() {
    const handler = () => {
      const leaves = this.app.workspace.getLeavesOfType("git-view");
      for (const leaf of leaves) {
        const el = leaf.view.containerEl;
        if (el.dataset.aiCommitObserved) continue;
        el.dataset.aiCommitObserved = "1";
        new MutationObserver(() => {
          this.injectButton();
        }).observe(el, { childList: true, subtree: true });
      }
    };
    this.registerEvent(this.app.workspace.on("layout-change", handler));
    handler();
  }
  async generateAndFill() {
    const { apiKey, model, customPrompt, timeout } = this.settings;
    if (!apiKey) {
      new import_obsidian.Notice("Set DeepSeek API key in settings");
      return;
    }
    const vaultPath = this.app.vault.adapter.basePath;
    if (!vaultPath) {
      new import_obsidian.Notice("Cannot determine vault path");
      return;
    }
    let diff;
    try {
      const result = (0, import_child_process.execSync)("git diff --cached", {
        cwd: vaultPath,
        encoding: "utf-8",
        maxBuffer: 10 * 1024 * 1024
      });
      diff = result.toString();
    } catch (e) {
      new import_obsidian.Notice(`Git error \u2014 ${errorMessage(e)}`);
      return;
    }
    if (!diff.trim()) {
      new import_obsidian.Notice("No staged changes");
      return;
    }
    const truncatedDiff = diff.length > 8e3 ? diff.substring(0, 8e3) + "\n...diff truncated" : diff;
    const notice = new import_obsidian.Notice("Generating...", 0);
    this.setButtonLoading(true);
    let message = "";
    let lastError;
    for (let attempt = 1; attempt <= RETRIES; attempt++) {
      try {
        if (attempt > 1) {
          notice.setMessage(`Generating... (attempt ${attempt}/${RETRIES})`);
        }
        const systemPrompt = customPrompt ? SYSTEM_PROMPT + "\n" + customPrompt : SYSTEM_PROMPT;
        const response = await Promise.race([
          (0, import_obsidian.requestUrl)({
            url: DEEPSEEK_API_URL,
            method: "POST",
            headers: {
              "Authorization": `Bearer ${apiKey}`,
              "Content-Type": "application/json"
            },
            body: JSON.stringify({
              model,
              messages: [
                { role: "system", content: systemPrompt },
                { role: "user", content: `Write a commit message for:

${truncatedDiff}` }
              ],
              temperature: 0.3,
              max_tokens: 500
            })
          }),
          timeoutPromise(timeout)
        ]);
        if (response.status < 200 || response.status >= 300) {
          throw new Error(`API ${response.status}: ${response.text}`);
        }
        const data = response.json;
        const msg = (data.choices?.[0]?.message?.content ?? "").trim();
        if (!msg) {
          throw new Error("Empty response from API");
        }
        message = cleanMessage(msg);
        break;
      } catch (e) {
        lastError = e;
        if (attempt < RETRIES && !isAbortError(e)) {
          await new Promise((r) => window.setTimeout(r, 1e3 * attempt));
        }
      }
    }
    if (message) {
      const gitLeaves = this.app.workspace.getLeavesOfType("git-view");
      if (gitLeaves.length > 0) {
        const textarea = gitLeaves[0].view.containerEl.querySelector(".commit-msg-input");
        if (textarea instanceof HTMLTextAreaElement) {
          Object.getOwnPropertyDescriptor(
            HTMLTextAreaElement.prototype,
            "value"
          ).set.call(textarea, message);
          textarea.dispatchEvent(new Event("input", { bubbles: true }));
          textarea.focus();
        }
      }
      notice.hide();
      const preview = message.length > 60 ? message.substring(0, 60) + "..." : message;
      new import_obsidian.Notice(`Done \u2014 ${preview}`);
    } else {
      notice.hide();
      if (isAbortError(lastError)) {
        new import_obsidian.Notice(`Request timed out (${timeout / 1e3}s)`);
      } else {
        new import_obsidian.Notice(errorMessage(lastError));
      }
      console.error("AI Commit error:", lastError);
    }
    this.setButtonLoading(false);
  }
  setButtonLoading(loading) {
    const btn = window.activeDocument.querySelector("#ai-commit-btn");
    if (!(btn instanceof HTMLElement)) return;
    if (loading) {
      btn.addClass("ai-commit-loading");
    } else {
      btn.removeClass("ai-commit-loading");
    }
  }
  async loadSettings() {
    const data = await this.loadData();
    this.settings = Object.assign({}, DEFAULT_SETTINGS, data);
  }
  async saveSettings() {
    await this.saveData(this.settings);
  }
};

/* nosourcemap */