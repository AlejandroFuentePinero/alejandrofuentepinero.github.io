# Gate 5 evidence: the _projects pass

Branch `refurb/phase-5-projects`, 2026-08-07. Scope: the 16 content files in
`_projects/`, the prose_check extension to that collection, the TERMINOLOGY
additions, and the Phase 5 DECISIONS (75 to 83) and FINDINGS (9 to 11)
entries. Nothing outside `_projects/`, `scripts/`, and the project documents
changed. The apps copy was not started.

## 1. Metrics per file

Output of `python3 scripts/prose_check.py --metrics` (committed as
`prose-check-output-projects.txt`). All 16 project pages are Tier A
(20-word sentences). Project pages carry no total budget (level 3 is
unbounded per CONTENT_MAP 8); their budgets are the 120-word lead before
the first heading and the 25-word excerpt.

| file | lead / 120 | excerpt / 25 | words | sentences | mean | longest | em+en dashes | banned hits |
|---|---|---|---|---|---|---|---|---|
| 7ph-graph.md | 95 | 21 | 975 | 72 | 12.1 | 20 | 0 | 0 |
| ai-jie.md | 93 | 22 | 615 | 46 | 12.1 | 19 | 0 | 0 |
| digital-twin.md | 97 | 25 | 627 | 46 | 12.4 | 19 | 0 | 0 |
| job-intelligence-engine.md | 89 | 19 | 545 | 42 | 12.0 | 19 | 0 | 0 |
| llm-engineering-lab.md | 85 | 21 | 830 | 66 | 11.2 | 20 | 0 | 0 |
| mlb-analytics-sql.md | 75 | 20 | 185 | 13 | 12.2 | 20 | 0 | 0 |
| python-labs.md | 57 | 22 | 301 | 20 | 12.4 | 20 | 0 | 0 |
| bird-elevational-migration.md | 93 | 23 | 389 | 25 | 14.6 | 20 | 0 | 0 |
| dynamic-community-reshuffling.md | 92 | 22 | 383 | 25 | 14.1 | 19 | 0 | 0 |
| ecosystem-pathway-cascades.md | 81 | 22 | 385 | 24 | 14.5 | 20 | 0 | 0 |
| forecasting-popviability-ringtails.md | 94 | 20 | 414 | 29 | 13.0 | 18 | 0 | 0 |
| forest-gap-abundance-gradients.md | 83 | 21 | 378 | 26 | 13.0 | 20 | 0 | 0 |
| heightened-protection-bird-trends.md | 93 | 19 | 405 | 28 | 13.2 | 19 | 0 | 0 |
| physiological-stress-climate-populations.md | 83 | 21 | 453 | 32 | 13.0 | 20 | 0 | 0 |
| predicting-abundance-from-niche-theory.md | 80 | 21 | 426 | 31 | 12.5 | 20 | 0 | 0 |
| spatiotemporal-bird-climate-impacts.md | 85 | 22 | 427 | 29 | 13.3 | 20 | 0 | 0 |

Counting notes, for honesty about what the tool sees:

- The longest sentence on every page is at or under the Tier A ceiling of 20.
- Toolchain rows (Stack lines, "Python · Gradio · ...") count toward words
  but are token lists, not prose, and skip sentence checks (DECISIONS 83).
- Word counts include headings, link labels and table cells. No page has a
  total budget, so the words column is context, not a ceiling.
- The 2 new checks were verified to fire: a synthetic project page with a
  130-word lead and a 26-word excerpt fails with both messages, and the
  extended checker surfaced 11 real violations in the drafts before landing
  clean. The 10 _pages files and the stats-include digit check still pass.

## 2. Side-by-side: what each file said, what it says now

Every file was rewritten in full, so the full line diffs in the PR files
view are the complete record. This table isolates the card surface (the
excerpt) and the page opening, which carry the change. Facts, numbers,
names, dates and links survive exactly, except the 4 corrections the record
forced, each noted inline and logged (DECISIONS 75 and 81).

