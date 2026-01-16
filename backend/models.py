from sqlalchemy import Column, Integer, String, Text, DateTime
from core.database import Base
from datetime import datetime

class AnalizKaydi(Base):
    __tablename__ = "analizler"

    id = Column(Integer, primary_key=True, index=True)
    
    # Kişisel Bilgiler
    isim_soyisim = Column(String, index=True)
    dogum_tarihi = Column(String)
    analiz_tarihi = Column(DateTime, default=datetime.utcnow)
    
    # Teknik Sonuçlar
    pin_kodu = Column(Integer)
    yasam_yolu = Column(Integer)
    baskin_element = Column(String)
    eksik_element = Column(String)
    
    # Yapay Zeka Çıktısı (Uzun metin olduğu için Text tipi)
    ai_raporu = Column(Text)
    
    # PDF Dosya Yolu (İleride tekrar indirmek isterse)
    pdf_yolu = Column(String)