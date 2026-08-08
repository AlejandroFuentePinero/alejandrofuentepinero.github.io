---
layout: default
title: "Skills"
description: "Behind the skills sits the education record: degrees in biology and quantitative ecology, and the certificates that retrained me for AI engineering."
permalink: /skills/
redirect_from:
  - /datascience/skills/
---

<div class="container page-block" markdown="1">

<header class="page-header">
  <h1>Skills and education</h1>
  <p class="page-lead">Every chip names a skill demonstrated on this site. Behind the skills sits the education record: degrees in biology and quantitative ecology, and the certificates that retrained me for AI engineering.</p>
</header>

## Skills {#skills}

{% include skills-row.html %}

My core strength is statistical modelling under uncertainty. The same discipline now runs my AI engineering: retrieval pipelines, agents and the evaluation that proves they work. Research added the habits that transfer: measurement design first, explicit assumptions, delivery under real constraints and writing that can be audited.

### What I deliver

* **End-to-end AI systems.** Retrieval-augmented generation (RAG) pipelines with measured retrieval, agent workflows with tool calling, and fine-tuned models.
* **Full-cycle modelling.** Problem framing, model selection, validation and uncertainty-aware decision support.
* **Data pipelines.** Clean, testable, version-controlled paths from raw data to decision-ready outputs with Python and SQL.
* **Evaluation and communication.** Leakage checks, calibration, error slicing and stress testing, reported with explicit assumptions and limits.

### Depth, by area

<ul class="capability-list">
<li class="capability">
<div markdown="1">

#### AI engineering {#ai-engineering}

I build language model systems and prove they work: grounded generation, agentic systems, fine-tuning and evaluation.

* Retrieval over vector stores (ChromaDB) and knowledge graphs (Neo4j, Cypher), measured for groundedness and relevance
* Agent workflows in LangGraph: planning loops, tool calling and human checkpoints
* Judge models benchmarked against labelled data, traced with Arize Phoenix
* Fine-tuning: supervised frontier runs and QLoRA on open Hugging Face models
* Guardrails: cross-family review models, per-turn logging and drift detection

</div>
</li>
<li class="capability">
<div markdown="1">

#### Statistical modelling under uncertainty {#statistical-modelling}

Bayesian hierarchical methods for noisy, sparse and structured data, with uncertainty carried into every forecast.

* Generalised linear, additive and mixed models with partial pooling
* Observation separated from process: N-mixture and integrated population models
* Spatiotemporal forecasting, species distribution models and threshold inference
* Gradient boosting with XGBoost, clustering and SHAP interpretability
* Validation design: temporal splits, leakage checks, calibration and causal framing

The methods grew from field ecology research, recorded on the [Research]({{ '/research/' | relative_url }}) page.

</div>
</li>
<li class="capability">
<div markdown="1">

#### Data and software foundations {#foundations}

Reliable engineering around the models: pipelines, reproducibility, geospatial work and delivery apps.

* Ingestion and transformation with pandas and scikit-learn: schema discipline, typed and tested code
* Analytical queries on PostgreSQL: joins, window functions, common table expressions and reusable views
* Reproducibility: pinned environments, deterministic runs, versioned artefacts and Git throughout
* Raster and vector workflows in R, with spatial feature engineering
* Delivery apps in Gradio, Streamlit and Shiny

</div>
</li>
</ul>

Languages: Spanish (first language), English (IELTS 7.0), French (basic).

## Education {#education}

{% include education-degrees.md %}

* The doctorate built modelling frameworks that predict vulnerability to extreme events and locate high-risk habitat.
* The master's degree centred on spatial analysis and statistical modelling for conservation planning.
* The bachelor's degree grounded biology in mathematics, biostatistics and ecological modelling.

{% include education-certificates.html %}

</div>
