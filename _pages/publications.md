---
layout: archive
title: "Publications"
permalink: /academic/publications/
author_profile: true
sidebar:
  nav: "academic"
---

You can also find my articles on <u><a href="https://scholar.google.com.au/citations?view_op=list_works&hl=en&user=7CKVdZwAAAAJ">my Google Scholar profile</a>.</u>

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
