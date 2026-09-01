-- Retail Sales & Customer Analytics
-- Business-focused SQL queries for portfolio/interview practice

-- 1. Overall KPIs
SELECT COUNT(DISTINCT Order_ID) AS orders,
       COUNT(DISTINCT Customer_ID) AS customers,
       SUM(Quantity) AS units_sold,
       ROUND(SUM(Sales),2) AS total_sales,
       ROUND(SUM(Profit),2) AS total_profit
FROM retail_sales;

-- 2. Sales and profit by category
SELECT Category,
       ROUND(SUM(Sales),2) AS sales,
       ROUND(SUM(Profit),2) AS profit,
       SUM(Quantity) AS units
FROM retail_sales
GROUP BY Category
ORDER BY sales DESC;

-- 3. Sales by city
SELECT City, ROUND(SUM(Sales),2) AS sales
FROM retail_sales
GROUP BY City
ORDER BY sales DESC;

-- 4. Top products by revenue
SELECT Product, ROUND(SUM(Sales),2) AS sales,
       ROUND(SUM(Profit),2) AS profit
FROM retail_sales
GROUP BY Product
ORDER BY sales DESC
LIMIT 10;

-- 5. Customer value
SELECT Customer_ID,
       COUNT(DISTINCT Order_ID) AS orders,
       ROUND(SUM(Sales),2) AS sales,
       ROUND(SUM(Profit),2) AS profit
FROM retail_sales
GROUP BY Customer_ID
ORDER BY sales DESC;

-- 6. Discount vs profitability
SELECT Discount,
       ROUND(SUM(Sales),2) AS sales,
       ROUND(SUM(Profit),2) AS profit,
       ROUND(AVG(Profit),2) AS avg_profit
FROM retail_sales
GROUP BY Discount
ORDER BY Discount;

-- 7. Monthly trend
SELECT EXTRACT(MONTH FROM Order_Date) AS month,
       ROUND(SUM(Sales),2) AS sales,
       ROUND(SUM(Profit),2) AS profit
FROM retail_sales
GROUP BY EXTRACT(MONTH FROM Order_Date)
ORDER BY month;

-- 8. Identify low-profit orders
SELECT Order_ID, Category, Product, Sales, Profit, Discount
FROM retail_sales
WHERE Profit < 500
ORDER BY Profit ASC;
