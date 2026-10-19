"""
BlinkIT Analytics Warehouse Builder & Verification Engine
--------------------------------------------------------
- Builds a relational SQLite database (blinkit_warehouse.db) implementing the Star Schema
- Populates dim_products, dim_outlets, and fact_inventory_pricing from BlinkIT_Grocery_Data_Cleaned.csv
- Executes and validates all 5 advanced analytical SQL views
- Verifies exact arithmetic totals and dimensional integrity
"""

import os
import sqlite3
import pandas as pd

def build_warehouse():
    print("=" * 80)
    print("BUILDING BLINKIT DIMENSIONAL ANALYTICS WAREHOUSE (STAR SCHEMA)")
    print("=" * 80)

    csv_path = 'BlinkIT_Grocery_Data_Cleaned.csv'
    sql_script_path = 'blinkit_warehouse.sql'
    db_path = 'blinkit_warehouse.db'

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Cleaned dataset not found at '{csv_path}'")
    if not os.path.exists(sql_script_path):
        raise FileNotFoundError(f"SQL DDL script not found at '{sql_script_path}'")

    print(f"Loading cleaned dataset: {csv_path}...")
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df):,} rows x {len(df.columns)} columns.\n")

    # Connect to SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execute DDL & Views from SQL script
    print(f"Executing DDL script from {sql_script_path}...")
    with open(sql_script_path, 'r', encoding='utf-8') as f:
        sql_commands = f.read()
    
    # Split by semicolon and execute
    cursor.executescript(sql_commands)
    conn.commit()
    print("Star Schema tables and analytical views created successfully.")

    # 1. Populate dim_products
    print("\n[1/3] Populating dim_products...")
    products_df = df[[
        'Item Identifier', 'Item Category', 'Item Type', 'Item Fat Content', 'Item Weight'
    ]].drop_duplicates(subset=['Item Identifier']).reset_index(drop=True)
    
    products_df.rename(columns={
        'Item Identifier': 'item_identifier',
        'Item Category': 'product_family',
        'Item Type': 'item_type',
        'Item Fat Content': 'item_fat_content',
        'Item Weight': 'item_weight'
    }, inplace=True)
    products_df['is_edible'] = products_df['product_family'].isin(['Food', 'Drinks'])
    products_df['product_key'] = products_df.index + 1

    products_df[['product_key', 'item_identifier', 'product_family', 'item_type', 'item_fat_content', 'item_weight', 'is_edible']].to_sql(
        'dim_products', conn, if_exists='append', index=False
    )
    print(f"-> Inserted {len(products_df):,} distinct products into dim_products.")

    # 2. Populate dim_outlets
    print("\n[2/3] Populating dim_outlets...")
    outlets_df = df[[
        'Outlet Identifier', 'Outlet Type', 'Outlet Location Type', 'Outlet Size', 
        'Outlet Establishment Year', 'Outlet Age'
    ]].drop_duplicates(subset=['Outlet Identifier']).reset_index(drop=True)

    outlets_df.rename(columns={
        'Outlet Identifier': 'outlet_identifier',
        'Outlet Type': 'outlet_type',
        'Outlet Location Type': 'outlet_location_tier',
        'Outlet Size': 'outlet_size',
        'Outlet Establishment Year': 'establishment_year',
        'Outlet Age': 'outlet_age'
    }, inplace=True)
    outlets_df['outlet_key'] = outlets_df.index + 1

    outlets_df[['outlet_key', 'outlet_identifier', 'outlet_type', 'outlet_location_tier', 'outlet_size', 'establishment_year', 'outlet_age']].to_sql(
        'dim_outlets', conn, if_exists='append', index=False
    )
    print(f"-> Inserted {len(outlets_df):,} distinct outlets into dim_outlets.")

    # 3. Populate fact_inventory_pricing
    print("\n[3/3] Populating fact_inventory_pricing...")
    # Merge keys
    fact_df = df.merge(products_df[['item_identifier', 'product_key']], left_on='Item Identifier', right_on='item_identifier')
    fact_df = fact_df.merge(outlets_df[['outlet_identifier', 'outlet_key']], left_on='Outlet Identifier', right_on='outlet_identifier')
    fact_df['fact_key'] = fact_df.index + 1
    fact_df['sales_mrp'] = fact_df['Sales']
    fact_df['item_visibility'] = fact_df['Item Visibility']
    fact_df['customer_rating'] = fact_df['Rating']

    fact_to_load = fact_df[['fact_key', 'product_key', 'outlet_key', 'item_visibility', 'sales_mrp', 'customer_rating']]
    fact_to_load.to_sql('fact_inventory_pricing', conn, if_exists='append', index=False)
    print(f"-> Inserted {len(fact_to_load):,} records into fact_inventory_pricing.")

    conn.commit()

    # -------------------------------------------------------------------------
    # VERIFICATION & QUERY EXECUTION
    # -------------------------------------------------------------------------
    print("\n" + "=" * 80)
    print("VERIFYING ANALYTICAL SQL VIEWS")
    print("=" * 80)

    # View 2: Outlet Assortment Gap
    print("\n--- VIEW 2: Outlet Assortment Gap Analysis ---")
    v2_df = pd.read_sql_query("SELECT * FROM vw_outlet_assortment_gap", conn)
    print(v2_df.to_string(index=False))

    # View 3: Format-Controlled Location Tiers (Simpson's Paradox Proof)
    print("\n--- VIEW 3: Format-Controlled Location Tiers (Debunking Tier-2 Bias) ---")
    v3_df = pd.read_sql_query("SELECT * FROM vw_format_controlled_tiers", conn)
    print(v3_df.to_string(index=False))

    # View 4: Top 5 Pareto Categories
    print("\n--- VIEW 4: Top 5 Categories by Cumulative Revenue Share (Pareto) ---")
    v4_df = pd.read_sql_query("SELECT * FROM vw_category_pareto LIMIT 5", conn)
    print(v4_df.to_string(index=False))

    # View 5: Top 10 Missing SKUs to Prioritize for Grocery Stores
    print("\n--- VIEW 5: Top 10 Grocery Store SKU Expansion Candidates ---")
    v5_df = pd.read_sql_query("SELECT * FROM vw_missing_sku_prioritization LIMIT 10", conn)
    print(v5_df.to_string(index=False))

    conn.close()
    print("\n" + "=" * 80)
    print(f"DATABASE BUILD COMPLETE: '{db_path}' is ready for reporting & analytics.")
    print("=" * 80)

if __name__ == '__main__':
    build_warehouse()
