---
title: "Physiological stress and rainforest mammal declines"
excerpt: "2 possum species collapsed, each through a different mix of heat stress and foraging limits. A model chain traced the causes across 30 years."
date: 2025-05-05
type: research
stack:
  - R
  - JAGS
  - Biophysical models
redirect_from:
  - /datascience/projects/physiological-stress-climate-populations/
---

Climate change kills through mechanisms, and this project measured which ones. Two ringtail possum species in the Australian Wet Tropics have collapsed at lower elevations and at sites with poor food, but not for the same reason. I built a single Bayesian framework that links the microclimate inside a possum's roost to its physiological stress, its nutrition and finally its population over 30 years.

For the green ringtail possum, Pseudochirops archeri, overheating and dehydration cut survival while restricted foraging cut the number of young. For the lemuroid ringtail possum, Hemibelideus lemuroides, the limits on foraging dominated. The framework bridges 2 traditions: mechanistic models that simulate a species from its traits, and statistical models that infer it from counts.

## Links

- **Paper page:** [Climate-Induced Physiological Stress Drives Rainforest Mammal Population Declines](/research/physiological-stress-declines-2025/)
- **Journal:** [Global Change Biology](https://doi.org/10.1111/gcb.70215)
- **Data:** [Dryad dataset](https://datadryad.org/dataset/doi:10.5061/dryad.fxpnvx13n)

## Architecture

Four model components feed one inference. Microclimate models simulate the conditions inside roosting habitat: temperature, humidity and heat stress. Physiological models turn those conditions into an energy, water and heat budget for each species. Nutrition and vegetation models add food quality. A hierarchical population model, one that accounts for the chance of missing an animal in a count, then links everything to recruitment and survival.

The whole chain runs as one Bayesian framework in R and JAGS. Uncertainty flows from the microclimate all the way to the demography instead of being dropped at each hand-off. The same joint fit supports scenario testing for management interventions.

## The decision that was hard

Ecology offers 2 model families and a habit of choosing one. Mechanistic models predict from first principles and often miss what populations actually do. Statistical models fit the counts and cannot say why. I joined them: the mechanistic estimates of stress became the covariates of an open population model, and the whole thing was fitted jointly.

The join is the hard part, because every component has to pass its uncertainty to the next rather than a single best guess. The reward is causal language that a correlation could never earn.

## What was measured

The framework quantified 30 years of population dynamics against species-specific estimates of temperature stress, water stress and foraging limitation. It separated direct effects from indirect ones and sized each mechanism's contribution to the decline. Fully integrated forecasts then supported scenario testing for interventions.

## What did not work

One shared mechanism did not explain both species. Direct heat stress, the obvious suspect, underperformed for the lemuroid ringtail. The model pointed instead to climate-driven limits on how much the animals could forage. A single-species story, applied to both, would have prescribed the wrong intervention for one of them.

## Role

I designed the multi-component workflow, developed each model and integrated them into the unified framework. I ran the fitting, validation and scenario testing, and wrote the manuscript.

## What this taught me about evaluation

It is cheap to know that a system fails, and expensive to learn why. The why is what changes the fix. This project is the research version of error analysis: decompose the failure into mechanisms and size each one. Intervene where the evidence points, and expect different causes in things that look alike.
