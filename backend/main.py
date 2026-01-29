import os
import sys
import time
import re
from collections import defaultdict
from datetime import datetime
from typing import List

# FastAPI ve Pydantic
from fastapi import FastAPI, Request, Form, Depends, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

# SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import desc

# Rate Limiting
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# Kendi Modüllerimiz
# Dikkat: database.py'dan sadece bağlantı araçlarını alıyoruz
from database import engine, get_db, Base
# Tabloları models.py'dan alıyoruz (Çift tanımlama olmasın diye)
from models import User, Analysis, BlogPost 
import dto
from services.auth import AuthService
from services.ai_writer import AIWriter

# Tabloları Oluştur
Base.metadata.create_all(bind=engine)

app = FastAPI(title="İnsan Ekspertizi")

# --- AYARLAR ---
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Rate Limiting Mantığı
request_counts = defaultdict(list)
@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    if request.url.path in ["/api/isim-analizi-yap", "/api/ruya-analizi"]:
        client_ip = request.client.host
        now = time.time()
        request_counts[client_ip] = [t for t in request_counts[client_ip] if now - t < 60]
        if len(request_counts[client_ip]) >= 10:
            return JSONResponse(status_code=429, content={"analiz": "Çok hızlısın, 1 dk bekle."})
        request_counts[client_ip].append(now)
    response = await call_next(request)
    return response

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
        return db.query(User).filter(User.email == email).first()
    except: return None

def kaydet(db: Session, tip: str, girdi: str, sonuc: str, user_id: int = None):
    try:
        yeni = Analysis(user_id=user_id, analysis_type=tip, input_text=girdi, result_text=sonuc)
        db.add(yeni)
        db.commit()
    except: pass

# --- AUTH API ---
@app.post("/api/register", response_model=dto.User)
def register(user: dto.UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="E-posta kullanımda.")
    hashed = AuthService.get_password_hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed)
    db.add(new_user)
    db.commit()
    return new_user

@app.post("/api/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not AuthService.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Hatalı giriş")
    return {"access_token": AuthService.create_access_token(data={"sub": user.email}), "token_type": "bearer"}

