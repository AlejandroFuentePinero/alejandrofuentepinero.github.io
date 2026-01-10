---
title: "Projects"
layout: archive
permalink: /datascience/projects/
collection: projects
entries_layout: grid
classes: wide
---

Below are selected case studies (academic + applied) with a data-science focus.

If you have 3 minutes: read the first two in “Featured case studies”.

{% include base_path %}

{%- comment -%}
Requirements in each project markdown (/_projects/*.md):
  tier: featured | learning | research
  order: (number)  # recommended for deterministic ordering inside each tier
{%- endcomment -%}

{%- assign featured = site.projects | where: "tier", "featured" | sort: "order" -%}
{%- assign learning = site.projects | where: "tier", "learning" | sort: "order" -%}
{%- assign research = site.projects | where: "tier", "research" | sort: "order" -%}
{%- assign other    = site.projects | where_exp: "p", "p.tier == nil" | sort: "date" | reverse -%}

<h2>Featured case studies</h2>
<p>Portfolio-grade, end-to-end projects (best signal).</p>

<div class="mm-card-grid">
  {%- for post in featured -%}
    {% include archive-single.html type="grid" %}
  {%- endfor -%}
</div>

<h2>Learning builds (curated)</h2>
<p>Smaller repos used to build core skills (kept clean and intentional).</p>

<div class="mm-card-grid">
  {%- for post in learning -%}
    {% include archive-single.html type="grid" %}
  {%- endfor -%}
</div>

<h2>Research case studies (translated)</h2>
<p>Academic projects reframed in industry language (methods + outcomes).</p>

<div class="mm-card-grid">
  {%- for post in research -%}
    {% include archive-single.html type="grid" %}
  {%- endfor -%}
</div>

{%- if other and other.size > 0 -%}
<h2>Other</h2>
<p>Uncategorized items (consider assigning a tier).</p>

<div class="mm-card-grid">
  {%- for post in other -%}
    {% include archive-single.html type="grid" %}
  {%- endfor -%}
</div>
{%- endif -%}
