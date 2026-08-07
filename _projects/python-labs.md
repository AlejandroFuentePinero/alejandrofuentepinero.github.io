---
title: "Python Labs"
excerpt: "Three lab collections: object-oriented Python systems, exploratory data analysis, and classical machine learning, built as one learning progression."
date: 2025-10-15
type: lab
stack:
  - Python
  - pandas
  - scikit-learn
redirect_from:
  - /datascience/projects/python_eda_mini_projects/
  - /datascience/projects/python-ML-projects/
  - /datascience/projects/python_oop_minisystems/
---

## Python OOP Systems: From Procedural to Object-Oriented Design

### Problem
Transitioning from analytical scripting to **structured software development** requires mastery of programming fundamentals — including control flow, modular design, encapsulation, and class hierarchies.  
**Goal:** Build a progression of small but complete Python systems that demonstrate increasing complexity — from procedural games to multi-class object-oriented applications — consolidating software engineering skills for data and analytics workflows.

### Approach
- Designed a **series of milestone projects** advancing from basic function decomposition (Tic-Tac-Toe) to full class orchestration (Library System).  
- Implemented **OOP principles** such as composition, inheritance, and polymorphism across multiple domains (banking, scheduling, inventory, lending).  
- Applied defensive programming, algorithmic reasoning (e.g., Luhn algorithm for credit card validation), and structured error handling.  
- Developed reusable CLI systems emphasizing clean interaction loops, input validation, and modular code structure.  
- Organized all projects into a unified, documented repository for maintainability and demonstration of cumulative learning.

### Stack
- **Language:** Python 3  
- **Core libraries:** `datetime`, `re`, `sys`, `os`  
- **Programming concepts:** procedural programming, OOP (classes, composition, inheritance, polymorphism), algorithms, CRUD logic, state management  
- **Development tools:** Jupyter Notebook, VS Code, Git/GitHub for version control

### Examples
- **Tic-Tac-Toe (CLI):** procedural function decomposition for board rendering, validation, and replay loop.  
- **Blackjack (CLI):** class composition (`Card`, `Deck`, `Hand`, `Chips`) for game logic and state control.  
- **Credit Card Validator:** implemented the **Luhn algorithm** and rule-based card classification (Visa/MasterCard).  
- **Bank Account Manager:** inheritance and polymorphism with `Account` subclasses and `Bank` orchestration for transfers.  
- **Product Inventory:** CRUD system linking `Inventory` and `Product` classes for add/remove/update/search workflows.  
- **Library Lending System:** inheritance and polymorphism with `Item` subclasses (`Book`, `Journal`, `DVD`), plus `Member` and `Loan` tracking.

### Results
- Demonstrated **strong OOP understanding** through layered class systems and interactive logic.  
- Built a portfolio of clean, modular codebases representing **progressive software design complexity**.  
- Established a foundation for scaling Python skills into data engineering, analytics, and applied ML workflows.

### Impact
- Consolidated **core programming fluency** — a prerequisite for professional data science and AI development.  
- Provided a public reference repository that documents **learning-to-implementation progression**, showcasing both conceptual and practical mastery.  
- Serves as a teaching and reference tool for future learners or collaborators seeking to understand Python OOP fundamentals in action.

