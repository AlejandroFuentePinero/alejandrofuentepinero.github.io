# MAINTENANCE.md: how to keep this site alive

This is the operating manual for routine changes after the 2026
refurbishment. It assumes you have read nothing else. When it cites a
numbered decision (for example DECISIONS 125), the reasoning lives in
`DECISIONS.md`; you do not need it to follow the steps.

The site is Jekyll on GitHub Pages, no build step beyond Jekyll, no
framework, one vanilla JS file (`assets/js/site.js`). Ruby is pinned by
`.ruby-version`. Build and preview locally with:

```
bundle install          # once per machine
bundle exec jekyll serve
```

`bundle exec jekyll build` must stay warning-free. `python3
scripts/prose_check.py` must print `clean` before any commit that
touches prose. Both run in CI on every push and pull request
(`.github/workflows/prose-check.yml`).

## The four hard rules

1. **Never break the record.** Citation strings, original abstracts,
   titles of degrees, courses, grants and awards, co-author names,
   dates and numeric results are never edited. See "Record markers"
   below.
2. **Never break URLs.** If a page moves, the new page carries a
   `redirect_from:` entry for every old URL and `MIGRATIONS.md` gains a
   line. Nothing may 404.
3. **No hand-typed numbers in the stats band.** Counts derive from the
   collections at build time; the only manual numbers live in
   `_data/stats.yml` with a source and date.
4. **No new frameworks, no second accent colour, no entrance
   animations.** Design tokens live in `_sass/_tokens.scss`, the only
   file that defines hex colours.

## Branch and deploy model

The live site serves from `main`; anything merged there deploys within
minutes. Never force push, never rewrite history on `main`. Small
commits, one concern per commit. No AI attribution and no em dashes in
commits, PRs or any written output.

**The checkpoint merge model, while `refurb/main` exists.** Work
happens on a topic branch cut from `refurb/main`; its PR targets
`refurb/main`, never `main`. The owner merges `refurb/main` into
`main` at checkpoints after review, and after any `main` change
(hotfix, checkpoint), `main` merges back into `refurb/main` promptly
so the branches never diverge silently. Local `bundle exec jekyll
serve` is the preview; there is no hosted preview.

**After `refurb/main` retires** (the owner deletes it once the final
phase has soaked), the model collapses to: branch from `main`, PR into
`main`, review the local build, merge.

## Adding a project

1. Create `_projects/<slug>.md`. The slug becomes the URL
   `/projects/<slug>/`. Copy the front matter shape from an existing
   file, for example `_projects/7ph-graph.md`:

   ```yaml
   ---
   title: "Result-oriented name"
   excerpt: "Result-first card text, 25 words or fewer."
   date: 2026-08-08          # drives newest-first ordering
   type: engineering         # engineering | research | lab (the filter)
   stack:                    # 2 to 5 chips, names verbatim
     - Python
   ---
   ```

2. The body opens with the outcome in one sentence, then a summary of
   at most 120 visible words before the first heading. Then the level 3
   headings the other projects use: Links, Architecture, the decision
   that was hard, what was measured, what did not work (only if the
   record supports it), Role.
3. Add the file to the `FILES` table in `scripts/prose_check.py` as
   `"_projects/<slug>.md": ("A", None),`. Tier A means full plain-verb
   discipline; `None` means no total budget, but the 120-words-before-
   first-heading and 25-word-excerpt checks still apply.
4. Build, run prose_check, fix what it flags.

The projects index and the stats band count the new project
automatically. If the project should appear on the home page, that is a
positioning decision, not a routine addition.

## Adding a publication

1. Create `_publications/<citekey>.md` with this front matter shape
   (copy `_publications/delafuente_williams_2022_possums_ddi.md`):

   ```yaml
   ---
   title: "Exact published title"
   collection: publications
   permalink: /research/<slug>-<year>/
   excerpt: 'The finding, stated as a finding, 25 words or fewer.
             Not a topic, not a question.'
   summary: |
     The plain-language summary, 120 words or fewer, written fresh
     from the finding, not paraphrased from the abstract. What was
     found, how, why it matters. This is the page opener.
   date: 2026-08-08
   venue: 'Journal Name'
   paperurl: 'https://doi.org/...'   # the publisher link
   citation: 'Verbatim citation string. Never edited afterwards.'
   pdf: '/files/<file>.pdf'          # optional, if a local PDF exists
   project: /projects/<slug>/        # optional cross-link
   media:                            # optional, verified headlines only
     - title: 'Exact headline'
       outlet: "Outlet name"
       url: "https://..."
   ---
   ```

2. The body holds nothing but the original abstract, verbatim, inside
   record markers:

   ```
   <!-- record -->
   ...abstract exactly as published...
   <!-- /record -->
   ```

   The layout renders it collapsed under "Original abstract as
   published". prose_check fails the file if any prose sits outside the
   markers.
3. Add the file to `FILES` in `scripts/prose_check.py` as
   `"_publications/<citekey>.md": ("B", 120),`.
4. Build, run prose_check. The paper count on the stats band and the
   /research/ index update themselves.

Talks follow the same mechanics (a `summary`, a collapsed abstract
labelled "as submitted", a 20-word excerpt, budget 100); copy
`_talks/IBRC_2025.md`.

## Adding an app

