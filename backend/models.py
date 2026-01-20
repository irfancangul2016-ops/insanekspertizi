# backend/models.py
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False) # Admin paneli için kritik

    # Kullanıcının analizleri ile ilişki kuruyoruz
    analyses = relationship("Analysis", back_populates="owner")

class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id")) # Hangi kullanıcıya ait?
    analysis_type = Column(String) # "ISIM" veya "RUYA"
    input_text = Column(Text)      # Kullanıcının girdiği (Rüya veya İsim)
    result_text = Column(Text)     # Yapay Zekanın cevabı
    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="analyses")