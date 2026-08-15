-- View all columns from the orders table
SELECT *
FROM orders
LIMIT 5;


-- View all orders from Central region
SELECT *
FROM orders
WHERE Region = 'Central';


-- View the 10 most profitable orders
SELECT "Product Name", Sales, Profit
FROM orders
ORDER BY Profit DESC
LIMIT 10;

-- View total sales from each category
SELECT Category, SUM(Sales)
FROM orders
GROUP BY Category;

-- View Sales and Profit by category
SELECT Category,
        SUM(Sales) AS Total_Sales,
        SUM(Profit) AS Total_Profit,
        SUM(Profit) / SUM(Sales) AS Profit_Margin
FROM orders
GROUP BY Category;

-- View region and total profit sorted by profitble region first
SELECT Region, SUM(Profit) AS Total_Profit
FROM orders
GROUP BY Region
ORDER BY Total_Profit DESC;

-- View top 5 sub-categories by total profit, highest first
SELECT "Sub-Category", SUM(Profit) AS Total_Profit
FROM orders
GROUP BY "Sub-Category"
ORDER BY Total_Profit DESC
LIMIT 5;