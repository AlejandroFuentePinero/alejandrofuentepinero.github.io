# AUDIT.md: Phase 0 Recon

Produced on branch `refurb/phase-0-audit`, 2026-08-07. No repo file other than this one was created or changed. All numbers below are measured, not estimated. Methods: scripted inventory and duplicate detection over every content file, curl checks on all 165 external URLs (155 from source, 10 that exist only in built HTML), internal href resolution against the built `_site`, Lighthouse via Chrome headless, and real-Chrome verification for apps and bot-blocked links.

A note used throughout: the brief says the live site serves from `master`. The repo has no `master` branch. The default and serving branch is `main`. Everywhere the brief says `master`, read `main`. Details in section 9.

---

## 1. Local build

Exact steps, verified from a clean state on this machine:

```
ruby -v          # ruby 3.3.12 (system Ruby, arm64-darwin25)
bundle install   # resolves github-pages 232, jekyll 3.10.0
bundle exec jekyll build
bundle exec jekyll serve   # serves at http://127.0.0.1:4000/
```

- **No gem pinning was needed.** The stock `Gemfile` (github-pages gem, no version constraint) resolves and builds on Ruby 3.3.12 with zero changes. Build time about 5.6 seconds.
- **There is no `Gemfile.lock` in the repo and no `.ruby-version`.** `bundle install` created a lock file locally (untracked, not committed in this phase). Recommendation for Phase 2: commit `Gemfile.lock` and add `.ruby-version` with `3.3.12` so builds are reproducible.
- **The build is not warning-free.** Two warnings, both local-only:
  1. `GitHub Metadata: No GitHub API authentication could be found.` Fix for local builds: `export JEKYLL_GITHUB_TOKEN=<a PAT with public_repo>`. The Pages build injects its own token, so this warning never appears in production. The "warning-free at every gate" rule needs either the token or an explicit carve-out for this message.
  2. `To use retry middleware with Faraday v2.0+, install faraday-retry gem.` Fix: add `gem "faraday-retry"` to the Gemfile. Local-only, safe: GitHub Pages ignores the repo Gemfile and builds with its own dependency set.
- `_config.dev.yml` exists for local overrides (`bundle exec jekyll serve --config _config.yml,_config.dev.yml`). Optional.

## 2. Content inventory

75 content files. Word counts are body prose after stripping front matter, Liquid and HTML. Recommendations are proposals for Gate 0 / Gate 1, not actions taken.

### _pages (24)

| File | Words | Recommendation | Note |
|---|---|---|---|
| 404.md | 30 | keep | restyle in Phase 4 |
| about.md | 485 | rewrite | becomes the new home; over budget already, see section 8 |
| academic.md | 321 | retire, redirect | content dissolves into /work/ and /research/ |
| archive-layout-with-content.md | 582 | delete | template demo, see section 3 |
| book_chapter.html | 1 | rebuild | broken: page loops `site.posts`, so /academic/book_chapter/ lists the blog post, not the 14 book chapters (which live only in cv.md) |
| category-archive.html | 0 | delete | dependency note in section 3 |
| collection-archive.html | 1 | delete | template demo |
| cv.md | 1,286 | merge into /work/ | plus generated CV PDF |
| datascience-communication.md | 104 | merge into /apps/ and /research/ | |
| datascience-education.md | 2,484 | merge into /work/ | heaviest page on the site; certificates demote to level 3 |
| datascience-projects.md | 137 | merge into /projects/ | contains live editing debris, see section 4 |
| datascience-skills.md | 1,346 | merge into skills row | prose list retires |
| datascience.md | 290 | retire, redirect | |
| grants_awards.html | 0 | merge into /work/ | renders `site.portfolio` |
| non-menu-page.md | 21 | delete | template demo |
| page-archive.html | 0 | delete | template demo |
| publications.md | 12 | merge into /research/ | |
| sitemap.md | 30 | rewrite | prints full talk abstracts via auto-excerpt, see section 4 |
| tag-archive.html | 0 | delete | dependency note in section 3 |
| talkmap.html | 23 | delete | orphaned: `talkmap_link: false` in _config.yml, nothing links to it |
| talks.html | 11 | merge into /research/ | |
| teaching.html | 0 | merge into /research/ | |
| terms.md | 284 | keep | light rewrite |
| threatened_species.md | 618 | keep | strong original content; fold into /research/ or /projects/; carries template redirects `/md/` and `markdown.html` |

