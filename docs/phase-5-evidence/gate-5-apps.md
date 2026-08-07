# Gate 5 evidence: the apps pass

Branch `refurb/phase-5-apps`, 2026-08-07. Scope: the pitch, demonstrates and
note strings in `_data/apps.yml`, the `/apps/` intro in `_pages/apps.html`,
the prose_check extension to the data file, one TERMINOLOGY row, and the
Phase 5 DECISIONS (84 to 89) and FINDINGS (12) entries. The roster, the
operational notes and the 2 repo links were settled before the pass
(CONTENT_MAP 5, Gate 1, FINDINGS 10). The digital twin stayed in observe
mode: site-side copy only. The `_publications` summaries were not started.

## 1. Metrics

Output of `python3 scripts/prose_check.py --metrics` (committed as
`prose-check-output-apps.txt`). `/apps/` is Tier A with a 200-word budget,
and the checker now folds the `_data/apps.yml` strings into the page count
(DECISIONS 89):

| file | tier | words / budget | sentences | mean | longest | em+en dashes | banned hits |
|---|---|---|---|---|---|---|---|
| _pages/apps.html (with apps.yml strings) | A | 198 / 200 | 16 | 12.0 | 20 | 0 | 0 |

Per string, against the 25-word card ceiling for pitches (REFURB_BRIEF 2.4)
and the CONTENT_MAP 8 composition (intro 30, entries at about 40):

| entry | pitch / 25 | demonstrates | note | entry total |
|---|---|---|---|---|
| digital-twin | 25 | 16 | 8 | 49 |
| 7ph-graph | 20 | 16 | 7 | 43 |
| job-intelligence-engine | 19 | 14 | 0 | 33 |
| birds-shiny | 20 | 16 | 7 | 43 |

The intro is 24 words of its 30. The remaining counted words are the page
title and the card link labels, which the checker sees once in source. The
longest sentence on the page is 20 words, at the Tier A ceiling, not over
it. Em dash count 0, en dash count 0, banned word hits 0, all enforced by
the extended checker, output committed beside this file.

## 2. Side-by-side: what each surface said, what it says now

The full line diffs are in the PR files view. This table isolates the
copy that changed.

### _data/apps.yml

| surface | before | after |
|---|---|---|
| twin pitch | "A conversational agent that answers questions about my work, with a second model reviewing every answer before it ships." (draft) | The project page excerpt, verbatim: "A conversational agent answers questions about my work, grounded in a curated knowledge base. A second model reviews every answer before a visitor sees it." |
| twin demonstrates | empty | "It shows evaluation discipline applied to an agent: a frozen baseline scores retrieval and answer quality." |
| twin note | "Embedded on the home page; this entry links the standalone Space." (semicolon) | "The chat also lives on the home page." |
| 7PH pitch | "Explore the Australian 7 Point Highlander metagame: 107 events, 4,591 decks, every chart carrying provenance and statistical guards." (draft) | The home card, split for the Tier A sentence limit: "A live knowledge graph of a competitive Magic format: 107 events, 4,591 decks. Every chart carries provenance and statistical guards." |
| 7PH demonstrates | absent | "It shows graph modelling and a build that refuses to draw charts the evidence cannot support." |
| JIE pitch | "A job market intelligence system built on 6,100 postings: skill demand, salary signals and ranked role recommendations." (draft, 4-word noun cluster) | The home card, verbatim: "An extraction pipeline turns 6,100 job postings into ranked role recommendations. A judge model scores the extraction layer's accuracy." |
| JIE demonstrates | absent | "It shows a deterministic pipeline where every model reports its score on held-out data." |
| birds pitch | "Interactive explorer for rainforest bird population trends in the Australian Wet Tropics, built from long-term standardised monitoring." (draft, 4-word noun cluster, vague "long-term") | "An explorer for population trends of rainforest birds in the Australian Wet Tropics, built from 17 years of standardised monitoring." |
| birds demonstrates | absent | "It shows research made usable: the models behind a published paper, open for anyone to query." |

The 2 Gate 1 operational notes ("First load can take about 10 seconds.",
"Free hosting, wakes in about 20 seconds.") shipped unchanged. The 7PH and
JIE source fields were already filled per FINDINGS 10 and are unchanged.

### _pages/apps.html

| surface | before | after |
|---|---|---|
| intro | "I build tools people can use. Each entry links the running app and the project page that records how it was built and measured." | "I build apps people can use. Each entry links the live app and the project page that records how I built and measured it." |

"Tools" broke the TERMINOLOGY row for things on /apps/ ("app, live app"),
and the passive "how it was built" became active (DECISIONS 87).

## 3. Agreement with the live surfaces

Every number and claim was checked against the surfaces that already ship:

- **Twin pitch** is the `_projects/digital-twin.md` excerpt verbatim, and
  its claims match the home embed context line (an agent answering
  questions about my work, a second model reviewing every answer). The
  demonstrates claim (a frozen baseline scores retrieval and answer
  quality) is the project page's baseline sentence (0.866 mean reciprocal
  rank, 4.56 judge score) without the level 3 numbers.
- **7PH pitch**: 107 events and 4,591 decks match the home card and the
  project page. The demonstrates claim restates the project page's
  "Charts refuse to draw when the evidence cannot support them."
- **JIE pitch** is the home card and project excerpt verbatim, 6,100
  postings included. The demonstrates claim restates the project page's
  "deterministic end to end" and held-out scoring.
- **Birds pitch**: 17 years and the Australian Wet Tropics match the home
  card and the project page. The demonstrates claim restates the project
  page's "an interactive app anyone can query".

## 4. Audience check, per entry

**Digital twin.** Recruiter: a live agent shipped with review built in.
Technical peer: retrieval, a judge gate and a frozen evaluation baseline,
depth one click away. Non-technical visitor: a chat about the work that is
checked before it answers.

**7PH Graph.** Recruiter: a live public data product at its own domain.
Technical peer: graph modelling plus a build that will not chart weak
evidence. Non-technical visitor: an explorable record of a game community
with its honesty rules visible.

**Job Intelligence Engine.** Recruiter: an end-to-end product from raw
postings to ranked recommendations. Technical peer: a deterministic
pipeline with judge-scored extraction and held-out scores. Non-technical
visitor: a tool that says which roles fit and why.

**Bird population trends.** Recruiter: research delivered as a usable
product. Technical peer: the models behind a published paper, queryable.
Academic: the 2021 trends, explorable per species without reading the
paper.

## 5. Checker and build

- The prose_check extension (DECISIONS 89) was verified to fire on seeded
  violations before landing clean: an em dash in the data file, a banned
  word in a demonstrates line, an over-length sentence, the page over its
  200 budget, and a 27-word pitch against the 25-word ceiling. Restored,
  the checker reports clean over 26 files and the stats include.
- `bundle exec jekyll build` is warning-free (committed as
  `build-output-apps.txt`), and the built `/apps/` page renders all 4
  entries with pitch, demonstrates and note, hides the empty birds Source
  link and the empty JIE note.

## 6. Open question for the owner

The birds Shiny app has no public source repo anywhere on GitHub (searched
the repo list, repository names and code for the app slug). The `source`
field stays empty and the card hides its Source link (FINDINGS 12). If the
R source still exists locally, publishing it and filling the field
completes the last gap on /apps/.
