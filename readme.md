# İş Yönetim Sistemi

Bu proje, bir iş yönetim sistemi için Python uygulamasıdır. Kullanıcılar, sistemde işlemler gerçekleştirebilir, işlemlerini takip edebilir ve raporlar alabilirler. 

## Kullanım

1. `main.py` dosyasını çalıştırarak programı başlatın.

2. Program başladığında, aşağıdaki seçeneklerden birini seçin:

   - **Giriş Yap**: Mevcut bir kullanıcı adı ve şifre ile giriş yapın.
   - **Yeni Kullanıcı Başvurusu**: Yeni bir kullanıcı başvurusu yapın.
   - **Çıkış**: Programı kapatın.

3. Yönetici veya çalışan olarak giriş yaptıktan sonra, menüler arasında gezinin ve işlemlerinizi gerçekleştirin.

## Dosyalar ve Sınıflar

- **main.py**: Programı başlatır ve kullanıcı girişini yönetir.
- **veritabani.py**: SQLite veritabanı işlemlerini gerçekleştiren `Veritabani` sınıfını içerir.
- **kullanici_islemleri.py**: İşlemleri yöneten `Islemler` sınıfını içerir.
- **menu.py**: Kullanıcıları temsil eden sınıfları içerir: `Kullanici`, `Admin`, ve `Calisan`.

## Sınıf Tanımları

- **Kullanici**: Temel kullanıcı sınıfıdır. Tüm kullanıcılar bu sınıftan türetilir.
- **Admin**: Yönetici kullanıcılar için türetilmiş sınıftır. Yöneticiye özgü işlemleri gerçekleştirir.
- **Calisan**: Çalışan kullanıcılar için türetilmiş sınıftır. Çalışana özgü işlemleri gerçekleştirir.
- **Veritabani**: SQLite veritabanı işlemlerini yöneten sınıftır.
- **Islemler**: Kullanıcı işlemlerini yöneten sınıftır. Kullanıcıların işlemlerini gerçekleştirir ve işlem kayıtlarını tutar.

## Gereksinimler

- Python 3.x
- pandas paketi ( **pip install pandas** )

Projeyi çalıştırmak için, pandas paketinin yüklü olması gerekmektedir. Pandas paketini yüklemek için terminal veya komut istemcisinde aşağıdaki komutu çalıştırabilirsiniz:


## Katkılar

Her türlü katkı ve geri bildirimleriniz değerlidir. Projeyle ilgili herhangi bir sorun veya öneriniz varsa lütfen bir issue (sorun) açın veya bir pull request (çekme isteği) gönderin.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını okuyun.
