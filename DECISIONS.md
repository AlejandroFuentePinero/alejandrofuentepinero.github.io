# DECISIONS.md: Phase 2 judgment calls

Produced on branch `refurb/phase-2-cleanup`, 2026-08-07. Working rule from Gate 1: only pressing decisions are surfaced; everything else follows best practice and is logged here so it can be traced and tested once the site is visible. Excluded from the Jekyll build.

## Redirects and URLs

1. **The two malformed publication URLs moved to their final slugs now, not Phase 4.** The instruction was to prove the redirect mechanism for these URLs in Phase 2. A redirect only exists once the page has left the old URL, so the honest proof is the real wiring: both papers now live at `/research/community-reshuffling-2022/` and `/research/ringtail-possum-collapse-2022/`, with `redirect_from` entries in both encoded and literal forms. This removes the two most fragile URLs on the site and de-risks Phase 4. The pages render fine outside a `/research/` index; every internal link to them is generated from the permalink, so nothing dangles.
2. **Interim redirects for the three absorbed talk URLs.** Their final targets (`/research/...`) do not exist until Phase 4, but the files had to go now for the consolidation. Each absorbed URL redirects to its canonical talk's current URL via `redirect_from` on the canonical file, so nothing 404s at any deploy. Phase 4 re-points them per MIGRATIONS.md.
3. **Template-leftover redirect entries dropped** (`/md/`, `/markdown.html` on the threatened species page, `/wordpress/blog-posts/` on the book chapters page) per the Gate 0 approval of deletion without redirect, even though their host pages are not otherwise reworked until Phase 4.

## Links

4. **All `/master/` GitHub links re-pointed to local paths, not just the audit's headline six.** The audit's summary named 4 hotlinked images and 2 PDF links, but the full grep found about 30 references riding the branch-rename redirect: every publication "Download paper" link, one `paperurl`, 9 certificate links on the education page, a talk poster and a talk image. Every target file already lives in this repo, so all now serve from `/files/` and `/images/`. This removes github.com and raw.githubusercontent.com as dependencies entirely, and the localised links also fix the CBCS talk image, which as a blob URL never rendered as an image.
5. **URLs with spaces were percent-encoded when localised** (the 2025 GCB PDF, including its U+2010 Unicode hyphen, encoded as `%E2%80%90`). The literal-space markdown links worked only by browser tolerance.
6. **The dead `codeofclimber.ru` comment URL was removed from `tag-list.html` too.** The audit only found the `category-list.html` copy; the include has an identical twin. Comment-only change, no rendered output affected.
7. **Phantom icon tags stripped now rather than Phase 6** (AUDIT.md 9.2 offered both). Every page load was 404ing up to 11 head requests, which is a broken-links problem, not a design problem. The groodle favicon references stay; Phase 6 generates the real icon set.

## Content

8. **Grants and awards single-render: `/academic/grants_awards/` is the canonical surface until Phase 4.** The CV page now links to it instead of re-rendering the whole portfolio loop. Chosen over the reverse (inlining in the CV and retiring the grants page) because the grants page is the URL CONTENT_MAP keeps redirecting to `/work/#grants-awards` later.
9. **Talk consolidation preserves every fact verbatim.** Absorbed titles, venues and dates appear as "Also presented" lines on the canonical entries. Nothing was retitled or redated. The ESA 2021 poster link survives on the canonical ESA-SCBO entry, re-pointed to the local PDF.
10. **A side effect to know about:** the "Also presented" line is now the first paragraph of the three canonical talks, so archive listings auto-excerpt it instead of a full abstract. Interim state; Phase 5 writes explicit excerpts for every talk.
11. **The Nmixture repo link was removed by unlinking the sentence, keeping the description text.** The talk description is real content; only the dead link went.

## Config and build

