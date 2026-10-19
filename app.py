"""
Blinkit Quick-Commerce Catalogue Architecture & Dark Store Assortment Simulator
==============================================================================
Production Streamlit Executive Dashboard & Decision Engine
------------------------------------------------------------------------------
Author: Candidate Portfolio (Senior Data Analyst / Junior Data Scientist Track)
Architecture: Integrated with SQLite Dimensional Star Schema (blinkit_warehouse.db)
"""

import os
import sqlite3
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ------------------------------------------------------------------------------
# PAGE CONFIGURATION & STYLING
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Blinkit Quick-Commerce Assortment Simulator",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for executive styling
st.markdown("""
<style>
    .metric-card {
        background-color: #f8f9fa;
        border-left: 5px solid #ffcc00;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        padding-top: 10px;
        padding-bottom: 10px;
        font-weight: 600;
    }
    .insight-box {
        background-color: #17263c;
        color: #e2ecf7 !important;
        border: 1px solid #2e476e;
        border-left: 5px solid #2986cc;
        padding: 14px;
        border-radius: 6px;
        margin-top: 10px;
        margin-bottom: 15px;
        font-size: 0.95rem;
    }
    .insight-box b {
        color: #6bb9f0 !important;
    }
    .warning-box {
        background-color: #332810;
        color: #fceecb !important;
        border: 1px solid #66501a;
        border-left: 5px solid #ffcc00;
        padding: 14px;
        border-radius: 6px;
        margin-top: 10px;
        margin-bottom: 15px;
        font-size: 0.95rem;
    }
    .warning-box b {
        color: #ffd740 !important;
    }
</style>

""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# DATA INGESTION & CACHING
# ------------------------------------------------------------------------------
@st.cache_data
def load_data():
    csv_path = 'BlinkIT_Grocery_Data_Cleaned.csv'
    if not os.path.exists(csv_path):
        st.error(f"Dataset '{csv_path}' not found. Please ensure it exists in the workspace.")
        st.stop()
    df = pd.read_csv(csv_path)
    return df

@st.cache_resource
def get_db_connection():
    db_path = 'blinkit_warehouse.db'
    if not os.path.exists(db_path):
        # Auto-build warehouse if db is missing
        import build_warehouse
        build_warehouse.build_warehouse()
    conn = sqlite3.connect(db_path, check_same_thread=False)
    return conn

df = load_data()
conn = get_db_connection()

# ------------------------------------------------------------------------------
# SIDEBAR CONTROLS
# ------------------------------------------------------------------------------
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2f/Blinkit-yellow-app-icon.svg", width=65)
    st.title("Blinkit Executive Portal")
    st.caption("Quick-Commerce Dark Store Economics & Catalogue Strategy")
    st.markdown("---")

    st.subheader("🛠️ Global Portfolio Levers")
    currency = st.radio("Display Currency Metric", ["$ (USD Normalized)", "₹ (INR Estimated 1:83)"])
    rate = 83.0 if "INR" in currency else 1.0
    symbol = "₹" if "INR" in currency else "$"

    st.markdown("---")
    st.markdown("### 🎯 Executive Navigation")
    st.info(
        "This tool supports commercial category managers and dark store operators in evaluating "
        "SKU assortment breadth, inventory holding costs, and format economics."
    )
    st.markdown("---")
    st.caption("Flagship Portfolio Project · Pair Programming Production Suite")

# ------------------------------------------------------------------------------
# HEADER & NETWORK METRICS
# ------------------------------------------------------------------------------
def format_compact_currency(amount, sym):
    if sym == "₹":
        if abs(amount) >= 1e7:
            return f"₹{amount/1e7:.2f} Cr"
        elif abs(amount) >= 1e5:
            return f"₹{amount/1e5:.2f} Lakh"
        else:
            return f"₹{amount:,.2f}"
    else:
        if abs(amount) >= 1e6:
            return f"${amount/1e6:.2f}M"
        elif abs(amount) >= 1e3:
            return f"${amount/1e3:.1f}k"
        else:
            return f"${amount:,.2f}"

st.title("⚡ Blinkit Catalogue Pricing & Assortment Decision Suite")
st.markdown(
    f"**Objective:** Diagnostic analysis of catalogue pricing architecture, store-format unit economics, "
    f"and simulation of dark store SKU expansion to capture **+{format_compact_currency(109009*rate, symbol)}** in inventory potential."
)

col1, col2, col3, col4 = st.columns(4)
total_catalogue_value = df['Sales'].sum() * rate
avg_unit_mrp = df['Sales'].mean() * rate
total_skus = df['Item Identifier'].nunique()
total_stores = df['Outlet Identifier'].nunique()

col1.metric("Total Catalogue Value", format_compact_currency(total_catalogue_value, symbol), "+9.07% potential gap")
col2.metric("Mean Unit Retail Price (MRP)", f"{symbol}{avg_unit_mrp:,.2f}", f"Parity across stores: ±{symbol}{1.85*rate:.2f}")
col3.metric("Network SKU Depth", f"{total_skus:,} SKUs", "16 Item Categories")
col4.metric("Fulfillment Outlets", f"{total_stores} Dark Stores", "8 Supermarkets · 2 Grocery Stores")

# ------------------------------------------------------------------------------
# TABS ARCHITECTURE
# ------------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Assortment Expansion Simulator", 
    "🔬 Pricing Variance & MRP Proof",
    "⚖️ Simpson's Paradox (Tier 2 Audit)", 
    "🎯 SKU Recommendation Engine",
    "🗄️ SQL Star Schema Explorer"
])

# ==============================================================================
# TAB 1: DARK STORE ASSORTMENT EXPANSION SIMULATOR
# ==============================================================================
with tab1:
    st.header("🏪 Dark Store Assortment Breadth & Inventory Simulator")
    st.markdown(
        "Grocery stores (`OUT010` and `OUT019`) currently stock only ~**541.5 SKUs** compared to "
        "~**930.0 SKUs** in Supermarket dark stores. This interactive simulator models the working "
        "catalogue-value potential of closing this assortment gap; actual demand and gross margin are not available in this dataset."
    )

    sim_col1, sim_col2 = st.columns([1, 2])

    with sim_col1:
        st.subheader("🕹️ Simulation Levers")
        target_store = st.selectbox("Select Target Dark Store", ["OUT010 (Tier 3 · Size Unknown)", "OUT019 (Tier 1 · Small)"])
        target_store_id = target_store.split()[0]

        # Extract current store stats
        store_data = df[df['Outlet Identifier'] == target_store_id]
        current_skus = len(store_data)
        supermarket_avg_skus = 930
        max_missing = supermarket_avg_skus - current_skus

        skus_to_add = st.slider(
            "Number of Missing SKUs to Onboard", 
            min_value=0, 
            max_value=int(max_missing), 
            value=int(max_missing),
            help=f"Closing the gap completely requires adding {max_missing} SKUs."
        )

        target_gross_margin = st.slider("Target Gross Margin %", min_value=10.0, max_value=35.0, value=22.5, step=0.5) / 100.0
        inventory_turns_per_year = st.slider("Projected Annual Inventory Turns (Velocity)", min_value=4.0, max_value=24.0, value=12.0, step=1.0)
        holding_cost_pct = st.slider("Annual Working Capital & Holding Cost %", min_value=5.0, max_value=25.0, value=15.0, step=0.5) / 100.0

    with sim_col2:
        st.subheader("📊 Projected Financial & Inventory Impact")
        
        # Calculate simulation
        current_val = store_data['Sales'].sum() * rate
        avg_price = df[df['Outlet Type'] != 'Grocery Store']['Sales'].mean() * rate
        incremental_inventory_value = skus_to_add * avg_price
        new_total_inventory_value = current_val + incremental_inventory_value

        annual_gross_merchandise_value = incremental_inventory_value * inventory_turns_per_year
        annual_gross_profit = annual_gross_merchandise_value * target_gross_margin
        annual_holding_cost = incremental_inventory_value * holding_cost_pct
        net_annual_operating_contribution = annual_gross_profit - annual_holding_cost

        m_col1, m_col2, m_col3 = st.columns(3)
        m_col1.metric("Catalogue Value Added", format_compact_currency(incremental_inventory_value, symbol), f"+{(incremental_inventory_value/current_val)*100:.1f}% expansion")
        m_col2.metric("Annual Sales Velocity", format_compact_currency(annual_gross_merchandise_value, symbol), f"{inventory_turns_per_year:.0f} turns/yr")
        m_col3.metric("Net Annual Contribution", format_compact_currency(net_annual_operating_contribution, symbol), f"After {holding_cost_pct*100:.1f}% holding cost")

        # Visualizing before and after
        chart_df = pd.DataFrame({
            'Metric': ['Current Catalogue Value', 'Incremental Uplift', 'Projected Total Value'],
            'Amount': [current_val, incremental_inventory_value, new_total_inventory_value]
        })
        fig = px.bar(
            chart_df, 
            x='Metric', 
            y='Amount', 
            text_auto='.2s',
            color='Metric', 
            color_discrete_sequence=['#6c757d', '#28a745', '#007bff'],
            title=f"Catalogue Inventory Expansion for {target_store_id}"
        )
        fig.update_layout(showlegend=False, height=320, margin=dict(t=40, b=20, l=20, r=20))
        st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"""
    <div class="insight-box">
        <b>💡 Executive Takeaway for Leadership:</b><br>
        Expanding <b>{target_store_id}</b> by <b>{skus_to_add} SKUs</b> requires an initial working capital investment of 
        <b>{symbol}{incremental_inventory_value:,.2f}</b>. At <b>{inventory_turns_per_year} annual turns</b> and a <b>{target_gross_margin*100:.1f}% margin</b>, 
        this generates <b>{symbol}{annual_gross_profit:,.2f}</b> in gross profit against <b>{symbol}{annual_holding_cost:,.2f}</b> in holding costs, 
        delivering a <b>net annual operating uplift of {symbol}{net_annual_operating_contribution:,.2f}</b>.
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# TAB 2: PRICING VARIANCE & MRP PROOF
# ==============================================================================
with tab2:
    st.header("🔬 Empirical Variance Decomposition: The 'Sales is MRP' Proof")
    st.markdown(
        "A foundational analytical error in retail analysis is assuming the `Sales` column represents total consumer revenue volume. "
        "Our mathematical decomposition proves that **99.97% of variance is explained by the SKU alone**, establishing that `Sales` "
        "is effectively **Item Maximum Retail Price (MRP)**."
    )

    # Variance decomposition calculation
    grand_mean = df['Sales'].mean()
    ss_total = ((df['Sales'] - grand_mean) ** 2).sum()
    sku_means = df.groupby('Item Identifier')['Sales'].transform('mean')
    ss_sku = ((sku_means - grand_mean) ** 2).sum()
    r2_sku = ss_sku / ss_total

    cat_means = df.groupby('Item Type')['Sales'].transform('mean')
    ss_cat = ((cat_means - grand_mean) ** 2).sum()
    r2_cat = ss_cat / ss_total

    outlet_means = df.groupby('Outlet Identifier')['Sales'].transform('mean')
    ss_outlet = ((outlet_means - grand_mean) ** 2).sum()
    r2_outlet = ss_outlet / ss_total

    v_col1, v_col2 = st.columns([1, 1])

    with v_col1:
        st.subheader("Variance Decomposition ($R^2$)")
        decomp_df = pd.DataFrame({
            'Factor': ['Item Identifier (SKU)', 'Category (Item Type)', 'Outlet Identifier (Store)'],
            'Variance Explained (%)': [r2_sku * 100, r2_cat * 100, r2_outlet * 100],
            'R_Squared': [r2_sku, r2_cat, r2_outlet]
        })
        fig_decomp = px.bar(
            decomp_df, 
            x='Factor', 
            y='Variance Explained (%)', 
            text=decomp_df['Variance Explained (%)'].apply(lambda x: f"{x:.2f}%"),
            color='Factor',
            color_discrete_sequence=['#0066cc', '#6c757d', '#dc3545'],
            title="Proportion of Sales Variance Explained by Factor"
        )
        fig_decomp.update_layout(showlegend=False, height=350)
        st.plotly_chart(fig_decomp, use_container_width=True)

    with v_col2:
        st.subheader("SKU-Level Price Consistency Inspector")
        sample_skus = df['Item Identifier'].value_counts().head(10).index.tolist()
        selected_sku = st.selectbox("Inspect SKU Price across Stores", sample_skus)
        sku_records = df[df['Item Identifier'] == selected_sku][['Outlet Identifier', 'Outlet Type', 'Sales']]
        sku_records['Sales'] = sku_records['Sales'] * rate

        fig_sku = px.scatter(
            sku_records, 
            x='Outlet Identifier', 
            y='Sales', 
            color='Outlet Type',
            size=[14]*len(sku_records),
            title=f"Unit Retail Price Dispersion for SKU: {selected_sku}",
            labels={'Sales': f'Price ({symbol})'}
        )
        fig_sku.update_layout(height=350)
        st.plotly_chart(fig_sku, use_container_width=True)

    st.markdown(f"""
    <div class="warning-box">
        <b>Mathematical Consequence:</b> The within-SKU standard deviation is only <b>{symbol}{df.groupby('Item Identifier')['Sales'].std().mean()*rate:.2f}</b>, 
        compared to the overall dataset standard deviation of <b>{symbol}{df['Sales'].std()*rate:.2f}</b>. 
        Because each record represents an item listed at an outlet with near-zero cross-store price variance, store sales totals 
        reflect <b>catalogue assortment breadth</b>, not purchasing velocity.
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# TAB 3: SIMPSON'S PARADOX & TIER 2 AUDIT
# ==============================================================================
with tab3:
    st.header("⚖️ Debunking the 'Tier 2 Outperformance Myth': Simpson's Paradox")
    st.markdown(
        "A naive aggregation suggests Tier 2 locations outperform Tier 1 and Tier 3 in average store sales. "
        "However, this is an illusion caused by **confounding by store format (Simpson's Paradox)**."
    )

    simpson_mode = st.radio(
        "Analytical View", 
        ["Naive Aggregated View (Confounded)", "Format-Controlled View (Debunked)"], 
        horizontal=True
    )

    if simpson_mode == "Naive Aggregated View (Confounded)":
        naive_df = df.groupby('Outlet Location Type')['Sales'].agg(['count', 'sum']).reset_index()
        stores_per_tier = df.groupby('Outlet Location Type')['Outlet Identifier'].nunique().reset_index()
        naive_df = naive_df.merge(stores_per_tier, on='Outlet Location Type')
        naive_df['Revenue_Per_Store'] = (naive_df['sum'] / naive_df['Outlet Identifier']) * rate

        fig_naive = px.bar(
            naive_df, 
            x='Outlet Location Type', 
            y='Revenue_Per_Store',
            text=naive_df['Revenue_Per_Store'].apply(lambda x: f"{symbol}{x:,.0f}"),
            color='Outlet Location Type',
            color_discrete_sequence=['#dc3545', '#28a745', '#ffc107'],
            title="Naive Sales-Column Value per Store by Location Tier (Misleading)"
        )
        fig_naive.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_naive, use_container_width=True)
        st.error("⚠️ Flawed Conclusion: 'Tier 2 cities are fundamentally more lucrative markets for Blinkit.'")
    else:
        controlled_df = df[df['Outlet Type'] != 'Grocery Store'].groupby('Outlet Location Type')['Sales'].agg(['sum']).reset_index()
        sm_stores = df[df['Outlet Type'] != 'Grocery Store'].groupby('Outlet Location Type')['Outlet Identifier'].nunique().reset_index()
        controlled_df = controlled_df.merge(sm_stores, on='Outlet Location Type')
        controlled_df['Revenue_Per_Supermarket'] = (controlled_df['sum'] / controlled_df['Outlet Identifier']) * rate

        fig_controlled = px.bar(
            controlled_df, 
            x='Outlet Location Type', 
            y='Revenue_Per_Supermarket',
            text=controlled_df['Revenue_Per_Supermarket'].apply(lambda x: f"{symbol}{x:,.0f}"),
            color='Outlet Location Type',
            color_discrete_sequence=['#007bff', '#007bff', '#007bff'],
            title="Supermarkets-Only Sales-Column Value per Store (Format Controlled)"
        )
        fig_controlled.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_controlled, use_container_width=True)
        st.success("✅ Robust Finding: When controlling for store format, Sales-column value per supermarket is nearly identical (~$131,000) across all urban tiers.")

    st.markdown("""
    <div class="insight-box">
        <b>Why this happened:</b> Tier 2 contains <b>zero Grocery Stores</b> (3 Supermarkets only), while Tier 1 contains 1 Grocery Store (OUT019) 
        and Tier 3 contains 1 Grocery Store (OUT010). Because Grocery Stores carry only ~541 SKUs (vs ~930 in Supermarkets), 
        their inclusion dragged down Tier 1 and Tier 3 averages. <b>This is a composition effect, not consumer demand variance.</b>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# TAB 4: SKU RECOMMENDATION ENGINE
# ==============================================================================
with tab4:
    st.header("🎯 Grocery Store Assortment Recommender")
    st.markdown(
        "Ranked list of SKUs stocked across all Supermarkets but missing in Grocery Stores (`OUT010` & `OUT019`). "
        "Use these priority scores to guide merchant catalogue onboarding."
    )

    query_missing = """
    SELECT 
        item_identifier,
        item_type,
        product_family,
        item_fat_content,
        supermarket_presence,
        mean_mrp,
        avg_rating,
        expansion_priority_score
    FROM vw_missing_sku_prioritization
    """
    missing_df = pd.read_sql_query(query_missing, conn)
    missing_df['mean_mrp'] = missing_df['mean_mrp'] * rate
    missing_df['expansion_priority_score'] = missing_df['expansion_priority_score'] * rate

    rec_col1, rec_col2 = st.columns([1, 2])

    with rec_col1:
        sel_family = st.multiselect("Filter Family", missing_df['product_family'].unique(), default=missing_df['product_family'].unique())
        sel_cat = st.multiselect("Filter Category", missing_df['item_type'].unique(), default=['Fruits and Vegetables', 'Snack Foods', 'Frozen Foods'])
        min_pres = st.slider("Minimum Supermarket Presence (Stores)", 1, 8, 7)

    filtered_missing = missing_df[
        (missing_df['product_family'].isin(sel_family)) &
        (missing_df['item_type'].isin(sel_cat)) &
        (missing_df['supermarket_presence'] >= min_pres)
    ]

    with rec_col2:
        fig_scatter = px.scatter(
            filtered_missing,
            x='mean_mrp',
            y='expansion_priority_score',
            color='item_type',
            size='supermarket_presence',
            hover_data=['item_identifier', 'avg_rating'],
            title="Expansion Priority Score vs. Unit Price (MRP)",
            labels={'mean_mrp': f'Mean MRP ({symbol})', 'expansion_priority_score': 'Priority Score'}
        )
        fig_scatter.update_layout(height=380)
        st.plotly_chart(fig_scatter, use_container_width=True)

    st.subheader(f"Recommended Onboarding Queue ({len(filtered_missing)} Candidate SKUs)")
    st.dataframe(
        filtered_missing.style.format({
            'mean_mrp': f'{symbol}{{:,.2f}}',
            'expansion_priority_score': f'{symbol}{{:,.2f}}',
            'avg_rating': '{:.2f}'
        }),
        use_container_width=True
    )

    csv_export = filtered_missing.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Export Candidate SKUs to CSV",
        data=csv_export,
        file_name='blinkit_recommended_expansion_skus.csv',
        mime='text/csv'
    )

# ==============================================================================
# TAB 5: SQL STAR SCHEMA EXPLORER
# ==============================================================================
with tab5:
    st.header("🗄️ SQL Analytics Warehouse & View Inspector")
    st.markdown(
        "The underlying analytical layer is backed by a relational SQLite/ANSI Star Schema (`blinkit_warehouse.db`). "
        "Select any analytical view below to inspect the live SQL results directly."
    )

    view_choice = st.selectbox(
        "Select Analytical Warehouse View",
        [
            "vw_outlet_assortment_gap", 
            "vw_format_controlled_tiers", 
            "vw_category_pareto", 
            "vw_missing_sku_prioritization",
            "vw_sku_pricing_variance"
        ]
    )

    limit_rows = st.slider("Row Limit", 5, 50, 15)
    view_data = pd.read_sql_query(f"SELECT * FROM {view_choice} LIMIT {limit_rows}", conn)
    st.dataframe(view_data, use_container_width=True)

    st.subheader("Interactive Custom SQL Query")
    custom_sql = st.text_area(
        "Write SQL query against `fact_inventory_pricing`, `dim_products`, `dim_outlets`:",
        value="SELECT p.item_type, COUNT(f.fact_key) AS listings, ROUND(AVG(f.sales_mrp), 2) AS avg_mrp FROM fact_inventory_pricing f JOIN dim_products p ON f.product_key = p.product_key GROUP BY p.item_type ORDER BY avg_mrp DESC LIMIT 5;"
    )

    if st.button("Execute SQL Query"):
        try:
            sql_res = pd.read_sql_query(custom_sql, conn)
            st.dataframe(sql_res, use_container_width=True)
            st.success(f"Query returned {len(sql_res)} rows.")
        except Exception as e:
            st.error(f"SQL Error: {e}")

# ------------------------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------------------------
st.markdown("---")
st.caption(
    "Blinkit Quick-Commerce Analytics Engineering Suite · Portfolio Flagship Project 1 · "
    "Designed for Senior Data Analyst / Junior Data Scientist Interview Evaluation"
)
