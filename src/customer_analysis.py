import matplotlib.pyplot as plt
import pandas as pd
pd.set_option("display.max_columns", None)
from pathlib import Path

#Get the project root directory
project_root = Path(__file__).resolve().parent.parent

#Path to the dataset
file_path = project_root / "data" / "raw" / "sample_-_superstore.xls"

#Load the dataset
df = pd.read_excel(file_path)

print("DATASET LOADED SUCCESSFULLY")

print("\nCUSTOMER SEGMENTS:")
print(df["Segment"].value_counts())

print("\n" + "=" * 50)
print("CUSTOMER SEGMENT PERFORMANCE")
print("=" * 50)

segment_performance = (
    df.groupby("Segment")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
)

segment_performance["Profit Margin"] = (
    segment_performance["Profit"] / segment_performance["Sales"]
)

print(segment_performance)

print("\n" + "=" * 50)
print("TOP 10 CUSTOMER BY SALES")
print("=" * 50)

customer_performance = (
    df.groupby("Customer Name")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
)

customer_performance["Profit Margin"] = (
    customer_performance["Profit"] / customer_performance["Sales"]
)

customer_performance = customer_performance.sort_values(
    "Sales",
    ascending=False
)

print(customer_performance.head(10))

print("\n" + "=" * 50)
print("TOP 10 CUSTOMERS BY PROFIT")
print("=" * 50)

top_profit_customers = customer_performance.sort_values(
    "Profit",
    ascending=False
)

print(top_profit_customers.head(10))

print("\n" + "=" * 50)
print("BOTTOM 10 CUSTOMERS BY PROFIT")
print("=" * 50)

bottom_profit_customers = customer_performance.sort_values(
    "Profit",
    ascending=True
)

print(bottom_profit_customers.head(10))

print("\n" + "=" * 50)
print("CUSTOMER DISCOUNT ANALYSIS")
print("=" * 50)

customer_discount = (
    df.groupby("Customer Name")
    .agg(
        Average_Discount=("Discount", "mean"),
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

customer_discount = customer_discount.sort_values(
    "Profit",
    ascending=True
)

print(customer_discount.head(10))

#Create customer segment profit chart
segment_performance["Profit"].plot(kind="bar")

plt.title("Profit by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Profit ($)")
plt.tight_layout()

plt.savefig(
    project_root / "outputs" / "profit_by_customer_segment.png"
)

plt.show()