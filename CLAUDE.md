# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Workflow Orchestration

### 1. Plan Mode Default

* Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions).
* If something goes sideways, STOP and re-plan immediately—don't keep pushing.
* Use plan mode for verification steps, not just building.
* Write detailed specs upfront to reduce ambiguity.

### 2. Subagent Strategy

* Use subagents liberally to keep main context window clean.
* Offload research, exploration, and parallel analysis to subagents.
* For complex problems, throw more compute at it via subagents.
* One **task** per subagent for focused execution.

### 3. Self-Improvement Loop

* After ANY correction from the user: update `tasks/lessons.md` with the pattern.
* Write rules for yourself that prevent the same mistake.
* Ruthlessly iterate on these lessons until mistake rate drops.
* Review lessons at session start for relevant project.

### 4. Verification Before Done

* Never mark a task complete without proving it works.
* Diff behavior between main and your changes when relevant.
* Ask yourself: "Would a staff engineer approve this?"
* Run tests, check logs, demonstrate correctness.

### 5. Demand Elegance (Balanced)

* For non-trivial changes: pause and ask "is there a more elegant way?"
* If a fix feels hacky: "Knowing everything I know now, implement the elegant solution."
* Skip this for simple, obvious fixes—don't over-engineer.
* Challenge your own work before presenting it.

### 6. Autonomous Bug Fixing

* When given a bug report: just fix it. Don't ask for hand-holding.
* Point at logs, errors, failing tests—then resolve them.
* Zero context switching required from the user.
* Go fix failing CI tests without being told how.

---

## Task Management

1. **Plan First**: Write plan to `tasks/todo.md` with checkable items.
2. **Verify Plan**: Check in before starting implementation.
3. **Track Progress**: Mark items complete as you go.
4. **Explain Changes**: High-level summary at each step.
5. **Document Results**: Add review section to `tasks/todo.md`.
6. **Capture Lessons**: Update `tasks/lessons.md` after corrections.

---

## Core Principles

* **Simplicity First**: Make every change as simple as possible. Impact minimal code.
* **No Laziness**: Find root causes. No temporary fixes. Senior developer standards.
* **Minimal Impact**: Changes should only touch what's necessary. Avoid introducing bugs.

---

## Project Overview

**omarora.in** is a personal knowledge repository and professional portfolio built with Hugo, a fast static site generator. The site documents research and writing across 8 knowledge domains: mathematics, theoretical physics, astronomy, quantitative finance, philosophy, history, art/music, and personal blog posts.

**Key characteristics:**
- Static site (no backend/database)
- Content-driven architecture (all data in Markdown files)
- Academic/professional focus with math support (LaTeX/KaTeX)
- Automatic deployment via GitHub Actions on push to main
- Custom theme based on minimal-academic with extensive template overrides

## Common Development Commands

```bash
# Local development server (live reload on file changes)
hugo server

# Build production site (minified, garbage collected)
hugo --gc --minify

# Build with specific base URL (for testing different domains)
hugo --gc --minify --baseURL "https://example.com/"

# Clean rebuild (remove old build artifacts first)
rm -rf public/ && hugo --gc --minify

# Check site for issues
hugo --gc --minify  # Any errors will print during build
```

## Content Structure

### Organizing Content

The site uses topic-based hierarchical organization in `/content/`:

```
content/
├── blog/                          # Personal writing and reflections
├── mathematics/                   # Math education and notes
├── theoretical-physics/           # Physics research and education
├── astronomy/                     # Astronomy and cosmology
├── quantitative-finance/          # Finance research and projects
├── philosophy/                    # Philosophy and critical thinking
├── history/                       # Historical perspectives
├── art-music/                     # Creative content
├── _index.md                      # Homepage (professional profile)
└── now.md                         # Current work/activities
```

### Adding New Pages

1. **Create a new Markdown file** in the appropriate subdirectory
2. **Add frontmatter** with required metadata:
```yaml
---
title: "Page Title"
date: 2026-03-30
tags: ["tag1", "tag2"]
summary: "Brief description for listings"
---
```

3. **Write content** in Markdown with support for:
   - **LaTeX math**: `$inline$` and `$$display$$` or `\(inline\)` and `\[display\]`
   - **Raw HTML**: Enabled for complex layouts
   - **Standard Markdown**: Full GFM support

### Menu Hierarchy

The site navigation menu is defined in `hugo.yaml` (not auto-generated). When adding major sections or subsections, you must update the menu structure in `hugo.yaml`:

```yaml
menu:
  main:
    - identifier: "section-name"
      name: "Display Name"
      url: "/section-name/"
      weight: 1
    - identifier: "subsection-name"
      name: "Subsection Title"
      url: "/section-name/subsection/"
      parent: "section-name"
      weight: 1
```

**Keep menu.main in sync with content structure** — mismatches will cause broken navigation.

## Key Configuration Files

