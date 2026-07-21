import pandas as pd
import numpy as np

# Loading the messy data
df = pd.read_csv("retail-labour-opt/data/raw/dirty_supermarket_sales_2025.csv")

print("==================================================")

# ---- TARGET 1: Standardizing Text Casing ----
print("Fix 1: Standardizing payment method text casing...")
df['payment_method'] = df['payment_method'].str.title() 

# ---- TARGET 2: Imputing Missing Store Names ----
print("Fix 2: Imputing missing store branch fields...")
df['store_name'] = df['store_name'].fillna('Unknown Branch')

# ---- TARGET 3: Plugging the Financial Discount Leak ----
print("Fix 3: Auditing and repairing discount calculation leaks...")
glitch_mask = df['final_amount'] < 0
df.loc[glitch_mask, 'discount_amount'] = df.loc[glitch_mask, 'total_amount']
df['final_amount'] = np.round(df['total_amount'] - df['discount_amount'], 2)

# ---- TARGET 4: Feature Engineering for Hourly Staffing ----
print("Fix 4: Engineering time-block features for optimization dashboard...")
df['transaction_date'] = pd.to_datetime(df['transaction_date'])
df['day_of_week'] = df['transaction_date'].dt.day_name()
df['hour_block'] = pd.to_datetime(df['transaction_time'], format='%H:%M').dt.hour

# Saving the dataset
output_filename = "retail-labour-opt/data/processed/clean_supermarket_sales_2025.csv"
df.to_csv(output_filename, index=False)

print('\n', f"💾 PIPELINE SUCCESS: Clean data saved to '{output_filename}'")
print("==================================================")
