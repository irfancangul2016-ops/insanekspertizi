# backend/schemas.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# --- ANALİZ ŞEMALARI ---
class AnalysisBase(BaseModel):
    analysis_type: str
    input_text: str
    result_text: str

class AnalysisCreate(AnalysisBase):
    pass

class Analysis(AnalysisBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

# --- KULLANICI ŞEMALARI ---
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    analyses: List[Analysis] = [] # Kullanıcının geçmiş analizleri

    class Config:
        orm_mode = True

# --- TOKEN (Giriş) ŞEMASI ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None