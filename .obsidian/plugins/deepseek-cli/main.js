const { Plugin, ItemView, Notice, requestUrl, MarkdownRenderer, PluginSettingTab, Setting, FuzzySuggestModal } = require('obsidian');

const VIEW_TYPE = 'deepseek-cli-chat';

// ====== Default settings ======
const DEFAULT_SETTINGS = {
    providerType: 'anthropic',
    baseUrl: 'https://api.deepseek.com/anthropic',
    apiKey: 'sk-14a5e1375ab64630a519aa18ea5a8dcd',
    model: 'deepseek-v4-pro',
    models: 'deepseek-v4-pro, deepseek-chat, deepseek-reasoner',
};

// ====== Helpers ======
function uid() {
    return Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
}
function buildAnthropicHeaders(apiKey) {
    return { 'x-api-key': apiKey, 'anthropic-version': '2023-06-01', 'Content-Type': 'application/json' };
}
function buildOpenAIHeaders(apiKey) {
    return { 'Authorization': `Bearer ${apiKey}`, 'Content-Type': 'application/json' };
}
function toAnthropicMessages(messages) {
    return messages.filter(m => m.content).map(m => ({ role: m.role, content: m.content }));
}
function toOpenAIMessages(messages) {
    return messages.filter(m => m.content).map(m => ({ role: m.role, content: m.content }));
}

// ====== SVG Icons ======
const ICONS = {
    send: '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>',
    trash: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>',
    settings: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>',
    history: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>',
    plus: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>',
    copy: '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>',
    refresh: '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 4 23 10 17 10"></polyline><polyline points="1 20 1 14 7 14"></polyline><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path></svg>',
    trashSmall: '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>',
    check: '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>',
    codeCopy: '<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>',
    codeCheck: '<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>',
    sidebarOpen: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg>',
    sidebarClose: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line><line x1="15" y1="9" x2="9" y2="15"></line></svg>',
    stop: '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" stroke="none"><rect x="6" y="6" width="12" height="12" rx="2"></rect></svg>',
    robot: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="8" width="16" height="13" rx="3"/><line x1="12" y1="4" x2="12" y2="8"/><circle cx="12" cy="3" r="1.5"/><circle cx="9" cy="13" r="1.5" fill="currentColor" stroke="none"/><circle cx="15" cy="13" r="1.5" fill="currentColor" stroke="none"/><line x1="8" y1="18" x2="16" y2="18"/></svg>',
    userPerson: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
    edit: '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>',
    addFiles: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="12" y1="18" x2="12" y2="12"/><line x1="9" y1="15" x2="15" y2="15"/></svg>',
    plan: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>',
    sparkle: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
    lock: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
    unlock: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 9.9-1"/></svg>',
    xSmall: '<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>',
    chevronDown: '<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>',
    loader: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="2" x2="12" y2="6"/><line x1="12" y1="18" x2="12" y2="22"/><line x1="4.93" y1="4.93" x2="7.76" y2="7.76"/><line x1="16.24" y1="16.24" x2="19.07" y2="19.07"/><line x1="2" y1="12" x2="6" y2="12"/><line x1="18" y1="12" x2="22" y2="12"/><line x1="4.93" y1="19.07" x2="7.76" y2="16.24"/><line x1="16.24" y1="7.76" x2="19.07" y2="4.93"/></svg>',
};

// ====== File Select Modal ======
class FileSelectModal extends FuzzySuggestModal {
    constructor(app, items, onSubmit) {
        super(app);
        this.items = items;
        this.onSubmit = onSubmit;
        this.selected = new Set();
        this.setPlaceholder('Search files to add as context...');
    }

    getItems() { return this.items; }
    getItemText(item) {
        return (this.selected.has(item.path) ? '✓ ' : '') + item.name;
    }
    onChooseItem(item, evt) {
        if (this.selected.has(item.path)) {
            this.selected.delete(item.path);
        } else {
            this.selected.add(item.path);
        }
        // Refresh suggestions to show checkmarks
        this.inputEl.value = '';
        this.inputEl.dispatchEvent(new Event('input'));
        // Show current selection count
        if (this.selected.size > 0) {
            this.resultContainerEl.createDiv({ text: `Selected: ${this.selected.size} file(s)`, cls: 'suggestion-hotkey' });
        }
    }

    onClose() {
        super.onClose();
        if (this.selected.size > 0) {
            this.onSubmit(Array.from(this.selected));
        }
    }
}

// ====== Chat View ======
class DeepSeekChatView extends ItemView {
    constructor(leaf, plugin) {
        super(leaf);
        this.plugin = plugin;
    }

    getViewType() { return VIEW_TYPE; }
    getDisplayText() { return 'DeepSeek CLI'; }
    getIcon() { return 'bot'; }

