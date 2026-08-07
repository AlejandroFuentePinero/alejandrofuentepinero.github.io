# MIGRATIONS.md: the redirect record

Every URL the built site served before the refurbishment, and what happens to it. The authoritative mapping is CONTENT_MAP.md section 2; this file adds wiring status. Excluded from the Jekyll build.

Status values:

- **wired (Phase 2)**: the redirect exists now and was tested locally in Phase 2.
- **interim (Phase 2)**: the old URL redirects now to a current URL so nothing 404s; Phase 4 re-points it to the final target when that page exists.
- **Phase 4**: the final target does not exist yet; the redirect is wired when Phase 4 builds the page.
- **keep**: the URL survives, no redirect needed.
- **gone**: deleted without redirect, approved at Gate 0 (template demos, plumbing and orphans with zero external references).

Mechanism notes, from CONTENT_MAP 2.1:

- `jekyll-redirect-from` is configured and Pages-whitelisted. Plain targets get a `redirect_from` entry on the destination page.
- Targets with an anchor (for example `/research/#talks`) need a stub file with `redirect_to`, created in Phase 4.
- Publication and talk permalinks have no trailing slash, so each old URL must resolve in both its extensionless and `.html` form. The Phase 2 tests cover both.
- The two malformed publication URLs carry `redirect_from` entries in both the percent-encoded and the literal-space form. Tested in Phase 2, evidence in the phase PR.

## 1. Top-level and section pages

| Current URL | Target | Status |
|---|---|---|
| `/` | rewritten in place | keep |
| `/404.html` | restyled in Phase 4 | keep |
| `/sitemap/` | rewritten in Phase 4 | keep |
| `/terms/` | light rewrite in Phase 5 | keep |
| `/about/` | `/` | wired (pre-existing, unchanged) |
| `/about.html` | `/` | wired (pre-existing, unchanged) |
| `/academic/` | `/research/` | Phase 4 |
| `/academic/cv/` | `/work/` | Phase 4 |
| `/cv/` | `/academic/cv/` today, `/work/` at Phase 4 | interim (pre-existing, re-point in Phase 4) |
| `/resume` | `/academic/cv/` today, `/work/` at Phase 4 | interim (pre-existing, re-point in Phase 4) |
| `/academic/publications/` | `/research/#publications` (stub) | Phase 4 |
| `/academic/talks/` | `/research/#talks` (stub) | Phase 4 |
| `/academic/teaching/` | `/research/#teaching` (stub) | Phase 4 |
| `/academic/book_chapter/` | `/research/#book-chapters` (stub) | Phase 4 |
| `/academic/grants_awards/` | `/work/#grants-awards` (stub) | Phase 4 |
| `/academic/threatened_species/` | `/research/threatened-species/` | Phase 4 |
| `/datascience/` | `/projects/` | Phase 4 |
| `/datascience/projects/` | `/projects/` | Phase 4 |
| `/datascience/skills/` | `/#skills` (stub) | Phase 4 |
| `/datascience/education/` | `/work/#education` (stub) | Phase 4 |
| `/datascience/communication/` | `/apps/` | Phase 4 |
| `/portfolio/grants/` | `/work/#grants-awards` (stub) | Phase 4 |
| `/portfolio/awards/` | `/work/#grants-awards` (stub) | Phase 4 |
| `/teaching/james_cook_university/` | `/research/#teaching` (stub) | Phase 4 |
| `/teaching/mentoring/` | `/research/#teaching` (stub) | Phase 4 |
| `/posts/2012/08/blog-post-1/` | `/posts/action-plan-australian-birds-2021/` | wired (Phase 2) |

## 2. Projects: 18 old URLs, 16 new pages

All Phase 4, wired when `/projects/` and its pages are built. Old URLs live under `/datascience/projects/`.

| Current URL (`/datascience/projects/...`) | New URL (`/projects/...`) | Status |
|---|---|---|
| `7ph-graph/` | `7ph-graph/` | Phase 4 |
| `ai-jie/` | `ai-jie/` | Phase 4 |
| `digital-twin/` | `digital-twin/` | Phase 4 |
| `job_intelligence_engine/` | `job-intelligence-engine/` | Phase 4 |
| `llm-engineering-lab/` | `llm-engineering-lab/` | Phase 4 |
| `mlb_analytics_sql/` | `mlb-analytics-sql/` | Phase 4 |
| `python_eda_mini_projects/` | `python-labs/` (merged) | Phase 4 |
| `python-ML-projects/` | `python-labs/` (merged) | Phase 4 |
| `python_oop_minisystems/` | `python-labs/` (merged) | Phase 4 |
| `bird-elevational-migration/` | `bird-elevational-migration/` | Phase 4 |
| `dynamic-community-reshuffling/` | `dynamic-community-reshuffling/` | Phase 4 |
| `ecosystem-pathway-cascades/` | `ecosystem-pathway-cascades/` | Phase 4 |
| `forecasting-popviability-ringtails/` | `forecasting-popviability-ringtails/` | Phase 4 |
| `forest-gap-abundance-gradients/` | `forest-gap-abundance-gradients/` | Phase 4 |
| `heightened-protection-bird-trends/` | `heightened-protection-bird-trends/` | Phase 4 |
| `physiological-stress-climate-populations/` | `physiological-stress-climate-populations/` | Phase 4 |
| `predicting-abundance-from-niche-theory/` | `predicting-abundance-from-niche-theory/` | Phase 4 |
| `spatiotemporal-bird-climate-impacts/` | `spatiotemporal-bird-climate-impacts/` | Phase 4 |

