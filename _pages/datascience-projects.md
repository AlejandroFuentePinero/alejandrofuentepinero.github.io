---
title: "Projects"
layout: archive
permalink: /datascience/projects/
collection: projects
entries_layout: grid
sidebar:
  nav: "datascience"
---

Below are selected case studies (academic + applied) with a data-science focus.

{% include base_path %}
{% for post in site.projects %}
  {% include archive-single.html %}
{% endfor %}
