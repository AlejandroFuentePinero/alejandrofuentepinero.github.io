# POSITIONING.md: Phase 1, positioning

Produced on branch `refurb/phase-1-positioning`, 2026-08-07. Inputs: REFURB_BRIEF.md section 2, AUDIT.md, and the Gate 0 outcomes. This file and CONTENT_MAP.md are the only Phase 1 deliverables. No code or content changed.

Revised the same day after the first Gate 1 round: warmer thesis options, anchor year 2016, skills row cut to demonstrated mastery.

---

## 1. The thesis

### 1.1 What the hero must do

The thesis is 2 or 3 sentences under the name and the role line. The budget is 60 words on the first screen, role line included (brief 4.1). It must survive three readers at once: a recruiter deciding in 40 seconds whether to keep reading, a technical peer testing for substance, and an academic checking that the research is real. All options are written to Tier B rules: sentences of 25 words or fewer, active voice, no em dashes.

**The voice, reset at Gate 1.** The first three options (A to C, in the PR history) were rejected as too corporate. This is a personal site; the hero should sound like Alejandro talking, warm and plain, not a positioning statement. The three options below all open as a greeting and keep the field story in first person. Warmth and rigour are not in tension; the copy aims for both.

**A note on honest claims, settled at Gate 1.** Brief 2.1 says the model output "determined whether a species received legal protection". Strictly, the models fed formal nominations: 15 nomination documents under the EPBC Act and to the IUCN through BirdLife International, with the 2022 possum forecast paper behind the lemuroid ringtail possum nomination. Regulators decide; the models made the case. Every option below therefore says "helped protect" or "helped decide", never "determined". The record is strong enough not to need inflation, and precision here is on brand.

**A note on the year count.** No option hard-codes a running year count ("I spent years", never "I spent N years"). The stats band directly under the hero carries the computed number (section 3.2), so the hero and the band can never disagree and nothing goes stale.

### 1.2 Option D: the care up front

> Hi, I'm Alejandro. I spent years in rainforests counting possums and birds, then building the models that helped protect them. That work taught me to be honest about uncertainty. Now I build AI systems, and I bring the same care: if I can't measure that it works, I don't ship it.

52 words, 4 sentences, longest sentence 22 words.

**The bet.** Maximum warmth. The story opens, the lesson follows, the engineering promise closes. The final sentence is the quotable one.

**Audience test.** The peer gets a shipping standard they can hold him to. The academic gets fieldwork that was counted and modelled, not name-dropped. The recruiter, though, does not reach "AI systems" until sentence four, about 35 words in.

**Risk.** On a skim, the possums arrive before the job. The role line above the hero has to carry "AI engineer" alone, and it can.

### 1.3 Option E: the friendly handshake

> Hi, I'm Alejandro. I build AI systems: retrieval pipelines, agents, and the evaluation that proves they work. I learned that discipline in the rainforest, forecasting wildlife populations where a wrong number could cost a species its protection. I like hard data, honest error bars, and tools people actually use.

50 words, 4 sentences, longest sentence 20 words.

**The bet.** The friendly open and the recruiter's answer in the same breath. The story sits in the middle as evidence, and the close is personality doing keyword work.

**Audience test.** The recruiter has the role by word 8. The peer gets a testable claim ("evaluation that proves they work") plus a taste statement they will recognise as one of their own. The academic gets the forecasting record with its stakes intact.

**Risk.** The least story-forward of the three. If the goal is maximum warmth, D beats it.

### 1.4 Option F: the rainforest office

> Hi, I'm Alejandro. For years my office was a rainforest. I tracked possums and birds, and my models helped decide which species got protected, so I learned to defend every number. I build AI systems now, and the habit stays: quantify the uncertainty, measure everything, say what you don't know.

51 words, 4 sentences, longest sentence 21 words.

**The bet.** The origin story with a smile. "For years my office was a rainforest" is the most charming line in any of the six options, and it earns the discipline claim that follows.

**Audience test.** The peer and the academic get a memorable, credible open. The recruiter waits until sentence four for "AI systems", about 33 words in.

**Risk.** Same as D: the skimmer meets the rainforest before the role. The charm is the mitigation; it buys a second sentence of attention.

