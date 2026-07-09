---
title: "OSG Reading Color CSS Guide"
aliases: ["Knowledge Design Reading Layer", "Obsidian CSS Companion Colors", "Document Styling Guide"]
tags: [systems, engineering, toolkit, obsidian, css, visual-design, knowledge-design, alpha-proxima]
created: 2026-07-09
updated: 2026-07-09
status: active
version: "1.0.0"
authors: ["Claude Code Architect"]
artifact_type: implementation-guide
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
dependencies: ["[[Graph View Color System]]", "[[ALPHAPROXIMA Enterprise Knowledge Architecture v1.0]]"]
related_documents: ["[[Color System - Implementation Checklist]]", "[[Graph View Color System]]", "[[Alpha Proxima Engineering Toolkit]]"]
related_research_programs: []
---

# OSG Reading Color CSS Guide

## Purpose

This guide explains how to enable, configure, and use the **OSG Knowledge Design System CSS snippet** (`osg-knowledge-design.css`).

The CSS snippet transforms Obsidian's reading layer—headings, callouts, code blocks, and metadata—into a visually structured document experience that reflects Alpha Proxima's companion-based knowledge architecture.

This layer complements the [[Graph View Color System]] by styling *document content* (what you read/write) while the graph styles *document nodes* (how the vault looks as a network).

---

## Quick Start

### Step 1: Enable the CSS Snippet

1. Open Obsidian
2. Navigate to **Settings → Appearance → CSS snippets**
3. Look for **`osg-knowledge-design`** in the list
4. Toggle the switch to enable it (checkbox should be checked ✓)
5. Close Settings

**Result:** Document headings and callouts now render with companion colors.

### Step 2: Verify it's Working

1. Open any note in your vault
2. Check that:
   - H1 headings have a purple underline (LUMIAION color: #7C3AED)
   - H2 headings have a colored left border
   - Callouts appear with background colors matching their type

If you see colored borders but no background colors, verify the snippet is enabled (toggle should show as "on").

### Step 3: Use Companion-Specific Colors

To apply companion colors to a document, add the companion name to the file path:

- Place a document in a folder containing `SOHMA` → headings render in purple
- Place a document in a folder containing `ATHENA` → headings render in blue
- Place a document in a folder containing `VORTEX` → headings render in green
- Place a document in a folder containing `JERANIUM` → headings render in teal
- Place a document in a folder containing `GAIA` → headings render in emerald (future)
- Place a document in a folder containing `ORION` → headings render in sky blue (future)

Example paths that trigger companion colors:

```
03_AI_COUNCIL/Departments/SOHMA Charter.md        → SOHMA purple
03_AI_COUNCIL/Departments/ATHENA Charter.md       → ATHENA blue
03_AI_COUNCIL/Departments/JERANIUM Charter.md     → JERANIUM teal
03_AI_COUNCIL/Departments/VORTEX Charter.md       → VORTEX green
```

---

## Color Palette

The CSS defines a complete color system aligned with Alpha Proxima companions:

### Core Companions

| Companion | Primary Color | Hex | Meaning |
|-----------|---------------|-----|---------|
| **LUMIAION** | Violet | `#7C3AED` | Constitutional Intelligence Core; central orchestration |
| **SOHMA** | Purple | `#9333EA` | Consciousness, meaning, interiority, symbolism |
| **ATHENA** | Blue | `#1D4ED8` | Health, biology, training, longevity, knowledge |
| **VORTEX** | Green | `#65A30D` | Finance, economics, strategy, resource flow |
| **JERANIUM** | Teal | `#0F766E` | Knowledge architecture, research, data, patterns |

### Future Companions

| Companion | Primary Color | Hex | Meaning |
|-----------|---------------|-----|---------|
| **GAIA** | Emerald | `#10b981` | (Planned) Natural systems, ecology, harmony |
| **ORION** | Sky Blue | `#0284c7` | (Planned) Cosmic perspective, expansion, vision |

---

## Styled Elements

### Headings (H1, H2, H3)

Headings automatically color-code based on document companion:

```markdown
# Title (H1)
- Large, bold
- Underlined with companion color
- Bottom border: 3px solid

## Section (H2)
- Left border: 4px solid companion color
- Darker text shade

### Subsection (H3)
- Left border: 2px solid companion color
- Tertiary emphasis
```

**Companion Detection:** Based on file path. If your file path contains `SOHMA`, all headings render in purple. If it contains `ATHENA`, they render in blue, etc.

### Callouts

Obsidian's native callout blocks (using `> [!type]` syntax) are styled with companion colors:

```markdown
> [!sohma]
> SOHMA perspective on this topic
> (renders with purple background and border)

> [!athena]
> ATHENA health/training insight
> (renders with blue background and border)

> [!vortex]
> VORTEX financial or strategic analysis
> (renders with green background and border)

> [!jeranium]
> JERANIUM research finding or pattern
> (renders with teal background and border)

> [!gaia]
> GAIA ecosystem or natural systems view
> (renders with emerald background and border - future)

> [!orion]
> ORION cosmic or expansive perspective
> (renders with sky blue background and border - future)
```

### Toggle/Details Blocks

Obsidian's collapsible `<details>` blocks are styled with neutral backgrounds:

```html
<details>
<summary>Click to expand</summary>

Content here. Auto-styled with subtle borders and hover effects.

</details>
```

### Code Blocks

Code blocks render with:
- Dark background (#1e293b)
- Left border in LUMIAION violet
- Light text for contrast

```python
# Python code example
# Auto-styled with dark background and colored border
def hello():
    return "styled code"
```

### Tables

Tables render with:
- Light gray headers with LUMIAION border
- Alternating row backgrounds on hover
- Clear visual hierarchy

### Inline Code & Links

- **Inline code** → light background with teal text
- **Links** → LUMIAION violet, underline on hover
- **Tags** → Companion-specific backgrounds if tagged `#companion/sohma`, `#companion/athena`, etc.

### Blockquotes

Blockquotes render with:
- Left border in neutral gray
- Italic text
- Subdued color for visual de-emphasis

---

## How to Use Companion-Specific Colors

### Method 1: Automatic (File Path Matching) ✅ Recommended

Place documents in companion-specific folders:

```
03_AI_COUNCIL/Departments/SOHMA Charter.md
03_AI_COUNCIL/Departments/ATHENA Charter.md
03_AI_COUNCIL/Departments/JERANIUM Charter.md
03_AI_COUNCIL/Departments/VORTEX Charter.md
```

The CSS automatically detects the companion name in the file path and applies corresponding colors to all headings.

**How it works:**
- The CSS contains rules like `.file-path-contains-sohma h1 { color: #9333EA; }`
- Obsidian's CSS sandbox supports file path matching via dynamic class names
- No manual tagging or frontmatter required

### Method 2: Tag-Based (Manual Tagging)

Add companion tags to documents for inline colored highlights:

```markdown
---
title: "Document About SOHMA"
tags: [systems, companion/sohma]
---

# Topic

This paragraph is about consciousness.

Use `#companion/sohma` tags inline to highlight companion-specific references.
```

Any tag matching `#companion/[name]` will render with the corresponding companion background color.

### Method 3: Callout-Based (Inline Perspective)

Use callout blocks to signal which companion perspective is presented:

```markdown
> [!sohma]
> **SOHMA Perspective:** Consciousness emerges from...

> [!athena]
> **ATHENA Perspective:** Biologically, this means...

> [!vortex]
> **VORTEX Perspective:** Economically, the ROI is...
```

Each callout type renders with its companion's colors and a distinctive background.

---

## CSS Architecture

### Variables (Root)

All colors are defined as CSS custom properties (variables) at `:root`:

```css
:root {
  --color-lumiaion-primary: #7C3AED;
  --color-sohma-primary: #9333EA;
  --color-athena-primary: #1D4ED8;
  /* ... etc ... */
}
```

**Why:** Easy to update all companion colors in one place. Change `--color-sohma-primary` and every SOHMA element updates instantly.

### File Path Matching

CSS selectors like `.file-path-contains-sohma h1` work because Obsidian dynamically assigns classes to elements based on the open file's path.

**Example:**
```css
.file-path-contains-sohma h1 {
  border-bottom-color: #9333EA;
  color: #581c87;
}
```

When you open `SOHMA Charter.md`, Obsidian assigns the class `.file-path-contains-sohma` to the document container, and this rule applies.

### Dark Mode Support

The CSS includes dark mode overrides:

```css
body.theme-dark .markdown-preview-view h1 {
  color: #f1f5f9;  /* Light text on dark background */
}
```

Colors adapt automatically when you switch Obsidian to dark theme.

### Responsive Design

Mobile and tablet breakpoints adjust font sizes and spacing:

- **Mobile (<640px):** Smaller headings, tighter spacing
- **Tablet/Desktop:** Full-size headings, comfortable margins
- **Print:** Page-break-avoid rules prevent awkward splits

---

## Limitations of CSS in Obsidian

### What CSS Can Do

✅ Style headings, lists, code blocks  
✅ Color text and backgrounds  
✅ Adjust fonts, spacing, borders  
✅ Respond to file paths and CSS classes  
✅ Dark/light mode switching  
✅ Responsive design (mobile, tablet, desktop)  

### What CSS Cannot Do

❌ Access frontmatter fields directly (e.g., can't read `companion: sohma` from YAML)  
❌ Dynamically load content (CSS is read-only)  
❌ Perform conditional logic beyond CSS rules  
❌ Modify document content (headings, text, images)  
❌ Override Obsidian's plugin behavior  
❌ Execute JavaScript (Obsidian restricts JS in snippets for security)  

### Workaround: Custom CSS Classes

If you need frontmatter-based styling, you can:

1. Use Obsidian plugins like **Templater** or **Dataview** to inject CSS classes into frontmatter
2. Use manual tags (`#companion/sohma`) for inline companion styling
3. Use file path organization (folder naming) for automatic companion detection

**Recommended approach:** Organize documents by companion (folder names), use callout blocks for explicit perspective marking, and use tags for inline references.

---

## Customization

### Changing Colors

To change companion colors globally:

1. Open `.obsidian/snippets/osg-knowledge-design.css` in your editor
2. Find the `:root` section at the top
3. Update the color hex codes:

```css
:root {
  --color-sohma-primary: #9333EA;  /* Change this */
  /* ... */
}
```

4. Save the file
5. Reload Obsidian (Settings → Reload)

All SOHMA elements update instantly.

### Adding New Companions

To add a new companion (e.g., GAIA or ORION):

1. Add CSS variables for the new companion:

```css
:root {
  --color-gaia-primary: #10b981;
  --color-gaia-light: #d1fae5;
  --color-gaia-border: #6ee7b7;
}
```

2. Add file path matching rules:

```css
.file-path-contains-gaia h1 {
  border-bottom-color: #10b981;
}

.file-path-contains-gaia h2 {
  border-left-color: #10b981;
  color: #065f46;
}
```

3. Add callout variant:

```css
.callout[data-callout="gaia"] {
  border-left-color: #10b981;
  background: #d1fae5;
}
```

4. Save and reload.

### Disabling Specific Styles

To disable a style (e.g., hide callout backgrounds), add `display: none;` or comment out the rule:

```css
/* Disable callout backgrounds */
.callout {
  /* background: var(--color-neutral-light); */ /* Commented out */
}
```

---

## Troubleshooting

### Snippet is Enabled but Styles Don't Appear

**Cause:** Obsidian cache issue.

**Solution:**
1. Settings → Appearance → CSS Snippets
2. Click the refresh icon (↻) next to the snippet name
3. Close and reopen Obsidian

### Headings Don't Change Color When Moving Files

**Cause:** File path matching is static; Obsidian caches class names.

**Solution:**
1. Close the file
2. Reload Obsidian (Ctrl+Shift+R / Cmd+Shift+R)
3. Reopen the file

### Companion Colors Not Matching Graph Colors Exactly

**Intentional Design Decision:**
- Graph View colors are optimized for node visibility in the graph network
- Reading Layer colors are optimized for text readability and document aesthetics
- They use the same *companion identity* but may differ slightly in hex values to improve contrast and readability

Example: LUMIAION is violet (`#7C3AED`) in the graph but uses both violet and gold (`#F59E0B`) in the reading layer for flexibility.

### Dark Mode Colors Are Hard to Read

**Cause:** Dark mode overrides may not cover all elements.

**Solution:**
1. Report the specific element in the vault
2. Add a dark mode override to `.obsidian/snippets/osg-knowledge-design.css`:

```css
body.theme-dark .your-element {
  color: #your-light-color;
  background: #your-dark-background;
}
```

---

## Best Practices

### 1. Organize by Companion

Structure your documents to align with companion focus:

```
03_AI_COUNCIL/Departments/
  ├── SOHMA Charter.md           (consciousness, meaning)
  ├── ATHENA Charter.md          (health, knowledge)
  ├── VORTEX Charter.md          (finance, strategy)
  └── JERANIUM Charter.md        (research, data)
```

This enables automatic companion coloring in headings.

### 2. Use Callouts for Multi-Perspective Documents

In documents where multiple companions weigh in:

```markdown
# Decision Topic

## Analysis

> [!athena]
> **ATHENA View:** The health implications are...

> [!vortex]
> **VORTEX View:** The financial impact is...

> [!jeranium]
> **JERANIUM View:** The data shows...
```

### 3. Tag Companion References

Use `#companion/[name]` tags to highlight perspective shifts:

```markdown
This section explores [[SOHMA]] thinking #companion/sohma about consciousness.

By contrast, [[ATHENA]] research #companion/athena suggests...
```

### 4. Use Code Blocks for Structure

Mark companion-specific code or examples with labeled blocks:

```python
# JERANIUM data pattern
data = [...]  # Styled with dark background and colored border
```

### 5. Leverage Blockquotes for Emphasis

Use blockquotes for important companion perspectives:

```markdown
> SOHMA reminds us that consciousness is not binary—it exists on a spectrum.
```

---

## Integration with Other Systems

### Graph View Color System

- **Graph:** Node colors (whole-vault navigation)
- **Reading Layer:** Document content colors (individual document reading)

Both systems use the same companion definitions but optimize for different contexts.

**Alignment:** A document in `SOHMA Charter.md` renders:
- Violet in the Graph View (node color)
- Purple headings and callouts in the Reading Layer (content color)

### Knowledge Design System

The CSS snippet implements the visual layer of the broader Knowledge Design System:

- **Knowledge Graph Architecture:** Defines what knowledge is (node/relationship types)
- **Reading Layer CSS:** Defines how knowledge looks (visual presentation)
- **Graph View Colors:** Defines how knowledge connects (network visualization)

Together, these create a coherent visual and structural language across the vault.

---

## Future Enhancements

### Planned

- [ ] Frontmatter-based companion styling (requires Obsidian plugin or custom JS)
- [ ] GAIA and ORION companion colors (after formal charter ratification)
- [ ] Animated transitions between callout types
- [ ] Custom fonts for specific companions
- [ ] Print stylesheet optimization
- [ ] Accessibility audit (WCAG AAA compliance)

### Possible

- [ ] Theme variants (e.g., "high contrast," "minimal," "academic")
- [ ] Export-to-PDF styling preservation
- [ ] Live preview of companion color swatches in settings
- [ ] CSS variable editor UI in Obsidian settings

---

## Resources

### Internal Documentation

- [[Graph View Color System]] — Node coloring and graph layout rules
- [[Color System - Implementation Checklist]] — Implementation status tracking
- [[ALPHAPROXIMA Enterprise Knowledge Architecture v1.0]] — Master reference for all systems
- [[Alpha Proxima Engineering Toolkit]] — Engineering documentation index

### External References

- [Obsidian CSS Snippets Documentation](https://help.obsidian.md/Customization/CSS+snippets)
- [Obsidian Theme Development](https://docs.obsidian.md/Themes/Obsidian+Publish)
- [MDN CSS Custom Properties (Variables)](https://developer.mozilla.org/en-US/docs/Web/CSS/--*)

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-09 | Claude Code Architect | Initial OSG Knowledge Design System CSS and guide. Companion colors, heading/callout styling, file path matching, dark mode support, responsive design. |

---

## Support & Feedback

For issues with the CSS snippet:

1. Check the **Troubleshooting** section above
2. Verify the snippet is enabled in **Settings → Appearance → CSS Snippets**
3. Try the **Refresh CSS** option
4. Report issues to [[Alpha Proxima Engineering Toolkit]] with:
   - Obsidian version
   - CSS snippet version (1.0.0)
   - Screenshot of the issue
   - Steps to reproduce