12. **Primer theme injection fixed with explicit `theme: null`.** Verified locally: `/assets/css/style.css` (76 KB dead CSS) no longer builds and the build stays warning-free. One residual risk: the production Pages build could in principle treat a null theme differently from the local github-pages gem. Verify `/assets/css/style.css` 404s on the live domain right after the merge; the rollback is deleting one config line.
13. **Site description rewritten to the settled positioning.** It is Tier B copy written early because "Professional website" was placeholder metadata; it gets the same Phase 5 polish pass as the hero.
14. **The author bio field stays "AI Engineer and Data Scientist" for now.** Copy rewriting is Phase 5; Phase 2 corrected only the factually broken field (the stray-@ Twitter handle). The sidebar itself is deleted in Phase 4.
15. **`og_image` stays empty.** The brief's Phase 2 list mentions a real `og_image`, but the actual 1200x630 asset is a Phase 6 deliverable and no honest value exists today. Deferred with this note rather than pointing it at an unsuitable image.
16. **MathJax removed after verification.** Grep for `$$`, `\(`, `\[`, `\begin{` and MathJax markers across all content found zero TeX. Removal also closes a latent bug: the tex2jax config enabled single-`$` inline math, which could have mangled dollar amounts like the grant figures.
17. **MIGRATIONS.md added to the build exclude list alongside the five named documents.** It is a project document like the others and would otherwise render as a page.
18. **`faraday-retry` added to the Gemfile** so local builds are warning-free. GitHub Pages ignores the repo Gemfile, so production is unaffected. The GitHub metadata warning is silenced locally by exporting `JEKYLL_GITHUB_TOKEN` (documented in AUDIT.md section 1, nothing committed).
19. **`.ruby-version` pins 3.3.12** per AUDIT.md section 1, and `Gemfile.lock` is now committed for reproducible builds.
20. **`.DS_Store` added to `.gitignore`.** It kept appearing untracked and slipped into a working commit once (removed from history before push).
21. **`package.json` exclude-list line removed with the file**, per the audit note.

## Verification against the live deployment

The deployment model merges this cleanup to `main` after review. Post-merge spot checks worth 5 minutes: the two new publication URLs and their four old forms, the three absorbed talk URLs, the old blog URL, `/assets/css/style.css` returning 404, and one localised PDF link opening from a publication page.

# DECISIONS.md: Phase 3 judgment calls

Produced on branch `refurb/phase-3-design-system`, 2026-08-07. Numbering continues from Phase 2.

## Typography

22. **Display serif: Newsreader.** A transitional serif drawn for on-screen long-form reading with an optical size axis, so the same file sets both large display and elegant intermediate sizes. It is the warmest of the three shortlisted faces and the closest match to the "well-set print journal" target. Instrument Serif ships a single weight and reads decorative at text sizes. Source Serif 4 is excellent but cooler and more anonymous.
23. **Body and UI sans: Inter.** Tall x-height, screen-first design, full weight range, real italics, tabular figures. It disappears behind the content, which is what the brief's content-first rule asks of the body face. Geist is newer with a shorter rendering track record. IBM Plex Sans is warmer but sets wider and competes with the serif for character.
24. **Code: JetBrains Mono.** Drawn for code with unambiguous 1/l/I and 0/O, and an x-height that sits well next to Inter. IBM Plex Mono pairs best inside the Plex family, which was not chosen.
25. **Variable fonts, latin subset, self-hosted.** One woff2 per family and style from the Google Fonts static CDN, committed to `assets/fonts/` with each family's OFL license text. Roman files are 132 KB (Newsreader), 73 KB (Inter) and 40 KB (JetBrains Mono); italic files download only when a page uses italics, via `unicode-range` and browser lazy font loading. The latin subset includes U+0000-00FF, which covers every Spanish diacritic; a Spanish sample line on the styleguide verifies it visually.
26. **Fluid scale interpretation.** The brief's rem values are read as the desktop sizes at the stated 17px base. The mobile end eases to a 16px base with a 1.2 ratio, fluid with `clamp()` between 390px and 1440px viewports. The computed ranges are annotated in `_sass/_tokens.scss`.
27. **`--step--1` sits below the 15px floor** (13.3px to 13.6px). This is the brief's own 0.80rem value, kept as written. It is used only for labels, captions and metadata; body copy never drops below `--step-0`. The styleguide states this rule beside the specimen.

