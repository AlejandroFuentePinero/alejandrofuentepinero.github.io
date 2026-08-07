# Gate 5 evidence: the talks pass

Branch `refurb/phase-5-talks`, 2026-08-07. Scope: the 12 files in `_talks/`,
the talk layout (summary, disclosure, poster, thesis and paper blocks), the
excerpt line on the `/research/` talk rows, the PhD seminar abstract repair,
the prose_check extension to the collection, the TERMINOLOGY additions, and
the DECISIONS (97 to 108) and FINDINGS (15 to 17) entries. `_teaching` and
`_posts` were not started.

## 1. Record integrity

Verified programmatically against git HEAD before anything else
(`record-check-talks.txt`). All 11 untouched abstracts are byte-identical,
the seminar abstract matches its 3 repairs and nothing else, and every fact
field (title, venue, date, location, award, also, type, permalink) is
unchanged on all 12 files:

```
IBRC_2025.md                                page   IDENTICAL       facts-ok
NFFF_2025.md                                row    IDENTICAL       facts-ok
PhD_completion_seminar.md                   page   REPAIRED-OK     facts-ok
cbcs_brisbane_2023.md                       row    IDENTICAL       facts-ok
chilean_congress_ornithology_2017.md        row    IDENTICAL       facts-ok
coder_nmix.md                               row    IDENTICAL       facts-ok
esa_scbo_2022.md                            page   IDENTICAL       facts-ok
tess_2021.md                                row    IDENTICAL       facts-ok
tess_2023.md                                row    IDENTICAL       facts-ok
wtma_workshop.md                            row    IDENTICAL       facts-ok
zenq_2022.md                                row    IDENTICAL       facts-ok
zenq_2023.md                                page   IDENTICAL       facts-ok
```

The 8 rows-only files also build byte-identical redirect pages: a full
`_site` diff against a build of `refurb/main` shows changes in only the 4
talk pages, `/research/`, and the 2 build-timestamp files (`feed.xml`,
`sitemap.xml`).

### The seminar abstract repair (DECISIONS 105, 106)

Source: the thesis PDF at ResearchOnline@JCU, eprint 91342, pages vii to
viii. The DOI is 10.25903/07p8-7k08. The repository blocks non-browser
requests and its record page carries only a 2-sentence blurb, not the
abstract, so the text came from the thesis itself. Full diff in
`thesis-abstract-diff-talks.txt`:

```
site text before: 278 words
thesis abstract:  519 words

replace: site=['reshufiling']       -> thesis=['reshuffling']
replace: site=['biogeo', 'chemical'] -> thesis=['biogeochemical']
replace: site=['causallinks']       -> thesis=['causal', 'links']
omitted by the seminar abstract: 137, 24, 26, 27 and 27 words
```

The 3 replacements are the repair. The omissions are the author's own
condensation of the thesis abstract into a seminar abstract, and every word
the seminar keeps matches the thesis exactly, so the abridgement stands and
the record was not expanded into a different one.

## 2. Metrics

Output of `python3 scripts/prose_check.py --metrics` committed as
`prose-check-output-talks.txt`. All 12 files are Tier B (25-word sentences).
The summary column applies to the 4 files with pages; the 8 rows-only files
have no summary by design. Sentence counts cover the checked prose only
(excerpt plus summary).

