import warnings
warnings.filterwarnings("ignore") # Uyarıları sustur

import os
import requests
import re
import datetime
from datetime import timedelta
from typing import List, Optional

from fastapi import FastAPI, Depends, HTTPException, status, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship, joinedload

from pydantic import BaseModel 
from passlib.context import CryptContext
from jose import JWTError, jwt

# --- 1. AYARLAR ---
DATABASE_URL = "sqlite:///./insan_ekspertizi.db"
SECRET_KEY = "cok_gizli_anahtar"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")

app = FastAPI()

# --- 2. AI MOTORU ---
class AIWriter:
    PERSONAS = {
        "yahya": "ROLÜN: Sen 'Yahya Bey', İslami kaynaklara hakim , beyefendi bir rüya tabiri uzmanısın.",
        "asli": "ROLÜN: Sen 'Aslı Hanım', astroloji ve enerji uzmanısın.",
        "mustafa": "ROLÜN: Sen 'Dr. Mustafa Bey', analitik psikoloji uzmanısın."
    }

    @staticmethod
    def _send_request(prompt_text):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key: return "HATA: API Key bulunamadı."
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        headers = {'Content-Type': 'application/json'}
        payload = {"contents": [{"parts": [{"text": prompt_text}]}]}
        try:
            res = requests.post(url, headers=headers, json=payload, timeout=60)
            if res.status_code == 200: return res.json()['candidates'][0]['content']['parts'][0]['text']
            return "Servis şu an cevap veremiyor."
        except Exception as e: return f"Bağlantı hatası: {str(e)}"

    @staticmethod
    def generate_name_analysis_rag(isim, mentor):
        return AIWriter._send_request(f"{AIWriter.PERSONAS.get(mentor,'yahya')}\n\nKişi: {isim}\nKarakter analizi yap.")

    @staticmethod
    def ruya_tabiri_motoru(ruya, mentor):
        return AIWriter._send_request(f"{AIWriter.PERSONAS.get(mentor,'yahya')}\n\nRüya: {ruya}\nYorumla.")

# --- 3. TABLOLAR ---
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    analyses = relationship("Analysis", back_populates="owner")

class Analysis(Base):
    __tablename__ = "analyses"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    analysis_type = Column(String)
    input_text = Column(String)
    result_text = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    owner = relationship("User", back_populates="analyses")

class BlogPost(Base):
    __tablename__ = "blog_posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)
    image_url = Column(String, nullable=True)
    author = Column(String, default="Editör")
    is_published = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(bind=engine)

# --- 4. ŞEMALAR ---
class UserCreate(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class AnalysisSchema(BaseModel):
    id: int
    analysis_type: str
    input_text: str
    result_text: str
    created_at: datetime.datetime
    class Config: orm_mode = True

class UserWithHistory(BaseModel):
    email: str
    analyses: List[AnalysisSchema] = []
    class Config: orm_mode = True

# --- 5. YARDIMCILAR ---
def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

def seed_blog_posts(db: Session):
    if db.query(BlogPost).count() == 0:
        db.add(BlogPost(title="Örnek Yazı", content="<p>İçerik...</p>", author="Admin"))
        db.commit()

def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.datetime.utcnow() + timedelta(minutes=60)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None: raise HTTPException(status_code=401)
    except JWTError: raise HTTPException(status_code=401)
    user = db.query(User).filter(User.email == email).first()
    if user is None: raise HTTPException(status_code=401)
    return user

# --- 6. API ---
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root(): return FileResponse('static/index.html')

@app.get("/blog")
def read_blog(): return FileResponse('static/blog.html')

# --- YENİ EKLENEN GİZLİ KONTROL PANELİ ---
@app.get("/api/debug/users")
def debug_users(db: Session = Depends(get_db)):
    """Sistemdeki kayıtlı tüm kullanıcıları gösterir (Şifreleri gizleyerek)"""
    users = db.query(User).all()
    return [{"id": u.id, "email": u.email} for u in users]
# ----------------------------------------

@app.post("/api/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Email'i küçük harfe çeviriyoruz ki 'Admin' ile 'admin' karışmasın
    clean_email = user.email.lower().strip()
    
    db_user = db.query(User).filter(User.email == clean_email).first()
    if db_user: raise HTTPException(status_code=400, detail="Bu email zaten kayıtlı")
    
    hashed_pw = pwd_context.hash(user.password)
    new_user = User(email=clean_email, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    return {"msg": "Kayıt başarılı"}

@app.post("/api/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Giriş yaparken de email'i küçültüyoruz
    clean_email = form_data.username.lower().strip()
    
    user = db.query(User).filter(User.email == clean_email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Böyle bir kullanıcı bulunamadı")
    if not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Şifre yanlış")
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/api/users/me", response_model=UserWithHistory)
async def read_users_me(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(User).options(joinedload(User.analyses)).filter(User.id == current_user.id).first()
    su_an = datetime.datetime.utcnow()
    for analiz in user.analyses:
        if (su_an - analiz.created_at).total_seconds() / 60 < 10: 
            analiz.result_text = "WAITING_FOR_MENTOR"
    return user

@app.post("/api/isim-analizi-yap")
async def isim_analiz(request: Request, isim: str = Form(...), soyisim: str = Form(...), mentor: str = Form("yahya"), db: Session = Depends(get_db)):
    try:
        tam_isim = f"{isim} {soyisim}".upper()
        sonuc = AIWriter.generate_name_analysis_rag(tam_isim, mentor)
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(" ")[1]
            user = await get_current_user(token, db)
            db.add(Analysis(user_id=user.id, analysis_type="ISIM", input_text=tam_isim, result_text=sonuc))
            db.commit()
        return {"analiz_sonucu": sonuc}
    except Exception as e: return JSONResponse({"hata": str(e)}, status_code=500)

@app.post("/api/ruya-analizi")
async def ruya_analiz(request: Request, ruya_metni: str = Form(...), mentor: str = Form("yahya"), db: Session = Depends(get_db)):
    try:
        sonuc = AIWriter.ruya_tabiri_motoru(ruya_metni, mentor)
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(" ")[1]
            user = await get_current_user(token, db)
            db.add(Analysis(user_id=user.id, analysis_type="RUYA", input_text=ruya_metni, result_text=sonuc))
            db.commit()
        return {"analiz": sonuc}
    except Exception as e: return JSONResponse({"analiz": str(e)}, status_code=500)

@app.get("/api/posts")
def get_public_posts(db: Session = Depends(get_db)):
    seed_blog_posts(db)
    return db.query(BlogPost).filter(BlogPost.is_published == True).order_by(BlogPost.created_at.desc()).all()