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

When a tree falls in a rainforest, the gap it leaves changes which birds live there, even though the total number of birds stays the same. Five years of mist-netting in a Thai lower montane rainforest showed it: 1,148 captures of 81 species across paired sites in gaps and under closed canopy. Total abundance did not differ between the 2. The mix of species did, and one gap specialist, the Hill Blue Flycatcher (Cyornis whitei), grew more abundant as gaps grew larger. Most species ignored gap size.

I joined the study as the analyst. My part was the analytical framework: generalised linear models, which relate counts to explanatory variables, fitted along a continuous gap gradient.

## Links

- **Paper page:** [The effect of forest gap dynamics on tropical rainforest birds](/research/forest-gap-birds-2025/)
- **Journal:** [Ecologica Montenegrina](https://doi.org/10.37828/em.2025.88.11)
- **PDF:** [Full text](/files/siri_et_al_2025_tropical_birds_forest_gap.pdf)

## Architecture

Generalised linear models relate each species' abundance to 2 gap covariates: the size of the gap and the distance to its edge. The error structure matches count data, and site-level terms absorb the differences between sites. Residual diagnostics validated each model before I read any effect.

## The decision that was hard

Gap studies usually compare 2 categories, gap against closed canopy, and here the category test came back flat. The design question was whether to stop there. Instead I modelled abundance along the continuous gap-size gradient, species by species. The gradient models found what the categories hid: a change in the assemblage and one strong specialist response.

## What was measured

The models produced effect sizes and confidence intervals per species along the gap gradient. Total abundance showed no difference between gaps and closed canopy. The make-up of the assemblage shifted strongly with gaps, and the 5-year design also captured seasonal turnover from migration. Gaps of 130 to 1,020 square metres read as moderate disturbance: not highly detrimental, yet enough to affect sensitive species.

## What did not work

The headline effect was absent. Total bird abundance did not differ between gaps and closed canopy, and most species ignored gap size entirely. The signal lived one level down, in the make-up of the assemblage and in single species. An aggregate-only analysis would have called these forests indifferent to gaps, and been wrong.

## Role

I designed the analytical framework, ran the models and validation, and interpreted the statistical outputs. I contributed to the manuscript.

## What this taught me about evaluation

Aggregate metrics hide the failures that matter. A system can hold its average while a subgroup collapses, exactly as total abundance held while assemblages changed. I now evaluate per slice before I trust any mean.
