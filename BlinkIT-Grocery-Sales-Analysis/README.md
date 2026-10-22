Blinkit Grocery Pricing & Catalogue Analysis
Exploratory data analysis of 8,523 product--outlet records across 10
outlets using Python, statistical testing, SQL, and Streamlit.

This project investigates product assortment, item-price patterns,
outlet formats, category concentration, and data quality in a Blinkit
grocery dataset.

The central question is: What does the dataset's Sales column
actually measure?

The analysis finds that SKU identity explains approximately 99.97% of
the observed variance in Sales ((R^2 = 0.9997)). This suggests that
the field behaves more like an item-level price measure than
transaction-level revenue. This interpretation should be confirmed
against the original source documentation and relevant price fields
before being treated as definitive.
Important interpretation note: The dataset is an aggregated
product--outlet snapshot without transaction quantities or timestamps.
The analysis therefore describes catalogue and price patterns, not
verified consumer spending, units sold, or realized revenue.

Project at a glance
- Records: 8,523 product--outlet combinations
- Outlets: 10
- Unique SKUs: 1,559
- Item categories: 16
- Cleaned dataset: 8,523 rows × 15 columns
- Tools: Python, pandas, NumPy, Matplotlib, Seaborn, SciPy,
  SQLite, SQL, Plotly, Streamlit
Key findings
1. SKU identity dominates variation in Sales
SKU identity explains approximately 99.97% of the observed variance in
the Sales column. This is consistent with an item-level price-like
measure, but does not independently prove that the column is MRP.
2. Grocery Stores have narrower assortments
The analysis reports an average assortment of approximately 541.5 SKUs
per Grocery Store, compared with 930 SKUs per Supermarket. Average
item-price values are much closer than the assortment counts, suggesting
that the observed total-value gap is primarily associated with catalogue
breadth in this dataset.
3. Store-format mix changes the apparent tier comparison
Tier 2 appears to have the highest overall value in the initial
comparison. When the comparison is restricted to Supermarkets, the
reported averages are very similar across tiers. This is a composition
effect: the mix of store formats affects the unadjusted comparison.
4. Catalogue value is concentrated in a small number of categories
The top five categories account for 59.03% of the summed Sales
values, according to the analysis. Fruits & Vegetables and Snack Foods
are the largest contributors.
5. Correlations with several outlet and product attributes are weak
The reported relationships between Sales and visibility, rating,
outlet age, and item weight are small. In particular, a statistically
significant result can still be practically negligible when the
correlation coefficient is close to zero.
Results summary
  Metric                        Reported result
  Sum of Sales values            1,201,681.49
  Mean                                   140.99
  Median                                 143.01
  Standard deviation                      62.28
  Minimum                                 31.29
  Maximum                                266.89
  Mean rating                          3.97 / 5
  Records rated exactly 4.0              39.18%

Currency: The source data does not clearly label the currency.
Values are therefore presented as currency units, not dollars or
rupees, until the source is verified.
Outlet comparison
  Store format              Outlets     Reported total Reported value per
                                         Sales value outlet
  Supermarket                     6         787,549.89 131,258.32
  Type 1                                               

  Supermarket                     1         131,477.78 131,477.78
  Type 2                                               

  Supermarket                     1         130,714.67 130,714.67
  Type 3                                               
  Grocery Store                   2         151,939.15 75,969.57
These figures describe summed values in the Sales column. They should
not be interpreted as verified store revenue unless the meaning of
Sales is established from the original source.
Methodology
The project is organized around four objectives:
1. Understand the business and dataset
   - Review catalogue taxonomy and outlet structure.
   - Establish baseline metrics and rating patterns.
2. Improve data reliability
   - Handle missing values and zero visibility values.
   - Review duplicates and outliers.
   - Harmonize inconsistent labels and outlet-size values.
3. Explore patterns and associations
   - Compare category and outlet groups.
   - Examine correlations.
   - Apply statistical tests, including Kruskal--Wallis tests.
   - Compare top and bottom cohorts.
4. Translate findings into decisions
   - Measure category concentration.
   - Compare outlets with store-format context.
   - Identify assortment gaps.
   - Develop candidate SKU recommendations.
Statistical interpretation
The reported 99.97% figure is a marginal, one-factor SKU-level
(R^2). It should not be read as an independent contribution in a
variance decomposition where all factors add up to 100%, because SKU
identity overlaps with category and other product attributes.

Multiple rows can represent the same SKU across different outlets.
Statistical tests that treat every product--outlet row as independent
may understate uncertainty. Results should therefore be treated as
exploratory until dependence between repeated SKU observations is
addressed in the inferential analysis.
Recommendations
1. Investigate assortment expansion at Grocery Stores. Use
   missing-SKU lists as a shortlist for business review, then validate
   space, availability, and demand before making changes.
