import os
import sys
# Sistem yolunu ayarla
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Depends, HTTPException, status, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import Optional

# --- KRİTİK İMPORTLAR ---
# Artık her şey database.py içinde
import database as models 
from database import engine, get_db
import dto # Veri tipleri (bunu değiştirmedik, aynen kalabilir)

# Servisler
from services.auth import AuthService
from services.ai_writer import AIWriter

app = FastAPI(title="İnsan Ekspertizi", version="3.0 - Kalıcı Hafıza")

# CORS (İzinler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Statik Dosyalar (Frontend)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# --- YARDIMCI FONKSİYONLAR ---

def get_user_id_from_request(request: Request, db: Session):
    """Kullanıcı giriş yapmış mı bakar"""
    auth_header = request.headers.get('Authorization')
    if not auth_header: return None
    try:
        token = auth_header.split(" ")[1]
        from jose import jwt
        from services.auth import SECRET_KEY, ALGORITHM
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        user = db.query(models.User).filter(models.User.email == email).first()
        return user.id if user else None
    except:
        return None

def kaydet(db: Session, tip: str, girdi: str, sonuc: str, user_id: int = None):
    """Analizi veritabanına yazar"""
    yeni = models.Analysis(
        user_id=user_id,
        analysis_type=tip,
        input_text=girdi,
        result_text=sonuc
    )
    db.add(yeni)
    db.commit()

# --- API UÇLARI (ENDPOINTS) ---

@app.post("/api/register", response_model=dto.User)
def register(user: dto.UserCreate, db: Session = Depends(get_db)):
    # Aynı mail var mı kontrol et
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Bu e-posta zaten kullanımda.")
    
    hashed_password = AuthService.get_password_hash(user.password)
    new_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/api/token")
def login(form_data: dto.UserCreate, db: Session = Depends(get_db)): 
    # Not: Basitlik için JSON login kullanıyoruz, form-data değil
    user = db.query(models.User).filter(models.User.email == form_data.email).first()
    if not user or not AuthService.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Hatalı giriş bilgileri")
    
    token = AuthService.create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

# Form-Data Login (Frontend uyumu için alternatif)
from fastapi.security import OAuth2PasswordRequestForm
@app.post("/api/token-form")
def login_form(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not AuthService.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Hatalı giriş")
    token = AuthService.create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/api/users/me", response_model=dto.User)
def get_me(request: Request, db: Session = Depends(get_db)):
    user_id = get_user_id_from_request(request, db)
    if not user_id: raise HTTPException(status_code=401, detail="Giriş gerekli")
    return db.query(models.User).filter(models.User.id == user_id).first()

@app.post("/api/isim-analizi-yap")
async def isim_analiz(request: Request, isim: str = Form(...), soyisim: str = Form(...), db: Session = Depends(get_db)):
    try:
        tam_isim = f"{isim} {soyisim}".upper()
        sonuc = AIWriter.generate_name_analysis_rag(tam_isim) # AI Servisi
        user_id = get_user_id_from_request(request, db)
        kaydet(db, "ISIM", tam_isim, sonuc, user_id)
        return JSONResponse({"analiz_sonucu": sonuc})
    except Exception as e:
        return JSONResponse({"hata": str(e)}, status_code=500)

@app.post("/api/ruya-analizi")
async def ruya_analiz(request: Request, ruya_metni: str = Form(...), db: Session = Depends(get_db)):
    try:
        sonuc = AIWriter.ruya_tabiri_motoru(ruya_metni) # AI Servisi
        user_id = get_user_id_from_request(request, db)
        kaydet(db, "RUYA", ruya_metni, sonuc, user_id)
        return JSONResponse({"analiz": sonuc})
    except Exception as e:
        return JSONResponse({"hata": str(e)}, status_code=500)

@app.get("/")
def home():
    path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(path): return FileResponse(path)
    return "Sistem Çalışıyor (Frontend Bulunamadı)"
# --- SİSTEM KONTROL KAPISI (Bunu en alta ekle) ---
@app.get("/api/test-db")
def veritabani_testi():
    import os
    db_url = os.getenv("DATABASE_URL")
    
    status = {
        "durum": "Bilinmiyor",
        "hafiza_tipi": "Bilinmiyor",
        "ayar_var_mi": "HAYIR ❌"
    }
    
    if db_url:
        status["ayar_var_mi"] = "EVET ✅"
        if "postgres" in db_url:
            status["durum"] = "BAŞARILI 🟢"
            status["hafiza_tipi"] = "KALICI HAFIZA (PostgreSQL) 🐘"
            status["mesaj"] = "Verileriniz güvende, silinmeyecek."
        else:
            status["durum"] = "UYARI 🔴"
            status["hafiza_tipi"] = "Bilinmeyen URL"
    else:
        status["durum"] = "TEHLİKE 🔴"
        status["hafiza_tipi"] = "GEÇİCİ HAFIZA (SQLite) 📄"
        status["mesaj"] = "Site kapanınca her şey silinir! Render ayarlarını kontrol et."
        
    return status