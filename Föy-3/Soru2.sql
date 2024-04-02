-- Yazýlým birimi ekleme
INSERT INTO birimler (birim_id, birim_ad)
VALUES (1, 'Yazýlým');

-- Donaným birimi ekleme
INSERT INTO birimler (birim_id, birim_ad)
VALUES (2, 'Donaným');

-- Güvenlik birimi ekleme
INSERT INTO birimler (birim_id, birim_ad)
VALUES (3, 'Güvenlik');

INSERT INTO calisanlar (calisan_id, ad, soyad, maas, katilmaTarihi, calisan_birim_id) VALUES 
(1, 'Ýsmail', 'Ýþeri', 100000, '2014-02-20', 1),
(2, 'Hami', 'Satýlmýþ', 80000, '2014-06-11', 1),
(3, 'Durmuþ', 'Þahin', 300000, '2023-02-20', 2),
(4, 'Kaðan', 'Yazar', 500000, '2014-02-20', 3),
(5, 'Meryem', 'Soysaldý', 500000, '2014-06-11', 3),
(6, 'Duygu', 'Akþehir', 200000, '2014-06-11', 2), 
(7, 'Kübra', 'Seyhan', 75000, '2014-01-20', 1),
(8, 'Gülcan', 'Yýldýz', 90000, '2014-04-11', 3);

INSERT INTO ikramiye ikramiye_calisan_id, ikramiye_ucret, ikramiye_tarih) VALUES 
(1, 5000, '2016-02-20'),
(2, 3000, '2016-06-11'),
(3, 4000, '2016-02-20'),
(1, 4500, '2016-02-20'),
(2, 3500, '2016-06-11');


INSERT INTO unvan (unvan_calisan_id, unvan_calisan, unvan_tarih) VALUES 
(1, 'Yönetici', '2016-02-20'),
(2, 'Personel', '2016-06-11'),
(8, 'Personel', '2016-06-11'),
(5, 'Müdür', '2016-06-11'),
(4, 'Yönetici Yardýmcýsý', '2016-06-11'),
(7, 'Personel', '2016-06-11'),
(6, 'Takým Lideri', '2016-06-11'),
(3, 'Takým Lideri', '2016-06-11');
