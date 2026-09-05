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

Rainforest ringtail possums in the Australian Wet Tropics are on course to collapse by 2050. Extreme heatwaves are the main reason. I built that forecast from 30 years of possum surveys. It fed the lemuroid ringtail possum's national protection nomination under the Environment Protection and Biodiversity Conservation Act (EPBC Act).

The hard part of counting possums is that you never see them all. A quiet night looks like decline. So the model has 2 layers: one for the chance of seeing a possum, one for how many are there. Once it learned how warming and heatwaves move survival, I ran it forward to 2050. Under forecast warming, populations fall below the level at which they can persist within 3 decades.

## Links

- **Paper page:** [Climate change threatens the future of rain forest ringtail possums by 2050](/research/ringtail-possum-collapse-2022/)
- **Journal:** [Diversity and Distributions](https://onlinelibrary.wiley.com/doi/full/10.1111/ddi.13652)
- **Data:** [Dryad dataset](https://datadryad.org/dataset/doi:10.5061/dryad.m63xsj44h)

## Architecture

The model is hierarchical, written in R and JAGS, and it has 2 layers. The observation layer describes detection, the chance of seeing a possum that is there, so that who searched where cannot pass for population change. The state layer describes true abundance and its trend, driven by 2 climate covariates: warming and the frequency of heatwaves. Fitting by posterior sampling gives every quantity a credible interval, the Bayesian version of an error bar.

The forecast is not a separate model. The fitted mechanism itself runs forward from 2022 to 2050, carrying its uncertainty with it. The forward runs yield the probability of extinction, and of falling below each of several viability thresholds.

## The decision that was hard

The tempting analysis fits a trend line to the raw counts and extends it. That approach cannot say why a population falls, and any change in survey effort corrupts it. Instead I estimated the mechanism: how warming and heatwaves move survival and abundance. Only a fitted mechanism supports a forward run with honest uncertainty.

The cost was a harder model, with 2 linked processes, more parameters and longer fits. The gain was a forecast that names its driver and carries defensible error bars into a legal document.

## What was measured

The fitted model shows a strong negative effect of climate change on population dynamics, with extreme heatwaves doing the most damage. The decline over the last 3 decades was rapid and severe. Under forecast warming, populations fall below viability thresholds by 2050. Each claim carries its credible interval, and the model states an extinction probability for every threshold.

## Role

I conceived the framework, structured the count and climate data, ran the forecasting models and wrote the manuscript. I communicated the findings to conservation authorities.

## What this taught me about evaluation

Separate the instrument from the thing it measures, or every trend inherits the instrument's noise. The same separation now shapes how I evaluate retrieval systems: score each stage of the pipeline on its own. A forecast without propagated uncertainty is an opinion with digits.
