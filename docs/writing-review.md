# Writing review: audit and rewrite plan

Written 2026-09-05. Phase 1 of the site-wide prose review. Excluded from
the Jekyll build like the rest of `docs/`. Phase 2 (the rewrite) appends
a change log at the end of this file, one entry per page.

## 1. How the site is built and where prose lives

Jekyll on GitHub Pages, no theme, one vanilla JS file. Prose lives in
five places:

| Surface | Where the words are | Rendered at |
|---|---|---|
| Static pages | `_pages/*.md` and `*.html` (hero, leads, timeline, skills text) | `/`, `/work/`, `/skills/`, `/projects/`, `/apps/`, `/digital-twin/`, `/research/`, `/research/threatened-species/`, `/terms/`, `/sitemap/`, `/404.html` |
| Project pages | `_projects/*.md` body, plus the `excerpt` front matter that becomes the card blurb on `/projects/` | `/projects/<slug>/` |
| Paper pages | `_publications/*.md` front matter only: `excerpt` (index row on `/research/`) and `summary` (page opener). The body is the verbatim abstract inside record markers and is never touched | `/research/<slug>/` |
| Talk pages | `_talks/*.md` front matter: `excerpt` (row on `/research/`) and, on 4 talks, `summary` | `/research/<slug>/` |
| Data-driven blurbs | `_data/apps.yml` (`pitch`, `demonstrates`, `note`), `_data/education.yml` (`detail`), `_data/grants.yml` and `_data/awards.yml` (`detail`), `_teaching/*.md` | `/apps/`, `/skills/`, `/work/`, `/research/` |

The home page carries 6 hand-written "Selected work" cards whose text
duplicates project excerpts and paper excerpts. The apps page pitches
duplicate the same 3 engineering excerpts. Any rewrite of a project
opener therefore touches up to 3 places: the page, its `excerpt`, and
the matching home card or app pitch.

Everything is policed by `scripts/prose_check.py` in CI. Its enforced
rules matter for the rewrite: no em or en dash outside record markers,
the banned-word list, at most 20 words per sentence on Tier A files
(project pages, apps, skills) and 25 on Tier B (home, work, research,
paper and talk summaries), at most 4 sentences per paragraph, acronyms
expanded on first use, and per-surface word budgets (home 450, project
opener 120 before the first heading, excerpt 25, paper summary 120,
talk summary 100, app pitch 25). Meta descriptions must be a verbatim
substring of the page prose.

## 2. Overall assessment

The site is accurate almost everywhere. Of 46 prose surfaces, 7 carry
a claim the primary source does not support, and none of those
misstates a research result. The engineering pages drifted where the
repos moved on after the page was written, and two lab pages describe
content their READMEs do not list.

The writing problem is uniform and structural. The refurbishment wrote
every page to the Simplified Technical English standard with numerals
for all numbers, and the result reads like a specification: one idea
per sentence, sentences of 8 to 14 words stacked without connectives,
paragraphs that open with a digit, and technical terms used as if the
reader already owns the project. A non-technical visitor cannot follow
the 7PH Graph, Deck Optimisation Engine, Job Intelligence Engine or
Digital Twin pages past the first paragraph. A technical visitor gets
precision but no story: what problem, why it matters, what happened,
what it cost.

Three patterns recur on nearly every page:

1. **Telegraphic runs.** "The app never fetches or builds. It opens a
   promoted artifact read-only. The deployed instance therefore carries
   no upstream credential at all." Three sentences, one idea, no link
   between them.
2. **Sentences that open with a numeral.** 41 of them across the site,
   a side effect of the numerals-for-all-numbers rule: "3 commands
   split the system", "28 decks held a known placement", "17 years of
   standardised bird monitoring", "820,000 Amazon products enter".
3. **Untranslated terms.** Area under the curve, R², mean reciprocal
   rank, nDCG, counterfactual, provenance, bootstrap, permutation test,
   posterior, credible interval, deviance, N-mixture, partial pooling,
   detection, quasi-extinction, beta-diversity, dispersal probability,
   thermal resistance surface, collinearity, link function, semaphore,
   JSONL checkpoint, temperature 0, QLoRA, 4-bit NF4 quantisation,
   t-SNE, mist-netting, canary corpus, guardrail, camp, the 75, fresh
   window, stratum, candidate universe.