@app.get("/api/users/me")
def get_me(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    if not user: raise HTTPException(status_code=401, detail="Oturum yok")
    
    analizler_db = db.query(Analysis).filter(Analysis.user_id == user.id).order_by(desc(Analysis.id)).all()
    
    analiz_listesi = []
    for a in analizler_db:
        analiz_listesi.append({
            "id": a.id,
            "input_text": a.input_text,
            "result_text": a.result_text,
            "created_at": a.created_at,
            "analysis_type": a.analysis_type
        })
    
    return {
        "email": user.email,
        "analyses": analiz_listesi,
        "is_admin": user.is_admin
    }

# --- ANALİZ API ---
@app.post("/api/isim-analizi-yap")
@limiter.limit("5/minute")
async def isim_analiz(request: Request, isim: str = Form(...), soyisim: str = Form(...), mentor: str = Form("yahya"), db: Session = Depends(get_db)):
    try:
        tam = f"{isim} {soyisim}".upper()
        sonuc = AIWriter.generate_name_analysis_rag(tam, mentor)
        u = get_current_user(request, db)
        kaydet(db, "ISIM", tam, sonuc, u.id if u else None)
        return {"analiz_sonucu": sonuc}
    except Exception as e: return JSONResponse({"hata": str(e)}, status_code=500)

@app.post("/api/ruya-analizi")
@limiter.limit("5/minute")
async def ruya_analiz(request: Request, ruya_metni: str = Form(...), mentor: str = Form("yahya"), db: Session = Depends(get_db)):
    try:
        sonuc = AIWriter.ruya_tabiri_motoru(ruya_metni, mentor)
        u = get_current_user(request, db)
        kaydet(db, "RUYA", ruya_metni, sonuc, u.id if u else None)
        return {"analiz": sonuc}
    except Exception as e: return JSONResponse({"analiz": str(e)}, status_code=500)

# --- BLOG API (PUBLIC) ---
@app.get("/api/blog/posts")
def get_posts(db: Session = Depends(get_db)):
    try:
        posts = db.query(BlogPost).order_by(desc(BlogPost.created_at)).all()
        data = []
        for p in posts:
            data.append({
                "id": p.id,
                "title": p.title,
                "slug": p.slug,
                "content": p.content,
                "image_url": p.image_url,
                "created_at": p.created_at,
                "views": p.views
            })
        return data
    except Exception: return []

@app.get("/api/blog/posts/{slug}")
def get_post_detail(slug: str, db: Session = Depends(get_db)):
    clean_slug = slug.strip().split("?")[0]
    post = db.query(BlogPost).filter(BlogPost.slug == clean_slug).first()
    if not post: raise HTTPException(status_code=404, detail="Yazı bulunamadı")
    post.views += 1
    db.commit()
    return {
        "id": post.id, "title": post.title, "slug": post.slug, 
        "content": post.content, "image_url": post.image_url, 
        "created_at": post.created_at, "views": post.views
    }

# --- ADMIN API (PROTECTED) ---
@app.post("/api/admin/blog/create")
def create_post(request: Request, title: str = Form(...), content: str = Form(...), image_url: str = Form(...), db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    # Admin yetki kontrolü
    admins = ["irfancangul2016@gmail.com", "admin@insanekspertizi.org"]
    if not user or (user.email not in admins and not user.is_admin):
        raise HTTPException(status_code=403, detail="Yetkisiz")
    
    slug = title.lower().replace(" ", "-").replace("ı","i").replace("ğ","g").replace("ü","u").replace("ş","s").replace("ö","o").replace("ç","c")
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    
    try:
        new_post = BlogPost(title=title, content=content, image_url=image_url, slug=slug)
        db.add(new_post)
        db.commit()
        return {"durum": "BAŞARILI", "slug": slug}
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": f"Kayıt Hatası: {str(e)}"})

@app.delete("/api/admin/blog/delete/{id}")
def delete_post(id: int, request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    admins = ["irfancangul2016@gmail.com", "admin@insanekspertizi.org"]
    if not user or (user.email not in admins and not user.is_admin):
        raise HTTPException(status_code=403, detail="Yetkisiz")
    
    db.query(BlogPost).filter(BlogPost.id == id).delete()
    db.commit()
    return {"durum": "SİLİNDİ"}

# --- ADMIN STATS ---
@app.get("/api/admin/stats")
def get_stats(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    admins = ["irfancangul2016@gmail.com", "admin@insanekspertizi.org"]
    
    # Yetki Kontrolü
    if not user or (user.email not in admins and not user.is_admin):
        raise HTTPException(status_code=403, detail="Yetersiz Yetki")
    
    try:
        # İstatistikler
        total_users = db.query(User).count()
        total_analyses = db.query(Analysis).count()
        total_posts = db.query(BlogPost).count()
        
        # Son Aktiviteler
        recent = db.query(Analysis).order_by(desc(Analysis.created_at)).limit(20).all()
        activities = []
        for r in recent:
            activities.append({
                "id": r.id,
                "user": r.user_id,
                "type": r.analysis_type,
                "input": r.input_text[:30] + "...",
                "date": r.created_at.strftime("%Y-%m-%d %H:%M")
            })

        return {
            "total_users": total_users,
            "total_analysis": total_analyses,
            "total_posts": total_posts,
            "activities": activities
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": f"Stats Hatası: {str(e)}"})

# --- STATIC FILES & SPA ROUTING ---
@app.get("/robots.txt", response_class=FileResponse)
def robots(): return FileResponse("robots.txt") if os.path.exists("robots.txt") else "Robots.txt yok"

@app.get("/sitemap.xml", response_class=FileResponse)
def sitemap(): return FileResponse("sitemap.xml") if os.path.exists("sitemap.xml") else "Sitemap yok"

@app.get("/")
def home(): return FileResponse(os.path.join(STATIC_DIR, "index.html"))

@app.get("/admin")
def admin(): return FileResponse(os.path.join(STATIC_DIR, "admin.html"))

@app.get("/blog")
@app.get("/blog/{slug}")
def blog(slug: str = None): return FileResponse(os.path.join(STATIC_DIR, "blog.html"))