    async onOpen() {
        const container = this.containerEl.children[1];
        container.empty();
        container.addClass('deepseek-cli-container');

        // === Top-level layout: sidebar + main ===
        const layout = container.createDiv('deepseek-cli-layout');

        // ---- History Sidebar ----
        this.sidebar = layout.createDiv('deepseek-cli-sidebar');
        const sidebarHeader = this.sidebar.createDiv('deepseek-cli-sidebar-header');
        sidebarHeader.createSpan({ text: 'History', cls: 'deepseek-cli-sidebar-title' });
        const newChatBtn = sidebarHeader.createEl('button', { cls: 'deepseek-cli-new-chat-btn' });
        newChatBtn.innerHTML = ICONS.plus + ' New';
        newChatBtn.addEventListener('click', () => this.newConversation());
        this.convList = this.sidebar.createDiv('deepseek-cli-sidebar-list');

        // ---- Main Chat Panel ----
        this.mainPanel = layout.createDiv('deepseek-cli-main');

        // Header bar
        this.header = this.mainPanel.createDiv('deepseek-cli-header');
        const headerLeft = this.header.createDiv('deepseek-cli-header-left');
        this.toggleBtn = headerLeft.createEl('button', { cls: 'deepseek-cli-icon-btn', attr: { 'aria-label': 'Show history' } });
        this.toggleBtn.innerHTML = ICONS.history;
        this.toggleBtn.addEventListener('click', () => this.toggleSidebar());
        this.headerStatus = headerLeft.createSpan('deepseek-cli-header-status');

        const headerRight = this.header.createDiv('deepseek-cli-header-right');

        // Model selector
        this.modelSelect = headerRight.createEl('select', { cls: 'deepseek-cli-model-select' });
        const models = (this.plugin.settings.models || DEFAULT_SETTINGS.models).split(',').map(m => m.trim()).filter(Boolean);
        models.forEach(m => {
            const opt = this.modelSelect.createEl('option', { text: m, value: m });
            if (m === this.plugin.settings.model) opt.selected = true;
        });
        this.modelSelect.addEventListener('change', async () => {
            this.plugin.settings.model = this.modelSelect.value;
            await this.plugin.saveSettings();
            this.updateStatus();
        });
        const clearBtn = headerRight.createEl('button', { cls: 'deepseek-cli-icon-btn', attr: { 'aria-label': 'Clear chat' } });
        clearBtn.innerHTML = ICONS.trash;
        clearBtn.addEventListener('click', () => this.clearChat());
        const settingsBtn = headerRight.createEl('button', { cls: 'deepseek-cli-icon-btn', attr: { 'aria-label': 'Settings' } });
        settingsBtn.innerHTML = ICONS.settings;
        settingsBtn.addEventListener('click', () => {
            this.app.setting.open();
            this.app.setting.openTabById('deepseek-cli');
        });

        // Chat area
        this.chatArea = this.mainPanel.createDiv('deepseek-cli-chat');

        // Loading indicator
        this.loadingEl = this.mainPanel.createDiv('deepseek-cli-loading');
        this.loadingEl.createDiv('deepseek-cli-loading-dot');
        this.loadingEl.createDiv('deepseek-cli-loading-dot');
        this.loadingEl.createDiv('deepseek-cli-loading-dot');
        this.loadingEl.style.display = 'none';

        // Input area
        const inputArea = this.mainPanel.createDiv('deepseek-cli-input-area');

        // Context file chips
        this.chipsContainer = inputArea.createDiv('deepseek-cli-chips');

        // Badge indicators
        this.badgesRow = inputArea.createDiv('deepseek-cli-badges');

        const inputRow = inputArea.createDiv('deepseek-cli-input-row');

        // "+" button
        this.plusBtn = inputRow.createEl('button', { cls: 'deepseek-cli-plus-btn' });
        this.plusBtn.innerHTML = ICONS.plus;
        this.plusBtn.setAttribute('aria-label', 'Add context');
        this.plusBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            this.togglePopover();
        });

        this.inputEl = inputRow.createEl('textarea', {
            placeholder: 'Ask DeepSeek...',
            cls: 'deepseek-cli-input',
            attr: { rows: '2' }
        });
        this.sendBtn = inputRow.createEl('button', { cls: 'deepseek-cli-send-btn' });
        this.sendBtn.innerHTML = ICONS.send;
        this.sendBtn.addEventListener('click', () => {
            if (this.isGenerating) {
                this.stopGeneration();
            } else {
                this.sendMessage();
            }
        });

        // Popover menu
        this.popover = inputArea.createDiv('deepseek-cli-popover');
        this.popover.style.display = 'none';
        this.buildPopoverContent();

        // Close popover on outside click
        document.addEventListener('click', (e) => {
            if (this.popover && this.popover.style.display !== 'none') {
                if (!this.popover.contains(e.target) && e.target !== this.plusBtn) {
                    this.popover.style.display = 'none';
                }
            }
        });

        // Enter = newline; only clicking Send button sends the message
        this.inputEl.addEventListener('input', () => {
            this.inputEl.style.height = 'auto';
            this.inputEl.style.height = Math.min(this.inputEl.scrollHeight, 120) + 'px';
        });

        // Load state
        this.conversation = this.plugin.getActiveConversation();
        this.sidebarVisible = false;
        this.sidebar.style.display = 'none';
        this.contextFiles = [];
        this.planMode = false;
        this.permission = 'read-only';
        this.renderSidebar();
        this.renderAllMessages();
        this.renderChips();
        this.renderBadges();
        this.updateStatus();
        this.scrollToBottom();
    }

    async onClose() {
        await this.plugin.saveDataFull();
    }

    // ===== Sidebar =====
    toggleSidebar() {
        this.sidebarVisible = !this.sidebarVisible;
        this.sidebar.style.display = this.sidebarVisible ? 'flex' : 'none';
        if (this.toggleBtn) {
            this.toggleBtn.innerHTML = this.sidebarVisible ? ICONS.sidebarClose : ICONS.history;
            this.toggleBtn.setAttribute('aria-label', this.sidebarVisible ? 'Hide history' : 'Show history');
            if (this.sidebarVisible) {
                this.toggleBtn.addClass('deepseek-cli-toggle-active');
            } else {
                this.toggleBtn.removeClass('deepseek-cli-toggle-active');
            }
        }
    }

    renderSidebar() {
        this.convList.empty();
        const conversations = this.plugin.conversations || [];
        const activeId = this.conversation?.id;

        conversations.forEach(conv => {
            const item = this.convList.createDiv('deepseek-cli-sidebar-item');
            if (conv.id === activeId) item.addClass('deepseek-cli-sidebar-item-active');

            const info = item.createDiv('deepseek-cli-sidebar-item-info');
            info.createDiv({ text: conv.title || 'New Chat', cls: 'deepseek-cli-sidebar-item-title' });
            info.createDiv({ text: this.formatTime(new Date(conv.updatedAt)), cls: 'deepseek-cli-sidebar-item-time' });

            item.addEventListener('click', () => this.switchConversation(conv.id));

            // Delete button
            const delBtn = item.createEl('button', { cls: 'deepseek-cli-sidebar-del-btn', attr: { 'aria-label': 'Delete' } });
            delBtn.innerHTML = ICONS.trashSmall;
            delBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                this.deleteConversation(conv.id);
            });
        });
    }

    // ===== Conversation Management =====
    async newConversation() {
        this.conversation = this.plugin.createConversation();
        this.renderSidebar();
        this.renderAllMessages();
        this.updateStatus();
        await this.plugin.saveDataFull();
    }

    async switchConversation(id) {
        await this.plugin.saveDataFull();
        const conv = this.plugin.conversations.find(c => c.id === id);
        if (!conv) return;
        this.conversation = conv;
        this.plugin.activeConversationId = id;
        this.renderSidebar();
        this.renderAllMessages();
        this.updateStatus();
        this.scrollToBottom();
        await this.plugin.saveDataFull();
    }

    async deleteConversation(id) {
        this.plugin.conversations = this.plugin.conversations.filter(c => c.id !== id);
        if (this.plugin.activeConversationId === id) {
            if (this.plugin.conversations.length > 0) {
                this.plugin.activeConversationId = this.plugin.conversations[0].id;
                this.conversation = this.plugin.conversations[0];
            } else {
                this.conversation = this.plugin.createConversation();
            }
        }
        this.renderSidebar();
        this.renderAllMessages();
        this.updateStatus();
        await this.plugin.saveDataFull();
    }

    async clearChat() {
        if (!this.conversation) return;
        this.conversation.messages = [];
        this.conversation.title = '';
        this.conversation.totalTokens = 0;
        this.renderAllMessages();
        this.updateStatus();
        await this.plugin.saveDataFull();
    }

    // ===== Header / Status =====
    updateStatus() {
        this.headerStatus.empty();
        const s = this.plugin.settings;
        const isConfigured = s.apiKey && s.baseUrl && s.model;
        if (isConfigured) {
            this.headerStatus.setText(`✨ ${s.model}`);
        } else {
            this.headerStatus.setText('⚠ Configure API settings');
        }
        // Show total tokens for current conversation
        const total = this.conversation?.totalTokens || 0;
        if (total > 0) {
            this.headerStatus.createSpan({ text: ` | ${total.toLocaleString()} tokens`, cls: 'deepseek-cli-token-total' });
        }
    }

    // ===== Message Rendering =====
    renderAllMessages() {
        this.chatArea.empty();
        const messages = this.conversation?.messages || [];
        if (messages.length === 0) {
            this.renderWelcome();
            return;
        }
        messages.forEach(msg => this.renderMessage(msg));
    }

    renderWelcome() {
        const welcome = this.chatArea.createDiv('deepseek-cli-welcome');
        welcome.createEl('div', { cls: 'deepseek-cli-welcome-icon' }).innerHTML = ICONS.robot;
        welcome.createEl('h3', { text: 'DeepSeek CLI Chat' });
        welcome.createEl('p', { text: `Connected via ${this.plugin.settings.providerType === 'anthropic' ? 'Anthropic protocol' : 'OpenAI protocol'} · ${this.plugin.settings.model}` });
        const hints = welcome.createDiv('deepseek-cli-welcome-hints');
        hints.createEl('div', { text: '💡 Ask questions about your notes', cls: 'deepseek-cli-hint' });
        hints.createEl('div', { text: '✏️ Get help with writing and editing', cls: 'deepseek-cli-hint' });
        hints.createEl('div', { text: '💻 Get code explanations and snippets', cls: 'deepseek-cli-hint' });
    }

    renderMessage(msg) {
        const wrapper = this.chatArea.createDiv(`deepseek-cli-msg deepseek-cli-msg-${msg.role}`);

        // Header
        const msgHeader = wrapper.createDiv('deepseek-cli-msg-header');
        const avatar = msgHeader.createDiv('deepseek-cli-avatar');
        if (msg.role === 'user') {
            avatar.createSpan({ cls: 'deepseek-cli-avatar-icon' }).innerHTML = ICONS.userPerson;
            msgHeader.createSpan({ text: 'You', cls: 'deepseek-cli-msg-name' });
        } else {
            avatar.createSpan({ cls: 'deepseek-cli-avatar-icon' }).innerHTML = ICONS.robot;
            msgHeader.createSpan({ text: 'DeepSeek', cls: 'deepseek-cli-msg-name' });
            if (msg.model) msgHeader.createSpan({ text: msg.model, cls: 'deepseek-cli-model-tag' });
            if (msg.tokens) {
                const total = msg.tokens.input + msg.tokens.output;
                msgHeader.createSpan({ text: `${total.toLocaleString()} tokens`, cls: 'deepseek-cli-msg-tokens' });
            }
        }
        if (msg.timestamp) msgHeader.createSpan({ text: this.formatTime(new Date(msg.timestamp)), cls: 'deepseek-cli-msg-time' });

        // Body
        const body = wrapper.createDiv('deepseek-cli-msg-body');
        const content = body.createDiv('deepseek-cli-msg-content');
        if (msg.role === 'assistant' && msg.content) {
            MarkdownRenderer.render(this.app, msg.content, content, '', this.plugin);
            // add code copy buttons after render (next tick)
            setTimeout(() => this.addCodeCopyButtons(body), 0);
        } else {
            content.setText(msg.content);
        }

        // Action buttons for user
        if (msg.role === 'user' && msg.content) {
            const actions = wrapper.createDiv('deepseek-cli-msg-actions');
            this.createActionBtn(actions, ICONS.copy, 'Copy', () => this.copyMessageContent(msg.content));
            this.createActionBtn(actions, ICONS.edit, 'Edit', () => this.editUserMessage(msg));
        }

        // Action buttons for assistant
        if (msg.role === 'assistant' && msg.content && !msg.content.startsWith('**Error:**')) {
            const actions = wrapper.createDiv('deepseek-cli-msg-actions');
            this.createActionBtn(actions, ICONS.copy, 'Copy', () => this.copyMessageContent(msg.content));
            this.createActionBtn(actions, ICONS.refresh, 'Regenerate', () => this.regenerateMessage(msg));
            this.createActionBtn(actions, ICONS.trashSmall, 'Delete', () => this.deleteMessage(msg));
        }
    }

    createActionBtn(container, iconHtml, tooltip, onClick) {
        const btn = container.createEl('button', { cls: 'deepseek-cli-action-btn', attr: { 'aria-label': tooltip } });
        btn.innerHTML = iconHtml;
        btn.addEventListener('click', () => onClick());
    }

    formatTime(date) {
        const now = new Date();
        const isToday = date.toDateString() === now.toDateString();
        if (isToday) return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        return date.toLocaleDateString([], { month: 'short', day: 'numeric' });
    }

    addCodeCopyButtons(container) {
        const preEls = container.querySelectorAll('pre');
        preEls.forEach(pre => {
            if (pre.closest('.deepseek-cli-code-block')) return;
            const wrapper = document.createElement('div');
            wrapper.className = 'deepseek-cli-code-block';
            pre.parentNode.insertBefore(wrapper, pre);
            wrapper.appendChild(pre);

            const codeEl = pre.querySelector('code');
            let lang = '';
            if (codeEl) {
                const cls = codeEl.className.match(/language-(\w+)/);
                if (cls) lang = cls[1];
            }

            const header = document.createElement('div');
            header.className = 'deepseek-cli-code-header';
            const langLabel = document.createElement('span');
            langLabel.className = 'deepseek-cli-code-lang';
            langLabel.textContent = lang || 'code';
            header.appendChild(langLabel);

            const copyBtn = document.createElement('button');
            copyBtn.className = 'deepseek-cli-code-copy-btn';
            copyBtn.innerHTML = ICONS.codeCopy + ' Copy';
            copyBtn.addEventListener('click', () => {
                navigator.clipboard.writeText(pre.textContent || '').then(() => {
                    copyBtn.innerHTML = ICONS.codeCheck + ' Copied';
                    setTimeout(() => { copyBtn.innerHTML = ICONS.codeCopy + ' Copy'; }, 2000);
                });
            });
            header.appendChild(copyBtn);
            wrapper.insertBefore(header, pre);
        });
    }

    // ===== Message Actions =====
    async copyMessageContent(content) {
        await navigator.clipboard.writeText(content);
        new Notice('Copied');
    }

    async regenerateMessage(msg) {
        const messages = this.conversation.messages;
        const idx = messages.indexOf(msg);
        if (idx === -1) return;
        // Remove the assistant message and all messages after it, adjusting tokens
        const removed = this.conversation.messages.slice(idx);
        this.conversation.messages = this.conversation.messages.slice(0, idx);
        for (const m of removed) {
            if (m.tokens) {
                this.conversation.totalTokens = Math.max(0, (this.conversation.totalTokens || 0) - m.tokens.input - m.tokens.output);
            }
        }
        await this.plugin.saveDataFull();
        this.renderAllMessages();
        this.scrollToBottom();
        const lastUser = this.conversation.messages.filter(m => m.role === 'user').pop();
        if (lastUser) {
            this.inputEl.value = lastUser.content;
            this.sendMessage();
        }
    }

    async deleteMessage(msg) {
        const idx = this.conversation.messages.indexOf(msg);
        if (idx === -1) return;
        // Subtract tokens if deleting an assistant message with tokens
        if (msg.tokens) {
            this.conversation.totalTokens = Math.max(0, (this.conversation.totalTokens || 0) - msg.tokens.input - msg.tokens.output);
        }
        this.conversation.messages.splice(idx, 1);
        await this.plugin.saveDataFull();
        this.renderAllMessages();
        this.updateStatus();
        this.scrollToBottom();
    }

    async editUserMessage(msg) {
        // Trim the conversation to just before this message
        const idx = this.conversation.messages.indexOf(msg);
        if (idx === -1) return;
        // If there are assistant messages after this user message, remove them
        const removed = this.conversation.messages.slice(idx + 1);
        for (const m of removed) {
            if (m.tokens) {
                this.conversation.totalTokens = Math.max(0, (this.conversation.totalTokens || 0) - m.tokens.input - m.tokens.output);
            }
        }
        this.conversation.messages = this.conversation.messages.slice(0, idx);
        // Set the message text in input, then re-send
        this.inputEl.value = msg.content;
        this.inputEl.style.height = 'auto';
        this.inputEl.style.height = Math.min(this.inputEl.scrollHeight, 120) + 'px';
        this.inputEl.focus();
        // Place cursor at end
        this.inputEl.setSelectionRange(this.inputEl.value.length, this.inputEl.value.length);
        // Remove this user message from the conversation
        await this.plugin.saveDataFull();
        this.renderAllMessages();
        this.updateStatus();
        this.scrollToBottom();
    }

    // ===== Popover =====
    togglePopover() {
        if (this.popover.style.display === 'none') {
            this.popover.style.display = 'block';
        } else {
            this.popover.style.display = 'none';
        }
    }

    buildPopoverContent() {
        this.popover.empty();
        const items = [
            { icon: ICONS.addFiles, label: 'Add Files & Folders', desc: 'Attach vault files as context', action: () => { this.popover.style.display = 'none'; this.openFileSelector(); } },
            { icon: ICONS.plan, label: 'Plan Mode', desc: 'AI outlines a plan before executing', action: () => { this.popover.style.display = 'none'; this.togglePlanMode(); } },
            { icon: ICONS.sparkle, label: 'Polish Prompt', desc: 'AI improves your prompt wording', action: () => { this.popover.style.display = 'none'; this.polishPrompt(); } },
            { icon: this.permission === 'read-only' ? ICONS.lock : ICONS.unlock,
              label: 'Permission',
              desc: this.permission === 'read-only' ? 'Read-only mode' : 'Read & Write mode',
              action: () => { this.popover.style.display = 'none'; this.togglePermission(); } },
        ];
        items.forEach(item => {
            const el = this.popover.createDiv('deepseek-cli-popover-item');
            const iconSpan = el.createSpan('deepseek-cli-popover-item-icon');
            iconSpan.innerHTML = item.icon;
            const textDiv = el.createDiv('deepseek-cli-popover-item-text');
            textDiv.createDiv({ text: item.label, cls: 'deepseek-cli-popover-item-label' });
            textDiv.createDiv({ text: item.desc, cls: 'deepseek-cli-popover-item-desc' });
            el.addEventListener('click', item.action);
        });
    }

    // ===== Badges =====
    renderBadges() {
        this.badgesRow.empty();
        if (this.planMode) {
            const badge = this.badgesRow.createSpan('deepseek-cli-badge deepseek-cli-badge-plan');
            badge.innerHTML = ICONS.plan + ' Plan';
        }
        const permBadge = this.badgesRow.createSpan('deepseek-cli-badge');
        if (this.permission === 'read-only') {
            permBadge.addClass('deepseek-cli-badge-readonly');
            permBadge.innerHTML = ICONS.lock + ' Read-only';
        } else {
            permBadge.addClass('deepseek-cli-badge-readwrite');
            permBadge.innerHTML = ICONS.unlock + ' Read & Write';
        }
    }

    // ===== Chips =====
    renderChips() {
        if (!this.chipsContainer) return;
        this.chipsContainer.empty();
        this.contextFiles.forEach(filePath => {
            const chip = this.chipsContainer.createDiv('deepseek-cli-chip');
            const name = filePath.split('/').pop();
            chip.createSpan({ text: '📄 ' + name, cls: 'deepseek-cli-chip-name' });
            const removeBtn = chip.createSpan('deepseek-cli-chip-remove');
            removeBtn.innerHTML = ICONS.xSmall;
            removeBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                this.removeContextFile(filePath);
            });
        });
    }

    removeContextFile(filePath) {
        this.contextFiles = this.contextFiles.filter(f => f !== filePath);
        this.renderChips();
    }

    // ===== File Selector =====
    openFileSelector() {
        const allFiles = this.app.vault.getMarkdownFiles();
        const items = allFiles.map(f => ({
            path: f.path,
            name: f.path,
        }));
        new FileSelectModal(this.app, items, (selectedPaths) => {
            selectedPaths.forEach(p => {
                if (!this.contextFiles.includes(p)) {
                    this.contextFiles.push(p);
                }
            });
            this.renderChips();
        }).open();
    }

    // ===== Plan Mode =====
    togglePlanMode() {
        this.planMode = !this.planMode;
        this.renderBadges();
        // Rebuild popover to update labels/toggles
        this.buildPopoverContent();
    }

    // ===== Permission =====
    togglePermission() {
        this.permission = this.permission === 'read-only' ? 'read-write' : 'read-only';
        this.renderBadges();
        this.buildPopoverContent();
    }

    // ===== Polish Prompt =====
    async polishPrompt() {
        const text = this.inputEl.value.trim();
        if (!text) {
            new Notice('Enter a prompt to polish first.');
            return;
        }
        const s = this.plugin.settings;
        if (!s.apiKey || !s.baseUrl) {
            new Notice('Please configure API settings.');
            return;
        }

        // Show polishing state
        this.inputEl.disabled = true;
        this.inputEl.placeholder = 'Polishing...';
        const origBg = this.sendBtn.style.background;
        this.sendBtn.style.background = 'var(--text-warning)';

        try {
            const polishSystem = 'You are a prompt improvement assistant. Take the user\'s message and rewrite it to be clearer, more specific, and more effective. Only output the improved prompt, nothing else. Do not add explanations, quotes, or any other text.';
            let improved = '';

            if (s.providerType === 'anthropic') {
                const response = await requestUrl({
                    url: s.baseUrl.replace(/\/$/, '') + '/v1/messages',
                    method: 'POST',
                    headers: buildAnthropicHeaders(s.apiKey),
                    body: JSON.stringify({
                        model: s.model,
                        max_tokens: 1024,
                        system: polishSystem,
                        messages: [{ role: 'user', content: text }],
                        stream: false,
                    }),
                });
                const data = response.json;
                improved = data.content?.map(c => c.text).join('') || text;
            } else {
                const response = await requestUrl({
                    url: s.baseUrl.replace(/\/$/, '') + '/v1/chat/completions',
                    method: 'POST',
                    headers: buildOpenAIHeaders(s.apiKey),
                    body: JSON.stringify({
                        model: s.model,
                        messages: [
                            { role: 'system', content: polishSystem },
                            { role: 'user', content: text },
                        ],
                        stream: false,
                        temperature: 0.7,
                    }),
                });
                const data = response.json;
                improved = data.choices?.[0]?.message?.content || text;
            }

            this.inputEl.value = improved.trim();
            this.inputEl.style.height = 'auto';
            this.inputEl.style.height = Math.min(this.inputEl.scrollHeight, 120) + 'px';
            new Notice('Prompt polished ✨');
        } catch (err) {
            new Notice('Polish failed: ' + err.message);
        }

        this.inputEl.disabled = false;
        this.inputEl.placeholder = 'Ask DeepSeek...';
        this.sendBtn.style.background = origBg;
        this.inputEl.focus();
    }

    // ===== System Instructions =====
    getSystemInstructions() {
        const parts = [];
        if (this.planMode) {
            parts.push('You are in PLAN mode. Before implementing anything, output a concise plan outlining your approach step by step. Do NOT execute or make any changes yet — wait for the user to review and approve the plan before proceeding. End your plan with a clear ask for approval, e.g. "Shall I proceed with this plan?"');
        }
        if (this.permission === 'read-only') {
            parts.push('You are in READ-ONLY mode. Do NOT create, modify, or delete any files. You can only read and provide advice, explanations, and code snippets for the user to copy manually.');
        } else {
            parts.push('You have READ & WRITE access. You may create, modify, and delete files as needed to help the user.');
        }
        return parts.join('\n\n');
    }

    // ===== Read Context Files =====
    async readFileContent(filePath) {
        try {
            const file = this.app.vault.getAbstractFileByPath(filePath);
            if (file) {
                return await this.app.vault.read(file);
            }
        } catch (e) {
            console.error('Error reading file:', filePath, e);
        }
        return '';
    }

    // ===== Send Message =====
    scrollToBottom() {
        setTimeout(() => { this.chatArea.scrollTop = this.chatArea.scrollHeight; }, 50);
    }

    showLoading() { this.loadingEl.style.display = 'flex'; this.scrollToBottom(); }
    hideLoading() { this.loadingEl.style.display = 'none'; }

    setSendingState() {
        this.isGenerating = true;
        this.sendBtn.innerHTML = ICONS.stop;
        this.sendBtn.style.background = 'var(--text-error)';
        this.sendBtn.disabled = false;
        this.inputEl.disabled = true;
    }

    setIdleState() {
        this.isGenerating = false;
        this.sendBtn.innerHTML = ICONS.send;
        this.sendBtn.style.background = '';
        this.sendBtn.disabled = false;
        this.inputEl.disabled = false;
        this.abortController = null;
    }

    stopGeneration() {
        if (this.abortController) {
            this.abortController.abort();
        }
    }

    async sendMessage() {
        const text = this.inputEl.value.trim();
        if (!text) return;
        const s = this.plugin.settings;
        if (!s.apiKey || !s.baseUrl) {
            new Notice('Please configure API settings.');
            return;
        }

        this.inputEl.value = '';
        this.inputEl.style.height = 'auto';
        this.setSendingState();

        // Ensure conversation exists
        if (!this.conversation) this.conversation = this.plugin.createConversation();

        // Set title from first message
        if (!this.conversation.title) {
            this.conversation.title = text.slice(0, 50) + (text.length > 50 ? '...' : '');
        }

        // Remove welcome
        const welcomeEl = this.chatArea.querySelector('.deepseek-cli-welcome');
        if (welcomeEl) welcomeEl.remove();

        // Build user message with context
        let userText = text;
        if (this.contextFiles.length > 0) {
            let contextStr = '';
            for (const filePath of this.contextFiles) {
                const content = await this.readFileContent(filePath);
                if (content) {
                    contextStr += `\n\n<context file="${filePath}">\n${content}\n</context>`;
                }
            }
            if (contextStr) {
                userText = `${text}\n\n--- Context Files ---${contextStr}`;
            }
        }

        // Append user message
        const userMsg = { role: 'user', content: userText, timestamp: Date.now() };
        this.conversation.messages.push(userMsg);
        this.renderMessage(userMsg);
        this.scrollToBottom();

        this.showLoading();

        const assistantMsg = { role: 'assistant', content: '', model: s.model, timestamp: Date.now() };

        this.abortController = new AbortController();
        const abortPromise = new Promise((_, reject) => {
            this.abortController.signal.addEventListener('abort', () => {
                reject(new DOMException('Aborted', 'AbortError'));
            });
        });

        try {
            let response, data;
            const apiMessages = this.conversation.messages.filter(m => m.content);
            const systemInstructions = this.getSystemInstructions();

            if (s.providerType === 'anthropic') {
                const body = { model: s.model, max_tokens: 4096, messages: toAnthropicMessages(apiMessages), stream: false };
                if (systemInstructions) body.system = systemInstructions;
                response = await Promise.race([
                    requestUrl({
                        url: s.baseUrl.replace(/\/$/, '') + '/v1/messages',
                        method: 'POST',
                        headers: buildAnthropicHeaders(s.apiKey),
                        body: JSON.stringify(body),
                    }),
                    abortPromise,
                ]);
                data = response.json;
                assistantMsg.content = data.content?.map(c => c.text).join('') || '';
                assistantMsg.tokens = data.usage ? {
                    input: data.usage.input_tokens || 0,
                    output: data.usage.output_tokens || 0,
                } : null;
            } else {
                let messages = toOpenAIMessages(apiMessages);
                if (systemInstructions) {
                    messages = [{ role: 'system', content: systemInstructions }, ...messages];
                }
                response = await Promise.race([
                    requestUrl({
                        url: s.baseUrl.replace(/\/$/, '') + '/v1/chat/completions',
                        method: 'POST',
                        headers: buildOpenAIHeaders(s.apiKey),
                        body: JSON.stringify({ model: s.model, messages, stream: false, temperature: 0.7 }),
                    }),
                    abortPromise,
                ]);
                data = response.json;
                assistantMsg.content = data.choices?.[0]?.message?.content || '';
                assistantMsg.tokens = data.usage ? {
                    input: data.usage.prompt_tokens || 0,
                    output: data.usage.completion_tokens || 0,
                } : null;
            }
            if (!assistantMsg.content) assistantMsg.content = '_(empty response)_';
        } catch (err) {
            if (err.name === 'AbortError' || err.message?.includes('abort')) {
                assistantMsg.content = '⏹ _Generation stopped._';
            } else {
                assistantMsg.content = `**Error:** ${err.message}`;
                console.error('API error:', err);
            }
        }

        this.hideLoading();
        assistantMsg.timestamp = Date.now();
        this.conversation.messages.push(assistantMsg);
        // Track total tokens
        if (assistantMsg.tokens) {
            this.conversation.totalTokens = (this.conversation.totalTokens || 0) +
                assistantMsg.tokens.input + assistantMsg.tokens.output;
        }
        this.conversation.updatedAt = Date.now();
        this.renderMessage(assistantMsg);
        this.scrollToBottom();

        this.setIdleState();
        this.renderSidebar();
        this.plugin.activeConversationId = this.conversation.id;
        await this.plugin.saveDataFull();
    }
}