The research pages are in better shape than the engineering pages.
Their "What this taught me about evaluation" closers are the best
writing on the site and should be kept nearly as they are. The paper
summaries are sound and mostly need connective tissue and one or two
translated terms each.

## 3. Per-page audit

Treatment key: **light** (sentence-level edits, translate terms, join
fragments), **restructure** (reorder into a story, keep most sentences),
**full** (rewrite from the source). Source status: **verified** means I
read the primary source and checked every factual claim on the page
against it.

### 3.1 Static pages

| Page | Source checked | Accuracy | Style | Treatment |
|---|---|---|---|---|
| Home `/` (`_pages/home.html`) | Owner-authored bio. Cards checked against the project and paper pages they point to | Job Intelligence Engine card repeats the 6,100 figure (see 3.2). No other issue | Hero is the warmest prose on the site and reads well. Cards are excerpts and inherit their pages' problems: "provenance and statistical guards", "judge model scores the extraction layer's accuracy", "model chain from microclimate to physiology to demography" | light (hero), cards follow their pages |
| Work `/work/` | Owner CV, no external source. Flying fox loss in the 2018 heatwave is public record | Nothing to correct | Lead is good. Timeline entries are competent but flat: "I build production AI systems for a national retailer" then a list. Fine as a timeline | light |
| Skills `/skills/` | Owner-authored | Nothing to correct | Bullet lists are keyword rows and stay that way. Intro paragraph is a stack of 4 assertions. Terms untranslated: RAG, groundedness, judge models, QLoRA, partial pooling, N-mixture, SHAP, leakage, calibration | light: intro and the 3 capability leads |
| Projects `/projects/` | n/a | n/a | Lead is fine | none (cards follow their pages) |
| Apps `/apps/` (`_data/apps.yml`) | Same READMEs as the project pages | Job Intelligence Engine pitch repeats 6,100 | Pitches are the project excerpts, same faults. "Demonstrates" lines are cryptic: "a frozen baseline scores retrieval and answer quality" | light, in step with each project |
| Digital twin `/digital-twin/` | n/a (2 hidden sentences for screen readers) | ok | ok | none |
| Research `/research/` | n/a | ok | Lead is good. Talk excerpts and paper excerpts are the rows, see 3.3 and 3.4 | light (book chapter line only) |
| Threatened species `/research/threatened-species/` | Nomination list is a record. Escalator to extinction link checked | ok | Good already. "Climate change is emptying the mountain tops" is the right register | none |
| Terms, sitemap, 404 | n/a | Terms says the twin chat is "on the home page". It moved to `/digital-twin/` on 2026-08-08 (DECISIONS 146) | fine | light: fix the location |

### 3.2 Engineering and lab project pages

