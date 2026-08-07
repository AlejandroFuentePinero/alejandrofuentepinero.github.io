# CLAUDE.md

Guidance for coding agents working on this site during and after its refurbishment.

## What this is

Alejandro de la Fuente's personal site: Jekyll on GitHub Pages, rebuilt from an
academicpages/Minimal Mistakes fork into one unified site. A full refurbishment
is underway. **Read `REFURB_BRIEF.md` before doing anything else.** It defines
the positioning, architecture, design system, prose standard and phase plan.
This file summarises the working rules; the brief is the authority on intent.

## Current state

The refurbishment is complete: Phases 0 to 7 all shipped (audit,
positioning, cleanup, design system, unified structure, content rewrite,
performance and SEO and accessibility, final QA with `MAINTENANCE.md`).
The site is in maintenance. Routine changes follow `MAINTENANCE.md`;
`refurb/main` retires once the owner deletes the phase branches after
the soak week.

## Authoritative documents

- `REFURB_BRIEF.md`: the full plan. Sections 2 (positioning), 3 (architecture),
  5 (design), 6 (prose standard) and 7 (phases) govern all work.
- `POSITIONING.md` and `CONTENT_MAP.md`: the settled thesis, stats band, skills
  row, URL tree and per-item content decisions. Do not relitigate these.
- `DECISIONS.md`: numbered log of judgment calls per phase. Add to it, never
  rewrite past entries. Numbering continues across phases.
- `MIGRATIONS.md`: the complete old-to-new redirect table. Every URL change
  gets a `redirect_from` entry and a line here.
- `AUDIT.md`, `FINDINGS.md`: Phase 0 inventory and out-of-scope findings.
  Anything you notice that is outside the current task goes in `FINDINGS.md`,
  not fixed inline.

## Branching and deployment

The brief's original model (single launch merge to `master` at Gate 7) was
superseded. The working model is:

- The live site serves from `main`. `refurb/main` is the integration branch.
- Each phase gets a branch `refurb/phase-N-name` cut from `refurb/main`; its PR
  targets `refurb/main`, never `main`.
- `refurb/main` merges into `main` at phase checkpoints after review, so the
  live site iterates phase by phase. No Cloudflare or Netlify preview; local
  `bundle exec jekyll serve` is the preview.
- Never force push. Never rewrite history on `main` or `refurb/main`.
- After any `main` change, merge `main` back into `refurb/main` promptly.

## Hard rules (survive the refurb, apply to all future maintenance)

**Never break the record.** Do not edit `recommended_citation`, citation text,
original abstracts, DOIs, journal names, co-author names, dates or numeric
results in `_publications/`. Abstracts live verbatim in collapsed
"Original abstract as published" blocks; they are never deleted or reworded.

**Never break URLs.** Scholar, ORCID and third parties link here. Every URL
change gets `redirect_from` and a `MIGRATIONS.md` line. Nothing may 404.

**No fabricated or hand-typed numbers.** Every stats band figure is either
derived by Liquid from the collections at build time or read from
`_data/stats.yml` with `source` and `as_of`. No literal digit appears in the
stats include (see DECISIONS 37 for the digit-free construction).

**No new frameworks.** No React, no Tailwind, no Node bundler, no jQuery.
The only JS on the site is `assets/js/site.js`, vanilla. SCSS lives in
`_sass/`; design tokens in `_sass/_tokens.scss` are the only place hex colours
are defined.

**Preserve the brand mark.** `images/groodle_favicon_256.png` (and its dark
variant) plus the full icon set stay. Never delete, rename or repath them.

**Keep the build clean.** `bundle exec jekyll build` stays warning-free.
GitHub Pages runs whitelisted plugins only; raise anything outside the list,
never add it silently. Ruby is pinned by `.ruby-version`.

**Prose standard.** All copy follows REFURB_BRIEF section 6: STE rules, no em
or en dashes in prose (en dashes only in numeric ranges inside citations), no
semicolons in body copy, banned-word list, density budget per surface, every
page opens with the result. From Phase 5, `scripts/prose_check.py` enforces
this in CI.

**Design restraint.** One accent, hairline rules, no gradients, no shadows,
no entrance animations, no counters. Motion is 150 to 200ms, colour and
opacity only, dead under `prefers-reduced-motion`. New components are built on
`/styleguide/` before rollout.

## Working method

- Surface only pressing decisions to the user; default to best practice and
  log the call in `DECISIONS.md` so it can be traced and tested later.
- Nothing outside the current phase or task gets improved. Out-of-scope
  findings go in `FINDINGS.md`.
- Small commits, one concern per commit. No em dashes in commit messages or
  any written output. No AI attribution anywhere.
- Build after every meaningful change. Gate evidence (screenshots, crawl
  reports) lives in `docs/`, which is excluded from the Jekyll build.

## Post-launch maintenance

**Follow `MAINTENANCE.md`.** It is the self-contained manual for every
routine change: adding a project, a publication or an app, refreshing the
two Scholar numbers in `_data/stats.yml`, the prose rules and density
budget in short form, the record-marker convention, extending the
`prose_check.py` FILES table, the branch model, and the regeneration
steps for the CV PDF, og:image, webp images and instanced fonts. It
assumes no other document has been read; when it and this file disagree,
the hard rules above win.
