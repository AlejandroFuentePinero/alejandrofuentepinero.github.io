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