### `hugo.yaml` — Main Hugo Configuration

**Important sections:**
- **baseURL**: `https://omarora.in/` — Change for different deployment
- **menu.main**: Site navigation structure (30+ items, must update when adding sections)
- **markup.goldmark.extensions.passthrough**: Math delimiter configuration
  - Block math: `$$...$$` and `\[...\]`
  - Inline math: `$...$` and `\(...\)`
- **params**: Author, SEO keywords, social links (Twitter, GitHub, ORCID, Google Scholar, etc.)

### `.github/workflows/hugo.yaml` — CI/CD Pipeline

**Build process:**
- Installs Hugo Extended v0.128.0
- Runs with flags: `--gc --minify --baseURL "https://omarora.in/"`
- Deploys to GitHub Pages automatically on push to main
- Can be manually triggered via "Run workflow" button

**Note**: Repository has both GitHub Pages and Netlify configurations (netlify.toml). GitHub Actions is the active deployment method.

### `.gitignore` — Build Artifacts

**Already ignored (don't commit):**
- `/public/` — Built site output
- `/isableFastRender/` — Build cache
- `.hugo_build.lock` — Build lock file
- `*.metadata.json`, `*.resolved` — Hugo metadata files
- Editor configs (`.vscode/`, `.idea/`)

## Theme & Customization

### Layout System

Custom layouts in `/layouts/` override theme templates:

| File | Purpose |
|------|---------|
| `_default/baseof.html` | Main page template (two-column layout with sidebar) |
| `_default/single.html` | Individual article layout |
| `_default/list.html` | Section/category listing layout |
| `handouts/list.html` | Specialized resource list layout |
| `index.html` | Homepage with profile section |

**To modify layout**: Edit files in `/layouts/_default/` or create new layouts as needed.

### Styling

**Custom CSS**: `/static/css/style.css` (743 lines)

**Design system:**
- **Background**: Warm beige (`#f7f5f0`)
- **Text**: Dark ink (`#0d1525`)
- **Accent**: Blue (`#1a3a5c`)
- **Fonts**: EB Garamond (serif, body text), JetBrains Mono (code)
- **Sidebar width**: 240px (responsive collapse on mobile)

**Update CSS** directly in `/static/css/style.css` — changes are live after `hugo server` reload.

### Math Rendering

**KaTeX** is loaded from CDN (v0.16.9) in the base layout for instant math rendering. Delimiters are configured in `hugo.yaml` — don't change them without updating both the config and any documentation about math syntax.

## Deployment & CI/CD

### GitHub Pages (Active)

- **Trigger**: Automatic deploy on any push to `main` branch
- **Or manual**: Visit GitHub Actions tab → "Deploy Hugo site to omarora.in" → "Run workflow"
- **Domain**: https://omarora.in/ (via CNAME record in `/static/CNAME`)
- **Build time**: ~10-20 seconds
- **HTTPS**: Automatic via GitHub Pages

### Netlify (Ready but Inactive)

Configuration exists in `netlify.toml` if you need to switch. Same build process (`hugo --gc --minify`).

## Important Notes & Quirks

1. **LaTeX Math Delimiters**: Must use `$...$` or `$$...$$` (or `\(...\)` / `\[...\]`). Plain `$` without closing delimiter will cause rendering issues.

2. **Menu Out of Sync**: If you add content but don't update `hugo.yaml` menu, the page won't appear in navigation (it will be built but unreachable from nav).

3. **Git Submodules**: The workflow uses `submodules: recursive` — if you see theme files missing, run `git submodule update --init --recursive` locally.

4. **Hugo Version**: Netlify uses 0.122.0, GitHub Actions uses 0.128.0. Minor version differences shouldn't matter, but be aware if you encounter build differences.

5. **Metadata Files**: Files like `*.metadata.json`, `*.resolved` are generated by Claude and properly ignored. Safe to delete locally if they accumulate.

6. **Performance**: The `--gc --minify` flags clean unused resources and minify output. Always use them for production builds.

7. **Static Assets**: Anything in `/static/` is copied as-is to `/public/`. Modify `/static/css/style.css` or add images in `/static/images/`.

8. **Homepage Organization**: The homepage (`content/_index.md`) shows profile info and displays the 6 most recent blog posts. Update this file to change profile section or recent post count.

9. **Now Page**: The `/now/` page (`content/now.md`) is a special page showing current work/activities. Update it regularly to keep it fresh (recommended monthly).

## Development Workflow Summary

1. **Edit content**: Modify `.md` files in `/content/` (use `hugo server` for live preview)
2. **Update menu**: If adding new sections, update menu structure in `hugo.yaml`
3. **Commit to main**: Push to GitHub
4. **Watch deployment**: GitHub Actions automatically builds and deploys (~30 seconds)
5. **Verify**: Check https://omarora.in/ for updates (CDN may cache for a few minutes)

