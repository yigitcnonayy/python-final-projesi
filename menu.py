class Kullanici:
    def __init__(self, kullanici_adi, sifre):
        # Kullanıcı adı ve şifre ile kullanıcıyı oluştur
        self.kullanici_adi = kullanici_adi
        self.sifre = sifre

class Admin(Kullanici):
    def __init__(self, kullanici_adi, sifre):
        # Admin kullanıcı oluştur
        super().__init__(kullanici_adi, sifre)

    def menu(self, islem_modulu): # Admin menüsü
        while True:
            print("\nAdmin Menüsü:")
            print("1. Onay Bekleyenleri Görüntüle")
            print("2. Kullanıcı Onayla")
            print("3. Kullanıcı Sil")
            print("4. Kullanıcı Listele")
            print("5. Kullanıcı İşlemlerini Görüntüle")
            print("6. İşlem Kayıtlarını Excel'e Aktar")
            print("7. Çıkış")
            secim = input("Seçiminizi yapın: ")

            if secim == "1":
                islem_modulu.onay_bekleyenler()
            elif secim == "2":
                islem_modulu.kullanici_onayla()
            elif secim == "3":
                islem_modulu.kullanici_sil()
            elif secim == "4":
                islem_modulu.kullanici_listele()
            elif secim == "5":
                kullanici_adi = input("İşlemleri görüntülenecek kullanıcı adı: ")
                islem_modulu.kullanici_islem_goruntule(kullanici_adi)
            elif secim == "6":
                islem_modulu.islem_kaydi_excel()
            elif secim == "7":
                break # menüyü durdurur
            else:
                print("Geçersiz seçim, tekrar deneyin.")

class Calisan(Kullanici):
    def __init__(self, kullanici_adi, sifre): # Çalışan kullanıcı oluştur

        super().__init__(kullanici_adi, sifre) #  üst sınıfın __init__ metodunu çağırır ve ona kullanici_adi ve sifre parametrelerini geçirir.

    def menu(self, islem_modulu):
        while True:
            # Çalışan menüsü
            print("\nÇalışan Menüsü:")
            print("1. Kendi Bilgilerini Görüntüle")
            print("2. İşlem Yap")
            print("3. İşlem Geçmişini Görüntüle")
            print("4. Rapor Al")
            print("5. Çıkış")
            secim = input("Seçiminizi yapın: ")

            if secim == "1":
                islem_modulu.kendi_bilgilerini_goruntule(self.kullanici_adi)
            elif secim == "2":
                islem_modulu.islem_yap(self.kullanici_adi)
            elif secim == "3":
                islem_modulu.islem_gecmisi_goruntule(self.kullanici_adi)
            elif secim == "4":
                islem_modulu.rapor_al(self.kullanici_adi)
            elif secim == "5":
                break # menüyü durdurur
            else:
                print("Geçersiz seçim, tekrar deneyin.")
