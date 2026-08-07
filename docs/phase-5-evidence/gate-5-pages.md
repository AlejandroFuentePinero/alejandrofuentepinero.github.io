# Gate 5 evidence: the _pages pass

Branch `refurb/phase-5-pages`, 2026-08-07. Scope: the 10 content files in
`_pages/`, TERMINOLOGY.md, `scripts/prose_check.py` with its GitHub Action,
the Phase 5 DECISIONS and FINDINGS entries, and the regenerated CV PDF.
The styleguide (internal, exempt) and the redirect stubs (no prose) were
not touched.

## 1. Metrics per file

Output of `python3 scripts/prose_check.py --metrics` (also committed as
`prose-check-output.txt`):

| file | tier | words / budget | sentences | mean | longest | em+en dashes | banned hits |
|---|---|---|---|---|---|---|---|
| _pages/home.html | B | 174 / 450 | 14 | 10.9 | 21 | 0 | 0 |
| _pages/work.md | B | 276 / 420 | 13 | 16.5 | 23 | 0 | 0 |
| _pages/projects.html | B | 34 / 440 | 3 | 11.0 | 13 | 0 | 0 |
| _pages/apps.html | A | 30 / 200 | 2 | 12.0 | 18 | 0 | 0 |
| _pages/research.html | B | 120 / 700 | 6 | 15.3 | 24 | 0 | 0 |
| _pages/contact.md | B | 38 / 60 | 3 | 10.7 | 12 | 0 | 0 |
| _pages/404.md | A | 28 / 30 | 3 | 9.3 | 13 | 0 | 0 |
| _pages/sitemap.md | A | 74 / 120 | 2 | 9.0 | 11 | 0 | 0 |
| _pages/terms.md | A | 129 / 150 | 15 | 8.5 | 15 | 0 | 0 |
| _pages/threatened_species.md | B | 101 / 150 | 7 | 14.4 | 21 | 0 | 0 |

Counting notes, for honesty about what the tool sees:

- Words inside verbatim record regions do not count toward budgets
  (grant and award lines, the education credential list, the certificates
  block, the volunteering, development, skills and media blocks, the
  nomination list). Records are exempt per CONTENT_MAP section 8.
- The twin frame copy on home travels as Liquid include parameters, which
  the checker cannot see. Counted by hand: title 4 + context 20 + links
  and placeholder 13 = 37 words. Home worst case is therefore about 236
  visible words including chips and stat labels, still far under 450.
- Word budgets for /projects/ and /research/ will only bind once the card
  excerpts and index entries are rewritten in their own collection passes;
  those words live in collection front matter, not these files.
- The longest sentence on every page is within its tier ceiling
  (20 Tier A, 25 Tier B). The 24-word sentence on /research/ is the
  postdoc line of the intro.

## 2. Side-by-side: what each file said, what it says now

Full line diffs are in the PR files view. This table isolates the prose
surfaces that changed. Facts, numbers, names, dates and links are
identical on both sides unless the line notes the settled degree title.

### home.html

| before | after |
|---|---|
| Card: "6,100 job postings turned into ranked role recommendations, with an LLM extraction layer scored by an LLM-as-judge evaluation framework." | "An extraction pipeline turns 6,100 job postings into ranked role recommendations. A judge model scores the extraction layer's accuracy." (acronym rule: LLM out of prose) |
| CTA: "I'm open to AI engineering roles, collaborations and interesting evaluation problems." | "I'm open to AI engineering roles, research collaborations and hard evaluation problems." |

Hero, role line, stats band, skills row, the other three cards and the twin
framing: unchanged, per the Gate 1 settlement. The polish pass reviewed them
rendered and made no edit (DECISIONS 71).

### work.md

| before | after |
|---|---|
| Lead: "For years my office was a rainforest." (7 words, flagged structural in DECISIONS 53) | The 60-word intro: rainforest office line, the protection story, the method lesson, and "if it can't be evaluated, it can't be trusted" (POSITIONING moves 5 and 9, seeded from datascience-skills.md in git history) |
| Timeline: role, organisation, dates only (DECISIONS 48) | Five entries, each with a summary of 40 words or fewer written from the retired academic.md paragraphs and the field record |
| "PhD candidate, Zoology and Ecology" / "Ph.D in Zoology and Ecology" visible, "Ph.D. in Quantitative Ecology" in the collapsed block | "Quantitative Ecology" everywhere, settled with the owner (DECISIONS 63) |
| Education block: Highlights section, internal Formal Education duplication, 1,900 words of course syllabi with em dashes and arrows | Visible degree list once, then certificates as records: title, provider, certificate link, one Covers line each. Every link kept. 3,810 to 1,838 words for the whole file |
| Grants and awards: nested four-line bullets per item | One line per item: year, organisation, title verbatim, amount verbatim |

### projects.html

| before | after |
|---|---|
| "If I can't measure that it works, I don't ship it." | Same opening line, then: "The rule holds for everything here: engineering systems, peer-reviewed research and practice labs. Filter by type, or browse them all, newest first." |

