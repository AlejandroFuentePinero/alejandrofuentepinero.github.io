# FINDINGS.md: out-of-scope observations

Found while working, not fixed, per the working rules in REFURB_BRIEF.md section 8. Excluded from the Jekyll build.

## Phase 4

1. **Degree title discrepancy.** cv.md records "Ph.D in Zoology and Ecology, James Cook University, 2024 (Cum laude)"; datascience-education.md records "Ph.D. in Quantitative Ecology — James Cook University (Cum laude)". Both wordings now appear on /work/ (the visible list uses the CV wording; the collapsed training block carries the other). One record should win in the Phase 5 rewrite. *Resolved in Phase 5: the owner chose Quantitative Ecology, applied everywhere (DECISIONS 63).*
2. **The 2023 Global Change Biology abstract carries PDF-copy artefacts**: doubled spaces and broken hyphenation ("spe-cies", "dy-namics"). The never-edit rule kept it verbatim. If the owner wants the source text repaired to match the journal's actual abstract, that is an owner call, not a rewrite.
3. **`images/Pasted Graphic.png`** (the CBCS talk video thumbnail, filename with a space) is now referenced only by a talk body that no longer renders a page. Candidate for the Phase 6 asset sweep along with `images/profile.jpeg`, which lost its last consumer when the sidebar author card went.
4. **The 2018 Bosque paper has no publisher link**; its "Paper" link serves the local PDF. Fine, but worth knowing when Phase 6 adds `ScholarlyArticle` JSON-LD.
5. **`jekyll-redirect-from` emits `/redirects.json`** listing every redirect pair. Pre-existing plugin behaviour, harmless, noted so nobody mistakes it for site content.

## Phase 5, _pages pass

6. **Likely typos inside the nomination record's author lists**: "Graig, M." where the book chapter citations spell "Craig M", and the "Freeman AND." initials style varies between entries. The list is a verbatim record and was not touched; whether to correct it against the submitted nominations is an owner call.
7. **Media engagement block headline typos** ("Aussi birds dissapearing due to warming", "possums species fromt their mountain homes"). The block moves to the relevant paper pages in the _publications pass (DECISIONS 49); fix the titles against the real headlines then.
8. **The award title "Best talk prize for best presentation"** (2023, Zoology and Ecology North Queensland) reads like a recording slip. Kept verbatim as an award title; owner may want to shorten it to what the prize was actually called.