1. Append an entry to `_data/apps.yml`. The fields, all consumed by
   /apps/ and checked by prose_check:

   ```yaml
   - id: my-app
     name: "My App"
     status: live            # live | archived; live feeds the stats band
     treatment: link         # embed | link | archive
     url: "https://..."
     source: "https://github.com/..."   # empty string hides the link
     project: /projects/<slug>/
     pitch: "25 words or fewer, Tier A."
     demonstrates: "One line opening with: It shows ..."
     note: ""                # operational note, may be empty
     screenshot: /images/apps/my-app.png
     screenshot_width: 1280
     screenshot_height: 800
   ```

2. Commit the screenshot at the stated path and convert it to webp
   (see "webp conversion" below; add the file to the list in
   `scripts/convert_images.sh` first).
3. Build and run prose_check. The "Live apps" stat counts entries with
   `status: live` automatically. No per-file prose_check change is
   needed: the checker reads `_data/apps.yml` itself.

## Updating _data/stats.yml

The only two numbers that ever need a manual refresh are the Scholar
pair on the `citations` entry: `value` and `as_of`.

```yaml
  - id: citations
    ...
    value: 193
    as_of: 2026-08-07
```

Read the current count from the Google Scholar profile named in
`source`, set `value`, set `as_of` to today. Everything else on the
band is computed: papers, projects and live apps from the collections
and data files, years from `start_year`. Never type a count into a
template; prose_check fails the build if a digit appears in
`_includes/stats-band.html`.

## Prose rules, short form

Full standard: REFURB_BRIEF.md section 6. The enforced core:

- One idea per sentence. At most 20 words per sentence in Tier A
  files, 25 in Tier B. At most 4 sentences per paragraph.
- Active voice. Numerals for numbers. Expand every acronym on first
  use per page (the allowlist lives in `scripts/prose_check.py`).
- **No em or en dashes anywhere in prose.** En dashes survive only
  inside citation strings. No semicolons in body copy. No exclamation
  marks.
- Every page and summary opens with the result, not the method.
- Banned words: delve, leverage (as a verb), seamless, robust,
  cutting-edge, state-of-the-art, passionate, journey, landscape
  (unless literal), realm, tapestry, navigate (unless literal),
  unlock, empower, harness, elevate, "in today's world", "it's worth
  noting", "at the end of the day", "not just X but Y", "isn't just
  X, it's Y", "dive into", "under the hood".

Density budget (REFURB_BRIEF 2.4), the ceilings prose_check enforces:

| Surface | Ceiling |
|---|---|
| Home page, total prose | 450 words |
| Project or app card (excerpt, pitch) | 25 words |
| Publication index entry (excerpt) | 25 words |
| Publication plain summary | 120 words |
| Talk excerpt / talk summary | 20 / 100 words |
| Project page, before first heading | 120 words |
| Any paragraph | 4 sentences |

Content that does not fit moves down a level. It does not get
squeezed.

## Record markers

Verbatim third-party or historical text (abstracts, the publisher's
book description, the nomination list) sits between HTML comments:

```
<!-- record -->
...never edited, never reworded, byte for byte...
<!-- /record -->
```

prose_check skips everything inside the markers and excludes it from
word budgets. If text inside a record looks wrong, do not fix it in
place: verify against the published source first, and log the call in
DECISIONS.md (see DECISIONS 92 and 105 for the two worked examples of
a verified repair).

## Extending prose_check

`scripts/prose_check.py` checks exactly what its tables name. When
content is added, extend them:

- New page, project, publication or talk file: add a row to `FILES`
  with its tier ("A" or "B") and word budget (`None` for unbudgeted
  level 3 depth).
- New teaching entry: append the path to `TEACHING_FILES` (the 120-word
  budget is shared across the section).
- New app: nothing to do, the checker reads `_data/apps.yml` whole.
- New acronym: add it to the allowlist or the expansion dictionary
  near the top of the script, and record the call in TERMINOLOGY.md.

The checker's habit, worth keeping: when you add a check or a file,
seed a deliberate violation once and watch it fail, then land clean.

## Regenerating scripted assets

All three scripts run locally from the repo root and their output is
committed, because GitHub Pages has no build step.

**CV PDF**: retired. `files/alejandro-de-la-fuente-cv.pdf` is a frozen
one-page pointer to /work/ kept only so old external links never 404
(DECISIONS 180). It is never regenerated. The print stylesheet still
serves anyone who prints /work/ from the browser.

**og:image** (`images/og-image.png`): the 1200x630 social card, built
from the tokens file and the site's own fonts (DECISIONS 120). Rerun
only if the name, role line, palette or fonts change:

```
python3 scripts/generate_og_image.py
```

**webp conversion**: every content image ships as webp beside its
committed png original (DECISIONS 123). When adding an image, add its
path to the list in `scripts/convert_images.sh`, then:

```
sh scripts/convert_images.sh     # requires: brew install webp
```

Icons, the brand mark and record-linked documents are excluded on
purpose. Reference images in markup with `<picture>` plus a webp
source, explicit width and height, and `loading="lazy"` below the
fold; copy any existing figure.

**Fonts** (`assets/fonts/*.woff2`): the committed files are NOT the
Google Fonts CDN originals. They are instanced to weight range 400 to
600 (DECISIONS 125). If a design change needs a weight outside that
range: re-download the CDN originals, widen `WGHT` in
`scripts/instance_fonts.py`, then:

```
python3 -m pip install fonttools brotli   # once
python3 scripts/instance_fonts.py
```

The script is idempotent; rerunning on already-instanced files changes
nothing.

## The pre-commit ritual

Every content change ends the same way:

```
bundle exec jekyll build          # zero warnings
python3 scripts/prose_check.py    # "clean"
```

Then look at the rendered page once in both themes. If the change
moved a URL, test the old URL locally before pushing.
