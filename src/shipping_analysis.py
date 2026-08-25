import pandas as pd
pd.set_option("display.max_columns", None)
from pathlib import Path
import matplotlib.pyplot as plt

#Get project root dir
project_root = Path(__file__).resolve().parent.parent

#Path to the dataset
file_path = project_root / "data" / "raw" / "sample_-_superstore.xls"

#Load dataset
df = pd.read_excel(file_path)

print("DATASET LOADED SUCCESSFULLY")

print("\nSHIPPING MODES:")
print(df["Ship Mode"].value_counts())

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

#Calc shipping time
df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

print("\n" + "=" * 50)
print("SHIPPING TIME ANALYSIS")
print("=" * 50)

print(df["Shipping Days"].describe())


print("\n" + "=" * 50)
print("AVERAGE SHIPPING DAYS BY MODE")
print("=" * 50)

shipping_by_mode = (
    df.groupby("Ship Mode")
    .agg(
        Average_Shipping_Days = ("Shipping Days", "mean"),
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

shipping_by_mode["Profit Margin"] = (
    shipping_by_mode["Profit"] / shipping_by_mode["Sales"]
)

print(shipping_by_mode)



print("\n" + "=" * 50)
print("UNIQUE ORDERS BY SHIPPING MODE")
print("=" * 50)

orders_by_mode = (
    df.groupby("Ship Mode")["Order ID"]
    .nunique()
    .sort_values(ascending=False)
)

print(orders_by_mode)

print("\n" + "=" * 50)
print("SHIPPING MODE BY REGION")
print("=" * 50)

shipping_region = pd.crosstab(
    df["Region"],
    df["Ship Mode"]
)

print(shipping_region)

shipping_speed = shipping_by_mode["Average_Shipping_Days"].sort_values()

shipping_speed.plot(kind="bar")

plt.title("Average Shipping Time by Shipping Mode")
plt.xlabel("Shipping Mode")
plt.ylabel("Average Shipping Days")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    project_root / "outputs" / "shipping_time_by_mode.png"
)

plt.show()