### 1.5 The decision: Option E, settled at Gate 1

E won because it is warm and still answers the recruiter immediately, and the 40-second reader is the one the current site fails hardest (AUDIT.md section 8). The wording is locked for structure now and gets one polish pass when first seen rendered, in Phase 4 or 5.

Two salvage moves, logged. D's closing line ("if I can't measure that it works, I don't ship it") becomes the opening line of the `/projects/` index or the `/work/` intro. F's rainforest-office line goes to the `/work/` timeline intro, where the reader has opted into the story.

---

## 2. The role descriptor

One line under 12 words (brief 4.1). Three options, revised to match the warmer voice:

| # | Descriptor | Words | Character |
|---|---|---|---|
| 1 | AI engineer. I build systems and measure whether they work. | 10 | Plain and falsifiable; safe with any thesis |
| 2 | AI engineer, raised on rainforest data and honest error bars. | 10 | Warm; carries the origin in passing |
| 3 | AI engineer: retrieval, agents, evaluation, uncertainty. | 6 | Keyword-dense |

Settled at Gate 1 with thesis E: option 2. E's first sentence already makes the plain claim, so the role line can afford personality. Option 3 was redundant either way: the skills row directly below already does the keyword work. Like the hero, the wording gets one polish pass when first rendered.

---

## 3. The stats band

### 3.1 The final five

Five stats, ordered to read as a sentence: experience, then what he built, then proof it runs, then the research record, then its traction. Labels are 4 words or fewer.

| # | Label | Value today | Type | Source |
|---|---|---|---|---|
| 1 | Years working with uncertainty | 10 | Declared anchor, computed render | `start_year: 2016` in `_data/stats.yml`; rendered as current year minus start year |
| 2 | Projects | 18 now, 16 after the Gate 1 merges | Derived | `site.projects \| size` |
| 3 | Live apps | 4 | Derived | count of `_data/apps.yml` entries with `status: live` |
| 4 | Peer-reviewed papers | 12 | Derived | `site.publications \| size` |
| 5 | Citations | 193 | Declared | Google Scholar profile 7CKVdZwAAAAJ, as of 2026-08-07 |

Rejected candidates, with reasons. Talks (15 now, 12 after consolidation): worthy, but a six-stat band starts to read as a dashboard; bench option if one of the five falls at the gate. h-index (7): a niche academic metric that invites judgment rather than credibility. Book chapters (14): impressive but confusing next to "12 papers" without context; it lives in `/research/`. Journals published in (10): trivia at band level. Media reach (70 national stories): belongs on the possum pages where it has context, not in a summary row.

### 3.2 The anchor year: 2016, settled at Gate 1

AUDIT.md 9.8 listed the options: 2016 (head biologist, CONAF), 2019 (research assistant, JCU), 2020 (PhD monitoring work). Gate 1 chose **2016**, the first professional data role. The band computes 10 in 2026 and can never go stale.

One label consequence, for honesty. In 2016 and 2017 the work was running field programs and population monitoring at Puyehue National Park; the full-time hierarchical modelling came later. So the label reads "Years working with uncertainty", not "Years modelling under uncertainty". The wider claim is watertight from 2016; the narrower one is not, and this band does not stretch. The hero copy carries no year count either way (section 1.1), so the choice changes one field in one data file.

### 3.3 `_data/stats.yml` schema

The band is data-driven: the include iterates this list in order, so adding, removing or reordering stats is a data change, not a template change. Derived entries carry no value; the include computes them. Declared entries are the only hand-maintained numbers on the site.

```yaml
# _data/stats.yml
# The stats band, in display order.
# type: derived        -> include computes site.<collection> | size
# type: derived_data   -> include counts entries of _data/<data>.yml matching `where`
# type: years_since    -> include renders current year minus start_year
# type: declared       -> include renders `value`; must carry source and as_of
band:
  - id: years_uncertainty
    label: "Years working with uncertainty"
    type: years_since
    start_year: 2016
    source: "First professional data role: head biologist, CONAF, Puyehue National Park"
    as_of: 2026-08-07

  - id: projects
    label: "Projects"
    type: derived
    collection: projects

  - id: live_apps
    label: "Live apps"
    type: derived_data
    data: apps
    where:
      status: live

  - id: publications
    label: "Peer-reviewed papers"
    type: derived
    collection: publications

  - id: citations
    label: "Citations"
    type: declared
    value: 193
    source: "Google Scholar profile 7CKVdZwAAAAJ"
    as_of: 2026-08-07
```

