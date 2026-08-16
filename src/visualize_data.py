import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from pathlib import Path

# Get the project root directory
project_root = Path(__file__).resolve().parent.parent

#Path to the dataset
file_path = project_root / "data" / "raw" / "sample_-_superstore.xls"

#Load the dataset
df = pd.read_excel(file_path)

#Create output folder for charts
output_dir = project_root / "outputs"
output_dir.mkdir(exist_ok=True)

print("Dataset loaded successfully!")
print(f"Charts will be saved to: {output_dir}")

#Calculate total sales by category
sales_by_category = df.groupby("Category")["Sales"].sum()

#Create the chart
sales_by_category.plot(kind="bar")

#Add labels and title
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales ($)")

#Make sure nothing gets cut off
plt.tight_layout()

#Save chart
plt.savefig(output_dir / "sales_by_category.png")

#Display Chart
plt.show()


profit_by_category = df.groupby("Category")["Profit"].sum()
profit_by_category.plot(kind="bar")
plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit ($)")
plt.tight_layout()
plt.savefig(output_dir / "profit_by_category.png")
plt.show()

profit_by_region = df.groupby("Region")["Profit"].sum()
profit_by_region.plot(kind="bar")
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit ($)")
plt.tight_layout()
plt.savefig(output_dir / "profit_by_region.png")
plt.show()


profit_by_discount = df.groupby("Discount").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
)
profit_by_discount["Profit_Margin"] = (
    profit_by_discount["Profit"] / profit_by_discount["Sales"]
)
profit_by_discount["Profit_Margin"].plot(kind="line", marker="o")
plt.title("Profit Margin by Discount Level")
plt.xlabel("Discount")
plt.ylabel("Profit Margin")
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.tight_layout()
plt.savefig(output_dir / "discount_profitability.png")
plt.show()

profit_by_subcategory = df.groupby("Sub-Category")["Profit"].sum()
profit_by_subcategory = profit_by_subcategory.sort_values()
print("\nWORST-PERFORMING SUB-CATEGORIES:")
print(profit_by_subcategory.head(5))
profit_by_subcategory.head(5).plot(kind="bar")
plt.title("5 Least Profitable Sub-Categories")
plt.xlabel("Sub-Category")
plt.ylabel("Total Profit ($)")
plt.tight_layout()
plt.savefig(output_dir / "worst_subcategories.png")
plt.show()