### _publications (12)

All 12 keep. Never edit citation strings or abstracts. Three data-quality problems found:

1. `delafuente_et_al_2022_ddi_reshuffling.md` has permalink `/publication/Diversity%20and%20Distributions%20-%202022%20-%20de%20la%20Fuente%20-%20...` (a percent-encoded paper title as URL).
2. `delafuente_williams_2022_possums_ddi.md` has a permalink containing literal spaces: `/publication/Diversity and Distributions - 2022 - Fuente - ...`.
   Both are live URLs that third parties may hold. Phase 1 must map both to clean slugs with exact-match redirects, and Phase 2 must test that `redirect_from` handles the encoded and the space forms. Flagged as a redirect edge case in section 9.
3. `delafuente_et_al_2022_ddi_reshuffling.md` has a malformed date: `2022-04-1` (single-digit day). Jekyll parses it, but fix it in Phase 2.

Word counts run 40 to 309 (median about 235), nearly all of it verbatim abstract.

### _talks (15)

13 typed `Talk`, 2 typed `Poster`. Consolidation map in section 4. Two stubs: `esa_2021_poster.md` (3 words) and `tropical_bes_2021.md` (8 words). None of the 15 has an explicit `excerpt`, which is what makes the sitemap print their first paragraphs in full.

### _projects (18)

All keep for content; the four Python skill labs (`mlb_analytics_sql`, `python_eda_mini_projects`, `python-ML-projects`, `python_oop_minisystems`) are merge candidates into fewer entries, a Gate 1 decision. Heaviest: `llm-engineering-lab.md` (1,546 words), `7ph-graph.md` (1,254). Every one of the 18 opens directly with a heading or image: zero words of prose before the first heading, so no page opens with the result (section 8).

### Others

| File | Words | Recommendation |
|---|---|---|
| _portfolio/awards.md | 144 | merge into /work/ |
| _portfolio/grants.md | 190 | merge into /work/ |
| _teaching/james_cook_university.md | 170 | keep, rewrite |
| _teaching/mentoring.md | 197 | keep, rewrite |
| _posts/2012-08-14-blog-post-1.md | 746 | keep, fix permalink (section 11) |
| _drafts/post-draft.md | 371 | delete, template demo draft |

## 3. Deletion candidates, grep-verified

Method: `grep -r` across the whole repo (excluding `.git`, `_site`, and the brief itself) for each candidate's name and, for assets, its URL-encoded form, case-insensitive. A candidate is listed as safe only when every reference is the file itself or another file in this same table. The logo `images/groodle_favicon_256.png` and everything icon-related are excluded from candidacy, per the brief. Section 9 covers the phantom icon references separately.

### Safe to delete (zero external references)

| Candidate | Grep evidence |
|---|---|
| `_pages/archive-layout-with-content.md` | referenced only by CHANGELOG.md (itself in this table) |
| `_pages/non-menu-page.md` | self-references only (its own `/nmp/`, `nmp.html` redirects) |
| `_pages/page-archive.html` | self only |
| `_pages/collection-archive.html` | self only |
| `_pages/talkmap.html` | linked only from talks.html behind `site.talkmap_link`, which is `false`; page is unreachable |
| `talkmap/` directory, `talkmap.py`, `talkmap.ipynb` | referenced by talkmap.html (above) and a dead upstream link; `_config.yml` mentions are exclude-list entries |
| `markdown_generator/` (6 files) | all references internal to the directory |
| `_drafts/post-draft.md` | zero references |
| `CHANGELOG.md`, `CONTRIBUTING.md` | reference each other only; upstream template docs |
| `package.json` | referenced only in the `_config.yml` exclude list (remove that line too) |

### Orphaned assets (zero references in any case or encoding)

`images/_MG_3336.JPG`, `images/_MG_3383.JPG`, `images/a_icon.png`, `images/esa_2021_poster.png`, `images/hl_hot.gif`, `images/iconinoni.png`, `images/IMG_3392.png`, `images/profile_1.jpeg`, `images/soil_abundance.png`, `files/iconinoni.png`, `files/machine_learning_specialisation.png`, `files/skill_summary.png`.

