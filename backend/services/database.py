import os
from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# --- 1. BAĞLANTI AYARLARI ---
# Render'daki ortam değişkenini al
DATABASE_URL = os.environ.get("DATABASE_URL")

print("--------------------------------------------------")
print("TEŞHİS: Veritabanı Bağlantısı Kontrol Ediliyor...")

if DATABASE_URL:
    print("✅ DURUM: Render Kalıcı Hafızası (PostgreSQL) Algılandı.")
    # Render düzeltmesi (postgres -> postgresql)
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
else:
    print("⚠️ UYARI: Render Ayarı Bulunamadı!")
    print("❌ DURUM: Geçici Hafıza (SQLite) Kullanılıyor. Veriler SİLİNECEK.")
    # Yerel çalışma için yedek
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'yerel_hafiza.db')}"

print(f"🔗 HEDEF: {DATABASE_URL}")
print("--------------------------------------------------")

# Motoru Başlat
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- 2. TABLO MODELLERİ (Hepsi Burada) ---

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    # İlişkiler
    analyses = relationship("Analysis", back_populates="owner")

class Analysis(Base):
    __tablename__ = "analyses"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    analysis_type = Column(String) # ISIM veya RUYA
    input_text = Column(Text)
    result_text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # İlişkiler
    owner = relationship("User", back_populates="analyses")

# Tabloları Veritabanında Oluştur
Base.metadata.create_all(bind=engine)

# --- 3. BAĞLANTI FONKSİYONU ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()