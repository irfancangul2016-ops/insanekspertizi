import os
from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime

# Veritabanı Bağlantısı
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL and DATABASE_URL.startswith("postgres"):
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    engine = create_engine(DATABASE_URL)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'yerel_hafiza.db')}"
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- TABLO MODELLERİ ---

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False) # Admin yetkisi
    
    analyses = relationship("Analysis", back_populates="owner")

class Analysis(Base):
    __tablename__ = "analyses"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    analysis_type = Column(String)
    input_text = Column(Text)
    result_text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    owner = relationship("User", back_populates="analyses")

# 👇 İŞTE BU EKSİK OLABİLİR, BUNUN BURADA OLDUĞUNDAN EMİN OL 👇
class BlogPost(Base):
    __tablename__ = "blog_posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    slug = Column(String, unique=True, index=True)
    content = Column(Text)
    image_url = Column(String)
    views = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()