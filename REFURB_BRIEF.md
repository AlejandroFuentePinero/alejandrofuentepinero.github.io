# Site Refurbishment Brief

Repo: `alejandrofuentepinero.github.io`
Stack: Jekyll, academicpages fork of Minimal Mistakes, GitHub Pages

## What this project is

A full end-to-end rebuild of the site: positioning, structure, content and design.

The current site is a well-populated academic template split into two parallel tracks, AI Engineering and Academia. The rebuild unifies them into one site telling one story: an engineer whose evaluation discipline comes from six years of building models with real consequences. All content is kept. The delivery changes completely.

The finished site must do two things at once. It must be scannable in 40 seconds by a recruiter, and it must reward a technical peer or an academic who goes three levels deep. It achieves both through progressive disclosure, a data-derived stats band, and prose written to one standard that serves engineers and academics alike.

The bar for the visual result: a visitor should notice the care before they notice any single element. Details, restraint, elegance. The site itself is evidence of how its owner works.

**Order of operations is strict: positioning before structure, structure before design, design before content rewriting.** Gate 1 outranks every other gate.

---

## How to use this file

1. Save to the repo root as `REFURB_BRIEF.md` and commit it on `master`. This is the only project commit `master` receives before launch.
2. Cut the integration branch: `git checkout -b refurb/main && git push -u origin refurb/main`.
3. Open Claude Code in the repo, check out `refurb/main`, and paste the kickoff prompt from section 9.

---

## 1. Non-negotiable constraints

**Preserve the brand mark.**
- `images/groodle_favicon_256.png` is the site logo. It stays. It is not template cruft.
- The full icon set stays: every favicon, apple-touch-icon, `mstile-*.png`, `browserconfig.xml`, `site.webmanifest`. Do not delete, rename or repath any of it. Phase 6 does not convert these to webp.
- The mark sits in the masthead, left of the name, at 28px to 32px.
- If a dark mode variant is needed, make one and keep the original. Do not recolour the only copy.
- The mark anchors the `og:image` in Phase 6.
- Phase 0 checks whether an SVG version exists. If not, redrawing it as vector is an optional Phase 3 task.

**Do not break the record.**
- Never edit `recommended_citation` or citation text in `_publications/`.
- Never delete an original abstract. Abstracts are demoted to a collapsed block, never removed. See section 4.5.
- Never change a DOI, journal name, co-author name, date or numeric result.

**Do not break URLs.**
- Every existing public URL keeps working. Scholar, ORCID and third parties link here.
- The unification in section 3 retires many URLs. Every one gets a `redirect_from` entry and a line in `MIGRATIONS.md`. None may 404.

**Do not break the build.**
- GitHub Pages runs whitelisted plugins only. Anything outside the list gets raised, not added silently.
- `bundle exec jekyll build` stays warning-free at every gate.

**No fabricated numbers.**
- Every figure in the stats band is either computed from the collections at build time or read from `_data/stats.yml` with a stated source and date. No number is ever typed directly into a template. See section 4.2.

**No new frameworks.**
- No React, no Tailwind build step, no Node bundler. SCSS in `_sass/`, Liquid in `_layouts/` and `_includes/`, minimal vanilla JS.
- Remove jQuery, Magnific Popup and Greedy Nav.

**The live site never breaks during the rebuild.**
- GitHub Pages serves this repo from `master`. Anything merged to `master` deploys immediately. Therefore `master` receives exactly one merge from this project: the final launch merge at Gate 7.
- All work happens on a long-lived integration branch: `refurb/main`, cut from `master` at the start.
- Each phase gets its own branch cut from `refurb/main`, named `refurb/phase-N-name`, and its PR targets `refurb/main`. Never `master`.
- `REFURB_BRIEF.md` itself is the one exception: commit it to `master` once at the start so every branch inherits it. It changes nothing the site serves.
- If a genuine live-site emergency arises during the project (a broken link someone reports, a security issue), fix it on a hotfix branch off `master`, merge to `master`, then merge `master` back into `refurb/main` immediately so the branches never diverge silently.
- Keep `refurb/main` fresh: after any `master` change, merge `master` into `refurb/main` the same day.
- Never force push either branch. Never rebase `refurb/main` after it has PRs merged into it.

