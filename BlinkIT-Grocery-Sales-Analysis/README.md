Blinkit Grocery Pricing & Catalogue Analysis
Exploratory data analysis of 8,523 product–outlet records across 10 outlets using Python, statistical testing, SQL, and Streamlit.

By Pooja Singh
Python
pandas
NumPy
Matplotlib
Seaborn
SciPy
SQLite
SQL
Plotly
Streamlit
Overview
Findings
Results
Method
Recommendations
Scenario
Warehouse
Data cleaning
Limitations
Run it
Overview
This project investigates product assortment, item-price patterns, outlet formats, category concentration, and data quality in a Blinkit grocery dataset.

The central question
What does the dataset’s Sales column actually measure?

The analysis finds that SKU identity explains approximately 99.97% of the observed variance in Sales (R² = 0.9997). This suggests that the field behaves more like an item-level price measure than transaction-level revenue. This interpretation should be confirmed against the original source documentation and relevant price fields before being treated as definitive.

Important interpretation note
The dataset is an aggregated product–outlet snapshot without transaction quantities or timestamps. The analysis therefore describes catalogue and price patterns, not verified consumer spending, units sold, or realized revenue.

Project at a glance
8,523
Product–outlet records
10
Outlets
1,559
Unique SKUs
16
Item categories
8,523 × 15
Cleaned dataset (rows × columns)
Key findings
Collapse all
SKU identity dominates variation in Sales
SKU identity explains approximately 99.97% of the observed variance in the Sales column. This is consistent with an item-level price-like measure, but does not independently prove that the column is MRP.

Grocery Stores have narrower assortments
The analysis reports an average assortment of approximately 541.5 SKUs per Grocery Store, compared with 930 SKUs per Supermarket. Average item-price values are much closer than the assortment counts, suggesting that the observed total-value gap is primarily associated with catalogue breadth in this dataset.

Store-format mix changes the apparent tier comparison
Tier 2 appears to have the highest overall value in the initial comparison. When the comparison is restricted to Supermarkets, the reported averages are very similar across tiers. This is a composition effect: the mix of store formats affects the unadjusted comparison.

Catalogue value is concentrated in a small number of categories
The top five categories account for 59.03% of the summed Sales values, according to the analysis. Fruits & Vegetables and Snack Foods are the largest contributors. Try it in the chart below.

Correlations with several outlet and product attributes are weak
The reported relationships between Sales and visibility, rating, outlet age, and item weight are small. In particular, a statistically significant result can still be practically negligible when the correlation coefficient is close to zero.

How concentrated is catalogue value?
Share of summed Sales values by item category
Chart
Table
Highlight the top

5
categories
59.03%
of the summed Sales values sit in the top 5 categories
Top 5 categories
Other categories
Fruits and Vegetables
14.82%
Snack Foods
14.60%
Household
11.32%
Frozen Foods
9.87%
Dairy
8.43%
Canned
7.55%
Baking Goods
6.82%
Health and Hygiene
5.66%
Meat
4.95%
Soft Drinks
4.87%
Breads
2.94%
Hard Drinks
2.44%
Others
1.87%
Starchy Foods
1.82%
Breakfast
1.30%
Seafood
0.76%
Category totals come from the notebook output; shares are each category’s summed Sales divided by the total of 1,201,681.49.

Results summary
Metric	Reported result
Sum of Sales values	1,201,681.49
Mean	140.99
Median	143.01
Standard deviation	62.28
Minimum	31.29
Maximum	266.89
Mean rating	3.97 / 5
Records rated exactly 4.0	39.18%
Currency
The source data does not clearly label the currency. Values are therefore presented as currency units, not dollars or rupees, until the source is verified.

Outlet comparison
Summed Sales value by store format
Adds up every outlet in the format
Summed value
Per outlet
Chart
Table
Supermarket Type 1
6 outlets
787,550
Supermarket Type 2
1 outlet
131,478
Supermarket Type 3
1 outlet
130,715
Grocery Store
2 outlets
151,939
Supermarket Type 1 has the largest summed value because it has six outlets, not because each outlet is larger. Switch to per outlet to compare the formats on equal terms.

These figures describe summed values in the Sales column. They should not be interpreted as verified store revenue unless the meaning of Sales is established from the original source.

Methodology
The project is organized around four objectives.

Objective 1
Understand the business and dataset
Review catalogue taxonomy and outlet structure.
Establish baseline metrics and rating patterns.
Objective 2
Improve data reliability
Handle missing values and zero visibility values.
Review duplicates and outliers.
Harmonize inconsistent labels and outlet-size values.
Objective 3
Explore patterns and associations
Compare category and outlet groups.
Examine correlations.
Apply statistical tests, including Kruskal–Wallis tests.
Compare top and bottom cohorts.
Objective 4
Translate findings into decisions
Measure category concentration.
Compare outlets with store-format context.
Identify assortment gaps.
Develop candidate SKU recommendations.
Statistical interpretation
What the 99.97% means
The reported 99.97% figure is a marginal, one-factor SKU-level R². It should not be read as an independent contribution in a variance decomposition where all factors add up to 100%, because SKU identity overlaps with category and other product attributes.

Repeated SKUs across outlets
Multiple rows can represent the same SKU across different outlets. Statistical tests that treat every product–outlet row as independent may understate uncertainty. Results should therefore be treated as exploratory until dependence between repeated SKU observations is addressed in the inferential analysis.

