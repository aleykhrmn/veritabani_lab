CREATE TABLE birimler (
    birim_id INT PRIMARY KEY,
    birim_ad CHAR(25) NULL
);

-- Calisanlar tablosu
CREATE TABLE calisanlar (
    calisan_id INT PRIMARY KEY,
    ad CHAR(25) NULL,
    soyad CHAR(25) NULL,
    maas INT NULL,
    katilmaTarihi DATETIME NULL,
    calisan_birim_id INT NULL,
    FOREIGN KEY (calisan_birim_id) REFERENCES birimler(birim_id)
);

-- Ikramiye tablosu
CREATE TABLE ikramiye (
    ikramiye_id INT PRIMARY KEY IDENTITY,
    ikramiye_calisan_id INT NULL,
    ikramiye_ucret INT NULL,
    ikramiye_tarih DATETIME NULL,
    FOREIGN KEY (ikramiye_calisan_id) REFERENCES calisanlar(calisan_id)
);

-- Unvan tablosu
CREATE TABLE unvan (
    unvan_id INT PRIMARY KEY IDENTITY,
    unvan_calisan_id INT NULL,
    unvan_calisan CHAR(25) NULL,
    unvan_tarih DATETIME NULL,
    FOREIGN KEY (unvan_calisan_id) REFERENCES calisanlar(calisan_id)
);



