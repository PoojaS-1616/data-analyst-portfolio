# Data Cleaning Process

These are the checks I ran on the Supermart data before analysing it, and the assumptions I made along the way.

## 1. Order date formats

Order dates came in two formats:

- `m/d/yyyy` (with slashes)
- `dd-mm-yyyy` (with dashes)

**How I read them:**

- I read slash dates **month-first**. Some of them have a day above 12 (up to 31) in the second position, which confirms this order.
- I read dash dates **day-first**, following the Indian convention, because both parts are 12 or below and the format is ambiguous.

**Impact:** Year-level results are not affected. The monthly trend could shift for the dash-format rows if those dates are really month-first.

## 2. Missing values

I checked every column and found **no missing values**.

## 3. Duplicates

I checked the Order IDs and found **no duplicates**.

## 4. Region labels

- Region "North" appears on **only one order** (OD1). It looks like a data-entry quirk, so I kept it and showed it, but it has no real effect on the results.
- Region labels are **not tied to cities**: each city appears under several regions. Because of this, I treated region and city as independent views.

## 5. State

Every order is in **Tamil Nadu** (9,994 orders), so I could not compare states. I did the geographic analysis at city and region level instead.

## 6. Product level

The dataset has no product or SKU column, so I used **sub-category** as the "product" level.

## 7. Currency

The dataset does not state a currency. I assumed **₹**, since every order is in Tamil Nadu.

## 8. Helper columns I added

| Column | Definition |
|---|---|
| Year | Year taken from the order date |
| Month | Year and month (for example 2017-08) taken from the order date |
| Profit Margin | Profit ÷ Sales |

## Summary of my assumptions

| Area | Assumption |
|---|---|
| Dash-format dates | Read day-first |
| Slash-format dates | Read month-first |
| Region "North" | One order, kept, treated as immaterial |
| Currency | ₹ |
| Product level | Sub-category |
