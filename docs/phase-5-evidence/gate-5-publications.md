# Gate 5 evidence: the publications pass

Branch `refurb/phase-5-publications`, 2026-08-07. Scope: the 12 files in
`_publications/`, the publication layout (summary, media and project
blocks), the media engagement move off `/work/`, the 2023 GCB abstract
repair, the prose_check extension to the collection, the TERMINOLOGY
additions, and the DECISIONS (90 to 96) and FINDINGS (13, 14) entries.
The `_talks` summaries were not started.

## 1. Record integrity

Before anything else: the transform was verified programmatically against
git HEAD. All 11 untouched abstracts are byte-identical inside their new
record markers, the 2023 GCB body equals the journal text, and all 12
citation strings are unchanged:

```
Williams_delafuente_2021.md                   IDENTICAL       cit-ok
delafuente_2025_GCB.md                        IDENTICAL       cit-ok
delafuente_2026_NCC.md                        IDENTICAL       cit-ok
delafuente_et_al_2021_ecography.md            IDENTICAL       cit-ok
delafuente_et_al_2022_ddi_reshuffling.md      IDENTICAL       cit-ok
delafuente_et_al_2023_GCB.md                  REPAIRED-OK     cit-ok
delafuente_pacheco_2017_bosque.md             IDENTICAL       cit-ok
delafuente_williams_2022_possums_ddi.md       IDENTICAL       cit-ok
gallardo_et_al_2018.md                        IDENTICAL       cit-ok
herbivory_awt_2024_oecologia.md               IDENTICAL       cit-ok
iriarte_et_al_2021.md                         IDENTICAL       cit-ok
siri_et_al_2025.md                            IDENTICAL       cit-ok
```

### The 2023 GCB repair (FINDINGS 2, DECISIONS 92)

Journal text sourced from PubMed 36654193 and the Europe PMC record for
10.1111/gcb.16608 (Wiley blocks non-browser requests at the DOI); the two
publisher-supplied copies agree word for word. The complete word-level
diff of the site text against the journal text:

```
replace: site=['spe-cies']   -> journal=['species']
replace: site=['popu-lation'] -> journal=['population']
replace: site=['stress-ors'] -> journal=['stressors']
replace: site=['dy-namics']  -> journal=['dynamics']
doubled-space runs in site body: 41
```

Nothing else differs. The repaired body is the journal text byte for byte.

## 2. Metrics

Output of `python3 scripts/prose_check.py --metrics` committed as
`prose-check-output-publications.txt`. All 12 files are Tier B (25-word
sentences). The budget column is the 120-word summary ceiling; the
excerpt column is the 25-word index ceiling. Sentence counts cover the
excerpt and the summary together (the two checked prose fields).

| file | summary / 120 | excerpt / 25 | sentences | mean | longest | em+en dashes | banned hits |
|---|---|---|---|---|---|---|---|
| delafuente_pacheco_2017_bosque.md | 105 | 23 | 9 | 14.2 | 22 | 0 | 0 |
| gallardo_et_al_2018.md | 89 | 23 | 8 | 14.0 | 23 | 0 | 0 |
| delafuente_et_al_2021_ecography.md | 95 | 25 | 8 | 15.0 | 20 | 0 | 0 |
| Williams_delafuente_2021.md | 118 | 23 | 9 | 15.7 | 23 | 0 | 0 |
| iriarte_et_al_2021.md | 82 | 16 | 6 | 16.3 | 23 | 0 | 0 |
| delafuente_et_al_2022_ddi_reshuffling.md | 106 | 25 | 9 | 14.6 | 19 | 0 | 0 |
| delafuente_williams_2022_possums_ddi.md | 113 | 23 | 10 | 13.6 | 20 | 0 | 0 |
| delafuente_et_al_2023_GCB.md | 118 | 24 | 9 | 15.8 | 24 | 0 | 0 |
| herbivory_awt_2024_oecologia.md | 104 | 25 | 8 | 16.1 | 24 | 0 | 0 |
| delafuente_2025_GCB.md | 95 | 21 | 8 | 14.5 | 21 | 0 | 0 |
| siri_et_al_2025.md | 111 | 23 | 9 | 14.9 | 21 | 0 | 0 |
| delafuente_2026_NCC.md | 70 | 20 | 6 | 15.0 | 24 | 0 | 0 |

The possum paper reads 113 words: the CONTENT_MAP 7.2 worked example,
verbatim, matching its recorded metric exactly. No paragraph exceeds 4
sentences and no sentence exceeds the Tier B 25. Em dash count 0, en dash
count 0 (citation en dashes sit inside numeric ranges in record fields,
exempt per REFURB_BRIEF 6.2 rule 6), banned word hits 0, unexpanded
acronyms 0.

