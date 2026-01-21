# backend/services/auth.py
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
import os

# --- AYARLAR ---
# Gerçek projede bu key .env dosyasından gelmeli, şimdilik buraya yazıyoruz.
SECRET_KEY = "COK_GIZLI_VE_GUCLU_BIR_ANAHTAR_BURAYA_RASTGELE_HARFLER_YAZ"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 3000

# Şifreleme Bağlamı (Bcrypt kullanır)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    @staticmethod
    def verify_password(plain_password, hashed_password):
        """Kullanıcının girdiği şifre ile veritabanındaki hash'i karşılaştırır."""
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        """Şifreyi veritabanına kaydetmeden önce hashler (karıştırır)."""
        return pwd_context.hash(password)

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        """Kullanıcıya giriş bileti (JWT Token) verir."""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt