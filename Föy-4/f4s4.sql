SELECT c.customer_name, p.description
FROM sales_order s
JOIN customer_master c ON s.customer_id = c.customer_id
JOIN product_master p ON s.product_id = p.product_id
WHERE s.order_date < (CURRENT_DATE - INTERVAL '10' DAY);