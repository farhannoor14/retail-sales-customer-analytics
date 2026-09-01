import pandas as pd

REQUIRED_COLUMNS = [
    "Order_ID", "Customer_ID", "Order_Date", "City", "Category",
    "Product", "Quantity", "Unit_Price", "Discount", "Sales", "Profit"
]

df = pd.read_csv("data/retail_sales.csv")

print("=== DATA QUALITY REPORT ===")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Missing values: {int(df.isna().sum().sum())}")
print(f"Duplicate rows: {int(df.duplicated().sum())}")
print(f"Required columns present: {set(REQUIRED_COLUMNS).issubset(df.columns)}")
print(f"Negative quantity rows: {int((df['Quantity'] < 0).sum())}")
print(f"Invalid discounts: {int(((df['Discount'] < 0) | (df['Discount'] > 1)).sum())}")

# Recalculate sales and flag unexpected differences.
expected_sales = df["Quantity"] * df["Unit_Price"] * (1 - df["Discount"])
difference = (df["Sales"] - expected_sales).abs()
print(f"Sales calculation exceptions (>0.01): {int((difference > 0.01).sum())}")