Checked and NOT orphans (referenced via URL-encoded names): the two Diversity and Distributions PDFs in `files/`, `files/python bootcamp.pdf`, `images/Pasted Graphic.png`. Do not delete these.

### On the brief's candidate list but not deletable as files

- `redirects.json`: does not exist in the repo. Nothing to delete.
- `about.html`, `/md/`, `markdown.html`, `/nmp/`, `nmp.html`, `/resume`, `/wordpress/blog-posts/`: these are `redirect_from` entries inside front matter, not files. `/about/`, `/about.html`, `/cv/`, `/resume` are real legacy URLs worth keeping. The template leftovers (`/md/`, `markdown.html` on threatened_species.md, `/nmp/`, `nmp.html` on non-menu-page.md, `/wordpress/blog-posts/` on book_chapter.html) can be dropped in Phase 2 when their host pages are reworked.
- `_config.dev.yml`: zero grep references but functionally used by the optional dev serve command. Keep or delete deliberately; not proposed.

### Conditional

`_pages/category-archive.html` and `_pages/tag-archive.html` (permalinks `/categories/`, `/tags/`): the Minimal Mistakes post layout links post tags and categories to these pages, and one published post exists. Delete them together with the Phase 4 layout replacement, not before, or the post's taxonomy links 404.

## 4. Duplicate map

Detected by pairwise similarity over all content bodies (SequenceMatcher, threshold 0.50) plus manual inspection. Ratio 1.00 means byte-identical prose.

### The known three, confirmed

1. **Featured Work block**: `about.md` (home) and `datascience.md` carry the same Job Intelligence Engine block, same text, same bullets, same inline CSS idea, different hotlinked image (`engine_path.png` vs `simple_workflow.png`).
2. **Grants and awards**: `_portfolio/grants.md` and `_portfolio/awards.md` render in full at `/academic/grants_awards/` AND inside `/academic/cv/` (both pages loop `site.portfolio`).
3. **Identical talk abstracts**: `melbourne_2022.md` and `zenq_2022.md` are identical (1.00).

### The rest

4. **Talks that are pasted publication abstracts** (similarity in parentheses):
   - `tess_2021.md` duplicates the Ecography 2021 abstract (0.95)
   - `zenq_2023.md` duplicates the 2023 Global Change Biology abstract (0.95)
   - `chilean_congress_ornithology_2017.md` duplicates the 2018 Gallardo et al. abstract (0.93)
   - `zenq_2022.md` and `melbourne_2022.md` duplicate the 2022 possums Diversity and Distributions abstract (0.85 each)
   - `esa_scbo_2022.md` duplicates the 2022 reshuffling Diversity and Distributions abstract (0.61)
   So 6 of 15 talks are near-verbatim copies of 5 publication abstracts. This is the consolidation input for section 4.5 of the brief.
5. **CV composite duplication**: `cv.md` re-renders publications, talks, teaching (Liquid loops) and grants and awards (item 2), and hand-lists 14 book chapters that appear nowhere else (the Book chapters page is broken, section 2). It also duplicates the degree list from datascience-education.md and overlaps the skills list with datascience-skills.md.
6. **Sitemap prints full abstracts**: `/sitemap/` uses `archive-single.html` for every document. Talks have no explicit `excerpt`, so Jekyll auto-excerpts their first paragraph, which for the six talks above is a full publication abstract. Confirmed in built output (the Ecography abstract appears verbatim on /sitemap/).
7. **Home "What I build" vs datascience-skills.md**: the five-bullet list restates the skills page's categories in marketing form. Both retire in the rebuild (brief 4.1 and 4.3).
8. **Profile images**: `images/profile.jpeg` (used) vs orphaned `profile_1.jpeg`, plus stray photo exports (section 3 orphans).

## 5. Link check

165 unique external URLs checked (155 extracted from source, 10 more that only exist in built HTML, e.g. Liquid-built profile links). Every URL was curled with redirects followed; every failure class was then verified in real Chrome to eliminate false positives.

### Genuinely broken (4)

