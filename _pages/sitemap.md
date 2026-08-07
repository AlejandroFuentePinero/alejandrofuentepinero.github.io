---
layout: default
title: "Sitemap"
permalink: /sitemap/
---

<div class="container page-block">
  <header class="page-header">
    <h1>Sitemap</h1>
    <p>Every page on the site, one line each. Robots can digest the <a href="{{ '/sitemap.xml' | relative_url }}">XML version</a>.</p>
  </header>

  <section class="section">
    <h2>Pages</h2>
    <ul>
      <li><a href="{{ '/' | relative_url }}">Home</a></li>
      <li><a href="{{ '/work/' | relative_url }}">Work</a>: timeline, education, grants and awards, CV</li>
      <li><a href="{{ '/projects/' | relative_url }}">Projects</a>: engineering, research and lab projects in one grid</li>
      <li><a href="{{ '/apps/' | relative_url }}">Apps</a>: live, usable systems</li>
      <li><a href="{{ '/research/' | relative_url }}">Research</a>: publications, talks, teaching, book chapters</li>
      <li><a href="{{ '/research/threatened-species/' | relative_url }}">Threatened species nominations</a></li>
      <li><a href="{{ '/contact/' | relative_url }}">Contact</a></li>
      <li><a href="{{ '/terms/' | relative_url }}">Terms and privacy policy</a></li>
    </ul>
  </section>

  <section class="section">
    <h2>Projects</h2>
    <ul>
      {% assign projects = site.projects | sort: "date" | reverse %}
      {% for project in projects %}
      <li><a href="{{ project.url | relative_url }}">{{ project.title }}</a> ({{ project.type }}, {{ project.date | date: "%Y" }})</li>
      {% endfor %}
    </ul>
  </section>

  <section class="section">
    <h2>Publications</h2>
    <ul>
      {% assign publications = site.publications | sort: "date" | reverse %}
      {% for publication in publications %}
      <li><a href="{{ publication.url | relative_url }}">{{ publication.title }}</a> (<em>{{ publication.venue }}</em>, {{ publication.date | date: "%Y" }})</li>
      {% endfor %}
    </ul>
  </section>

  <section class="section">
    <h2>Talks</h2>
    <ul>
      {% assign talks = site.talks | sort: "date" | reverse %}
      {% for talk in talks %}
      <li>{% if talk.redirect_to %}{{ talk.title }}{% else %}<a href="{{ talk.url | relative_url }}">{{ talk.title }}</a>{% endif %} ({{ talk.venue }}, {{ talk.date | date: "%Y" }})</li>
      {% endfor %}
    </ul>
  </section>

  <section class="section">
    <h2>Posts</h2>
    <ul>
      {% for post in site.posts %}
      <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> ({{ post.date | date: "%Y" }})</li>
      {% endfor %}
    </ul>
  </section>
</div>