**Preview while building.** Pages serves only one deployment per repo, so `refurb/main` cannot be previewed at the github.io URL. Two options, decide at Gate 0:
- Local: `bundle exec jekyll serve` from `refurb/main`. Free, private, sufficient for solo review.
- Shareable: point Cloudflare Pages or Netlify free tier at the `refurb/main` branch of the repo for an auto-deploying preview URL. Worth it for reviewing on a phone and for the screenshot evidence at gates.

**One phase, one branch, one PR into `refurb/main`.** Stop at every gate.

---

## 2. Positioning

### 2.1 The thesis

Alejandro builds AI systems and can tell you whether they work.

The evidence for the second half is what makes him different. He spent 6 years building Bayesian population models where the output determined whether a species received legal protection. That work demanded quantified uncertainty, honest error bars, and evaluation that stands up to scrutiny. He now applies the same discipline to retrieval systems, agents and language model pipelines, where the hard part is not building the thing but knowing if it is right.

The academic record is not a previous career. It is where the method comes from. The unified site makes this a single story, not two CVs stapled together.

### 2.2 Three audiences, one layered page

**The technical peer** wants the hard part: architecture, trade-offs, what was measured, what failed. Served at level 3.

**The recruiter** has 40 seconds: role, seniority, stack, the stats band, contact. Served at levels 1 and 2, entirely above the fold.

**The academic or non-technical visitor** needs to understand the work without decoding an abstract. Served by the plain-language summaries and the STE prose standard, which by design reads cleanly for a specialist and a non-specialist at once.

Test every page against all three in Phase 5. A page that works for only one audience is not finished.

### 2.3 Progressive disclosure

Every piece of content has three levels. The visitor chooses the depth. Nothing dense appears before it is asked for.

- **Level 1, the surface.** One line. In cards, indexes, the stats band.
- **Level 2, the summary.** 60 to 120 words, plain language: what it was, what it found or achieved, why it matters. This opens every page and for most visitors it is the whole visit.
- **Level 3, the depth.** Architecture, methods, trade-offs, results, original abstracts, the live app itself. Below the fold, behind a disclosure, or on a sub-page.

No level 3 content ever appears above level 2. No page opens with method.

### 2.4 Density budget

Hard ceilings, enforced by `scripts/prose_check.py` from Phase 5 onward.

| Surface | Ceiling |
|---|---|
| Home page, total prose | 450 words |
| Home page, first screen | 60 words |
| Stats band label | 4 words per stat |
| Project or app card | 25 words |
| Project page, before first heading | 120 words |
| Publication index entry | 25 words |
| Publication page, plain summary | 120 words |
| Talk entry | 20 words |
| Work timeline entry | 40 words |
| Any paragraph | 4 sentences |

Content that will not fit moves down a level. It does not get squeezed.

---

## 3. Information architecture: one unified site

### 3.1 The unification

The AI Engineering and Academia split goes. One nav, one story. All content is preserved; only its organisation changes.

```
/                    Home. Hero, stats band, skills row, selected work,
                     digital twin, one call to action.
/work/               Timeline of roles. CV PDF download. Grants and awards
                     as a short section.
/projects/           One card grid. Engineering and research projects
                     together, filterable by type, newest first.
/projects/<slug>/    Level 2 summary, then level 3 depth. Same template
                     for engineering and research projects.
/apps/               Live, usable things. Each app: card, one-line pitch,
                     embedded or linked, source link.
/research/           Publications, then talks, then teaching. One page,
                     three sections, anchor links.
/research/<slug>/    Per-paper page: plain summary, collapsed original
                     abstract, citation, DOI.
/contact/            Email, LinkedIn, GitHub, Scholar, ORCID. One line on
                     what he is open to. No form.
/styleguide/         Internal. Not in nav.
```

Nav is five items: Work, Projects, Apps, Research, Contact. The logo links home.

**Retired URLs**, all redirected: `/datascience/` and everything under it maps into `/projects/` and the home page; `/academic/` maps into `/work/` and `/research/`; `/academic/cv/` redirects to `/work/`; the projects that lived under `/datascience/projects/<slug>/` redirect to `/projects/<slug>/`. Phase 1 produces the complete mapping table before anything moves.

### 3.2 The Apps section

New. This is where the site stops telling and starts showing. Candidates, confirm in Phase 1:

- **Digital twin.** The conversational agent. Embedded iframe, kept per section 4.4.
- **7PH Graph** at 7phgraph.com. The metagame knowledge graph explorer.
- **Job Intelligence Engine** Streamlit app, if publicly reachable.
- The bird trends **Shiny app**, if still live.

