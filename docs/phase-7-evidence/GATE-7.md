# Gate 7 evidence: final QA

Run on branch `refurb/phase-7-final-qa`, 2026-08-08. `refurb/main` and
`main` were content-identical at run time (they differ by a merge
commit only), so live-domain checks describe exactly this tree. Every
scripted check lives beside this file and reruns from the repo root
after `bundle exec jekyll build`; the JS checks need
`NODE_PATH=<dir with puppeteer-core, pngjs>` (installed ad hoc, not
committed).

| # | Check | Result | Measured how |
|---|---|---|---|
| 1 | Full link check, live domain | **PASS, 381 of 381** | `live_link_check.py`, report in `link-check-report.txt` |
| 2 | HTML validation, ten pages, every layout | **PASS, 0 errors on 11 pages** | Nu Html Checker 26.8.7, `html_validate.py`, `html-validation-report.txt` |
| 3 | prefers-reduced-motion kills every transition, both themes | **PASS** | headless Chrome emulation, `reduced_motion_check.js`, `reduced-motion-report.txt` |
| 4 | No theme flash on hard reload, either mode | **PASS** | CDP screencast pixel analysis, `theme_flash_check.js`, `theme-flash-report.txt` |
| 5 | Twin embed drill: lazy, blocked-network fallback, full screen | **PASS, after one fix** | `twin_embed_drill.js`, `twin-embed-drill-report.txt`, two screenshots |
| 6 | Stats band increment test | **PASS, 12 to 13 to 12** | build-and-parse, `stats-increment-report.txt` |
| 7 | Print /work/ against the committed CV PDF | **Diff found, PDF regenerated** | `scripts/generate_cv_pdf.py` plus pypdf text diff |
| 8 | prose_check clean, CI green | **PASS** | local run and the GitHub Actions history |
| 9 | Cross-browser | **Chrome proven, manual list delivered** | `chrome_console_check.js`, `manual-browser-checklist.md` |
| 10 | Warning-free build | **PASS** | `build-output.txt` |

## 1. Full link check

`live_link_check.py` imports the Gate 4 crawler's URL inventory and
resolves everything on the live domain. 381 checks, 381 passed:

- 143 inventory URLs: every `MIGRATIONS.md` redirect in every recorded
  form (extensionless, `.html`, percent-encoded and literal-space),
  followed through HTTP and meta-refresh chains to a final 200, plus
  every kept and new URL.
- 97 unique internal references extracted from the built site (href,
  src, srcset, meta content, CSS url(), so fonts, images, webp
  variants and PDFs included), each 200 on the live domain.
- 66 fragment links verified against the built HTML: the anchor id
  exists on the target page. The styleguide's bare `href="#"`
  component placeholders (DECISIONS 34) are excluded by design.
- 75 external links with browser headers. Bot-walled hosts pass only
  on the exact status AUDIT.md section 5 recorded as
  verified-in-browser. The two free-tier app hosts that answer
  scripted clients with wake pages passed only after a same-day load
  in real Chrome: `shiny-app-live-chrome.jpg`,
  `streamlit-app-live-chrome.jpg`.

One genuinely dead link was found and fixed: the Siri 2025 DOI
resolves to a defunct hostname upstream, so the site links the working
publisher page instead (DECISIONS 129, FINDINGS 23).

## 2. HTML validation

Validator: the Nu Html Checker at validator.w3.org/nu, version 26.8.7
as self-reported in each JSON response (no local Java runtime, and the
validator Docker image pull stalled: DECISIONS 133). Eleven built
pages covering all seven layouts (default, page, project, publication,
talk, post, styleguide) plus home and the 404.

One error, fixed: `aria-label` on the role-less skills chip-row div
(DECISIONS 131). Six info-level notices retained with reasons, all
recorded in `html-validation-report.txt`. Final run: 0 errors on all
11 pages.

## 3. prefers-reduced-motion

Headless Chrome emulates `prefers-reduced-motion: reduce` crossed with
both colour schemes on 5 representative pages, then reads every
element's computed transition and animation durations. The kill switch
sets 0.01ms (the imperceptible-not-zero idiom), so the bar is no
element above 5ms: zero offenders in all 10 emulated combinations, and
`scroll-behavior` is never `smooth`. A control run without the
emulation sees 26 to 59 elements with real durations per page, so a
clean result cannot be a blind scan. The one surviving delay (the
mobile nav's `visibility` flip, 150ms) is unobservable: the element's
opacity has already snapped to 0 when it runs.

## 4. Theme flash

For each direction (stored dark with OS light, stored light with OS
dark): apply the theme the way the toggle does, hard reload with cache
disabled and network throttled, capture every frame of the reload as
PNG via CDP screencast, and read exact corner pixels against the token
palette (light paper #FAFAF7, dark paper #1F1E1D). Zero wrong-theme
frames at or after firstPaint, zero opposite-theme paints at any
point, in both directions.

## 5. Twin embed drill

`twin_embed_drill.js`, three proofs on the built home page:

- **Lazy**: zero requests to the Space host before scrolling, frame
  state `idle`; scrolling into view creates the iframe and the Space
  requests fire.
- **Fallback**: with every Space request blocked, the frame reaches
  `failed` and shows the screenshot fallback with its link
  (`twin-embed-fallback.png`). The drill first caught a real bug here:
  Chrome fires `load` on a fast-failed iframe, so the frame showed a
  broken embed instead of the fallback. Fixed with a reachability
  probe in `assets/js/site.js` (DECISIONS 130) and re-proven.
- **Full screen**: clicking "Open full screen" opens a new tab on
  `https://alejandrofupi-digital-twin.hf.space/`
  (`twin-embed-loaded.png` shows the loaded state).

## 6. Stats band increment

Dummy publication added, built, removed, rebuilt; the rendered band
read 12, 13, 12 peer-reviewed papers with every other figure
unchanged. Full values in `stats-increment-report.txt`. The dummy
never reached a commit.

## 7. CV PDF

A fresh print of /work/ (print stylesheet, every disclosure opened)
was text-diffed against the committed PDF with pypdf. A real diff
existed: the committed file predated the publications pass and still
carried the media block DECISIONS 93 moved to the paper pages, 9 pages
against the current 8. Regenerated per the brief's "only if a diff
exists", and the method is now the committed script
`scripts/generate_cv_pdf.py` (DECISIONS 132).

## 8. prose_check and CI

`python3 scripts/prose_check.py`: clean, 53 files and the stats
include. GitHub Actions `prose check` green on `refurb/main` and
`main`; the run on this branch's push is linked from the PR.

## 9. Cross-browser

Chrome, automated (`chrome-console-report.txt`): 12 pages at 1280px
and 390px each load with zero console errors, zero uncaught page
errors and zero failed local requests; the theme toggle flips and
persists, the projects filter hides 11 of 16 cards on "engineering"
and restores all, the nav disclosure opens and closes on Escape at
phone width.

Firefox, Safari desktop and iOS Safari were not automated and nothing
is claimed for them: `manual-browser-checklist.md` is the human pass,
12 numbered checks with exact URLs.

## 10. Build

`bundle exec jekyll build` warning-free: `build-output.txt`.
