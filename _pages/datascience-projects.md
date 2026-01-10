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
* Flagship Projects: end-to-end builds that ship a working app/pipeline with reproducible architecture and documented outputs.
* Research Projects: research-grade modelling and analytics work presented in a DS format, where the primary deliverable is a peer-reviewed paper in an international scientific journal.
* Skill Labs: short, focused builds created to implement and cement specific techniques through hands-on practice.


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

---

## Flagship Projects
Working apps/pipelines with reproducible architecture and documented outputs.
<div class="mm-card-grid projects-tier projects-tier--featured">
{% for post in featured %}
  {% include archive-single.html %}
{% endfor %}
</div>

---

## Research Projects
Peer-reviewed modelling/analytics work presented in a DS case-study format.
<div class="mm-card-grid projects-tier projects-tier--research">
{% for post in research %}
  {% include archive-single.html %}
{% endfor %}
</div>

---

## Skill Labs
Short technique-focused builds used to cement specific skills.
<div class="mm-card-grid projects-tier projects-tier--learning">
{% for post in learning %}
  {% include archive-single.html %}
{% endfor %}
</div>

---

{% if other and other.size > 0 %}
## Other
<div class="mm-card-grid projects-tier projects-tier--other">
{% for post in other %}
  {% include archive-single.html %}
{% endfor %}
</div>
{% endif %}
