CREATE VIEW salesman_view AS
SELECT * 
FROM salesman_master
WHERE tgt_to_get > 200;