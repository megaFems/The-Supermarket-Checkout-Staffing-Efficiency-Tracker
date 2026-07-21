### Importing Essential libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



################ Week Day-Hour Traffic Velocity Heatmap ################

# 1. Loading the generated traffic matrix
df_matrix = pd.read_csv("retail-labour-opt/data/processed/matrix_hourly_traffic.csv", index_col='hour_block')

# 2. Seting up the plotting environment style
plt.figure(figsize=(12, 8))
sns.set_theme(style="whitegrid")

# 3. Creating the heatmap
ax = sns.heatmap(
    df_matrix, 
    annot=True, 
    fmt="d", 
    cmap="YlOrRd", 
    linewidths=0.5,
    cbar_kws={'label': 'Hourly Transaction Volume'}
)

# 4. Polishing the labels for executive presentation
plt.title("Retail Labor Optimization: Hourly Transaction Velocity Matrix", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Day of the Week", fontsize=12, fontweight='bold', labelpad=10)
plt.ylabel("Hour of Day (24h Clock)", fontsize=12, fontweight='bold', labelpad=10)

# Formating y-axis ticks to read clearly as time blocks
plt.yticks(rotation=0)

# 5. Saving the graphic
plt.tight_layout()
output_image = "retail-labour-opt/output/figures/my_fiverr_portfolio_heatmap.png"
plt.savefig(output_image, dpi=300)
print("==================================================")
print(f" VISUALIZATION SUCCESS: Heatmap generated!")
print(f"💾 File saved as: '{output_image}'")
print("==================================================")
plt.show()



##################### Customer Behaviour Matrix ####################

# Loading the clean dataset
df = pd.read_csv("clean_supermarket_sales_2025.csv")

print("   CUSTOMER BEHAVIOR MATRIX (PEAK)     ")
print("==================================================\n")

# Filtering only for the critical peak hours (5 PM & 6 PM)
peak_hours_mask = df['hour_block'].isin([17, 18])
df_peak = df[peak_hours_mask]

# Grouping by the engineered day of week and customer type, count transactions
customer_pivot = df_peak.pivot_table(
    index='day_of_week', 
    columns='Customer Type', 
    values='customer_id', 
    aggfunc='count', 
    fill_value=0
)

# Reordering the days logically
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
customer_pivot = customer_pivot.reindex(day_order)

print("🔹 PEAK HOUR TRANSACTION VELOCITY (MEMBER VS NORMAL):")
print(customer_pivot)
print("\n" + "="*50 + "\n")

# Exporting for visualization
customer_pivot.to_csv("matrix_peak_customers.csv")
print("💾 SUCCESS: Peak customer behavior matrix exported to 'matrix_peak_customers.csv'")




################## Bottleneck Analysis Chart ##########################

# 1. Loading the cleaned data
df = pd.read_csv("clean_supermarket_sales_2025.csv")

print(" GENERATING REGISTER BOTTLENECK CHART ")
print("==================================================")

# 2. Isolating the high-pressure peak hours (17:00 and 18:00)
df_peak = df[df['hour_block'].isin([17, 18])].copy()

# 3. Creating an explicit ordered category for days of the week
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df_peak['day_of_week'] = pd.Categorical(df_peak['day_of_week'], categories=day_order, ordered=True)

# 4. Grouping the data to get counts of payment methods used on each day during peak hours
payment_counts = df_peak.groupby(['day_of_week', 'payment_method'], observed=False).size().unstack(fill_value=0)

# 5. Plotting the Stacked Bar Chart
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")
colors = ['#2ec4b6', '#e71d36', '#ff9f1c'] # Teal, Red, Orange

payment_counts.plot(kind='bar', stacked=True, color=colors, ax=plt.gca(), width=0.7)

# 6. Formatting for executive presentation slide
plt.title("Checkout Bottleneck Analysis: Peak Hour Payment Methods (5PM - 7PM)", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Day of the Week", fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel("Number of Transactions", fontsize=11, fontweight='bold', labelpad=10)
plt.xticks(rotation=45)
plt.legend(title="Payment Type", frameon=True)

plt.tight_layout()

# 7. Saving the visual
output_image = "retail-labour-opt/output/figures/my_fiverr_portfolio_payment_bottlenecks.png"
plt.savefig(output_image, dpi=300)
print(f"\n💾 VISUALIZATION SUCCESS: Second asset saved as: '{output_image}'")
print("==================================================")
plt.show()





########################## Final Dashboard ###############################3

# 1. Loading the required clean dataset and matrices
df = pd.read_csv("retail-labour-opt/data/processed/clean_supermarket_sales_2025.csv")
df_traffic = pd.read_csv("data/processed/matrix_hourly_traffic.csv", index_col='hour_block')
df_customer = pd.read_csv("data/processed/matrix_peak_customers.csv", index_col='day_of_week')

# Setting standard day order for consistency across plots
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df_customer = df_customer.reindex(day_order)

# Isolating peak hour payment data for the third chart
df_peak = df[df['hour_block'].isin([17, 18])].copy()
df_peak['day_of_week'] = pd.Categorical(df_peak['day_of_week'], categories=day_order, ordered=True)
payment_counts = df_peak.groupby(['day_of_week', 'payment_method'], observed=False).size().unstack(fill_value=0)

# 2. Initializing a 2x2 grid layout using GridSpec
fig = plt.figure(figsize=(18, 12))
sns.set_theme(style="whitegrid")
plt.suptitle("EXECUTIVE RETAIL OPTIMIZATION DASHBOARD (2025)", fontsize=22, fontweight='bold', y=0.96)

# Creating a 2-row, 2-column grid layout
gs = fig.add_gridspec(2, 2)

# Custom color palette for clean presentation
colors_payment = ['#2ec4b6', '#e71d36', '#ff9f1c']
colors_customer = ['#4ea8de', '#56cfe1']

# --- CHART 1: The Main Traffic Heatmap (Row 0, Spans columns 0 and 1) ---
ax1 = fig.add_subplot(gs[0, :]) 
sns.heatmap(df_traffic, annot=True, fmt="d", cmap="YlOrRd", linewidths=0.5, ax=ax1, cbar_kws={'label': 'Hourly Count'})
ax1.set_title("1. Hourly Transaction Velocity Matrix (Operational Pressure Lines)", fontsize=13, fontweight='bold', pad=10)
ax1.set_xlabel("Day of the Week", fontweight='bold')
ax1.set_ylabel("Hour of Day (24h Clock)", fontweight='bold')

# --- CHART 2: Customer Type Profile (Row 1, Column 0) ---
ax2 = fig.add_subplot(gs[1, 0])
df_customer.plot(kind='bar', ax=ax2, color=colors_customer, width=0.6, edgecolor='black')
ax2.set_title("2. Peak Hour Customer Mix (5PM - 7PM Volume Dynamics)", fontsize=13, fontweight='bold', pad=10)
ax2.set_xlabel("Day of the Week", fontweight='bold')
ax2.set_ylabel("Customer Count", fontweight='bold')
ax2.set_xticklabels(day_order, rotation=35)
ax2.legend(title="Customer Type")

# --- CHART 3: Payment Method Bottlenecks (Row 1, Column 1) ---
ax3 = fig.add_subplot(gs[1, 1])
payment_counts.plot(kind='bar', stacked=True, color=colors_payment, ax=ax3, width=0.6, edgecolor='black')
ax3.set_title("3. Peak Hour Register Bottlenecks (Payment Vulnerabilities)", fontsize=13, fontweight='bold', pad=10)
ax3.set_xlabel("Day of the Week", fontweight='bold')
ax3.set_ylabel("Transaction Count", fontweight='bold')
ax3.set_xticklabels(day_order, rotation=35)
ax3.legend(title="Payment Method")

# 3. Final polish and export
plt.tight_layout(rect=[0, 0, 1, 0.93])
output_dashboard = "retail-labour-opt/output/figures/retail_store_final_dashboard.png"
plt.savefig(output_dashboard, dpi=300)

print("==================================================")
print("Presentation Dashboard Created ")
print(f"💾 Dashboard saved as: '{output_dashboard}'")
print("==================================================")
plt.show()
