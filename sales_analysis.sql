CREATE TABLE sales(
    Date DATE,
    Product VARCHAR(50),
    Category VARCHAR(50),
    Quantity INT,
    Price INT,
    Region VARCHAR(50)
);

-- Total Sales
SELECT SUM(Quantity * Price) AS TotalSales
FROM sales;

-- Top Selling Products
SELECT Product,
       SUM(Quantity * Price) AS Revenue
FROM sales
GROUP BY Product
ORDER BY Revenue DESC;

-- Monthly Sales
SELECT MONTH(Date) AS Month,
       SUM(Quantity * Price) AS Revenue
FROM sales
GROUP BY MONTH(Date)
ORDER BY Month;

-- Region Wise Sales
SELECT Region,
       SUM(Quantity * Price) AS Revenue
FROM sales
GROUP BY Region;