SELECT c.ad, c.soyad, b.birim_ad AS birim, u.unvan_calisan AS unvan, i.ikramiye_ucret
FROM calisanlar c
INNER JOIN ikramiye i ON c.calisan_id = i.ikramiye_calisan_id
INNER JOIN birimler b ON c.calisan_birim_id = b.birim_id
INNER JOIN unvan u ON c.calisan_id = u.unvan_calisan_id;