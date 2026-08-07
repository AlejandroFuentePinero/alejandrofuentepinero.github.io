# FINDINGS.md: out-of-scope observations

Found while working, not fixed, per the working rules in REFURB_BRIEF.md section 8. Excluded from the Jekyll build.

## Phase 4

1. **Degree title discrepancy.** cv.md records "Ph.D in Zoology and Ecology, James Cook University, 2024 (Cum laude)"; datascience-education.md records "Ph.D. in Quantitative Ecology — James Cook University (Cum laude)". Both wordings now appear on /work/ (the visible list uses the CV wording; the collapsed training block carries the other). One record should win in the Phase 5 rewrite. *Resolved in Phase 5: the owner chose Quantitative Ecology, applied everywhere (DECISIONS 63).*
2. **The 2023 Global Change Biology abstract carries PDF-copy artefacts**: doubled spaces and broken hyphenation ("spe-cies", "dy-namics"). The never-edit rule kept it verbatim. If the owner wants the source text repaired to match the journal's actual abstract, that is an owner call, not a rewrite. *Resolved in the publications pass: the owner settled it, and the text was repaired word for word against the journal abstract (DECISIONS 92).*
3. **`images/Pasted Graphic.png`** (the CBCS talk video thumbnail, filename with a space) is now referenced only by a talk body that no longer renders a page. Candidate for the Phase 6 asset sweep along with `images/profile.jpeg`, which lost its last consumer when the sidebar author card went.
4. **The 2018 Bosque paper has no publisher link**; its "Paper" link serves the local PDF. Fine, but worth knowing when Phase 6 adds `ScholarlyArticle` JSON-LD.
5. **`jekyll-redirect-from` emits `/redirects.json`** listing every redirect pair. Pre-existing plugin behaviour, harmless, noted so nobody mistakes it for site content.

## Phase 5, _pages pass

6. **Likely typos inside the nomination record's author lists**: "Graig, M." where the book chapter citations spell "Craig M", and the "Freeman AND." initials style varies between entries. The list is a verbatim record and was not touched; whether to correct it against the submitted nominations is an owner call.
7. **Media engagement block headline typos** ("Aussi birds dissapearing due to warming", "possums species fromt their mountain homes"). The block moves to the relevant paper pages in the _publications pass (DECISIONS 49); fix the titles against the real headlines then. *Resolved in the publications pass: every linked headline verified against its source and corrected (DECISIONS 94). The one unverifiable line is FINDINGS 13.*
8. **The award title "Best talk prize for best presentation"** (2023, Zoology and Ecology North Queensland) reads like a recording slip. Kept verbatim as an award title; owner may want to shorten it to what the prize was actually called.

## Phase 5, _projects pass

9. **The 7PH pilot count may be stale against the live app.** The project page records 1,083 pilots (with 107 events, 4,591 decks, 4,995 cards). The digital twin repo's decisions log (session 65, 2026-08-03) records the live 7phgraph.com footer at 1,086 pilots. The page numbers describe the artifact at its stated date and were kept exactly. Refreshing them against the live footer is an owner call, and the home card carries only the event and deck counts, which agree.
10. **Apps-pass inputs confirmed in passing**: the 7PH Graph source repo is public at github.com/AlejandroFuentePinero/7ph-graph, and the Job Intelligence Engine repo is github.com/AlejandroFuentePinero/job-intelligence-engine. CONTENT_MAP 5.1 left both `source` fields to confirm in Phase 5; the apps copy pass can now fill them.
11. **The digital twin decisions log flags this repo's 7PH page and its 2 PNG files as previously untracked.** They are tracked and rewritten as of this pass; noted only so the twin-side note is not chased twice.

## Phase 5, apps pass

12. **No public source repo exists for the birds Shiny app.** The `source` field of the birds-shiny entry stays empty: GitHub search over the owner's repo list, repository names and code found nothing for BirdsPopTrendAWT (Shiny apps often deploy straight from a local RStudio session, with no repo). If the R source still exists locally, publishing it and filling the field completes the last gap on /apps/. Owner call. *Settled at the apps-pass merge: the owner confirmed no public repo exists. The field stays empty and the card hides the link.*

## Phase 5, publications pass

13. **The El Austral media line cannot be verified.** "Woody bamboo flowering in Puyehue National Park" carries no link, and the outlet is a Chilean print newspaper, so the real headline (presumably Spanish) is unknown; the recorded line reads as a description rather than a headline. It moved to the 2017 bamboo paper page unaltered. If the owner holds the clipping, the line can be replaced with the real headline and date.

14. **Two citations record early-view pagination.** The possum paper citation reads "00, 1– 11" and the 2023 Global Change Biology citation "00, 1-9"; the versions of record have volume and page numbers (the 2023 paper is 29(8), 2132-2140 per PubMed). Citations are never edited under the hard rule, so both stay as recorded. Updating them to the versions of record is an owner call.

## Phase 5, talks pass

15. **The teaching section is 3 times its word budget.** CONTENT_MAP 8 budgets 120 words for teaching on /research/; the 2 entries render 367. They were migrated whole in Phase 4 and are the next pass's material, so nothing was touched here. The page's rendered prose total sits above the 700 budget mainly because of them. Seen in passing while checking the rendered page, for that pass to fix: the James Cook University entry records "Role: Guess lecturer" where it means guest lecturer.

16. **Doubled spaces inside 3 talk locations**: "Mission Beach,  Australia", "Palm Cove,  Australia" and "Santa Cruz,  Chile". Locations are facts and were not touched, and HTML collapses the space so nothing renders wrong. Worth a single pass if the owner ever wants the source clean.

17. **The 8 rows-only talk files keep full abstracts that nothing renders.** Their `redirect_to` output replaces the body (DECISIONS 39), so the text survives in the source as a record and never reaches a reader. That is deliberate, but it means those abstracts are outside every prose check. If a rows-only talk is ever promoted to a page, wrap its abstract in record markers and add a summary first, or the checker will fail the file.
