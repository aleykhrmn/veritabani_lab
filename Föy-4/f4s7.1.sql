CREATE TABLE Kitaplar (
    kitap_id INT IDENTITY(1,1) PRIMARY KEY,
    baslik VARCHAR(255) NOT NULL,
    yazar VARCHAR(255) NOT NULL,
    yayinevi VARCHAR(255),
    yayin_tarihi DATE,
    sayfa_sayisi INT
);