### 3.4 Render rules

- No literal digit ever appears in the stats include or any template; `scripts/prose_check.py` greps for digits there and fails the build if it finds any (brief 4.2). Digits enter only through Liquid computation or a `value:` field in this file.
- Declared stats render their `as_of` in muted text (for example "as of Aug 2026"), formatted by Liquid from the date field.
- Presentation per brief 4.2: number in the display serif at `--step-3` with tabular figures, label beneath at `--step--1` in `--ink-muted`, hairline rules between, no icons, no cards, no count-up animation.
- Maintenance: the two declared entries (`years_uncertainty` never changes; `citations` needs a dated refresh) are the only manual numbers on the site. MAINTENANCE.md documents the refresh in Phase 7.

---

## 4. The skills row

### 4.1 The chips

Ten chips in two visually continuous groups. The rule, tightened at Gate 1: a chip claims mastery demonstrated by a shipped system or a peer-reviewed paper. Certificates and course-scaffolded labs do not qualify, however recent. Each chip names its evidence.

**Builds with** (5):

| Chip | Evidence |
|---|---|
| Python | Digital twin, AI-JIE, 7PH Graph, Job Intelligence Engine: shipped systems |
| RAG pipelines | The digital twin: a production retrieval system with a 149-question evaluation set |
| Knowledge graphs | 7PH Graph: a live Neo4j and Cypher store with per-value provenance |
| LLM-as-judge evaluation | The twin's guardrail model running in production; the AI-JIE judge framework |
| SQL | The MLB analytics project: schema design, reusable views, window functions |

**Grounded in** (5):

| Chip | Evidence |
|---|---|
| Bayesian inference | 12 papers |
| Hierarchical models | The possum and bird population models behind the protection nominations |
| Uncertainty quantification | Published viability forecasts with propagated uncertainty |
| Evaluation design | The twin's evaluation set and canary corpus; retrieval metrics; peer review survived 12 times |
| R | The entire research record and the Shiny app |

### 4.2 What was cut, and one logged assumption

Cut at Gate 1 under the mastery rule: "LLM agents" and "QLoRA fine-tuning". Their main evidence was the LLM Engineering Lab, a course-scaffolded lab. They return the day a shipped system demonstrates them.

Already excluded from the brief's candidate list: GCP, Vertex AI and BigQuery (nothing in the record supports them) and AWS (foundational familiarity is not mastery). If real cloud work exists off-site, name the project and it can join the row.

Logged assumption: SQL stays on the strength of the MLB analytics project, which is self-directed applied work on a real database rather than a guided course. If that later reads as lab-grade evidence, the row drops to 9 chips.

### 4.3 `_data/skills.yml` schema

Deliberately minimal: labels only, no URLs, no proficiency levels, nothing speculative. The include renders groups in order as one continuous row with a group prefix.

```yaml
# _data/skills.yml
# The home page skills row. Two groups, rendered as one chip row.
# Rule: a chip claims working competence demonstrated on this site.
groups:
  - name: "Builds with"
    chips:
      - Python
      - RAG pipelines
      - Knowledge graphs
      - LLM-as-judge evaluation
      - SQL
  - name: "Grounded in"
    chips:
      - Bayesian inference
      - Hierarchical models
      - Uncertainty quantification
      - Evaluation design
      - R
```

---

## 5. The unification narrative: the copy moves

The moves that make one method visible across both halves of the record. Each is a concrete edit with a source and a destination; Phases 4 and 5 execute them.

