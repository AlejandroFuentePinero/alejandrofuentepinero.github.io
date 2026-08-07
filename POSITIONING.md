# POSITIONING.md: Phase 1, positioning

Produced on branch `refurb/phase-1-positioning`, 2026-08-07. Inputs: REFURB_BRIEF.md section 2, AUDIT.md, and the Gate 0 outcomes. This file and CONTENT_MAP.md are the only Phase 1 deliverables. No code or content changed.

---

## 1. The thesis

### 1.1 What the hero must do

The thesis is 2 or 3 sentences under the name and the role line. The budget is 60 words on the first screen, role line included (brief 4.1). It must survive three readers at once: a recruiter deciding in 40 seconds whether to keep reading, a technical peer testing for substance, and an academic checking that the research is real. The three options below make three genuinely different bets, and each could carry the site. All are written to Tier B rules: sentences of 25 words or fewer, active voice, no em dashes.

**A note on honest claims, before the options.** Brief 2.1 says the model output "determined whether a species received legal protection". Strictly, the models fed formal nominations: 15 nomination documents under the EPBC Act and to the IUCN through BirdLife International, with the 2022 possum forecast paper behind the lemuroid ringtail possum nomination. Regulators decide; the models made the case. Every option below therefore says "fed" or "helped decide", never "determined". The record is strong enough not to need inflation, and precision here is on brand.

**A note on the year count.** None of the recommended copy hard-codes a running year count. The stats band directly under the hero carries the computed number (section 3.2), so the hero and the band can never disagree and nothing goes stale. Option B is the exception: it uses "six years" for the closed 2019 to 2024 period, which is a historical fact and cannot rot.

### 1.2 Option A: the builder who measures

> I build AI systems and measure whether they work. The discipline comes from years of Bayesian population modelling, where my numbers fed legal protection decisions for threatened species. That work demanded quantified uncertainty and evaluation that survives scrutiny. I apply the same standard to retrieval systems, agents and language model pipelines.

51 words, 4 sentences, longest sentence 19 words.

**The bet.** Identity first. He is a builder; the evaluation discipline is the edge, not the identity. The present tense opens and closes the copy, and the past sits in the middle as evidence.

**Audience test.** The recruiter gets role and differentiator in sentence one, nine words in. The peer gets a falsifiable claim ("measure whether they work") that the stats band, the apps and the project pages must then back. The academic gets the research named as the source of the method, not as a former life.

**Risk.** "I build X and measure it" is becoming a common claim in 2026. The defence is that sentence two is not a claim, it is a record, and almost nobody else has it.

### 1.3 Option B: consequences first

> For six years my models helped decide which species were nominated for legal protection. Wrong answers had real consequences, so I learned to quantify uncertainty and defend every number in review. I now build AI systems to the same standard: retrieval, agents and fine-tuned models, with nothing shipped unmeasured.

49 words, 3 sentences, longest sentence 18 words.

**The bet.** Narrative first. Open on the stakes, because stakes are the one thing no other AI engineer's hero can copy. The most memorable of the three.

**Audience test.** The peer and the academic get the strongest possible open. The recruiter, though, does not learn what he does today until sentence three, roughly 30 words in. Their 40 seconds start with a puzzle: is this a biologist?

**Risk.** Leading with the past is structurally the two-CVs problem this rebuild exists to fix. Handled well it reads as an origin story; skimmed, it reads as a career changer. The skim is the recruiter's default mode.

### 1.4 Option C: uncertainty as the product

> I build AI systems that know what they do not know. Retrieval pipelines, agents and fine-tuned models ship with evaluation frameworks and honest error bars. The method comes from Bayesian ecology, where quantified uncertainty helped decide whether a species received legal protection.

42 words, 3 sentences, longest sentence 17 words.

**The bet.** Capability first. Calibration, guardrails and evaluation are concrete, scarce and increasingly what teams hire for. The sharpest technical hook of the three.

**Audience test.** The peer gets the best first sentence on this page. The academic reads "quantified uncertainty" as fluent statistics. The recruiter gets a memorable line but a narrower one: it frames a reliability specialist more than a builder.

**Risk.** It positions the edge as the job. The record (three live apps, a knowledge graph, an end-to-end recommender) shows a builder whose systems are evaluated, not an evaluator who sometimes builds. Choosing C narrows perceived role fit to evaluation-heavy positions.

### 1.5 Recommendation: Option A

Three reasons.

1. It answers the recruiter's only question, "what do you do", in nine words, then differentiates. B delays that answer; C narrows it.
2. It matches the record. The site's strongest evidence is built systems with evaluation attached: the twin's guardrail model, 7PH Graph's statistical guards, the AI-JIE judge framework. A builder thesis lets each of those pages confirm the hero.
3. It degrades gracefully. Sentence one alone works as a role line. Sentences two and three are Option B's story. Sentence four carries Option C's keywords. A absorbs the best of both losers.

Honest counterpoints: B is the most memorable and the best spoken aloud; if the site's main job were talks and profiles, B wins. C is the strongest differentiator for evaluation and reliability roles; if the target market shifts that way, revisit. For a unified portfolio serving all three audiences at once, A.

---

## 2. The role descriptor

One line under 12 words (brief 4.1). Three options:

| # | Descriptor | Words | Character |
|---|---|---|---|
| 1 | AI engineer. I build systems and measure whether they work. | 10 | Mirrors thesis A; plain and falsifiable |
| 2 | AI engineer, formed by six years of consequence-bearing Bayesian modelling. | 10 | Carries the origin; pairs with thesis B |
| 3 | AI engineer: retrieval, agents, fine-tuning, evaluation. | 6 | Keyword-dense; pairs with thesis C |

Recommendation: option 1 with thesis A. One caution against option 3: as a standalone line it does recruiter-keyword work, but the skills row directly below the hero already does that job, so spending the role line on keywords is redundant.

---

## 3. The stats band

### 3.1 The final five

Five stats, ordered to read as a sentence: experience, then what he built, then proof it runs, then the research record, then its traction. Labels are 4 words or fewer.

| # | Label | Value today | Type | Source |
|---|---|---|---|---|
| 1 | Years modelling under uncertainty | 7 | Declared anchor, computed render | `start_year: 2019` in `_data/stats.yml`; rendered as current year minus start year |
| 2 | Projects | 18 now, 16 after the Gate 1 merges | Derived | `site.projects \| size` |
| 3 | Live apps | 3 | Derived | count of `_data/apps.yml` entries with `status: live` |
| 4 | Peer-reviewed papers | 12 | Derived | `site.publications \| size` |
| 5 | Citations | 193 | Declared | Google Scholar profile 7CKVdZwAAAAJ, as of 2026-08-07 |

Rejected candidates, with reasons. Talks (15 now, 12 after consolidation): worthy, but a six-stat band starts to read as a dashboard; bench option if one of the five falls at the gate. h-index (7): a niche academic metric that invites judgment rather than credibility. Book chapters (14): impressive but confusing next to "12 papers" without context; it lives in `/research/`. Journals published in (10): trivia at band level. Media reach (70 national stories): belongs on the possum pages where it has context, not in a summary row.

### 3.2 The anchor year decision

The brief flags this and AUDIT.md 9.8 lists the options: 2016 (head biologist, CONAF), 2019 (research assistant, JCU), 2020 (PhD monitoring work).

**Recommendation: 2019.** That is when continuous quantitative work on the Wet Tropics monitoring program began, and it survives scrutiny: any reader of the CV sees an unbroken line from 2019 research assistant through PhD to postdoc. Anchoring at 2016 yields a bigger number (10) but invites the challenge "were you building models as a park biologist?", and the thesis claims consequence-bearing modelling specifically. Under-claiming is the brand.

Consequences of the 2019 anchor: the band computes 7 in 2026, and the brief's "6 years" phrasing in section 2.1 is already stale, which is exactly why no year count is typed anywhere. The hero copy in options A and C carries no count. Option B's "six years" refers to the closed 2019 to 2024 period and stays true forever.

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
    label: "Years modelling under uncertainty"
    type: years_since
    start_year: 2019
    source: "Start of quantitative work on the JCU Wet Tropics monitoring program"
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

Twelve chips in two visually continuous groups. Rule for inclusion: a chip claims working competence demonstrated by work visible on this site. Each chip below names its evidence.

**Builds with** (7):

| Chip | Evidence |
|---|---|
| Python | Every engineering project |
| RAG pipelines | Digital twin; LLM Engineering Lab |
| LLM agents | LLM Engineering Lab multi-agent systems; twin tool use |
| QLoRA fine-tuning | LLM Engineering Lab (Llama 3.2, 4-bit) |
| Knowledge graphs | 7PH Graph (Neo4j, Cypher, GraphRAG) |
| LLM-as-judge evaluation | AI-JIE evaluation framework; twin guardrail and 149-question eval set |
| SQL | MLB analytics project; JIE pipeline (PostgreSQL) |

**Grounded in** (5):

| Chip | Evidence |
|---|---|
| Bayesian inference | 9 research projects, 12 papers |
| Hierarchical models | Possum and bird population models |
| Uncertainty quantification | Viability forecasts behind protection nominations |
| Evaluation design | 149-question eval set, canary corpus, retrieval metrics |
| R | Shiny app; the entire research record |

### 4.2 Corrections to the brief's candidate list

Brief 4.3 suggests GCP, Vertex AI and BigQuery. Nothing in the repo supports them: the skills page documents AWS at a foundational level and no GCP work at all. Under the no-fabricated-claims rule those three chips are out, and AWS stays out too because foundational familiarity is not working competence. If real GCP or cloud work exists off-site, name the project and it can join the row; otherwise the row must not outrun the record.

One pairing to defend at the gate: "LLM-as-judge evaluation" (a technique he builds with) and "Evaluation design" (the discipline he brings) both appear. They are different claims and both earn their place, but if the gate wants 11 chips, drop "LLM-as-judge evaluation"; the AI-JIE and twin cards carry that keyword anyway.

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
      - LLM agents
      - QLoRA fine-tuning
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

## 7. Decisions this file asks Gate 1 to settle

1. Thesis: A, B or C (recommendation: A).
2. Role descriptor: 1, 2 or 3 (recommendation: 1).
3. The "helped decide / fed nominations" honesty standard for protection claims, replacing the brief's "determined".
4. Stats band: the five stats and their order in 3.1.
5. Anchor year 2019 for the experience stat.
6. Skills row: the 12 chips in 4.1, including the exclusion of GCP, Vertex AI, BigQuery and AWS.
7. Twin embed at 720px with the "Ask the digital twin" framing.
