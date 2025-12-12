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
            return False
        else :    
            self.bakiye -= miktar
            self.hareketler.append(f"CEKİLEN : -{miktar} TL")
            print(f'Sistem : {self.isim} hesabindan {miktar} para cekildi')
            return True
        
    def bilgi_ver(self):
        print(f"--- HESAP BİLGİSİ ---\nSayın {self.isim}, bakiyeniz: {self.bakiye} TL\n---------------------")

        for islem in self.hareketler:
            print(f' -> {islem}')
        print("--------------------\n")
        
    def transfer_et(self, alici_hesap, miktar):
        if self.para_cek(miktar):
            alici_hesap.para_yatir(miktar)
            print(f'Sistem : {self.isim} hesabindan {alici_hesap.isim} hesabına {miktar} para gönderildi')
        else:
            print(f"HATA : {self.isim} hesanbinda yeterli miktarda para bulunmamaktadir")
            

class VadeliHesap(BankaHesabi):
    def __init__(self, sahip_ismi, baslangic_parasi, faiz_orani):
        super().__init__(sahip_ismi, baslangic_parasi)
        self.faiz_orani = faiz_orani


        
    def faiz_islet(self):
        gelen_faiz = (self.bakiye * self.faiz_orani / 100)   
        self.bakiye += gelen_faiz
        self.hareketler.append(f"FAİZ GELİRİ: +{gelen_faiz} TL (%{self.faiz_orani})")
        print(f"Sistem: Faiz işletildi. Kazanılan: {gelen_faiz} TL")
        
        
vadeli1 = VadeliHesap("Aras Vadeli", 1000, 10)
vadeli1.para_yatir(500) 
vadeli1.faiz_islet()
vadeli1.bilgi_ver()