# MIGRATIONS.md: the redirect record

Every URL the built site served before the refurbishment, and what happens to it. The authoritative mapping is CONTENT_MAP.md section 2; this file adds wiring status. Excluded from the Jekyll build.

Status values:

- **wired (Phase 2)** / **wired (Phase 4)**: the redirect exists and was tested locally in the named phase.
- **keep**: the URL survives, no redirect needed.
- **gone**: deleted without redirect, approved at Gate 0 (template demos, plumbing and orphans with zero external references).

Mechanism notes, from CONTENT_MAP 2.1:

- `jekyll-redirect-from` is configured and Pages-whitelisted. Plain targets get a `redirect_from` entry on the destination page.
- Targets with an anchor (for example `/research/#talks`) need a stub file with `redirect_to`; the stubs live in `_pages/redirects/`.
- Publication and talk permalinks have no trailing slash, so each old URL must resolve in both its extensionless and `.html` form. The Phase 2 tests cover both.
- The two malformed publication URLs carry `redirect_from` entries in both the percent-encoded and the literal-space form. Tested in Phase 2, evidence in the phase PR.

## 1. Top-level and section pages

| Current URL | Target | Status |
|---|---|---|
| `/` | rewritten in place | keep |
| `/404.html` | restyled (Phase 4) | keep |
| `/sitemap/` | rewritten (Phase 4) | keep |
| `/terms/` | light rewrite in Phase 5 | keep |
| `/contact/` | `/` (stub) | wired (2026-08-08, page retired: the footer carries the contact links on every page) |
| `/about/` | `/` | wired (pre-existing, unchanged) |
| `/about.html` | `/` | wired (pre-existing, unchanged) |
| `/academic/` | `/research/` | wired (Phase 4) |
| `/academic/cv/` | `/work/` | wired (Phase 4) |
| `/cv/` | `/work/` | wired (Phase 4, re-pointed) |
| `/resume` | `/work/` | wired (Phase 4, re-pointed) |
| `/academic/publications/` | `/research/#publications` (stub) | wired (Phase 4) |
| `/academic/talks/` | `/research/#talks` (stub) | wired (Phase 4) |
| `/academic/teaching/` | `/research/#teaching` (stub) | wired (Phase 4) |
| `/academic/book_chapter/` | `/research/#book-chapters` (stub) | wired (Phase 4) |
| `/academic/grants_awards/` | `/work/#grants-awards` (stub) | wired (Phase 4) |
| `/academic/threatened_species/` | `/research/threatened-species/` | wired (Phase 4) |
| `/datascience/` | `/projects/` | wired (Phase 4) |
| `/datascience/projects/` | `/projects/` | wired (Phase 4) |
| `/datascience/skills/` | `/skills/` | wired (Phase 4, re-pointed 2026-08-08 to the new page; the stub retired for a `redirect_from` entry) |
| `/datascience/education/` | `/skills/#education` (stub) | wired (Phase 4, re-pointed 2026-08-08 to the new page) |
| `/datascience/communication/` | `/apps/` | wired (Phase 4) |
| `/portfolio/grants/` | `/work/#grants-awards` (stub) | wired (Phase 4) |
| `/portfolio/awards/` | `/work/#grants-awards` (stub) | wired (Phase 4) |
| `/teaching/james_cook_university/` | `/research/#teaching` (stub) | wired (Phase 4) |
| `/teaching/mentoring/` | `/research/#teaching` (stub) | wired (Phase 4) |
| `/posts/2012/08/blog-post-1/` | `/research/#book-chapters` (stub) | wired (Phase 2 to the post; re-pointed 2026-08-08 when the post retired) |
| `/posts/action-plan-australian-birds-2021/` | `/research/#book-chapters` (stub) | wired (2026-08-08, the post retired into the chapter rows) |

## 2. Projects: 18 old URLs, 16 new pages

All wired in Phase 4 via `redirect_from` on the new pages. Old URLs live under `/datascience/projects/`.

| Current URL (`/datascience/projects/...`) | New URL (`/projects/...`) | Status |
|---|---|---|
| `7ph-graph/` | `7ph-graph/` | wired (Phase 4) |
| `ai-jie/` | `ai-jie/` | wired (Phase 4) |
| `digital-twin/` | `digital-twin/` | wired (Phase 4) |
| `job_intelligence_engine/` | `job-intelligence-engine/` | wired (Phase 4) |
| `llm-engineering-lab/` | `llm-engineering-lab/` | wired (Phase 4) |
| `mlb_analytics_sql/` | `mlb-analytics-sql/` | wired (Phase 4) |
| `python_eda_mini_projects/` | `python-labs/` (merged) | wired (Phase 4) |
| `python-ML-projects/` | `python-labs/` (merged) | wired (Phase 4) |
| `python_oop_minisystems/` | `python-labs/` (merged) | wired (Phase 4) |
| `bird-elevational-migration/` | `bird-elevational-migration/` | wired (Phase 4) |
| `dynamic-community-reshuffling/` | `dynamic-community-reshuffling/` | wired (Phase 4) |
| `ecosystem-pathway-cascades/` | `ecosystem-pathway-cascades/` | wired (Phase 4) |
| `forecasting-popviability-ringtails/` | `forecasting-popviability-ringtails/` | wired (Phase 4) |
| `forest-gap-abundance-gradients/` | `forest-gap-abundance-gradients/` | wired (Phase 4) |
| `heightened-protection-bird-trends/` | `heightened-protection-bird-trends/` | wired (Phase 4) |
| `physiological-stress-climate-populations/` | `physiological-stress-climate-populations/` | wired (Phase 4) |
| `predicting-abundance-from-niche-theory/` | `predicting-abundance-from-niche-theory/` | wired (Phase 4) |
| `spatiotemporal-bird-climate-impacts/` | `spatiotemporal-bird-climate-impacts/` | wired (Phase 4) |

