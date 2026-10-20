# Project Review — BlinkIT Grocery Sales Analysis

## Review basis

The supplied `Blinkit Grocery Sales Analysis.pdf` defines four objectives and 16 tasks. The V2 notebook and supporting project assets were reviewed against those stated requirements.

## Task coverage

| PDF objective | Tasks | Coverage in V2 notebook |
|---|---|---|
| 1. Understand the business and sales performance | 1.1–1.4 | Product assortment, outlet types/locations, value distribution, ratings |
| 2. Make sure information is reliable | 2.1–2.4 | Missing-value audit/imputation, duplicates, IQR outliers, label and outlet-size standardisation |
| 3. Find what is driving better sales performance | 3.1–3.4 | Product/category comparisons, outlet comparisons, correlations/variance, high-/low-value cohorts |
| 4. Help management make better decisions | 4.1–4.4 | Category concentration, fair outlet/location comparisons, assortment gaps, recommendations |

This confirms coverage of the questions listed in the PDF; it does not guarantee a particular grade because the PDF does not provide a detailed scoring rubric.

## Validation performed for this package

- **V2 notebook:** executed from the project root using Jupyter `nbconvert`. All 33 of 33 code cells executed, all 33 had outputs, and no error outputs were recorded.
- **`run_analysis.py`:** completed successfully; rebuilt the cleaned CSV (8,523 rows × 15 columns, no nulls in the exported result) and exported 10 core figures (13 panels). The runtime printed font-fallback warnings because Arial was not installed; the run completed successfully.
- **`build_warehouse.py`:** completed successfully and populated 1,559 product dimension rows, 10 outlet dimension rows and 8,523 fact rows.
- **SQL Pareto view correction:** the original view grouped by both item type and SKU-prefix-derived family, which split the Dairy category across `Food` and `Drinks`. The packaged SQL now groups the Pareto calculation by item type and labels a category `Mixed` when multiple derived families occur. The resulting top five are Fruits and Vegetables, Snack Foods, Household, Frozen Foods and Dairy, totaling 59.03% of the `Sales` column values.
- **Documentation:** README points to the V2 notebook and describes execution commands, deliverables and limitations.

## Interpretation caveats to preserve in the final submission

1. The `Sales` column behaves like a unit retail price/MRP: SKU identity explains approximately 99.97% of its variance and within-SKU variation is small. Since there are no dates or quantities, the analysis cannot establish transaction revenue, demand velocity or profit. Describe totals as catalogue-value comparisons unless the dataset source confirms the field semantics.
2. Currency is not labelled in the data. `$` is a formatting convention in the current project, not a verified currency unit.
3. The 526 zero-visibility values are treated as data-quality anomalies and imputed using cross-outlet SKU values. Keep this documented as an assumption.
4. Outlet-size labels conflict for `OUT010`, `OUT017` and `OUT045`; these are marked `Unknown` for size comparisons.
5. The source workbook's external provenance is not independently verified here.

## Final assessment

The V2 notebook meets the stated analytical scope of the PDF, and its outputs were successfully generated during this validation. The project package includes the executed notebook, raw and cleaned data, charts, scripts, SQL/database assets, README, detailed explanation, flowchart and this review. GitHub publication is optional unless separately required by the submission instructions.

## Packaging notes

The ZIP is curated to avoid duplicate and stale copies. The older duplicate notebook, nested `Blinkit_Flagship_Package.zip`, `career_tracker.html`, and the older file-by-file manual were excluded because they contain duplicate assets or older path/setup instructions. The current V2 notebook and the updated project documentation are the canonical versions in this package.