Each app entry: name, one-line pitch of 25 words, a screenshot or the live embed, a "what it demonstrates" line, and a source link. Dead or unreachable apps are listed with a screenshot and marked as archived rather than embedded. Phase 0 verifies which are live.

### 3.3 The academic CV dissolves

Replaced by `/work/`: role, organisation, dates, 40 words per entry. Publications, talks and teaching are not repeated in the timeline; they are linked. Grants and awards become one short section on this page, ending the current duplication between `_portfolio/` and `/academic/grants_awards/`. A generated CV PDF serves recruiters who want the traditional document, linked from `/work/` and `/contact/`.

### 3.4 Sitemap and blog

The sitemap page currently prints every abstract in full. It becomes titles and one-line descriptions. The single blog post keeps its content, gets its permalink fixed with a redirect, and lives without a "Blog" nav item unless more posts exist.

---

## 4. Content strategy per surface

### 4.1 Home page

Under 450 words of prose. Structure, top to bottom:

1. **Hero.** Name, one-line role under 12 words, the thesis in 2 or 3 sentences. 60 words on the first screen.
2. **Stats band.** Section 4.2.
3. **Skills row.** Section 4.3.
4. **Selected work.** 3 or 4 cards, engineering and research mixed. Each card is a result, not a description.
5. **Digital twin.** Section 4.4.
6. **One call to action.** Contact. The twin is an experience, not the CTA.

The old "What I build" five-bullet list is deleted. The skills row and the stack chips on project cards carry its keyword load.

### 4.2 Stats band

A single quiet row of 4 to 6 figures directly under the hero. This is the recruiter's 10-second summary and the academic's credibility check in one element.

**Computation rule.** Each stat is one of:
- **Derived**: computed by Liquid from the collections at build time. `{{ site.publications | size }}` peer-reviewed papers. `{{ site.projects | size }}` projects. Talks likewise. These can never go stale.
- **Declared**: read from `_data/stats.yml`, each entry carrying `value`, `label`, `source`, `as_of`. Years of experience (computed from a start year, not typed as a number), citation count with its Scholar as-of date, journals published in.

No number appears literally in any template or markdown file. `scripts/prose_check.py` greps for digits in the stats include and fails if it finds any.

**Candidate stats**, final pick in Phase 1: peer-reviewed papers (derived), projects shipped (derived), years working with data under uncertainty (declared, computed from start year), invited and conference talks (derived), citations (declared, dated), live apps (derived from the apps data file).

**Presentation.** Number in the display serif at `--step-3`, label beneath in the sans at `--step--1` in `--ink-muted`. Hairline rules between. No icons, no cards, no counters animating up from zero. If a count-up exists anywhere in the codebase it is a bug.

### 4.3 Skills row

One compact row of chips, not a prose list. Sourced from `_data/skills.yml` so it is maintained in one place.

Two groups, visually continuous: **Builds with** (Python, LLM pipelines, RAG, agents, fine-tuning, GCP, Vertex AI, BigQuery, Neo4j) and **Grounded in** (Bayesian inference, hierarchical models, evaluation design, uncertainty quantification, R). Confirm the exact list in Phase 1; cap at roughly 12 chips total. A chip row scans in 3 seconds and does the recruiter-keyword work without portfolio-cliché prose.

### 4.4 The digital twin embed

The iframe stays on the home page. Rules:

- It loads lazily: `loading="lazy"` plus an IntersectionObserver so it costs nothing until scrolled near.
- It sits inside a styled frame with a heading, one line of context, and a visible "open full screen" link to the Hugging Face Space. The current apology ("Doesn't load?") is replaced by a graceful fallback: if the frame fails, the container shows a screenshot and the link.
- Reserve the vertical space explicitly so the embed never causes layout shift.
- The twin also gets a full entry in `/apps/` and its project page keeps the depth.

### 4.5 Publications and talks

The prose standard for these is section 6, applied so one text serves academics and engineers alike. STE discipline is what makes this possible: short sentences, one meaning per term, no filler, which a specialist reads as precision and a non-specialist reads as clarity.

**The page is the plain summary.** 120 words for a paper, 100 for a talk: what was found, how, why it matters. Written fresh from the finding, not paraphrased from the abstract. A paraphrased abstract is still an abstract.