// ====== Settings Tab ======
class DeepSeekCLISettingTab extends PluginSettingTab {
    constructor(app, plugin) {
        super(app, plugin);
        this.plugin = plugin;
    }

    display() {
        const { containerEl } = this;
        containerEl.empty();
        containerEl.createEl('h2', { text: 'DeepSeek CLI Chat Settings' });
        containerEl.createEl('p', { text: 'Configure the API provider. These settings should match your DeepSeek CLI environment variables.', cls: 'setting-item-description' });

        new Setting(containerEl)
            .setName('Protocol')
            .setDesc('Anthropic for DeepSeek Anthropic API, OpenAI for OpenAI-compatible APIs')
            .addDropdown(d => d.addOption('anthropic', 'Anthropic').addOption('openai', 'OpenAI')
                .setValue(this.plugin.settings.providerType)
                .onChange(async v => { this.plugin.settings.providerType = v; await this.plugin.saveSettings(); }));

        new Setting(containerEl)
            .setName('Base URL').setDesc('API base URL (e.g. https://api.deepseek.com/anthropic)')
            .addText(t => t.setPlaceholder('https://api.deepseek.com/anthropic').setValue(this.plugin.settings.baseUrl)
                .onChange(async v => { this.plugin.settings.baseUrl = v; await this.plugin.saveSettings(); }));

        new Setting(containerEl)
            .setName('API Key').setDesc('Your API key')
            .addText(t => {
                t.setPlaceholder('sk-...').setValue(this.plugin.settings.apiKey)
                    .onChange(async v => { this.plugin.settings.apiKey = v; await this.plugin.saveSettings(); });
                t.inputEl.type = 'password';
                t.inputEl.addClass('deepseek-cli-api-key-input');
            })
            .addExtraButton(btn => btn.setIcon('eye').setTooltip('Show API key').onClick(() => {
                const inputEl = containerEl.querySelector('.deepseek-cli-api-key-input');
                const isPw = inputEl.type === 'password';
                inputEl.type = isPw ? 'text' : 'password';
                btn.setIcon(isPw ? 'eye-off' : 'eye');
                btn.setTooltip(isPw ? 'Hide API key' : 'Show API key');
            }));

        new Setting(containerEl)
            .setName('Model').setDesc('Model name (e.g. deepseek-v4-pro)')
            .addText(t => t.setPlaceholder('deepseek-v4-pro').setValue(this.plugin.settings.model)
                .onChange(async v => { this.plugin.settings.model = v; await this.plugin.saveSettings(); }));

        new Setting(containerEl)
            .setName('Available Models').setDesc('Comma-separated list of models for the selector dropdown')
            .addText(t => t.setPlaceholder('deepseek-v4-pro, deepseek-chat, deepseek-reasoner').setValue(this.plugin.settings.models || '')
                .onChange(async v => { this.plugin.settings.models = v; await this.plugin.saveSettings(); }));

        containerEl.createEl('hr');
        containerEl.createEl('p', { text: 'Tip: Your DeepSeek CLI settings come from ~/.zshrc environment variables (DEEPSEEK_PROVIDER_TYPE, DEEPSEEK_PROVIDER_BASE_URL, DEEPSEEK_PROVIDER_API_KEY, DEEPSEEK_MODEL). Keep them in sync.', cls: 'setting-item-description' });
    }
}

