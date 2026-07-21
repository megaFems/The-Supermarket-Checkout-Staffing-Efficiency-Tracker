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

```
---

Synthetic Engine (src/bonus_generate_data.py): Generates 2,000 transaction records with embedded real-world defects (text-casing variants, missing branch attributes, and uncapped discounts).

Exploratory Audit (src/01_eda_audit.py): Scans for null values, audits min/max financial profiles, and isolates negative revenue transactions.

ETL Pipeline (src/02_data_pipeline.py): Standardizes text formatting, imputes missing store IDs, clips discount calculations, and engineers temporal features (hour_block, day_of_week).

Aggregation Engine (src/03_aggregate_matrices.py): Builds pivot matrices tracking hourly traffic velocity, peak-hour customer demographics, and payment channel distribution.

Dashboard Renderer (src/04_visualize_dashboard.py): Compiles an executive-ready grid layout combining three core business visualizations into a single high-resolution asset.

---

# Repository Directory Structure
```text
retail-labor-optimization/
│
├── data/
│   ├── raw/
│   │   └── dirty_supermarket_sales_2025.csv    # (Ignored or tracked)
│   └── processed/
│       ├── clean_supermarket_sales_2025.csv
│       ├── matrix_hourly_traffic.csv
│       ├── matrix_hourly_revenue.csv
│       └── matrix_peak_customers.csv
│
├── outputs/
│   ├── figures/
│   │   ├── retail_store_final_dashboard.png
│   │   ├── fiverr_portfolio_heatmap.png
│   │   └── fiverr_portfolio_payment_bottlenecks.png
│   └── reports/
│       └── summary_report.md
│
├── src/
│   ├── __init__.py
│   ├── 01_generate_data.py
│   ├── 02_eda_audit.py
│   ├── 03_data_pipeline.py
│   ├── 04_aggregate_matrices.py
│   └── 05_visualize_dashboard.py
│
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```
-----

💡 Key Analytical Insights
The Bimodal Rush: Transaction traffic follows a minor bump at 12:00 PM before exploding into a primary surge between 17:00 and 18:00 (5 PM - 7 PM), averaging 50+ transactions per hour.

Customer Profile Bottlenecks: Casual ("Normal") shoppers heavily outnumber loyalty members during peak evening surges. Because non-members require longer processing times, lane speed drops during peak volume blocks.

Financial Protection: The diagnostic audit caught active coupon discount leaks where transactions yielded negative revenue (final_amount < 0), safeguarding profit margins.

---

⚡ Quickstart & Execution

1. Clone the repository
   
2. Set up the virtual environment & install dependencies
   
3. Run the full analytics suite

      python src/01_eda_audit.py
      python src/02_data_pipeline.py
      python src/03_aggregate_matrices.py
      python src/04_visualize_dashboard.py


