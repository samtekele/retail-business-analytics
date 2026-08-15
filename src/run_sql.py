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

connection.close()

