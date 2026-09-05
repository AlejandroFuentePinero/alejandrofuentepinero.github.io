# TERMINOLOGY.md: one term per concept

Started during the Phase 5 `_pages` pass, per REFURB_BRIEF.md section 6.2 rule 9.
Every naming choice on the site is recorded here so later passes reuse it instead
of inventing a synonym. Excluded from the Jekyll build. Verbatim records
(citations, abstracts, titles of degrees, courses, grants, awards and talks) keep
their original wording and outrank this file.

## People and roles

| Concept | Term | Not | Notes |
|---|---|---|---|
| The site owner in prose | I, me | "Alejandro" in third person | The site speaks in first person. The name appears in the hero, citations and metadata. |
| Current profession | AI engineer | AI/ML engineer, data scientist | Matches the settled role line. |
| The doctorate as a credential | Ph.D. in Quantitative Ecology, James Cook University, 2024 (Cum laude) | Zoology and Ecology | Settled at Gate 5 with the owner. Applied on /work/, the timeline and the CV PDF. |
| The doctorate in prose | PhD | Ph.D., doctorate | "PhD candidate", "my PhD". Periods only in the formal credential line above. |
| Degree abbreviations in records | B.S., M.S., Ph.D. | BS, MS, PhD | The education list keeps the CV's punctuation, normalised to a trailing period. |

## The work

| Concept | Term | Not | Notes |
|---|---|---|---|
| The three project types | engineering, research, lab | case study, portfolio piece | Filter values and card labels. Plural "labs" only in the filter button. |
| Things on /apps/ | app, live app | demo, tool, product | "Live apps" is the settled stats band label. |
| The home page chatbot | the digital twin | twin bot, chatbot, AI twin | "Digital twin" capitalised only as a card or app name. |
| The twin's checking model | a second model, judge model | guardrail model, LLM-as-judge | In prose. The settled chip label "LLM-as-judge evaluation" is the keyword form and stays. |
| Language models in prose | language model, model | LLM | The acronym stays out of prose. It survives in chip labels and verbatim course titles. |
| Statistical modelling family | hierarchical Bayesian model | Bayesian hierarchical model | The chips "Bayesian inference" and "Hierarchical models" are settled labels, unchanged. |
| Knowing whether a thing works | evaluation | evals, testing, validation | "Validation" only in its statistical sense inside research depth. |
| Quantified doubt | uncertainty | error bars | "Honest error bars" survives only in the settled hero. |
| The measurement-first credo | if it can't be evaluated, it can't be trusted | variants | Lives in the /work/ intro. The /projects/ variant "If I can't measure that it works, I don't ship it" is its shipping form, used there only. |

## The record

| Concept | Term | Not | Notes |
|---|---|---|---|
| The study region | the Australian Wet Tropics, then the Wet Tropics | Wet Tropics of North Queensland | Full form on first use per page. The heritage-area phrase appears only in verbatim records. |
| Papers in prose | paper, publications (section) | article, manuscript | "Peer-reviewed papers" is the settled stats band label. |
| The legal outcome | protection nomination | listing, conservation assessment | "Nomination record" for the whole set at /research/threatened-species/. |
| The Australian act | the Environment Protection and Biodiversity Conservation Act (EPBC Act), then the EPBC Act | EPBC alone on first use | Expanded on first use per page. |
| The IUCN | the International Union for Conservation of Nature (IUCN), then IUCN | | Expanded on first use per page. |
| Upslope collapse pattern | the escalator to extinction | | Always with the PNAS link on first use. |
| Rainforest | rainforest, one word | rain forest | "Rain forest" survives only inside the verbatim 2022 possum paper title. |
| The CV document | the CV, download the CV as a PDF | resume, curriculum vitae | |

## Project pages (added in the _projects pass)

