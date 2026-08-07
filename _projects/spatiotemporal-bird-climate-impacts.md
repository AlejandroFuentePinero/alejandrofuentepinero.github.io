---
title: "Climatic drivers of rainforest bird change"
excerpt: "Warming and shifting rainfall drove opposite trends in lowland and upland birds across 47 species. Cyclones and droughts had only marginal effects."
date: 2023-01-18
type: research
stack:
  - R
  - JAGS
  - Remote sensing
redirect_from:
  - /datascience/projects/spatiotemporal-bird-climate-impacts/
---

Not every climate driver matters equally, and this study measured which ones move rainforest bird populations. Across 47 species in the Australian Wet Tropics, warming and changing rainfall drove the strongest responses. The directions flip by elevation. Lowland populations gained from rising temperature and precipitation, while upland species declined under the same drivers.

Hierarchical population models separated detection from true change, 2000 to 2016. Heatwaves cut lowland populations, matching where those events concentrate. Cyclones and droughts, the expected disasters, had marginal effects on community change.

## Links

- **Paper page:** [The climatic drivers of long-term population changes in rainforest montane birds](/research/montane-bird-climate-drivers-2023/)
- **Journal:** [Global Change Biology](https://onlinelibrary.wiley.com/doi/full/10.1111/gcb.16608)
- **Data:** [Dryad dataset](https://datadryad.org/dataset/doi:10.5061/dryad.hx3ffbgjj)

## Architecture

The state process models latent population dynamics across space and time, with spatial and temporal random effects. The observation process models detection from repeated surveys, so survey noise stays out of the trends. Climate predictors enter at the site-year level: temperature, precipitation, heatwave exposure, drought and cyclone indices.

Cyclone damage needed its own measurement. High-resolution satellite imagery quantified cyclone-induced change in rainforest vegetation structure, which then joined the model as a predictor. JAGS ran the model fitting, and R handled processing and visualisation.

## The decision that was hard

A single warming trend would fit the data and answer nothing. Management needs to know which driver does the damage, and drivers travel together: hot years bring heatwaves, cyclones flatten vegetation. We modelled 5 drivers jointly rather than one at a time, accepting the collinearity risk. Joint estimation is what let the surprising answer, that cyclones barely matter, emerge at all.

## What was measured

The model measured effect sizes per driver, with credible intervals, across the elevational gradient. Warming and rainfall change carried the community-wide signal, positive in the lowlands and negative in the uplands. Heatwaves added a negative effect on lowland populations, matching the observed distribution of extreme events across elevations.

## What did not work

We expected cyclones and droughts to be major drivers of change. The model found marginal effects on spatiotemporal community change for both. Responses were species-specific and unrelated to the elevational gradient. The expected disaster story did not survive measurement, and the paper reports that plainly.

## Role

I designed the spatiotemporal modelling framework and processed the satellite-derived vegetation metrics. I ran the fitting, validated the models and co-authored the manuscript.

## What this taught me about evaluation

Measure every plausible cause, including the ones you expect to win. The dramatic driver here lost to the chronic one, and only joint measurement could show that. In engineering I keep the same habit: benchmark the assumed bottleneck before optimising it.