// ====== Plugin ======
class DeepSeekCLIPlugin extends Plugin {
    async onload() {
        console.log('Loading DeepSeek CLI Chat plugin');
        await this.loadSettings();
        this.conversations = [];
        this.activeConversationId = null;
        await this.loadConversations();

        this.addSettingTab(new DeepSeekCLISettingTab(this.app, this));
        this.registerView(VIEW_TYPE, (leaf) => new DeepSeekChatView(leaf, this));

        this.addRibbonIcon(ICONS.robot, 'Open DeepSeek CLI Chat', () => this.activateView());
        this.addCommand({ id: 'open-deepseek-cli-chat', name: 'Open DeepSeek CLI Chat', callback: () => this.activateView() });

        this.app.workspace.onLayoutReady(() => this.activateView());
    }

    async onunload() { console.log('Unloading DeepSeek CLI Chat plugin'); }

    // ===== Settings =====
    async loadSettings() {
        const data = await this.loadData();
        this.settings = Object.assign({}, DEFAULT_SETTINGS);
        if (data) {
            this.conversations = data.conversations || [];
            this.activeConversationId = data.activeConversationId || null;
            for (const key of Object.keys(DEFAULT_SETTINGS)) {
                if (key in data) this.settings[key] = data[key];
            }
        }
    }