**The original abstract survives verbatim** in a collapsed block labelled "Original abstract as published". Never edited, never deleted. Level 3.

Then citation, DOI, figures.

**Index entries** state the finding, not the topic. "Rainforest birds in the Australian Wet Tropics are following the escalator to extinction" is right. "Can habitat suitability derived from SDMs predict species abundance?" is wrong: a question, and an unexpanded acronym.

**Talks consolidate.** Duplicate abstracts exist across `_talks/zenq_2022`, `_talks/melbourne_2022` and the ESA/SCBO 2022 pair. One canonical entry per piece of work, other appearances listed as venues beneath it. Default: talks live as entries on `/research/`, with individual pages only for the 3 or 4 strongest. Confirm in Phase 1.

### 4.6 Project pages

Open with the outcome in one sentence. Then the level 2 summary under 120 words. Then level 3 with real headings: architecture, **the decision that was hard and how it was resolved**, what was measured and how, what did not work. The hard-decision section is what a technical peer came for and it is currently missing from every project.

Stack chips on every project. Research projects use the identical template. Same shape, same depth structure: this is what makes one method visible across both halves of the record.

---

## 5. Design direction

Elegant and quiet. Content first. One accent, used rarely. Generous space, strong type. Nothing decorative that does not carry information. The visitor should notice the care before any single element.

**Banned:** gradients, glassmorphism, neumorphism, card drop shadows, stock illustration, hero background images, animated blobs, gradient text, emoji as icons, animated number counters, more than one accent colour, any effect whose purpose is to look modern.

**Target:** a well-set print journal that happens to be a website. Warm paper, near-black ink, hairline rules, one clay accent, a serif for display, a clean sans for text.

### 5.1 Colour tokens

Define once in `_sass/_tokens.scss` as CSS custom properties. No hardcoded hex anywhere else.

```
Light
--paper            #FAFAF7
--paper-sunk       #F0EEE6
--ink              #141413
--ink-muted        #6B6960
--ink-faint        #93918A
--rule             #E5E3DB
--accent           #D97757
--accent-deep      #C15F3C
--accent-wash      #F7EDE7

Dark
--paper            #1F1E1D
--paper-sunk       #2B2A28
--ink              #F2F0E9
--ink-muted        #A3A199
--ink-faint        #6E6C65
--rule             #3A3936
--accent           #E08A6C
--accent-deep      #F0A98D
--accent-wash      #2E2622
```

These are a reconstruction of the Anthropic palette, not sampled values. Verify against anthropic.com and swap before Phase 3 if exactness matters.

Accent rules: links, active nav, at most one emphasis element per screen. Never a large fill. Never more than roughly 5% of a viewport.

Dark mode follows `prefers-color-scheme` with a manual toggle persisted in `localStorage`. An inline blocking script in `<head>` sets the theme before first paint. No flash, ever.

### 5.2 Typography

Two families, self-hosted woff2 in `assets/fonts/`, no Google Fonts CDN.

- **Display:** a warm transitional serif. Newsreader, Source Serif 4 or Instrument Serif. Pick one, justify it.
- **Body and UI:** Inter, Geist or IBM Plex Sans.
- **Code:** JetBrains Mono or IBM Plex Mono.

Scale, 1.250 major third, fluid with `clamp()`:

```
--step--1   0.80rem
--step-0    1.00rem    base, 17px desktop
--step-1    1.25rem
--step-2    1.563rem
--step-3    1.953rem   stats band numbers
--step-4    2.441rem
--step-5    3.052rem   home display only
```

Body line height 1.65, headings 1.15. Measure capped at 68 characters. `text-wrap: balance` on headings, `text-wrap: pretty` on paragraphs. Nothing below 15px. Tabular figures (`font-variant-numeric: tabular-nums`) in the stats band.

### 5.3 Space and layout

8px scale: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128.

The persistent left sidebar author card goes. Replace with a slim sticky header (logo, name, five nav items, theme toggle) and contact links once, in the footer.

- Prose: single centred column, max 68ch.
- Indexes and the stats band: 1120px container.
- Project and app grids: two columns at 900px and above, one below.
- Full-bleed escape hatch for figures and the twin embed.

### 5.4 Motion

150ms to 200ms, `ease-out`, colour and opacity only. No entrance animations, no scroll reveals, no parallax, no counters. Everything disabled under `prefers-reduced-motion`.

