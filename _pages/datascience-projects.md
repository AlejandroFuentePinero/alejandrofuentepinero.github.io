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

{% assign projects_sorted = site.projects | sort: "order" %}

{% for post in projects_sorted reversed %}
  {% include archive-single.html %}
{% endfor %}

</div>