| URL | Where | Status |
|---|---|---|
| `http://www.fundacionzoodesantillana.org/` | cv.md | dead domain, connection failure |
| `https://github.com/AlejandroFuentePinero/Nmixture_Frogs_CodeR` | _talks/coder_nmix.md | 404, repo gone or renamed |
| `https://github.com/academicpages/academicpages.github.io/blob/master/_talks/talkmap.ipynb` | _pages/talkmap.html | 404 (page is itself orphaned) |
| `http://www.codeofclimber.ru/2015/sorting-site-tags-in-jekyll/` | _includes/category-list.html (comment) | dead domain, template comment |

### Malformed but currently functioning (fix in Phase 2)

- **The stray-@ Twitter URL, confirmed**: `_config.yml` line 108 sets `twitter: "@Afuentepinero"` and `_includes/author-profile.html` builds `https://twitter.com/{{ author.twitter }}`, producing `https://twitter.com/@Afuentepinero` in the sidebar of every page. x.com happens to tolerate the @ and redirects, so it resolves today, but the config value should lose the @.
- **PDF links with literal spaces on the `master` branch**: e.g. the 2025 GCB paper links `github.com/.../blob/master/files/Global Change Biology - 2025 - ... .pdf` (spaces unencoded, plus a Unicode hyphen U+2010 in the filename). Browsers auto-encode and GitHub redirects `master` to `main`, so it opens (verified 200), but it is fragile twice over. Same pattern on the Ecography paper (`blob/master/...`).
- **Streamlit app link**: 303 to a login wall. Covered in section 6; the link on datascience-communication.md currently sends visitors to a Streamlit login page.

### Bot-blocked, verified fine in a real browser (not broken)

13 URLs return 403 to curl: 8 Wiley/DOI article links, nytimes.com, jcu.edu.au, pnas.org, scielo.cl, sciencedirect.com, plus moxfield.com, and LinkedIn returns 999. Spot-verified in Chrome: the Wiley GCB 70215 article, the JCU news release, and moxfield.com all load fully. These need no fix.

### Internal links

All internal hrefs across 76 built pages resolve, with one class of exception: 11 icon URLs referenced from the head of every page point to files that do not exist (9 `apple-touch-icon-*.png` sizes, `images/manifest.json`, `images/safari-pinned-tab.svg`, plus `mstile-144x144.png` and `browserconfig.xml` in meta tags). Full analysis in section 9, because it contradicts a brief constraint.

### Hotlinked assets (4 instances, 3 files)

All served from `raw.githubusercontent.com/.../master/files/...`:
- `about.md` line 74: `engine_path.png`
- `datascience.md` line 111: `simple_workflow.png`
- `_projects/job_intelligence_engine.md` lines 13 and 36: `project_pipeline_simple.png` and one more
These work today only because GitHub redirects the renamed `master` branch. Localise in Phase 2 (the files already exist in `files/`).

## 6. What the site ships

Measured from the built `_site` and Lighthouse (Chrome headless, local serve).

| Metric | Value | Of which Minimal Mistakes / template |
|---|---|---|
| Total JS | 244 KB raw | main.min.js 128 KB raw / 44.9 KB gzip (MM bundle incl. jQuery 1.12.4, Magnific Popup, Greedy Nav, FitVids, smooth-scroll, Stickyfill); talkmap Leaflet 112 KB (orphaned page) |
| First-party JS | 0.5 KB (collapse.js, 306 B gzip) | everything else is template or vendor |
| Total CSS | 208 KB raw | main.css 102 KB raw / 21.8 KB gzip (MM); style.css 76 KB raw / 11.4 KB gzip (injected Primer theme, linked from nowhere: pure dead weight); academicons 8 KB; collapse.css 0.3 KB |
| Home page URL references | 42 (href/src in HTML) | |
| Home page total bytes (Lighthouse) | 3,357 KiB | dominated by the twin iframe and hotlinked images |
| CDN dependencies | MathJax 2.7.4 from cdnjs on every page (async) | none of it is first-party |

**The Primer stylesheet**: `_config.yml` declares no `theme`, so the github-pages gem injects `jekyll-theme-primer 0.6.0`, which emits `/assets/css/style.css` (76 KB). No page links it as a stylesheet; the sitemap even lists it as if it were a page. Resolve in Phase 2 (exclude it or declare the vendored setup properly).