### 5.5 Components

Each built in isolation on `/styleguide/` before rollout.

1. Sticky header with logo, nav, theme toggle
2. Home hero
3. Stats band
4. Skills chip row
5. Project and app card with stack chips
6. Embed frame for the digital twin, with fallback state
7. Publication row
8. Talk row
9. Disclosure block for original abstracts, styled as an appendix, not hidden content
10. Callout: note, result, warning
11. Figure with caption and full-bleed variant
12. Work timeline entry
13. Footer
14. Print stylesheet for `/work/`

---

## 6. Prose standard

### 6.1 One standard, two tiers

The whole site is written to ASD-STE100 rules. Full STE uses a controlled dictionary of roughly 900 words with one approved meaning each; applied literally to a bio it produces flat copy. So:

**Tier A, full STE discipline including the vocabulary restriction in 6.3:** project pages, app descriptions, method sections, skills, README files, anything procedural.

**Tier B, all STE rules with natural voice:** the hero, the thesis, work timeline, plain-language summaries of papers and talks.

The paper summaries are deliberately Tier B. STE-ruled prose with natural vocabulary is what lets one text serve an academic and an engineer at once: the specialist reads precision, everyone else reads clarity.

### 6.2 Rules everywhere

1. One idea per sentence.
2. Maximum 20 words per sentence in Tier A, 25 in Tier B.
3. Maximum 4 sentences per paragraph.
4. Active voice. Name the actor.
5. Present or simple past. No perfect continuous.
6. **Zero em dashes and zero en dashes in prose.** Full stop, comma, colon or rewrite. En dashes survive only in numeric ranges inside citations.
7. No semicolons in body copy.
8. Maximum 3 words in a noun cluster. "High-throughput spatial forecasting workflow" fails.
9. One term per concept site-wide. Every choice recorded in `TERMINOLOGY.md`.
10. Expand every acronym on first use per page.
11. Numerals for all numbers.
12. No exclamation marks in body copy.
13. Every project and paper page opens with the result.
14. Write for a reader whose first language is not English.

**Banned words:** delve, leverage as a verb, seamless, robust, cutting-edge, state-of-the-art, passionate, journey, landscape unless literal, realm, tapestry, navigate unless literal, unlock, empower, harness, elevate, "in today's world", "it's worth noting", "at the end of the day", "not just X but Y", "isn't just X, it's Y", "dive into", "under the hood".

**Banned constructions:** the triadic list used for rhythm, the sentence fragment for emphasis, opening a paragraph with "Importantly" or "Notably", closing a section by restating it.

### 6.3 Tier A vocabulary

Short common verbs: use, make, build, run, test, find, show, add, remove, change. One meaning per word. No synonyms for variety. No phrasal verbs where a single verb exists. No gerund as sentence subject. No idiom or metaphor.

### 6.4 Never rewritten

Citation strings. Original abstracts. Third-party quotations. Course, degree, grant and award titles. Any number, sample size, coefficient or date.

---

## 7. Phases

Each phase ends at a gate: open the PR, post evidence, stop.

### Phase 0. Recon, no code changes

Deliverable: `AUDIT.md`. No other file touched.

- Get the site building locally. Record exact commands, Ruby version, gem pinning.
- Inventory every content file: path, collection, permalink, word count, tier, keep / rewrite / merge / delete.
- Grep-verify every candidate template artefact before proposing deletion. Zero false positives. Known candidates: `archive-layout-with-content`, `non-menu-page`, `page-archive`, `markdown_generator`, `/md/`, `markdown.html`, `/nmp/`, `nmp.html`, `about.html`, `/resume`, `/wordpress/blog-posts/`, `redirects.json`, `talkmap.ipynb`, `_drafts/`, `CONTRIBUTING.md`, `CHANGELOG.md`. The logo and icon set are not candidates.
- Full duplicate map. Known: Featured Work repeated on `/` and `/datascience/`; grants and awards in two places; identical abstracts across at least three talks.
- Check every external and internal link. Known break: `https://twitter.com/@Afuentepinero` has a stray `@`.
- List hotlinked assets. Known: featured images served from `raw.githubusercontent.com`.
- Record the blog post permalink mismatch: URL `/posts/2012/08/blog-post-1/`, published December 2021.
- **App liveness check.** Verify which candidate apps in section 3.2 are reachable today: the digital twin Space, 7phgraph.com, the Job Intelligence Engine app, the Shiny app. Record load time for each.
- Check whether an SVG logo exists.
- Baseline Lighthouse on four representative pages. Total JS and CSS bytes, and how much is Minimal Mistakes.
- **Stats inventory.** Every figure that could feed the stats band: counts per collection, first publication year, first professional data role year, current Scholar citation count with date, journals published in. Mark each derived or declared.
- **Density audit.** Word count per page against section 2.4. Show the gap in numbers.
- **Audience audit.** For the home page, the projects index and one publication page: what a recruiter, a technical peer and an academic each get and do not get. Be blunt.