### Links & Resources
- 💻 **Code repository:** [GitHub – Python OOP Mini-Systems](https://github.com/AlejandroFuentePinero/python-oop-mini-systems)

## Exploratory Data Analysis (EDA) Projects in Python

### Problem
Data scientists often encounter diverse datasets requiring tailored cleaning, transformation, and exploratory techniques before modelling.  
**Goal:** Build a reproducible Python EDA framework demonstrating how to extract insights, engineer features, and communicate patterns from unstructured datasets across different domains — public safety (911 calls) and financial markets.

### Approach
- Designed two **end-to-end EDA pipelines** using real-world datasets:
  1. **911 Calls Analysis:** time and location-based patterns of emergency calls.
  2. **Finance Data Analysis:** stock price behaviour, returns, and inter-company correlations.
- Implemented **data ingestion → cleaning → transformation → visualisation** using pandas and numpy for data handling and seaborn/plotly for insight communication.
- Created reusable analysis templates for:
  - Date/time feature engineering (`.dt` accessors, grouping, resampling)
  - String and categorical handling (type conversion, feature splitting)
  - Correlation and pairwise analysis
  - Multi-panel and interactive visualisations for pattern discovery.

### Stack
- **Language:** Python 3  
- **Libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`, `datetime`  
- **Tools:** Jupyter Notebook, Git/GitHub  
- **Concepts:** EDA, data cleaning, feature extraction, time series analysis, correlation analysis, visualisation design

### Case Studies

#### **1. 911 Calls EDA**
**Objective:** Explore temporal and spatial patterns in emergency call data.  
- Parsed timestamps into year, month, day, and hour features for time-based analysis.  
- Mapped call reasons and types to broader categories (e.g., EMS, Fire, Traffic).  
- Visualised daily and monthly call volume, call-type distributions, and temporal trends.  
- Identified operational peaks and seasonal call variation patterns.

**Skills:** datetime manipulation, grouping and aggregation, categorical encoding, visualisation (line, bar, count, heatmap).

---

#### **2. Finance Data EDA**
**Objective:** Investigate stock price dynamics and inter-company behaviour.  
- Collected multi-stock price data via Yahoo Finance API.  
- Calculated moving averages, daily returns, and cumulative returns.  
- Conducted pairwise correlation and risk–return analysis across multiple tickers.  
- Visualised price trends and co-movement patterns through heatmaps and scatter matrices.

**Skills:** time-series analysis, rolling windows, correlation matrices, multi-plot visual storytelling.

---

### Results
- Demonstrated **consistent EDA methodology** applicable across domains.  
- Built a reproducible framework highlighting how to structure exploratory workflows for both categorical–temporal and continuous–financial data.  
- Strengthened proficiency in **data storytelling and visualisation** using modern Python tools.

### Impact
- Forms the **analytical bridge** between raw data handling and predictive modelling.  
- Provides an adaptable template for future projects involving data cleaning and insight extraction.  
- Complements the “Python OOP Mini-Systems” repository by demonstrating **data-centric rather than logic-centric** Python application.

### Links & Resources
- 💻 **Code repository:** [GitHub – Python EDA Projects](https://github.com/AlejandroFuentePinero/python-eda-mini-projects)

## Machine Learning Projects in Python

### Problem
Mastering machine learning requires understanding both theory and practice — how algorithms behave with real data, how to prepare features, and how to evaluate model performance. Here, I showcase a collection of hands-on machine learning projects. Each project demonstrates end-to-end implementation of key algorithms, emphasising data preparation, model training, evaluation, and interpretation.

### Approach
- Created a structured repository with subprojects covering:
  - **Regression:** Linear and Polynomial Regression  
  - **Classification:** Logistic Regression, K-Nearest Neighbours (KNN), Decision Trees, Random Forests, Support Vector Machines (SVM) 
  - **Ensemble Methods:** Gradient Boosting, XGBoost  
  - **Clustering:** K-Means, Hierarchical Clustering  
  - **Dimensionality Reduction:** Principal Component Analysis (PCA)  
  - **Natural Language Processing (NLP):** Naive Bayes text classification and TF-IDF feature extraction  
  - **Deep Learning:** Neural Networks using TensorFlow and Keras  
- Implemented complete **data preprocessing → model training → evaluation → visualization** workflows using Scikit-learn and supporting libraries.  
- Emphasised algorithmic intuition through visual diagnostics (e.g., decision boundaries, feature importance, ROC curves). 

### Stack
- **Language:** Python 3  
- **Libraries:** `scikit-learn`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `xgboost`, `tensorflow`, `keras`  
- **Environment**: Jupyter Notebook, Git/GitHub  
- **Concepts:** EDA, data manipulation, supervised & unsupervised learning, model validation, scaling, feature engineering, interpretability, neural networks

### Structure
Each section of the repository represents a standalone ML project:
1. Linear Regression  
2. Logistic Regression  
3. K-Nearest Neighbors (KNN)  
4. Decision Trees and Random Forests  
5. Support Vector Machines (SVM)  
6. K-Means Clustering  
7. Principal Component Analysis (PCA)  
8. Recommender Systems  
9. Natural Language Processing (NLP)  
10. Neural Nets and Deep Learning with TensorFlow and Keras
11. Cross-validation
12. Introduction to Big Data and PySpark workflows

### Results and Impact
* Developed a complete, modular portfolio of ML workflows covering predictive and unsupervised methods.
* Strengthened understanding of data preparation, evaluation metrics, and model trade-offs.
* Strengthened proficiency in data storytelling and visualisation using modern Python tools.
* This repository establishes a practical foundation for model interpretability and applied machine learning, bridging exploratory data analysis and advanced AI workflows. It complements the Python OOP Mini-Systems, EDA Projects, and Coding Challenges repositories as part of a coherent learning progression.

### Links & Resources
- 💻 **Code repository:** [GitHub – Machine Learning Fundamentals](https://github.com/AlejandroFuentePinero/python-ML-course-projects)
