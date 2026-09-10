import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

file_path = "data/raw/sample_-_superstore.xls"
df = pd.read_excel(file_path)

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)
print(monthly_sales)

train = monthly_sales.iloc[:36]
test = monthly_sales.iloc[36:]

print("\nTraining Data:")
print(train)

print("\nTesting Data:")
print(test)

model = ExponentialSmoothing(
    train["Sales"],
    trend="add",
    seasonal="add",
    seasonal_periods=12
)

model_fit = model.fit()
predictions = model_fit.forecast(12)

print("\n2017 Predictions:")
print(predictions)

mae = mean_absolute_error(test["Sales"], predictions)

print("\nMean Absolute Error:")
print(mae)

mape = mean_absolute_percentage_error(test["Sales"], predictions) * 100
print("\nMean Absolute Percentage Error:")
print(mape)

plt.figure(figsize=(10, 5))

plt.plot(test["Order Date"].astype(str), test["Sales"], marker="o", label="Actual Sales")
plt.plot(test["Order Date"].astype(str), predictions, marker="o", label="Predicted Sales")

plt.title("Actual vs Predicted Monthly Sales - 2017")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig("outputs/actual_vs_predicted_sales.png")
plt.show()

final_model = ExponentialSmoothing(
    monthly_sales["Sales"],
    trend="add",
    seasonal="add",
    seasonal_periods=12
)

final_model_fit = final_model.fit()
future_forecast = final_model_fit.forecast(12)

print("\nNext 12 Months Sales Forecast:")
print(future_forecast)

future_dates = pd.period_range(
    start="2018-01",
    periods=12,
    freq="M"
)

forecast_df = pd.DataFrame({
    "Order Date": future_dates,
    "Forecasted Sales": future_forecast.values
})

print("\n2018 Sales Forecast:")
print(forecast_df)

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales["Order Date"].astype(str),
    monthly_sales["Sales"],
    label="Historical Sales"
)

plt.plot(
    forecast_df["Order Date"].astype(str),
    forecast_df["Forecasted Sales"],
    label="Forecasted Sales"
)

plt.title("Monthly Sales Forecast")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig("outputs/monthly_sales_forecast.png")
plt.show()

forecast_df.to_csv("outputs/2018_sales_forecast.csv", index=False)