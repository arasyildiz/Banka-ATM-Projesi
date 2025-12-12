import sqlite3

DB_NAME = "banka.db"

def baglanti_kur():
    """Veritabanına bağlanır ve bağlantı nesnesini döndürür."""
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except sqlite3.Error as e:
        print(f"Veritabanı hatası: {e}")
        return None

def tablolari_olustur():
    """Gerekli tabloları oluşturur (İlk kurulum için)."""
    conn = baglanti_kur()
    if conn is not None:
        cursor = conn.cursor()
        
        sorgu = """
        CREATE TABLE IF NOT EXISTS hesaplar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT NOT NULL,
            bakiye REAL DEFAULT 0,
            hesap_turu TEXT DEFAULT 'Normal'
        )
        """
        cursor.execute(sorgu) 
        conn.commit()         
        conn.close()
        print("Veritabanı ve Tablo başarıyla hazırlandı.")
    else:
        print("Bağlantı kurulamadı!")
        
def hesap_ekle(isim, bakiye, tur = "Normal"):
    conn = baglanti_kur()
    if conn is not None:
        cursor = conn.cursor()
        
        sorgu = "INSERT INTO hesaplar(isim, bakiye, hesap_turu) VALUES(? ,? ,?)"
        cursor.execute(sorgu, (isim, bakiye, tur))    
        conn.commit()
        conn.close()
        print(f"Kayıt Başarılı: {isim} veritabanına eklendi.")
        
def hesap_bilgisini_getir(aranacak_isim):
    conn = baglanti_kur()
    if conn is not None:
        cursor = conn.cursor()
        
        sorgu = "SELECT * FROM hesaplar where isim = ?"
        
        cursor.execute(sorgu, (aranacak_isim,))
        kayit = cursor.fetchone()
        conn.close()
        return kayit
    
def bakiye_guncelle(isim, yeni_bakiye):
    conn = baglanti_kur()
    cursor = conn.cursor()
    
    sorgu = "UPDATE hesaplar SET bakiye = ? WHERE isim = ?"
    cursor.execute(sorgu, (yeni_bakiye, isim))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    tablolari_olustur()