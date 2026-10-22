<h1>Data Cleaning Process</h1>

<p><strong>Project: Amazon India Business Performance Dashboard</strong></p>

<h2>Overview</h2>

<p>
  Before building the dashboard, I reviewed the dataset for missing values,
  duplicate records, data types and inconsistent labels. The dataset contains
  <strong>10,000 order records</strong> covering products, sales, profit,
  payment methods, fulfilment, order status and shipping states.
</p>

<p>
  The main source-data issue identified was that <code>Order_Date</code>
  values were stored as text. These were converted into Excel dates.
  No records were removed.
</p>

<h2>Original Columns</h2>

<p>
  <code>Order_ID</code>,
  <code>Order_Date</code>,
  <code>Category</code>,
  <code>Product</code>,
  <code>Quantity</code>,
  <code>Unit_Price_INR</code>,
  <code>Discount_Pct</code>,
  <code>Total_Sales_INR</code>,
  <code>Profit_INR</code>,
  <code>Payment_Method</code>,
  <code>Fulfillment</code>,
  <code>Order_Status</code>,
  <code>Ship_State</code>
</p>

<p>
  <code>Order_Month</code> was added during data preparation;
  it is not an original source column.
</p>

<h2>Validation Checks</h2>

<table>
  <thead>
    <tr>
      <th>Check</th>
      <th>Finding</th>
      <th>Action</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Missing values</td>
      <td>No missing values identified in the checked columns</td>
      <td>No rows removed or values imputed</td>
    </tr>
    <tr>
      <td>Duplicate records</td>
      <td>No repeated rows identified</td>
      <td>No duplicates removed</td>
    </tr>
    <tr>
      <td>Duplicate Order IDs</td>
      <td>No repeated <code>Order_ID</code> values identified</td>
      <td>All order records retained</td>
    </tr>
    <tr>
      <td>Numeric fields</td>
      <td>
        No blanks, text entries or unexpected negative values identified
        in Quantity, Unit Price, Discount, Sales or Profit
      </td>
      <td>Existing values retained</td>
    </tr>
    <tr>
      <td>Text labels</td>
      <td>
        Category, Product, Payment Method, Fulfilment, Order Status
        and State labels were consistent in the checks performed
      </td>
      <td>No label corrections required</td>
    </tr>
    <tr>
      <td>Date values</td>
      <td><code>Order_Date</code> was stored as text</td>
      <td>Converted to Excel dates</td>
    </tr>
  </tbody>
</table>

<h3>Discount Validation</h3>

<p>
  <code>Discount_Pct</code> was checked as a numeric field.
  The original cleaning notes do not record the exact minimum, maximum
  or percentage scale used, so this document does not claim a verified
  discount range.
</p>

<p>
  To reproduce this check, confirm whether discounts are stored as fractions,
  such as <code>0.10</code> for 10%, or percentage points,
  such as <code>10</code> for 10%. Record the observed minimum and maximum
  and validate them against the confirmed definition.
</p>

<h3>Text Consistency</h3>

<p>
  Labels were checked for inconsistent spelling and unwanted spaces.
  For example, <code>"UPI"</code> and <code>"UPI "</code> can be treated
  as different labels because the second value contains a trailing space.
</p>

<p><strong>Category labels:</strong></p>

<ul>
  <li>Electronics &amp; Mobiles</li>
  <li>Home &amp; Kitchen</li>
  <li>Apparel &amp; Fashion</li>
  <li>Beauty &amp; Personal Care</li>
  <li>Pantry &amp; Groceries</li>
</ul>

<p><strong>Order statuses:</strong></p>

<ul>
  <li>Delivered</li>
  <li>Shipped</li>
  <li>Returned</li>
  <li>Cancelled</li>
</ul>

<h2>Date Correction</h2>

<p>
  The <code>Order_Date</code> column contained text rather than Excel
  date values. The initial check:
</p>

<pre><code>=ISNUMBER(B2)</code></pre>

<p>returned <code>FALSE</code> for the affected dates.</p>

<p>
  The text values were converted into Excel dates and displayed using
  a consistent date format. Changing the display format alone would
  not have converted the underlying text values.
</p>

<h3>Reproducing and Validating the Conversion</h3>

<p>
  The original notes do not identify the conversion method used.
  A repeatable Excel procedure is:
</p>

<ol>
  <li>
    Confirm the source date order, such as day-month-year or
    month-day-year, before converting any values.
  </li>
  <li>
    Select <code>Order_Date</code>, then choose
    <strong>Data &gt; Text to Columns</strong>.
  </li>
  <li>
    Select <strong>Delimited</strong>, proceed without selecting
    a delimiter that splits the date, and choose <strong>Date</strong>
    in the final step.
  </li>
  <li>
    Select the date order that matches the source and finish the conversion.
  </li>
  <li>
    Apply a consistent display format, such as <code>dd-mmm-yyyy</code>.
  </li>
  <li>
    Repeat <code>=ISNUMBER(B2)</code> for the populated date cells.
    The expected result is <code>TRUE</code> after successful conversion.
  </li>
  <li>
    Compare sample converted dates with the originals to confirm
    that the day and month have not been swapped.
  </li>
</ol>

<p>
  These steps provide a reproducible procedure; the original notes
  do not retain the post-conversion formula results.
</p>

<h2>Order_Month Helper Column</h2>

<p>
  After correcting <code>Order_Date</code>, an <code>Order_Month</code>
  helper column was derived in <code>YYYY-MM</code> format to support
  monthly summaries.
</p>

<p>For a cleaned date in <code>B2</code>, this can be reproduced with:</p>

<pre><code>=TEXT(B2,"yyyy-mm")</code></pre>

<p>
  The formula returns a month label such as <code>2024-04</code>.
  <code>Order_Date</code> remains the underlying Excel date, while
  <code>Order_Month</code> provides a consistent grouping label
  for the dashboard's monthly calculations.
</p>

<h2>Returned and Cancelled Orders</h2>

<p>
  Returned and cancelled orders were retained because they are valid
  order statuses, rather than data-cleaning errors.
</p>

<p>Keeping these records supports calculation of:</p>

<ul>
  <li>Return and cancellation rates.</li>
  <li>Category and segment comparisons.</li>
  <li>Recorded sales value associated with returned and cancelled orders.</li>
</ul>

<p>
  In this dataset, returned and cancelled orders retain a sales value
  while their recorded profit is zero. Their associated sales value
  should not be interpreted as confirmed financial loss.
  Dashboard sales totals include these records unless an exclusion
  is explicitly applied.
</p>

<h2>Final Review and Outcome</h2>

<p>
  The final review covered missing values, duplicates, numeric fields,
  dates and text labels.
</p>

<ul>
  <li><strong>Records before preparation:</strong> 10,000.</li>
  <li><strong>Records after preparation:</strong> 10,000.</li>
  <li><strong>Records removed:</strong> 0.</li>
  <li>
    <strong>Source-data correction:</strong>
    Text dates converted into Excel dates.
  </li>
  <li>
    <strong>Derived field added:</strong>
    <code>Order_Month</code> for monthly summaries.
  </li>
</ul>

<p>
  No missing values, duplicate records or duplicate Order IDs were
  identified in the checks performed. The prepared dataset was used
  for the dashboard's KPIs, charts and segment analyses.
</p>

<p>
  <strong>Documentation limitations:</strong>
  The exact original date-conversion method, post-conversion formula
  results and discount bounds remain undocumented. These details
  should be confirmed to complete the cleaning audit trail.
</p>
