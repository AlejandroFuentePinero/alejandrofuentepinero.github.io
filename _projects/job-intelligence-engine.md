---
title: "Job Intelligence Engine"
excerpt: "Sorts 6,162 postings into 2 shortlists, target now or worth a stretch, and names the skill to learn next."
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

Job hunting in data roles is hard because the options all look alike. Titles overlap, skill lists run long, and no posting says whether you are a realistic candidate. The Job Intelligence Engine reads 6,162 postings and answers that question for one person at a time.

It sorts roles into 2 shortlists: target now, or worth a stretch. Each entry explains the gap. Then it asks a what-if per missing skill: learn this, and how many stretch roles open up? Its skill models tell a role that needs a skill from one that does not about 9 times in 10, the 0.88 to 0.95 area under the curve reported below.

Its language model extraction layer, [AI-JIE](/projects/ai-jie/), has its own page.

## Links

- **Live app:** [job-intelligence-engine.streamlit.app](https://job-intelligence-engine.streamlit.app/)
- **Source:** [job-intelligence-engine on GitHub](https://github.com/AlejandroFuentePinero/job-intelligence-engine)
- **Technical report:** [Methods, evaluation and results](https://github.com/AlejandroFuentePinero/job-intelligence-engine/blob/main/docs/narrative/technical_report.md)

<img src="/files/app_demo.gif" alt="Job Intelligence Engine demo" width="960" height="540" loading="lazy">

## Architecture

The pipeline first cleans the raw postings: titles, seniority, locations, salary fields, and about 1,300 skill tokens mapped into 27 skill families. On top of that sit 2 learned layers. A salary model estimates expected pay and shows which features drive the estimate. And 27 per-skill models, one per family, turn sparse skill mentions into calibrated probabilities. A posting that never names a tool can still score high for it when everything else about the role says so.

A graph layer then embeds jobs and skills from how often they occur together and clusters the jobs into 20 families. Those families show which roles behave alike in skill space, whatever their titles say.

Positioning a person separates 2 ideas that most job tools collapse into one score. Suitability asks how well a role fits your current profile. Competitiveness asks how high the barrier is: missing skills, rare requirements and seniority expectations. The recommender turns those 2 axes into the target-now and stretch shortlists, each entry carrying an explanation of its gap.

<figure>
  <picture>
    <source type="image/webp" srcset="/files/project_pipeline_simple.webp">
    <img src="/files/project_pipeline_simple.png" alt="Job Intelligence Engine system workflow" width="1536" height="1024" loading="lazy" style="width:100%; max-width:1100px;">
  </picture>
</figure>

## The decision that was hard

Upskilling advice is a claim about a world that does not exist yet: learn this skill and your options improve. The tempting design recomputes everything for each scenario, including which jobs you now qualify for. That quietly inflates every gain, because when the pool of candidate jobs changes, the denominator changes with it.

So the engine freezes the candidate universe. Each add-one-skill scenario recomputes your position over exactly the same set of jobs, which keeps the gains comparable. A guardrail rejects any skill that would damage your current target-now list. The ranking rewards real movement: stretch roles promoted to target now, gaps closed, alignment gained.

## What was measured

The salary model reaches an R² of about 0.30 on held-out postings, meaning it explains roughly 30% of the variation in posted pay, with a typical error near $25,000. That sounds weak until you remember what posted salaries are: wide ranges, missing values and negotiation noise. It is the expected ceiling for this data. The skill models hold 0.88 to 0.95 area under the curve for most families and weaken on the rare ones.

The other tests check correctness rather than trust. Contract evaluations require every artefact to share one job universe in one order, and every probability to stay bounded and finite. Repeated runs must reproduce the same rankings, and the 2 shortlists must never overlap. An empty universe or a misaligned input fails fast instead of producing a quietly wrong answer. A rebuild-versus-benchmark check catches silent changes to the processed dataset after a refactor.

## What did not work

Salary prediction as fine-grained optimisation did not survive contact with the data. Posted pay is too noisy to rank individual roles by predicted dollars, so the engine now uses salary only as an alignment check against your target band. The core ranking stays anchored in skill match.

Dictionary skill extraction hit its ceiling too. It matches exact tokens, so a synonym or an implied requirement becomes a false negative, and the rare skill families stay unstable. That recorded limit is what [AI-JIE](/projects/ai-jie/) exists to remove: a language model reads intent where a dictionary reads strings.

## Stack

Python · pandas · NumPy · scikit-learn · SBERT · XGBoost/LightGBM · SHAP · Streamlit · NetworkX
