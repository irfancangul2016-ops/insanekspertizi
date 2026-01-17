import os
import time
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Veritabanı Bağlantı Ayarları
# Önce Render'daki gerçek veritabanına bak, yoksa geçici (sqlite) kullan.
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    # Eğer ortam değişkeni yoksa (Localde çalışıyorsan) SQLite kullan
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'yerel_hafiza.db')}"
else:
    # Render'ın verdiği postgres:// linkini sqlalchemy'nin anladığı postgresql:// formatına çevir
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Motoru Başlat
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- TABLO TANIMI (MODEL) ---
class Musteri(Base):
    __tablename__ = "musteriler"

    id = Column(Integer, primary_key=True, index=True)
    tarih = Column(String)
    isim = Column(String)
    soyisim = Column(String)
    dogum_tarihi = Column(String)
    pin_kodu = Column(Integer)
    baskin_element = Column(String)
    eksik_element = Column(String)

# Tabloları Oluştur (Yoksa)
Base.metadata.create_all(bind=engine)

class Database:
    def __init__(self):
        self.db = SessionLocal()

    def kayit_ekle(self, data: dict):
        """Yeni müşteri kaydeder"""
        try:
            tarih_saat = time.strftime("%Y-%m-%d %H:%M:%S")
            
            yeni_musteri = Musteri(
                tarih=tarih_saat,
                isim=data.get('isim'),
                soyisim=data.get('soyisim'),
                dogum_tarihi=f"{data.get('gun')}.{data.get('ay')}.{data.get('yil')}",
                pin_kodu=data.get('pin', 0),
                baskin_element=data.get('baskin_element', '-'),
                eksik_element=data.get('eksik_element', '-')
            )
            
            self.db.add(yeni_musteri)
            self.db.commit()
            self.db.refresh(yeni_musteri)
            print(f"--> VERİTABANI KAYDI BAŞARILI: {yeni_musteri.isim}")
            return yeni_musteri
        except Exception as e:
            print(f"Veritabanı Hatası: {e}")
            self.db.rollback()
        finally:
            self.db.close()

    def tum_kayitlari_getir(self):
        """Tüm listeyi çeker"""
        try:
            kayitlar = self.db.query(Musteri).order_by(Musteri.id.desc()).all()
            # SQLAlchemy objelerini sözlüğe çevir (Admin paneli için)
            sonuc = []
            for k in kayitlar:
                sonuc.append({
                    "id": k.id,
                    "tarih": k.tarih,
                    "isim": k.isim,
                    "soyisim": k.soyisim,
                    "dogum_tarihi": k.dogum_tarihi,
                    "pin_kodu": k.pin_kodu,
                    "baskin_element": k.baskin_element,
                    "eksik_element": k.eksik_element
                })
            return sonuc
        except Exception as e:
            print(f"Liste Hatası: {e}")
            return []
        finally:
            self.db.close()