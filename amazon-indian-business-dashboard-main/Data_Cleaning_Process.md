# Data Cleaning Process

**Project: Amazon India Business Performance Dashboard**

## Overview

Before building the dashboard, I checked the dataset for missing values, duplicate records, incorrect data types and inconsistent labels.

The dataset contains **10,000 order records** covering products, sales, profit, payment methods, fulfilment, order status and shipping states.

The main issue identified was that `Order_Date` values were stored as text. These were converted into Excel dates. **No records were removed.**

## Original Columns

`Order_ID`, `Order_Date`, `Category`, `Product`, `Quantity`, `Unit_Price_INR`, `Discount_Pct`, `Total_Sales_INR`, `Profit_INR`, `Payment_Method`, `Fulfillment`, `Order_Status`, `Ship_State`

The `Order_Month` helper column was added during data preparation.

## Validation Checks

| Check | Finding | Action |
|---|---|---|
| Missing values | No missing values identified in the checked columns | No rows removed or values imputed |
| Duplicate records | No repeated rows identified | No duplicates removed |
| Duplicate Order IDs | No repeated `Order_ID` values identified | All order records retained |
| Numeric fields | No blanks, text entries or unexpected negative values identified | Existing values retained |
| Text labels | Labels were consistent in the checks performed | No label corrections required |
| Date values | `Order_Date` was stored as text | Converted to Excel dates |

### Numeric Fields

The following columns were checked for numeric values, blanks and unexpected negative values:

- `Quantity`
- `Unit_Price_INR`
- `Discount_Pct`
- `Total_Sales_INR`
- `Profit_INR`

The original cleaning notes do not record the discount scale or exact minimum and maximum. A verified discount range is therefore not claimed here.

### Text Consistency

Text fields were checked for inconsistent spelling and unwanted spaces.

For example, `"UPI"` and `"UPI "` can be treated as different labels because the second value contains a trailing space.

**Category labels:**

- Electronics & Mobiles
- Home & Kitchen
- Apparel & Fashion
- Beauty & Personal Care
- Pantry & Groceries

**Order statuses:**

- Delivered
- Shipped
- Returned
- Cancelled

## Date Correction

The `Order_Date` column contained text rather than Excel date values.

The initial check:

```excel
=ISNUMBER(B2)
```

returned `FALSE` for the affected dates.

The text values were converted into Excel dates and displayed using a consistent date format. Changing the display format alone would not have converted the underlying text.

### Reproducing the Conversion

The original notes do not identify the conversion method used. The following procedure provides a way to reproduce and validate the correction:

1. Confirm whether the source dates use day-month-year or month-day-year.
2. Select the `Order_Date` column.
3. Choose **Data > Text to Columns**.
4. Select **Delimited** and proceed without selecting a delimiter that splits the date.
5. In the final step, select **Date** and choose the order matching the source.
6. Finish the conversion and apply a consistent display format, such as `dd-mmm-yyyy`.
7. Repeat `=ISNUMBER(B2)` across the populated date cells. The expected result is `TRUE`.
8. Compare sample converted dates with the original values to check that days and months have not been swapped.

The original notes do not retain the post-conversion formula results.

## Order_Month Helper Column

After correcting `Order_Date`, an `Order_Month` helper column was derived in `YYYY-MM` format for monthly summaries.

For a cleaned date in `B2`, the month label can be generated with:

```excel
=TEXT(B2,"yyyy-mm")
```

For example, an April 2024 date produces `2024-04`.

`Order_Date` remains the underlying Excel date. `Order_Month` provides a consistent grouping label for the dashboard's monthly calculations.

## Returned and Cancelled Orders

Returned and cancelled orders were retained because they are valid order statuses, rather than data-cleaning errors.

Keeping these records supports:

- Return and cancellation rate calculations.
- Comparisons across categories and business segments.
- Analysis of the recorded sales value associated with these statuses.

In this dataset, returned and cancelled orders retain a sales value while their recorded profit is zero.

Their associated sales value should **not be interpreted as confirmed financial loss**. Dashboard sales totals include these records unless an exclusion is explicitly applied.

## Final Outcome

| Measure | Result |
|---|---|
| Records before preparation | 10,000 |
| Records after preparation | 10,000 |
| Records removed | 0 |
| Source-data correction | Text dates converted into Excel dates |
| Derived field added | `Order_Month` |

No missing values, duplicate records or duplicate Order IDs were identified in the checks performed.

The prepared dataset was used for the dashboard's KPIs, monthly trends, category comparisons, product analysis, order outcomes and payment, fulfilment and state summaries.

## Documentation Limitations

The following details were not recorded in the original cleaning notes:

- The exact date-conversion method used.
- Post-conversion formula results.
- The discount scale and observed minimum and maximum.

These details should be confirmed to complete the cleaning audit trail.
