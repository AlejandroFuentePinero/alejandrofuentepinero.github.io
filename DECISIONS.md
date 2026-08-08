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

# DECISIONS.md: Phase 4 judgment calls

Produced on branch `refurb/phase-4-structure`, 2026-08-07. Numbering continues from Phase 3. Working rule unchanged: only pressing decisions were surfaced; everything else follows best practice and is logged here.

## Redirects and URLs

39. **The 8 non-page talk URLs redirect via `redirect_to` on the talk documents themselves.** No stub files needed: the plugin replaces each document's output with a redirect page while its front matter stays available to the /research/ talk rows. Verified in the gem source that `redirect_to` replaces `doc.content`, which is why the rows read only front matter.
40. **The three interim talk redirects now point at their final targets directly, with no chains.** `melbourne_2022` and `tropical_bes_2021` got standalone stubs to `/research/#talks`, replacing the Phase 2 `redirect_from` entries that would have produced two-hop chains through the canonical talks' URLs. `esa_2021_poster` redirects straight to the kept `/research/elevational-shifts-talk-2022/` page.
41. **The teaching collection switched to `output: false` with two stubs at the old URLs.** The two entries render inline on /research/, which needs their raw content; `redirect_to` on the documents would have replaced that content with redirect HTML (decision 39), so the stubs carry the redirects instead.
42. **All anchor-target stubs live in `_pages/redirects/`**, one file per old URL, `sitemap: false`.
43. **The old URL inventory is crawled by script.** `docs/phase-4-evidence/crawl_old_urls.py` serves the built site with GitHub Pages resolution semantics (extensionless URLs resolve to `.html` files), requests all 143 old and new URL forms, follows meta-refresh chains, and requires every one to end in a 200. The report is committed beside it.

## Structure

