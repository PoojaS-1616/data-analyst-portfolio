# Pooja Singh | Data Analytics Portfolio

A collection of business analytics projects using Excel, Python and SQL to investigate business questions, build dashboards and communicate actionable findings.

The projects cover retail performance, profitability, product pricing and outlet assortment, with an emphasis on data validation and clear interpretation.

[LinkedIn](https://www.linkedin.com/in/pooja-singh-data/) · [Email](mailto:poojas.s199977@gmail.com) · [GitHub](https://github.com/PoojaS-1616)

## Projects

| Project | Analytical focus | Tools |
|---|---|---|
| [Amazon India Business Performance](./amazon-indian-business-dashboard-main/) | Sales, profitability, category concentration and order outcomes | Excel |
| [Supermart Grocery Sales](./Supermart-Grocery-Sales-Dashboard/) | Sales growth, regional performance, discounts and margins | Excel |
| [BlinkIT Grocery Pricing & Catalogue](./BlinkIT-Grocery-Sales-Analysis/) | Data validation, pricing patterns and outlet assortment | Python, SQL, Streamlit |

### Amazon India Business Performance Dashboard

Analysed **10,000 orders** and built an Excel dashboard answering four business questions about overall performance, business drivers, order outcomes and geographic contribution.

- Developed 6 KPIs and 9 charts covering sales, profit, products and order statuses.
- Identified that Electronics contributes approximately **79% of sales** from **30% of orders**.
- Found that returned and cancelled orders represent **9.85% of orders**.
- Presented recommendations for reviewing category dependence and investigating order losses.

**Deliverables:** Excel dashboard, dashboard preview and data-cleaning documentation.

[View project →](./amazon-indian-business-dashboard-main/)

### Supermart Grocery Sales Dashboard

Analysed **9,994 orders** to compare sales growth, category performance and profitability.

- Built Year, Region and Category dropdown filters that update dashboard KPIs and charts.
- Observed **28.6% sales growth in 2018** and examined monthly sales patterns.
- Investigated the relationship between discounts and profit, finding no clear correlation in the analysis.
- Identified sub-categories with high sales and below-average margins.

**Deliverables:** Interactive Excel dashboard, dashboard preview and data-cleaning documentation.

[View project →](./Supermart-Grocery-Sales-Dashboard/)

### BlinkIT Grocery Pricing & Catalogue Analysis

Analysed **8,523 product–outlet records across 10 outlets** using Python, SQL and Streamlit.

- Documented data cleaning, missing-value handling and exploratory analysis.
- Used variance decomposition to investigate the meaning of the `Sales` field.
- Found that item identity explains approximately **99.97% of its variance**, suggesting a SKU-linked price or value.
- Built a SQL star-schema warehouse and an interactive Streamlit dashboard.

**Interpretation:** The meaning of `Sales` requires source validation before treating it as transaction revenue. The available records alone do not establish units sold or demand over time.

**Deliverables:** Analysis notebook, cleaned dataset, SQL scripts, visualisations and Streamlit application.

[View project →](./BlinkIT-Grocery-Sales-Analysis/) · [View SQL script →](./BlinkIT-Grocery-Sales-Analysis/blinkit_warehouse.sql)

## Technical Skills Demonstrated

| Area | Application |
|---|---|
| Excel | Data cleaning, SUMIFS, COUNTIFS, helper sheets, dropdown filters and dashboards |
| Python | Data preparation, transformation and exploratory analysis with pandas and NumPy |
| SQL | Star-schema design, joins, aggregations and views |
| Statistics | Correlation analysis, variance decomposition and hypothesis testing |
| Visualisation | Excel charts, Matplotlib, Seaborn, Plotly and Streamlit |
| Business analysis | KPI interpretation, segment comparisons, recommendations and analytical limitations |

## Analytical Approach

1. Define the business question and relevant metrics.
2. Validate field definitions and assess data quality.
3. Clean and transform the data.
4. Investigate patterns and test assumptions.
5. Communicate findings through charts and dashboards.
6. Recommend next steps while documenting limitations.

Detailed methods, findings and supporting files are available in each project folder.

## Current Development

I am strengthening my statistical inference, regression, advanced SQL and Python problem-solving skills, alongside dashboard design and business communication.

## Contact

- **LinkedIn:** [pooja-singh-data](https://www.linkedin.com/in/pooja-singh-data/)
- **Email:** [poojas.s199977@gmail.com](mailto:poojas.s199977@gmail.com)
- **GitHub:** [PoojaS-1616](https://github.com/PoojaS-1616)
