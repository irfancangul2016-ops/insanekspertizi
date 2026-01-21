# backend/main.py
import os
import sys

# --- SİSTEM YOLU AYARI ---
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from fastapi import FastAPI, Depends, HTTPException, status, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from datetime import timedelta
from pydantic import BaseModel
import uvicorn

# --- KENDİ MODÜLLERİMİZ ---
from database import engine, get_db
import models
import dto  # <--- ARTIK SCHEMAS YOK, DTO VAR
from services.auth import AuthService
from services.ai_writer import AIWriter
from services.calculator import EbcedCalculator

# --- VERİTABANI OLUŞTURMA ---

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="İnsan Ekspertizi API", version="2.0")

# --- GÜVENLİK ---
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")

# --- CORS AYARLARI ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- DOSYA YOLLARI ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# --- YARDIMCI FONKSİYONLAR ---

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Giriş bilgileri doğrulanamadı",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        from services.auth import SECRET_KEY, ALGORITHM
        from jose import jwt
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except Exception:
        raise credentials_exception
    
    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        raise credentials_exception
    return user

def analiz_kaydet(db: Session, tip: str, girdi: str, sonuc: str, user_id: int = None):
    try:
        yeni_analiz = models.Analysis(
            user_id=user_id,
            analysis_type=tip,
            input_text=girdi,
            result_text=sonuc
        )
        db.add(yeni_analiz)
        db.commit()
    except Exception as e:
        print(f"❌ Kayıt Hatası: {str(e)}")

# --- AUTH ENDPOINTLERİ ---

@app.post("/api/register", response_model=dto.User) # <--- DTO OLDU
def register(user: dto.UserCreate, db: Session = Depends(get_db)): # <--- DTO OLDU
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Bu e-posta zaten kayıtlı.")
    
    hashed_password = AuthService.get_password_hash(user.password)
    new_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/api/token", response_model=dto.Token) # <--- DTO OLDU
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not AuthService.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-posta veya şifre hatalı",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=3000)
    access_token = AuthService.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/api/users/me", response_model=dto.User) # <--- DTO OLDU
def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user

# --- ANALİZ ENDPOINTLERİ ---

@app.post("/api/isim-analizi-yap")
async def isim_analizi_servisi(
    isim: str = Form(...),
    soyisim: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        tam_isim = f"{isim} {soyisim}".upper()
        analiz_metni = AIWriter.generate_name_analysis_rag(tam_isim)
        analiz_kaydet(db, "ISIM", tam_isim, analiz_metni, user_id=None)
        
        return JSONResponse({
            "kisi": tam_isim,
            "analiz_sonucu": analiz_metni,
            "kaynak": "İnsan Ekspertizi Arşivi"
        })
    except Exception as e:
        return JSONResponse({"hata": f"Sunucu Hatası: {str(e)}"}, status_code=500)

@app.post("/api/ruya-analizi")
async def ruya_analizi_servisi(
    ruya_metni: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        if len(ruya_metni.strip()) < 5:
            return JSONResponse({"analiz": "Lütfen rüyanızı detaylı anlatın."})

        analiz_sonucu = AIWriter.ruya_tabiri_motoru(ruya_metni)
        analiz_kaydet(db, "RUYA", ruya_metni, analiz_sonucu, user_id=None)
        
        return JSONResponse({"analiz": analiz_sonucu})
    except Exception as e:
        return JSONResponse({"analiz": f"Hata: {str(e)}"}, status_code=500)

# --- DİĞER ENDPOINTLER ---

class AnalizIstegi(BaseModel):
    isim: str
    soyisim: str
    dogum_gun: int
    dogum_ay: int
    dogum_yil: int
    anne_adi: str

@app.post("/api/analiz-yap")
async def api_analiz(istek: AnalizIstegi):
    try:
        pin = EbcedCalculator.calculate_pin_code(istek.isim, istek.soyisim, istek.anne_adi)
        element_skorlari = EbcedCalculator.analyze_elements(istek.isim + istek.soyisim)
        return JSONResponse({
            "ad_soyad": f"{istek.isim} {istek.soyisim}",
            "pin_kodu": pin,
            "elementler": element_skorlari
        })
    except Exception as e:
        return JSONResponse(content={"hata": str(e)}, status_code=500)

@app.get("/", response_class=HTMLResponse)
async def ana_sayfa():
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return f.read()
    return "Sistem Aktif (Arayüz Bulunamadı)"

@app.get("/manifest.json")
async def get_manifest():
    return FileResponse(os.path.join(STATIC_DIR, "manifest.json"), media_type="application/json")

@app.get("/sw.js")
async def get_sw():
    return FileResponse(os.path.join(STATIC_DIR, "sw.js"), media_type="application/javascript")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)