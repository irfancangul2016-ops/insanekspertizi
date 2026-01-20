from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# --- TOKEN (GİRİŞ) ŞEMALARI ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# --- ANALİZ ŞEMALARI ---
class AnalysisBase(BaseModel):
    analysis_type: str
    input_text: str
    result_text: str

class AnalysisCreate(AnalysisBase):
    pass

class Analysis(AnalysisBase):
    id: int
    user_id: Optional[int] = None # Misafirler için boş olabilir
    created_at: datetime

    class Config:
        # Pydantic V2 uyumu için (ORM nesnelerini okuyabilmesi için)
        from_attributes = True

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
        from_attributes = True