| Page | Source checked | Accuracy issues | Style issues | Treatment |
|---|---|---|---|---|
| Digital Twin `/projects/digital-twin/` | [README](https://github.com/AlejandroFuentePinero/digital-twin), `src/ingest.py`, `src/retrieval.py`, `docs/DECISIONS.md`, `docs/MAINTENANCE.md`, `eval/tests.jsonl`, `data/canaries/corpus.json` (verified) | **Stack line says `text-embedding-3-small`; the code and README use `text-embedding-3-large`.** The drift trend "12, then 9, then 6" was true at the July and August points but the latest canary (DECISIONS session after Aug 3) records 9 major flags, the first increase. Restate as a range or drop the trend. 0.866 MRR, 4.56 accuracy, 149 questions, 7 types, 50 canaries, 52 flags with 33 from re-chunking, 6 to 7k tokens: all confirmed | Opener leads with a metric no visitor can read (MRR). "Guardrail", "frozen baseline", "canary corpus", "drift", "classifier" untranslated. Architecture section is a component list, not an explanation of why a second model reads every answer | restructure |
| 7PH Graph `/projects/7ph-graph/` | [README](https://github.com/AlejandroFuentePinero/7ph-graph), ADR 0011, 0016, 0017, `docs/deploy.md`, `docs/research-log.md`, acceptance report (verified) | **"24 architecture decision records": the repo now holds 26.** Every other figure confirmed: 28 decks with 27 top-8, 4.9 of the top 8 survive a resample, rank 7 interval 1 to 40, permutation 0.0915 against 0.0885 with range 0.0823 to 0.0947, tests larger than source, Playwright and WCAG AA pass, Kùzu to Ladybug, protected Space | The hardest page on the site to read cold. "Provenance", "statistical guards", "rule name", "immutable snapshot", "promoted artifact", "recorded oracle", "bootstrap", "permutes", "honest interval" all unexplained. "The flag is an action for a human, not a notice" and "The design covers classes of uncertainty not yet invented" only make sense to the author. Sentences open with 3, 28, 27 | full |
| Job Intelligence Engine `/projects/job-intelligence-engine/` | [README](https://github.com/AlejandroFuentePinero/job-intelligence-engine), [technical report](https://github.com/AlejandroFuentePinero/job-intelligence-engine/blob/main/docs/narrative/technical_report.md) (verified) | **"6,100 postings" appears nowhere in the sources; the report gives 6,162** (the job by skill matrix). Fix on the page, the excerpt, the home card and the app pitch. 27 skill models, ROC AUC 0.88 to 0.95, test R² 0.30, MAE about 25k, 20 latent families, frozen universe, non-overlap contract: all confirmed | "Area under the curve", "R²", "counterfactual", "calibrated demand probabilities", "candidate universe", "latent job families", "contract evaluations" untranslated. Opens with a metric sentence starting "27 per-skill models" | restructure |
| AI-JIE `/projects/ai-jie/` | [README](https://github.com/AlejandroFuentePinero/ai-jie), [technical report](https://github.com/AlejandroFuentePinero/ai-jie/blob/main/docs/technical_report.md) (verified) | **"Cohen's kappa tracked agreement between judge and human" is not in the README or the report.** The report records a human evaluation of 10 v20 extractions compared against judge scores, without kappa. Drop the kappa claim. Everything else confirmed: 4.11 of 5, structural fields at 5.00, 3,892 postings, 33 versions, semaphore of 20, temperature 0, about 3 times faster, 2.96 circular judge, 36% to 78% industry hint, 12 judge dimensions, 3 seeds | Best-structured engineering page; the story is already there. "Chain-of-thought scaffolding", "Pydantic-validated", "semaphore", "JSONL checkpoint", "temperature 0", "passthrough fields", "section-boundary guard" untranslated. Sentences open with 3 and "Overall human score" fragment | light to restructure |
| Deck Optimisation Engine `/projects/deck-optimisation-engine/` | [README](https://github.com/AlejandroFuentePinero/deck-optimisation-engine), [postmortem](https://github.com/AlejandroFuentePinero/deck-optimisation-engine/blob/main/docs/postmortem-2026-08-08.md) (verified) | Nothing to correct. 19,691 lists from 508 events, 6 to 9% power, 22 to 32 point floor, 163 tests, 5 retries: all confirmed | Written in the repo's private vocabulary: "camp", "stratum", "window", "the 75", "flex slots", "mainboard and sideboard", "fresh window", "detection floor", "statistical power", "disconfirmation instrument". None defined. A visitor who does not play Magic cannot start. The audit story (the engine measured itself and demoted half its readings) is the strongest engineering narrative on the site and is buried | full |
| LLM Engineering Lab `/projects/llm-engineering-lab/` | [README](https://github.com/AlejandroFuentePinero/llm-engineering-lab) (verified) | Nothing to correct. $29.95 MAE, 86.3% R², 10,000 held out, 820k curated, 800k in the vector store, 23k lite, 110-token cap, T4, 80/10/10 ensemble weights, 5-minute refresh, 200-item runs: all confirmed. "11 projects" matches flagship plus 10 supporting | "R²", "QLoRA", "4-bit NF4 quantisation", "t-SNE", "held-out", "ensemble", "agent fleet" untranslated. Opens with "820,000 Amazon products enter". Flagship section is a pipeline description with no reason given for any step | restructure |
| MLB Analytics with SQL `/projects/mlb-analytics-sql/` | [README](https://github.com/AlejandroFuentePinero/MLB_Analytics_Project), `sql/advanced_queries.sql` (verified) | **"Physical attributes separate Hall of Fame careers from the rest": the README's Hall of Fame finding is debut age, career length and games played, not physique.** "Some low-payroll teams consistently beat expectations" is supported by an overperformers query in the SQL but the README's stated finding is the opposite emphasis (postseason success tracks payroll); soften "consistently" and pair it with the README's headline. Covariance-based trend slope confirmed in the SQL | Lab page, short. Fine once the findings are right | light |
| Python Labs `/projects/python-labs/` | 3 READMEs: [OOP](https://github.com/AlejandroFuentePinero/python-oop-mini-systems), [EDA](https://github.com/AlejandroFuentePinero/python-eda-mini-projects), [ML](https://github.com/AlejandroFuentePinero/python-ML-course-projects) (verified, folder listing confirmed) | **The machine learning repo holds 11 notebooks, not 12, and neither the README nor the folder names mention hierarchical clustering or PySpark.** Cross-validation appears only as a learning focus, not a section. Restate the ML collection from the README's catalogue. OOP and EDA descriptions confirmed | Lab page. Opens with "3 lab collections", "2 end-to-end pipelines", "12 sections". Otherwise fine for a catalogue | light |

### 3.3 Research project pages

Each is paired with a paper page. The abstract verifies the findings and
the sample sizes. Method detail beyond the abstract (algorithms,
software, validation design) comes from the papers' bodies and the
owner, and is marked "owner-verified" where I could not check it.

| Page | Source checked | Accuracy issues | Style issues | Treatment |
|---|---|---|---|---|
| Physiological stress and possum declines | Abstract via Crossref, [doi:10.1111/gcb.70215](https://doi.org/10.1111/gcb.70215) (verified) | None. Findings, 2 species, 30 years, mechanisms per species all match | Good opener ("Climate change kills through mechanisms"). "4 model components feed one inference" opens with a numeral. "Open population model", "joint inference", "scenario testing", "recruitment" untranslated | light |
| Climatic drivers of rainforest bird change | Abstract via Crossref, [doi:10.1111/gcb.16608](https://doi.org/10.1111/gcb.16608) (verified) | None. 47 species, 2000 to 2016, 5 drivers, heatwave effect, marginal cyclones all match. Satellite cyclone metric is owner-verified | Good. "State process", "observation process", "site-year level", "collinearity" untranslated | light |
| Ringtail possum viability forecast | Abstract via Crossref, [doi:10.1111/ddi.13652](https://doi.org/10.1111/ddi.13652) (verified) | None. 1992 to 2021, forecast to 2050, heatwaves as main driver, viability thresholds all match | Opener is 3 flat sentences ending in the EPBC Act. "Imperfect detection", "fitted mechanism", "credible interval", "quasi-extinction" untranslated | restructure (sample below) |
| Community reshuffling | Abstract via Crossref, [doi:10.1111/ddi.13514](https://doi.org/10.1111/ddi.13514) (verified) | None. 7,613 assemblages, dispersal success, extinction rate rising with elevation all match | "Dispersal probability", "thermal resistance surfaces", "dissimilarity indices", "beta-diversity" untranslated. Second paragraph is a method list | light |
| Climate, foliage chemistry and herbivory | Abstract via Crossref, [doi:10.1007/s00442-024-05630-y](https://doi.org/10.1007/s00442-024-05630-y) (verified) | None. 25 sites, 3 species, geology over single nutrients, species-specific responses all match | "Pathway coefficients", "mediated paths", "random effects for site nesting" untranslated. "3 widespread rainforest tree species anchored" opens with a numeral | light |
| Rainforest bird declines | Abstract via Crossref, [doi:10.1371/journal.pone.0254307](https://doi.org/10.1371/journal.pone.0254307) (verified) | None. 17 years, 1,977 surveys, 114 sites, 42 species, over 40% and almost 50%, 190% match. The abstract names TRIM (a log-linear trend model), which the page calls generalised linear models: compatible, owner-verified. Effort and habitat covariates are owner-verified | Opens with "17 years of". "14 species carried enough evidence" opens with a numeral. Otherwise clear | light |
| Predicting abundance from suitability | Abstract via Crossref, [doi:10.1111/ecog.05776](https://doi.org/10.1111/ecog.05776) (verified) | None. 50 species, 29 years, 55% deviance match. The 9 algorithms and spatial cross-validation are owner-verified (not in the abstract) | "Deviance", "presence-only", "spatial folds", "link functions", "calibration" untranslated. "9 algorithms model" opens with a numeral | light |
| Forest gap effects on tropical birds | Abstract via Crossref, [doi:10.37828/em.2025.88.11](https://doi.org/10.37828/em.2025.88.11) (verified) | None. 5 years, 1,148 captures, 81 species, flycatcher, 130 to 1,020 m² match | "Mist-netting", "error structures", "residual diagnostics" untranslated. Otherwise clear | light |
| Seasonal altitudinal migration | **No source. Manuscript under review at Diversity and Distributions, no preprint linked** | Cannot verify. Rewrite with caution: keep every number and claim exactly as the page states them | "N-mixture", "centred season", "random slopes", "posterior predictions", "centroid shift", "turnover" untranslated. "Breathe with the seasons" is a good image and can stay | light, no factual change |

### 3.4 Paper pages (front matter `summary` and `excerpt` only)

Abstracts were re-fetched and compared byte for byte with the record
blocks: all 12 match.

| Paper | Source checked | Accuracy | Style | Treatment |
|---|---|---|---|---|
| Physiological stress (2025) | Crossref abstract (verified) | ok | Good. Latin names unexplained (which possum is which) | light |
| Mountains magnify mechanisms (2026) | Local PDF, standfirst and body (verified) | ok | Good | light |
| Abundance and niche theory (2021) | Crossref abstract (verified) | ok | "Deviance" untranslated | light |
| Community reshuffling (2022) | Crossref abstract (verified) | ok | "Dissimilarity indices" untranslated | light |
| Climatic drivers of bird change (2023) | Crossref abstract (verified) | ok | Good | light |
| Chusquea flowering (2017) | Local PDF, English summary (verified) | ok. 8 plots, 20 boxes, 33.50 and 17.66 Mg, 146.86 million, 87.5% match | Fine. "Phenology" could take a clause | light |
| Ringtail possums by 2050 (2022) | Crossref abstract (verified) | ok. "70 national news outlets" comes from the Mediaportal report on the page | Good | light |
| Urban wetland birds (2018) | Local PDF, English abstract (verified) | ok. 50 species, 55%, 20%, 35 and 24 match | "55% of the recorded species" opens with a numeral | light |
| Foliage chemistry and herbivory (2024) | Crossref abstract (verified) | ok | Good | light |
| Viscacha records (2021) | Local PDF, page 2 abstract (verified) | ok. 722 km matches | Good | none |
| Forest gap birds (2025) | Crossref abstract (verified) | ok | Good | none |
| Rainforest bird declines (2021) | Crossref abstract (verified) | ok | Good | none |

### 3.5 Talks, teaching, data blurbs

| Surface | Source | Accuracy | Style | Treatment |
|---|---|---|---|---|
| 4 talk summaries (`_talks/`) | Abstracts inside their record blocks | ok | Already narrative, first person, well paced. The best-written summaries on the site | none, except term translation where the paper pages change a term |
| 12 talk excerpts | Same | ok | Fine | none |
| Teaching and mentoring | Owner CV | ok | Fine | none |
| `_data/education.yml` details | Owner CV | ok | Fine | none |
| `_data/grants.yml`, `_data/awards.yml` | Owner CV, record | never edited | n/a | none |

### 3.6 Sources not reachable or not checked

- **Seasonal altitudinal migration** (`_projects/bird-elevational-migration.md`): no public source. Marked "rewrite with caution, no source verified".
- **Home hero, work timeline, skills intro**: owner-authored biography with no external source. Treated as verified page content.

## 4. Factual corrections to make in Phase 2

1. Digital Twin: embedding model is `text-embedding-3-large`.
2. Digital Twin: the canary drift trend is no longer monotone. Report the detector cleanup (52 to 12 flags) and drop the "12, then 9, then 6" line, or state the current point.
3. 7PH Graph: 26 architecture decision records, not 24.
4. Job Intelligence Engine, home card, app pitch, excerpt: 6,162 postings, not 6,100.
5. AI-JIE: remove the Cohen's kappa sentence.
6. MLB Analytics: replace the Hall of Fame physique finding with the README's (debut younger, play longer, more games); soften the low-payroll claim to what the query shows.
7. Python Labs: describe the ML collection from its repo (11 notebooks, no PySpark or hierarchical clustering).
8. Terms page: the twin chat lives at `/digital-twin/`, not the home page.

## 5. Proposed style guide for the rewrite

The rewrite stays inside `scripts/prose_check.py` as it stands. Every
rule below fits under the checker's ceilings, so no budget, tier or
banned-word change is needed, and CI keeps enforcing the mechanics.

**Voice.** First person. "I" for every decision, design choice and
piece of analysis that was mine, on engineering and research pages
alike. "We" survives only where a finding belongs to the co-author
team of a paper, and then only in paper summaries and talk summaries.
Where "we" would be ambiguous, name the thing instead: "the study
found", "the model shows".

**Shape of a project page.** The opener (under 120 words, before the
first heading) answers, in this order: what problem, why it matters,
what I found or built, and the one number that proves it, with its
meaning attached. The level 3 headings stay exactly as they are
(Links, Architecture, The decision that was hard, What was measured,
What did not work, Role, What this taught me about evaluation). Each
section is a short story with a reason in it, not a component list.

**Sentences.** Vary length between about 6 and 20 words (25 on Tier
B). Join related ideas with "so", "because", "which", "and then".
Never open a sentence with a numeral: restructure, or lead with the
noun ("A total of 28 decks", "Across 47 species"). Numerals stay
numerals everywhere else, per the existing rule. No em or en dash, no
semicolon, no exclamation mark.

**Terms.** Every technical term gets a plain clause the first time it
appears on a page, and keeps its precise name beside the plain one:
"a hierarchical Bayesian model, which fits the population and the
chance of seeing an animal at the same time". Once translated on a
page, the precise term is used alone. A short site-wide translation
list goes into `TERMINOLOGY.md` so the same term gets the same clause
on every page.

**Numbers.** Keep every figure. Give it a meaning in the same sentence
or the next: "0.88 to 0.95 area under the curve, so the model picks a
role that needs a skill from one that does not about 9 times in 10".
Never a metric without a reading.

**Register.** Confident, warm, plain. Short words. No hype, no
rule-of-three flourish, no fragments for effect, no "delve", "leverage",
"seamless", "robust" or the rest of the banned list. Honest limits are
part of the story, not a disclaimer at the end.

**Consistency.** A project excerpt, its home card and its app pitch say
the same thing in the same words. Meta descriptions stay a verbatim
substring of the page, within 160 characters.

Two calls the brief leaves open, resolved as follows and logged in
`DECISIONS.md` at the start of Phase 2:

- Brief 6.3 (Tier A vocabulary: no synonyms, no idiom or metaphor,
  short common verbs) is relaxed for connective prose on project and
  app pages. The checker never enforced it and it is the direct cause
  of the telegraphic register. The enforced rules (6.2) stay.
- Sentence-initial numerals are banned site-wide. Rule 11 (numerals
  for all numbers) still holds inside sentences.

## 6. Sample rewrites

Three paragraphs from three different pages, written to the guide
above and checked against the prose checker's rules by hand (sentence
length, dashes, numerals, banned words).

### 6.1 Job Intelligence Engine, page opener (engineering, Tier A)

Current:

> The Job Intelligence Engine turns 6,100 job postings into ranked role
> recommendations. It separates the roles to target now from the roles
> worth a stretch, with the reasons attached. A counterfactual layer
> ranks which missing skill changes your options the most.
>
> The pipeline is deterministic end to end. The salary model explains
> about 30% of variance on held-out postings, the expected ceiling for
> noisy posted pay. 27 per-skill models score demand at 0.88 to 0.95
> area under the curve.

Proposed:

> Job hunting in data roles is hard because the options all look alike.
> Titles overlap, skill lists run long, and no posting tells you whether
> you are a realistic candidate. The Job Intelligence Engine reads 6,162
> real postings and answers that question for one person at a time.
>
> It sorts roles into 2 shortlists: target now, or worth a stretch. Each
> entry explains the gap. Then it asks a what-if question per missing
> skill: learn this, and how many stretch roles open up? Its skill models tell a role that needs a skill from one that does
> not about 9 times in 10. That is the 0.88 to 0.95 area under the curve
> reported below.

### 6.2 Ringtail possum viability forecast, page opener (research, Tier A)

Current:

> A hierarchical Bayesian model on 30 years of surveys forecast the
> collapse of rainforest ringtail possums by 2050. The forecast fed a
> national protection nomination for the lemuroid ringtail possum. The
> nomination ran under the Environment Protection and Biodiversity
> Conservation Act (EPBC Act).
>
> The model fits possum population dynamics in the Australian Wet
> Tropics from 1992 to 2021. It separates real population change from
> imperfect detection. It then runs the fitted mechanism forward to
> 2050 under forecast warming. Populations fall below viability
> thresholds within 3 decades, with extreme heatwaves doing most of the
> damage.

Proposed:

> Rainforest ringtail possums in the Australian Wet Tropics are on
> course to collapse by 2050. Extreme heatwaves are the main reason. I
> built that forecast from 30 years of possum surveys. It fed the
> lemuroid ringtail possum's national protection nomination under the
> Environment Protection and Biodiversity Conservation Act (EPBC Act).
>
> The hard part of counting possums is that you never see them all. A
> quiet night looks like decline. So the model has 2 layers: one for
> the chance of seeing a possum, one for how many are there. Once it
> learned how warming and heatwaves move survival, I ran it forward to
> 2050. Under forecast warming, populations fall below the level at
> which they can persist within 3 decades.

### 6.3 7PH Graph, "The decision that was hard" (engineering, Tier A)

Current:

> The source ships placements it never normalised and field sizes its
> own deck counts contradict. Some finishes exist only as a tie band.
> The easy design was a boolean estimated flag. The shipped design
> gives each uncertain value a companion column holding a rule name.
>
> The column is null where the source's own number stands. It holds a
> rule name where a pass here produced the value, and none where no
> rule fit. One query then answers: which of this deck's numbers did we
> decide, and under which rule? The design covers classes of
> uncertainty not yet invented.
>
> It earned its keep fast. 28 decks held a known placement with no
> norm, so every ranked average silently dropped them. 27 of the 28
> were top-8 finishes. The bias ran in one direction and hit hardest
> the pilots who made the cut.

Proposed:

> The tournament data arrives messy. Some events report a finish only
> as a band, such as top 8. Others report field sizes that their own
> deck counts contradict. The easy fix was a yes-or-no flag marking a
> value as estimated.
>
> I chose something stricter: every uncertain value gets a companion
> column that names the rule which produced it. The column stays empty
> when the source's own number stands. One query can then answer: which
> of this deck's numbers did the build decide, and under which rule?
> The same column will hold whatever new kind of uncertainty the next
> season brings.
>
> The design paid for itself fast. A total of 28 decks had a placement
> but no score on the shared scale. Every ranked average silently
> dropped them. All but 1 of the 28 were top-8 finishes. The
> bias ran one way, and it hit hardest the pilots who had made the cut.

## 7. Phase 2 plan

Order, one commit per page or small group, build and prose check after
each, change log appended below:

1. Factual corrections that touch several surfaces first (Job
   Intelligence Engine count, Digital Twin embedding model), so cards
   and pitches never disagree with pages mid-way.
2. Engineering pages, hardest first: 7PH Graph, Deck Optimisation
   Engine, Digital Twin, Job Intelligence Engine, LLM Engineering Lab,
   AI-JIE. Each page carries its excerpt, home card and app pitch in
   the same commit.
3. Lab pages: MLB Analytics, Python Labs.
4. Research pages, then paper summaries, in publication order.
5. Static pages: skills, work, home hero, terms.
6. Final read-through as a visitor, voice consistency pass, summary.

## 8. Change log

Appended during Phase 2, one entry per page.
