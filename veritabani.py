import sqlite3
import pandas as pd

class Veritabani:
    def __init__(self, db_adi="is_yonetim_sistemi.db"):
        self.conn = sqlite3.connect(db_adi)
        self.cursor = self.conn.cursor() # cursor veritabanı sorgularını yürütür ve sonuç işler
        self.tablo_olustur()

    def tablo_olustur(self):
        # Kullanıcılar tablosunu oluşturur
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS kullanicilar (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            kullanici_adi TEXT UNIQUE NOT NULL,
                            sifre TEXT NOT NULL,
                            kullanici_tipi TEXT NOT NULL,
                            onay_durumu INTEGER DEFAULT 0)''')
        
        # İşlem kaydı tablosunu oluşturur
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS islem_kaydi (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            kullanici_adi TEXT NOT NULL,
                            islem TEXT NOT NULL,
                            tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                            FOREIGN KEY(kullanici_adi) REFERENCES kullanicilar(kullanici_adi))''')
        self.conn.commit()

    def kullanici_ekle(self, kullanici_adi, sifre, kullanici_tipi):
        try:
            if kullanici_tipi == "admin":
                # Yönetici kullanıcı ekler
                self.cursor.execute("INSERT INTO kullanicilar (kullanici_adi, sifre, kullanici_tipi, onay_durumu) VALUES (?, ?, ?, 1)",
                                    (kullanici_adi, sifre, kullanici_tipi))
            else:
                # Çalışan kullanıcı ekler
                self.cursor.execute("INSERT INTO kullanicilar (kullanici_adi, sifre, kullanici_tipi) VALUES (?, ?, ?)",
                                    (kullanici_adi, sifre, kullanici_tipi))
            self.conn.commit()
        except sqlite3.IntegrityError: # veritabanında bütünlükten biri ihlal edildiğinde kullanılır
            raise ValueError("Kullanıcı zaten mevcut.") # raise ekrana bilinçli hata yazdırmaya yarar
    
    def kullanici_basvuru(self, kullanici_adi, sifre):
        try:
            # Kullanıcı başvurusu yapar
            self.cursor.execute("INSERT INTO kullanicilar (kullanici_adi, sifre, kullanici_tipi, onay_durumu) VALUES (?, ?, ?, 0)",
                                (kullanici_adi, sifre, "calisan"))
            self.conn.commit()
        except sqlite3.IntegrityError:  # veritabanında bütünlükten biri ihlal edildiğinde kullanılır
            raise ValueError("Kullanıcı zaten mevcut.") # raise ekrana bilinçli hata yazdırmaya yarar
    
    def kullanici_onayla(self, kullanici_adi):
        # Kullanıcıyı onaylar
        self.cursor.execute("UPDATE kullanicilar SET onay_durumu = 1 WHERE kullanici_adi = ?", (kullanici_adi,))
        self.conn.commit()

    def onay_bekleyenler(self):
        # Onay bekleyen kullanıcıları getirir
        self.cursor.execute("SELECT kullanici_adi FROM kullanicilar WHERE onay_durumu = 0")
        return [row[0] for row in self.cursor.fetchall()]

    def kullanici_sil(self, kullanici_adi):
        # Kullanıcıyı siler
        self.cursor.execute("DELETE FROM kullanicilar WHERE kullanici_adi = ?", (kullanici_adi,))
        self.conn.commit()
    
    def kullanici_listele(self):
        # Onaylı kullanıcıları listeler
        self.cursor.execute("SELECT kullanici_adi FROM kullanicilar WHERE onay_durumu = 1")
        return [row[0] for row in self.cursor.fetchall()]
    
    def kullanici_islem_goruntule(self, kullanici_adi):
        # Belirli bir kullanıcının işlem kaydını getirir
        self.cursor.execute("SELECT * FROM islem_kaydi WHERE kullanici_adi = ?", (kullanici_adi,))
        return self.cursor.fetchall() # veritabanı sorguları yürütür ve sonuçları alır fetchall ile tüm sorguları liste şeklinde döndürür
    
    def islem_kaydi_ekle(self, kullanici_adi, islem):
        # İşlem kaydı ekler
        self.cursor.execute("INSERT INTO islem_kaydi (kullanici_adi, islem) VALUES (?, ?)", (kullanici_adi, islem))
        self.conn.commit()
    
    def islem_kaydi_excel(self, dosya_adi="islem_kaydi.xlsx"):
        # İşlem kayıtlarını Excel dosyasına aktarır
        self.cursor.execute("SELECT * FROM islem_kaydi")
        rows = self.cursor.fetchall() # veritabanı satırlarındaki sorguları yürütür ve sonuçları alır fetchall ile tüm sorguları liste şeklinde döndürür
        df = pd.DataFrame(rows, columns=["ID", "Kullanıcı", "İşlem", "Tarih"])
        if not dosya_adi.endswith('.xlsx'):
            dosya_adi += '.xlsx'
        df.to_excel(dosya_adi, index=False)
    
    def kullanici_getir(self, kullanici_adi):
        # Belirli bir kullanıcıyı getirir
        self.cursor.execute("SELECT * FROM kullanicilar WHERE kullanici_adi = ?", (kullanici_adi,))
        return self.cursor.fetchone()   # veritabanı sorguları yürütür ve sonuçları alır fetchall ile tüm sorguları liste şeklinde döndürür
