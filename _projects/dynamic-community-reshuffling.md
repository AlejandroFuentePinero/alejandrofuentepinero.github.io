---
title: "Community reshuffling under elevational shifts"
excerpt: "Simulated uphill shifts of 7,613 assemblages predicted mass local extinctions of upland species, mapping the escalator to extinction along the elevational gradient."
date: 2022-04-01
type: research
stack:
  - R
  - Spatial forecasting
redirect_from:
  - /datascience/projects/dynamic-community-reshuffling/
---

Species climb at different speeds when warming pushes them uphill, so communities do not shift, they reshuffle. A simulation of 7,613 vertebrate assemblages in the Australian Wet Tropics quantified that reshuffling. The local extinction rate rises with elevation, pointing to mass local extinctions of upland species.

Each species moves by its own dispersal probability, computed from dispersal ability and thermal resistance surfaces. Dissimilarity indices then measure how far each community drifts from its current composition. The pattern is a worked example of the ["escalator to extinction"](https://www.pnas.org/doi/abs/10.1073/pnas.1817416115): upslope escape until no habitat remains.

## Links

- **Paper page:** [Predicted alteration of vertebrate communities](/research/community-reshuffling-2022/)
- **Journal:** [Diversity and Distributions](https://onlinelibrary.wiley.com/doi/full/10.1111/ddi.13514)
- **Data:** [Dryad dataset](https://datadryad.org/dataset/doi:10.5061/dryad.ksn02v759)

## Architecture

The workflow harmonises spatial layers: species distribution models, thermal resistance surfaces and elevational patch definitions. A simulation engine shifts each of the 7,613 assemblages uphill, species by species, weighted by dispersal probability. Beta-diversity metrics score the change per patch: turnover, co-occurrence, local extinction rate.

The run count made engineering part of the method. Parallel processing, efficient file input and output, and streamlined loops cut the multi-species forecasts to a practical runtime. Everything runs in R under version control.

## The decision that was hard

The simple simulation shifts every species uphill at the same rate, and it is wrong in a specific way. Uniform shifts preserve community composition by construction, so the question of reshuffling cannot even be asked. We gave each species its own dispersal success, from its dispersal ability and the terrain between patches. That choice multiplied the compute, and it is what made heterogeneous outcomes, the actual finding, visible.

## What was measured

Dispersal success depended strongly on species' ability, terrain composition and climate change. The heterogeneous success rates produced marked temporal change between assemblages along the gradient. The local extinction rate, the share of species unable to shift, was highest at high elevation. Species co-occurrence declined substantially in high-altitude ecosystems.

## Role

I designed and implemented the simulation workflow, built the optimised pipelines, analysed the reshuffling patterns and wrote the manuscript.

## What this taught me about evaluation

A simulation inherits every assumption you feed it, so the assumptions must be the visible part. I carry that into engineering: scenario tests state their inputs first. A faster pipeline is worthless until its outputs match the slow one. Throughput work and correctness work are separate jobs.
