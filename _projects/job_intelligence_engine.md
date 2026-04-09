---
title: "Job Intelligence Engine"
excerpt: "A job-market intelligence system combining LLM-powered extraction with deterministic analytics — turning messy postings into interpretable skill demand, salary signals, and clear best_now vs stretch recommendations, delivered as a reproducible Python pipeline + Streamlit app."
date: 2026-01-02
tier: featured
order: 1
---

## Links (start here)
- **Live app:** [Streamlit App](https://job-intelligence-engine.streamlit.app/)
- **GitHub repo (core pipeline):** [Job Intelligence Engine](https://github.com/AlejandroFuentePinero/job-intelligence-engine)
- **GitHub repo (AI extension):** [AI-JIE](https://github.com/AlejandroFuentePinero/ai-jie)

![Job Intelligence Engine — Demo](https://raw.githubusercontent.com/AlejandroFuentePinero/alejandrofuentepinero.github.io/master/files/app_demo.gif)

## Overview

Job postings are noisy: roles and skills overlap heavily in meaning, postings describe the same requirements with different language, and "fit" often devolves into keyword matching or generic advice. The result is wasted time—applying to roles that are either unrealistic right now or undershoot your actual potential.

**Job Intelligence Engine** converts raw job ads into a structured, interpretable market layer, then positions an individual within that landscape to make decisions that are both realistic and strategic. The app surfaces recommendations with explicit rationale and interpretation panels; the repo contains the deterministic pipeline and persisted artefacts that reproduce those outputs.

- What roles are realistic **now** (high fit, low friction)?
- What roles are worth a **stretch** (clear upside, clear gaps)?
- What should I learn next to change my options **measurably**?

## What it delivers

- **Interpretable market signals:** structured skill demand and salary drivers you can inspect and reason about.
- **Career positioning:** separates **best_now** roles (strong fit, lower barriers) from **stretch** roles (higher upside, clearer gaps), with explicit rationale.
- **Upskilling recommendations:** counterfactual "add-one-skill" analysis that ranks what to learn by the change it produces in suitability, competitiveness, and salary alignment.

## How it works

The system runs as a deterministic pipeline. It normalises raw postings (titles, locations, salaries, skill tokens), learns market structure via probabilistic skill-requirement models and a tuned salary model, then translates those signals into transparent positioning scores, recommendations, and upskilling targets. The engine separates suitability (fit to your current profile) from competitiveness (barrier to entry driven by missing or rare skill requirements) — a distinction most job tools collapse into a single score. Outputs are served through a lightweight Streamlit interface.

<figure>
  <img src="https://raw.githubusercontent.com/AlejandroFuentePinero/alejandrofuentepinero.github.io/master/files/project_pipeline_simple.png" alt="Job Intelligence Engine — system workflow" style="width:100%; max-width:1100px;">
</figure>

## AI Extension: LLM-Powered Extraction & Evaluation

The original pipeline relies on deterministic NLP for skill extraction. The AI extension replaces this with an LLM-powered extraction system that understands semantic context — distinguishing required from preferred skills, classifying seniority, and assigning job families directly from unstructured postings.

**Architecture:** Async batch pipeline built with GPT-4o-mini, the `instructor` library, and Pydantic schemas at temperature=0. A chain-of-thought scaffolding approach uses intermediate reasoning fields to force the model to deliberate before classifying — a prompt architecture decision that dramatically improved extraction accuracy for ambiguous skill categories (required vs. preferred), at the cost of additional token usage per posting.

**Evaluation framework:** LLM-as-judge system using GPT-4o as an independent evaluator, calibrated against human annotations via Cohen's kappa. Includes a human evaluation persistence layer, a HuggingFace Hub dataset pipeline for reproducible eval sets, and trend tracking across prompt iterations.

**Key engineering decisions:**
- Two-model design: cheaper model (GPT-4o-mini) for high-volume extraction, stronger model (GPT-4o) for low-volume evaluation — optimising cost without sacrificing eval rigour.
- Async concurrency with checkpointing for fault-tolerant batch processing.
- Structured output validation via Pydantic, eliminating post-hoc parsing of LLM responses.

**Stack addition:** OpenAI API · instructor · Pydantic · asyncio · HuggingFace Hub

## Stack

Python · pandas · NumPy · scikit-learn · SBERT · XGBoost/LightGBM · SHAP · Streamlit · NetworkX · OpenAI API · instructor · Pydantic · asyncio · HuggingFace Hub
