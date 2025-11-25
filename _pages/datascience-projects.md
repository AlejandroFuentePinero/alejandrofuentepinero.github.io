---
title: "Projects"
layout: archive
permalink: /datascience/projects/
collection: projects
entries_layout: grid
classes: wide
---

Below are selected case studies (academic + applied) with a data-science focus.

{% include base_path %}

{% assign projects_sorted = site.projects | sort: "order" %}
{% for post in projects_sorted %}
  {% include archive-single.html %}
{% endfor %}
