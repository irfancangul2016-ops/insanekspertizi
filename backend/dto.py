from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# --- 1. ANALİZ ŞEMASI (Giden Pakette Bu Olmalı) ---
class Analysis(BaseModel):
    id: int
    analysis_type: str
    input_text: str
    result_text: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# --- 2. KULLANICI ŞEMALARI ---
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool = True
    is_admin: bool = False
    
    # İŞTE EKSİK OLAN PARÇA BU:
    analyses: List[Analysis] = [] 
    
    class Config:
        from_attributes = True

# --- 3. TOKEN (GİRİŞ BİLETİ) ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None