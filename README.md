# Retail Business Analytics

Python • SQL • Pandas • Matplotlib • SQLite

## Project Overview

Analyzed 9,994 retail transactions to identify sales trends, profitability drivers, regional performance, and the impact of discounts on business profitability.

This project uses Python, Pandas, SQL, and data visualization to transform raw retail data into actionable business insights.

## Business Questions

This project investigates several questions:

- Which product categories generate the most sales?
- Which categories generate the most profit?
- Which regions are the most profitable?
- How does discounting affect profit margins?
- Which product sub-categories are losing money?
- Which sub-categories generate the highest profits?

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- SQL
- SQLite
- SQLAlchemy
- Git / GitHub

## Key Findings

### Overall Performance

- Total sales: $2.30M
- Total profit: $286.4K
- Overall profit margin: 12.47%
- Total quantity sold: 37,873

### Category Performance

Technology generated the highest sales ($836.2K) and highest profit ($145.5K).

Furniture generated $742.0K in sales but only $18.5K in profit, resulting in a significantly lower profit margin of 2.49%.

### Regional Performance

The West region generated the highest total profit at approximately $108.4K, followed by the East at $91.5K.

### Discount Analysis

Higher discount levels were associated with significantly lower profitability. Discount levels of 30% or higher consistently resulted in negative profit margins in the analyzed dataset.

### Sub-Category Performance

Tables were the largest source of sub-category losses, generating approximately $17.7K in negative profit. Bookcases were the second-largest loss-producing sub-category at approximately $3.5K.

## Visualizations

### Sales by Category

![Sales by Category](outputs/sales_by_category.png)

### Profit by Category

![Profit by Category](outputs/profit_by_category.png)

### Profit by Region

![Profit by Region](outputs/profit_by_region.png)

### Discount vs. Profitability

![Discount vs. Profitability](outputs/discount_profitability.png)

### Least Profitable Sub-Categories

![Least Profitable Sub-Categories](outputs/worst_subcategories.png)

## Project Structure

```text
retail-business-analytics/
│
├── data/
│   └── raw/
│       └── sample_-_superstore.xls
│
├── outputs/
│   ├── sales_by_category.png
│   ├── profit_by_category.png
│   ├── profit_by_region.png
│   ├── discount_profitability.png
│   └── worst_subcategories.png
│
├── src/
│   ├── explore_data.py
│   ├── run_sql.py
│   └── visualize_data.py
│
├── .gitignore
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/samtekele/retail-business-analytics.git
cd retail-business-analytics
```

### 2. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn openpyxl sqlalchemy xlrd
```

### 3. Run the data analysis

```bash
python src/explore_data.py
```

### 4. Generate visualizations

```bash
python src/visualize_data.py
```

### 5. Run the SQL analysis

```bash
python src/run_sql.py
```

## Future Improvements

- Build an interactive Power BI dashboard
- Add time-series sales and profit analysis
- Add customer segmentation analysis
- Analyze shipping performance
- Add automated reporting
- Expand the SQL analysis with more advanced queries