1. **The hero replaces the two-track welcome.** "Hi, I'm Alejandro, AI Engineer & Data Scientist" plus the puma-and-jaguar paragraph go. The thesis (section 1) opens the site. The field story compresses to one clause ("my numbers fed legal protection decisions") and its long form moves to the `/work/` introduction, where a reader who wants the story has asked for it.
2. **The "What I build" bullet list is deleted.** Its keyword load moves to the skills row and to stack chips on project cards, per brief 4.1. No replacement prose.
3. **Research projects lose the apology.** The projects index currently frames them as "peer-reviewed modelling work presented in a DS case-study format", a costume. New framing: they are projects, full stop, in the same card template with the same stack chips (R, Stan-family tools, GLMs) and result-first excerpts. The word "research" survives as a filter value, not as a disclaimer.
4. **Publication index entries state findings, not topics.** "Can habitat suitability derived from SDMs predict species abundance?" becomes a declarative result. The worked example and standard live in CONTENT_MAP.md section 7.
5. **One timeline.** `cv.md` and the education page dissolve into `/work/`: CONAF 2016, Kaa-Iya 2017, JCU research assistant 2019, PhD 2020 to 2024, postdoc and AI work 2024 onward, one unbroken line with no era boundary. Certificates demote to a collapsed block. The academic CV's list duplications (publications, talks, grants rendered inline) become links.
6. **The stats band mixes the records in one row.** Papers and citations sit beside projects and live apps with identical treatment. The band is the unification argument in five numbers.
7. **Each research project page ends with the transfer.** One closing line under a consistent heading (working title "What this taught me about evaluation") naming the method that now appears in the engineering work: detection versus process separation, forecast validation, uncertainty propagation. This is the level 3 thread stitching the two halves.
8. **Each engineering project page opens with a measured result**, so the engineering pages read like the abstracts of the research pages: claim, method, evidence. Same shape both directions.
9. **The skills page's "What I bring from research" section** condenses to two sentences inside the `/work/` introduction; the page retires. The best sentence in it ("if it can't be evaluated, it can't be trusted") is thesis material; keep it somewhere visible.
10. **The digital twin is framed as evidence, not novelty** (section 6): the one line of context above the embed names the guardrail, making the toy an exhibit of the thesis.

---

## 6. The digital twin on the home page

**Placement.** Position 5 of the home page, after selected work, before the contact call to action, per brief 4.1. The twin is an experience, not the CTA. It keeps a full entry in `/apps/` (link treatment, not a second embed) and its project page keeps the depth.

**Framing.** A styled frame with a heading, one line of context, and a visible full-screen link:

> **Ask the digital twin**
> A retrieval-augmented agent that answers questions about my work. A second model reviews every answer before you see it.

The context line is the thesis in miniature: the demo itself ships with a guardrail. The current apology ("Doesn't load?") goes; the fallback becomes a screenshot plus the link to the Hugging Face Space, shown only when the frame fails (brief 4.4).

**Embed spec** (implemented in Phases 3 and 4):

- Height 720px on desktop, capped at 85vh on small screens. The current 1100px iframe is most of two screens and is the main reason the recruiter's 40 seconds die inside a chatbot (AUDIT.md section 8). Space is reserved explicitly so the embed never shifts layout.
- `loading="lazy"` plus an IntersectionObserver; the frame costs nothing until scrolled near.
- Visible "Open full screen" link to the Space at all times, not only on failure.
- Accessible iframe title, per the Phase 6 checklist.

**Constraint.** The twin itself is in observe mode: no changes to the Space or its repo. Every change above is site-side (frame, height, lazy loading, fallback), which is fully within that constraint.

---

## 7. Gate 1 decision log

Settled: thesis E with role descriptor 2; the honesty standard for protection claims; the five stats and their order; the 2016 anchor with the label change in 3.2; the mastery rule and the 10 chips; and, in CONTENT_MAP.md, the project demotions, the four talk pages, the four home cards and the worked summary. **No open decisions remain in this file.**

Assumptions proceeding as logged, to test once the site is visible:

1. The SQL chip stays (4.2).
2. Twin embed at 720px with the "Ask the digital twin" framing, all site-side.
3. The CONTENT_MAP mechanical layer (slugs, redirect targets, teaching inline, blog permalink, threatened species home) as written.
4. Hero and role-line wording is locked for structure and gets one polish pass when first rendered, in Phase 4 or 5.
