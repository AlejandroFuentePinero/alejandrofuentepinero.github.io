---
title: "Python Labs"
excerpt: "Three lab collections cover the fundamentals: object-oriented Python, data analysis and machine learning. The machine learning collection runs from regression to neural networks."
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

Every shipped system on this site rests on fundamentals I practised somewhere first. These 3 lab collections are that somewhere: object-oriented Python systems, exploratory data analysis and classical machine learning. They form one learning progression, and none of them pretends to be more than practice.

Each collection keeps its own repository and its own arc. One runs from procedural scripts to class design, another from raw data to insight, and the third from linear regression to neural networks.

## Links

- **Object-oriented systems:** [python-oop-mini-systems on GitHub](https://github.com/AlejandroFuentePinero/python-oop-mini-systems)
- **Exploratory data analysis:** [python-eda-mini-projects on GitHub](https://github.com/AlejandroFuentePinero/python-eda-mini-projects)
- **Machine learning:** [machine learning course projects on GitHub](https://github.com/AlejandroFuentePinero/python-ML-course-projects)

## Object-oriented Python systems

A series of milestone builds moves from procedural games to multi-class applications. Tic-Tac-Toe practises breaking a program into functions. Blackjack composes Card, Deck, Hand and Chips classes into a working game with betting. A credit card validator implements the Luhn checksum and classifies card types by their prefixes.

The later systems exercise inheritance and polymorphism, where a family of classes shares one interface. A bank account manager routes transfers through checking, savings and business subclasses of a single Account. An inventory system links Inventory and Product classes for create, update and search workflows. A library system tracks Book, Journal and DVD loans across Member records.

## Exploratory data analysis

Two end-to-end pipelines practise the arc from cleaning to insight. The 911 calls analysis pulls time features out of emergency call records and maps call volumes by reason, day and month. The finance analysis pulls price data for several banks, computes moving averages and returns, and reads how the stocks move together from correlation matrices.

## Machine learning

Eleven notebooks cover the classical toolkit in scikit-learn and end with neural networks in TensorFlow and Keras. Regression and classification come first: linear and logistic regression, K-nearest neighbours, decision trees, random forests and support vector machines. Then K-means clustering and principal component analysis, which compresses many features into a few, cover the unsupervised side.

Naive Bayes text classification and a similarity-based recommender complete the classical set. The last 3 notebooks build feedforward neural networks in Keras for regression, for classification, and for a credit-risk problem on LendingClub-style loan data.

## Stack

Python 3 · pandas · NumPy · matplotlib · seaborn · Plotly · scikit-learn · TensorFlow · Keras · Jupyter · Git/GitHub
