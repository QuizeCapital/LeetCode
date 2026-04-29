/* Write your T-SQL query statement below */
SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT DISTINCT od.sales_id
    FROM Orders od
    JOIN Company cp ON od.com_id = cp.com_id
    WHERE cp.name = 'RED'
);
-- Anothrt working example 


-- SELECT sp.name
-- FROM SalesPerson sp
-- LEFT JOIN Orders od ON sp.sales_id = od.sales_id
-- LEFT JOIN Company cp ON od.com_id = cp.com_id
-- GROUP BY sp.sales_id, sp.name
-- HAVING SUM(CASE WHEN cp.name = 'RED' THEN 1 ELSE 0 END) = 0;



