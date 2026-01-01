---
title: "Job Intelligence Engine"
excerpt: "End-to-end job-market intelligence system that turns messy job ads into structured skill signals, salary forecasts, and interpretable career positioning — delivered through a deterministic Python pipeline and a lightweight Streamlit app (best_now vs stretch)."
tags: [Python, data-science, machine-learning, NLP, feature-engineering, XGBoost, scikit-learn, PCA, pipelines, interpretability, SHAP, Streamlit, graphs, NetworkX, reproducibility]
date: 2025-12-21
order: 1
---

## Overview
Job postings are high-volume, inconsistent, and full of overlapping terminology — yet they still encode real signals about what the market rewards.  
**Job Intelligence Engine** converts raw job ads into decision-ready outputs: interpretable market insights, a constraint-aware recommender, and ROI-ranked upskilling targets that clarify what to learn next.

![Job Intelligence Engine — system workflow](https://raw.githubusercontent.com/AlejandroFuentePinero/alejandrofuentepinero.github.io/master/files/project_pipeline_simple.png)

## What it delivers
- **Market signals (interpretable):** structured skill demand and salary drivers, designed to be read and trusted rather than treated as a black box.
- **Career positioning:** separates **best_now** roles (good fit, low barrier) from **stretch** roles (bigger step, strong upside) with explicit rationale.
- **Upskilling recommendations:** counterfactual “add-one-skill” analysis that quantifies how missing skills change suitability, competitiveness, and salary potential.

## How it works
The system runs as a deterministic pipeline. It first normalises raw postings into a clean dataset (titles, locations, salaries, and skill tokens). It then learns market structure via probabilistic skill-requirement models and a tuned XGBoost salary model built on structured features and learned skill components. Finally, it constructs a job–skill landscape and turns those signals into interpretable positioning scores, job recommendations (best_now vs stretch), and upskilling targets, surfaced through a lightweight Streamlit interface.

## Engineering standards
Deterministic runs, modular `src/` design, saved artefacts, and an end-to-end pipeline that rebuilds outputs reliably from raw data to app-ready assets.

## Links
- **GitHub repo:** [Job Intelligence Engine](https://github.com/AlejandroFuentePinero/job-intelligence-engine)
- **Live app:** [Streamlit App](<APP_URL>)