**Gate 0.** Nothing deleted yet.

### Phase 1. Positioning and content architecture, no code changes

The most important phase. Deliverables: `POSITIONING.md` and `CONTENT_MAP.md`. Nothing else.

`POSITIONING.md`:
- Three candidate theses for the hero, each under 60 words, each working for all three audiences. Argue for one.
- The one-line role descriptor, three options.
- The final stats band: which 4 to 6 stats, each marked derived or declared, with the `_data/stats.yml` schema.
- The final skills row: the chip list, capped near 12, with the `_data/skills.yml` schema.
- The unification narrative: the exact copy moves that make the academic and engineering work read as one method.
- Digital twin placement and framing on the home page.

`CONTENT_MAP.md`:
- The confirmed URL tree from section 3.1 and the complete old-to-new redirect table. Every current URL accounted for.
- Every content item: keep, rewrite, merge into X, demote to level 3, or delete. With reasoning.
- The 3 or 4 home page projects, and why those.
- The apps roster from the Phase 0 liveness check: embed, link, or archive per app.
- The talks decision: which 3 or 4 keep pages.
- One publication summary written in full as the worked example, so the standard is visible before it is applied 12 times.
- Word targets per page against section 2.4.

**Gate 1.** Outranks every other gate. Expect several rounds. Nothing downstream starts until the thesis, stats, skills and URL map are settled.

### Phase 2. Cleanup

- Delete what Gate 0 approved. Fix all broken links. Localise hotlinked images.
- Fix the blog post permalink with `redirect_from`.
- Merge duplicate grants and awards. De-duplicate talks per the Gate 1 decision.
- Create `_data/stats.yml` and `_data/skills.yml` per the approved schemas.
- Rewrite `_config.yml` metadata: real description, real `og_image`, correct Twitter handle, correct author block. The current `og:description` reads "About me".
- Create `MIGRATIONS.md` with the full redirect table from `CONTENT_MAP.md`.

**Gate 2.** Clean link check, warning-free build, every redirect in place and tested locally.

### Phase 3. Design system

- `_sass/_tokens.scss` and `_sass/_typography.scss` per section 5.
- Self-host fonts, woff2, `font-display: swap`, Latin subset plus Spanish diacritics.
- Dark mode with no flash.
- `/styleguide/` with every token, every type step, all 14 components in both themes. The stats band renders with live derived numbers, the embed frame with its fallback state visible.
- Strip jQuery, Magnific Popup, Greedy Nav. Vanilla JS nav, theme toggle, and the IntersectionObserver for the embed.
- Optional: vector logo if Phase 0 found none.

**Gate 3.** Review on phone and desktop, both themes. Iterate here, not later.

### Phase 4. Layout and structure

- Apply the design system to `_layouts/` and `_includes/`. The sidebar author card goes.
- Build the unified nav and the new home page per section 4.1, including the stats band, skills row and the twin embed with lazy loading and fallback.
- Build `/projects/` merging both tracks, with the type filter.
- Build `/apps/` from the approved roster.
- Build `/work/` with the timeline, grants section and CV PDF. Redirect `/academic/cv/`.
- Build `/research/` and rebuild publication pages with the disclosure structure.
- Build `/contact/`. Replace the sitemap page. Style the 404.
- Wire every redirect from `MIGRATIONS.md`.

**Gate 4.** Screenshots of every page type at 390, 768 and 1440, both themes. Twin embed demonstrated loading lazily and failing gracefully.

### Phase 5. Content rewrite

Collection by collection, one PR each: `_pages`, `_projects`, apps copy, `_publications` summaries, `_talks` summaries, `_teaching`, `_posts`.

