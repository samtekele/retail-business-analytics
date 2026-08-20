import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#Get the project root directory
project_root = Path(__file__).resolve().parent.parent

#Path to the dataset
file_path = project_root / "data" / "raw" / "sample_-_superstore.xls"

#Load the dataset
df = pd.read_excel(file_path)

#Make sure Order Date is treated as a date
df["Order Date"] = pd.to_datetime(df["Order Date"])

#Create new time-based columns
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.month_name()

print("TIME COLUMNS CREATED SUCESSFULLY")

print("\nYEARS IN DATABASE")
print(sorted(df["Year"].unique()))

print("\nFIRST 5 ORDER DATES: ")
print(df[["Order Date", "Year", "Month", "Month Name"]].head())

print("\n" + "=" * 50)
print("YEARLY SALES AND PROFIT")
print("=" * 50)

yearly_performance = (
    df.groupby("Year")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

yearly_performance["Profit Margin"] = (
    yearly_performance["Profit"] / yearly_performance["Sales"]
)

print(yearly_performance)

#Calculate year-over-yaer sales growth
yearly_performance["Sales Growth"] = (
    yearly_performance["Sales"].pct_change()
)

print("\nYEAR-OVER-YEAR SALES GROWTH:")
growth_display = yearly_performance[["Sales", "Sales Growth"]].copy()
growth_display["Sales Growth"] = growth_display["Sales Growth"] * 100
print(growth_display)


print("\n" + "=" * 50)
print("MONTHLY SALES PERFORMANCE")
print("=" * 100)

monthly_performance = (
    df.groupby(["Month", "Month Name"])
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values("Month")
)

print(monthly_performance)


#Create yearly sales trend chart
yearly_performance["Sales"].plot(
    kind="line",
    marker="o"
)

plt.title("Yearly Sales Trend")
plt.xlabel("Year")
plt.ylabel("Total Sales ($)")
plt.xticks(yearly_performance.index)
plt.tight_layout()
plt.savefig(
    project_root / "outputs" / "yearly_sales_trend.png"
)
plt.show()


#Create monthly sales trend chart
plt.figure()

plt.plot(
    monthly_performance["Month Name"],
    monthly_performance["Sales"],
    marker="o"
)
plt.title("Monthly Sales Performance")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    project_root / "outputs" / "monthly_sales_trend.png"
)
plt.show()

#Create yearly profit trend chart
plt.figure()

yearly_performance["Profit"].plot(
    kind="line",
    marker="o"
)

plt.title("Yearly Profit Trend")
plt.xlabel("Year")
plt.ylabel("Total Profit ($)")
plt.xticks(yearly_performance.index)

plt.tight_layout()

plt.savefig(
    project_root / "outputs" / "yearly_profit_trend.png"
)
plt.show()