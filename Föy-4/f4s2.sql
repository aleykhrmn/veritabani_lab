CREATE VIEW product_view AS
SELECT Product_no AS "pro_no", 
Description AS "desc", 
Profit_percent AS "profit", 
Unit_measure AS "Unit_measure", 
Qty_on_hand AS "qty"
FROM product_master;