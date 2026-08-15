import pandas as pd
import sqlite3

#Load the excel dataset
file_path = "data/raw/sample_-_superstore.xls"

df = pd.read_excel(file_path)

#Connect to SQLite database
connection = sqlite3.connect("data/retail.db")

#Store the dataframe as a table called orders
df.to_sql(
    "orders",
    connection,
    if_exists="replace",
    index=False
)

#Confirm that the databse was created
print("Database created successfully!")
print(f"Rows added to orders table: {len(df)}")

#Close connection
connection.close()

