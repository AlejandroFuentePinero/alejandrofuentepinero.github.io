# Gate 6 evidence: performance, SEO, accessibility

Branch `refurb/phase-6-performance-seo-a11y`, 2026-08-08. All numbers
measured, not estimated.

## Measurement method

Lighthouse 13.4, Chrome headless, default mobile emulation and
throttling, against the local build. Two serving setups matter:

- **Phase start**: `python3 -m http.server` (no compression), the same
  setup as the AUDIT.md baseline.
- **Final**: `http-server` with gzip, matching GitHub Pages compression.
  woff2 and images are incompressible either way, so the difference is
  the ~30 KB of HTML, CSS and JS text per page.

Raw Lighthouse JSON is committed beside this file:
`lighthouse-before/` (phase start) and `lighthouse-after/` (final).

## Lighthouse against target and baseline

Categories are Performance / Accessibility / Best Practices / SEO.
Target: 95+ / 100 / 100 / 100 on 4 pages, home measured with the twin
embed below the fold (it is on the page and lazy).

| Page | AUDIT.md (Phase 0, legacy site) | Phase start | **Final** |
|---|---|---|---|
| Home `/` | 67 / 91 / 96 / 92, LCP 20.2 s | 85 / 96 / 100 / 100, LCP 4.2 s | **97 / 100 / 100 / 100, LCP 2.5 s** |
| `/projects/` | 75 / 88 / 96 / 92 (as `/datascience/projects/`) | 97 / 95 / 100 / 100, LCP 2.6 s | **99 / 100 / 100 / 100, LCP 2.0 s** |
| Publication (possum 2022) | audit failed, NO_FCP | 93 / 96 / 100 / 100, LCP 3.1 s | **97 / 100 / 100 / 100, LCP 2.5 s** |
| `/work/` | audit failed, NO_FCP (as `/academic/cv/`) | 95 / 94 / 100 / 100, LCP 2.9 s | **99 / 100 / 100 / 100, LCP 2.1 s** |

CLS is 0 and TBT is 0 ms on every page in every run. The Phase 0
NO_FCP diagnostic did not survive the rebuild: both failing page types
now measure normally (FINDINGS 22).

What moved Performance:

1. The embed fallback screenshot (207 KB png, hidden but downloaded on
   every home load) became a lazy 35 KB webp: home 85 to 93.
2. Serving with compression, as Pages does: 93 to 94.
3. Instancing the fonts to the used weight range 400:600, 458 KB to
   322 KB across five files (DECISIONS 125): home and publication LCP
   3.1 s to 2.5 s, Performance 94 to 97.

## Bundle report against budget

Measured from the built site, gzip at default level:

| Asset | Raw | Gzip | Budget | Loaded by |
|---|---|---|---|---|
| `assets/js/site.js` (all first-party JS) | 5,039 B | **1,749 B** | 15 KB | every page |
| `assets/css/site.css` | 21,067 B | **4,418 B** | 30 KB | every page |
| `assets/css/styleguide.css` | 2,302 B | 702 B | (internal page only) | /styleguide/ |

**Iframe exemption, proven:** zero `<iframe>` tags exist in any built
HTML; `assets/js/site.js` creates the twin iframe only when the embed
frame on the home page scrolls into view. The Space URL appears in the
built output of exactly 4 pages (home, /apps/, the twin project page,
the styleguide) as link hrefs and data attributes, which cost nothing.
The other measured pages (/projects/, /work/, the publication) contain
no reference at all, and their scores above are the proof the embed
does not affect pages it is not on.

## Accessibility checklist

- **4.5:1 body contrast, both themes.** Computed from the tokens:
  body ink on paper 17.63:1 light / 14.60:1 dark; muted text on paper
  5.26:1 / 6.43:1; muted on sunk paper 4.74:1 / 5.54:1. The failing
  colour, `--ink-faint` (2.90:1 / 3.16:1), no longer colours any text
  (DECISIONS 121). Accent-deep (4.04:1 light) appears only on hover
  and focus states, never static body text (DECISIONS 28).
- **Visible focus rings.** Global `:focus-visible` 2px accent-deep
  outline with 2px offset; the skip link becomes visible on focus.
