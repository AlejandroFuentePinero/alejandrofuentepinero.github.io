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
This section showcases my projects, curated learning builds, and translated research case studies. Use Projects to see end-to-end work first, then Skills, Education, and Communication for supporting context.

<h2>Featured work</h2>

<div style="display:flex; gap:28px; align-items:flex-start; flex-wrap:wrap; margin-top:0.5rem;">
  <!-- Left: text -->
  <div style="flex:1 1 520px; min-width:320px;">
    <p style="margin-top:0;">
      <strong>Job Intelligence Engine</strong> — an end-to-end pipeline that turns real job ads into a skill taxonomy,
      fit-for-purpose models, and decision-ready outputs for role targeting and upskilling. Built with reproducible
      architecture and documented evaluation.
    </p>

    <p style="margin:0;">
      <a href="/datascience/projects/job_intelligence_engine/"><strong>View the Job Intelligence Engine project</strong></a>
    </p>
  </div>

  <!-- Right: image (slightly larger) -->
  <div style="flex:0 1 640px; min-width:320px;">
    <img
      src="https://raw.githubusercontent.com/AlejandroFuentePinero/alejandrofuentepinero.github.io/master/files/engine_path.png"
      alt="Job Intelligence Engine"
      style="width:100%; height:auto; display:block;"
    >
  </div>
</div>

<hr style="margin: 2rem 0;" />

<div class="mm-card-grid" style="grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 28px;">
  {% include feature_row id="feature_row" %}
</div>
