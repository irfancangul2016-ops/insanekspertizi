# backend/dto.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# --- TOKEN (GİRİŞ) ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# --- ANALİZ VERİLERİ ---
class AnalysisBase(BaseModel):
    analysis_type: str
    input_text: str
    result_text: str

class AnalysisCreate(AnalysisBase):
    pass

class Analysis(AnalysisBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True

# --- KULLANICI VERİLERİ ---
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    analyses: List[Analysis] = []

    class Config:
        from_attributes = True