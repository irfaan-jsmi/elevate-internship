SELECT * FROM ecommerce_sales_data LIMIT 10;
SELECT COUNT(*) AS Total_Records
FROM ecommerce_sales_data;
SELECT SUM(Sales) AS Total_Sales
FROM ecommerce_sales_data;
SELECT AVG(Sales) AS Average_Sales
FROM ecommerce_sales_data;
SELECT AVG(Profit) AS Average_Profit
FROM ecommerce_sales_data;
SELECT Category,
       SUM(Sales) AS Total_Sales
FROM ecommerce_sales_data
GROUP BY Category;
SELECT Region,
       SUM(Profit) AS Total_Profit
FROM ecommerce_sales_data
GROUP BY Region;
SELECT "Product Name",
       SUM(Sales) AS Total_Sales
FROM ecommerce_sales_data
GROUP BY "Product Name"
ORDER BY Total_Sales DESC
LIMIT 5;
SELECT *
FROM ecommerce_sales_data
ORDER BY Profit DESC
LIMIT 10;