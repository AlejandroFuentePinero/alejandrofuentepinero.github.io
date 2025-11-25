---
title: "Projects"
layout: archive
permalink: /datascience/projects/
collection: projects
entries_layout: grid
classes: wide
#sidebar:
#  nav: "datascience"
---

Below are selected case studies (academic + applied) with a data-science focus.

<div class="mm-card-grid">
{% include base_path %}

{%- assign ordered_projects   = site.projects | where_exp: "p", "p.order"        | sort: "order" -%}
{%- assign unordered_projects = site.projects | where_exp: "p", "p.order == nil" | sort: "date" | reverse -%}

{%- for post in ordered_projects -%}
  {% include archive-single.html %}
{%- endfor -%}

{%- for post in unordered_projects -%}
  {% include archive-single.html %}
{%- endfor -%}