| file | summary / 100 | excerpt / 20 | sentences | mean | longest | em+en dashes | banned hits |
|---|---|---|---|---|---|---|---|
| zenq_2023.md (page) | 93 | 18 | 9 | 12.3 | 18 | 0 | 0 |
| esa_scbo_2022.md (page) | 97 | 18 | 8 | 14.4 | 18 | 0 | 0 |
| PhD_completion_seminar.md (page) | 97 | 16 | 9 | 12.6 | 24 | 0 | 0 |
| IBRC_2025.md (page) | 94 | 17 | 8 | 13.9 | 19 | 0 | 0 |
| cbcs_brisbane_2023.md | n/a | 17 | 1 | 17.0 | 17 | 0 | 0 |
| chilean_congress_ornithology_2017.md | n/a | 17 | 1 | 17.0 | 17 | 0 | 0 |
| coder_nmix.md | n/a | 17 | 1 | 17.0 | 17 | 0 | 0 |
| NFFF_2025.md | n/a | 18 | 1 | 18.0 | 18 | 0 | 0 |
| tess_2021.md | n/a | 15 | 1 | 15.0 | 15 | 0 | 0 |
| tess_2023.md | n/a | 19 | 1 | 19.0 | 19 | 0 | 0 |
| wtma_workshop.md | n/a | 16 | 1 | 16.0 | 16 | 0 | 0 |
| zenq_2022.md | n/a | 18 | 1 | 18.0 | 18 | 0 | 0 |

No summary exceeds 100 words, no excerpt exceeds 20, no paragraph exceeds 4
sentences and no sentence exceeds the Tier B 25. Em dash count 0 and en dash
count 0 in all new prose. The em dashes and non-breaking spaces in the IBRC
2025 abstract sit inside its record markers, where they belong and where no
new prose can inherit them. Banned word hits 0, unexpanded acronyms 0, no
excerpt asks a question.

## 3. Side-by-side: the rows

Before this pass the talk rows carried no excerpt at all (DECISIONS 45: the
only existing prose was full abstracts, and auto-excerpting them was the
sitemap failure the audit flagged). The "before" column is therefore what a
reader saw on `/research/`: title, venue, award, nothing else. Full line
diffs are in the PR files view.

| talk | before | after |
|---|---|---|
| Songs of disappearance (ZENQ 2023) | no excerpt | "Climate drivers split rainforest bird populations by elevation: lowland species gained, upland species declined under the same warming." |
| Predicted alteration of vertebrate communities (ESA-SCBO 2022) | no excerpt | "Species climb at different speeds under warming, so mountain communities reshuffle and high-elevation species face mass local extinction." |
| PhD exit seminar (James Cook University 2024) | no excerpt | "Three decades of monitoring show birds tracking gradual warming while ringtail possums collapse under extreme heatwaves." |
| Microclimatic drivers (International Bat Research Conference 2025) | no excerpt | "Solar radiation, not air temperature alone, drives spectacled flying foxes into high-cost cooling behaviour such as fanning." |
| Crisis in the tropics (CBCS 2023) | no excerpt | "More than 30 years of rainforest monitoring show climate change eroding montane biodiversity fastest among narrow-range species." |
| Seasonal variation in urban wetlands (Chilean Ornithology 2017) | no excerpt | "Bird richness peaks in spring across the urban wetlands of Llanquihue, and diversity stays high all year." |
| Introduction to hierarchical models (CodeR 2022) | no excerpt | "Hierarchical models estimate population size from counts of unmarked animals, while separating real change from imperfect detection." |
| Why canopy microclimate matters (National Flying Fox Forum 2025) | no excerpt | "Roost canopies differ by several degrees, so standard weather data can understate the heat risk to flying foxes." |
| Predicting species abundance (TESS 2021) | no excerpt | "Environmental suitability predicted local abundance for 50 endemic species, explaining 55% of deviance on average." |
| Possums in Peril (TESS 2023) | no excerpt | "Warming pushes ringtail possums up the mountains, and the species already near the summits have nowhere left to go." |
| An uphill battle (Wet Tropics Management Authority 2024) | no excerpt | "Rainforest ringtail possums are declining under climate change, evidence brought to a Wet Tropics threat workshop." |
| Climate change threatens ringtail possums (ZENQ 2022) | no excerpt | "Extreme heatwaves drove a severe ringtail possum decline, and the forecast has populations below viability thresholds by 2050." |

The TESS 2021 excerpt is deliberately the first sentence of its paper page's
index entry: the same work, and the 2 surfaces must not disagree (the
DECISIONS 79 principle). The ZENQ 2023 and ESA-SCBO excerpts are written
differently from their papers' index entries, because the talk and the paper
now both have pages and neither should read as a copy of the other.

