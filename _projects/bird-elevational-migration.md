---
title: "Seasonal altitudinal migration in rainforest birds"
excerpt: "Rainforest birds move uphill each summer and back down each winter. 16 years of counts make it the first system-wide measure of this movement."
date: 2025-09-15
type: research
stack:
  - R
  - JAGS
  - N-mixture models
redirect_from:
  - /datascience/projects/bird-elevational-migration/
---

Rainforest bird communities in the Australian Wet Tropics breathe with the seasons. Most species shift uphill in summer and downhill in winter. Total abundance peaks in the lowlands in winter and in the uplands in summer. This is the first system-wide quantification of partial altitudinal migration in tropical rainforest birds.

The evidence is 16 years of bird counts, 2000 to 2016, across more than 100 sites and full elevational gradients. A hierarchical Bayesian model estimates abundance and detection jointly and isolates the seasonal signal. The manuscript is under review at Diversity and Distributions.

## Links

- **Manuscript:** under review at Diversity and Distributions

## Architecture

An N-mixture model separates true abundance from detection, fitted in JAGS with structured priors and multi-level random effects. Season enters centred: winter at minus 0.5, summer at plus 0.5. Altitudinal migration is then a single term, the season by elevation interaction, readable directly as uphill or downhill movement.

Species-level random slopes pool information across mountains, which raises power for scarce species. Posterior predictions reconstruct abundance across continuous elevation bands per season. Derived metrics quantify the redistribution: centroid shift, range shift and turnover, computed with the vegan and betapart packages in R.

## The decision that was hard

Partial migration is subtle: only part of a population moves, and imperfect detection can fake the signal either way. The tempting analysis compares 2 seasonal abundance maps and reads the difference as movement. We defined migration inside the model instead, as the season by elevation interaction. The model estimates the effect jointly with detection, so a quiet bird in winter is not a bird that left.

## What was measured

Most species show predictable seasonal redistribution, uphill in summer and downhill in winter. The individual shifts aggregate into a community-level pattern of seasonal breathing across the gradient. Species differ: narrow-range specialists barely move, while generalists track resources widely. Model checking used posterior predictive checks, convergence diagnostics and cross-season model comparisons.

## Role

I designed the model architecture, engineered the data and prediction pipelines, ran the Bayesian analysis and wrote the manuscript.

## What this taught me about evaluation

Define the effect as a term in the model before fitting, not as a story after. I apply the same rule to engineering evaluations: pick the metric before the run, then let it disappoint you. Effects that only appear after flexible post-processing usually are not effects.
