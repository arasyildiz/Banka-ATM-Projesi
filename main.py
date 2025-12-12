from hesaplar import BankaHesabi, VadeliHesap

print("--- BANKA SİSTEMİ BAŞLATILIYOR ---\n")

aras_hesap = BankaHesabi("Aras Normal", 500)
aras_hesap.para_yatir(100)

vadeli_hesap = VadeliHesap("Aras Vadeli", 2000, 15)
vadeli_hesap.faiz_islet()

aras_hesap.bilgi_ver()
vadeli_hesap.bilgi_ver()