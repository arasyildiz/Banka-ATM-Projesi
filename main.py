class BankaHesabi:
    def __init__(self, sahip_ismi, baslangic_parasi):
        self.isim = sahip_ismi
        self.bakiye = baslangic_parasi
        self.hareketler = []
        print(f'Sistem : {self.isim} hesabi basariyla acildi')
        
    def para_yatir(self, miktar):
        self.bakiye += miktar
        self.hareketler.append(f"YATIRILAN : +{miktar} TL")
        print(f'Sistem : {self.isim} hesabina {miktar} para yatirildi')
        
    def para_cek(self, miktar):
        if miktar > self.bakiye:
            self.hareketler.append(f"REDDEDİLEN CEKİM : -{miktar} TL (Yetersiz Bakiye)")
            print(f"HATA : {self.isim} hesanbinda yeterli miktarda para bulunmamaktadir")
        else :    
            self.bakiye -= miktar
            self.hareketler.append(f"CEKİLEN : -{miktar} TL")
            print(f'Sistem : {self.isim} hesabindan {miktar} para cekildi')
    
    
    def bilgi_ver(self):
        print(f"--- HESAP BİLGİSİ ---\nSayın {self.isim}, bakiyeniz: {self.bakiye} TL\n---------------------")

        for islem in self.hareketler:
            print(f' -> {islem}')
        print("--------------------\n")
        
        
    
hesap1 = BankaHesabi("Aras", 1000)
hesap1.para_yatir(500)
hesap1.para_cek(1300)
hesap1.para_cek(6000)
hesap1.bilgi_ver()