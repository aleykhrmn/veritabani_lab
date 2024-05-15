SELECT c.name AS Customer_Name, p.Description AS Product_Name
FROM Sales_Order so
INNER JOIN client_master c ON so.Client_no = c.client_no
INNER JOIN Sales_Order_Details sod ON so.S_order_no = sod.S_order_no
INNER JOIN Product_master p ON sod.Product_no = p.Product_no
WHERE DATEDIFF(DAY, so.S_order_date, GETDATE()) > 10;