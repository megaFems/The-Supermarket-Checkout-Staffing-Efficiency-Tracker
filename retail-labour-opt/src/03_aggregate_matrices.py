import pandas as pd

# 1. Loading cleaned data
df = pd.read_csv("retail-labour-opt/data/processed/clean_supermarket_sales_2025.csv")
print("==================================================\n")

# Ordering the days logically instead of alphabetically for a cleaner final view
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# 2. Building the Traffic Velocity Pivot Table (Count of Transactions)
traffic_pivot = df.pivot_table(
    index='hour_block', 
    columns='day_of_week', 
    values='customer_id', 
    aggfunc='count', 
    fill_value=0
)
# Reindexing columns to standard weekly chronological order
traffic_pivot = traffic_pivot.reindex(columns=day_order)

# 3. Building the Revenue Efficiency Pivot Table (Sum of Final Revenue)
revenue_pivot = df.pivot_table(
    index='hour_block', 
    columns='day_of_week', 
    values='final_amount', 
    aggfunc='sum', 
    fill_value=0
).round(2)
revenue_pivot = revenue_pivot.reindex(columns=day_order)

# 4. Printing a sneak peek of the Traffic Velocity Matrix for the lead's review
print("🔹 TRANSACTION VELOCITY MATRIX (TRAFFIC HEATMAP PREVIEW):")
print(traffic_pivot)
print("\n" + "="*50 + "\n")

# 5. Exporting both matrices to CSV so we can easily plug them into visualization tools
traffic_pivot.to_csv("retail-labour-opt/data/prcessed/matrix_hourly_traffic.csv")
revenue_pivot.to_csv("retail-labour-opt/data/prcessed/matrix_hourly_revenue.csv")

print("SUCCESS: Matrix aggregations exported!")
print("   - 'matrix_hourly_traffic.csv' -> For staffing counts.")
print("   - 'matrix_hourly_revenue.csv' -> For cash flow coverage.")
print("==================================================")
