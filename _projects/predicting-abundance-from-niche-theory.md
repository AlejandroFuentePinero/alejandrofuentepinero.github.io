---
title: "Predicting abundance from environmental suitability"
excerpt: "Maps of where a species can live predicted about half the variation in local numbers. The models faced 50 species and places they never saw."
date: 2021-10-12
type: research
stack:
  - R
  - Ensemble ML
  - MaxEnt
redirect_from:
  - /datascience/projects/predicting-abundance-from-niche-theory/
---

Records of where a species has been seen are everywhere, and counts of how many live there are expensive. So I tested whether a map of environmental suitability, built from the cheap records, can stand in for abundance. It can, within limits: the models explained 55% of the variation in local numbers on average across 50 species found only in the Australian Wet Tropics. The fitted relationship then predicts abundance at fine resolution across each species' range.

Suitability came from an ensemble of 9 algorithms trained on presence-only records with climate and terrain layers. Abundance came from 29 years of uninterrupted monitoring. Spatial cross-validation, which tests the model on places it never saw, kept the predictive claims honest.

## Links

- **Paper page:** [Predicting species abundance by implementing the ecological niche theory](/research/abundance-niche-theory-2021/)
- **Journal:** [Ecography](https://doi.org/10.1111/ecog.05776)
- **Data:** [Dryad dataset](https://datadryad.org/dataset/doi:10.5061/dryad.0zpc866wv)

## Architecture

Nine algorithms model each species' environmental suitability. The roster runs from surface range envelopes and classification trees to MaxEnt, boosted regression and neural networks, with random forests, regression splines, discriminant analysis and additive models completing the set. Their predictions combine into one ensemble suitability surface per species.

A second stage models observed abundance as a flexible function of that suitability and tests several link functions, the mathematical bridges between suitability and count. Survey effort and detectability enter as model terms. The outputs are gridded abundance maps with uncertainty bands, plus tabular summaries for managers. Everything runs in R under version control.

## The decision that was hard

The claim only matters if it extrapolates, and standard cross-validation flatters spatial models. Nearby sites share environments, so random folds leak information and inflate accuracy. I validated across spatial folds instead, predicting into areas the model never saw. The 55% figure survived that design, which is why it is worth reporting.

## What was measured

The abundance-suitability relationship was strong for endemic species, and ensembles beat single algorithms on both accuracy and calibration. Mean explained deviance, the share of variation the model accounts for, reached 55% across taxa. Sensitivity analysis covered link functions and validation folds. The maps prioritise high-density areas the way managers need: at fine scale, with uncertainty attached.

## What did not work

The relationship is not uniform. Its strength varied between species, tied to biases in the estimates that the models cannot remove. For a species with a weak relationship, a suitability map is a hypothesis, not a shortcut to abundance. The paper says so rather than averaging the caveat away.

## Role

I led the study design, implemented the modelling and spatial validation, and produced the scripts and figures. I wrote the manuscript and coordinated the co-authors.

## What this taught me about evaluation

An offline metric is a proxy, and a proxy earns trust only through validation against the outcome it stands for. That is this paper in one line, and it is also retrieval evaluation in one line. Design the validation so the model cannot lean on what it already saw.
