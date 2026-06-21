import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("sales_data.csv")

# Total Sales
df["Sales"] = df["Quantity"] * df["Price"]

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# Extract Month
df["Month"] = df["Date"].dt.strftime("%B")

print(df.head())

# Total Sales
print("\nTotal Sales:")
print(df["Sales"].sum())

# Top Selling Products
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("\nTop Products")
print(top_products)

# Monthly Sales
monthly_sales = df.groupby("Month")["Sales"].sum()
print("\nMonthly Sales")
print(monthly_sales)

# Region Sales
region_sales = df.groupby("Region")["Sales"].sum()
print("\nRegion Sales")
print(region_sales)

# Plot Monthly Sales
plt.figure(figsize=(8,5))
monthly_sales.plot(kind="bar")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

# Plot Top Products
plt.figure(figsize=(8,5))
top_products.plot(kind="bar")
plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("top_products.png")
plt.show()