    async saveSettings() {
        await this.saveDataFull();
        const leaves = this.app.workspace.getLeavesOfType(VIEW_TYPE);
        for (const leaf of leaves) {
            if (leaf.view instanceof DeepSeekChatView) leaf.view.updateStatus();
        }
    }

    // ===== Conversations =====
    async loadConversations() {
        const data = await this.loadData();
        if (data) {
            this.conversations = data.conversations || [];
            this.activeConversationId = data.activeConversationId || null;
        }
    }

    async saveDataFull() {
        await this.saveData({
            conversations: this.conversations,
            activeConversationId: this.activeConversationId,
            ...this.settings,
        });
    }

    createConversation() {
        const conv = {
            id: uid(),
            title: '',
            messages: [],
            createdAt: Date.now(),
            updatedAt: Date.now(),
        };
        this.conversations.unshift(conv);
        this.activeConversationId = conv.id;
        return conv;
    }

    getActiveConversation() {
        if (!this.activeConversationId && this.conversations.length > 0) {
            this.activeConversationId = this.conversations[0].id;
        }
        if (!this.activeConversationId) return null;
        return this.conversations.find(c => c.id === this.activeConversationId) || null;
    }

    async activateView() {
        const { workspace } = this.app;
        let leaf = workspace.getLeavesOfType(VIEW_TYPE)[0];
        if (!leaf) {
            leaf = workspace.getRightLeaf(false);
            await leaf.setViewState({ type: VIEW_TYPE, active: true });
        }
        workspace.revealLeaf(leaf);
    }
}

module.exports = DeepSeekCLIPlugin;

/* nosourcemap */