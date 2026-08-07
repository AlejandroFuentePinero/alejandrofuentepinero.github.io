---
title: "Predicting abundance from environmental suitability"
excerpt: "An ensemble of 9 algorithms predicted local abundance from environmental suitability, explaining 55% of deviance on average across 50 rainforest species."
date: 2021-10-12
type: research
stack:
  - R
  - Ensemble ML
  - MaxEnt
redirect_from:
  - /datascience/projects/predicting-abundance-from-niche-theory/
---

Occurrence records are everywhere and counts are expensive, so we tested whether suitability can stand in for abundance. It can: models explained 55% of deviance on average across 50 endemic species of the Australian Wet Tropics. The fitted relationship predicts local abundance at fine resolution across each species' range.

Suitability came from an ensemble of 9 algorithms over presence-only data and climate and topography layers. Abundance came from 29 years of uninterrupted monitoring. Spatial cross-validation kept the predictive claims honest.

## Links

- **Paper page:** [Predicting species abundance by implementing the ecological niche theory](/research/abundance-niche-theory-2021/)
- **Journal:** [Ecography](https://doi.org/10.1111/ecog.05776)
- **Data:** [Dryad dataset](https://datadryad.org/dataset/doi:10.5061/dryad.0zpc866wv)

## Architecture

9 algorithms model each species' environmental suitability. The roster runs from surface range envelopes and classification trees to MaxEnt, boosted regression and neural networks. Random forests, regression splines, discriminant analysis and additive models complete the set. Their predictions combine into one ensemble suitability surface per species.

A second stage models observed abundance as a flexible function of that suitability and tests several link functions. Survey effort and detectability enter as model terms. Outputs are gridded abundance maps with uncertainty bands, plus tabular summaries for managers. Everything runs in R under version control.

## The decision that was hard

The claim only matters if it extrapolates, and standard cross-validation flatters spatial models. Nearby sites share environments, so random folds leak information and inflate accuracy. We validated across spatial folds instead, predicting into areas the model never saw. The 55% figure survived that design, which is why it is worth reporting.

## What was measured

The abundance-suitability relationship was strong for endemic species, and ensembles beat single algorithms on accuracy and calibration. Mean explained deviance reached 55% across taxa. Sensitivity analysis covered link functions and validation folds. The maps prioritised high-density areas the way managers need: at fine scale, with uncertainty attached.

## What did not work

The relationship is not uniform. Its strength varied between species, tied to intrinsic estimation biases the models cannot remove. For species with weak relationships, a suitability map is a hypothesis, not a shortcut to abundance. The paper says so rather than averaging the caveat away.

## Role

I led the study design, implemented the modelling and spatial validation, and produced the scripts and figures. I wrote the manuscript and coordinated the co-authors.

## What this taught me about evaluation

An offline metric is a proxy, and a proxy earns trust only through validation against the outcome it stands for. That is this paper in one line, and it is also retrieval evaluation in one line. Design the validation so the model cannot lean on what it already saw.
