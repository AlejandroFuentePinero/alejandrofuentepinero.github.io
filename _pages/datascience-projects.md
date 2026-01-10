---
title: "Projects"
layout: archive
permalink: /datascience/projects/
collection: projects
entries_layout: list
classes: wide projects-page
show_excerpts: true
---

Below are selected case studies (academic + applied) with a data-science focus.

If you have 3 minutes: read the first two in “Featured case studies”.

{% include base_path %}

{%- comment -%}
Add to each /_projects/*.md:
  tier: featured | learning | research
  order: <number>
{%- endcomment -%}

{%- assign featured = site.projects | where: "tier", "featured" | sort: "order" -%}
{%- assign learning = site.projects | where: "tier", "learning" | sort: "order" -%}
{%- assign research = site.projects | where: "tier", "research" | sort: "order" -%}
{%- assign other    = site.projects | where_exp: "p", "p.tier == nil" | sort: "date" | reverse -%}

<hr>

## Featured case studies
Portfolio-grade, end-to-end projects.

<div class="projects-tier projects-tier--featured">
{%- for post in featured -%}
  {% include archive-single.html type="list" %}
{%- endfor -%}
</div>

<hr>

## Learning builds (curated)
Smaller repos used to build core skills.

<div class="projects-tier projects-tier--learning">
{%- for post in learning -%}
  {% include archive-single.html type="list" %}
{%- endfor -%}
</div>

<hr>

## Research case studies (translated)
Academic projects reframed in industry language.

<div class="projects-tier projects-tier--research">
{%- for post in research -%}
  {% include archive-single.html type="list" %}
{%- endfor -%}
</div>

{%- if other and other.size > 0 -%}
<hr>

## Other
<div class="projects-tier projects-tier--other">
{%- for post in other -%}
  {% include archive-single.html type="list" %}
{%- endfor -%}
</div>
{%- endif -%}
