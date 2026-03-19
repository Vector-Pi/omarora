# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal academic website built with Hugo, hosted on GitHub Pages via GitHub Actions. The site showcases research interests in mathematics, theoretical physics, AI, quantitative finance, and interdisciplinary topics.

## Repository Structure

- `content/` - Markdown content organized by section (blog, research, problems, etc.)
- `themes/minimal-academic/` - Custom Hugo theme with academic styling
- `static/` - Static assets (images, PDFs)
- `scripts/` - Python scripts for content generation
- `layouts/` - Custom layout templates overriding the theme
- `public/` - Generated static files (not tracked in git)

## Development Commands

### Building and Running Locally

```bash
hugo server --buildDrafts --watch
```

This command starts a local development server with live reloading.

### Production Build

```bash
hugo --gc --minify
```

Generates optimized static files in the `public/` directory.

### Testing Changes

Since this is a static site, testing primarily involves:
1. Visual inspection through the local development server
2. Checking links with `hugo check`
3. Validating HTML output with online validators

### Linting

There are no specific linting configurations for this project. For Markdown content:
- Follow consistent heading structures
- Use proper frontmatter formatting
- Maintain consistent formatting for mathematical expressions

## Deployment Process

### GitHub Pages Deployment

The site is deployed automatically via GitHub Actions when changes are pushed to the main branch:

1. GitHub Action workflow in `.github/workflows/hugo.yaml` triggers on push to main
2. Hugo builds the site with `--gc --minify` flags
3. Built files are deployed to GitHub Pages

### Manual Deployment

For manual deployment to GitHub Pages:
1. Run `hugo --gc --minify` to build the site
2. Commit and push the changes to the main branch

Note: The repository also contains a `netlify.toml` file, but the primary deployment is through GitHub Pages.

## Content Management

### Adding Blog Posts

Create new Markdown files in `content/blog/` with front matter:
```yaml
---
title: "Post Title"
date: 2026-03-17
tags: ["Tag1", "Tag2"]
summary: "Brief summary of the post"
---
```

### Managing Site Sections

Sections and subpages are defined in `hugo.yaml` menu configuration. The Python script `scripts/generate_structure.py` can regenerate section structure.

### Problem Database

Olympiad problems are managed via `vondb.json` and synchronized to content files using `scripts/sync_problems.py`.

## Architecture Notes

1. **Theme System**: Uses a custom minimal academic theme with responsive design and dark mode support
2. **Math Support**: KaTeX integration for mathematical notation rendering
3. **Navigation**: Hierarchical menu system defined in hugo.yaml
4. **Content Organization**: Flat structure with manual categorization via tags and directories
5. **Responsive Design**: Mobile-friendly CSS with flexible container sizing

## Key Files to Understand

- `hugo.yaml` - Site configuration and navigation menu
- `themes/minimal-academic/layouts/_default/baseof.html` - Base HTML template
- `themes/minimal-academic/static/css/style.css` - Main stylesheet with dark mode support
- `scripts/sync_problems.py` - Script for managing olympiad problem content
- `content/_index.md` - Homepage content with author bio
- `.github/workflows/hugo.yaml` - GitHub Actions deployment workflow

## Workflow Recommendations

1. When adding new content, follow the existing Markdown structure and front matter conventions
2. For structural changes, update both the content files and the corresponding menu entries in hugo.yaml
3. Test changes locally with `hugo server` before committing
4. Use the sync scripts for bulk content operations to maintain consistency
5. Verify mathematical notation renders correctly with KaTeX
6. Check that navigation links work properly after structural changes
7. Ensure dark mode styling is consistent with light mode