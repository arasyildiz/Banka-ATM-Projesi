from hesaplar import BankaHesabi
import veritabani

print("--- TEST BAŞLIYOR ---\n")
veritabani.tablolari_olustur()

kullanici_adi = "TestKullanicisi"

# 1. Veritabanından çekmeye çalış
gelen_veri = veritabani.hesap_bilgisini_getir(kullanici_adi)

if gelen_veri is not None:
    print("Kullanıcı veritabanından yüklendi!")
    hesap = BankaHesabi(kullanici_adi, gelen_veri[2]) # DB'deki bakiye
else:
    print("Yeni kullanıcı oluşturuluyor...")
    hesap = BankaHesabi(kullanici_adi, 1000)
    veritabani.hesap_ekle(kullanici_adi, 1000)

# 2. ŞİMDİKİ BAKİYE
print(f"Açılış Bakiyesi: {hesap.bakiye_sorgula}")

# 3. HARCAMA YAP (Bu veritabanına işlenecek mi?)
hesap.para_cek(200) 
print("200 TL harcandı. Program kapatılıyor...")

hesap.bakiye_duzenle(3000)
print(hesap.bakiye_sorgula())

# Burada program bitiyor.
# TEKRAR ÇALIŞTIRDIĞINDA bakiyenin 800 olması lazım (Eskiden olsa 1000 kalırdı).