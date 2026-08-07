---
title: "MLB Analytics with SQL"
excerpt: "A reusable SQL workflow answered 4 questions on 150 years of baseball data, from college talent pipelines to payroll overperformance."
date: 2025-11-24
type: lab
stack:
  - PostgreSQL
  - SQL
  - Python
redirect_from:
  - /datascience/projects/mlb_analytics_sql/
---

This lab built a reusable SQL workflow over 150 years of Major League Baseball (MLB) data. 4 business questions drove it: talent pipelines, salary dynamics, career shapes and player profiles. The source is the Lahman Database, 1871 to 2024, spanning players, salaries, teams, universities and post-season results.

It is a practice lab: the point was schema design, reusable views and window functions on a real database. A Python notebook turns the query outputs into charts.

## Links

- **Source:** [MLB Analytics SQL Project on GitHub](https://github.com/AlejandroFuentePinero/MLB_Analytics_Project)

## What it covers

Each question gets modular SQL over a clean relational schema. Reusable analytical views hold the shared logic, so no analysis repeats itself. The queries use ranking and tiling window functions, cumulative sums, multi-step common table expressions and population covariance for trend estimation. Date handling and null-aware profiling round out the toolkit.

## What it found

Some low-payroll teams consistently beat expectations. College talent pipelines shifted visibly by decade. Physical attributes separate Hall of Fame careers from the rest. Career length, debut and retirement windows follow clear era patterns.

## Stack

PostgreSQL · Python · pandas · matplotlib · seaborn · Git/GitHub
