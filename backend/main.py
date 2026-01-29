import os
import sys
import time
import re  # <--- YENİ EKLENEN (Temizlikçi)
from collections import defaultdict
from datetime import datetime
from sqlalchemy.orm import joinedload
from typing import List
from sqlalchemy import desc
# Pydantic modelleri için
from pydantic import BaseModel

# Modül yollarını ayarla
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Depends, HTTPException, status, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime, desc, text
from sqlalchemy.orm import Session

# Modüller
import database as models
from database import engine, get_db
import dto
from services.auth import AuthService
from services.ai_writer import AIWriter

# --- BYPASS: BLOG POST MODELİ (Main İçinde) ---
class BlogPost(models.Base):
    __tablename__ = "blog_posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    slug = Column(String, unique=True, index=True)
    content = Column(Text)
    image_url = Column(String)
    views = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="İnsan Ekspertizi")

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

# Rate Limiting
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

# --- YARDIMCI ---
def get_current_user(request: Request, db: Session):
    auth_header = request.headers.get('Authorization')
    if not auth_header: return None
    try:
        token = auth_header.split(" ")[1]
        from jose import jwt
        from services.auth import SECRET_KEY, ALGORITHM
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        return db.query(models.User).filter(models.User.email == email).first()
    except: return None

def kaydet(db: Session, tip: str, girdi: str, sonuc: str, user_id: int = None):
    try:
        yeni = models.Analysis(user_id=user_id, analysis_type=tip, input_text=girdi, result_text=sonuc)
        db.add(yeni)
        db.commit()
    except: pass

# --- API ---

@app.post("/api/register", response_model=dto.User)
def register(user: dto.UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="E-posta kullanımda.")
    hashed = AuthService.get_password_hash(user.password)
    new_user = models.User(email=user.email, hashed_password=hashed)
    db.add(new_user)
    db.commit()
    return new_user

@app.post("/api/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not AuthService.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Hatalı giriş")
    return {"access_token": AuthService.create_access_token(data={"sub": user.email}), "token_type": "bearer"}

# --- GÜNCELLENMİŞ GEÇMİŞİ GETİRME FONKSİYONU ---
@app.get("/api/users/me")
def get_me(request: Request, db: Session = Depends(get_db)):
    # 1. Kullanıcıyı bul
    user = get_current_user(request, db)
    if not user: 
        raise HTTPException(status_code=401, detail="Oturum yok")
    
    # 2. Analizleri doğrudan tablodan çek (En garantili yöntem)
    # En yeniden en eskiye doğru sırala (desc)
    analizler_db = db.query(models.Analysis).filter(models.Analysis.user_id == user.id).order_by(desc(models.Analysis.id)).all()
    
    # 3. Listeyi manuel oluştur
    analiz_listesi = []
    for a in analizler_db:
        analiz_listesi.append({
            "id": a.id,
            "input_text": a.input_text,
            "result_text": a.result_text,
            "created_at": a.created_at,
            "analysis_type": a.analysis_type
        })
    
    # 4. Paketi gönder
    return {
        "email": user.email,
        "analyses": analiz_listesi
    }
@app.post("/api/isim-analizi-yap")
async def isim_analiz(request: Request, 
                      isim: str = Form(...), 
                      soyisim: str = Form(...), 
                      mentor: str = Form("yahya"), # <--- YENİ EKLENDİ (Varsayılan Yahya)
                      db: Session = Depends(get_db)):
    try:
        tam = f"{isim} {soyisim}".upper()
        # Mentoru parametre olarak gönderiyoruz
        sonuc = AIWriter.generate_name_analysis_rag(tam, mentor)
        
        u = get_current_user(request, db)
        kaydet(db, "ISIM", tam, sonuc, u.id if u else None)
        return {"analiz_sonucu": sonuc}
    except Exception as e: return JSONResponse({"hata": str(e)}, status_code=500)

@app.post("/api/ruya-analizi")
async def ruya_analiz(request: Request, 
                      ruya_metni: str = Form(...), 
                      mentor: str = Form("yahya"), # <--- YENİ EKLENDİ
                      db: Session = Depends(get_db)):
    try:
        # Mentoru parametre olarak gönderiyoruz
        sonuc = AIWriter.ruya_tabiri_motoru(ruya_metni, mentor)
        
        u = get_current_user(request, db)
        kaydet(db, "RUYA", ruya_metni, sonuc, u.id if u else None)
        return {"analiz": sonuc}
    except Exception as e: return JSONResponse({"analiz": str(e)}, status_code=500)

