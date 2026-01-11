---
title: "Data Science"
permalink: /datascience/
layout: splash
classes: wide
toc: false
---
## Welcome to my Data Science portfolio
A map of my end-to-end projects, core skills, education, and public work.

<!-- 4-card navigation row -->
<div style="
  display:grid;
  grid-template-columns: repeat(4, minmax(220px, 1fr));
  gap:22px;
  margin: 1.25rem 0 1.75rem 0;
">
  <div style="border:1px solid #eee; border-radius:16px; padding:22px; background:#fff; box-shadow:0 1px 2px rgba(0,0,0,0.04);">
    <h3 style="margin:0 0 .4rem 0;">Projects</h3>
    <p style="margin:0 0 1rem 0;">End-to-end builds and case studies.</p>
    <a class="btn btn--primary" href="/datascience/projects/">Explore projects</a>
  </div>

  <div style="border:1px solid #eee; border-radius:16px; padding:22px; background:#fff; box-shadow:0 1px 2px rgba(0,0,0,0.04);">
    <h3 style="margin:0 0 .4rem 0;">Skills</h3>
    <p style="margin:0 0 1rem 0;">Core methods and tooling.</p>
    <a class="btn btn--primary" href="/datascience/skills/">See skills</a>
  </div>

  <div style="border:1px solid #eee; border-radius:16px; padding:22px; background:#fff; box-shadow:0 1px 2px rgba(0,0,0,0.04);">
    <h3 style="margin:0 0 .4rem 0;">Education</h3>
    <p style="margin:0 0 1rem 0;">Degrees and certifications.</p>
    <a class="btn btn--primary" href="/datascience/education/">View education</a>
  </div>

  <div style="border:1px solid #eee; border-radius:16px; padding:22px; background:#fff; box-shadow:0 1px 2px rgba(0,0,0,0.04);">
    <h3 style="margin:0 0 .4rem 0;">Communication</h3>
    <p style="margin:0 0 1rem 0;">Talks and public resources.</p>
    <a class="btn btn--primary" href="/datascience/communication/">View communication</a>
  </div>
</div>

<!-- mobile fallback: 2 columns then 1 column -->
<style>
  @media (max-width: 1100px) {
    .page__content > div[style*="grid-template-columns: repeat(4"] {
      grid-template-columns: repeat(2, minmax(220px, 1fr)) !important;
    }
  }
  @media (max-width: 640px) {
    .page__content > div[style*="grid-template-columns: repeat(4"] {
      grid-template-columns: 1fr !important;
    }
  }
</style>

<hr style="margin: 1.5rem 0;">

<h2 style="margin-top:1.25rem;">Featured work</h2>

<div style="display:flex; gap:28px; align-items:flex-start; flex-wrap:wrap; margin-top:0.5rem;">
  <!-- Left: text -->
  <div style="flex:1 1 520px; min-width:320px;">
    <p style="margin-top:0;">
      <strong>Job Intelligence Engine</strong> — an end-to-end pipeline that turns real job ads into a skill taxonomy,
      fit-for-purpose models, and decision-ready outputs for role targeting and upskilling.
    </p>

    <ul style="margin:0 0 1rem 1.1rem; padding:0; list-style-position:outside;">
      <li>Interpretable market signals</li>
      <li>Career positioning</li>
      <li>Upskilling recommendations</li>
    </ul>

    <a class="btn btn--primary" href="/datascience/projects/job_intelligence_engine/">View project</a>
  </div>

  <!-- Right: image -->
  <div style="flex:0 1 720px; min-width:320px;">
    <img
      src="/simple_workflow.png"
      alt="Job Intelligence Engine workflow"
      style="width:100%; height:auto; display:block;"
    >
  </div>
</div>
