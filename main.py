class BankaHesabi:
    def __init__(self, sahip_ismi, baslangic_parasi):
        self.isim = sahip_ismi
        self.bakiye = baslangic_parasi
        print(f'Sistem : {self.isim} hesabi basariyla acildi')
        
    def para_yatir(self, miktar):
        self.bakiye += miktar
        print(f'Sistem : {self.isim} hesabina {miktar} para yatirildi')
        
    def para_cek(self, miktar):
        if miktar > self.bakiye:
            print(f"HATA : {self.isim} hesanbinda yeterli miktarda para bulunmamaktadir")
        else :    
            self.bakiye -= miktar
            print(f'Sistem : {self.isim} hesabindan {miktar} para cekildi')
    
    def bilgi_ver(self):
            print(f"--- HESAP BİLGİSİ ---\nSayın {self.isim}, bakiyeniz: {self.bakiye} TL\n---------------------")
    
    
hesap1 = BankaHesabi("Aras", 1000)
hesap1.para_yatir(500)
hesap1.para_cek(1300)
hesap1.bilgi_ver()
hesap1.para_cek(2000) # Bakalım bakiye yetecek mi?