44. **Publication bodies lost their `# Abstract` heading and download line; nothing else.** The disclosure summary "Original abstract as published" replaces the heading, and each download link moved to a `pdf` front matter field rendered as a PDF link. Abstract text is byte-identical. Where the paper link and the download were the same file (the 2018 Bosque paper), the pdf field was dropped rather than render the same link twice.
45. **Publication leads and index entries reuse the existing front matter excerpts verbatim.** They are topics, not findings; Phase 5 rewrites them to the standard in CONTENT_MAP 7. Talk rows carry no excerpt at all this phase, because the only existing prose is full abstracts, and auto-excerpting them is the exact sitemap failure the audit flagged.
46. **Talk awards and second-venue facts moved into front matter** (`award:`, `also:`) so rows and pages render them consistently. Wording comes from the awards file and the talks' own "Also presented" lines; titles, venues and dates untouched.
47. **The Python labs merged with headings demoted one level** under each lab's title heading, so the merged page keeps a sane outline. A structural card line was written for the merged page (the only card copy that could not migrate verbatim); Phase 5 polishes it.
48. **Timeline entries carry role, organisation and dates only.** The 40-word summaries are Phase 5 copy; the structure does not fake them in the meantime.
49. **CV sections with no mapped Phase 4 destination survive as collapsed blocks on /work/**: volunteering and field experience, professional development, the field and modelling skills list, and media engagement. CONTENT_MAP routes media engagement to the relevant paper pages in Phase 5; until then the record stays reachable.
50. **Education renders the cv.md degree list visibly; everything else from the education page sits verbatim in one collapsed "Certificates and training" block.** The block internally duplicates the degrees (its own Formal Education details); accepted inside level 3 until the Phase 5 rewrite.
51. **Retired-page prose that CONTENT_MAP routes to Phase 5 destinations was not republished this phase.** The academic.md postdoc and PhD paragraphs (seeds for the /research/ intro) and the datascience-skills depth content (destined for the /work/ intro and project pages) live in git history at this branch's parent; DECISIONS records that so the Phase 5 passes can pull them.
52. **Editorial service renders as a small disclosure at the end of the publications section**; book chapters live in `_data/book_chapters.yml` (citations verbatim) so the section's count is derived, per CONTENT_MAP 3.1.
53. **Structural text written this phase, flagged for the Phase 5 polish pass**: the /projects/ lead (option D's closing line, per POSITIONING 1.5), the /work/ lead (option F's rainforest line, same source), the home CTA and contact availability line, the /apps/ intro, the 404 copy, the sitemap intro, and the two /research/ pointer lines (threatened species record, book chapters post).
54. **Two additions to the styleguide**: the type filter row as component 15, and the app card media variant under component 5. Both were needed by pages the styleguide's 14 components did not cover; both follow the accent-underline and hairline idioms.
55. **Stack chips were extracted into front matter from each project's own Stack section**, 2 to 5 chips per project, names verbatim.

## Behaviour

56. **The embed observer runs with rootMargin 0** (settled from decision 36): the Space can only boot, and only steal scroll, while the frame is already on screen. Residual behaviour, logged: a visitor who scrolls the frame into view and keeps moving during the boot window can still be pulled back once when the app focuses its input. Accepted for now; the only stronger fix is a scroll-restore guard, revisit if real use shows it.
57. **The projects filter only ever hides.** The control ships `hidden` and is revealed by JS; filtering toggles `hidden` on cards. With JS off the control never appears and every project shows.
58. **The CV PDF is generated from /work/ through the print stylesheet** with every disclosure opened, committed at `files/alejandro-de-la-fuente-cv.pdf` and linked from /work/ and /contact/. Regeneration steps go into MAINTENANCE.md in Phase 7.

## Config and strip

59. **Zero jQuery ships.** `main.min.js`, the plugin and vendor JS trees, the entire legacy SCSS tree with its vendor imports, the academicons and font-awesome font files, every legacy layout and include, and the `ui-text`/`authors`/`comments` data files are gone. The only JS on the site is `assets/js/site.js`.
60. **Config consumed only by deleted templates went with them**: analytics, comments, staticman, social-share and SEO-verification blocks, archive settings, `compress_html`, reading-time and breadcrumb flags. The author block is trimmed to the seven fields the header, footer and contact page consume. `jekyll-paginate` stays in the plugin list for GitHub Pages parity even though nothing paginates.
61. **The 404 was rewritten, not migrated**: the old copy carried a triple-hyphen dash and a dead Google `fixurl` script. New copy is 3 lines and 2 links.
62. **The base head is deliberately minimal** (title pattern, meta description from `page.description | excerpt | site.description`, canonical, icons, theme script, fonts, one stylesheet, one script). Phase 6 owns real SEO metadata, og:image and JSON-LD.

# DECISIONS.md: Phase 5 judgment calls, _pages pass

Produced on branch `refurb/phase-5-pages`, 2026-08-07. Numbering continues from Phase 4. Working rule unchanged: only pressing decisions were surfaced; everything else follows best practice and is logged here.

## Settled with the owner

63. **The PhD field reads "Quantitative Ecology" everywhere.** The one surfaced decision: the CV recorded "Zoology and Ecology", the education page "Quantitative Ecology" (FINDINGS 1). The owner chose Quantitative Ecology. Applied to the /work/ education list, the timeline entry and the regenerated CV PDF. Degree punctuation normalised alongside: credential lines read B.S., M.S., Ph.D. (the CV's "Ph.D" lacked its final period), and prose uses "PhD" without periods, per TERMINOLOGY.md.

## Copy

64. **Tier classification.** Tier B: home, /work/, /projects/, /research/, /contact/, /research/threatened-species/. Tier A: /apps/, 404, sitemap, terms. The styleguide is internal and exempt; the redirect stubs carry no prose.
65. **The timeline stays at 5 entries.** CONTENT_MAP 8 budgeted 6 entries, but only 5 roles exist and the AI engineering work is projects, not employment. Inventing a sixth entry would fake a role. The 40-word summaries were written from the retired academic.md paragraphs, POSITIONING 3.2 and the volunteering record; no new facts introduced.
66. **The certificates block compressed to title, provider, certificate link and one "Covers" line per course.** The Highlights and Formal Education subsections went entirely: they were the internal degree duplication DECISIONS 50 deferred to this pass, plus a summary-of-a-summary. Every certificate link survives, including the three module certificates. The dropped syllabus prose lives in git history at this branch's parent. The Murray Logan workshop appeared twice (core texts and R) and now appears once, under R.
67. **Grants and awards compacted to one line per item**: year, organisation, project title verbatim, amount verbatim. Award titles kept verbatim, including "Best talk prize for best presentation" as recorded.
68. **The terms page now describes the real site.** The old text was template boilerplate about Disqus comments, ad cookies and Google Analytics, none of which exist. The rewrite states what is true: no cookies, no analytics, the localStorage theme value, GitHub Pages request logging, and the digital twin's message logging on Hugging Face, which nothing on the site previously disclosed. Word budgets set where CONTENT_MAP 8 had none: terms 150, sitemap 120.
69. **Record spelling repairs limited to unambiguous typos** ("Organisaion", "Spaninsh", "iberian", a stray "Year 2016" missing its colon). Names, titles, dates and amounts untouched. The media engagement block was not touched at all: DECISIONS 49 routes it to paper pages in the _publications pass.
70. **The threatened species page title pluralised** to "Threatened species nominations"; the permalink is unchanged and the nomination list is byte-identical inside its record markers.
71. **The Gate 1 surfaces shipped unchanged.** Hero, role line, stats band, skills row and the twin framing were reviewed rendered, per the POSITIONING assumption of one polish pass, and needed no edit. The home CTA line and the four card texts were polished; the Job Intelligence Engine card lost its unexpanded "LLM" acronyms to a judge-model phrasing.

## Tooling

72. **Verbatim records are marked in source** with `<!-- record -->` and `<!-- /record -->` comments. `scripts/prose_check.py` skips them for every check and excludes them from word budgets, because records are never rewritten and nothing in them is actionable. The markers ship as invisible HTML comments.
73. **prose_check scope this pass**: the 10 _pages files plus the digit check on the stats include. Later Phase 5 passes extend the FILES table collection by collection. Acronym rule: an allowlist (AI, CV, PDF, XML, URL, and the acronym-shaped proper names CONAF, CSIRO, ORCID) plus an expansion dictionary; anything else fails. The checker was verified to fail on the pre-rewrite pages (83 violations) and on a digit seeded into the stats include, and runs in CI via `.github/workflows/prose-check.yml` on pushes and pull requests.
74. **The CV PDF was regenerated** with the Phase 4 method (the /work/ print stylesheet with every disclosure opened): 9 pages, down from 18, with the settled degree title.

# DECISIONS.md: Phase 5 judgment calls, _projects pass

Produced on branch `refurb/phase-5-projects`, 2026-08-07. Numbering continues from the _pages pass. Working rule unchanged: only pressing decisions were surfaced; everything else follows best practice and is logged here.

## Settled with the owner

75. **Source material for the hard-decision and did-not-work sections.** 4 decisions surfaced and settled: (1) the LLM Engineering Lab page draws both sections from its repo README's recorded material rather than omitting them; (2) research pages write "the decision that was hard" from the recorded methodological crux, the documented choice plus the alternative it rejected, with no invented anecdotes; (3) "What did not work" appears only where the record supports it and is omitted on the 4 pages whose sources record no failure (possum forecast, bird declines, community reshuffling, elevational migration), to be filled from owner input in a later pass; (4) the AI-JIE page follows its technical report on models, stating that extraction started on gpt-4o-mini and moved to gpt-5.4-mini for the final batch, replacing the page's stale GPT-4o-mini and GPT-4o claim.

## Copy

76. **All 16 project pages are Tier A.** Research pages use the identical heading template as engineering pages (Links, Architecture, the hard decision, what was measured, what did not work where recorded, Role), and each research page closes with "What this taught me about evaluation". The paper cross-link lives in the Links section as "Paper page".
77. **Engineering depth was sourced from the projects' own records, not invented**: the 7PH Graph material from the page's existing copy, the digital twin's hard decision and failures from its architecture decision records and decisions log (including the frozen baseline, 0.866 mean reciprocal rank and 4.56 judge accuracy, and the drift-flag trajectory 12, 9, 6), the Job Intelligence Engine's from its technical report (the frozen candidate universe, salary R² about 0.30, skill models 0.88 to 0.95 area under the curve), and the lab's from its README (quadratic resampling closing the guess-low exploit, ensemble error $29.95 and R² 86.3%). Every number new to a page traces to one of those documents.
78. **Titles rewritten for the grid and the sitemap.** Research titles compress to result-oriented names, with the possum and bird pages matching their home card names ("Ringtail possum viability forecast", "Rainforest bird declines"). AI-JIE's title drops its unexpanded "LLM" and ampersand. Slugs, dates and types are unchanged, so no URL moves.
79. **Excerpts.** The 4 home-card projects reuse the live home card text verbatim, so the 2 surfaces cannot disagree. The other 12 excerpts are new, result-first and 25 words or fewer. This finalises the python-labs card line flagged in DECISIONS 47.
80. **Labs carry a reduced template.** MLB SQL and Python Labs open with the outcome and say plainly that they are practice. They omit the hard-decision and did-not-work sections: the labs record no such material, and inventing it would fake the signal the lab reclassification exists to give.
81. **Fact corrections sourced from the record**, beyond decision 75's model names: the niche-theory page's "23 focal species" became the paper's 50 endemic species, and the spatiotemporal page reports cyclones and droughts as marginal, as the paper concluded, instead of the old page's cyclone-damage headline. The bird-declines survey count renders as 1,977 so it cannot read as a year. The elevational-migration page states its manuscript is under review at Diversity and Distributions and carries no paper cross-link, because no paper page exists yet.
82. **2 wording detours around the banned-word list.** "Landscape composition" from the reshuffling paper renders as "terrain composition" (the checker cannot tell literal from figurative "landscape"), and the escalator to extinction carries its PNAS link on first use per TERMINOLOGY.

## Tooling

83. **prose_check extensions.** The 16 project files join FILES as Tier A with no total budget (level 3 unbounded per CONTENT_MAP 8), plus 2 project-only checks: at most 120 visible words before the first heading, and a front-matter excerpt of at most 25 words. Toolchain rows separated by " · " skip sentence checks (version dots otherwise read as sentence ends), and bold markers are stripped before sentence splitting. Allowlist and expansion additions are recorded in TERMINOLOGY.md. The extended checker surfaced 11 violations in the rewritten drafts before landing clean, so every added check has fired at least once.

# DECISIONS.md: Phase 5 judgment calls, apps pass

Produced on branch `refurb/phase-5-apps`, 2026-08-07. Numbering continues from the _projects pass. Working rule unchanged: only pressing decisions were surfaced; everything else follows best practice and is logged here. The roster, the operational notes and the 2 repo links were settled before the pass started (CONTENT_MAP 5, Gate 1, FINDINGS 10).

## Copy

84. **Pitches reuse settled surfaces where one exists, per the decision 79 principle.** The twin pitch is its project page excerpt verbatim (25 words, the cap exactly) and the Job Intelligence Engine pitch is its home card verbatim, so those surfaces cannot disagree. The 7PH pitch is its home card split into 2 sentences for the Tier A 20-word sentence limit, with the active "carries" replacing "backed by" at the split. The birds pitch was written fresh: the CONTENT_MAP 5.1 draft carried a 4-word noun cluster ("rainforest bird population trends") and a vague "long-term", which became the recorded 17 years, agreeing with the home card and the project page.
85. **Demonstrates lines state the engineering signal the pitch does not carry.** All 4 open "It shows" (recorded in TERMINOLOGY.md) and every claim traces to the app's project page: the twin's frozen baseline scoring retrieval and answer quality, 7PH's charts refusing to draw without evidence, the Job Intelligence Engine's deterministic pipeline scored on held-out data, and the Shiny app as the models behind a published paper, open for anyone to query.
86. **The twin note lost its semicolon.** "Embedded on the home page; this entry links the standalone Space." broke the no-semicolon rule and now reads "The chat also lives on the home page.", matching the project page's phrasing. The Gate 1 operational notes for 7PH and the Shiny app shipped unchanged, as settled.
87. **The /apps/ intro polish (decision 53)**: "tools" became "apps" per the TERMINOLOGY row for things on /apps/, and the passive "how it was built and measured" became "how I built and measured it". With the data strings counted, the page totals 198 words of its 200 budget.
88. **The Shiny app source field stays empty.** GitHub search (the owner's repo list, repository search, code search for the app slug) found no public repo for the app anywhere; the only code hits are this site and the twin's knowledge base. The card's existing guard hides the Source link, so the entry renders correctly without it. Surfaced to the owner as FINDINGS 12.

## Tooling

89. **prose_check reads _data/apps.yml directly, instead of the gate evidence hand-counting it.** The open call this pass: the pitch, demonstrates and note strings reach the page through Liquid, so the page-level checker never sees them. Extending the checker won over a hand count because the strings are Tier A prose with hard ceilings that must survive post-launch maintenance, and a hand count goes stale the first time an app is added or edited. CI runs bare python3 with no pyyaml, so the checker parses the flat one-line YAML itself, appends the strings to the apps.html blocks (so every existing check and the 200-word page budget covers them), scans the data file for dashes, and enforces the 25-word card ceiling per pitch. Every new check fired on a seeded violation (em dash, banned word, over-length sentence, over-budget page, 27-word pitch) before landing clean.

# DECISIONS.md: Phase 5 judgment calls, publications pass

Produced on branch `refurb/phase-5-publications`, 2026-08-07. Numbering continues from the apps pass. Working rule unchanged: only pressing decisions were surfaced; everything else follows best practice and is logged here. Settled before the pass started: the CONTENT_MAP 7 worked example applies verbatim to the possum paper, the 2023 GCB abstract is repaired against the journal, and the media headlines are verified against their sources.

## Copy

90. **The summary lives in front matter and replaces the excerpt as the page opener.** The publication layout wraps the whole body in the abstract disclosure, so the 120-word summary could not live in the body without splitting the record. It lives in a `summary` block scalar per file, rendered above the disclosure through markdownify, in normal body type like the project leads. The excerpt no longer renders on the paper page, where its first sentence would duplicate the summary's opening. It remains the index finding on /research/ and now feeds each paper page's meta description through the existing head logic.

91. **The worked example shipped verbatim** (CONTENT_MAP 7.1, 7.2 and 7.4): the possum index entry, the summary, and the page order of summary, collapsed abstract, citation, links, media with the Mediaportal source, and project cross-link. The other 11 summaries were written fresh from the findings to the same shape. Every number was cross-checked against the live surfaces: the home cards, the project pages with the DECISIONS 81 corrections (1,977 surveys, 50 endemic species, cyclones and droughts as marginal) and the threatened-species page (14 bird nominations plus the possum, through the EPBC Act and the IUCN via BirdLife International).

92. **The 2023 GCB abstract repair (settles FINDINGS 2).** Wiley blocks non-browser requests at the DOI, so the journal text came from 2 independent publisher-supplied copies: PubMed record 36654193 and the Europe PMC record for 10.1111/gcb.16608, which agree word for word. The word-level diff against the site text showed exactly 4 broken hyphenations (spe-cies, popu-lation, stress-ors, dy-namics) and 41 doubled spaces, and no other difference. The repaired body is that journal text byte for byte, and the diff is committed in the gate evidence.

93. **Media routing (executes DECISIONS 49).** Each entry moved to the paper its coverage belongs to: the James Cook University release, the Mediaportal 70-national-stories report, both ABC pieces and the Skyrail Rainforest Foundation post to the possum paper; the Narromine story to the birds paper; the El Austral line to the 2017 bamboo paper. The ABC pieces predate the possum paper by 10 months, but they interview the owner about the same possum-decline research and the CV grouped them under the possum block, so the paper page carries them. The New York Times photo credit has no relevant paper and is the media block's one remaining entry on /work/.

94. **Headlines verified against sources, typos fixed (settles FINDINGS 7).** Verified exact: "Possums threatened by climate change" (James Cook University, via the Wayback Machine, since the live page sits behind a bot wall) and the New York Times selfies headline. Corrected against the live pages: "Aussie birds disappearing due to warming" (was "Aussi birds dissapearing"), "Global warming drives Wet Tropics possum species from their mountain homes" (was "possums species fromt"), and "Tropical Rainforest Research in Education" (was "Tropical rainforest research"). The ABC interview now carries its own published title, "Climate change drives possums from high altitude homes in Queensland's wet tropics". The El Austral line could not be verified (print outlet, no link) and moved unaltered: FINDINGS 13.

95. **Media and project fields render from the layout.** Media items carry title, outlet and url in front matter and render as "headline · outlet" lines inside a citation-block, reusing that component unchanged. Items without a url (El Austral) render unlinked. The project cross-link resolves its label from the project page's own title at build time, so a future retitle cannot desynchronise the 2 surfaces. Outlet labels are site prose, so the acronym rule applies to them: the release outlet reads James Cook University, not JCU.

## Tooling

96. **prose_check publications policy (the front matter call).** Publication prose reaches the page through front matter, so the checker reads the 2 fields the pages render as prose: the excerpt (25-word ceiling, no question marks, per the index-entries-are-findings rule) and the summary (all Tier B checks plus the 120-word budget). The title and citation fields are verbatim records and are skipped, which also exempts the citation en dashes, sitting inside numeric ranges as the brief permits. Media titles are third-party records verified against their sources and are skipped. The body must be nothing but the record-marked abstract: any prose outside the markers fails. All 8 new checks fired on seeded violations before landing clean.

# DECISIONS.md: Phase 5 judgment calls, talks pass

Produced on branch `refurb/phase-5-talks`, 2026-08-07. Numbering continues from the publications pass. Working rule unchanged: only pressing decisions were surfaced; everything else follows best practice and is logged here. Settled before the pass started: the 12-entry consolidation and the 4 kept pages stand (DECISIONS 39, 40), the duplicated ZENQ and ESA-SCBO abstracts stay collapsed on their pages, and the PhD seminar abstract is repaired against the published thesis record.

## Copy

97. **The talk pages reuse the publications mechanics exactly.** A `summary` block scalar in front matter, rendered above everything by the talk layout through markdownify, then the submitted abstract inside a collapsed disclosure. The excerpt is the row entry on /research/ and no longer renders on the page, where its first sentence would repeat the summary's opening. This closes the interim state DECISIONS 10 and 45 recorded: every talk now carries explicit prose, so nothing auto-excerpts an abstract.

98. **The disclosure reads "Original abstract as submitted", not "as published".** Talks submit abstracts to a committee; journals publish them. The papers keep their own wording, and both labels sit in TERMINOLOGY.

99. **The 2 duplicated abstracts stay, collapsed and uniform.** The ZENQ 2023 abstract duplicates the 2023 Global Change Biology paper and the ESA-SCBO 2022 abstract duplicates the reshuffling paper. One template for all 4 pages beats a special case: the duplication sits invisibly at level 3, the record is never touched, and each page carries a "Paper page" cross-link so a reader who wants the paper is 1 click away rather than reading the same text twice by accident.

100. **The 4 summaries were written from what each talk argued, not from its abstract.** Each opens on the result and states the method only where it carries the argument. Every number traces to the record: 47 species and 5 drivers from 2000 to 2016 (birds), 7,613 assemblages (reshuffling), three decades of monitoring (seminar). The birds summary deliberately does not reuse the paper page's closing sentence, because the same work now has 2 pages and they must not read as a copy.

101. **The seminar page links the thesis, not 4 chapter papers.** The exit seminar is the whole doctorate, and its 4 chapters already have paper pages reachable from /research/. Linking all 4 from the talk page would duplicate the index; linking none would strand the deepest page on the site. The page carries 1 link, to the published thesis at its DOI, with the title verbatim. The flying fox talk links nothing, because no paper exists yet.

102. **The ESA-SCBO poster arc moved from the body into front matter.** The body of a page file must hold nothing but the record-marked abstract, so the poster sentence became a `poster` block (title verbatim, venue, local PDF link) rendered by the layout as an "Also presented" section. The row's `also` line is unchanged. Same mechanism for the seminar's `thesis` block.

103. **The "Abstract - " prefix lines were dropped from the 4 page files only.** They are presentation, not record, exactly as DECISIONS 44 read the papers' "# Abstract" headings; the disclosure summary now carries that label. The 8 rows-only files keep their prefixes, because their bodies are not touched at all.

104. **The talk row gained the excerpt below the venue, per the styleguide.** Component 8 was built at Gate 3 with the order title, venue, excerpt, so the page follows the component rather than the publication row's order. No CSS changed: `.talk-row__excerpt` already existed and had never been used.

## The record

105. **The PhD seminar abstract repair (3 artefacts, nothing else).** The published thesis is "An uphill battle: the impacts of climate change on Montane rainforest vertebrates" (James Cook University, 2024, DOI 10.25903/07p8-7k08). ResearchOnline blocks non-browser requests, and its record page carries only a 2-sentence repository blurb, so the abstract came from the thesis PDF itself, page vii to viii. The word-level diff against the site text found exactly 3 differences: "reshufiling" to "reshuffling", "biogeo chemical" to "biogeochemical", and "causallinks" to "causal links". Every other word matches the thesis exactly. The diff is committed in the gate evidence.

106. **The seminar abstract stays abridged.** The site text is 278 words of the thesis abstract's 519: it omits the habitat-suitability and community-reshuffling paragraphs, 2 closing sentences, and part of the final sentence, and every word it keeps matches the thesis. That is the submitted seminar abstract, an author's own condensation, not corruption, so it was repaired and not expanded. Restoring the missing 241 words would replace one record with a different one.

107. **The IBRC 2025 record keeps its non-breaking spaces.** The abstract carries U+00A0 in 3 places alongside its em dashes. A first pass flattened them to ordinary spaces; they were restored byte for byte. The em dashes stay inside the markers and appear nowhere in the new prose.

## Tooling

108. **prose_check reads talks the way it reads publications.** `check_publication` became `check_front_matter`, shared by both collections with a `has_page` flag. All 12 talk files are checked on the excerpt (20-word ceiling, no questions); the 4 page files add the summary (Tier B, 100-word budget) and the rule that the body holds nothing but the record. The 8 rows-only files render as redirects, so their unrendered bodies are treated as records and only the excerpt is checked, which is why the em dashes in the NFFF and IBRC abstracts never reach a reader or the checker. A new check fires if a rows-only entry grows a summary that nothing would render. All 12 new checks fired on seeded violations before landing clean.

# DECISIONS.md: Phase 5 judgment calls, teaching and posts pass

Produced on branch `refurb/phase-5-teaching-posts`, 2026-08-07. Numbering continues from the talks pass. Working rule unchanged: only pressing decisions were surfaced; everything else follows best practice and is logged here. Settled before the pass started: the teaching collection stays `output: false` with its 2 stubs (DECISIONS 41), the student abstract is a third-party record routed like the paper and talk abstracts, the 2 named record repairs fall under the DECISIONS 69 rule, and the post keeps its content with the chapter list exempt.

## Copy

109. **The course list renders as a collapsed block, not an open list.** The list is a record and exempt from the 120-word teaching budget, but 11 entries under 6 year headings would dominate the page the way the 367-word migration did (FINDINGS 15). A "Course list" disclosure follows the page's own editorial service block and the /work/ certificates block: the visible prose states the shape (11 roles, 6 courses, 2019 to 2025) and the record sits complete at level 3. The nomination list stays open on its own page because that page exists for the record; the teaching section is one of 4 on /research/.

110. **Record repairs, 6 words, under the DECISIONS 69 rule.** "Guess lecturer" became "Guest lecturer" (FINDINGS 15), 4 lowercase "demonstrator" role lines were capitalised to the majority form, and "Toolkit for the Field Biologist" gained the final period every sibling line carries. Course titles, years, degree levels and the lecture title are untouched, including the lowercase "Advanced statistics" (FINDINGS 18).

111. **The mentoring entry opens with the student's finding and keeps every fact in prose.** Result first, then Olivia Bond, Johns Hopkins University, the School for International Training and the year, then the method. The project title sits verbatim in record markers and the abstract is byte-identical inside a collapsed "Project abstract" block. The framing deliberately does not reuse the IBRC 2025 talk excerpt's wording: related work, 2 surfaces, no copy (the DECISIONS 100 principle). The old "**Abstract**" label line was presentation, replaced by the disclosure label, per the DECISIONS 103 reading.

112. **Entry titles: "Courses" and "Mentoring".** "Teaching: James Cook University" repeated the section heading above it and the venue line below it. Titles are the site's own labels, not records; venue and location render from front matter unchanged.

113. **The post's opening 2 paragraphs are the publisher's text, marked as a record.** This settles the open question the pass carried: the wording matches CSIRO Publishing's description of the book, so it is third-party text under brief 6.4, never reworded. Both paragraphs moved byte-identical into record markers inside a collapsed "Publisher's description" block, and new owner prose opens the post with the result. The post title now names the book as published, The Action Plan for Australian Birds 2020, replacing the 2021 misname; the permalink is unchanged, so no URL moves and MIGRATIONS.md gains no line.

114. **The post renders the chapter list from `_data/book_chapters.yml`**, executing the DECISIONS 52 single-source rule. The hand-typed list was verified identical to the data file on all 14 items before it was replaced with a Liquid loop, so the same record now renders on /research/ and the post from one source and cannot diverge. The counts in the post prose stay hand-written numerals: the no-literal-digit rule is scoped to the stats include, and the 2021 book cannot grow a 15th account.

## Tooling

115. **prose_check reads the teaching files directly and joins the /research/ budget to what the page serves.** The entries reach the page through Liquid (DECISIONS 41), so the checker reads them the way it reads `_data/apps.yml`: per-file Tier B checks with dash scans outside record regions, plus a 120-word section budget shared across the 2 files. Their words also join research.html's page total together with the 24 publication and talk excerpts its rows render, so the 700-word page budget now measures the rendered page: 694 of 700 words, which closes FINDINGS 15. Every check newly applied to these files fired on a seeded violation before landing clean (14 violations in the seeded run, committed in the gate evidence).

116. **The post's budget is 120, not CONTENT_MAP's "keep 746".** The 746 was the whole old post, blurb and list included. Both are records now, so the budget applies to the owner's prose alone, at the level 2 standard every other page opener carries. The content the 746 described survives complete: blurb collapsed, list rendered from the data file.

# DECISIONS.md: Phase 6 judgment calls

Produced on branch `refurb/phase-6-performance-seo-a11y`, 2026-08-08. Numbering continues from Phase 5. Working rule unchanged: only pressing decisions were surfaced; everything else follows best practice and is logged here. The recurring question this phase was reuse: every new visitor-facing string (a description, an alt text, a JSON-LD value) derives from a settled surface or a data file, so no fact exists in 2 versions.

## SEO metadata

117. **Meta descriptions are lifted, not written.** Each `_pages` file carries a `description` that is a contiguous verbatim span of its own lead, chosen to fit 160 characters (the head's truncation limit). The home description equals the site description in `_config.yml`. Collection pages already derive their descriptions from checked front matter (publication and talk excerpts, project excerpts, the post's auto-excerpt), so they carry no description field. prose_check enforces all of this mechanically: substring for pages, equality for home, presence everywhere except the 404.

118. **The site description lost 2 words.** The new 160-character check caught the settled 165-character description truncating mid-word in every rendered meta tag. "Grounded in years of Bayesian wildlife forecasting" became "Grounded in Bayesian wildlife forecasting" in both copies (config and home front matter). Every fact survives; the years claim stays on the stats band where it is computed, not typed.

119. **JSON-LD derives or omits, never invents.** One include renders four shapes: Person (home), ScholarlyArticle (publications), CreativeWork (projects), SoftwareApplication (apps, from the data file). prose_check fails any literal value in the include beyond the six schema.org constants. ScholarlyArticle carries no author field: the citation string is the only author record, and parsing it would risk misrepresenting co-authors, so the field is omitted rather than derived badly. The url field renders only from absolute publisher links, which is why the 2018 Gallardo paper (whose Paper link serves the local PDF, FINDINGS 4) has none.

120. **The og:image is generated, not designed by hand.** `scripts/generate_og_image.py` reads the light palette from `_sass/_tokens.scss` (hex stays defined in exactly one file), sets the name in Newsreader and the hero's role line in Inter over warm paper with the groodle mark, and screenshots 1200x630 with headless Chrome. og and twitter metadata reuse the head's computed title and description; `og:type` is article for dated documents and website otherwise.

## Accessibility

121. **`--ink-faint` is no longer a text colour.** It measured 2.90:1 on light paper and 3.16:1 on dark, so its six text uses (stats as-of, card notes, publication and talk row years, timeline dates, footer fine print, the disclosure marker glyph) moved to `--ink-muted`, which measures 5.26:1 light and 6.43:1 dark on paper. ink-faint remains for hairline borders only. The token values are untouched; only usage changed.

122. **Heading levels follow structure, not size.** Card titles on /projects/ and /apps/ and the five timeline roles sat as h3 directly under h1 and became h2. Sizing is class-based, so nothing moved visually. Home keeps h3 cards correctly under its h2 sections. The one remaining skip is the threatened-species nomination list, whose h3 headings live inside record markers: FINDINGS 20.

## Performance

123. **webp beside the original, markup with fallback.** `scripts/convert_images.sh` converts the 9 content images (2.5 MB worst case to 211 KB); `<picture>` serves webp with the png as fallback, every img carries explicit dimensions and `loading="lazy"` below the fold. A global `picture { display: contents }` keeps the wrappers layout-neutral inside flex components. Icons and the mark stay png per the brief. The biggest single win was the embed fallback screenshot: 207 KB hidden on every home load, now lazy and 35 KB.

124. **The demo gif stays a gif.** Animated webp measured 26 MB at normal settings and 7.7 MB at best (`-lossy -mixed -min_size`) against the 11 MB original: too little to justify a second multi-megabyte file in history. It lazy-loads below the fold. The real fix is a video file, which replaces the asset itself: FINDINGS 21.

125. **Fonts instanced to the weights the site uses.** The stylesheet requests only 400 (body), 500 (display) and 600 (strong, h4 to h6), so `scripts/instance_fonts.py` narrows each variable font to wght 400:600 in place, keeping every glyph and the full opsz axis; the @font-face declarations state the same range. 458 KB became 322 KB across five files and home LCP went from 3.1 s to 2.5 s, the change that carried Performance past 95. Provenance note: the files are no longer byte-identical to the Google CDN originals (DECISIONS 25); re-fetch and rerun the script to widen the range.

## Crawling

126. **sitemap.xml lists pages only.** Front matter defaults set `sitemap: false` on everything under `files/` and `images/`, removing 19 PDFs: each document is linked from the page that gives it context, and the sitemap advertises canonical surfaces. The styleguide and every redirect were already excluded. robots.txt stays the plugin-generated Sitemap pointer, which allows everything.

127. **The asset sweep deleted 3 files.** `images/profile.jpeg`, `files/engine_path.png` and `files/simple_workflow.png` had zero references outside the project documents (their consumers retired in Phase 4). `images/Pasted Graphic.png` stays despite FINDINGS 3 naming it: the CBCS talk body references it, that body is an unrendered record (DECISIONS 39, 108), and records keep their references. Grep evidence per file, including URL-encoded forms, is committed in the gate evidence.

## Tooling

128. **prose_check reads the three new string kinds.** Descriptions per decision 117. Literal alt text gets the dash and banned-word scans and a 25-word cap (the card ceiling); empty alt is the decorative convention and passes; the acronym rule does not apply because alt text depicts an image rather than introducing terms, and derived alt strings mirror fields checked elsewhere. The JSON-LD include per decision 119. Every new check fired on a seeded violation before landing clean (9 violations in the seeded run, committed in the gate evidence), and the description length check fired on a real defect during development (decision 118).

# DECISIONS.md: Phase 7 judgment calls

Produced on branch `refurb/phase-7-final-qa`, 2026-08-08. Numbering continues from Phase 6. Working rule unchanged: only pressing decisions were surfaced; everything else follows best practice and is logged here.

## Fixes the QA run forced

129. **The Siri 2025 paper links moved from the DOI to the publisher page.** The link check found `https://doi.org/10.37828/em.2025.88.11` resolving to `biotaxa.prod.amazon.auckland.ac.nz`, a hostname that does not resolve on two independent DNS resolvers, so the Paper and Journal links 404 for every visitor. `https://www.biotaxa.org/em/article/view/87143` serves the article (200, verified). The `paperurl` field and the project page's Journal link now point there. The citation string keeps its DOI verbatim, records are never edited. If the registrant repairs the DOI, the links can move back: FINDINGS 23.

130. **The embed fallback gained a reachability probe.** The Gate 7 drill proved that on a fast network failure Chrome commits its own error page inside the iframe and still fires `load`, so the frame reported "loaded" and showed a broken frame; the 15 second timeout never ran because `load` cleared it. The fallback logic in `assets/js/site.js` now also issues a `no-cors` HEAD fetch of the embed URL, which rejects on network failure and flips the frame to the fallback. The timeout stays as the backstop, and a spurious probe failure fails safe: the fallback still links the Space. Verified both ways by the drill: normal load reaches "loaded" and opens full screen, blocked load reaches "failed" with the screenshot fallback visible.

131. **The skills chip-row lost its `aria-label`.** The Nu Html Checker flagged `aria-label` on a role-less `div` as an error on home and the styleguide, the run's only validation error. The labelled section wrapping the row on home carries the accessible name, so the div's label was invalid and redundant at once. Removed in `_includes/skills-row.html`; all 11 pages revalidate with zero errors. Info-level notices were retained with reasons, logged in the validation report.

132. **The CV PDF was stale and is now script-regenerated.** The committed PDF predated the publications pass: it still carried the media engagement block that DECISIONS 93 moved to the paper pages, typo'd headlines included, at 9 pages against today's 8. The Phase 4 method (print stylesheet, every disclosure opened) is now a committed script, `scripts/generate_cv_pdf.py`, so the regeneration steps in MAINTENANCE.md are executable rather than prose. Text-level diff after regeneration: identical to a fresh print of /work/.

## Method calls

133. **HTML validation ran on the hosted Nu Html Checker** (validator.w3.org/nu, version 26.8.7 as self-reported in each JSON response) instead of a local vnu: this machine has no Java runtime and the validator Docker image pull did not complete in reasonable time. Same engine, version pinned in the report. 11 built pages covering all 7 layouts plus home and the 404.

134. **The link check extends the Gate 4 crawler rather than replacing it.** `docs/phase-7-evidence/live_link_check.py` imports the Gate 4 URL inventory (all 143 old and new forms, every MIGRATIONS.md redirect) and resolves it on the live domain, then adds every internal reference extracted from the built site (97), fragment anchor verification against the built HTML (66), and all 75 external links with browser headers. Bot-walled hosts pass only on the exact status AUDIT.md section 5 recorded. The two free-tier app hosts that answer scripts with wake pages (shinyapps 202, streamlit 303) pass only with a same-day real-Chrome load; both screenshots are committed. Result: 381 of 381 after the fixes above.

135. **The stats increment test ran against the rendered band.** A dummy publication was added, built, and removed; the parsed band read 12, then 13, then 12 peer-reviewed papers with every other figure unchanged. The dummy never reached a commit.

136. **CLAUDE.md's Current state section was brought current** alongside the mandated placeholder replacement. It still named `refurb/phase-4-structure` as the working branch; an orientation file that misstates the project state misleads every future session, which defeats its purpose. The rewrite states the refurbishment is complete and routes routine work to MAINTENANCE.md.

# DECISIONS.md: post-launch additions

Produced on branch `refurb/twin-education-tabs`, 2026-08-08. Owner-directed changes after launch. Working rule unchanged: only pressing decisions are surfaced; the rest follows best practice and is logged here.

## The two new tabs

137. **The digital twin gets its own page at /digital-twin/.** Owner direction: the twin should be reachable as its own tab, full screen, rather than only as the home embed. The page reuses the embed frame component with a new `embed-frame--tall` modifier that stretches the body to the viewport below the header; the lazy iframe and the fallback probe (DECISIONS 130) apply unchanged. The home embed stays until the home page iterates: FINDINGS 25.

138. **The nav grows to seven items, the twin first.** Owner direction added Skills and Digital twin, and put Digital twin before Work. Order: Digital twin, Work, Skills, Projects, Apps, Research, Contact. Skills sits beside Work in the who-I-am cluster. The five-item rule (brief 3.1) is superseded by the owner call.

139. **Nav active state matches by prefix, not substring.** `page.url contains item.url` would light both Projects and Digital twin on /projects/digital-twin/, because that URL contains the new page URL as a substring. The header now compares `item.url` against the same-length prefix of `page.url`, which is what DECISIONS 28 ("the page URL sits under the nav item's URL") always meant.

140. **Skills and education merge into one page at /skills/, skills first.** Owner direction: one tab may carry both, and skills present before education. The nav label is the single word Skills, the h1 is "Skills and education", and the education section carries a stable #education anchor.

141. **/work/ keeps its education and skills content, sourced from shared includes.** The CV PDF is /work/ printed (DECISIONS 132), so moving education off /work/ would strip the CV. The degree record, the certificates disclosure and the field skills disclosure moved verbatim into `_includes/education-degrees.md`, `_includes/education-certificates.html` and `_includes/skills-field-record.html`, rendered on both /work/ and /skills/ from one source. The built /work/ page was diffed byte-identical around the swap, so the record and the CV pipeline are untouched.