Per file:
1. Classify tier.
2. Rewrite to section 6 and the level structure of section 2.3.
3. Preserve every fact, number, name, date and link.
4. Side-by-side diff in the PR.
5. Metrics table: sentence count, mean length, longest sentence, em dash count (0), banned word hits (0), word count against budget.
6. Audience check: one line per page on what each of the three audiences takes away.

Build `TERMINOLOGY.md` during the `_pages` pass.

Write `scripts/prose_check.py` failing on: any em or en dash outside a citation, any banned word, any over-length sentence, any paragraph over 4 sentences, any unexpanded acronym on first use, any page over its word budget, any literal digit inside the stats include. Wire into a GitHub Action.

**Gate 5, once per collection.**

### Phase 6. Performance, SEO, accessibility

- webp with fallback, explicit dimensions, lazy loading below the fold. Icons stay png and ico.
- Real `og:image`, 1200x630, warm paper, logo, name, role.
- JSON-LD: `Person` on home, `ScholarlyArticle` per publication, `CreativeWork` per project, `SoftwareApplication` per app.
- Every title and meta description rewritten. Pattern: `Page Name | Alejandro de la Fuente`.
- Accessibility: 4.5:1 body contrast both themes, visible focus rings, correct heading order, real alt text, keyboard-navigable nav, toggle and disclosures, an accessible iframe title on the twin, skip link.
- `robots.txt`, clean `sitemap.xml`.

**Gate 6.** Performance 95+, Accessibility 100, Best Practices 100, SEO 100 on four pages, measured with the twin embed below the fold. First-party JS under 15KB gzipped, CSS under 30KB gzipped. The iframe is exempt from the JS budget but must not affect the scores of any page it is not on.

### Phase 7. Final QA

- Full link check, including every `MIGRATIONS.md` redirect resolving on the live domain.
- HTML validation on ten pages. Chrome, Firefox, Safari, desktop and iOS.
- `prefers-reduced-motion` kills all transitions.
- No theme flash on hard reload in either mode.
- The twin embed: loads lazily, fails gracefully with the network blocked, opens full screen.
- The stats band renders the correct derived counts; add one dummy publication locally and confirm the paper count increments, then remove it.
- Print `/work/` and check it.
- `scripts/prose_check.py` clean across every markdown file.
- `MAINTENANCE.md`: how to add a project, a publication with its plain summary, an app; how to update `_data/stats.yml`; the prose rules in short form; the token list; the density budget.

**Gate 7, the launch merge.** This is the only merge to `master` in the whole project.

Launch sequence:
1. Merge `master` into `refurb/main` one final time and resolve anything.
2. Full build and full QA re-run on `refurb/main` after that merge.
3. Open the single PR `refurb/main` into `master`. The PR body links every phase PR and the final QA checklist.
4. Merge with a merge commit, not a squash, so phase history survives.
5. Within 15 minutes of deploy, verify on the live domain: home page, one project, one publication, one app, the twin embed, five spot-checked redirects from `MIGRATIONS.md`, both themes, on a phone.
6. Rollback plan: if the live site is broken, `git revert -m 1` the merge commit on `master` and push. Pages redeploys the old site in minutes. Fix on `refurb/main`, relaunch.
7. After a stable week, delete the phase branches. Keep `refurb/main` until then.

---

## 8. Working method

- Plan mode at the start of every phase. Present, then wait.
- Small commits, clear messages, one phase per commit.
- Ambiguity gets a question, not a guess. Nothing outside the current phase gets improved.
- Out-of-scope findings go in `FINDINGS.md`, not fixed now.
- Build after every meaningful change. Never force push. Never rewrite history on `master` or `refurb/main`.
- Every PR targets `refurb/main`. A PR opened against `master` is a bug, whatever it contains. Close it and reopen against `refurb/main`.
- At the start of every phase, merge the latest `refurb/main` into the new phase branch before writing anything.

Model allocation: highest capability, high effort for Phase 1 positioning, the design system, and the plain-language paper summaries. Mid tier, medium effort for bulk mechanical rewriting, with a high-effort review pass against section 6. Low effort or scripted for link checking and image conversion.

---

## 9. Kickoff prompt