### 7ph-graph.md

| surface | before | after |
|---|---|---|
| excerpt | 66-word paragraph describing the graph, the pipeline and the guards | The live home card text, verbatim: "A live knowledge graph of a competitive Magic format: 107 events, 4,591 decks, every chart backed by provenance and statistical guards." |
| opening | "Competitive Magic: The Gathering formats generate a rich relational record..." (topic-first, method before result) | "7PH Graph is a live knowledge graph of the Australian 7 Point Highlander metagame... It links 107 events, 1,083 pilots, 4,591 decks and 4,995 cards behind an interactive explorer at 7phgraph.com." |

All counts, the permutation-test numbers (0.0915 against 0.0885, 90% range
0.0823 to 0.0947), the bootstrap (4.9 of the top 8, rank 7 interval 1 to
40), and the 28-deck imputation story are unchanged. The old "Refusals, not
guesses" and "Key engineering decisions" content now lives under the
template headings.

### ai-jie.md

| surface | before | after |
|---|---|---|
| excerpt | "An async LLM pipeline that extracts structured job intelligence... rigorous LLM-as-judge evaluation framework" (with an em dash) | "A chain-of-thought extraction pipeline turned 3,892 job postings into validated, intent-classified records. Human review scored the final prompt at 4.11 of 5." |
| opening | "Raw job postings are unstructured, inconsistent, and full of ambiguity..." (problem-first) | "AI-JIE reads raw job postings and produces validated job records with skills split by intent... A human evaluation of the final prompt scored 4.11 of 5, with structural fields at 5.00." |

Corrections per the technical report (owner's call, DECISIONS 75): the
extraction model arc is stated as gpt-4o-mini to gpt-5.4-mini, and the
page now carries the report's recorded failures (circular evaluation, judge
misalignment, the reverted industry-hint experiment). 33 versions, 3,892
postings, 28-posting human eval and 4.11 of 5 are unchanged.

### digital-twin.md

| surface | before | after |
|---|---|---|
| excerpt | "A conversational agent that answers professional questions about me — ..." (em dash, feature list) | "A conversational agent answers questions about my work, grounded in a curated knowledge base. A second model reviews every answer before a visitor sees it." |
| opening | "A 'tell me about yourself' page only goes so far..." (scene-setting) | "The digital twin is a conversational agent that answers questions about my work on my behalf... On the frozen evaluation baseline, retrieval scores 0.866 mean reciprocal rank and answers score 4.56 on the judge's scale." |

New recorded material from the twin's own decisions log and architecture
decision records: the monolithic-prompt failure behind classify-then-route,
the guardrail-blind-to-tool-content failure and its fix, the drift-detector
rebuild (52 flags on a healthy system down to 12), and the baseline numbers.
Models, the 149-question set, 7 question types, the 50-probe canary and the
privacy commitments are unchanged. Page copy only: the Space and its repo
were not touched (observe mode).

### job-intelligence-engine.md

| surface | before | after |
|---|---|---|
| excerpt | "A deterministic job-market intelligence system that turns messy postings into interpretable skill demand..." | The live home card text, verbatim: "An extraction pipeline turns 6,100 job postings into ranked role recommendations. A judge model scores the extraction layer's accuracy." |
| opening | "Job postings are noisy: roles and skills overlap heavily in meaning..." (problem-first, em dash in body) | "The Job Intelligence Engine turns 6,100 job postings into ranked role recommendations... The salary model explains about 30% of variance on held-out postings... 27 per-skill models score demand at 0.88 to 0.95 area under the curve." |

New recorded material from the technical report: the frozen candidate
universe as the hard decision, the measured results, the contract
evaluations, and the recorded limits (salary noise, dictionary extraction)
that cross-link AI-JIE as the successor extraction layer. The best-now and
stretch framing, suitability against competitiveness, and all links are
unchanged.

### llm-engineering-lab.md

