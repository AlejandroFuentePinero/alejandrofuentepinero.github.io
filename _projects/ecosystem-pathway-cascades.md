---
title: "Climate, foliage chemistry and herbivory"
excerpt: "Climate and geology set the stage for how much insects eat rainforest leaves. Single soil nutrients, the expected drivers, predicted little after accounting for geology."
date: 2024-10-25
type: research
stack:
  - R
  - JAGS
  - Hierarchical models
redirect_from:
  - /datascience/projects/ecosystem-pathway-cascades/
---

How much of a rainforest leaf gets eaten by insects depends, in the end, on the climate and the rock beneath the tree, not on any single soil nutrient. That is the finding of this study. It traced the influence of climate and geology through soil chemistry and leaf chemistry to herbivory itself, separating the direct routes from the indirect ones.

The evidence comes from 25 sites in the Australian Wet Tropics chosen to span gradients of temperature, rainfall and geology, and from 3 widespread rainforest tree species. Trees of different species responded differently to the same resources, which is the practical warning of the paper.

## Links

- **Paper page:** [Relationships between abiotic factors, foliage chemistry and herbivory](/research/foliage-chemistry-herbivory-2024/)
- **Journal:** [Oecologia](https://link.springer.com/article/10.1007/s00442-024-05630-y)
- **Data:** [Dryad dataset](https://datadryad.org/dataset/doi:10.5061/dryad.d51c5b08s)

## Architecture

The models are hierarchical, specified in JAGS and processed in R. Pathway coefficients carry the network: climate and geology to soil nutrients, soil to foliage chemistry, foliage chemistry to herbivory. Because the model estimates the direct and the mediated paths together, it can say how much of an effect travels through the soil and how much bypasses it. Random effects absorb the nesting of trees within sites, and posterior analysis reads each pathway's strength with its uncertainty.

## The decision that was hard

Cascades invite a pile of pairwise regressions: soil against foliage, foliage against herbivory, each defensible alone. But pairwise results cannot separate a direct effect from a route through a mediator, and that separation was the whole question. I committed to one structured network model with explicit pathway coefficients. It cost model complexity and harder fitting, and it is the only design that answers what drives what.

## What was measured

Climate and geology showed an overarching influence over soil chemistry, foliar nitrogen and insect herbivory, both directly and indirectly. Each pathway carries a posterior estimate of its strength and its uncertainty. The 3 tree species responded to the same resources in different ways.

## What did not work

The expected workhorse, individual soil nutrients, did not deliver. Once the geology of a site was accounted for, single nutrients showed only equivocal influence on foliage chemistry. A simple nutrient-to-leaf story would have been publishable and wrong. The honest conclusion names specific limiting factors rather than convenient proxies of resource availability.

## Role

I designed the pathway models, structured the multivariate field dataset, fitted and interpreted the Bayesian models and wrote the manuscript.

## What this taught me about evaluation

Correlated inputs will hand you a tidy false story unless the analysis is built to separate paths. In engineering terms: attribute an improvement to the component that caused it, or the next change breaks it. Ablations are pathway analysis with a worse name.
