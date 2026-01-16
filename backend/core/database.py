from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Dosya tabanlı basit veritabanı (insan_ekspertizi.db adında bir dosya oluşacak)
SQLALCHEMY_DATABASE_URL = "sqlite:///./insan_ekspertizi.db"

# Motoru başlat
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Oturum açıcı (SessionLocal)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Taban model
Base = declarative_base()

# Veritabanı bağlantısı için yardımcı fonksiyon
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()