| surface | before | after |
|---|---|---|
| excerpt | "Eleven production-minded Python projects spanning the full LLM engineering stack — ..." (em dash, 58 words) | "11 projects spanning retrieval, fine-tuning and autonomous agents. The flagship ensemble predicts product prices with a mean absolute error of $29.95." |
| opening | "This lab is my sandbox for building LLM systems that hold up in real work..." | "This lab holds 11 Python systems across the language model stack... Its final ensemble reaches a mean absolute error of $29.95 and R² of 86.3% on 10,000 held-out products." |

Per the owner's pointer to the repo README: the ensemble result, the
weighted-resampling failure story (models gaming the mean absolute error by
guessing low) and the fair-benchmark decision fill the brief 4.6 sections.
The 1,546-word page restructures into the template with the pipeline
numbers (820,000 products, 110-token cap, 80/10/10 ensemble), the model
benchmark table, and one-line entries for the 10 supporting projects.

### mlb-analytics-sql.md and python-labs.md (labs)

| surface | before | after |
|---|---|---|
| MLB excerpt | "End-to-end SQL analytics project using the Lahman Baseball Database..." | "A reusable SQL workflow answered 4 questions on 150 years of baseball data, from college talent pipelines to payroll overperformance." |
| Python labs excerpt | "Three lab collections: object-oriented Python systems, exploratory data analysis, and classical machine learning, built as one learning progression." | "3 lab collections, one progression: object-oriented Python systems, exploratory data analysis and classical machine learning, the practice ground behind the shipped systems." (the DECISIONS 47 polish) |

Both open with the outcome and say plainly that they are practice labs.
They omit the hard-decision and did-not-work sections (DECISIONS 80).
Dataset ranges, algorithms, class names and all 4 repository links are
unchanged.

### The 9 research pages

All 9 move from the Problem / Approach / Stack / Results / Impact template
to the engineering template, open with the finding, and close with "What
this taught me about evaluation" plus their paper page in Links. The
apology framing is gone: no page calls itself a case-study presentation of
research. Representative openings:

| page | before (topic-first) | after (result-first) |
|---|---|---|
| forecasting-popviability-ringtails | "Understanding population sustainability is critical to conservation prioritisation—but count data are often imperfect..." | "A hierarchical Bayesian model on 30 years of surveys forecast the collapse of rainforest ringtail possums by 2050. The forecast fed a national protection nomination..." |
| heightened-protection-bird-trends | "Rapid shifts in bird population trends can signal emerging conservation needs..." | "17 years of standardised bird monitoring showed upland rainforest populations nearly halving. The evidence supported protection nominations for 14 rainforest species..." |
| bird-elevational-migration | "Seasonal shifts in abundance along mountain gradients—known as altitudinal migration—remain one of the least quantified..." | "Rainforest bird communities in the Australian Wet Tropics breathe with the seasons. Most species shift uphill in summer and downhill in winter." |
| spatiotemporal-bird-climate-impacts | "Tropical montane bird populations are increasingly threatened by climate change and extreme events..." | "Not every climate driver matters equally, and this study measured which ones move rainforest bird populations." |

Numbers added to research pages come from the papers' published abstracts
(1,977 surveys, 114 sites, 42 species, the 40% / 190% / 50% changes, 7,613
assemblages, 25 sites, 3 tree species, 1,148 captures, 81 species, 50
species, 55% deviance, 47 species). 2 old-page claims were corrected to the
papers and logged (DECISIONS 81): 23 focal species became the paper's 50,
and the cyclone-damage headline became the paper's marginal-effect finding.
The hard-decision sections state each paper's recorded crux (DECISIONS 75),
and "What did not work" appears on the 5 pages whose papers record a
negative or equivocal result, and is omitted on the other 4.

## 3. Audience check

One line per audience per page, against brief section 2.

