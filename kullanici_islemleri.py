import pandas as pd

class Islemler:
    def __init__(self, veritabani):
        self.veritabani = veritabani  # Veritabanı bağlantısını kur

    def kullanici_basvuru(self):
        kullanici_adi = input("Yeni kullanıcı adı: ")
        sifre = input("Yeni şifre: ")
        try:
            self.veritabani.kullanici_basvuru(kullanici_adi, sifre)             # Kullanıcı başvurusunu veritabanına ilet
            print("Kullanıcı başvurusu alındı, admin onayı bekleniyor.")
        except ValueError as e:  # Hatayı denetleme durumunda "e" değişkenine değer ata ve hata mesajını yazdır
            print(f"Hata: {e}")

    def kullanici_onayla(self):
        onay_bekleyenler = self.veritabani.onay_bekleyenler()         # Onay bekleyen kullanıcıları al
        if not onay_bekleyenler:
            print("Onay bekleyen kullanıcı yok.")
            return
        print("Onay bekleyen kullanıcılar:")        # Onay bekleyen kullanıcıları listele
        for kullanici_adi in onay_bekleyenler:
            print(kullanici_adi)
        kullanici_adi = input("Onaylanacak kullanıcı adı: ")
        self.veritabani.kullanici_onayla(kullanici_adi)
        print(f"{kullanici_adi} onaylandı.")
        self.islem_kaydi_ekle(kullanici_adi, "Kullanıcı onaylandı")

    def onay_bekleyenler(self):
        onay_bekleyenler = self.veritabani.onay_bekleyenler()  # Onay bekleyen kullanıcıları al
        if not onay_bekleyenler:
            print("Onay bekleyen kullanıcı yok.") # Onay bekleyen kullanıcı yoksa mesaj göster
        else:
            print("Onay bekleyen kullanıcılar:")
            for kullanici_adi in onay_bekleyenler:
                print(kullanici_adi)

    def kullanici_sil(self):
        kullanici_adi = input("Silinecek kullanıcı adı: ")
        self.veritabani.kullanici_sil(kullanici_adi)
        print(f"{kullanici_adi} silindi.")
        self.islem_kaydi_ekle(kullanici_adi, "Kullanıcı silindi")        # İşlem kaydı ekle

    def kullanici_listele(self):
        kullanicilar = self.veritabani.kullanici_listele()  # Onaylı kullanıcıları al
        if not kullanicilar:            # Onaylı kullanıcı yoksa mesaj göster
            print("Onaylı kullanıcı yok.")
        else:
            # Onaylı kullanıcıları listele
            print("Onaylı kullanıcılar:")
            for kullanici_adi in kullanicilar:
                print(kullanici_adi)

    def kullanici_islem_goruntule(self, kullanici_adi):
        islemler = self.veritabani.kullanici_islem_goruntule(kullanici_adi)        # Belirtilen kullanıcının işlemlerini al
        if not islemler:
            # İşlem kaydı yoksa mesaj göster
            print(f"{kullanici_adi} kullanıcısının işlem kaydı yok.")
        else:
            # Kullanıcının işlem kayıtlarını listele
            print(f"{kullanici_adi} kullanıcısının işlem kayıtları:")
            for islem in islemler:
                print(islem)

    def islem_kaydi_ekle(self, kullanici_adi, islem):
        # İşlem kaydını veritabanına ekle
        self.veritabani.islem_kaydi_ekle(kullanici_adi, islem)

    def islem_kaydi_excel(self):
        # Excel dosyası adını al
        dosya_adi = input("Excel dosyası adı: ")
        # İşlem kayıtlarını Excel'e aktar
        self.veritabani.islem_kaydi_excel(dosya_adi)
        print(f"İşlem kayıtları {dosya_adi}.xlsx dosyasına aktarıldı.")

    def kendi_bilgilerini_goruntule(self, kullanici_adi):
        # Kullanıcı bilgilerini al
        kullanici = self.veritabani.kullanici_getir(kullanici_adi)
        # Kullanıcı bilgilerini göster
        print(f"Kullanıcı Adı: {kullanici[1]}")
        print(f"Kullanıcı Tipi: {kullanici[3]}")

    def islem_yap(self, kullanici_adi):
        # Yapılacak işlemi al
        islem = input("Yapılacak işlem: ")
        # İşlem kaydını ekle
        self.islem_kaydi_ekle(kullanici_adi, islem)
        print("İşlem kaydedildi.")

    def islem_gecmisi_goruntule(self, kullanici_adi):
        # Belirtilen kullanıcının işlem geçmişini al
        islemler = self.veritabani.kullanici_islem_goruntule(kullanici_adi)
        if not islemler:
            # İşlem kaydı yoksa mesaj göster
            print("İşlem kaydı bulunamadı.")
        else:
            # Kullanıcının işlem kayıtlarını listele
            print("İşlem kayıtları:")
            for islem in islemler:
                print(islem)

    def rapor_al(self, kullanici_adi):
        # Belirtilen kullanıcının işlem kayıtlarını al
        islemler = self.veritabani.kullanici_islem_goruntule(kullanici_adi)
        if not islemler:
            # Rapor için işlem kaydı yoksa mesaj göster
            print("Rapor için işlem kaydı bulunamadı.")
        else:
            # Rapor dosyası adını al
            dosya_adi = input("Rapor dosyası adı: ")
            # İşlem kayıtlarını DataFrame'e dönüştür
            df = pd.DataFrame(islemler, columns=["ID", "Kullanıcı", "İşlem", "Tarih"])
            if not dosya_adi.endswith('.xlsx'):
                # Dosya adı .xlsx ile bitmiyorsa, uzantıyı ekle
                dosya_adi += '.xlsx'
            # DataFrame'i Excel dosyasına yaz
            df.to_excel(dosya_adi, index=False)
            print(f"Rapor {dosya_adi} dosyasına kaydedildi.")
