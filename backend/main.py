import os
import sys
import time
from collections import defaultdict
from datetime import datetime

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

# --- 🛠️ BYPASS AMELİYATI: BLOG SINIFINI BURADA TANIMLIYORUZ ---
# Veritabanı dosyası inat ettiği için tabloyu burada oluşturuyoruz.
class BlogPost(models.Base):
    __tablename__ = "blog_posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    slug = Column(String, unique=True, index=True)
    content = Column(Text)
    image_url = Column(String)
    views = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

# Tabloları Garanti Oluştur
models.Base.metadata.create_all(bind=engine)

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

@app.get("/api/users/me")
def get_me(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    if not user: raise HTTPException(status_code=401, detail="Oturum yok")
    return user

@app.post("/api/isim-analizi-yap")
async def isim_analiz(request: Request, isim: str = Form(...), soyisim: str = Form(...), db: Session = Depends(get_db)):
    try:
        tam = f"{isim} {soyisim}".upper()
        sonuc = AIWriter.generate_name_analysis_rag(tam)
        u = get_current_user(request, db)
        kaydet(db, "ISIM", tam, sonuc, u.id if u else None)
        return {"analiz_sonucu": sonuc}
    except Exception as e: return JSONResponse({"hata": str(e)}, status_code=500)

@app.post("/api/ruya-analizi")
async def ruya_analiz(request: Request, ruya_metni: str = Form(...), db: Session = Depends(get_db)):
    try:
        sonuc = AIWriter.ruya_tabiri_motoru(ruya_metni)
        u = get_current_user(request, db)
        kaydet(db, "RUYA", ruya_metni, sonuc, u.id if u else None)
        return {"analiz": sonuc}
    except Exception as e: return JSONResponse({"analiz": str(e)}, status_code=500)

# --- BLOG API (ARTIK LOCAL CLASS KULLANIYOR) ---
@app.get("/api/blog/posts")
def get_posts(db: Session = Depends(get_db)):
    try:
        # models.BlogPost yerine direkt BlogPost kullanıyoruz
        return db.query(BlogPost).order_by(desc(BlogPost.created_at)).all()
    except Exception as e:
        print(f"BLOG HATASI: {e}")
        return JSONResponse(status_code=500, content={"detail": f"Veritabanı Hatası: {str(e)}"})

@app.get("/api/blog/posts/{slug}")
def get_post_detail(slug: str, db: Session = Depends(get_db)):
    post = db.query(BlogPost).filter(BlogPost.slug == slug).first()
    if not post: raise HTTPException(status_code=404, detail="Yazı yok")
    post.views += 1
    db.commit()
    return post

@app.post("/api/admin/blog/create")
def create_post(request: Request, title: str = Form(...), content: str = Form(...), image_url: str = Form(...), db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    if not user or not user.is_admin: raise HTTPException(status_code=403, detail="Yetkisiz")
    
    slug = title.lower().replace(" ", "-").replace("ı","i").replace("ğ","g").replace("ü","u").replace("ş","s").replace("ö","o").replace("ç","c")[:50]
    
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