**7PH Graph.** Recruiter: a live graph product with 4,591 decks and a
domain, reachable in one click. Peer: provenance columns, refusal design,
a permutation test that killed a shipped chart. Academic: statistical
honesty (bootstrap intervals, null-model testing) applied to a hobby
dataset.

**AI-JIE.** Recruiter: an extraction pipeline scored 4.11 of 5 by human
review. Peer: extract-then-classify scaffolding, circular-eval bug, judge
calibration, a reverted experiment with its numbers. Academic: inter-rater
agreement, cross-seed validation, an honest 4.00 on the weakest dimension.

**Digital twin.** Recruiter: the agent that answers questions about him,
with a second model checking it. Peer: classify-then-route with recorded
failure modes and a 0.866 MRR baseline. Academic: a 149-question evaluation
design with drift monitoring, uncertainty about its own answers built in.

**Job Intelligence Engine.** Recruiter: 6,100 postings turned into ranked
recommendations in a live app. Peer: frozen-universe counterfactuals,
contract evaluations, honest R² of 0.30. Academic: calibrated probability
models and a stated refusal to over-claim causality.

**LLM Engineering Lab.** Recruiter: 11 systems, a $29.95 mean absolute
error flagship. Peer: fair-benchmark design, the resampling exploit, QLoRA
details. Academic: a same-held-out-split comparison across 12 model
families.

**MLB SQL and Python Labs.** Recruiter: SQL and Python fundamentals,
honestly labelled practice. Peer: window functions and class design without
inflated claims. Academic: transparent about what is coursework, which
protects the credibility of everything labelled research.

**Possum forecast.** Recruiter: a forecast that fed a national protection
nomination. Peer: detection separated from state, mechanism propagated
forward, thresholds stated. Academic: the published method summarised
accurately, with the paper page and Dryad one click away.

**Bird declines.** Recruiter: 17 years of evidence behind 14 protection
nominations and a live app. Peer: per-species models over a pooled index,
effort adjustment as the load-bearing choice. Academic: the PLOS One
numbers stated exactly, nominations named by framework.

**Elevational migration.** Recruiter: a first-of-its-kind measurement,
current work. Peer: the interaction-term definition and centred coding.
Academic: an under-review manuscript described without overclaiming.

**Community reshuffling.** Recruiter: 7,613 simulated communities,
escalator to extinction. Peer: per-species dispersal against the uniform
alternative, compute as method. Academic: the PNAS framing linked, the
paper's conclusions intact.

**Pathway cascades.** Recruiter: cause-to-effect modelling on real field
data. Peer: structured network over pairwise regressions, an equivocal
result reported. Academic: the negative soil-nutrient finding stated,
which is the paper's actual point.

**Physiological stress.** Recruiter: a model chain that explains why
populations decline. Peer: mechanistic-plus-statistical join with
propagated uncertainty. Academic: species-specific mechanisms, the
divergent H. lemuroides result kept.

**Niche theory.** Recruiter: predicting abundance where surveys are too
expensive. Peer: spatial cross-validation as the hard call, 55% deviance.
Academic: the interspecific-variation caveat reported, not averaged away.

**Climate drivers.** Recruiter: which climate drivers matter, measured.
Peer: joint estimation of 5 drivers, satellite-derived damage predictor.
Academic: the marginal cyclone result stated plainly, matching the paper.

**Forest gaps.** Recruiter: analytical role in an international
collaboration. Peer: gradient models over category tests, per-slice logic.
Academic: the null total-abundance result leads, the collaboration credited.

## 4. Checker and build

- `python3 scripts/prose_check.py` exits clean over all 26 files and the
  stats include: `prose-check-output-projects.txt`.
- `bundle exec jekyll build` is warning-free: `build-output-projects.txt`.
  All 16 project pages render under `_site/projects/`.
- The 4 home-card excerpts were machine-compared against
  `_pages/home.html` and agree byte for byte.
- CI (`.github/workflows/prose-check.yml`) runs the same checker on this
  branch unchanged.