## 3. Publications: 12 old URLs, 12 new pages

The two malformed URLs moved in Phase 2; the other 10 move in Phase 4.

| Current URL (`/publication/...`) | New URL (`/research/...`) | Status |
|---|---|---|
| `delafuente_pacheco_2017_bosque` | `chusquea-flowering-2017/` | Phase 4 |
| `gallardo_et_al_2018` | `urban-wetland-birds-2018/` | Phase 4 |
| `delafuente_et_al_2021_ecography` | `abundance-niche-theory-2021/` | Phase 4 |
| `Williams_delafuente_2021_plosone` | `rainforest-bird-declines-2021/` | Phase 4 |
| `SAREM_NotasMamSud_12-2021_Iriarte` | `mountain-vizcacha-records-2021/` | Phase 4 |
| reshuffling paper, encoded and literal forms (CONTENT_MAP 2.5) | `community-reshuffling-2022/` | wired (Phase 2) |
| possums paper, encoded and literal forms (CONTENT_MAP 2.5) | `ringtail-possum-collapse-2022/` | wired (Phase 2) |
| `delafuente_et_al_2023_GCB` | `montane-bird-climate-drivers-2023/` | Phase 4 |
| `delafuente_etal_2024_oecologia` | `foliage-chemistry-herbivory-2024/` | Phase 4 |
| `delafuente_2025_gcb` | `physiological-stress-declines-2025/` | Phase 4 |
| `siri_2025` | `forest-gap-birds-2025/` | Phase 4 |
| `delafuente_2026_ncc` | `mountains-magnify-mechanisms-2026/` | Phase 4 |

The exact old strings for the two wired rows, each covered in encoded and literal form, with and without `.html`:

```
/publication/Diversity%20and%20Distributions%20-%202022%20-%20de%20la%20Fuente%20-%20Predicted%20alteration%20of%20vertebrate%20communities%20in%20response%20to
/publication/Diversity and Distributions - 2022 - de la Fuente - Predicted alteration of vertebrate communities in response to
/publication/Diversity%20and%20Distributions%20-%202022%20-%20Fuente%20-%20Climate%20change%20threatens%20the%20future%20of%20rain%20forest%20ringtail%20possums%20by%202050
/publication/Diversity and Distributions - 2022 - Fuente - Climate change threatens the future of rain forest ringtail possums by 2050
```

## 4. Talks: 15 old URLs

The three absorbed talk URLs are wired now so they never 404; they re-point to their final targets in Phase 4 with the rest.

| Current URL (`/talks/...`) | Final target | Status |
|---|---|---|
| `ZENQ_2023` | `/research/songs-of-disappearance-2023/` (kept page) | Phase 4 |
| `esa_scbo_2022` | `/research/elevational-shifts-talk-2022/` (kept page) | Phase 4 |
| `esa_2021_poster` | `/research/elevational-shifts-talk-2022/` | interim (Phase 2): `/talks/esa_scbo_2022` |
| `PhD_exit_seminar` | `/research/phd-exit-seminar-2024/` (kept page) | Phase 4 |
| `IBRC_2025` | `/research/flying-fox-heat-2025/` (kept page) | Phase 4 |
| `cbcs_brisbane_2023` | `/research/#talks` (stub) | Phase 4 |
| `chilean_congress_ornithology_2017` | `/research/#talks` (stub) | Phase 4 |
| `coder_nmix` | `/research/#talks` (stub) | Phase 4 |
| `melbourne_2022` | `/research/#talks` (stub) | interim (Phase 2): `/talks/zenq_2022` |
| `NFFF_2025` | `/research/#talks` (stub) | Phase 4 |
| `tess_2021` | `/research/#talks` (stub) | Phase 4 |
| `TESS_2023` | `/research/#talks` (stub) | Phase 4 |
| `tropical_bes_2021` | `/research/#talks` (stub) | interim (Phase 2): `/talks/tess_2021` |
| `wtma_workshop_2024` | `/research/#talks` (stub) | Phase 4 |
| `zenq_2022` | `/research/#talks` (stub) | Phase 4 |

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