| Concept | Term | Not | Notes |
|---|---|---|---|
| Level 3 headings on project pages | Links, Architecture, The decision that was hard, What was measured, What did not work, Role, Stack | Overview, Approach, Results, Impact | One template for engineering and research pages. What did not work appears only where the record supports it. |
| The research closing section | What this taught me about evaluation | lessons learned | Research pages only, after Role, per POSITIONING move 7. |
| The recommendation buckets (Job Intelligence Engine) | best-now and stretch | best_now in prose | The underscore form is the code identifier and survives only in code and records. |
| Toolchain rows | tokens separated by " · " | prose sentences | Stack lines and model lists. The checker skips sentence checks on them. |
| Journal names as link labels | the venue string as cited | reworded labels | "Plos One" keeps the citation's casing. |

## Apps (added in the apps pass)

| Concept | Term | Not | Notes |
|---|---|---|---|
| The what-it-demonstrates line | opens with "It shows" | Demonstrates:, This demo shows | One line per app in `_data/apps.yml`, stating the engineering signal the pitch does not carry. |

## Publications (added in the publications pass)

| Concept | Term | Not | Notes |
|---|---|---|---|
| The block that opens a paper page | plain summary, the front matter `summary` field | lead, rewritten abstract | 120 words, Tier B, written fresh from the finding. The original abstract stays verbatim in the collapsed block. |
| The paper-to-project cross-link | Project page: | Read more, See also | Mirrors the project pages' "Paper page:" label. The link label is the project page's own title, resolved at build time. |
| Media lines on paper pages | verified headline · outlet | reworded or summarised headlines | Media titles are third-party records, verified against their sources and never rewritten. Outlet labels are site prose, so acronyms in them expand (James Cook University, not JCU). |
| The Chilean rodent | viscacha | vizcacha | Follows the paper's own spelling. "vizcacha" survives only in the settled page slug. |
| The Skyrail funder in prose | Skyrail Rainforest Foundation | Skyrail Foundation | The short form survives only in the verbatim grant lines. |

## Talks (added in the talks pass)

| Concept | Term | Not | Notes |
|---|---|---|---|
| The block that opens a talk page | plain summary, the front matter `summary` field | lead, rewritten abstract | 100 words, Tier B, written fresh from what the talk showed. Mirrors the publications row above. |
| The collapsed abstract on a talk page | Original abstract as submitted | Original abstract as published | Talks submit abstracts, journals publish them. The papers keep "as published". |
| The talk-to-paper cross-link | Paper page: | Read the paper, See also | Mirrors the publications pages' "Project page:" label. The link label is the paper page's own title, resolved at build time. |
| The earlier-appearance block | Also presented | Previously presented, Encore | One block per talk, carrying the absorbed appearance's verbatim title and venue. |
| Press and pulse | press for gradual trends, pulse for extreme events | chronic and acute | The thesis's own pairing, used in prose on the seminar page. |
| The bat species | spectacled flying fox, then flying foxes | Spectacled Flying Fox in prose | Capitalised only inside verbatim records and the talk title. |

## Teaching and the post (added in the teaching and posts pass)

| Concept | Term | Not | Notes |
|---|---|---|---|
| The two teaching entries | Courses, Mentoring | Teaching: James Cook University | Entry titles under the /research/ Teaching heading. Venue and location render from front matter. |
| The collapsed course record | Course list | Teaching history, Appointments | Mirrors the editorial service and certificates disclosures. |
| The student abstract block | Project abstract | Original abstract as submitted | A student's project abstract is a third-party record under brief 6.4. The "as submitted" label belongs to the owner's talks. |
| Mentoring in prose | I mentored | supervised, coached | Matches the entry title "Mentoring". |
| The publisher blurb block | Publisher's description | About the book, Blurb | Third-party record, byte-identical, attributed by its label. |

## Plain-language translations (added in the writing review)

Since DECISIONS 188 the standard is engaging plain English, and every
technical term gets a plain clause the first time it appears on a page,
with the precise term kept beside it. The same term gets the same clause
on every page. Once translated on a page, the precise term stands alone.

