---
title: "Job Intelligence Engine"
excerpt: "The engine ranks 6,100 postings into 2 shortlists: target now, or worth a stretch. Its skill-demand models score 0.88 to 0.95 area under the curve."
date: 2026-01-02
type: engineering
stack:
  - Python
  - scikit-learn
  - SBERT
  - XGBoost
  - Streamlit
redirect_from:
  - /datascience/projects/job_intelligence_engine/
---

The Job Intelligence Engine turns 6,100 job postings into ranked role recommendations. It separates the roles to target now from the roles worth a stretch, with the reasons attached. A counterfactual layer ranks which missing skill changes your options the most.

The pipeline is deterministic end to end. The salary model explains about 30% of variance on held-out postings, the expected ceiling for noisy posted pay. 27 per-skill models score demand at 0.88 to 0.95 area under the curve.

Its language model extraction layer, [AI-JIE](/projects/ai-jie/), has its own page.

## Links

- **Live app:** [job-intelligence-engine.streamlit.app](https://job-intelligence-engine.streamlit.app/)
- **Source:** [job-intelligence-engine on GitHub](https://github.com/AlejandroFuentePinero/job-intelligence-engine)
- **Technical report:** [Methods, evaluation and results](https://github.com/AlejandroFuentePinero/job-intelligence-engine/blob/main/docs/narrative/technical_report.md)

<img src="/files/app_demo.gif" alt="Job Intelligence Engine demo" width="960" height="540" loading="lazy">

## Architecture

The pipeline normalises raw postings first: titles, seniority, locations, salary fields and skill tokens mapped into skill families. 2 learned layers sit on top. A tuned salary response model estimates expected pay with interpretable drivers. 27 per-skill requirement models turn sparse skill mentions into calibrated demand probabilities per job.

A graph layer embeds jobs and skills from their co-occurrence and clusters them into 20 latent job families. The families expose which roles behave alike in skill space, whatever their titles say.

User positioning separates 2 ideas most job tools collapse into one score. Suitability measures fit to your current profile. Competitiveness measures the barrier: missing, rare skill requirements and seniority expectations. The recommender turns the 2 axes into the best-now and stretch shortlists, each with explicit gap explanations.

<figure>
  <picture>
    <source type="image/webp" srcset="/files/project_pipeline_simple.webp">
    <img src="/files/project_pipeline_simple.png" alt="Job Intelligence Engine system workflow" width="1536" height="1024" loading="lazy" style="width:100%; max-width:1100px;">
  </picture>
</figure>

## The decision that was hard

Upskilling advice is a counterfactual claim: add this skill and your options improve. The tempting design recomputes everything per scenario, including which jobs qualify. That inflates every lift, because a changed candidate universe changes the denominator.

The engine freezes the candidate universe instead. Each add-one-skill scenario recomputes positioning on the same job set. Deltas stay comparable, and a guardrail rejects skills that harm the current best-now set. The ranking rewards real movement: stretch roles promoted to best-now, gaps closed, alignment gained.

## What was measured

The salary model reaches a test R² of about 0.30 with a mean absolute error near $25,000. That is the expected range for posted salaries, which carry ranges, gaps and negotiation noise. The skill models hold 0.88 to 0.95 area under the curve for most families, weaker on rare ones.

Contract evaluations enforce correctness, not trust. Artefacts must share one job universe in one order. Probabilities must stay bounded and finite. Repeated runs must reproduce the same rankings, and the 2 shortlists must never overlap.

Empty universes and misaligned inputs fail fast instead of producing quietly wrong output. A rebuild-versus-benchmark check catches silent changes to the processed dataset after refactors.

## What did not work

Salary prediction as fine-grained optimisation did not survive contact with the data. Posted pay is too noisy to rank individual roles by predicted dollars. The engine now uses salary only as an alignment check against a target band. Core ranking stays anchored in skill match.

Dictionary skill extraction hit its ceiling. It reads exact tokens, so synonyms and implicit requirements become false negatives, and rare skill families stay unstable. That recorded limit is what [AI-JIE](/projects/ai-jie/) exists to remove: a language model reads intent where a dictionary reads strings.

## Stack

Python · pandas · NumPy · scikit-learn · SBERT · XGBoost/LightGBM · SHAP · Streamlit · NetworkX
