ALTER TABLE Proje
ADD CONSTRAINT CK_TeslimTarihi CHECK (teslim_tarihi >= '2025-01-01');