142. **The two datascience stubs re-point to /skills/.** `/datascience/skills/` lands on the dedicated page instead of the home chip row, via `redirect_from` on the new page; its stub existed only to carry a fragment, which the new target does not need, so it retired. `/datascience/education/` keeps its stub and lands on /skills/#education. MIGRATIONS.md rows updated.

143. **/skills/ distills the retired datascience pages.** Owner direction: the page should faithfully represent the old /datascience/skills/ and /datascience/education/ content, restructured to the system. The old prose, recovered from git history, condensed into the chip row, a core-strength paragraph, 4 delivery bullets, 5 depth disclosures (stack, Bayesian and hierarchical modelling, language models and agents, machine learning and evaluation, data and software engineering), the field skills record, the degree record with 3 distilled outcome lines, and the certificates record. The old em-dash bullets were rewritten to the prose standard, "LLM" stays out of prose per TERMINOLOGY.md, and MCP joined the expansion dictionary. The prose_check budget is ("B", None): the depth lives in level 3 disclosures, the same shape as project pages.

144. **The embed iframe mounts into the frame body.** site.js appended the created iframe to the section, whose only positioned box is the body div, so `inset: 0` resolved against the document and the iframe painted at the page origin, clipped out of its frame. Reproduced on the live home page by injecting an iframe both ways: as a child of the section it lands at document y 0, as a child of the body it fills the reserved space exactly. One line in site.js now appends into `.embed-frame__body`. Found while building /digital-twin/, where the offset was unmissable.

