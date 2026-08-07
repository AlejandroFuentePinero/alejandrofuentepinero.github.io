---
title: "Rainforest bird declines"
excerpt: "17 years of bird monitoring showed upland populations nearly halving. The evidence supported protection nominations for 14 rainforest species."
date: 2021-12-22
type: research
stack:
  - R
  - GLMs
  - Shiny
redirect_from:
  - /datascience/projects/heightened-protection-bird-trends/
---

17 years of standardised bird monitoring showed upland rainforest populations nearly halving. The evidence supported protection nominations for 14 rainforest species under national and international frameworks. It also went live as an interactive app anyone can query.

The record covers 1,977 surveys at 114 sites in the Australian Wet Tropics, from sea level to 1,500 m. Trend models for 42 species, adjusted for survey effort, quantified change from 2000 to 2016. Mid and high elevation species declined by more than 40% at their lower edges. Upland specialists and regional endemics lost almost 50%.

## Links

- **Paper page:** [Long-term changes in populations of rainforest birds](/research/rainforest-bird-declines-2021/)
- **Journal:** [Plos One](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0254307)
- **Live app:** [Bird population trends explorer](https://alejandrodelafuente.shinyapps.io/BirdsPopTrendAWT/)

## Architecture

The pipeline harmonises multi-source count data into one time series per species and site. Generalised linear models estimate each species' trend, with covariates for survey effort and habitat change. The effort adjustment matters most: a decline must be a decline, not a change in who searched.

A Shiny app publishes the trends interactively. Managers and policymakers can explore each trajectory, its confidence interval and the nomination thresholds. The whole analysis runs in R under version control.

## The decision that was hard

A nomination document needs one defensible number per species, but monitoring data offer many candidate analyses. We modelled each species separately, with explicit covariate adjustment, instead of pooling a community index. A pooled index reads impressively and hides which species is collapsing. Per-species models are noisier, and they name the species a nomination must name.

## What was measured

Most mid and high elevation species lost more than 40% of local abundance at their lower edges. Lowland species expanded uphill, increasing by up to 190% in higher areas. Upland specialists and regional endemics declined by almost 50%.

14 species carried enough evidence to support nominations for heightened protection. The nominations ran under national threatened species lists and through the International Union for Conservation of Nature (IUCN).

## Role

I designed and ran the analytical workflow, harmonised the time series, and built and deployed the Shiny app. I drafted the manuscript and coordinated the policy communication.

## What this taught me about evaluation

An analysis that feeds a decision must survive hostile review, so every adjustment has to be visible and defensible. I hold engineering evaluations to the same bar: publish the method beside the metric. The Shiny app was the other lesson. Results people can interrogate earn more trust than results people must accept.