2. Monitor the largest categories. The top five categories
   represent a substantial share of the summed Sales values in this
   snapshot.
3. Compare outlets within store format. Avoid attributing
   differences to location tier when outlet formats are unevenly
   represented.
4. Interpret category differences as price-mix patterns. Average
   values may reflect differences in the products stocked, not
   necessarily stronger demand.
5. Audit visibility against transaction data. The current dataset
   cannot establish whether visibility affects units sold.
6. Review rating quality. The concentration of records at a rating
   of exactly 4.0 may warrant checking how ratings are collected or
   rounded.
7. Standardize master data. Review inconsistent fat-content labels,
   conflicting outlet-size values, and other catalogue inconsistencies.
8. Validate high-value SKU distribution. Prioritize candidate
   products for review, but do not interpret catalogue value as demand
   without transaction data.
Illustrative assortment scenario
The notebook estimates a theoretical catalogue-value opportunity of
109,008.97 (reported notebook output; verify before publication)
based on its assortment-gap assumptions and unrounded values. Treat this
as an illustrative scenario, not an incremental revenue forecast: it
assumes additional listings can be added and that the Sales value is a
suitable proxy for the value of those listings.
Before publishing, confirm the exact unrounded output in the notebook
and replace the temporary figure above with that verified value. The
README draft intentionally flags this figure for verification rather
than presenting an unchecked number as a fact.

SQL warehouse and dashboard
The project includes a SQLite warehouse designed around a star schema.
  Table or view                      Purpose
  dim_products                     Product attributes such as family,
                                     category, fat content, and weight

  dim_outlets                      Outlet attributes such as format,
                                     tier, size, establishment year,
                                     and age

  fact_inventory_pricing           Product--outlet records with the
                                     analysed Sales field,
                                     visibility, and rating

  vw_sku_pricing_variance          Variation in Sales by SKU

  vw_outlet_assortment_gap         Assortment breadth comparison by
                                     outlet format

  vw_format_controlled_tiers       Tier comparisons within the same
                                     store format

  vw_category_pareto               Category concentration and
                                     cumulative shares

  vw_missing_sku_prioritization    Candidate SKUs present in
                                     supermarkets but missing from
                                 Grocery Stores
The Streamlit dashboard includes:
- Assortment Expansion Simulator
- Pricing Variance & MRP Proof
- Tier Comparison Audit
- SKU Recommendation Engine
- SQL Star Schema Explorer
Dashboard link: Add your deployed Streamlit URL here when available.
Until then, run the app locally using the instructions below.
Data cleaning decisions
The analysis documents the following data-quality issues:
- Missing item weights: 1,463 rows (17.16%)
- Zero item-visibility values: 526 rows
- Inconsistent fat-content labels
- Conflicting outlet-size values for some outlets
- Outliers retained where removal was not justified
Please refer to the notebook for the specific imputation and
harmonization rules applied to each field. These decisions should be
reviewed alongside the analysis because imputation can influence
comparisons between outlet types.
Limitations
- The meaning of Sales is not established by the field name
  alone. The variance pattern suggests a price-like measure, but
  source documentation or cross-checking against MRP is needed to
  confirm it.
- No transaction quantities are available. Units sold, conversion,
  realized revenue, and demand cannot be measured directly.
- No timestamps are available. Seasonality, trends, and
  time-series forecasting are out of scope.
- The assortment opportunity is theoretical. More listings do not
  guarantee demand or incremental revenue, and outlet space may
  constrain expansion.
- Statistical independence needs care. Repeated SKUs across
  outlets can affect the uncertainty of tests that operate on
  product--outlet rows.
- Currency is unlabelled. Values are reported as currency units
  until verified from the source.
Getting started
Requirements
Use a Python environment compatible with the packages listed in
requirements.txt.
Option 1: Run the notebook
jupyter notebook BlinkIT_Grocery_Sales_Analysis_v2.ipynb
Run the notebook cells in order. Confirm that the raw Excel workbook is
in the expected folder before running the analysis.
Option 2: Run the analysis script
python -m pip install -r requirements.txt
python run_analysis.py
The script is intended to write the cleaned CSV and visual outputs.
Check the paths configured in the script before running it.
Option 3: Run the Streamlit dashboard
python -m pip install -r requirements.txt
streamlit run app.py
If the SQLite database is not present, the app may build it from the
cleaned CSV, depending on the repository configuration. Ensure the
required input file exists before starting the app.
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
Tools used
Python · pandas · NumPy · Matplotlib · Seaborn · SciPy · SQL · SQLite ·
Plotly · Streamlit
Author
Pooja Singh
Portfolio note: This is an exploratory analysis of an aggregated
catalogue snapshot. Findings are descriptive and should not be
interpreted as causal or as verified revenue results without
transaction-level and source-definition evidence.