**Lighthouse baseline** (categories: Performance / Accessibility / Best Practices / SEO):

| Page | Scores | FCP | LCP | Weight |
|---|---|---|---|---|
| Home `/` | 67 / 91 / 96 / 92 | 2.8 s | 20.2 s | 3,357 KiB |
| Projects `/datascience/projects/` | 75 / 88 / 96 / 92 | 2.7 s | 5.5 s | 611 KiB |
| Publication (Ecography 2021) | audit fails, NO_FCP | | | |
| CV `/academic/cv/` | audit fails, NO_FCP | | | |

The two failures are reproducible and real: Lighthouse headless reports "the page did not paint any content" for publication pages and the CV, locally AND on the live site, with and without MathJax blocked, across repeated runs. The pages render instantly in real Chrome with zero console errors, so users are not affected, but Gate 6 targets cannot be measured on these page types until the cause is found. Logged as an open diagnostic for Phase 6.

Against the Phase 6 budgets: the MM JS bundle alone (44.9 KB gzip) is 3x the 15 KB first-party JS budget, so the budget is only reachable by dropping the bundle, which the brief already plans. main.css at 21.8 KB gzip fits the 30 KB CSS budget even before the rewrite.

## 7. App liveness

Three curl samples per app plus real-Chrome verification, measured 2026-08-07.

| App | Verdict | Evidence |
|---|---|---|
| Digital twin (alejandrofupi-digital-twin.hf.space) | **Live and healthy** | 200 in 1.24 s / 2.11 s / 1.21 s; chat UI verified rendering inside the home page embed in Chrome |
| 7PH Graph (7phgraph.com) | **Live, slow cold start** | 200 via redirect to www.7phgraph.com; 9.04 s cold, then 2.07 s / 1.99 s; 291 KB HTML |
| Job Intelligence Engine (job-intelligence-engine.streamlit.app) | **Not publicly reachable** | 303 to a Streamlit login wall after 17.6 s / 28.3 s; the app is private or suspended. As shipped, the site links visitors into a login page |
| Birds trend Shiny app (alejandrodelafuente.shinyapps.io/BirdsPopTrendAWT) | **Live, sleeping** | 202 holding page in about 2 s; verified in Chrome: wakes and renders the full app in roughly 20 s (free-tier sleep) |

Consequence for the brief's section 3.2 roster: the twin and 7PH Graph are embed/link ready. The Streamlit app must either be made public again or enter /apps/ as archived with a screenshot. The Shiny app works but needs a "takes about 20 seconds to wake" line or archived treatment; decide at Gate 1.

## 8. Density and audience audits

### Density, measured against brief 2.4

| Surface | Ceiling | Measured now | Gap |
|---|---|---|---|
| Home page, total prose | 450 | 485 | +35, and that excludes the sidebar author card |
| Home page, first screen | 60 | 112 words before the second paragraph even starts | +52 minimum |
| Stats band label | 4 per stat | no stats band exists | n/a |
| Project or app card | 25 | project excerpts 19 to 64 words; 9 of 18 over budget | up to +39 |
| Project page, before first heading | 120 | 0 on all 18 | inverted: no page opens with prose at all; every one opens with a heading or image, so no page opens with the result |
| Publication index entry | 25 | 7 to 17 words, all within budget | fails on content, not length: entries are topic questions, not findings |
| Publication page, plain summary | 120 | 0: no page has one, all open with the verbatim abstract (median 235 words) | missing entirely |
| Talk entry | 20 | no talk has an excerpt; index shows bare titles, sitemap shows full abstracts | missing entirely |
| Work timeline entry | 40 | cv.md entries are 10 to 25 words each, but the page is 1,286 words total | format, not length, is the problem |
| Any paragraph | 4 sentences | home paragraph 1 is 5 sentences, 112 words | multiple violations across pages |

Heaviest pages: datascience-education.md 2,484 words, llm-engineering-lab.md 1,546, datascience-skills.md 1,346, cv.md 1,286.

### Audience audit, blunt

