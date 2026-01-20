# backend/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite veritabanı dosyası oluşturuyoruz (insan_ekspertizi.db)
SQLALCHEMY_DATABASE_URL = "sqlite:///./insan_ekspertizi.db"

# Veritabanı motorunu başlat
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Oturum (Session) oluşturucu
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Modellerin miras alacağı temel sınıf
Base = declarative_base()

# Veritabanı oturumu almak için yardımcı fonksiyon
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()