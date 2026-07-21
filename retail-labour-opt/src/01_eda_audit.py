import pandas as pd

# 1. Loading the gen'd data
df = pd.read_csv("retail-labor-optimization/data/raw/dirty_supermarket_sales_2025.csv")

print("==================================================\n")

# ---- INVESTIGATION 1: Missing Operational Tracking ----
print("🔍 PROBING: Checking for Missing Identifiers")
missing_summary = df.isnull().sum()
print(missing_summary[missing_summary > 0])

# Store Name has missing records. We can't drop these because we lose revenue tracking; we must impute them.
print("-" * 50)

# ---- INVESTIGATION 2: Categorical Fragmentation ----
print("🔍 INVESTIGATION 2: Checking Unique Categorical Groups")
print("Raw unique values in 'payment_method':")
print(df['payment_method'].unique())
print("\nValue counts for 'payment_method':")
print(df['payment_method'].value_counts())
print("💡 INFERENCE: The database is capturing duplicates due to casing variations (e.g., 'CASH' vs 'Cash'). This will break pivot tables and aggregations until normalized.\n")
print("-" * 50)

# ---- INVESTIGATION 3: Auditing Financial Integrity----
print("🔍 INVESTIGATION 3: Auditing Financial Columns (Min/Max Profiles)")
financial_profile = df[['quantity', 'unit_price', 'total_amount', 'discount_amount', 'final_amount']].describe().loc[['min', 'max', 'mean']]
print(financial_profile.to_string())

# Isolating the negative offenders
negative_revenue = df[df['final_amount'] < 0]
print(f"\n CRITICAL FINDING: Found {len(negative_revenue)} rows where 'final_amount' is negative!")
print("Sample of negative revenue anomalies:")
print(negative_revenue[['total_amount', 'discount_amount', 'final_amount']].head(3).to_string())
print("💡 INFERENCE: The POS application has a structural bug allowing discount coupons to exceed total basket price, leaking phantom losses into the ledger.\n")
print("-" * 50)

# ---- INVESTIGATION 4: Operational Check (Firsthand Business Inference) ----
print("🔍 INVESTIGATION 4: Firsthand Operational Inferences (Socio-Temporal Check)")
# Extracting temporary hours just to see if a traffic pattern exists even in the dirt
df['temp_hour'] = df['transaction_time'].str.split(':').str[0].astype(int)
peak_hours_raw = df['temp_hour'].value_counts().sort_index()

print("\nRaw Transaction Volume by Hour Block:")
for hour, count in peak_hours_raw.items():
    # Simple text bar chart to visualize peak loads inline
    bar = "█" * (count // 15)
    print(f"   {hour:02d}:00 block -> {count:3d} transactions {bar}")

print("\n💡 FIRSTHAND BUSINESS INFERENCE:")
print(" Even with messy data, a clear operational wave is visible.")
print(" Traffic heavily accelerates after 16:00 (4 PM) and peaks between 17:00 and 18:00 (5-6 PM).")
print(" This confirms that an hourly scheduling model is highly viable once data is standardized.")
