---
title: "Job Intelligence Engine"
excerpt: "A deterministic job-market intelligence system that turns messy postings into interpretable skill demand, salary signals, and clear best_now vs stretch recommendations — delivered as a reproducible Python pipeline + Streamlit app."
date: 2026-01-02
order: 1
---

## Links (start here)
- **Live app:** [Streamlit App](https://job-intelligence-engine.streamlit.app/)
- **GitHub repo:** [Job Intelligence Engine](https://github.com/AlejandroFuentePinero/job-intelligence-engine)

## Overview
Job postings are noisy: roles and skills overlap heavily in meaning, postings describe the same requirements with different language, and “fit” often devolves into keyword matching or generic advice. The result is wasted time—applying to roles that are either unrealistic right now or undershoot your actual potential.

**Job Intelligence Engine** converts raw job ads into a structured, interpretable market layer, then positions an individual within that landscape to make decisions that are both realistic and strategic. The app surfaces recommendations with explicit rationale and interpretation panels; the repo contains the deterministic pipeline and persisted artefacts that reproduce those outputs.

- What roles are realistic **now** (high fit, low friction)?
- What roles are worth a **stretch** (clear upside, clear gaps)?
- What should I learn next to change my options **measurably**?

<figure>
  <img src="https://raw.githubusercontent.com/AlejandroFuentePinero/alejandrofuentepinero.github.io/master/files/project_pipeline_simple.png" alt="Job Intelligence Engine — system workflow" style="width:100%; max-width:1100px;">
  <figcaption style="text-align:center; font-size:0.9em; color:#666;">
    System workflow: job ads → deterministic pipeline → market insights, best_now vs stretch recommendations, and ROI-ranked upskilling.
  </figcaption>
</figure>

## What it delivers
- **Interpretable market signals:** structured skill demand and salary drivers you can inspect and reason about.
- **Career positioning:** separates **best_now** roles (strong fit, lower barriers) from **stretch** roles (higher upside, clearer gaps), with explicit rationale.
- **Upskilling recommendations:** counterfactual “add-one-skill” analysis that ranks what to learn by the change it produces in suitability, competitiveness, and salary alignment.

## How it works
The system runs as a deterministic pipeline. It normalises raw postings (titles, locations, salaries, skill tokens), learns market structure via probabilistic skill-requirement models and a tuned salary model, then translates those signals into transparent positioning scores, recommendations, and upskilling targets. Outputs are served through a lightweight Streamlit interface.

## Stack
Python, pandas, scikit-learn, Sentence Transformers (SBERT), KMeans, XGBoost, SHAP, Streamlit, NetworkX.

## Engineering standards
Reproducible, modular `src/` design with persisted artefacts and an end-to-end build that reliably regenerates app-ready assets fro