## 3. Side-by-side: index excerpts

Full line diffs are in the PR files view. Excerpts were topics; they are
now findings (brief 4.5: no questions, no unexpanded acronyms). The
summaries are new fields with no before state.

| paper | before | after |
|---|---|---|
| Bosque 2017 | "First description of the synchronous flowering of Chusquea montana in Puyehue National Park" | "Chusquea montana flowered and seeded massively and synchronously in Puyehue National Park in 2015. This paper is the first description of the event." |
| Rev. Chilena de Ornitologia 2018 | "Bird community seasonal variation in urban wetlands of South Chile." | "The urban wetlands of Llanquihue, southern Chile, hold 50 bird species and high diversity in every season, despite the pressure of the city." |
| Ecography 2021 | "Can habitat suitability derived from SDMs predict species abundance?" (a question, and an unexpanded acronym: the brief's own negative example) | "Environmental suitability predicted local abundance for 50 endemic rainforest species, explaining 55% of deviance on average. Cheap occurrence data can stand in for costly counts." |
| Plos One 2021 | "Rainforest birds in the Australian Wet Tropics are following the escalator to extinction." | "Upland rainforest birds in the Australian Wet Tropics declined by almost 50% in 17 years. The evidence supported protection nominations for 14 species." |
| Notas sobre Mamíferos Sudamericanos 2021 | "Mountain vizcachas occur much more north than once though. New records expand their range by 722 km." | "New photographic records would extend the northern range of Wolffsohn's viscacha in Chile by 722 km." |
| Diversity and Distributions 2022 (reshuffling) | "Climate-driven community re-shuffling in the mountains of the Australian Wet Tropics." | "Species climb at different speeds under warming, so mountain communities reshuffle. Local extinction rates rise with elevation, pointing to mass local extinctions of upland species." |
| Diversity and Distributions 2022 (possums) | "Rainforest ringtail possum are collapsing in the Australian Wet Tropics" | The CONTENT_MAP 7.1 entry, verbatim: "Ringtail possum populations in the Wet Tropics fall below viability thresholds by 2050 under forecast warming. Extreme heatwaves do most of the damage." |
| Global Change Biology 2023 | "The climatic drivers of long-term population changes in rainforest montane birds" (the title as topic) | "Warming and shifting rainfall drove opposite population trends in lowland and upland rainforest birds across 47 species. Cyclones and droughts had only marginal effects." |
| Oecologia 2024 | "Relationships between abiotic factors, foliage chemistry and herbivory in a tropical montane ecosystem." (the title as topic) | "Climate and geology, not single soil nutrients, shape foliage chemistry and insect herbivory in tropical montane rainforest. Tree species respond differently to the same resources." |
| Global Change Biology 2025 | "Climate-Induced Physiological Stress Drives Rainforest Mammal Population Declines." (the title as topic) | "Climate change drove rainforest possum declines through physiological stress: overheating and dehydration for one species, limits on foraging for the other." |
| Ecologica Montenegrina 2025 | "The effect of forest gap dynamics on tropical rainforest birds." (the title as topic) | "Natural forest gaps reshaped bird assemblages in Thai montane rainforest while total abundance stayed level. Only one gap specialist increased with gap size." |
| Nature Climate Change 2026 | "Mountains magnify mechanisms in climate change biology." (the title as topic) | "Mountains compress climates into short distances. That compression makes them natural laboratories for finding the mechanisms behind climate-driven biological change." |

The escalator-to-extinction phrase left the birds excerpt because index
entries cannot carry the PNAS link TERMINOLOGY requires on first use; the
phrase now lives, linked, in the reshuffling summary.

## 4. Media verification and routing (DECISIONS 93, 94)

Every linked headline was verified against its source before moving.

| recorded on /work/ | verified against | result |
|---|---|---|
| "Possums threatened by climate change" | James Cook University release (Wayback snapshot; the live page sits behind a bot wall) | exact match |
| "Aussi birds dissapearing due to warming" | narrominenewsonline.com.au | corrected: "Aussie birds disappearing due to warming" |
| "Global warming drives Wet Tropics possums species fromt their mountain homes." | abc.net.au article | corrected: "Global warming drives Wet Tropics possum species from their mountain homes" |
| grouped "Interview" link under the ABC entry | abc.net.au radio item | now carries its own published title: "Climate change drives possums from high altitude homes in Queensland's wet tropics" |
| "It's Easy to Hate Selfies. But Can They Also Be a Force for Good?" | nytimes.com (Wayback snapshot; the live page sits behind a captcha wall) | exact match |
| "Woody bamboo flowering in Puyehue National Park." | no link, Chilean print outlet | unverifiable, moved unaltered, surfaced as FINDINGS 13 |
| "Tropical rainforest research" | skyrail.com.au blog | corrected: "Tropical Rainforest Research in Education" |
| "70 national stories" | Mediaportal report (login-walled) | kept as the CONTENT_MAP 7.4 media line with its Mediaportal source |

Routing: possum paper takes the James Cook University release, the
Mediaportal report, both ABC pieces (they interview the owner about the
same possum-decline research) and the Skyrail Rainforest Foundation post.
The birds paper takes the Narromine story. The 2017 bamboo paper takes
the El Austral line. The New York Times photo credit has no relevant
paper and is the one entry remaining in the /work/ media block.

## 5. Audience check

One line per audience per paper (brief 2.2).

**Bosque 2017.** Recruiter: measure-first instinct visible in his first
professional role, documenting a rare event as it happened. Peer: the
sampling design (8 plots, 20 seed boxes) and the phenology comparison,
with the PDF for depth. Academic: the event reported with the paper's own
figures and units, abstract verbatim below.

**Urban wetland birds 2018.** Recruiter: seasonal survey work turned into
one clear conclusion about urban wetlands. Peer: what was counted, how
richness moved by season, and where the design details live. Academic:
richness, seasonality and similarity reported accurately, record intact.

**Abundance and niche theory 2021.** Recruiter: cheap data validated to
predict expensive data, a transferable result. Peer: the proxy-validation
logic behind the 55% figure, with the project page for the ensemble and
the spatial validation. Academic: the relationship stated with its
between-species caveat, no overclaim.

**Rainforest bird declines 2021.** Recruiter: a monitored decline that fed
14 protection nominations, one repeatable sentence. Peer: the evidence
scale (1,977 surveys, 114 sites) and effort-adjusted trend models, project
page one click away. Academic: the declines quantified as published, with
the nominations and the app as consequences.

**Mountain viscacha records 2021.** Recruiter: a minor record presented at
its true size. Peer: what photographic evidence can and cannot claim.
Academic: the 722 km extension with the paper's own hedge preserved.

**Community reshuffling 2022.** Recruiter: a large simulation with a
headline consequence, mass local extinctions of upland species. Peer: the
per-species dispersal design that makes reshuffling measurable at all.
Academic: the findings in the abstract's own structure, with the escalator
phrase linked to its PNAS source.

**Ringtail possum collapse 2022.** The CONTENT_MAP 7.5 check, unchanged:
the recruiter gets a sentence they can repeat in a phone screen, the peer
gets the method skeleton and a path to level 3, the academic gets the
finding stated accurately with the real abstract one click below.

**Montane bird climate drivers 2023.** Recruiter: he ranks causes rather
than just detecting change. Peer: joint estimation of 5 drivers with
detection separated, hard decision on the project page. Academic: the
marginal cyclone and drought result reported as published, above the
repaired abstract.

**Foliage chemistry and herbivory 2024.** Recruiter: careful causal
analysis with an honest negative result. Peer: pathway modelling over
pairwise regressions, and why geology confounds single nutrients.
Academic: the equivocal nutrient result kept equivocal.

**Physiological stress declines 2025.** Recruiter: mechanism-level
diagnosis that changes what managers do. Peer: the mechanistic-statistical
join and per-species causal routes, depth on the project page. Academic:
species-specific mechanisms reported exactly, Latin names as published.

**Forest gap birds 2025.** Recruiter: the average stayed flat and the
subgroup story mattered, an evaluation mindset in one line. Peer: gradient
models where the category test came back flat. Academic: captures, gap
sizes and the single specialist response as published.

**Mountains magnify mechanisms 2026.** Recruiter: a Nature-family venue in
the current record. Peer: the argument in 3 sentences without decoding a
comment format. Academic: the thesis stated without inflating a 3-page
piece into a study.

## 6. Checker and build

`prose_check` runs green over 38 files plus the stats include
(`prose-check-output-publications.txt`). The 8 new publication checks
(excerpt ceiling, excerpt question, summary budget, missing excerpt or
summary, body prose outside record markers, dashes in the checked fields,
banned words, sentence length) each fired on a seeded violation before
landing clean. The build is warning-free
(`build-output-publications.txt`). CI runs the checker via the existing
workflow on this branch's pushes and PR.
