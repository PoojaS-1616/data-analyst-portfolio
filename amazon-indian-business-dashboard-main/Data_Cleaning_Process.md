# Data Cleaning Process

**Amazon India Business Performance Dashboard**

Before building the dashboard, I checked the dataset to make sure the numbers could be trusted. The dataset has **10,000 Amazon India orders**, with details on products, sales, profit, payment method, fulfilment, order status and shipping state.

## The columns

`Order_ID`, `Order_Date`, `Category`, `Product`, `Quantity`, `Unit_Price_INR`, `Discount_Pct`, `Total_Sales_INR`, `Profit_INR`, `Payment_Method`, `Fulfillment`, `Order_Status`, `Ship_State`

Together, these cover everything the dashboard needs: sales, profit, products, orders, payments, fulfilment and location.

## What I checked

**Missing values.** 

I looked for blank cells in every important column. There were none, so no rows had to be removed.

**Duplicates.**

I checked for repeated rows and repeated Order IDs. I found none, so nothing was removed.

**Numbers.**

I checked Quantity, Unit Price, Discount, Sales and Profit for blanks, text entered by mistake, and unexpected negative values. They were all fine to use. I also confirmed that discounts stayed within a sensible percentage range, since a wrong discount would distort sales and profit.

**Text columns.**

I checked Category, Product, Payment Method, Fulfilment, Order Status and State for stray spaces and inconsistent spellings. These can make one item look like two, for example "UPI" and "UPI". The values were consistent, so each group adds up correctly.

- **Categories:**- Electronics & Mobiles, Home & Kitchen, Apparel & Fashion, Beauty & Personal Care, Pantry & Groceries
- **Order statuses:**-  Delivered, Shipped, Returned, Cancelled

## The one problem I found: dates stored as text

The `Order_Date` column needed fixing. Excel was reading the dates as plain text instead of real dates. A quick test showed it: `=ISNUMBER(B2)` returned `FALSE`.

Text dates can't be sorted, filtered or grouped by month properly, so the monthly trend chart would not have worked. I converted them into proper Excel dates and used one consistent date format throughout.

## Returned and cancelled orders were kept

I did not delete returned or cancelled orders. They are not errors; they are real business outcomes. Keeping them lets the dashboard show return rate, cancellation rate, and how much revenue is lost to each.

## Final check

After the fixes, I went through every column once more: missing values, duplicates, dates, numbers, discounts, and the text fields. Everything held up.

## Result

The data was clean and ready for analysis. The date fix was the only change needed, and no records were removed. This cleaned data is the base for every KPI and chart on the dashboard: sales and profit, monthly trends, categories, top products, order status, payment, fulfilment and state performance.
