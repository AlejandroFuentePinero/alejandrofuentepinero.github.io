---
title: "Courses"
collection: teaching
type: "Undergraduate and Master's courses"
permalink: /teaching/james_cook_university/
venue: "James Cook University"
location: "Townsville, Australia"
date: "2019-01-01"
---

I held 11 teaching roles across 6 courses at James Cook University between 2019 and 2025. I tutored and demonstrated in undergraduate ecology, demonstrated in Master's statistics, helped develop a course, and gave a guest lecture on conservation under climate change.

<ul class="talk-list">
  {% for course in site.data.courses %}
  <li class="talk-row">
    <span class="talk-row__year">{{ course.year }}</span>
    <div>
      <h4 class="talk-row__title">{{ course.course }}</h4>
      <p class="talk-row__venue">{{ course.level }} &middot; {{ course.role }}</p>
      {% if course.lecture %}<p class="talk-row__excerpt">&ldquo;{{ course.lecture }}&rdquo;</p>{% endif %}
    </div>
  </li>
  {% endfor %}
</ul>
