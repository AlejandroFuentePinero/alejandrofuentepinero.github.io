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

## Acronym policy

Expand every acronym on first use per page (section 6.2 rule 10). Exceptions,
treated as words and never expanded: AI, CV, PDF, XML, URL. Proper names that
look like acronyms and are never expanded: CONAF, CSIRO, ORCID, 7PH, R.
Acronyms inside verbatim records (citations, course titles, the nomination
list, award venues) are exempt. `scripts/prose_check.py` enforces this with
the same allowlist and an expansion dictionary.

## Mechanics

- No em dashes and no en dashes anywhere. En dashes survive only in numeric
  ranges inside verbatim citations.
- No semicolons in body copy.
- Date ranges in prose and timelines spell "to": "2020 to 2024".
- Numerals for all numbers in prose (section 6.2 rule 11). Words like
  "three decades" are ranges of narrative time, not data, and may stay words.
- Verbatim record regions in source files sit between `<!-- record -->` and
  `<!-- /record -->` markers. `scripts/prose_check.py` skips them.
