---
title: "MLB Analytics with SQL"
excerpt: "Reusable SQL over 150 years of baseball data answers 4 questions. One finding: the average debutant has grown more than 5 inches taller."
date: 2025-11-24
type: lab
stack:
  - PostgreSQL
  - SQL
  - Python
redirect_from:
  - /datascience/projects/mlb_analytics_sql/
---

Baseball keeps better records than almost any other sport, which makes it a good place to practise SQL on real, messy, long-running data. This lab builds a reusable SQL workflow over 150 years of Major League Baseball (MLB) history, from 1871 to 2024. The source is the Lahman Database of players, salaries, teams, colleges and post-season results. It was driven by 4 questions: where players come from, how money moves, what shape a career takes, and how players' bodies have changed.

It is a practice lab. The point was schema design, reusable views and window functions on a database big enough to punish sloppy queries. A Python notebook turns the query outputs into charts.

## Links

- **Source:** [MLB Analytics SQL Project on GitHub](https://github.com/AlejandroFuentePinero/MLB_Analytics_Project)

## What it covers

Each question gets its own modular SQL over a clean relational schema. Shared logic lives in reusable analytical views, so no analysis repeats itself. The queries lean on window functions, which compute rankings and running totals across rows without collapsing them. Cumulative sums, multi-step common table expressions and population covariance for estimating trends do the rest. Date handling and null-aware profiling round out the toolkit.

## What it found

Only about 28% of players have a documented college, spread across more than 1,100 schools. That pipeline has moved: early talent came from the Northeast and Midwest, modern talent comes from the South and West. Money follows a familiar pattern. The Yankees lead cumulative payroll by a wide margin, the median team spends roughly two thirds of what the top tier spends, and post-season success tracks payroll closely.

Careers are short, and only a minority last a decade. Hall of Fame players debut younger, play longer and play more games than everyone else. Players have also grown: the average debut height has risen from about 5 ft 8 in to more than 6 ft 1 in, with weight rising even faster.

## Stack

PostgreSQL · Python · pandas · matplotlib · seaborn · Git/GitHub
