---
title: "Physiological stress and rainforest mammal declines"
excerpt: "A model chain from microclimate to physiology to demography showed heat stress and foraging limits driving possum declines, species by species."
date: 2025-05-05
type: research
stack:
  - R
  - JAGS
  - Biophysical models
redirect_from:
  - /datascience/projects/physiological-stress-climate-populations/
---

Climate change kills through mechanisms, and this project measured which ones. A unified Bayesian framework linked microclimate, physiological stress, nutrition and population dynamics for 2 rainforest ringtail possums over 30 years. Both species collapsed at lower elevations and in low-nutrition sites, but through different causal routes.

For Pseudochirops archeri, overheating and dehydration cut survival, and restricted foraging cut recruitment. For Hemibelideus lemuroides, foraging constraints dominated. The framework bridges mechanistic models, which simulate species from traits, and statistical models, which infer them from counts.

## Links

- **Paper page:** [Climate-Induced Physiological Stress Drives Rainforest Mammal Population Declines](/research/physiological-stress-declines-2025/)
- **Journal:** [Global Change Biology](https://doi.org/10.1111/gcb.70215)
- **Data:** [Dryad dataset](https://datadryad.org/dataset/doi:10.5061/dryad.fxpnvx13n)

## Architecture

4 model components feed one inference. Microclimate models simulate conditions inside roosting habitat: temperature, humidity, thermal stress. Physiological models turn those conditions into energy, water and heat budgets per species. Nutritional and vegetation models add food quality, and a hierarchical population model links everything to recruitment and survival.

The population model accounts for imperfect detection in the count data. The whole chain runs as one Bayesian framework in R and JAGS, so uncertainty propagates from microclimate to demography. Joint inference also supports scenario testing for management interventions.

## The decision that was hard

The field offers 2 model families and a habit of choosing one. Mechanistic models predict from first principles and often miss what populations actually do. Statistical models fit the counts and cannot say why. We joined them: mechanistic stress estimates became the covariates of an open population model, fitted jointly.

The join is the hard part: every component must hand its uncertainty to the next instead of a point estimate. The reward is causal language a correlation cannot earn.

## What was measured

The framework quantified 30 years of population dynamics against species-specific estimates of temperature stress, water stress and foraging limitation. It separated direct effects from indirect ones and sized each mechanism's contribution to decline. Fully integrated forecasts then supported scenario testing for interventions.

## What did not work

One shared mechanism did not explain both species. Direct heat stress, the obvious suspect, underperformed for Hemibelideus lemuroides. The model pointed to climate-driven limits on foraging activity instead. A single-species story, applied to both, would have prescribed the wrong intervention for one of them.

## Role

I designed the multi-component workflow, developed each model and integrated them into the unified framework. I ran the fitting, validation and scenario testing, and wrote the manuscript.

## What this taught me about evaluation

It is cheap to know that a system fails, and expensive to learn why. The why is what changes the fix. This project is the research version of error analysis: decompose the failure into mechanisms and size each one. Intervene where the evidence points, and expect different causes in things that look alike.
