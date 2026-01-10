---
title: "MLB Analytics with SQL"
excerpt: "End-to-end SQL analytics project using the Lahman Baseball Database. Designed a complete relational workflow with schema creation, reusable views, advanced CTEs, window functions, and business-focused analyses on talent pipelines, salary dynamics, and player careers."
date: 2025-11-24
tier: featured   # featured | learning | research
order: 2
---

## Problem
Historical sports datasets present a classic relational challenge: many tables, long time spans, inconsistent keys, and subtle relationships.  
The Lahman Database (1871–2024) contains **decades of MLB data** covering players, salaries, teams, universities, post-season results, and biographical information.  
The goal of this project is to build a **professional, production-quality SQL analytics workflow** to answer four major baseball questions around talent development, payroll behaviour, career trajectories, and physical performance profiles.

## Approach
- Designed and implemented a fully reproducible **PostgreSQL schema** for the entire Lahman dataset, ensuring correct keys, constraints, and datatypes.
- Created a modular SQL environment with dedicated files for schema, views, analysis queries, advanced queries, and optimised solutions.
- Structured the project around four analytical pillars:
  1. **Talent Pipelines:** Which colleges contribute the most MLB players, and how does this shift by decade?
  2. **Salary & Payroll Dynamics:** Team spending patterns, cumulative payroll milestones, and decade-level comparisons.
  3. **Player Career Analysis:** Career length, debut/retirement windows, age distributions, and team loyalty.
  4. **Player Profiles & Comparison:** Height–weight trends, cross-era comparisons, and physical attributes of standout players.
- Built **reusable analytical views** to avoid repeated logic and keep the workflow clean and maintainable.
- Developed a **Python notebook** (`mlb_visual_analysis.ipynb`) to visualise the most impactful insights from SQL queries, including:
  - Career length distributions  
  - Payroll growth and cumulative spending over time  
  - School-to-MLB talent funnels  
  - Physical attribute comparisons  
- Organised extensive project documentation in `/docs/`: schema design notes, project overview, and business-focused interpretations.

## SQL Concepts Implemented
This project spans the full spectrum of practical SQL used in real analytics and data-engineering workflows:

- **Relational design & data types**
  - Full schema with primary keys, composite keys, foreign keys, and constraints.
  - Work across integers, numerics, booleans, text, and dates, including casting and normalisation.

- **Date & time manipulation**
  - Deriving debut decades with `EXTRACT` + `FLOOR`, building decade indices, and filtering by time windows (e.g., post-1950, post-1995). 
  - Constructing birth dates and computing ages and career lengths using `MAKE_DATE` and `AGE`.

- **Analytical & window functions**
  - Ranking and partitioning with `ROW_NUMBER`, `RANK`, and `NTILE` for salary percentiles and payroll terciles.   
  - Running totals and cumulative metrics using `SUM(...) OVER (PARTITION BY ... ORDER BY ...)` for cumulative team payroll.   
  - Distributional statistics with `PERCENTILE_CONT` for median payrolls and career summaries.
    
- **Data completeness & NULL-aware profiling**
  - Measuring coverage of key fields using COUNT vs COUNT(column) and CASE-based counts.
    
- **Conditional / filtered aggregation**
  - Computing team-level compositions using CASE expressions and FILTER clauses inside aggregates.
    
- **Statistical SQL**
  - Linear trend estimation using `COVAR_POP` / `VAR_POP` to compute per-state slopes in player production over decades.   

- **CTEs and recursive-style pipelines**
  - Multi-step CTE pipelines that layer transformations (e.g., from raw salaries → yearly totals → rank by payroll → join to postseason participation).   
  - Use of CTEs to encapsulate complex logic such as state-decade player counts, Hall of Fame flags, and primary franchise detection based on total games played.

- **Reusable views & optimisation**
  - Canonical views for recurring transformations (debut decades, team-year payroll, average franchise payroll, postseason teams, LCS/WS teams, debut/final teams) that replace duplicated CTE boilerplate and ensure consistent logic across queries. :contentReference[oaicite:8]{index=8}  

- **Business-facing analytics**
  - Identifying top-spending teams, overperforming low-payroll clubs, long-career players, Hall of Fame vs non-HOF career patterns, and state-level growth in talent pipelines.

- **Python integration**
  - Exporting results from SQL and building visualisations with `matplotlib` and `seaborn` to turn query outputs into interpretable charts.

## Stack
- **Database:** PostgreSQL  
- **Languages:** SQL, Python  
- **Libraries:** `pandas`, `matplotlib`, `seaborn` 
- **Environment:** VS Code, Jupyter Notebook, Git/GitHub  
- **Concepts:** schema design, window functions, CTEs, NTILE-based bucketing, statistical SQL, views, data normalisation, analytical SQL, data visualisation

## Results and Impact
* Produced a complete, production-quality SQL analytics system using real multi-table historical data (1871–2024), following sports-analytics pipelines.  
* Demonstrated advanced SQL competency across the full analytical stack, including:
  - Window functions (RANK, NTILE, LAG/LEAD, cumulative aggregates)
  - Statistical SQL (COVAR_POP, VAR_POP trend estimation)
  - Date manipulation and career-length calculations
  - Multi-step CTE pipelines and recursive logic
  - Reusable view architecture for query optimisation
* Delivered interpretable insights for baseball decision-making, such as:
  - Decade-level shifts in college talent pipelines  
  - Team payroll growth and cumulative spending milestones  
  - Long-career vs short-career player characteristics  
  - Identification of low-payroll teams that consistently outperform expectations  
  - Cross-era comparisons of player physical attributes  
* Integrated SQL with Python (`pandas`, `matplotlib`, `seaborn`) to generate clear visualisations for the most impactful queries.  
* Established a clean, reproducible repository structure with separation of schema, views, analysis queries, advanced queries, documentation, and visual analytics — mirroring real-world data-engineering best practices.

## Links & Resources
- **GitHub Repository:**  
  [MLB Analytics SQL Project](https://github.com/AlejandroFuentePinero/MLB_Analytics_Project)