145. **The measure is retired: text runs to the container.** Owner direction from the live /work/ page: paragraphs wrapped at 68ch inside the 1120px container read as pinned left and cut right. The max-width clamps came off p, ul, ol, blockquote, the page lead, the hero lines, disclosures, callouts and figcaptions, and .prose-column widened to the container. The --measure token stays for the styleguide notes. The 68ch readability rationale (brief 5.3) is superseded by the owner call.

## The home page iteration

Produced on `refurb/main`, 2026-08-08. Owner feedback on the home page.

146. **The home twin embed is retired.** Owner direction: with /digital-twin/ live as its own tab, the home section duplicating it came off. FINDINGS 25 closes. The embed frame component itself is unchanged and still serves /digital-twin/ and the styleguide.

147. **The hero opens warmer, from the twin's profile narrative.** Owner direction: the home page is a personal site, not a CV. The thesis grew to two paragraphs drawn from the digital twin knowledge base (the grandfather in rural Spain, a decade of ecology on three continents, the pivot to AI engineering). The role line and the meta description (which must equal the site description) are unchanged.

148. **The skills row leaves the home page for a keyword row in the hero.** Owner direction: the "Builds with" and "Grounded in" groups read as CV material. Six high-level chips (Bayesian inference, Population modelling, System design, AI engineering, Evaluation, Conservation) sit under the thesis with a new `chip--accent` modifier that draws the border in the accent. The skills-row include and `_data/skills.yml` stay: /skills/ and the styleguide still use them.