### apps.html

| before | after |
|---|---|
| "Live, usable systems. Each entry links the running app, its source and the project page behind it." (fragment opener, source link not true of every app) | "I build tools people can use. Each entry links the running app and the project page that records how it was built and measured." |

### research.html

| before | after |
|---|---|
| No intro | 58-word intro from the DECISIONS 51 seeds: the method claim, the PhD record, the live postdoc work |
| "See also the threatened species nomination record this research supported." | "See the threatened species nomination record this research supported." |
| "[derived count] species accounts in The Action Plan for Australian Birds 2020, CSIRO Publishing. Background in this post." | "I co-authored [derived count] species accounts in The Action Plan for Australian Birds 2020, published by CSIRO Publishing. The story behind them is in this post." |

### contact.md

| before | after |
|---|---|
| "I'm open to AI engineering roles, collaborations and interesting evaluation problems." | Availability line matched to the home CTA, plus "Email is the fastest way to reach me." |
| "Prefer the traditional document? Download the CV as a PDF." | "If you want the traditional document, download the CV as a PDF." |

### 404.md

| before | after |
|---|---|
| "The address may have changed with the site's redesign. Try the home page, the sitemap, or email me if a link brought you here." | "The address may have changed when I rebuilt the site. Try the home page or the sitemap, or email me the broken link." |

### sitemap.md

| before | after |
|---|---|
| "Every page on the site, one line each. Robots can digest the XML version." (metaphor, fragment) | "This page lists every page on the site, one line each. Crawlers can read the XML version." |

### terms.md

| before | after |
|---|---|
| Minimal Mistakes boilerplate: Disqus comment cookies, third-party advertisers, Google Analytics, none of which exist on this site | What is true: no cookies, no analytics, no ads, no forms. The localStorage theme value. GitHub Pages request logging with the GitHub privacy statement linked. The digital twin's message logging on Hugging Face, previously undisclosed. |

### threatened_species.md

| before | after |
|---|---|
| One dense paragraph: "robust representation", "highlighs" typo, hyphen-as-dash, topic-first | Two paragraphs opening with the result: 15 nominations (14 birds, the possum), EPBC Act and IUCN expanded on first use, the escalator to extinction with its PNAS link kept. Title pluralised to "Threatened species nominations". Nomination list byte-identical inside record markers. |

## 3. Audience check, one line per audience per page

| page | recruiter | technical peer | academic or non-technical |
|---|---|---|---|
| home | Role, stats and stack sit above the fold and the CTA names roles as the ask | The judge-model card and the twin's guardrail line show evaluation discipline before any click | Both research cards state findings with consequences, in plain words |
| /work/ | Five roles, degree list and the CV PDF scan in under a minute | The intro commits to a testable standard and every summary names a method | The career line reads as one unbroken record, with grants, awards and field work intact one level down |
| /projects/ | The shipping credo plus a filterable grid, newest first | The credo is falsifiable, and the filter separates systems from labs | Research projects sit as equals in the same grid, no case-study costume |
| /apps/ | Proof that things run, one click from each card | Each entry routes to the project page where the build and measurement live | Research made usable: the bird trends app and the twin sit beside the engineering |
| /research/ | Three sentences compress the record and its stakes | Methods are named: three decades of monitoring, forecasting, per-paper depth below | Publications, talks, teaching and chapters on one indexed page, record untouched |
| /contact/ | The ask is explicit and the CV is one line away | "Hard evaluation problems" is an invitation, not a slogan | Scholar and ORCID sit in the same short list as email |
| 404 | A route out in two lines | Same | Same, with a human contact if a link is broken |
| /sitemap/ | Every page, one line each | Same | Same, plus the XML pointer for machines |
| /terms/ | Nothing to wade through, no false analytics claims | The twin logging disclosure is accurate about where messages go | Plain-language privacy in 15 short sentences |
| threatened species | 15 species, formal legal nominations, one screen | The mechanism is stated: upslope contraction until habitat runs out | The record is listed as submitted, with the acts expanded and nothing reworded inside it |

## 4. prose_check.py

- Output on this branch: `prose-check-output.txt` (clean, 10 files plus the
  stats include).
- Negative verification: run against the pre-rewrite `work.md` and
  `threatened_species.md`, it reports 83 violations (em and en dashes,
  banned constructions, over-length sentences, unexpanded acronyms); with a
  digit seeded into `_includes/stats-band.html` it fails the digit check.
  Both checks restored and re-verified clean.
- CI: `.github/workflows/prose-check.yml` runs the checker with metrics on
  pushes to `main` and `refurb/**` and on every pull request.

## 5. Build

`bundle exec jekyll build` is warning-free: `build-output.txt`.

## 6. CV PDF

Regenerated from the rewritten /work/ with the Phase 4 method (print
stylesheet, every disclosure opened): 9 pages, down from 18, carrying the
settled degree title and the new timeline summaries.
