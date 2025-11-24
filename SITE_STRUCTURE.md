# Jekyll Site Structure and Configuration

## Overview
This is a Jekyll-based blog deployed via GitHub Pages at https://www.jasonkronemeyer.com

## URL Structure and Permalinks

### Default Permalink Pattern
Jekyll uses the default permalink structure which **includes categories in the URL path**:
```
/:categories/:year/:month/:day/:title:output_ext
```

### Examples
- Post with categories `[Public Safety, RF Technology, RoF]`:
  - Filename: `_posts/2025-11-21-Radio-Over-Fiber.md`
  - URL: `/public%20safety/rf%20technology/rof/2025/11/21/Radio-Over-Fiber.html`

- Post with categories `[smart buildings, sustainability, certifications]`:
  - Filename: `_posts/2025-11-05-SMART-Building-Certifications.md`
  - URL: `/smart%20buildings/sustainability/certifications/2025/11/05/SMART-Building-Certifications.html`

- Post with categories `[Photonics, Networking, Technology]`:
  - Filename: `_posts/2025-11-19-Photonic-Networking.md`
  - URL: `/photonics/networking/technology/2025/11/19/Photonic-Networking.html`

### ⚠️ Critical for Internal Linking
**Always verify actual generated URLs** by checking the `_site` directory after building:
```bash
bundle exec jekyll build
find _site -name "*Post-Title*"
```

Categories with spaces are URL-encoded (`%20`) in the final URL.

## Directory Structure

```
jasonkronemeyer.github.io/
├── _config.yml              # Jekyll configuration
├── _posts/                  # Published blog posts (YYYY-MM-DD-slug.md)
├── _drafts/                 # Draft posts (no date prefix needed)
├── dev/                     # Development/working notes and research
├── _layouts/                # Page templates
│   ├── default.html
│   ├── post.html
│   └── research.html
├── _includes/               # Reusable components
├── _site/                   # Generated site (gitignored, check for actual URLs)
├── assets/                  # CSS, images, etc.
├── images/                  # Image assets
├── maps/                    # Map-related content
├── notes/                   # General notes
├── papers/                  # Academic papers/references
├── practice/                # Practice-related content
├── research/                # Research content
└── about/                   # About pages
```

## Front Matter Standards

### Required Fields
```yaml
---
layout: post
title: "Post Title"
date: YYYY-MM-DD
categories: [category1, category2, category3]
---
```

### Optional Fields
```yaml
status: research          # draft | research | brief | complete
tags: [tag1, tag2]       # Tags for organization (don't affect URL)
excerpt: "Short description"
description: "Meta description for SEO"
```

### Status Field Convention
- `draft` - Initial working draft
- `research` - Research and development phase
- `brief` - Brief summary or overview
- `complete` - Finished, ready for publication

## Common Workflows

### Creating a New Post
1. Create file in `_posts/` with format: `YYYY-MM-DD-slug-title.md`
2. Add front matter with layout, title, date, and categories
3. Write content
4. Build and verify URL: `bundle exec jekyll build && find _site -name "*slug-title*"`

### Working on Drafts
- Option 1: Place in `_drafts/` folder (no date prefix needed)
- Option 2: Place in `dev/` folder for working notes
- Option 3: Use `status: draft` in front matter and keep in `_posts/`

### Internal Linking Between Posts
**Always use full category path:**
```markdown
[Link Text](https://www.jasonkronemeyer.com/category1/category2/YYYY/MM/DD/Post-Title.html)
```

**Verification steps:**
1. Build site: `bundle exec jekyll build`
2. Find actual path: `find _site -name "*Post-Title*"`
3. Copy the path after `_site/` and use in link

### Building and Testing Locally
```bash
# Serve locally with drafts
bundle exec jekyll serve --drafts

# Build for production
bundle exec jekyll build

# Check generated URLs
find _site -name "*.html" | grep posts
```

## Deployment

- **Platform**: GitHub Pages
- **Branch**: main
- **Process**: Automatic on push to main
- **Build time**: ~30-60 seconds after push

## Categories in Use

Common category structures observed:
- Public safety/tech: `[Public Safety, RF Technology, RoF, DAS, POLAN]`
- Buildings: `[smart buildings, sustainability, certifications]`
- Technology: `[Photonics, Networking, Technology]`
- Research: `[blue tech, digital opportunity, research]`
- AI/Education: `[AI, education, future-of-work]`
- Data Science: `[data-science, policy, practice]`

## Cross-Referencing Posts

When adding references to other posts in your blog:
1. Build the site to get the actual URL
2. Use the full absolute URL with domain
3. Test the link after deployment

Example reference format:
```markdown
**Related Post:**
- [Post Title](https://www.jasonkronemeyer.com/full/category/path/YYYY/MM/DD/Post-Slug.html)
```

## Tips for AI Agents

1. **Never assume URL structure** - Always check `_site` output
2. **Categories matter** - They're part of the URL path, not just metadata
3. **Spaces in categories** - Get URL-encoded as `%20`
4. **Slug from filename** - The date and `.md` are stripped to create the slug
5. **Case sensitivity** - Preserve case in slugs (e.g., `SMART-Building` not `smart-building`)

## Theme and Styling

- **Theme**: Minima (default Jekyll theme)
- **Custom CSS**: `assets/main.scss`
- **Math support**: MathJax/KaTeX enabled via kramdown
- **Syntax highlighting**: Rouge

## Useful Commands

```bash
# Check Jekyll configuration
bundle exec jekyll doctor

# View all generated URLs
bundle exec jekyll build --verbose

# Clean build artifacts
bundle exec jekyll clean

# Serve with live reload
bundle exec jekyll serve --livereload

# Check for broken links (after build)
find _site -name "*.html" -exec grep -l "404" {} \;
```

## Configuration Files

- `_config.yml` - Main Jekyll configuration
- `Gemfile` - Ruby dependencies
- `.gitignore` - Excludes `_site/`, vendor/, etc.

## Notes for Contributors/AI Agents

- **Always build locally first** before committing link changes
- **Verify internal links** by checking `_site` directory structure
- **Use consistent category naming** to avoid URL duplication
- **Front matter categories** determine URL structure, so changes affect links
- **Test cross-references** after deployment to catch 404s early

---

*Last updated: November 21, 2025*
