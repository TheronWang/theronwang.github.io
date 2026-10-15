# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Site Overview

Personal academic website for Theron S. Wang (Ph.D. candidate at UT Arlington, NLP / Animal Language Understanding). Built on the [al-folio](https://github.com/alshedivat/al-folio) Jekyll theme and deployed to GitHub Pages.

## Local Development

**With Docker (recommended):**

```bash
docker-compose up
# Site available at http://localhost:8080
```

**With native Ruby:**

```bash
bundle install
bundle exec jekyll serve
# Site available at http://localhost:4000
```

Deployment is automatic via GitHub Actions on push to `main` — no manual deploy step needed.

## Formatting

```bash
npx prettier --write .       # format all Liquid/HTML/JS/CSS files
npx prettier --check .       # check without writing
```

Prettier is configured in `.prettierrc` with `printWidth: 150` and the Shopify Liquid plugin.

## Content Architecture

| What                              | Where                               |
| --------------------------------- | ----------------------------------- |
| Site-wide settings, nav, features | `_config.yml`                       |
| About page bio & profile          | `_pages/about.md`                   |
| Publications                      | `_bibliography/papers.bib` (BibTeX) |
| News items                        | `_news/*.md`                        |
| Blog posts                        | `_posts/YYYY-MM-DD-title.md`        |
| CV data                           | `_data/cv.yml`                      |
| Co-author links                   | `_data/coauthors.yml`               |
| Venue abbreviation colors/URLs    | `_data/venues.yml`                  |
| Projects                          | `_projects/*.md`                    |

### Adding a news item

Create `_news/YYYYEVENTNAME.md` with this frontmatter:

```yaml
---
layout: post
date: YYYY-MM-DD
inline: true
related_posts: false
---
```

### Adding a publication

Add a BibTeX entry to `_bibliography/papers.bib`. Extra al-folio fields:

- `abbr` — venue abbreviation badge (must be defined in `_data/venues.yml` for colored badge)
- `selected = true` — shows on the about page under "Selected Publications"
- `preview` — thumbnail image filename from `assets/img/`
- `html`, `pdf` — link buttons rendered on the publications page

### News item date convention

Use the actual event date as `date:` in the frontmatter (not the date you created the file). The news feed sorts and displays by this date.