**Home page.**
- *Recruiter (40 seconds):* gets a role line ("AI Engineer & Data Scientist") in an H2 and a personal story about pumas and jaguars. No stats, no stack, no CV link, no contact above the fold. The second screen is a 1,100 px iframe: the recruiter's 40 seconds end inside a chatbot they did not ask for. The keyword load ("What I build") is below the twin, and the page's one CTA is a demo button for a project whose app is behind a login wall. A recruiter leaves with "biologist who now does AI", which is the two-CVs problem the brief exists to fix.
- *Technical peer:* "What I build" is five bullets of claims with zero links to evidence. No architecture, no numbers, no trade-offs anywhere on the page. The featured work block reads as marketing ("exactly what to learn next to close the gap") and its screenshot is an AI cartoon, not the system. The peer has no path to depth except the nav.
- *Academic:* nothing above the fold says researcher. Publications are two clicks away behind a nav item labelled "Academia". The story paragraph mentions the research but links none of it.

**Projects index (/datascience/projects/).**
- *All three audiences* first read a leftover editing instruction that renders as body text: the fragment beginning "Everything below that" and ending "the grid includes" (datascience-projects.md line 16, which also contains an em dash the site rules ban). It is the first impression of the flagship page.
- *Recruiter:* the three-tier structure (Flagship / Research / Skill Labs) is genuinely good scaffolding, but cards run to 64 words, and MLB SQL exercises sit visually equal to peer-reviewed population models. Nothing says which three projects matter.
- *Technical peer:* cards describe intent, not results; no stack chips, no filter. "Rigorous evaluation" is claimed on the section header, never shown on a card.
- *Academic:* research projects are framed apologetically as "peer-reviewed modelling work presented in a DS case-study format", as if the science needed a costume.

