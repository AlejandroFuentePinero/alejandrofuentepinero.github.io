---
title: "Community reshuffling under elevational shifts"
excerpt: "A simulation of 7,613 wildlife communities predicts mass local extinctions as warming pushes mountain-top species out of habitat. Each species climbs at its own speed."
date: 2022-04-01
type: research
stack:
  - R
  - Spatial forecasting
redirect_from:
  - /datascience/projects/dynamic-community-reshuffling/
---

When warming pushes mountain species uphill, they do not move as a group. A species that flies crosses a valley that stops one that walks, so communities do not shift, they reshuffle. I simulated that reshuffling for 7,613 vertebrate communities in the Australian Wet Tropics. The local extinction rate, the share of species unable to move, rises with elevation and points to mass local extinctions of upland species.

Each species moves by its own chance of dispersing, computed from how far it can travel and how much the terrain resists it. Dissimilarity indices then measure how far each community drifts from its current make-up. The result is a worked example of the ["escalator to extinction"](https://www.pnas.org/doi/abs/10.1073/pnas.1817416115): species escape upslope until no habitat remains.

## Links

- **Paper page:** [Predicted alteration of vertebrate communities](/research/community-reshuffling-2022/)
- **Journal:** [Diversity and Distributions](https://onlinelibrary.wiley.com/doi/full/10.1111/ddi.13514)
- **Data:** [Dryad dataset](https://datadryad.org/dataset/doi:10.5061/dryad.ksn02v759)

## Architecture

The workflow lines up 3 kinds of spatial layer. Species distribution models map where each species can live, thermal resistance surfaces score how hard each stretch of terrain is to cross, and patch boundaries define each elevational band. A simulation engine then shifts each of the 7,613 communities uphill, one species at a time, weighted by that species' chance of dispersing. Beta-diversity metrics, which compare the make-up of 2 communities, score the change in each patch: turnover, co-occurrence and the local extinction rate.

The number of runs made engineering part of the method. Parallel processing, efficient file input and output, and streamlined loops brought the multi-species forecasts down to a practical runtime. Everything runs in R under version control.

## The decision that was hard

The simple simulation shifts every species uphill at the same rate, and it is wrong in a specific way. Uniform shifts preserve the make-up of a community by construction, so the question of reshuffling cannot even be asked. I gave each species its own dispersal success, from its dispersal ability and the terrain between patches. That choice multiplied the compute, and it is what made the uneven outcomes, the actual finding, visible.

## What was measured

Dispersal success depended strongly on a species' ability, on the terrain and on the amount of warming. The uneven success among species produced marked change in community make-up along the gradient over time. The local extinction rate, the share of species unable to shift, was highest at high elevation. Species co-occurrence, how many species still share a patch, fell substantially in high-altitude ecosystems.

## Role

I designed and implemented the simulation workflow, built the optimised pipelines, analysed the reshuffling patterns and wrote the manuscript.

## What this taught me about evaluation

A simulation inherits every assumption you feed it, so the assumptions must be the visible part. I carry that into engineering: scenario tests state their inputs first. A faster pipeline is worthless until its outputs match the slow one, because throughput work and correctness work are separate jobs.