149. **The stats band renders in the accent, and its labels fit one line.** Owner direction asked for Claude's orange on the numbers and text: that is the existing `--accent` token (#D97757), so no new colour entered `_tokens.scss`. Values take `--accent`, labels and the as-of note take `--accent-deep` for the better small-text contrast (about 4.2:1 on light paper, slightly under the 4.5 target, an owner-directed trade). The first label shortened to "Years with uncertainty", the as-of note went inline, and the items get `justify-content: flex-end` so every value top-aligns whatever the label wraps to.

150. **The portrait is the GitHub avatar.** Downloaded from github.com/AlejandroFuentePinero to `images/alejandro-avatar.jpg` (460px JPEG, 39 KB) and shown as a circle at the top right of the hero, shrinking fluidly on small screens.

151. **Selected work carries seven cards, though the owner said six.** The owner named seven items (twin, 7PH Graph, JIE, the two Global Change Biology papers, the Nature Climate Change opinion, the Ecography paper) while asking for six in total. The explicit list won over the count; the discrepancy is flagged for the owner to drop one if six was meant. The opinion piece has no project page, so its card links to the paper page; the other research cards link to their project pages.

152. **/digital-twin/ serves the bare app.** Owner direction: the tab is the app, so the page header, the framing prose, the project link and the embed frame came off. A direct iframe (`.twin-app`) fills the viewport below the sticky header, loading immediately instead of through the lazy observer, which is right for a page whose only content is the app. The h1 and the lead survive visually hidden through a new `.visually-hidden` utility, so screen readers get context and the meta description keeps its required verbatim source in page prose. The embed frame component and its tall modifier stay for the styleguide; the stale styleguide note naming /digital-twin/ as the tall consumer was corrected. Supersedes the page shape in DECISIONS 137; the fallback probe (DECISIONS 130) no longer applies to this page.

