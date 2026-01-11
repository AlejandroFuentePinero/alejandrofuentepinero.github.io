---
title: "Data Science"
permalink: /datascience/
layout: splash
classes: wide
toc: false
# no sidebar here; keep it on the subpages
---

## Welcome to my Data Science portfolio
This section showcases my projects, curated learning builds, and translated research case studies. Use Projects to see end-to-end work first, then Skills, Education, and Communication for supporting context.

<h2>Featured work</h2>

<div style="display:flex; gap:28px; align-items:flex-start; flex-wrap:wrap; margin-top:0.5rem;">
  <!-- Left: text -->
  <div style="flex:1 1 460px; min-width:320px;">
    <p style="margin-top:0;">
      <strong>Job Intelligence Engine</strong> — an end-to-end pipeline that turns real job ads into a skill taxonomy,
      fit-for-purpose models, and decision-ready outputs for role targeting and upskilling. Built with reproducible
      architecture and documented evaluation.
    </p>

    <p style="margin:0;">
      <a href="/datascience/projects/job_intelligence_engine/"><strong>View the Job Intelligence Engine project</strong></a>
    </p>
  </div>

  <!-- Right: image (slightly bigger) -->
  <div style="flex:0 1 640px; min-width:320px;">
    <img
      src="https://raw.githubusercontent.com/AlejandroFuentePinero/alejandrofuentepinero.github.io/master/files/engine_path.png"
      alt="Job Intelligence Engine"
      style="width:100%; height:auto; display:block;"
    >
  </div>
</div>

<hr style="margin: 2rem 0;" />

<style>
/* 4-up card grid for the DS landing page */
.ds-nav-grid{
  display:grid;
  grid-template-columns:repeat(4, minmax(0, 1fr));
  gap:28px;
}
.ds-nav-card{
  border:1px solid rgba(0,0,0,0.08);
  border-radius:14px;
  padding:28px;
  background:#fff;
  box-shadow:0 1px 2px rgba(0,0,0,0.04);
}
.ds-nav-card h3{ margin:0 0 10px 0; }
.ds-nav-card p{ margin:0 0 16px 0; }
.ds-nav-card .btn{ display:inline-block; }

/* responsive */
@media (max-width: 1100px){
  .ds-nav-grid{ grid-template-columns:repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 650px){
  .ds-nav-grid{ grid-template-columns:1fr; }
}
</style>

<div class="ds-nav-grid">
  <div class="ds-nav-card">
    <h3>Projects</h3>
    <p>End-to-end builds and case studies.</p>
    <a class="btn btn--primary" href="/datascience/projects/">Explore projects</a>
  </div>

  <div class="ds-nav-card">
    <h3>Skills</h3>
    <p>Core methods and tooling.</p>
    <a class="btn btn--primary" href="/datascience/skills/">See skills</a>
  </div>

  <div class="ds-nav-card">
    <h3>Education</h3>
    <p>Degrees and certifications.</p>
    <a class="btn btn--primary" href="/datascience/education/">View education</a>
  </div>

  <div class="ds-nav-card">
    <h3>Communication</h3>
    <p>Talks and public resources.</p>
    <a class="btn btn--primary" href="/datascience/communication/">View communication</a>
  </div>
</div>
