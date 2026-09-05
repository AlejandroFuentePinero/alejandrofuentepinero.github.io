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

Not every climate driver matters equally, and this study measured which ones actually move rainforest bird populations. Across 47 species in the Australian Wet Tropics, warming and changing rainfall drove the strongest responses, and the direction flipped with elevation. Lowland populations gained from rising temperature and rainfall while upland species declined under the same drivers.

The evidence is 17 years of surveys, 2000 to 2016, fitted with hierarchical population models that separate real change from the chance of missing a bird. Heatwaves cut lowland populations, which is where those events concentrate. Cyclones and droughts, the disasters everyone expected to matter, had only marginal effects on the community.

## Links

- **Paper page:** [The climatic drivers of long-term population changes in rainforest montane birds](/research/montane-bird-climate-drivers-2023/)
- **Journal:** [Global Change Biology](https://onlinelibrary.wiley.com/doi/full/10.1111/gcb.16608)
- **Data:** [Dryad dataset](https://datadryad.org/dataset/doi:10.5061/dryad.hx3ffbgjj)

## Architecture

The state process models the hidden population dynamics across space and time, with random effects that let each site and year vary around the shared trend. The observation process models detection from repeated surveys, so survey noise stays out of the trends. Climate predictors enter for each site and year: temperature, precipitation, heatwave exposure, and drought and cyclone indices.

Cyclone damage needed its own measurement. High-resolution satellite imagery quantified how much each cyclone changed the structure of the rainforest canopy, and that measure joined the model as a predictor. JAGS fitted the model, and R handled processing and visualisation.

## The decision that was hard

A single warming trend would fit the data and answer nothing. Management needs to know which driver does the damage, and drivers travel together: hot years bring heatwaves, and cyclones flatten vegetation. I modelled all 5 drivers jointly rather than one at a time, accepting the risk that correlated predictors make individual effects harder to pin down. Joint estimation is what let the surprising answer, that cyclones barely matter, emerge at all.

## What was measured

The model measured an effect size per driver, with credible intervals, across the elevational gradient. Warming and rainfall change carried the community-wide signal, positive in the lowlands and negative in the uplands. Heatwaves added a negative effect on lowland populations, matching where those extreme events actually fall across elevations.

## What did not work

I expected cyclones and droughts to be major drivers of change. The model found marginal effects on community change for both, and the responses were species-specific and unrelated to elevation. The expected disaster story did not survive measurement, and the paper reports that plainly.

## Role

I designed the spatiotemporal modelling framework and processed the satellite-derived vegetation metrics. I ran the fitting, validated the models and co-authored the manuscript.

## What this taught me about evaluation

Measure every plausible cause, including the ones you expect to win. The dramatic driver here lost to the chronic one, and only joint measurement could show that. In engineering I keep the same habit: benchmark the assumed bottleneck before optimising it.