153. **The contact page retires to the footer.** Owner direction: the footer already carries the email, LinkedIn, GitHub, Scholar and ORCID links on every page, so the dedicated page and the home Get in touch section came off. /contact/ redirects to the home page through a stub in `_pages/redirects/`, the nav drops to six items, the sitemap loses its Contact line, `_pages/contact.md` left the prose_check FILES table (redirect stubs are out of scope by design), and MIGRATIONS.md records the re-point. Nothing 404s.

154. **The Ecography card is dropped from Selected work.** Owner call resolving the flag in DECISIONS 151: six cards was the intent. The paper keeps its page and its project page; only the home card went.

155. **The hero portrait grows by a quarter,** to clamp(7.5rem, 17.5vw, 12.5rem), owner direction.

156. **The stats band settles: ink numbers, orange labels, plain Citations.** Owner direction asked for cream numbers to complement the orange labels. Literal cream is invisible on the light theme's paper, so the numbers take `--ink`, which renders as the palette's warm cream (#F2F0E9) in dark mode and near-black in light: the cream the owner saw, theme-safe, no new token. The first label reads "Years of experience", and the visible "as of Aug 2026" note came off the Citations label; the freshness date and source stay recorded in `_data/stats.yml`, where the hard rule requires them.

## The work page iteration

Produced on `refurb/main`, 2026-08-08. Owner feedback on the work page.

157. **The CV download retires from /work/.** Owner direction: the site is the CV, so the PDF link came off the page header. The PDF itself stays at `/files/alejandro-de-la-fuente-cv.pdf` so nothing anyone holds 404s, and the `/cv/` and `/resume` redirects into /work/ are unchanged. The MAINTENANCE.md regeneration procedure now maintains an unlinked artefact (FINDINGS 26).

158. **The timeline opens at Officeworks.** The postdoc ended in May 2026 and its entry closes at 2026, with its summary moved to past tense. The new top entry (AI engineer, Officeworks, 2026 to now) is drawn from the digital twin knowledge base and stays inside its stated confidentiality boundary: generic system descriptions, no internal names, vendors or results.

159. **Education leaves /work/.** Owner direction: degrees, certificates and training belong with /skills/, which already rendered both includes at /skills/#education. The one education redirect stub already targeted /skills/, so nothing re-points. The include comments now name /skills/ as the sole consumer.

160. **The field and modelling disclosure leaves /work/.** Owner direction: it read as CV filler there. The identical record already renders on /skills/ through the same include, so every skill in it stays visible on the skills page and the include survives with one consumer.

161. **Media engagement on /work/ lists the full record again.** Owner direction: the section looked thin with only the New York Times credit. The seven old-site entries return under the disclosure using the verified headlines and outlets recorded on the paper pages in the excerpt rewrite, so the possum, bird and bamboo stories are now dual-listed on /work/ and their paper pages. That dual listing supersedes the /work/-off routing half of the excerpt-rewrite decision; the paper-page half stands.

162. **A heading after a closed disclosure gets air.** `.disclosure + h2` takes `margin-top: var(--space-2xl)` so "Grants and awards" no longer sits on the media disclosure's hairline. The same rule spaces "Education" above the certificates on /skills/. Spacing only, inside the existing token scale, so it skipped the styleguide-first path for new components.
