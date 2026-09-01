import pandas as pd

DATA_PATH = "data/retail_sales.csv"

df = pd.read_csv(DATA_PATH, parse_dates=["Order_Date"])

print("=== DATASET OVERVIEW ===")
print(df.info())
print("\n=== KPIs ===")
print(f"Orders: {df['Order_ID'].nunique()}")
print(f"Customers: {df['Customer_ID'].nunique()}")
print(f"Units sold: {df['Quantity'].sum()}")
print(f"Sales: {df['Sales'].sum():,.2f}")
print(f"Profit: {df['Profit'].sum():,.2f}")
print(f"Profit margin: {df['Profit'].sum()/df['Sales'].sum():.1%}")

print("\n=== CATEGORY PERFORMANCE ===")
category = (df.groupby("Category", as_index=False)
              .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"), Units=("Quantity", "sum"))
              .sort_values("Sales", ascending=False))
print(category.to_string(index=False))

print("\n=== CITY PERFORMANCE ===")
city = (df.groupby("City", as_index=False)
          .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
          .sort_values("Sales", ascending=False))
print(city.to_string(index=False))

print("\n=== TOP CUSTOMERS ===")
customers = (df.groupby("Customer_ID", as_index=False)
               .agg(Orders=("Order_ID", "nunique"), Sales=("Sales", "sum"), Profit=("Profit", "sum"))
               .sort_values("Sales", ascending=False))
print(customers.head(10).to_string(index=False))

print("\n=== MONTHLY TREND ===")
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
monthly = df.groupby("Month", as_index=False).agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
print(monthly.to_string(index=False))
