WITH RankedEmployees AS (
    SELECT 
        c.ad, 
        c.soyad, 
        c.maas,
        b.birim_ad,
        u.unvan_calisan,
        ROW_NUMBER() OVER (PARTITION BY c.calisan_birim_id ORDER BY c.maas DESC) AS rank
    FROM 
        calisanlar c
    INNER JOIN 
        birimler b ON c.calisan_birim_id = b.birim_id
    INNER JOIN 
        unvan u ON c.calisan_id = u.unvan_calisan_id
)
SELECT 
    ad, 
    soyad, 
    maas,
    birim_ad AS birim,
    unvan_calisan AS unvan
FROM 
    RankedEmployees
WHERE 
    rank = 1;
