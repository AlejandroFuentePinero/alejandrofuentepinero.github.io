# Gate 5 evidence: the teaching and posts pass

Branch `refurb/phase-5-teaching-posts`, 2026-08-07. Scope: the 2 files in
`_teaching/`, the 1 file in `_posts/`, the prose_check extension to both
collections, the TERMINOLOGY additions, and the DECISIONS (109 to 116) and
FINDINGS (18 and 19) entries. No layout or include changed: the /research/
teaching section and the post layout render the new content as they are.
No URL moved, so MIGRATIONS.md gains no line. This PR closes Phase 5.

## 1. Record integrity

Verified programmatically against `refurb/main` before anything else
(`record-check-teaching-posts.txt`).

**The course list** carries exactly 6 word-level repairs under the
DECISIONS 69 rule and no other change:

```
replace: old=['demonstrator.'] -> new=['Demonstrator.']
replace: old=['Guess'] -> new=['Guest']
replace: old=['demonstrator'] -> new=['Demonstrator']   (3 role lines)
replace: old=['Biologist'] -> new=['Biologist.']
facts-ok: all 6 course titles, the lecture title, both degree levels
and all 6 years verbatim
```

**The student project abstract** (Olivia Bond, 2025) is byte-identical
(1,275 bytes) inside record markers in a collapsed "Project abstract"
block, per the third-party-record rule in brief 6.4. The project title
sits verbatim in its own record markers, and the student's name, year and
both institutions appear verbatim in the framing prose.

**The publisher's description** is byte-identical (1,353 bytes) inside
record markers in a collapsed block. The pass confirmed the open question
it carried: the post's opening 2 paragraphs match CSIRO Publishing's
description of the book, so they are third-party text, marked as a record
and never reworded (DECISIONS 113).

**The chapter list** in the old post was verified identical to
`_data/book_chapters.yml` on all 14 items, then replaced with a Liquid
loop over the data file, so the record that renders on /research/ and on
the post now has one source (DECISIONS 114). The built post renders all
14 citations.

## 2. Metrics

