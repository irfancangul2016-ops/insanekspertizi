# backend/dto.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# --- KULLANICI ŞEMALARI ---
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool = True       # Varsayılan değer eklendi
    is_admin: bool = False       # KRİTİK DÜZELTME: Varsayılan değer eklendi
    
    class Config:
        from_attributes = True

# --- TOKEN (GİRİŞ BİLETİ) ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None