# --- BLOG API ---
@app.get("/api/blog/posts")
def get_posts(db: Session = Depends(get_db)):
    try:
        posts = db.query(BlogPost).order_by(desc(BlogPost.created_at)).all()
        # Otomatik çeviriciye güvenme, veriyi elle listeye dök
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
    except Exception as e:
        print(f"BLOG LISTE HATASI: {e}")
        return []
@app.get("/api/blog/posts/{slug}")
def get_post_detail(slug: str, db: Session = Depends(get_db)):
    clean_slug = slug.strip().split("?")[0]
    
    post = db.query(BlogPost).filter(BlogPost.slug == clean_slug).first()
    
    if not post: 
        raise HTTPException(status_code=404, detail="Yazı bulunamadı")
    
    # Görüntülenmeyi artır
    post.views += 1
    db.commit()
    
    # MANUEL PAKETLEME (Verinin kaybolmasını engeller)
    return {
        "id": post.id,
        "title": post.title,
        "slug": post.slug,
        "content": post.content,
        "image_url": post.image_url,
        "created_at": post.created_at,
        "views": post.views
    }
# --- PYDANTIC MODELLERİ (VERİ PAKETLEME İÇİN) ---
class AnalysisSchema(BaseModel):
    id: int
    analysis_type: str
    input_text: str
    result_text: str
    created_at: datetime

    class Config:
        orm_mode = True

class UserWithHistory(BaseModel):
    email: str
    analyses: List[AnalysisSchema] = []

    class Config:
        orm_mode = True
@app.post("/api/admin/blog/create")
def create_post(request: Request, title: str = Form(...), content: str = Form(...), image_url: str = Form(...), db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    if not user or not user.is_admin: raise HTTPException(status_code=403, detail="Yetkisiz")
    
    # 🧼 SLUG TEMİZLİK ROBOTU
    # 1. Türkçe karakterleri düzelt
    slug = title.lower().replace(" ", "-").replace("ı","i").replace("ğ","g").replace("ü","u").replace("ş","s").replace("ö","o").replace("ç","c")
    # 2. Sadece harf, rakam ve tire (-) bırak. Soru işareti (?) dahil her şeyi sil.
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    # 3. Fazla tireleri sil
    slug = re.sub(r'-+', '-', slug).strip('-')
    
    try:
        new_post = BlogPost(title=title, content=content, image_url=image_url, slug=slug)
        db.add(new_post)
        db.commit()
        return {"durum": "BAŞARILI", "slug": slug}
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": f"Kayıt Hatası: {str(e)}"})

# --- BLOG YAZILARINI GETİREN API (Halka Açık) ---
@app.get("/api/posts")
def get_public_posts(db: Session = Depends(get_db)):
    # En son eklenen en üstte görünsün diye (desc) sıralıyoruz
    posts = db.query(BlogPost).order_by(BlogPost.id.desc()).all()
    return posts
    
@app.delete("/api/admin/blog/delete/{id}")
def delete_post(id: int, request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    if not user or not user.is_admin: raise HTTPException(status_code=403, detail="Yetkisiz")
    db.query(BlogPost).filter(BlogPost.id == id).delete()
    db.commit()
    return {"durum": "SİLİNDİ"}

# --- ADMIN STATS ---
@app.get("/api/admin/stats")
def get_stats(request: Request, db: Session = Depends(get_db)):
    admin = get_current_user(request, db)
    if not admin or not admin.is_admin: raise HTTPException(status_code=403, detail="Yetkisiz")
    
    try:
        return {
            "total_users": db.query(models.User).count(),
            "total_analysis": db.query(models.Analysis).count(),
            "total_posts": db.query(BlogPost).count(),
            "activities": [] 
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": f"Stats Hatası: {str(e)}"})

# --- DB REPAIR ---
@app.get("/api/db-repair")
def repair_db():
    try:
        models.Base.metadata.create_all(bind=engine)
        return "Tablolar (BlogPost dahil) garantiye alındı."
    except Exception as e:
        return f"Hata: {e}"

# --- SAYFALAR ---
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