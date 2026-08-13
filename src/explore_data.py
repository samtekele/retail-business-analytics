import pandas as pd

file_path = "data/raw/sample_-_superstore.xls"

df = pd.read_excel(file_path)

print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)

print("\nDATASET SHAPE:")
print(df.shape)

print("\nCOLUMN NAMES:")
print(df.columns.tolist())

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\n" + "=" * 50)
print("BUSINESS METRICS")
print("=" * 50)

print("\nTOTAL SALES:")
print(f"${df['Sales'].sum():,.2f}")

print("\nTOTAL PROFIT:")
print(f"${df['Profit'].sum():,.2f}")

print("\nTOTAL QUANTITY SOLD:")
print(f"{df['Quantity'].sum():,}")

print("\nTOTAL TRANSACTIONS:")
print(f"{len(df):,}")

print("\n" + "=" * 50)
print("SALES BY CATEGORY")
print("=" * 50)

sales_by_category = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(sales_by_category)

print("\n" + "=" * 50)
print("PROFIT BY CATEGORY")
print("=" * 50)

profit_by_category = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print(profit_by_category)

print("\n" + "=" * 50)
print("SALES BY REGION")
print("=" * 50)

sales_by_region = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(sales_by_region)

print("\n" + "=" * 50)
print("PROFIT BY REGION")
print("=" * 50)

profit_by_region = (
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print(profit_by_region)



print("\n" + "=" * 50)
print("PROFIT MARGINS")
print("=" * 50)

overall_profit_margin = df["Profit"].sum() / df["Sales"].sum()

print("\nOVERALL PROFIT MARGIN:")
print(f"{overall_profit_margin:.2%}")

category_profit_margin = (
    df.groupby("Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

category_profit_margin["Profit Margin"] = (
    category_profit_margin["Profit"] /
    category_profit_margin["Sales"]
)

print("\nPROFIT MARGIN BY CATEGORY:")
print(category_profit_margin.sort_values("Profit Margin", ascending=False))

region_profit_margin = (
    df.groupby("Region")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

region_profit_margin["Profit Margin"] = (
    region_profit_margin["Profit"] /
    region_profit_margin["Sales"]
)

print("\nPROFIT MARGIN BY REGION:")
print(region_profit_margin.sort_values("Profit Margin", ascending=False))


print("\n" + "=" * 50)
print("DISCOUNT ANALYSIS")
print("=" * 50)

discount_by_category = (
    df.groupby("Category")
    .agg(
        Average_Discount=("Discount", "mean"),
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    )
)

print("\nDISCOUNT BY CATEGORY:")
print(discount_by_category.sort_values("Average_Discount", ascending=False))

print("\n" + "=" * 50)
print("FURNITURE SUB-CATEGORY ANALYSIS")
print("=" * 50)

furniture = df[df["Category"] == "Furniture"]

furniture_analysis = (
    furniture.groupby("Sub-Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum"),
        Average_Discount=("Discount", "mean")
    )
)

furniture_analysis["Profit Margin"] = (
    furniture_analysis["Profit"] /
    furniture_analysis["Sales"]
)

print(
    furniture_analysis
    .sort_values("Profit Margin")
)



print("\n" + "=" * 50)
print("DISCOUNT VS PROFITABILITY")
print("=" * 50)

discount_analysis = (
    df.groupby("Discount")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
)

discount_analysis["Profit Margin"] = (
    discount_analysis["Profit"] /
    discount_analysis["Sales"]
)

print("\nPROFITABILITY BY DISCOUNT LEVEL:")
print(discount_analysis.sort_index())

print("\n" + "=" * 50)
print("CATEGORY PERFORMANCE BY REGION")
print("=" * 50)

region_category = (
    df.groupby(["Region", "Category"])
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum"),
        Average_Discount=("Discount", "mean")
    )
)

region_category["Profit Margin"] = (
    region_category["Profit"] /
    region_category["Sales"]
)

print(region_category)