```
Read REFURB_BRIEF.md in full before you do anything else.

This is a full rebuild of my site into one unified story: positioning,
structure, content and design. Section 2 is the argument the site makes and
section 3 is the unified architecture. Everything else serves those two.

Branching first, before anything else. The live site serves from master and
must keep serving untouched until the final launch. Verify that REFURB_BRIEF.md
is committed on master and that the integration branch refurb/main exists. If
refurb/main does not exist, create it from master and push it. All of your
work happens on branches cut from refurb/main, and every PR targets
refurb/main. You never touch master. If you find yourself about to commit,
merge or push to master, stop and tell me instead.

You are executing Phase 0 only, on branch refurb/phase-0-audit cut from
refurb/main. Phase 0 produces AUDIT.md and changes nothing else. Enter plan
mode, present your Phase 0 plan, and wait for my approval.

On top of what the brief lists, AUDIT.md must include:

1. Exact steps to get bundle exec jekyll serve running, including Ruby version
   and any gem pinning.
2. Grep-verified deletion candidates, zero false positives. My logo and the
   full icon set are not candidates. Do not propose them.
3. The complete duplicate map. I know about the Featured Work block, the
   grants and awards overlap, and at least three identical talk abstracts.
   Find the rest.
4. Every external link checked. There is a malformed Twitter URL with a
   stray @ in it.
5. What the site ships: total JS, total CSS, request count, and how much is
   Minimal Mistakes rather than mine.
6. The app liveness check from section 3.2. Which of my apps are reachable
   right now and how fast they load. The apps section and the home page
   embed depend on this being accurate.
7. The stats inventory from Phase 0. Every number that could feed the stats
   band, marked derived or declared, with its source. I will not put a
   single hand-typed number on that band.
8. The density audit against section 2.4 and the audience audit for the
   home page, projects index and one publication page. Be blunt in the
   audience audit. It is the reason for this project.
9. Anything in the brief you think is wrong or will not work on GitHub
   Pages, especially around the redirect volume the unification creates.
   Argue with me now, not in Phase 4.
10. A recommendation on the preview option from section 1: local serve only,
    or a Cloudflare Pages / Netlify preview wired to refurb/main. State the
    trade-off in two sentences.

Constraints while you work:
- No em dashes in anything you write, including AUDIT.md and commit messages.
- Do not touch _publications citation strings or original abstracts.
- Do not add a JS framework or a build step.
- Stop at Gate 0. Do not start Phase 1.
```

---

## 10. Phase handoff prompts

**Phase 1:** `Phase 0 is merged. Execute Phase 1 from REFURB_BRIEF.md. Positioning and content architecture only, no code. Deliver POSITIONING.md and CONTENT_MAP.md and nothing else. Three real thesis options, not one option and two strawmen. The final stats band and skills row with their data file schemas. The complete old-to-new URL table with every current URL accounted for. The worked publication summary written in full. Expect several rounds of pushback before this gate closes.`

**Phase 2:** `Positioning is settled. Execute Phase 2, cleanup. Only delete what I approved at Gate 0. Create _data/stats.yml and _data/skills.yml exactly per the approved schemas. Every URL change gets a redirect_from and a MIGRATIONS.md line, and I want the redirects tested locally before the PR.`

**Phase 3:** `Execute Phase 3. Design system and /styleguide/ only, no content pages. All 14 components, both themes, with the stats band rendering live derived numbers and the embed frame showing its fallback state. I will spend real time at this gate, so make the styleguide complete.`

**Phase 4:** `Execute Phase 4. Build the unified structure from CONTENT_MAP.md on the approved design system. The sidebar goes, the nav becomes the five items, /apps/ ships from the approved roster, the twin embeds lazily with the fallback. Screenshots at 390, 768 and 1440 in both themes for every page type, plus proof the embed fails gracefully.`

**Phase 5:** `Execute Phase 5 for _pages only. Build TERMINOLOGY.md during this pass. Side-by-side diffs, the metrics table and the audience check for every file. Write scripts/prose_check.py including the no-digits-in-stats check, and wire it into CI before you finish. Stop after _pages.`

**Phase 6:** `Execute Phase 6. Hit the Lighthouse and bundle targets with the twin embed in place. Report actual numbers, not estimates. Icons stay png and ico. Add SoftwareApplication JSON-LD to each app.`

**Phase 7:** `Execute Phase 7. Full QA plus MAINTENANCE.md, all on refurb/main. Run the stats band increment test from the brief. Give me the checklist with pass or fail against every item. Then prepare, but do not open, the launch PR from refurb/main into master: draft the PR body with links to every phase PR and the QA checklist. I open and merge that PR myself.`
