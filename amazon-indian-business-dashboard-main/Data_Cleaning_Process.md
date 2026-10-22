Data Cleaning Process
Project: Amazon India Business Performance Dashboard
Overview
Before building the dashboard, I reviewed the dataset for missing values, duplicate records, data types and inconsistent labels. The dataset contains 10,000 order records covering products, sales, profit, payment methods, fulfilment, order status and shipping states.

The main source-data issue identified was that Order_Date values were stored as text. These were converted into Excel dates. No records were removed.
Original Columns
Order_ID, Order_Date, Category, Product, Quantity, Unit_Price_INR, Discount_Pct, Total_Sales_INR, Profit_INR, Payment_Method, Fulfillment, Order_Status, Ship_State

Order_Month was added during data preparation; it is not an original source column.
Validation Checks
Check	Finding	Action
Missing values	No missing values identified in the checked columns	No rows removed or values imputed
Duplicate records	No repeated rows identified	No duplicates removed
Duplicate Order IDs	No repeated Order_ID values identified	All order records retained
Numeric fields	No blanks, text entries or unexpected negative values identified in Quantity, Unit Price, Discount, Sales or Profit	Existing values retained
Text labels	Category, Product, Payment Method, Fulfilment, Order Status and State labels were consistent in the checks performed	No label corrections required
Date values	Order_Date was stored as text	Converted to Excel dates


Discount Validation
Discount_Pct was checked as a numeric field. The original cleaning notes do not record the exact minimum, maximum or percentage scale used, so this document does not claim a verified discount range.

To reproduce this check, confirm whether discounts are stored as fractions, such as 0.10 for 10%, or percentage points, such as 10 for 10%. Record the observed minimum and maximum and validate them against the confirmed definition.
Text Consistency
Labels were checked for inconsistent spelling and unwanted spaces. For example, "UPI" and "UPI " can be treated as different labels because the second value contains a trailing space.

The category labels were:
- Electronics & Mobiles
- Home & Kitchen
- Apparel & Fashion
- Beauty & Personal Care
- Pantry & Groceries
The order statuses were:
- Delivered
- Shipped
- Returned
- Cancelled
Date Correction
The Order_Date column contained text rather than Excel date values. The initial check:
=ISNUMBER(B2)
returned FALSE for the affected dates.

The text values were converted into Excel dates and displayed using a consistent date format. Changing the display format alone would not have converted the underlying text values.
Reproducing and Validating the Conversion
The original notes do not identify the conversion method used. A repeatable Excel procedure is:
1. Confirm the source date order, such as day-month-year or month-day-year, before converting any values.
2. Select Order_Date, then choose Data > Text to Columns.
3. Select Delimited, proceed without selecting a delimiter that splits the date, and choose Date in the final step.
4. Select the date order that matches the source and finish the conversion.
5. Apply a consistent display format, such as dd-mmm-yyyy.
6. Repeat =ISNUMBER(B2) for the populated date cells. The expected result is TRUE after successful conversion.
7. Compare sample converted dates with the originals to confirm that the day and month have not been swapped.
These steps provide a reproducible procedure; the original notes do not retain the post-conversion formula results.
Order_Month Helper Column
After correcting Order_Date, an Order_Month helper column was derived in YYYY-MM format to support monthly summaries.

For a cleaned date in B2, this can be reproduced with:
=TEXT(B2,"yyyy-mm")
The formula returns a month label such as 2024-04. Order_Date remains the underlying Excel date, while Order_Month provides a consistent grouping label for the dashboard's monthly calculations.
Returned and Cancelled Orders
Returned and cancelled orders were retained because they are valid order statuses, rather than data-cleaning errors.

Keeping these records supports calculation of:
- Return and cancellation rates.
- Category and segment comparisons.
- Recorded sales value associated with returned and cancelled orders.
In this dataset, returned and cancelled orders retain a sales value while their recorded profit is zero. Their associated sales value should not be interpreted as confirmed financial loss. Dashboard sales totals include these records unless an exclusion is explicitly applied.
Final Review and Outcome
The final review covered missing values, duplicates, numeric fields, dates and text labels.
- Records before preparation: 10,000.
- Records after preparation: 10,000.
- Records removed: 0.
- Source-data correction: Text dates converted into Excel dates.
- Derived field added: Order_Month for monthly summaries.
No missing values, duplicate records or duplicate Order IDs were identified in the checks performed. The prepared dataset was used for the dashboard's KPIs, charts and segment analyses.

The exact original date-conversion method, post-conversion formula results and discount bounds remain undocumented. These details should be confirmed to complete the cleaning audit trail.