## 3. Publications: 12 old URLs, 12 new pages

The two malformed URLs moved in Phase 2; the other 10 moved in Phase 4.

| Current URL (`/publication/...`) | New URL (`/research/...`) | Status |
|---|---|---|
| `delafuente_pacheco_2017_bosque` | `chusquea-flowering-2017/` | wired (Phase 4) |
| `gallardo_et_al_2018` | `urban-wetland-birds-2018/` | wired (Phase 4) |
| `delafuente_et_al_2021_ecography` | `abundance-niche-theory-2021/` | wired (Phase 4) |
| `Williams_delafuente_2021_plosone` | `rainforest-bird-declines-2021/` | wired (Phase 4) |
| `SAREM_NotasMamSud_12-2021_Iriarte` | `mountain-vizcacha-records-2021/` | wired (Phase 4) |
| reshuffling paper, encoded and literal forms (CONTENT_MAP 2.5) | `community-reshuffling-2022/` | wired (Phase 2) |
| possums paper, encoded and literal forms (CONTENT_MAP 2.5) | `ringtail-possum-collapse-2022/` | wired (Phase 2) |
| `delafuente_et_al_2023_GCB` | `montane-bird-climate-drivers-2023/` | wired (Phase 4) |
| `delafuente_etal_2024_oecologia` | `foliage-chemistry-herbivory-2024/` | wired (Phase 4) |
| `delafuente_2025_gcb` | `physiological-stress-declines-2025/` | wired (Phase 4) |
| `siri_2025` | `forest-gap-birds-2025/` | wired (Phase 4) |
| `delafuente_2026_ncc` | `mountains-magnify-mechanisms-2026/` | wired (Phase 4) |

The exact old strings for the two wired rows, each covered in encoded and literal form, with and without `.html`:

```
/publication/Diversity%20and%20Distributions%20-%202022%20-%20de%20la%20Fuente%20-%20Predicted%20alteration%20of%20vertebrate%20communities%20in%20response%20to
/publication/Diversity and Distributions - 2022 - de la Fuente - Predicted alteration of vertebrate communities in response to
/publication/Diversity%20and%20Distributions%20-%202022%20-%20Fuente%20-%20Climate%20change%20threatens%20the%20future%20of%20rain%20forest%20ringtail%20possums%20by%202050
/publication/Diversity and Distributions - 2022 - Fuente - Climate change threatens the future of rain forest ringtail possums by 2050
```

## 4. Talks: 15 old URLs

All 15 wired in Phase 4: the four kept pages carry `redirect_from`, the rest redirect to `/research/#talks`.

| Current URL (`/talks/...`) | Final target | Status |
|---|---|---|
| `ZENQ_2023` | `/research/songs-of-disappearance-2023/` (kept page) | wired (Phase 4) |
| `esa_scbo_2022` | `/research/elevational-shifts-talk-2022/` (kept page) | wired (Phase 4) |
| `esa_2021_poster` | `/research/elevational-shifts-talk-2022/` | wired (Phase 4, direct to the kept page) |
| `PhD_exit_seminar` | `/research/phd-exit-seminar-2024/` (kept page) | wired (Phase 4) |
| `IBRC_2025` | `/research/flying-fox-heat-2025/` (kept page) | wired (Phase 4) |
| `cbcs_brisbane_2023` | `/research/#talks` (stub) | wired (Phase 4) |
| `chilean_congress_ornithology_2017` | `/research/#talks` (stub) | wired (Phase 4) |
| `coder_nmix` | `/research/#talks` (stub) | wired (Phase 4) |
| `melbourne_2022` | `/research/#talks` (stub) | wired (Phase 4, stub) |
| `NFFF_2025` | `/research/#talks` (stub) | wired (Phase 4) |
| `tess_2021` | `/research/#talks` (stub) | wired (Phase 4) |
| `TESS_2023` | `/research/#talks` (stub) | wired (Phase 4) |
| `tropical_bes_2021` | `/research/#talks` (stub) | wired (Phase 4, stub) |
| `wtma_workshop_2024` | `/research/#talks` (stub) | wired (Phase 4) |
| `zenq_2022` | `/research/#talks` (stub) | wired (Phase 4) |

## 5. Deleted without redirect, per the Gate 0 approvals

| URL | Why no redirect | Status |
|---|---|---|
| `/archive-layout-with-content/` | Template demo | gone (Phase 2) |
| `/non-menu-page/`, `/nmp/`, `/nmp.html` | Template demo and its own redirects | gone (Phase 2) |
| `/page-archive/` | Template demo | gone (Phase 2) |
| `/collection-archive/` | Template demo | gone (Phase 2) |
| `/categories/`, `/tags/` | Template taxonomy plumbing; the post layout links them until the Phase 4 layout swap | gone (Phase 4) |
| `/talkmap.html`, `/talkmap/map.html` | Orphaned behind `talkmap_link: false` | gone (Phase 2) |
| `/markdown_generator/` | Upstream tooling directory | gone (Phase 2) |
| `/md/`, `/markdown.html` | Template leftovers on the threatened species page | gone (Phase 2) |
| `/wordpress/blog-posts/` | Template leftover on the book chapters page | gone (Phase 2) |

## 6. Project documents

`/AUDIT/` and `/REFURB_BRIEF/` rendered as pages because root markdown builds by default. All six project documents (REFURB_BRIEF.md, AUDIT.md, POSITIONING.md, CONTENT_MAP.md, DECISIONS.md, MIGRATIONS.md) are now on the `_config.yml` exclude list. No redirects: they were never site content.
