---
title: "SQL Coding Challenges"
excerpt: "Ongoing SQL interview-practice log (DataLemur-style) to keep querying sharp alongside flagship projects, with emphasis on core analytical patterns (joins, CTEs, window functions, time series, cohorts)."
tags: [SQL, analytics, window-functions, CTE, joins, time-series, cohort-analysis, interview-practice]
date: 2025-12-20
order: 7
---

## Overview
**Goal:** Maintain strong, interview-ready SQL fluency in parallel with flagship projects through short, focused challenges.  
Each entry captures the problem type and the key SQL pattern(s) used, building a lightweight evidence trail of consistent practice.

---

## Approach
- Solve short, interview-style SQL problems (e.g., DataLemur).
- Emphasis on:
  - Correctness under edge cases (duplicates, ties, NULLs, missing dates).
  - Clear query structure (CTEs, readable joins, well-scoped window functions).
  - Reusable mental patterns (Top-N per group, retention, rolling metrics, de-dup).

---

## Focus Areas
- **Joins & Anti-joins:** existence checks, missing records, deduped joins  
- **CTEs:** multi-step transformations, readability, intermediate validation  
- **Window Functions:** rank/dense_rank, lag/lead, rolling aggregations  
- **Time Series:** daily/weekly aggregates, rolling windows, period comparisons  
- **Cohorts & Funnels:** retention, conversion, step drop-off

---

## Challenge Log
Add new challenges as you complete them. Keep notes short and pattern-focused.

| # | Date | Platform | Source | Challenge | Difficulty | Core Pattern(s) | Notes |
|---:|:-----|:---------|:-------|:----------|:----------:|:----------------|:------|
| 1 | 20/12/2025 | DataLemur | Twitter | Histogram of Tweets | Easy | `CTE`, `group_by`, `histogram` | Two-stage aggregation: tweets per user → count users per bucket |
| 2 | 20/12/2025 | DataLemur | LinkedIn | Data Science Skills | Easy | `group_by`, `having`, `set_filter` | Filter to required skills, then HAVING count = 3 |
| 3 | 20/12/2025 | DataLemur | Facebook | Page With No Likes | Easy | `left_join`, `COALESCE`, `zero_count` | Left join + COALESCE to treat NULL likes as 0 |
| 4 | 20/12/2025 | DataLemur | Tesla | Unfinished Parts | Easy | `NULL_filter` | `WHERE finish_date IS NULL` |
| 5 | 20/12/2025 | DataLemur | Uber | User's Third Transaction | Medium | `window_row_number`, `CTE` | Row-number per user ordered by date, filter rn = 3 |
| 6 | 20/12/2025 | DataLemur | FAANG | Second Highest Salary | Medium | `dense_rank`, `dedup_ties` | Distinct salaries + dense_rank to handle duplicates |
| 7 | 20/12/2025 | DataLemur | Snapchat | Sending vs. Opening Snaps | Medium | `pivot_case_when`, `percent_calc`, `CTE` | Conditional aggregation pivot + percent of total time |
| 8 | 20/12/2025 | DataLemur | NY Times | Laptop vs. Mobile Viewership | Easy | `conditional_aggregation`, `CASE` | Conditional SUM by device bucket |
| 9 | 22/12/2025 | DataLemur | Twitter | 3-Day Rolling Average Tweets | Medium | `window_avg`, `partition_by`, `order_by`, `window_frame` | Rolling average per user using window `AVG() OVER (...)`; ensure correct frame (often `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` after daily aggregation) |
| 10 | 22/12/2025 | DataLemur | Google | Odd and Even Measurements | Medium | `row_number`, `window_function`, `partition_by`, `FILTER`, `modulo` | Assign row_number within each day by time; sum values where rn%2=1 (odd) vs rn%2=0 (even) using FILTER |





---

## Stack
- **Language:** SQL (PostgreSQL-style)
- **Environment:** DataLemur (browser) + local notes

---

## Impact
- Keeps SQL fluency current through consistent repetition of high-frequency interview patterns.
- Reinforces correctness under common edge cases (ties, duplicates, NULL handling).
- Complements the full-scale SQL portfolio project by demonstrating ongoing practice and readiness.
