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

<!-- Figure (place directly under the overview for scan-first comprehension) -->
![Job Intelligence Engine — system workflow](https://github.com/AlejandroFuentePinero/alejandrofuentepinero.github.io/blob/master/files/project_pipeline_simple.png)

## What it delivers
- **Market signals (interpretable):** structured skill demand and salary drivers, designed to be read and trusted rather than treated as a black box.
- **Career positioning:** separates **best_now** roles (good fit, low barrier) from **stretch** roles (bigger step, strong upside) with explicit rationale.
- **Upskilling recommendations:** counterfactual “add-one-skill” analysis that quantifies how missing skills change suitability, competitiveness, and salary potential.

## How it works (high level)
Clean and normalise raw postings → model skill requirements (probabilistic) → model salary response (tuned XGBoost with learned skill components) → construct a job–skill landscape (graph-style structure) → generate interpretable positioning, recommendations, and upskilling outputs → serve results through a lightweight Streamlit UI.

## Engineering standards
Deterministic runs, modular `src/` design, saved artefacts, and an end-to-end pipeline that rebuilds outputs reliably from raw data to app-ready assets.

## Links
- **GitHub repo:** [Job Intelligence Engine](https://github.com/AlejandroFuentePinero/job-intelligence-engine)
- **Live app:** [Streamlit demo](<APP_URL>)
