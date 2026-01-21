import os
import sys
# Sistem yolunu ayarla
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Depends, HTTPException, status, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import desc
from datetime import timedelta
from typing import List

# Modüller
import database as models
from database import engine, get_db
import dto
from services.auth import AuthService
from services.ai_writer import AIWriter

app = FastAPI(title="İnsan Ekspertizi")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Statik Dosyalar
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# --- YARDIMCI FONKSİYONLAR ---
def get_current_user(request: Request, db: Session):
    auth_header = request.headers.get('Authorization')
    if not auth_header: return None
    try:
        token = auth_header.split(" ")[1]
        from jose import jwt
        from services.auth import SECRET_KEY, ALGORITHM
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        user = db.query(models.User).filter(models.User.email == email).first()
        return user
    except:
        return None

def kaydet(db: Session, tip: str, girdi: str, sonuc: str, user_id: int = None):
    try:
        yeni = models.Analysis(
            user_id=user_id, analysis_type=tip, input_text=girdi, result_text=sonuc
        )
        db.add(yeni)
        db.commit()
    except Exception as e:
        print(f"Kayıt Hatası: {e}")

# --- API UÇLARI ---

@app.post("/api/register", response_model=dto.User)
def register(user: dto.UserCreate, db: Session = Depends(get_db)):
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
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not AuthService.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Hatalı giriş")
    
    token = AuthService.create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/api/users/me", response_model=dto.User)
def get_me(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    if not user: raise HTTPException(status_code=401, detail="Oturum bulunamadı")
    return user

@app.post("/api/isim-analizi-yap")
async def isim_analiz(request: Request, isim: str = Form(...), soyisim: str = Form(...), db: Session = Depends(get_db)):
    try:
        tam_isim = f"{isim} {soyisim}".upper()
        sonuc = AIWriter.generate_name_analysis_rag(tam_isim)
        user = get_current_user(request, db)
        user_id = user.id if user else None
        kaydet(db, "ISIM", tam_isim, sonuc, user_id)
        return JSONResponse({"analiz_sonucu": sonuc})
    except Exception as e:
        return JSONResponse({"hata": str(e)}, status_code=500)

@app.post("/api/ruya-analizi")
async def ruya_analiz(request: Request, ruya_metni: str = Form(...), db: Session = Depends(get_db)):
    try:
        sonuc = AIWriter.ruya_tabiri_motoru(ruya_metni)
        user = get_current_user(request, db)
        user_id = user.id if user else None
        kaydet(db, "RUYA", ruya_metni, sonuc, user_id)
        return JSONResponse({"analiz": sonuc})
    except Exception as e:
        return JSONResponse({"analiz": str(e)}, status_code=500)

# --- 👑 ADMIN PANELI API UÇLARI (YENİ) ---

@app.get("/api/admin/stats")
def get_stats(request: Request, db: Session = Depends(get_db)):
    # 1. Güvenlik Kontrolü: İsteyen kişi Admin mi?
    admin = get_current_user(request, db)
    if not admin or not admin.is_admin:
        raise HTTPException(status_code=403, detail="Erişim Reddedildi! Sadece Yöneticiler.")
    
    # 2. İstatistikleri Topla
    total_users = db.query(models.User).count()
    total_analysis = db.query(models.Analysis).count()
    
    # Son 50 analizi getir
    recent_activity = db.query(models.Analysis)\
        .order_by(desc(models.Analysis.id))\
        .limit(50)\
        .all()
    
    # Veriyi JSON formatına çevir
    activity_list = []
    for item in recent_activity:
        owner_email = item.owner.email if item.owner else "Misafir"
        activity_list.append({
            "id": item.id,
            "type": item.analysis_type,
            "input": item.input_text,
            "result": item.result_text[:50] + "...", # Sadece başını göster
            "user": owner_email,
            "date": item.created_at.strftime("%d.%m.%Y %H:%M")
        })
        
    return {
        "total_users": total_users,
        "total_analysis": total_analysis,
        "activities": activity_list
    }

# --- 🕵️‍♂️ GİZLİ GEÇİT: SENİ ADMIN YAPAR ---
# Bu linki tarayıcıdan bir kez çalıştırınca admin olursun.
@app.get("/api/gizli-admin-ol/{email}")
def make_admin(email: str, secret: str, db: Session = Depends(get_db)):
    
@app.get("/admin")
def admin_panel():
    path = os.path.join(STATIC_DIR, "admin.html")
    if os.path.exists(path): return FileResponse(path)
    return "Admin paneli dosyası bulunamadı."

@app.get("/")
def home():
    path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(path): return FileResponse(path)
    return "Sistem Çalışıyor"
# --- 🚑 ACİL DURUM TAMİR KİTİ (Bunu en alta ekle) ---
from sqlalchemy import text

@app.get("/api/db-repair")
def repair_database(db: Session = Depends(get_db)):
    try:
        # Veritabanına zorla 'is_admin' sütununu ekle
        db.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS is_admin BOOLEAN DEFAULT FALSE;"))
        db.commit()
        return {"durum": "BAŞARILI", "mesaj": "Veritabanı tamir edildi! 'is_admin' sütunu eklendi."}
    except Exception as e:
        return {"durum": "HATA", "mesaj": str(e)}