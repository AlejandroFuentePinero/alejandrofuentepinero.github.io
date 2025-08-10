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
{% for post in site.projects reversed %}
  {% include archive-single.html %}
{% endfor %}
</div>