Recommendations
Investigate assortment expansion at Grocery Stores
Use missing-SKU lists as a shortlist for business review, then validate space, availability, and demand before making changes.

Monitor the largest categories
The top five categories represent a substantial share of the summed Sales values in this snapshot.

Compare outlets within store format
Avoid attributing differences to location tier when outlet formats are unevenly represented.

Interpret category differences as price-mix patterns
Average values may reflect differences in the products stocked, not necessarily stronger demand.

Audit visibility against transaction data
The current dataset cannot establish whether visibility affects units sold.

Review rating quality
The concentration of records at a rating of exactly 4.0 may warrant checking how ratings are collected or rounded.

Standardize master data
Review inconsistent fat-content labels, conflicting outlet-size values, and other catalogue inconsistencies.

Validate high-value SKU distribution
Prioritize candidate products for review, but do not interpret catalogue value as demand without transaction data.

Illustrative assortment scenario
The notebook estimates a theoretical catalogue-value opportunity of 109,008.97, based on its assortment-gap assumptions and unrounded values. Treat this as an illustrative scenario, not an incremental revenue forecast: it assumes additional listings can be added and that the Sales value is a suitable proxy for the value of those listings.

If Grocery Stores listed more items
Average listings per outlet, supermarkets vs Grocery Stores
Share of the assortment gap closed

100%
109,008.97
theoretical catalogue value added, 9.07% of the summed Sales values
Listed today
Added in the scenario
Supermarkets
average per outlet
930.0
Grocery Stores
average per outlet
930.0
At 100%: a gap of 388.5 SKUs per Grocery Store × 2 Grocery Stores × the unrounded average Sales value per Grocery Store listing (about 140.29) gives the notebook’s 109,008.97. The slider scales that figure in a straight line, so it is only as reliable as the assumptions above.

SQL warehouse and dashboard
The project includes a SQLite warehouse designed around a star schema.

dim_products
dimension
dim_outlets
dimension
fact_inventory_pricing
fact
All
Tables
Views
Table or view	Type	Purpose
dim_products	Table	Product attributes such as family, category, fat content, and weight
dim_outlets	Table	Outlet attributes such as format, tier, size, establishment year, and age
fact_inventory_pricing	Table	Product–outlet records with the analysed Sales field, visibility, and rating
vw_sku_pricing_variance	View	Variation in Sales by SKU
vw_outlet_assortment_gap	View	Assortment breadth comparison by outlet format
vw_format_controlled_tiers	View	Tier comparisons within the same store format
vw_category_pareto	View	Category concentration and cumulative shares
vw_missing_sku_prioritization	View	Candidate SKUs present in supermarkets but missing from Grocery Stores
The Streamlit dashboard includes
Assortment Expansion Simulator
Pricing Variance & MRP Proof
Tier Comparison Audit
SKU Recommendation Engine
SQL Star Schema Explorer
Dashboard link
Not deployed yet. Run the app locally until then.
Show how
Data cleaning decisions
The analysis documents the following data-quality issues.

Missing item weights: 1,463 rows (17.17%)
Zero item-visibility values: 526 rows
Inconsistent fat-content labels
Conflicting outlet-size values for some outlets
Outliers retained where removal was not justified
Please refer to the notebook for the specific imputation and harmonization rules applied to each field. These decisions should be reviewed alongside the analysis because imputation can influence comparisons between outlet types.

Limitations
The meaning of Sales is not established by the field name alone. The variance pattern suggests a price-like measure, but source documentation or cross-checking against MRP is needed to confirm it.
No transaction quantities are available. Units sold, conversion, realized revenue, and demand cannot be measured directly.
No timestamps are available. Seasonality, trends, and time-series forecasting are out of scope.
The assortment opportunity is theoretical. More listings do not guarantee demand or incremental revenue, and outlet space may constrain expansion.
Statistical independence needs care. Repeated SKUs across outlets can affect the uncertainty of tests that operate on product–outlet rows.
Currency is unlabelled. Values are reported as currency units until verified from the source.
Getting started
Requirements. Use a Python environment compatible with the packages listed in requirements.txt.

Run the notebook
Run the analysis script
Run the dashboard
jupyter notebook BlinkIT_Grocery_Sales_Analysis_v2.ipynb
Copy
Run the notebook cells in order. Confirm that the raw Excel workbook is in the expected folder before running the analysis.

Repository structure
BlinkIT-Grocery-Sales-Analysis/
├── BlinkIT Grocery Data.xlsx
├── BlinkIT_Grocery_Data_Cleaned.csv
├── BlinkIT_Grocery_Sales_Analysis_v2.ipynb
├── run_analysis.py
├── blinkit_warehouse.sql
├── build_warehouse.py
├── app.py
├── requirements.txt
├── dashboard_live_screenshot.png
├── dashboard_preview.png
├── visuals/
└── README.md
Copy
Tools used: Python · pandas · NumPy · Matplotlib · Seaborn · SciPy · SQL · SQLite · Plotly · Streamlit

Author: Pooja Singh

Portfolio note
This is an exploratory analysis of an aggregated catalogue snapshot. Findings are descriptive and should not be interpreted as causal or as verified revenue results without transaction-level and source-definition evidence.
