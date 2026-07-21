# The-Supermarket-Checkout-Staffing-Efficiency-Tracker
End-to-end Python pipeline and executive dashboard optimizing store cashier schedules, identifying register bottlenecks, and preventing POS discount leakage.

# 🛒 Retail Labor & Revenue Optimization Analytics System

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/data-pandas%20%7C%20numpy-orange.svg)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/visualization-seaborn%20%7C%20matplotlib-green.svg)](https://seaborn.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An end-to-end data engineering and operations analytics pipeline designed to optimize store staffing, identify transaction bottlenecks, and eliminate Point-of-Sale (POS) discount leakage across high-volume retail locations.

---

## 📊 Executive Summary Dashboard

![Executive Retail Dashboard](outputs/figures/retail_store_final_dashboard.png)

---

## 📌 Business Problem

Multi-branch retail operations frequently face two opposing financial challenges:
1. **Peak Hour Understaffing:** Long lines between 5:00 PM and 7:00 PM lead to queue abandonment and customer friction.
2. **Off-Peak Wage Leakage:** Overstaffed cashier lanes during low-velocity afternoon blocks inflate labor costs without driving revenue.
3. **Data Integrity Issues:** Uncleaned POS extractions lead to duplicate payment categories and untracked coupon discount leaks.

This project delivers an automated pipeline that cleans POS extraction logs, audits financial anomalies, and compiles a **3-dimensional operational decision framework** to align staffing schedules with real-time consumer traffic.

---

## 🛠️ Data Pipeline Architecture

The framework consists of five modular execution stages:

```text
[ Raw POS Logs ] ──> [ EDA & Diagnostics ] ──> [ Cleaning & Validation Pipeline ]
                                                            │
[ Multi-Chart Visual Dashboard ] <── [ Matrix Aggregations ] ↵
