import sqlite3
import pandas as pd

connection = sqlite3.connect("data/retail.db")

query = """
SELECT "Sub-Category", SUM(Profit) AS Total_Profit
FROM orders
GROUP BY "Sub-Category"
ORDER BY Total_Profit DESC
LIMIT 5;
"""

results = pd.read_sql_query(query, connection)

print(results)




print("\nTRANSACTION PROFIT STATUS:")

query = """
SELECT
    Sales,
    Profit,
    CASE
        WHEN Profit > 0 THEN 'Profitable'
        WHEN Profit < 0 THEN 'Loss'
        ELSE 'Break Even'
    END AS Profit_Status
From orders
LIMIT 10;
"""

result = pd.read_sql(query, connection)

print(result)


print("\nPROFIT STATUS SUMMARY:")
query = """
SELECT
    CASE
        WHEN Profit > 0 THEN 'Profitable'
        WHEN Profit < 0 THEN 'Loss'
        ElSE 'Break Even'
    END AS Profit_Status,
    Count(*) AS Transaction_Count,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM orders
GROUP BY Profit_Status;
"""

result = pd.read_sql_query(query, connection)
print(result)


print("\nHIGH PROFIT SUB-CATEGORIES:")
query = """
SELECT
    "Sub-Category",
    SUM(Profit) AS Total_Profit
FROM orders
GROUP BY "Sub-Category"
HAVING SUM(Profit) > 20000
ORDER BY Total_Profit DESC;
"""

result = pd.read_sql_query(query, connection)
print(result)

print("\nTRANSACTIONS ABOVE AVERAGE PROFIT:")

query = """
SELECT
    "Order ID",
    Sales,
    Profit
FROM orders
WHERE Profit > (
    SELECT AVG(Profit)
    FROM orders
)
ORDER BY Profit DESC
LIMIT 10;
"""

result = pd.read_sql_query(query, connection)
print(result)

print("\nCATEGORY PERFORMANCE CTE:")

query = """
WITH Category_Performance AS (
    SELECT
        Category,
        SUM(Sales) AS Total_Sales,
        SUM(Profit) AS Total_Profit
    FROM orders
    GROUP BY Category
)
SELECT *
FROM Category_Performance
ORDER BY Total_Profit DESC;
"""

result = pd.read_sql_query(query, connection)
print(result)

print("\nHIGH PROFIT CATEGORIES USING CTE:")
query = """
WITH Category_Performance AS (
    SELECT
        Category,
        SUM(Sales) AS Total_Sales,
        SUM(Profit) AS Total_Profit
    FROM orders
    GROUP BY Category
)

SELECT *
FROM Category_Performance
WHERE Total_Profit > 100000
ORDER BY Total_Profit DESC;
"""

result = pd.read_sql_query(query, connection)
print(result)


print("\nSEGMENT PROFITABILITY ANALYSIS:")
query = """
WITH Segment_Performance AS (
    SELECT
        Segment,
        SUM(Sales) AS Total_Sales,
        SUM(Profit) AS Total_Profit
    FROM orders
    GROUP BY Segment
)

SELECT
    Segment,
    Total_Sales,
    Total_Profit,
    Total_Profit / Total_Sales AS Profit_Margin
FROM Segment_Performance
WHERE Total_Profit > 50000
ORDER BY Profit_Margin DESC;
"""

result = pd.read_sql_query(query, connection)
print(result)

connection.close()