Output of `python3 scripts/prose_check.py --metrics` committed as
`prose-check-output-teaching-posts.txt`. All 3 files are Tier B. The
teaching budget of 120 words is shared across both entries; records
(course list, project abstract, publisher's description, chapter list)
are exempt and collapsed.

| file | words / budget | sentences | mean | longest | em+en dashes | banned hits |
|---|---|---|---|---|---|---|
| _teaching/james_cook_university.md | 41 of the shared 120 | 2 | 20.5 | 25 | 0 | 0 |
| _teaching/mentoring.md | 56 of the shared 120 | 3 | 18.7 | 22 | 0 | 0 |
| teaching combined | 97/120 | 5 | | | 0 | 0 |
| _posts/2021-12-01-action-plan-australian-birds.md | 80/120 | 5 | 15.2 | 19 | 0 | 0 |

The teaching section drops from 367 rendered words (FINDINGS 15) to 97
words of prose. The /research/ page budget check now measures the
rendered page (own blocks, both teaching entries, and the 24 publication
and talk excerpts its rows render) and passes at **694/700**. Em dash
count 0 and en dash count 0 outside record regions in every touched
file, front matter included. Banned word hits 0, unexpanded acronyms 0,
no paragraph over 4 sentences, no sentence over the Tier B 25.

## 3. Side-by-side

**_teaching/james_cook_university.md.** Before: title "Teaching: James
Cook University", one intro line ("My teaching experience includes
tutoring and lecturing on ecological courses and advanced statistics."),
then the full 45-line course list open on the page. After: title
"Courses" (the old title repeated the section heading and the venue
line, DECISIONS 112), 2 sentences of framing ("I held 11 teaching roles
across 6 courses at James Cook University between 2019 and 2025. I
tutored and demonstrated in undergraduate ecology, demonstrated in
Master's statistics, helped develop a course, and gave a guest lecture
on conservation under climate change."), then the repaired course list
as a record inside a collapsed "Course list" block (DECISIONS 109, 110).

**_teaching/mentoring.md.** Before: name, year and institution lines,
then the project abstract printed in full under a bold "Abstract" label.
After: the entry opens with the student's finding ("The worst heat
stress responses in the spectacled flying fox come when high temperature
and high solar exposure coincide."), names Olivia Bond, Johns Hopkins
University, the School for International Training and the method, then
the project title and the byte-identical abstract sit as records, the
abstract collapsed (DECISIONS 111). The framing does not reuse the IBRC
2025 talk excerpt's wording: related work, 2 surfaces, no copy.

**_posts/2021-12-01-action-plan-australian-birds.md.** Before: title
"The Action Plan for Australian Birds 2021" (the book is the 2020 plan),
the publisher's 2 paragraphs presented as the owner's prose, a broken
"Chapters contribution:" setext heading, and the hand-typed 14-item
list. After: the corrected title, 76 words of owner prose opening with
the result ("I co-authored 14 species accounts...") and closing on the
nomination record cross-link, the publisher's description collapsed as
an attributed record, and the list rendered from the data file under
"The 14 species accounts". The post's meta description now serves the
owner's first paragraph instead of the blurb.

## 4. Audience check

**The teaching section on /research/.** Recruiter: university teaching at
a glance, 11 roles to Master's level, and a mentored student project
that reached a result. Peer: statistics demonstration, course
development and a guest lecture topic in one paragraph, with boosted
regression trees and the microclimate finding in the mentoring entry.
Academic: the complete course history with years, levels and the
verbatim lecture title one click down, and the student's abstract
preserved untouched.

**The post.** Recruiter: 14 co-authored accounts in the decade's
national bird review, stated in the first sentence. Peer: monitoring
evidence flowing into formal protection nominations, with the nomination
record linked. Academic: the correct book title, the publisher's
context, and all 14 citations rendered in full.

## 5. Checker and build

`prose_check` runs green over 53 files plus the stats include
(`prose-check-output-teaching-posts.txt`). The teaching entries reach
the page through Liquid, so the checker reads the 2 files directly, the
way it reads `_data/apps.yml`: per-file Tier B checks, dash scans
outside record regions, the shared 120-word section budget, and the join
of teaching words and row excerpts into the /research/ page budget
(DECISIONS 115). Every check newly applied to these files fired on a
seeded violation before landing clean; the 14-violation run is
`seeded-violations-teaching-posts.txt`. The build is warning-free
(`build-output-teaching-posts.txt`). CI runs the checker via the
existing workflow on this branch's pushes and PR.

**Coverage is now complete.** With this pass the checker covers every
markdown file the site serves as readable content: 10 pages, 16
projects, 12 publications, 12 talks, the post and the 2 teaching
entries, 53 files. What remains outside it remains by design: the
redirect stubs in `_pages/redirects/` render no prose, the 8 rows-only
talk bodies render as redirects (FINDINGS 17), the styleguide is
internal, and the project documents are excluded from the build. Phase
7's requirement that `prose_check` run clean across every markdown file
becomes true at this gate.

## 6. Phase 5 closes here

All 7 collections in the brief's Phase 5 list are done: `_pages`,
`_projects`, the apps copy, `_publications`, `_talks`, `_teaching` and
`_posts`. Remaining for Phase 6 (performance, SEO, accessibility, per
brief section 7): webp with fallback and explicit dimensions, the real
1200x630 `og:image`, JSON-LD (Person, ScholarlyArticle, CreativeWork,
SoftwareApplication), rewritten titles and meta descriptions,
accessibility (contrast, focus, heading order, alt text, skip link, the
iframe title), `robots.txt` and a clean `sitemap.xml`, the Lighthouse
and bundle targets, and the orphaned-asset sweep (FINDINGS 3). Open
owner calls carried in FINDINGS: 6, 8, 9, 13, 14, 18, 19.