- **Correct heading order.** Scripted scan of every built page: one
  h1 per page, no skips anywhere except the threatened-species
  nomination list, whose headings are inside record markers
  (FINDINGS 20). Card grids and the timeline were fixed this phase
  (DECISIONS 122).
- **Real alt text.** Every rendered image carries alt text describing
  what it shows; the lab cartoon's alt was rewritten from its title to
  a description. Screenshot alts derive from app names. The header
  marks are `alt=""` decorative. prose_check now lints literal alt
  text (DECISIONS 128).
- **Keyboard navigable.** Nav toggle, theme toggle and the projects
  filter are native buttons with `aria-expanded` / `aria-pressed`
  state; disclosures are native `details/summary`; Escape closes the
  mobile nav. No custom focus traps exist.
- **Accessible iframe title.** site.js sets `title` on the twin iframe
  from the frame's heading; the fallback screenshot has alt text.
- **Skip link.** First element of `<body>` on every page, targets
  `#main`.
- **Lighthouse Accessibility: 100 on all four measured pages.**

## SEO

- Titles follow `Page Name | Alejandro de la Fuente` from the one
  pattern in the default layout; the home page is the bare site title.
- Every page has a real meta description, derived per DECISIONS 117
  and enforced by prose_check. The 165-character site description was
  caught truncating and trimmed (DECISIONS 118).
- og:title, og:description, og:url, og:type, og:image (1200x630,
  `og-image.png` beside this file, generated per DECISIONS 120) and
  `twitter:card` on every page.
- JSON-LD: Person on home, ScholarlyArticle on all 12 publications,
  CreativeWork on all 16 projects, SoftwareApplication for all 4 apps.
  Every value derives from front matter, config or the data file
  (checker-enforced). Validation output: `jsonld-validation.txt`
  (parse plus shape checks; a validator.schema.org run against the
  live URLs is a 5-minute post-merge check).
- `sitemap.xml` lists the 42 canonical pages and nothing else: no
  styleguide, no redirect stubs, no PDFs (DECISIONS 126). robots.txt
  allows everything and points at the sitemap. No real page is
  noindexed (the styleguide's noindex is deliberate and pre-existing).

## Images

- 9 content images converted to webp with committed originals as
  `<picture>` fallback, explicit width/height everywhere, lazy loading
  below the fold: `scripts/convert_images.sh`, DECISIONS 123.
- Largest wins: llm-engineering-cartoon 2.5 MB to 211 KB,
  project_pipeline_simple 1.6 MB to 62 KB, digital-twin screenshot
  207 KB to 35 KB.
- Icons and the groodle mark stay png, untouched, per the brief.
- The 11 MB demo gif is the one asset webp cannot fix: DECISIONS 124,
  FINDINGS 21.

## Asset sweep

3 orphans deleted (4.2 MB): `images/profile.jpeg`,
`files/engine_path.png`, `files/simple_workflow.png`. Grep evidence
per file, raw and URL-encoded forms: `asset-sweep.txt`.
`images/Pasted Graphic.png` stays: a record references it
(DECISIONS 127).

## prose_check and build

- `prose-check-final.txt`: clean over 53 files, the stats include and
  the JSON-LD include, with the metrics table.
- `prose-check-seeded.txt`: every new check fired on a seeded
  violation before landing clean.
- `build-log.txt`: `bundle exec jekyll build`, warning-free.
- CI (`.github/workflows/prose-check.yml`) runs the checker on this
  branch's pushes and stays green.

## What remains for Phase 7

Phase 6 leaves no open diagnostic. Phase 7 per the brief: the full
link and redirect crawl on the live domain, HTML validation on ten
pages, cross-browser and iOS checks, the reduced-motion and
theme-flash checks, the twin embed failure drill with the network
blocked, the stats band increment test with a dummy publication, the
/work/ print check, a final prose_check sweep, and MAINTENANCE.md
(which should also absorb the regeneration steps for the og:image,
webp conversions and font instancing scripts added this phase). Owner
calls parked in FINDINGS: 20 (record heading levels), 21 (demo video
replacement), plus the pre-existing 6, 8, 9, 13, 14, 16, 18, 19.
