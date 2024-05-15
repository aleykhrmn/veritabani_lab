CREATE TABLE Proje (
    proje_id INT PRIMARY KEY,
    proje_adý VARCHAR(100),
    teslim_tarihi DATE,
    bütçe DECIMAL(10, 2) DEFAULT 0.00, -- Default kýsýtlayýcý
    sorumlu_personel VARCHAR(50)
);