**Publication page (Ecography 2021).**
- *Recruiter:* the index entry is "Can habitat suitability derived from SDMs predict species abundance?", a question with an unexpanded acronym (the brief's own example of wrong). The page is title, citation, and a 300-word verbatim abstract. A recruiter gets nothing they can repeat in a phone screen.
- *Technical peer:* the abstract is the only content; there is no "how", no figures on the page, and the PDF link is a fragile GitHub blob URL on a renamed branch.
- *Academic:* gets exactly what Wiley already gives them, minus the journal context. The page adds zero value over the DOI link for its best-served audience, and nothing for the other two.

## 9. Brief corrections: argue now, not in Phase 4

1. **`master` does not exist.** The repo's default and Pages-serving branch is `main`. The brief's branch instructions all still work with `main` substituted, and that is what this project does. But two artefacts of the old name are live: the 4 hotlinked images and 2 PDF links reference `/master/` paths and survive only via GitHub's branch-rename redirect. Localising and re-pointing them in Phase 2 removes the dependency.
2. **The protected icon set does not exist.** The brief orders: "The full icon set stays: every favicon, apple-touch-icon, mstile-*.png, browserconfig.xml, site.webmanifest. Do not delete, rename or repath any of it." There is nothing to preserve: zero icon files exist in the repo beyond `groodle_favicon_256.png` (and the orphaned `a_icon.png`/`iconinoni.png`). `_includes/head/custom.html` references 13 phantom icon files, so every page load 404s up to 11 requests. The constraint as written is unsatisfiable. Proposed correction: keep the groodle mark (it works as favicon today), and in Phase 6 generate a real icon set from it and fix the references, or strip the phantom tags in Phase 2.
3. **MathJax is not in the brief.** `head/custom.html` loads MathJax 2.7.4 from cdnjs on every page. The design constraints (no CDN fonts, minimal vanilla JS, Lighthouse 95+) imply it must go or be replaced, but the brief never mentions it. Nothing obvious on the site uses TeX; Phase 2 should verify and remove, or Phase 6 must self-host it.
4. **Redirect volume is a non-issue; two redirect edge cases are real.** `jekyll-redirect-from` is already in `_config.yml` and is Pages-whitelisted. Each retired URL becomes one small static HTML file; the roughly 40 to 60 redirects the unification needs cost nothing. The real risks: (a) the two publication permalinks containing spaces and percent-encoding; a `redirect_from` for those exact strings must be tested locally in Phase 2 before anything moves; (b) `redirect_to` on retired section landing pages only supports one target, so pages whose content splits (academic.md into /work/ plus /research/) need a chosen primary target.
5. **Lighthouse cannot currently score publication pages or the CV** (NO_FCP, section 6). Gate 6's "95+ on four pages" needs this diagnosed first, or the four pages chosen around it. It reproduces on the live site, so it predates this project.
6. **The Primer theme injection** ships 76 KB of dead CSS because `_config.yml` declares no theme (section 6). One config line in Phase 2.
7. **The sitemap-prints-abstracts problem is a talks problem.** Brief 3.4 attributes it to the sitemap page; the mechanism is that talks lack explicit excerpts, so any archive listing auto-excerpts their full first paragraph. Fixing talks (Gate 1 consolidation) fixes the sitemap almost for free.
8. **Section 2.1 says "6 years" of Bayesian modelling work; pick the anchor now.** The CV supports several start years: 2016 (head biologist, CONAF), 2019 (research assistant, JCU), or 2020 (PhD monitoring work). "Years working with data under uncertainty" must be computed from one declared start year (section 10); the thesis phrasing should match whatever Gate 1 declares.
9. **Book chapters have no working surface.** The brief's architecture (3.1) never mentions the 14 book chapters; today their only correct listing is inside cv.md, and the dedicated page is broken (section 2). Phase 1 must give them a home in /research/.

## 10. Stats inventory

Every number that could feed the stats band. Derived = computed by Liquid from collections at build time, can never go stale. Declared = must live in `_data/stats.yml` with `value`, `source`, `as_of`.

| Candidate stat | Type | Source | Current value |
|---|---|---|---|
| Peer-reviewed publications | derived | `site.publications \| size` | 12 |
| Projects | derived | `site.projects \| size` | 18 |
| Talks and posters | derived | `site.talks \| size` (13 talks + 2 posters; a `type` filter can split them) | 15 |
| Live apps | derived | future `_data/apps.yml` roster | 3 reachable today (section 7) |
| Teaching entries | derived | `site.teaching \| size` | 2 |
| First publication year | derived | min date in `_publications` | 2017 |
| Journals published in | derived | unique `venue` values in `_publications` | 10 unique journals |
| Years working with data under uncertainty | declared | start year to be chosen at Gate 1 (options in section 9.8), rendered as a computed difference, never a typed number | 2016, 2019 or 2020 anchor |
| Citations | declared | Google Scholar profile 7CKVdZwAAAAJ | 193 as of 2026-08-07 |
| h-index | declared | same Scholar profile | 7 as of 2026-08-07 |
| Book chapters | declared today (hand list in cv.md); becomes derived if Phase 2 creates `_data/book_chapters.yml` | The Action Plan for Australian Birds 2020, CSIRO Publishing | 14 |
| Media coverage | declared | JCU media / Mediaportal link in cv.md | 70 national stories (2022) |
| Editorial service | derived-able | journal list in cv.md, move to a data file | 8 journals |

Nothing on this list needs to be hand-typed into a template. The two Scholar numbers are the only ones requiring a dated manual refresh.

## 11. Blog post permalink mismatch

Confirmed: `_posts/2012-08-14-blog-post-1.md` has front-matter date 2021-12-01 but filename date 2012-08-14 and explicit permalink `/posts/2012/08/blog-post-1/`. The post (The Action Plan for Australian Birds 2021) is real content. Phase 2: rename the file to `2021-12-01-...`, set a clean permalink, add `redirect_from: /posts/2012/08/blog-post-1/`.

## 12. SVG logo

No SVG version of the mark exists (the only SVGs in the repo are icon-font files). The optional Phase 3 vector redraw of `groodle_favicon_256.png` is therefore live.

## 13. Preview recommendation

**Recommendation: Cloudflare Pages wired to `refurb/main`.** The gates demand phone review (Gate 3), screenshot evidence at three widths (Gate 4), and theme testing on iOS (Gate 7), all of which are painful against localhost but trivial against a real URL, and the twin iframe plus Hugging Face behave more honestly on a deployed origin than on 127.0.0.1. Cost is about 15 minutes of one-time setup and a second build environment to sanity-check against github-pages gem versions, while local serve remains the day-to-day loop either way.
