SELECT 
    unvan_calisan AS unvan,
    COUNT(*) AS calisan_sayisi
FROM 
    unvan
GROUP BY 
    unvan_calisan
HAVING 
    COUNT(*) > 1;
