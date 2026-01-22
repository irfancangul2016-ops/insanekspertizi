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

# SQLAlchemy ve Veritabanı
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship, joinedload

# Pydantic (Veri Şemaları)
from pydantic import BaseModel 

# Güvenlik (Şifreleme)
from passlib.context import CryptContext
from jose import JWTError, jwt

# --- 1. AYARLAR VE VERİTABANI BAĞLANTISI ---
DATABASE_URL = "sqlite:///./test.db"
SECRET_KEY = "cok_gizli_anahtar"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() # <-- 'Base not defined' hatasının çözümü

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")

app = FastAPI()

# --- 2. YAPAY ZEKA MOTORU (AI WRITER - REQUESTS MODU) ---
# (Buraya dokunma, bu senin çalışan motorun)
RUYA_SOZLUGU = {}
try:
    from services import ruya_data
    RUYA_SOZLUGU = getattr(ruya_data, "RUYA_SOZLUGU", {})
except: pass

class AIWriter:
    # Karakterler
    PERSONAS = {
        "yahya": "ROLÜN: Sen 'Yahya Bey', İslami kaynaklara hakim , beyefendi bir rüya tabiri uzmanısın. Asla laubali olma. 'Siz' diliyle konuş. ",
        "asli": "ROLÜN: Sen 'Aslı Hanım', astroloji ve enerji uzmanısın. Kurumsal ve profesyonel bir dille, 'Siz' hitabıyla kozmik döngülerden bahset.",
        "mustafa": "ROLÜN: Sen 'Dr. Mustafa Bey', analitik psikoloji uzmanısın. Jung ve Freud ekolüyle, tamamen bilimsel ve soğukkanlı yorum yap."
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
            if res.status_code == 200:
                return res.json()['candidates'][0]['content']['parts'][0]['text']
            return "Servis şu an cevap veremiyor."
        except Exception as e:
            return f"Bağlantı hatası: {str(e)}"

    @staticmethod
    def generate_name_analysis_rag(isim: str, mentor="yahya"):
        mentor_key = mentor.lower() if mentor in AIWriter.PERSONAS else "yahya"
        prompt = f"{AIWriter.PERSONAS[mentor_key]}\n\nKişi: {isim}\nBu kişi için karakter analizi yap."
        return AIWriter._send_request(prompt)

    @staticmethod
    def ruya_tabiri_motoru(ruya_metni: str, mentor="yahya"):
        mentor_key = mentor.lower() if mentor in AIWriter.PERSONAS else "yahya"
        prompt = f"{AIWriter.PERSONAS[mentor_key]}\n\nRüya: {ruya_metni}\nBu rüyayı yorumla."
        return AIWriter._send_request(prompt)

# --- 3. VERİTABANI TABLOLARI (MODELS) ---

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    # İlişki Tanımı
    analyses = relationship("Analysis", back_populates="owner")

class Analysis(Base):
    __tablename__ = "analyses"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    analysis_type = Column(String) # "ISIM" veya "RUYA"
    input_text = Column(String)
    result_text = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    # İlişki Tanımı
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

# Veritabanını Oluştur
Base.metadata.create_all(bind=engine)

# --- 4. PYDANTIC ŞEMALARI (SCHEMAS) ---
# "UserWithHistory is not defined" hatası almamak için bunları API'lerden ÖNCE yazıyoruz.

class AnalysisSchema(BaseModel):
    id: int
    analysis_type: str
    input_text: str
    result_text: str
    created_at: datetime.datetime
    class Config:
        orm_mode = True

class UserWithHistory(BaseModel):
    email: str
    analyses: List[AnalysisSchema] = []
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# --- 5. YARDIMCI FONKSİYONLAR ---

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None: raise HTTPException(status_code=401)
    except JWTError:
        raise HTTPException(status_code=401)
    user = db.query(User).filter(User.email == email).first()
    if user is None: raise HTTPException(status_code=401)
    return user

# --- 6. API ROUTE'LARI (YOLLAR) ---

# Statik Dosyalar (HTML, CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse('static/index.html')

@app.get("/blog")
def read_blog():
    return FileResponse('static/blog.html')

# Kayıt Ol
@app.post("/api/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user: raise HTTPException(status_code=400, detail="Email zaten kayıtlı")
    hashed_pw = pwd_context.hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    return {"msg": "Kayıt başarılı"}

# Giriş Yap (Token Al)
@app.post("/api/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Hatalı giriş")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# Geçmişi Getir (10 Dakika Kuralı Dahil)
@app.get("/api/users/me", response_model=UserWithHistory)
async def read_users_me(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(User).options(joinedload(User.analyses)).filter(User.id == current_user.id).first()
    
    # Zaman Kontrolü
    su_an = datetime.datetime.utcnow()
    for analiz in user.analyses:
        gecen_sure = (su_an - analiz.created_at).total_seconds() / 60
        # Eğer 10 dakikadan azsa (Test için 0 yapabilirsin)
        if gecen_sure < 10: 
            analiz.result_text = "WAITING_FOR_MENTOR"
            
    return user

# İsim Analizi Yap
@app.post("/api/isim-analizi-yap")
async def isim_analiz(
    request: Request, 
    isim: str = Form(...), 
    soyisim: str = Form(...), 
    mentor: str = Form("yahya"),
    db: Session = Depends(get_db)
):
    try:
        tam_isim = f"{isim} {soyisim}".upper()
        sonuc = AIWriter.generate_name_analysis_rag(tam_isim, mentor)
        
        # Kullanıcıyı bul (Token'dan)
        auth_header = request.headers.get('Authorization')
        user_id = None
        if auth_header:
            try:
                token = auth_header.split(" ")[1]
                user = await get_current_user(token, db)
                user_id = user.id
            except: pass
        
        if user_id:
            db_analiz = Analysis(user_id=user_id, analysis_type="ISIM", input_text=tam_isim, result_text=sonuc)
            db.add(db_analiz)
            db.commit()
            
        return {"analiz_sonucu": sonuc}
    except Exception as e:
        return JSONResponse({"hata": str(e)}, status_code=500)

# Rüya Analizi Yap
@app.post("/api/ruya-analizi")
async def ruya_analiz(
    request: Request, 
    ruya_metni: str = Form(...), 
    mentor: str = Form("yahya"),
    db: Session = Depends(get_db)
):
    try:
        sonuc = AIWriter.ruya_tabiri_motoru(ruya_metni, mentor)
        
        auth_header = request.headers.get('Authorization')
        user_id = None
        if auth_header:
            try:
                token = auth_header.split(" ")[1]
                user = await get_current_user(token, db)
                user_id = user.id
            except: pass
            
        if user_id:
            db_analiz = Analysis(user_id=user_id, analysis_type="RUYA", input_text=ruya_metni, result_text=sonuc)
            db.add(db_analiz)
            db.commit()
            
        return {"analiz": sonuc}
    except Exception as e:
        return JSONResponse({"analiz": str(e)}, status_code=500)

# Blog Yazılarını Getir
@app.get("/api/posts")
def get_public_posts(db: Session = Depends(get_db)):
    posts = db.query(BlogPost).filter(BlogPost.is_published == True).order_by(BlogPost.created_at.desc()).all()
    return posts