## Colour and accessibility

28. **The accent carries links as an underline, not as text colour.** Measured on the final tokens: `--accent-deep` on light paper is 4.04:1, below the 4.5:1 body-text bar Phase 6 must hit, and `--accent` is 2.99:1. So link and active-nav text stays ink with an accent underline; accent-coloured text appears only on hover and at display sizes. In dark mode every accent pairing clears 6:1, but the treatment stays identical in both themes for consistency.
29. **Dark logo variant generated, original untouched.** `images/groodle_favicon_256_dark.png` maps the black silhouette to dark-theme ink and turns the white interior detail transparent so the paper shows through (luminance-to-alpha). The header swaps variants with CSS per theme.
30. **The optional SVG redraw was declined.** Tracing the 256px raster would soften the mark, and at its 30px header size the PNG is crisp on every density. Revisit only if a use appears at large sizes; the Phase 6 `og:image` uses the PNG per the brief.

## Theme mechanics

31. **Two explicit theme states, no third "system" toggle position.** With no stored choice, the `prefers-color-scheme` rules in CSS decide, so a visitor who never touches the toggle already follows their OS. The first toggle click stores an explicit choice in `localStorage`; the inline blocking script in the head applies it before first paint. `meta name="color-scheme"` covers the pre-CSS instant. Print always forces the light palette via the token mixin.

## Scope protection

32. **Parallel bundle, legacy untouched.** The new system lives in `assets/css/site.css`, `assets/css/styleguide.css`, `assets/js/site.js` and five new includes. No legacy layout, stylesheet or script changed, so every existing page ships byte-identical HTML (verified by diffing full `_site` builds of this branch against `refurb/main`; the only content diff was the sitemap fix in 33). The jQuery, Magnific Popup and Greedy Nav strip completes in Phase 4 with the layout swap, per the adapted plan.
33. **The styleguide is hidden everywhere a page can leak.** `sitemap: false` keeps it out of `sitemap.xml`, `noindex` out of search, and a `hidden: true` flag plus a one-line `unless post.hidden` guard in the legacy `/sitemap/` page loop keeps it (and the two CSS entry files, which Jekyll also treats as pages) out of the human sitemap. With the guard, `/sitemap/` builds byte-identical to the baseline.
34. **Styleguide nav links are placeholders.** The five nav targets do not exist until Phase 4; real hrefs would 404 from a live internal page. The header include takes a `demo` flag, and the five real URLs live in `_data/navigation.yml` under a new `refurb` key, ready for Phase 4.

## Components

35. **Embed frame fallback triggers on a 15 second timeout** or an iframe error, swapping to a screenshot plus the full-screen link. The screenshot asset `images/apps/digital-twin.png` was captured now; it is also the exact path `_data/apps.yml` already points at for Phase 4.
36. **Known issue, logged for Phase 4: the Space steals scroll once when it boots.** The twin's app focuses its input when it finishes loading, and the browser scrolls the page to a focused cross-origin iframe. If a visitor triggers the lazy load and moves on during the boot window, the page can jump back to the embed once. Site-side mitigations to weigh when the embed lands on the home page: a smaller IntersectionObserver rootMargin so loading starts only when the frame is visible, or a scroll-restore guard. The Space itself stays in observe mode; nothing there changed.
37. **The stats include stays digit-free by construction.** Hash pairs are read with `.first` and `.last` because a bracket index is a literal digit; counts come from `where_exp` plus `size`; the year count comes from date arithmetic; even the comment block avoids digits so the future `prose_check.py` grep stays clean. Verified in the built page: 10 / 18 / 4 / 12 / 193 with "as of Aug 2026" formatted by Liquid from the date field.
38. **Evidence lives in the repo.** `docs/phase-3-evidence/` holds the gate screenshots and the no-flash reload capture, and `docs` joins the build exclude list so none of it ships to the site.
