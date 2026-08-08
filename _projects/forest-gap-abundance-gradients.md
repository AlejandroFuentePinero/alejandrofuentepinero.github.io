---
title: "Forest gap effects on tropical birds"
excerpt: "Forest gaps changed which bird species lived where, while total numbers stayed level. One specialist, the Hill Blue Flycatcher, increased with gap size."
date: 2025-07-16
type: research
stack:
  - R
  - GLMs
redirect_from:
  - /datascience/projects/forest-gap-abundance-gradients/
---

Natural forest gaps reshaped which birds lived where, while total abundance stayed level between gaps and closed canopy. The evidence is 5 years of mist-netting in Thai lower montane rainforest: 1,148 captures, 81 species, paired sites. One gap specialist, the Hill Blue Flycatcher (Cyornis whitei), increased in abundance with total gap size. Most species showed no relationship with gap size at all.

I joined the study as the analyst. My part was the analytical framework: generalised linear models along a continuous gap gradient.

## Links

- **Paper page:** [The effect of forest gap dynamics on tropical rainforest birds](/research/forest-gap-birds-2025/)
- **Journal:** [Ecologica Montenegrina](https://doi.org/10.37828/em.2025.88.11)
- **PDF:** [Full text](/files/siri_et_al_2025_tropical_birds_forest_gap.pdf)

## Architecture

Generalised linear models relate each species' abundance to gap covariates: gap size and distance to edge. Error structures match the count data, and site-level terms absorb between-site variability. Residual diagnostics validated each model before we read any effect.

## The decision that was hard

Gap studies usually compare 2 categories, gap against closed canopy, and the category test came back flat here. The design question was whether to stop there. We modelled abundance along the continuous gap-size gradient instead, species by species. The gradient models found what the categories hid: assemblage change and a single strong specialist response.

## What was measured

The models produced effect sizes and confidence intervals per species along the gap gradient. Total abundance showed no difference between gaps and closed canopy. Assemblage composition shifted strongly with gaps, and the 5-year design also captured seasonal turnover from migration. Gaps of 130 to 1,020 square metres read as moderate disturbance: not highly detrimental, yet enough to affect sensitive species.

## What did not work

The headline effect was absent. Total bird abundance did not differ between gaps and closed canopy, and most species ignored gap size entirely. The signal lived one level down, in composition and in single species. An aggregate-only analysis would have called these forests indifferent to gaps and been wrong.

## Role

I designed the analytical framework, ran the models and validation, and interpreted the statistical outputs. I contributed to the manuscript.

## What this taught me about evaluation

Aggregate metrics hide the failures that matter. A system can hold its average while a subgroup collapses, exactly as total abundance held while assemblages changed. I now evaluate per slice before I trust any mean.
