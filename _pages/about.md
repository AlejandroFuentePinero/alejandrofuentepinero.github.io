---
permalink: /
title: ""
classes: wide hide-page-title
layout: archive
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

# Welcome!

## Hi, I’m Alejandro — Data Scientist (PhD-trained)

I work at the intersection of **rigorous modelling** and **practical decision support** — building reproducible Python/SQL pipelines and ML systems that turn messy data into outputs people can act on.

My background is in **quantitative ecology and climate-change science**, where I built uncertainty-aware models to understand how living systems respond to environmental change. In industry-focused data science, I bring the same strengths: careful assumptions, clear validation, and decision-ready delivery.

---

## What I do

I build end-to-end analytics and ML workflows that prioritise reliability and usability:

- define measurable questions (metrics, cohorts, success criteria)  
- engineer clean, testable data pipelines with validation and artefacts  
- train and evaluate models with transparent trade-offs  
- communicate results clearly (what changed, why it matters, what to do next)

---

## Featured work

<div class="ds-feature">
  <!-- Left: text -->
  <div class="ds-feature-text">
    <p>
      <strong>Job Intelligence Engine</strong> — parses thousands of real data job ads into a skills taxonomy and market signals, then recommends best-fit roles and a prioritised upskilling plan.
    </p>

    <ul>
      <li>Skill demand & salary signals by role/family</li>
      <li>Best-now vs stretch role job recommendations</li>
      <li>Ranked upskilling priorities (positioning lift)</li>
    </ul>

    <p style="margin-top:0.5rem; font-size:0.95rem;">
      <strong>Stack:</strong> Python • NLP embeddings • XGBoost/LightGBM • Streamlit • reproducible pipeline & persisted artefacts • SHAP
    </p>

    <a class="btn btn--primary" href="/datascience/projects/job_intelligence_engine/">See demo & details</a>
  </div>


<!-- Right: image (clickable) -->
<div class="ds-feature-media">
  <a href="/datascience/projects/job_intelligence_engine/" aria-label="Open Job Intelligence Engine">
    <img
      src="https://raw.githubusercontent.com/AlejandroFuentePinero/alejandrofuentepinero.github.io/master/files/engine_path.png"
      alt="Job Intelligence Engine workflow"
    >
  </a>
</div>

<style>
  /* Featured work 2-column layout (homepage) */
  .ds-feature {
    display: grid;
    grid-template-columns: 1.05fr 1fr;
    gap: 28px;
    align-items: start;
    margin-top: 0.75rem;
  }
  .ds-feature-text p { margin-top: 0; }
  .ds-feature-text ul { margin: 0 0 1rem 1.1rem; padding: 0; }

  .ds-feature-media img {
    width: 100%;
    height: auto;
    display: block;
    max-height: 340px;   /* size control */
    object-fit: contain;
  }

  @media (max-width: 1100px) {
    .ds-feature { grid-template-columns: 1fr; }
  }
</style>



