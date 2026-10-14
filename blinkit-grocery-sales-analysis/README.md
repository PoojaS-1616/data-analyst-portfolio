# BlinkIT Grocery Pricing Architecture & Catalogue Assortment Analysis

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458.svg)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-green.svg)](https://seaborn.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)]()

> An end-to-end exploratory data analysis, statistical hypothesis testing, and business optimization project evaluating **8,523 product-outlet combinations** across **1,559 SKUs** and **10 fulfillment outlets** for Blinkit, examining catalogue pricing architecture, assortment breadth, and store-level economics.

> **Note on Currency:** The raw dataset contains unlabelled numerical values. While Blinkit operates in India using Indian Rupees (₹), values in this project are formatted with $ to adhere to standard global portfolio reporting conventions, with identical numerical interpretations and mathematical findings.

---

## 📌 Executive Summary

Blinkit operates distributed quick-commerce dark stores across Indian urban tiers. This project investigates store-level pricing architecture, fulfillment format economics, and catalogue assortment breadth.

### 🌟 Key Analytical Discoveries:
1. **The Nature of "Sales":** A variance decomposition reveals that `Item Identifier` (SKU) explains **99.97% of the variance in `Sales`** ($R^2 = 0.9997$), with a within-SKU standard deviation of only **$1.15** (against **$62.28** overall). `Outlet Identifier` explains only **0.03%**. The column **behaves like / is consistent with Item Retail Price (MRP)** with minor store pricing variation.
2. **Mechanical Price Parity:** Mean sales per stocked record fall in a tight band of **$139.42 to $143.12** across all 10 outlets. This is a mathematical consequence of sampling from the same price catalogue.
3. **The Assortment Gap:** The lower revenue in Grocery Stores ($75,970 vs ~$131,258 in supermarkets) is **associated with catalogue assortment breadth**—they stock ~541.5 SKUs compared to ~930.0 SKUs in Supermarkets.
4. **Catalogue Potential Uplift:** Expanding Grocery Store catalogues by 388.5 SKUs to match supermarket levels represents a theoretical catalogue inventory value of **+$109,009 (+9.07% network expansion)**.
5. **Debunking the "Tier 2 Myth" (Composition Effect):** Tier 2 appeared superior overall ($131,050 vs $118,033 in Tier 3 and $112,133 in Tier 1) *only* because Tier 2 contains zero Grocery Stores. This is a **composition effect (confounding by store format)**. Among Supermarkets alone, revenue per store is identical across all tiers (**Tier 1: $131,295, Tier 2: $131,050, Tier 3: $131,334**).
6. **Pareto Assortment Concentration:** Category share of listings correlates **0.997** with category share of sales. The top 5 categories (**Fruits & Vegetables, Snack Foods, Household, Frozen Foods, Dairy**) comprise **57.26%** of all listings and generate **59.03% ($709,370)** of total network revenue.
7. **Zero Correlation Drivers:** Product display visibility ($r = -0.0060, p = 0.58$), customer rating ($r = 0.0113, p = 0.30$), and store longevity ($r = 0.0007, p = 0.95$) exhibit zero linear correlation with product sales.

---

## 🗂️ Project Deliverables & Structure

```text
blinkit-grocery-sales-analysis/
├── BlinkIT_Grocery_Sales_Analysis.ipynb   # Main Jupyter Notebook (47 cells, 28 code cells + 10 figures / 13 panels)
├── BlinkIT_Grocery_Data_Cleaned.csv      # Cleaned & feature-engineered dataset (8,523 rows x 15 cols)
├── BlinkIT_Grocery_Data.xlsx             # Primary raw dataset (also supports BlinkIT Grocery Data.xlsx)
├── Project_Explanation.md                # In-depth technical manual, math derivations & interview defense guide
├── README.md                             # Project overview and quickstart documentation
├── requirements.txt                      # Project dependency specification
├── .gitignore                            # Standard git exclusions (with leading dot)
├── run_analysis.py                       # Automated standalone execution pipeline (exports visuals/)
└── visuals/                              # Directory containing 10 exported figures (13 panels)
```

---

## 🎯 Analytical Roadmap (4 Objectives, 16 Tasks)

| Phase | Tasks Covered | Core Deliverable / Method |
|---|---|---|
| **Objective 1: Understand the Business** | Tasks 1.1 – 1.4 | Assortment profiling (Food 71.87%, Non-Consumable 18.76%, Drinks 9.37%), outlet network mapping (10 stores), baseline financial metrics ($1.20M total, $140.99 mean, symmetric distribution from $31.29 to $266.89 with skewness $\approx 0.13$), and customer rating clustering analysis (39.18% at 4.0). |
| **Objective 2: Make Data Reliable** | Tasks 2.1 – 2.4 | Cross-outlet SKU mean imputation for Item Weight (17.16% missing), zero-visibility repair (526 rows with bias diagnosis), duplicate audit (0 found), IQR outlier evaluation (100% retained with domain rationale), fat label harmonization, and labeling split stores (OUT010, OUT017, OUT045) as `Unknown`. |
| **Objective 3: What Drives Sales?** | Tasks 3.1 – 3.4 | Category and fat content performance, 2x4 outlet factor matrix, variance decomposition ($R^2 = 0.9997$ on SKU), Pearson correlation testing, Kruskal-Wallis non-parametric ANOVA ($H = 107.30, p = 5.31 \times 10^{-16}$ across categories), and Top 25% vs Bottom 25% cohort segmentation. |
| **Objective 4: Business Decisions** | Tasks 4.1 – 4.4 | Pareto category catalogue analysis (Top 5 = 59.03%, Top 8 = 79.06%, Top 10 = 88.87%), per-outlet fair normalization (composition effect analysis), assortment breadth opportunity modeling (+$109k, 9.07%), and 8 strategic recommendations. |

---

## 🚀 Quickstart & Installation

### 1. Clone or Open Workspace
```bash
cd blinkit-grocery-sales-analysis
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Analysis
You can execute the analysis in two ways:

#### Option A: Interactive Jupyter Notebook
Open `BlinkIT_Grocery_Sales_Analysis.ipynb` in VS Code or Jupyter and choose **Kernel > Restart and Run All**.

#### Option B: Standalone Terminal Execution Pipeline
```bash
python run_analysis.py
```
This executes the complete data pipeline, displays formatted terminal metrics, and exports all high-resolution figures into the `visuals/` directory without deprecation warnings.

---

## 📊 Core Figures Included (10 Figures, 13 Panels)

- **Figure 1 (2 Panels):** Product Category Frequency & Product Family Donut Chart
- **Figure 2 (2 Panels):** Outlet Format & Urban Location Tier Distribution
- **Figure 3 (1 Panel):** Overall Sales Density Distribution with KDE & Central Tendency Lines
- **Figure 4 (2 Panels):** Rating Spike Distribution & Category Average Rating Bar Chart
- **Figure 5 (4 Panels):** Boxplot Quad-Grid for IQR Statistical Outlier Detection
- **Figure 6 (2 Panels):** Total Category Revenue vs. Average Unit Price per Category
- **Figure 7 (8 Panels):** 2x4 Comprehensive Outlet Matrix (Proving Per-Item Price Parity: $139.42 to $143.12)
- **Figure 8 (3 Panels):** Pearson Correlation Heatmap & Scatter Regression Trendlines
- **Figure 9 (2 Panels):** Top 25% vs Bottom 25% Sales Cohort Composition
- **Figure 10 (1 Panel):** Pareto Cumulative Catalogue Concentration Analysis Chart

---

## 💡 Strategic Recommendations for Leadership

1. **Assortment Expansion in Grocery Stores:** Expand SKU count in `OUT010` and `OUT019` from ~541.5 to ~930.0 SKUs to unlock **+$109,009 (+9.07%)** in catalogue value potential.
2. **Maintain Assortment Depth in Top 5 Categories:** Prioritize stock replenishment for Fruits & Veg, Snacks, Household, Frozen, and Dairy to protect **59.03% ($709,370)** of catalogue coverage.
3. **Standardize Store Format over City Tier:** Supermarkets perform identically across all tiers (~$131.2k/store). Standardize dark store format rather than prioritizing specific city tiers.
4. **Acknowledge Category Price Tiers:** Recognize that lower unit prices in Baking Goods ($126.43) reflect product unit economics (MRP), not operational failure.
5. **Audit In-App Visibility vs Unit Volume:** In-app visibility shows no correlation with price ($r = -0.0060$); evaluate visibility against actual unit transaction logs when available.
6. **Redesign Customer Feedback:** Shift from single 1-5 ratings (39.18% at 4.0) to multidimensional metrics (Freshness, Delivery Speed, Packaging).
7. **Master Data Governance:** Resolve conflicting store size records and standardize product classifications across IT systems.
8. **Optimize High-MRP SKU Distribution:** Broaden distribution of high-unit-price SKUs, recognizing that total SKU sales mathematically reflects store count $\times$ price ($r = 0.53$).

---

## 👤 Author
**Pooja Singh**  
*Data Science & Business Analytics*
