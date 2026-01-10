---
layout: archive
title: "Projects"
permalink: /datascience/projects/
collection: projects
author_profile: true
classes: wide projects-page
entries_layout: grid
---

This page is a map of my data-science work, grouped into three tiers:

> Flagship Projects: end-to-end projects where I solved a real problem and delivered a working app/pipeline with reproducible architecture, orchestration, and documented outputs.
> Research Projects: research-grade modelling and analytics work presented in a DS format, where the primary deliverable is an analysis/paper/report (methods, validation, and findings).
> Skill Labs: short, focused projects built to implement and cement specific techniques (e.g., ML workflows, EDA patterns, OOP systems) through hands-on application.

If you’re short on time: start with Flagship Projects, then scan one Research Project.


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

## Flagship Projects
End-to-end projects where I solved a real problem and delivered a working app/pipeline with reproducible architecture, orchestration, and documented outputs.
<div class="mm-card-grid projects-tier projects-tier--featured">
{% for post in featured %}
  {% include archive-single.html %}
{% endfor %}
</div>

## Research Projects
Rigorous modelling/analysis projects where the primary deliverable is a paper or report, presented in a data-science format (methods, validation, and decision-relevant insights).
<div class="mm-card-grid projects-tier projects-tier--research">
{% for post in research %}
  {% include archive-single.html %}
{% endfor %}
</div>

## Skill Labs
Short, focused projects built to implement and cement specific techniques through hands-on application.
<div class="mm-card-grid projects-tier projects-tier--learning">
{% for post in learning %}
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
