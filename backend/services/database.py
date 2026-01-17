import sqlite3
import os
from datetime import datetime

class Database:
    def __init__(self, db_name="kozmik_hafiza.db"):
        # Veritabanını ana dizinde değil, tmp klasöründe veya services içinde tutalım
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(base_dir, db_name)
        self.init_db()

    def init_db(self):
        """Tablo yoksa oluşturur"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS musteriler (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tarih TEXT,
                isim TEXT,
                soyisim TEXT,
                dogum_tarihi TEXT,
                pin_kodu INTEGER,
                baskin_element TEXT,
                eksik_element TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def kayit_ekle(self, data: dict):
        """Yeni bir müşteri analizi kaydeder"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            tarih_saat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            cursor.execute('''
                INSERT INTO musteriler (tarih, isim, soyisim, dogum_tarihi, pin_kodu, baskin_element, eksik_element)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                tarih_saat,
                data.get('isim'),
                data.get('soyisim'),
                f"{data.get('gun')}.{data.get('ay')}.{data.get('yil')}",
                data.get('pin', 0),
                data.get('baskin_element', '-'),
                data.get('eksik_element', '-')
            ))
            
            conn.commit()
            conn.close()
            print(f"--> KAYIT BAŞARILI: {data.get('isim')} veritabanına eklendi.")
        except Exception as e:
            print(f"Veritabanı Hatası: {e}")

    def tum_kayitlari_getir(self):
        """Tüm müşteri listesini çeker (Admin için)"""
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row # Sözlük gibi erişmek için
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM musteriler ORDER BY id DESC") # En yeniden eskiye
            rows = cursor.fetchall()
            
            liste = [dict(row) for row in rows]
            conn.close()
            return liste
        except Exception as e:
            return []
        