## 4. Side-by-side: the pages

The 4 pages previously opened with the raw abstract, prefixed "Abstract - ".
They now open with a 100-word summary, and the abstract sits below in a
collapsed "Original abstract as submitted" block, verbatim.

**Songs of disappearance (2023).** Before: "Abstract - Climate-driven
biodiversity erosion is escalating at an alarming rate..." After: "Not every
rainforest bird is losing. I showed hierarchical population models for 47
species in the mountains of the Australian Wet Tropics..."

**Predicted alteration of vertebrate communities (2022).** Before: the
poster line, then "Abstract - Climate change is driving species to migrate
to novel areas..." After: "Climate change does not move a community, it
moves each species at its own speed..." The poster arc moved into front
matter and renders as an "Also presented" block with its title verbatim and
the local PDF link intact (DECISIONS 102).

**PhD exit seminar (2024).** Before: "Abstract - Climate change has exposed
biodiversity to unprecedented conditions..." After: "Two animals in the same
rainforest fail in two different ways..." The page links the published
thesis at its DOI (DECISIONS 101).

**Microclimatic drivers (2025).** Before: "Abstract - Climate change is
exerting profound impacts on biodiversity..." After: "Air temperature is the
number managers use to predict heat risk for flying foxes, and it is not
enough..." No paper exists yet, so the page links nothing.

The excerpts also now feed each page's meta description through the existing
head logic. Before this pass those descriptions were Jekyll's auto-excerpt,
which was the first sentences of the abstract.

## 5. Audience check

One line per audience per talk page (brief 2.2).

**Songs of disappearance 2023.** Recruiter: he ranks causes and says which
one matters, in a talk that won its meeting's prize. Peer: 47 species, 5
drivers estimated jointly, elevation as the axis where the sign flips, with
the paper page 1 click away. Academic: the finding stated as published,
including the marginal cyclone and drought result, above the submitted
abstract.

**Elevational shifts 2022.** Recruiter: a simulation at real scale, 7,613
assemblages, with an award at the field's main Australasian meeting. Peer:
the per-species dispersal design and the thermal resistance layers that make
community reshuffling measurable. Academic: the escalator to extinction
framing with its source linked, the poster-to-talk arc intact, and the paper
page for the full method.

**PhD exit seminar 2024.** Recruiter: one sentence for a phone screen, two
species failing in two different ways under the same warming. Peer: press
against pulse as an explicit contrast, and the move from trend to mechanism
that the rest of the record is built on. Academic: the whole doctorate in
100 words, the submitted abstract below it, and the published thesis linked
at its DOI.

**Flying fox heat 2025.** Recruiter: current postdoctoral work, so the
research record is alive and not a 2022 artefact. Peer: behavioural
observation joined to microclimate measurement, and the finding that the
cheap predictor fails exactly where the cost is highest. Academic: the
solar radiation result stated as submitted, with the abstract, its em dashes
and its Latin name untouched below.

## 6. Checker and build

`prose_check` runs green over 50 files plus the stats include
(`prose-check-output-talks.txt`). `check_publication` became
`check_front_matter`, shared by publications and talks. The 12 new talk
checks (excerpt ceiling, excerpt question, missing excerpt, summary budget,
missing summary on a page, summary on a redirect entry, body prose outside
record markers, em dash, en dash, banned word, over-length sentence,
over-length paragraph) each fired on a seeded violation before landing
clean; the log is `seeded-violations-talks.txt`. The build is warning-free
(`build-output-talks.txt`). CI runs the checker via the existing workflow on
this branch's pushes and PR.

Out of scope and logged, not fixed: the `/research/` page's rendered prose
sits above its 700-word budget mainly because the 2 teaching entries run 367
words against a 120 budget, which the `_teaching` pass owns (FINDINGS 15).
