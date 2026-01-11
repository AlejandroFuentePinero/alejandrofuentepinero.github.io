---
title: "Data Science"
permalink: /datascience/
layout: splash
classes: wide
toc: false
# no sidebar here; keep it on the subpages

# Use 2x2 grid (MM feature_row supports 2 items/row cleanly)
feature_row_1:
  - title: "Projects"
    excerpt: "End-to-end builds and case studies in ML, Bayesian modelling, forecasting, remote sensing, and hierarchical modelling."
    url: "/datascience/projects/"
    btn_label: "Explore projects"
    btn_class: "btn--primary"
  - title: "Skills"
    excerpt: "Analytics, modelling, ML, Bayesian inference, spatial analysis, and reproducible data workflows."
    url: "/datascience/skills/"
    btn_label: "See skills"
    btn_class: "btn--primary"

feature_row_2:
  - title: "Education"
    excerpt: "Degrees, training, and certificates (with links)."
    url: "/datascience/education/"
    btn_label: "View education"
    btn_class: "btn--primary"
  - title: "Communication"
    excerpt: "Talks, workshops, and public resources."
    url: "/datascience/communication/"
    btn_label: "View communication"
    btn_class: "btn--primary"
---

## Welcome to my Data Science portfolio
This section showcases my projects, curated learning builds, and translated research case studies. Use Projects to see end-to-end work first, then Skills, Education, and Communication for supporting context.

## Featured work

<style>
/* Featured block: 2 columns on desktop, stacks on mobile */
.ds-featured {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 32px;
  align-items: start;
  margin-top: 0.25rem;
  margin-bottom: 1.75rem;
}
.ds-featured p { margin-top: 0; }
.ds-featured img { width: 100%; height: auto; display: block; }
@media (max-width: 900px) {
  .ds-featured { grid-template-columns: 1fr; }
  .ds-featured img { max-width: 900px; margin: 0 auto; }
}
</style>

<div class="ds-featured">
  <div>
    <p>
      <strong>Job Intelligence Engine</strong> — an end-to-end pipeline that turns real job ads into a skill taxonomy,
      fit-for-purpose models, and decision-ready outputs for role targeting and upskilling. Built with reproducible
      architecture and documented evaluation.
    </p>

    <p style="margin-top:1rem;">
      <a class="btn btn--primary" href="/datascience/projects/job_intelligence_engine/">View the Job Intelligence Engine project</a>
    </p>
  </div>

  <div>
    <img
      src="https://raw.githubusercontent.com/AlejandroFuentePinero/alejandrofuentepinero.github.io/master/files/engine_path.png"
      alt="Job Intelligence Engine"
    >
  </div>
</div>

{% include feature_row id="feature_row_1" %}
{% include feature_row id="feature_row_2" %}
