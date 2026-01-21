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
    is_active: bool
    is_admin: bool
    
    class Config:
        from_attributes = True

# --- TOKEN (GİRİŞ BİLETİ) ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None