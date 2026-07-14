SELECT
    CAST(substr("Order Date", 7, 4) AS INTEGER) AS Year,
    CAST(substr("Order Date", 1, instr("Order Date", '/') - 1) AS INTEGER) AS Month,
    ROUND(SUM(Sales), 2) AS Total_Revenue,
    COUNT(DISTINCT "Order ID") AS Order_Volume
FROM "Sample - Superstore"
GROUP BY
    CAST(substr("Order Date", 7, 4) AS INTEGER),
    CAST(substr("Order Date", 1, instr("Order Date", '/') - 1) AS INTEGER)
ORDER BY
    Year,
    Month;