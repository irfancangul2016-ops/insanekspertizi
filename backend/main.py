import os
import sys
import time
from collections import defaultdict
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Depends, HTTPException, status, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import desc, text
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

# --- 🛡️ GÜVENLİK: RATE LIMITING ---
request_counts = defaultdict(list)
LIMIT_PER_MINUTE = 10
WINDOW_SIZE = 60

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    if request.url.path in ["/api/isim-analizi-yap", "/api/ruya-analizi"]:
        client_ip = request.client.host
        now = time.time()
        request_counts[client_ip] = [t for t in request_counts[client_ip] if now - t < WINDOW_SIZE]
        if len(request_counts[client_ip]) >= LIMIT_PER_MINUTE:
            return JSONResponse(status_code=429, content={"analiz": "✋ Çok hızlı gidiyorsun! 1 dakika bekle."})
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
        user = db.query(models.User).filter(models.User.email == email).first()
        return user
    except:
        return None

def kaydet(db: Session, tip: str, girdi: str, sonuc: str, user_id: int = None):
    try:
        yeni = models.Analysis(user_id=user_id, analysis_type=tip, input_text=girdi, result_text=sonuc)
        db.add(yeni)
        db.commit()
    except Exception as e:
        print(f"Kayıt Hatası: {e}")

# --- API UÇLARI ---

@app.post("/api/register", response_model=dto.User)
def register(user: dto.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user: raise HTTPException(status_code=400, detail="E-posta kullanımda.")
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
    if not user: raise HTTPException(status_code=401, detail="Oturum yok")
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

# --- 📰 BLOG API (YENİ) ---

@app.get("/api/blog/posts")
def get_posts(db: Session = Depends(get_db)):
    # En yeniden eskiye doğru getir
    return db.query(models.BlogPost).order_by(desc(models.BlogPost.created_at)).all()

@app.get("/api/blog/posts/{slug}")
def get_post_detail(slug: str, db: Session = Depends(get_db)):
    post = db.query(models.BlogPost).filter(models.BlogPost.slug == slug).first()
    if not post: raise HTTPException(status_code=404, detail="Yazı bulunamadı")
    # Görüntülenmeyi artır
    post.views += 1
    db.commit()
    return post

@app.post("/api/admin/blog/create")
def create_post(request: Request, title: str = Form(...), content: str = Form(...), image_url: str = Form(...), db: Session = Depends(get_db)):
    # Sadece Admin
    user = get_current_user(request, db)
    if not user or not user.is_admin: raise HTTPException(status_code=403, detail="Yetkisiz")
    
    # Slug oluştur (Basitçe: Türkçe karakterleri at, tire koy)
    slug = title.lower().replace(" ", "-").replace("ı","i").replace("ğ","g").replace("ü","u").replace("ş","s").replace("ö","o").replace("ç","c")
    
    new_post = models.BlogPost(title=title, content=content, image_url=image_url, slug=slug)
    db.add(new_post)
    db.commit()
    return {"durum": "BAŞARILI", "slug": slug}

@app.delete("/api/admin/blog/delete/{id}")
def delete_post(id: int, request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    if not user or not user.is_admin: raise HTTPException(status_code=403, detail="Yetkisiz")
    
    post = db.query(models.BlogPost).filter(models.BlogPost.id == id).first()
    if post:
        db.delete(post)
        db.commit()
    return {"durum": "SİLİNDİ"}

# --- ADMIN ISTATISTIK GUNCELLEME ---
@app.get("/api/admin/stats")
def get_stats(request: Request, db: Session = Depends(get_db)):
    admin = get_current_user(request, db)
    if not admin or not admin.is_admin: raise HTTPException(status_code=403, detail="Yetkisiz")
    
    total_users = db.query(models.User).count()
    total_analysis = db.query(models.Analysis).count()
    total_posts = db.query(models.BlogPost).count() # Blog sayısı
    
    recent_activity = db.query(models.Analysis).order_by(desc(models.Analysis.id)).limit(50).all()
    
    activity_list = []
    for item in recent_activity:
        owner_email = item.owner.email if item.owner else "Misafir"
        activity_list.append({
            "id": item.id, "type": item.analysis_type, "input": item.input_text, 
            "result": item.result_text[:50]+"...", "user": owner_email, 
            "date": item.created_at.strftime("%d.%m.%Y %H:%M")
        })
        
    return {"total_users": total_users, "total_analysis": total_analysis, "total_posts": total_posts, "activities": activity_list}

# --- SEO & PAGE ROUTES ---

@app.get("/robots.txt", response_class=FileResponse)
def robots_txt():
    with open("robots.txt", "w") as f:
        f.write("User-agent: *\nAllow: /\nSitemap: https://insanekspertizi.org/sitemap.xml")
    return FileResponse("robots.txt")

@app.get("/sitemap.xml", response_class=FileResponse)
def sitemap_xml(db: Session = Depends(get_db)):
    # Dinamik Sitemap (Blog yazılarını da ekler)
    posts = db.query(models.BlogPost).all()
    urls = ""
    for post in posts:
        urls += f"<url><loc>https://insanekspertizi.org/blog/{post.slug}</loc><priority>0.8</priority></url>\n"
        
    content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url><loc>https://insanekspertizi.org/</loc><priority>1.0</priority></url>
   {urls}
</urlset>"""
    with open("sitemap.xml", "w") as f: f.write(content)
    return FileResponse("sitemap.xml")

@app.get("/admin")
def admin_panel():
    path = os.path.join(STATIC_DIR, "admin.html")
    if os.path.exists(path): return FileResponse(path)
    return "Admin paneli yok"

# Blog Sayfaları (Tek dosya üzerinden çalışacak)
@app.get("/blog/{slug}")
def blog_detail(slug: str):
    # Detay sayfası da aslında blog.html'i açacak, JS ile içeriği çekecek
    path = os.path.join(STATIC_DIR, "blog.html")
    if os.path.exists(path): return FileResponse(path)
    return "Blog sayfası yok"

@app.get("/blog")
def blog_list():
    path = os.path.join(STATIC_DIR, "blog.html")
    if os.path.exists(path): return FileResponse(path)
    return "Blog sayfası yok"

@app.get("/")
def home():
    path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(path): return FileResponse(path)
    return "Sistem Çalışıyor"

@app.get("/api/db-repair")
def repair_database(db: Session = Depends(get_db)):
    try:
        db.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS is_admin BOOLEAN DEFAULT FALSE;"))
        db.commit()
        return {"durum": "BAŞARILI"}
    except Exception as e: return {"durum": "HATA", "mesaj": str(e)}