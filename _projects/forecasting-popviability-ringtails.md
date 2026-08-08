---
title: "Ringtail possum viability forecast"
excerpt: "A model on 30 years of surveys forecasts possum collapse by 2050, heatwaves doing most of the damage. The forecast fed a national protection nomination."
date: 2022-11-06
type: research
stack:
  - R
  - JAGS
  - Forecasting
redirect_from:
  - /datascience/projects/forecasting-popviability-ringtails/
---

A hierarchical Bayesian model on 30 years of surveys forecast the collapse of rainforest ringtail possums by 2050. The forecast fed a national protection nomination for the lemuroid ringtail possum. The nomination ran under the Environment Protection and Biodiversity Conservation Act (EPBC Act).

The model fits possum population dynamics in the Australian Wet Tropics from 1992 to 2021. It separates real population change from imperfect detection. It then runs the fitted mechanism forward to 2050 under forecast warming. Populations fall below viability thresholds within 3 decades, with extreme heatwaves doing most of the damage.

## Links

- **Paper page:** [Climate change threatens the future of rain forest ringtail possums by 2050](/research/ringtail-possum-collapse-2022/)
- **Journal:** [Diversity and Distributions](https://onlinelibrary.wiley.com/doi/full/10.1111/ddi.13652)
- **Data:** [Dryad dataset](https://datadryad.org/dataset/doi:10.5061/dryad.m63xsj44h)

## Architecture

The model is hierarchical, written in R and JAGS. An observation layer describes detection, so who searched where cannot masquerade as population change. A state layer describes true abundance and its trend, driven by climate covariates: warming and heatwave frequency. Posterior sampling gives every quantity a credible interval.

The forecast is not a separate model. The fitted mechanism itself propagates forward, from 2022 to 2050, carrying its uncertainty. The forward runs yield probabilities of absolute and quasi-extinction under different viability thresholds.

## The decision that was hard

The tempting analysis fits a trend to raw counts and extrapolates it. That approach cannot say why a population falls, and effort changes corrupt it. The model instead estimates the mechanism: how warming and heatwaves move survival and abundance. Only a fitted mechanism supports a forward run with honest uncertainty.

The cost was a harder model: 2 linked processes, more parameters, longer fits. The gain was a forecast that names its driver and carries defensible error bars into a legal document.

## What was measured

The fitted model shows a strong negative effect of climate change on population dynamics, extreme heatwaves above all. The decline over the last 3 decades was rapid and severe. Under forecast warming, populations fall below viability thresholds by 2050. Each claim carries its credible interval, and the model states extinction probabilities per threshold.

## Role

I conceived the framework, structured the count and climate data, ran the forecasting models and wrote the manuscript. I communicated the findings to conservation authorities.

## What this taught me about evaluation

Separate the instrument from the thing it measures, or every trend inherits the instrument's noise. The same separation now shapes how I evaluate retrieval systems: score each pipeline stage on its own. A forecast without propagated uncertainty is an opinion with digits.
