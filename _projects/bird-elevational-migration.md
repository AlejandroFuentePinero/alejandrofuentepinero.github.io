---
title: "Altitudinal Migration and Community ‘Breathing’ in Tropical Mountains"
excerpt: "Modelled seasonal elevational migration across bird communities in the Australian Wet Tropics using hierarchical Bayesian abundance models and posterior-predicted community metrics."
tags: [R, bayesian-modelling, biodiversity, spatial-ecology, community-dynamics, climate-change]
date: 2024-11-01
---

## Problem
Tropical mountain birds often shift their elevation seasonally to track favourable conditions, yet these movements remain poorly quantified at the community level.  
**Goal:** Quantify and visualise how entire bird communities “breathe” along elevation gradients through the year — expanding upslope during warm seasons and contracting downslope in cooler ones.

## Approach
- Compiled long-term bird monitoring data across **160 sites** and multiple mountains in the Wet Tropics of Australia.  
- Fitted a **hierarchical Bayesian model** linking abundance to **elevation × season** interactions, capturing partial migration tendencies at the species level.  
- Used **posterior-predicted abundances (`N_pred`)** to compute ecological metrics:  
  - Species-level **centroid shifts** (mean elevation change across seasons).  
  - **Range width** and redistribution of abundance along elevation.  
  - **Community turnover** and synchrony among species through time.  
- Visualised outcomes via **heatmaps**, **ridge plots**, and **community ‘breathing’ diagrams** showing system-wide expansion and contraction dynamics.

## Stack
- **Hierarchical modelling:** multi-level structure accounting for species-level variation in seasonal elevational responses.  
- **Predictive analysis:** posterior predictions (`brms`, `bayestestR`) used to estimate centroid shifts and turnover uncertainty.  
- **Visualisation:** multi-panel figures combining `ggplot2`, `patchwork`, and `ggrepel` for dynamic community representations.  
- **Implementation:** all in **R**, with reproducible scripts for data cleaning, model fitting, and post-processing.

## Results
- ~70% of species displayed significant **upslope migration** during the warm season.  
- Communities exhibited a distinct **“breathing” pattern** — contraction to mid-elevations during the cool season and expansion upslope in warmer months.  
- Migration was **partial and asynchronous** across species, highlighting the complexity of community reorganisation under climate variability.  

## Impact
- Provided the first predictive, community-level quantification of altitudinal migration in tropical birds.  
- Demonstrated how **Bayesian predictive modelling** can extract dynamic behavioural and ecological patterns from sparse field data.  
- Created a transferable analytical pipeline for studying seasonal redistribution in other ecological systems.

## Links & Resources
- 💻 **Code repository:** [GitHub – Altitudinal migration project](https://github.com/AlejandroFuentePinero/awt_bird_altitudinal_migration)  
- 📄 **Paper (in prep):** “Community breathing: Predicting altitudinal migration from abundance models”

## Role
- Designed and implemented the Bayesian modelling framework.  
- Led analysis of community redistribution and synchrony metrics.  
- Created all visual outputs and reproducible R pipelines.  
- Wrote the manuscript and integrated ecological interpretation.