| Term | Plain clause used on first appearance |
|---|---|
| hierarchical (population) model | a model with 2 layers, one for the chance of seeing an animal and one for how many are there |
| imperfect detection | the chance of missing an animal that is there |
| credible interval | the Bayesian version of an error bar |
| posterior sampling / posterior | fitting that gives every quantity its credible interval |
| random effects | terms that let each site and year vary around the shared trend |
| generalised linear model | a model that relates counts to explanatory variables |
| N-mixture model | a model that separates true abundance from the chance of detecting an animal |
| spatial cross-validation | testing the model on places it never saw |
| explained deviance | the share of variation the model accounts for |
| link function | the mathematical bridge between suitability and count |
| beta-diversity metrics | metrics that compare the make-up of 2 communities |
| local extinction rate | the share of species unable to move |
| thermal resistance surface | a layer that scores how hard each stretch of terrain is to cross |
| partial altitudinal migration | seasonal uphill and downhill movement where only part of each population moves |
| mean reciprocal rank (MRR) | a retrieval score that rewards putting the right passage near the top |
| nDCG | a retrieval score that rewards a well-ordered list |
| vector store | a database that finds passages by meaning rather than by exact words |
| guardrail / judge model | a second model that checks every answer before a visitor sees it |
| canary corpus | probe questions replayed against the live system between releases |
| drift | the system's answers changing between releases |
| temperature 0 | the setting that removes the model's randomness |
| area under the curve (0.88 to 0.95) | tells a role that needs a skill from one that does not about 9 times in 10 |
| R² of 0.30 | the model explains roughly 30% of the variation |
| calibrated probability | a probability that means what it says |
| architecture decision record | a short document recording one design choice and the reasons behind it |
| statistical power (6 to 9%) | the chance of detecting an effect that is really there |
| detection floor | the smallest effect an instrument can tell apart from noise |
| bootstrap | redrawing the data at random, with replacement, and rescoring many times |
| permutation test | shuffling the data to destroy the signal and seeing what survives |
| QLoRA | a technique that shrinks a model to 4-bit precision and trains only small adapter layers |
| t-SNE | a projection that places similar items near each other |
| window function (SQL) | a query function that computes rankings and running totals across rows without collapsing them |
| sideboard (Magic) | the 15 spare cards swapped in between games |
| camp (deck engine) | one of the sub-groups a deck's players split into |

## Acronym policy

Expand every acronym on first use per page (section 6.2 rule 10). Exceptions,
treated as words and never expanded: AI, CV, PDF, XML, URL, and since the
_projects pass API, SQL, JSON, JSONL, GPU, DVD. Proper names that
look like acronyms and are never expanded: CONAF, CSIRO, ORCID, 7PH, R, and
since the _projects pass GPT (model family), JAGS, JIE (inside AI-JIE),
SBERT, SHAP, SNE (inside t-SNE), AA (the accessibility grade) and IELTS
(the test's proper name, on the /skills/ languages line). nDCG is
treated as a metric name: its 4-word expansion would break the noun-cluster
rule, so it stays unexpanded beside the expanded mean reciprocal rank (MRR).
Acronyms inside verbatim records (citations, course titles, the nomination
list, award venues) are exempt, and so are media titles, which are
third-party records. ABC inside "ABC News" is the broadcaster's proper name
and is never expanded. `scripts/prose_check.py` enforces this with the same
allowlist and an expansion dictionary (MRR and MLB joined it in the
_projects pass, MCP with the /skills/ page: the Model Context Protocol
expands on first use like the EPBC Act).

## Mechanics

- No em dashes and no en dashes anywhere. En dashes survive only in numeric
  ranges inside verbatim citations.
- No semicolons in body copy.
- Date ranges in prose and timelines spell "to": "2020 to 2024".
- Numerals for all numbers in prose (section 6.2 rule 11). Words like
  "three decades" are ranges of narrative time, not data, and may stay words.
- Verbatim record regions in source files sit between `<!-- record -->` and
  `<!-- /record -->` markers. `scripts/prose_check.py` skips them.
