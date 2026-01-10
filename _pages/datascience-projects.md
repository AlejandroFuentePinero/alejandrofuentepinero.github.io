---
layout: archive
title: "Projects"
permalink: /datascience/projects/
collection: projects
author_profile: true
classes: wide projects-page
entries_layout: grid
---

This page is a map of my data-science work, grouped by deliverable type:

> - **Featured case studies**: industry-style, end-to-end projects with code (reproducible pipeline + outputs).
> - **Research case studies**: industry-style case studies of rigorous modelling work where the primary deliverable is an analysis/paper (methods, validation, and decision-relevant insights).
> - **Learning builds**: smaller repos from structured practice (kept clean), included to show breadth—not as the main evidence of senior capability.

If you’re short on time: start with **Featured case studies**, then scan one **Research case study**.


{% include base_path %}

{%- comment -%}
In each /_projects/*.md add:
  tier: featured | learning | research
  order: <number>
{%- endcomment -%}

{%- assign featured = site.projects | where: "tier", "featured" | sort: "order" -%}
{%- assign learning = site.projects | where: "tier", "learning" | sort: "order" -%}
{%- assign research = site.projects | where: "tier", "research" | sort: "order" -%}
{%- assign other    = site.projects | where_exp: "p", "p.tier == nil" | sort: "date" | reverse -%}

## Featured case studies
<div class="mm-card-grid projects-tier projects-tier--featured">
{% for post in featured %}
  {% include archive-single.html %}
{% endfor %}
</div>

## Learning builds (curated)
<div class="mm-card-grid projects-tier projects-tier--learning">
{% for post in learning %}
  {% include archive-single.html %}
{% endfor %}
</div>

## Research case studies (translated)
<div class="mm-card-grid projects-tier projects-tier--research">
{% for post in research %}
  {% include archive-single.html %}
{% endfor %}
</div>

{% if other and other.size > 0 %}
## Other
<div class="mm-card-grid projects-tier projects-tier--other">
{% for post in other %}
  {% include archive-single.html %}
{% endfor %}
</div>
{% endif %}
