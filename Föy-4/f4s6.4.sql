CREATE TABLE Proje (
    proje_id INT PRIMARY KEY,
    proje_ad� VARCHAR(100),
    teslim_tarihi DATE,
    b�t�e DECIMAL(10, 2) DEFAULT 0.00, -- Default k�s�tlay�c�
    sorumlu_personel VARCHAR(50)
);