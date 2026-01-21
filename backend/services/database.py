import os
import time
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# --- KRİTİK BAĞLANTI NOKTASI ---
# Burası Render'daki ayarı okumaya çalışır.
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    print("🔴 DİKKAT: Render ayarı bulunamadı, GEÇİCİ HAFIZA (SQLite) kullanılıyor!")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'yerel_hafiza.db')}"
else:
    print("🟢 BAŞARILI: Render Kalıcı Hafızası (PostgreSQL) Devrede!")
    # Render "postgres://" verir, Python "postgresql://" ister. Düzeltiyoruz:
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Motoru Başlat
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- TABLOLAR ---

# 1. ESKİ TABLO: MUSTERİLER
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

# 2. YENİ TABLO: KULLANICILAR
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    analyses = relationship("Analysis", back_populates="owner")

# 3. YENİ TABLO: ANALİZ GEÇMİŞİ
class Analysis(Base):
    __tablename__ = "analyses"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    analysis_type = Column(String)
    input_text = Column(Text)
    result_text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    owner = relationship("User", back_populates="analyses")

# Tabloları Kur
Base.metadata.create_all(bind=engine)

# --- YARDIMCI FONKSİYONLAR ---

class Database:
    def __init__(self):
        self.db = SessionLocal()

    def kayit_ekle(self, data: dict):
        try:
            tarih_saat = time.strftime("%Y-%m-%d %H:%M:%S")
            yeni = Musteri(
                tarih=tarih_saat,
                isim=data.get('isim'),
                soyisim=data.get('soyisim'),
                dogum_tarihi=f"{data.get('gun')}.{data.get('ay')}.{data.get('yil')}",
                pin_kodu=data.get('pin', 0),
                baskin_element=data.get('baskin_element', '-'),
                eksik_element=data.get('eksik_element', '-')
            )
            self.db.add(yeni)
            self.db.commit()
            return yeni
        except Exception as e:
            self.db.rollback()
            print(f"Hata: {e}")
        finally:
            self.db.close()

    def tum_kayitlari_getir(self):
        try:
            kayitlar = self.db.query(Musteri).order_by(Musteri.id.desc()).all()
            return [{"id": k.id, "isim": k.isim} for k in kayitlar]
        except:
            return []
        finally:
            self.db.close()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()