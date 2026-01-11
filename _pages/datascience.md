---
title: "Data Science"
permalink: /datascience/
layout: splash
classes: wide
toc: false
---

## Welcome to my Data Science portfolio
End-to-end case studies, core skills, education, and public work.

<!-- Styles (stable selectors; avoids "Word-like" reflow) -->
<style>
  /* 4-card nav row */
  .ds-nav {
    display: grid;
    grid-template-columns: repeat(4, minmax(240px, 1fr));
    gap: 22px;
    margin: 1.25rem 0 1.75rem 0;
  }
  .ds-card {
    border: 1px solid #eee;
    border-radius: 16px;
    padding: 22px;
    background: #fff;
    box-shadow: 0 1px 2px rgba(0,0,0,0.04);
  }
  .ds-card h3 { margin: 0 0 .45rem 0; }
  .ds-card p  { margin: 0 0 1rem 0; }

  /* Make buttons feel "big" and consistent */
  .ds-card .btn,
  .ds-feature .btn {
    padding: 0.85em 1.15em;
    font-size: 1.02em;
    border-radius: 10px;
  }

  /* Featured work 2-column layout */
  .ds-feature {
    display: grid;
    grid-template-columns: 1.05fr 1fr; /* text a bit wider */
    gap: 28px;
    align-items: start;
    margin-top: 0.75rem;
  }
  .ds-feature-text p { margin-top: 0; }
  .ds-feature-text ul { margin: 0 0 1rem 1.1rem; padding: 0; }
  .ds-feature-media img { width: 100%; height: auto; display: block; }

  /* Responsive */
  @media (max-width: 1100px) {
    .ds-nav { grid-template-columns: repeat(2, minmax(240px, 1fr)); }
    .ds-feature { grid-template-columns: 1fr; }
  }
  @media (max-width: 640px) {
    .ds-nav { grid-template-columns: 1fr; }
  }
</style>

<!-- 4-card navigation row -->
<div class="ds-nav">
  <div class="ds-card">
    <h3>Projects</h3>
    <p>End-to-end builds.</p>
    <a class="btn btn--primary" href="/datascience/projects/">Explore projects</a>
  </div>

  <div class="ds-card">
    <h3>Skills</h3>
    <p>Core methods and tooling.</p>
    <a class="btn btn--primary" href="/datascience/skills/">See skills</a>
  </div>

  <div class="ds-card">
    <h3>Education</h3>
    <p>Degrees and certifications.</p>
    <a class="btn btn--primary" href="/datascience/education/">View education</a>
  </div>

  <div class="ds-card">
    <h3>Communication</h3>
    <p>Talks and public resources.</p>
    <a class="btn btn--primary" href="/datascience/communication/">View communication</a>
  </div>
</div>

<hr style="margin: 1.5rem 0;">

## Featured work

<div class="ds-feature">
  <!-- Left: text -->
  <div class="ds-feature-text">
    <p>
      <strong>Job Intelligence Engine</strong> — turns real job ads into a skill taxonomy and models that produce role recommendations and upskilling priorities.
    </p>

    <ul>
      <li>Interpretable market signals</li>
      <li>Career positioning</li>
      <li>Upskilling recommendations</li>
    </ul>

    <a class="btn btn--primary" href="/datascience/projects/job_intelligence_engine/">View Job Intelligence Engine</a>
  </div>

  <!-- Right: image (clickable, no extra CTA) -->
  <div class="ds-feature-media">
    <a href="/datascience/projects/job_intelligence_engine/" style="display:block;">
      <img
        src="https://raw.githubusercontent.com/AlejandroFuentePinero/alejandrofuentepinero.github.io/master/files/simple_workflow.png"
        alt="Job Intelligence Engine workflow"
      >
    </a>
  </div>

