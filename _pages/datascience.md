---
title: "Data Science"
permalink: /datascience/
layout: splash
classes: wide
toc: false
# no sidebar here; keep it on the subpages

feature_row:
  - title: "Projects"
    excerpt: "End-to-end builds and case studies."
    url: "/datascience/projects/"
    btn_label: "Explore projects"
    btn_class: "btn--primary"
  - title: "Skills"
    excerpt: "Core methods and tooling."
    url: "/datascience/skills/"
    btn_label: "See skills"
    btn_class: "btn--primary"
  - title: "Education"
    excerpt: "Degrees and certifications."
    url: "/datascience/education/"
    btn_label: "View education"
    btn_class: "btn--primary"
  - title: "Communication"
    excerpt: "Talks and public resources."
    url: "/datascience/communication/"
    btn_label: "View communication"
    btn_class: "btn--primary"
---

## Welcome to my Data Science portfolio
A map of my end-to-end projects, core skills, education, and public work.

{% include feature_row id="feature_row" %}

---

<h2 style="margin-top:1.5rem;">Featured work</h2>

<div style="display:flex; gap:28px; align-items:flex-start; flex-wrap:wrap; margin-top:0.25rem;">
  <!-- Left: text -->
  <div style="flex:1 1 520px; min-width:320px;">
    <p style="margin-top:0;">
      <strong>Job Intelligence Engine</strong> — an end-to-end pipeline that turns real job ads into a skill taxonomy,
      fit-for-purpose models, and decision-ready outputs for role targeting and upskilling.
    </p>

    <ul style="margin:0 0 0.9rem 1.1rem;">
      <li>Reproducible pipeline: ingest → normalize → taxonomy → modelling → reporting</li>
      <li>Documented evaluation and error analysis for decision-ready outputs</li>
      <li>Outputs: role targeting, skill-gap diagnosis, and upskilling priorities</li>
    </ul>

    <a class="btn btn--primary" href="/datascience/projects/job_intelligence_engine/">View project</a>
  </div>

  <!-- Right: image -->
  <div style="flex:0 1 640px; min-width:320px;">
    <img
      src="https://raw.githubusercontent.com/AlejandroFuentePinero/alejandrofuentepinero.github.io/master/files/simple_workflow.png"
      alt="Job Intelligence Engine workflow"
      style="width:100%; height:auto; display:block;"
    >
  </div>
</div>
