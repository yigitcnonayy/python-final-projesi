from veritabani import Veritabani  # Veritabani sınıfını içe aktar
from menu import Admin, Calisan  # Admin ve Calisan sınıflarını içe aktar
from kullanici_islemleri import Islemler  # Islemler sınıfını içe aktar



"""             
# Bu kodun en sonuna veritabanı isminde değişken tanımlayıp Veritabanı class'ını atıyoruz
# Sonrasında işlemler class'ının içine yolluyoruz
# böylelikle kod başladığında işlemler class'ına veritabanı gönderilmiş oluyor
# self.veritabani diyerek değişkeni kullanmış oluyoruz
"""



def giris(veritabani, islem_modulu):
    while True:
        # Giriş ekranı
        print("\nHoşgeldiniz! Lütfen giriş yapın veya kayıt olun.")
        print("1. Giriş Yap")
        print("2. Kayıt Ol (Çalışan)")
        print("3. Çıkış")
        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            kullanici_adi = input("Kullanıcı Adı: ")
            sifre = input("Şifre: ")
            kullanici = veritabani.kullanici_getir(kullanici_adi)  # Veritabanından kullanıcıyı getir
            if kullanici and kullanici[2] == sifre:  # Kullanıcı var mı ve şifre doğru mu kontrol et
                if kullanici[4] == 1:
                    if kullanici[3] == "admin":
                        Admin(kullanici_adi, sifre).menu(islem_modulu)
                    elif kullanici[3] == "calisan":
                        Calisan(kullanici_adi, sifre).menu(islem_modulu)
                else:
                    print("Hesabınız henüz onaylanmamış.")
            else:
                print("Kullanıcı adı veya şifre hatalı.")
        elif secim == "2":
            islem_modulu.kullanici_basvuru()  # Kullanıcı başvuru işlemini başlat
        elif secim == "3":
            print("Çıkış yapılıyor.")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    veritabani = Veritabani()  # Veritabanı nesnesini oluştur
    islem_modulu = Islemler(veritabani)  # Islemler modülünü oluştur ve veritabanını geç


 # Sabit admin kullanıcı
    try:
        veritabani.kullanici_ekle("admin", "admin123", "admin")
    except ValueError:
        pass  # Admin zaten ekli
    
    giris(veritabani, islem_modulu)  # Giriş fonksiyonunu başlat
