# from ebced.yil_etkisi import yil_etkisi
# from fastapi import FastAPI
# from api.analiz_endpoint import router as analiz_router
# from ebced.yapi_yorumlari import yapi_yorumlari

# app = FastAPI()

# app.include_router(analiz_router)

# kisi_element = {
#     "Ateş": 3,
#     "Su": 1,
#     "Hava": 0,
#     "Toprak": 2
# }

# yil_element = "Ateş"

# yorumlar = yil_etkisi(kisi_element, yil_element)

# yapi = yapi_yorumlari(kisi_element)
# yil = yil_etkisi(kisi_element, yil_element)

# tum_yorumlar = yapi + yil






# from fastapi import FastAPI
# from schemas.analysis import AnalysisRequest, AnalysisResponse
# from services.calculator import EbcedCalculator
# from services.interpreter import Analyzer

# app = FastAPI(title="İnsan Ekspertizi API v2")

# @app.post("/analyze", response_model=AnalysisResponse)
# def analyze_person(request: AnalysisRequest):
#     # 1. Hesapla
#     calc_result = EbcedCalculator.calculate_name(request.name)
#     year_elem = EbcedCalculator.calculate_year_element(request.current_year)
    
#     # 2. Yorumla
#     comments = Analyzer.generate_comments(
#         user_elements=calc_result["elements"],
#         dominant_element=calc_result["dominant_element"],
#         year_element=year_elem
#     )
    
#     # 3. Döndür
#     return {
#         "ebced_score": calc_result["ebced_score"],
#         "dominant_element": calc_result["dominant_element"],
#         "year_element": year_elem,
#         "comments": comments
#     }

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)



# # backend/main.py
# from fastapi import FastAPI
# from schemas.analysis import AnalizIstegi, AnalizSonucu
# from services.calculator import EbcedCalculator
# from services.interpreter import Interpreter

# app = FastAPI(title="Ebced Analiz API - V2")

# @app.post("/analiz-yap", response_model=AnalizSonucu)
# def analiz_endpoint(istek: AnalizIstegi):
#     # 1. İsim ve Soyismi Birleştir
#     tam_isim = f"{istek.isim} {istek.soyisim}"
    
#     # 2. Hesaplamaları Yap (Calculator Servisi)
#     ebced_degeri = EbcedCalculator.calculate_ebced(tam_isim)
#     kisi_elementi = EbcedCalculator.find_dominant_element(ebced_degeri)
#     yil_elementi = EbcedCalculator.calculate_year_element(istek.mevcut_yil)
    
#     # Not: Şimdilik element puanlarını basit tutuyoruz, 
#     # ileride harf harf analiz ekleyeceğiz.
#     element_puanlari = {kisi_elementi: 4} # Örnek veri
    
#     # 3. Yorumları Üret (Interpreter Servisi)
#     yorumlar = Interpreter.generate_comments(kisi_elementi, yil_elementi)
    
#     # 4. Cevabı Paketle ve Gönder
#     return {
#         "tam_isim": tam_isim,
#         "ebced_degeri": ebced_degeri,
#         "kisi_elementi": kisi_elementi,
#         "yil_elementi": yil_elementi,
#         "element_puanlari": element_puanlari,
#         "yorumlar": yorumlar
#     }

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)



# # backend/main.py
# from fastapi import FastAPI
# from schemas.analysis import AnalizIstegi, AnalizSonucu
# from services.calculator import EbcedCalculator
# from services.interpreter import Interpreter

# app = FastAPI(title="İnsan Ekspertizi - Ebced Pro")

# @app.post("/analiz-yap", response_model=AnalizSonucu)
# def analiz_endpoint(istek: AnalizIstegi):
#     # 1. Hazırlık
#     tam_isim = f"{istek.isim} {istek.soyisim}"
    
#     # 2. Hesaplamalar (Sırasıyla)
#     # A. Ebced Hesabı
#     ebced_degeri = EbcedCalculator.calculate_ebced(tam_isim)
    
#     # B. Pin Kodu Hesabı
#     pin_kodu = EbcedCalculator.calculate_pin_code(ebced_degeri, istek.dogum_yili)
    
#     # C. Element Puanlama (Karmaşık Mantık)
#     element_puanlari = EbcedCalculator.calculate_element_distribution(ebced_degeri, pin_kodu)
    
#     # D. Baskın Element ve Yıl Elementi
#     kisi_elementi = EbcedCalculator.get_dominant_element(element_puanlari)
#     yil_elementi = EbcedCalculator.calculate_year_element(istek.mevcut_yil)
    
#     # 3. Yorumlama
#     yorumlar = Interpreter.generate_comments(
#         kisi_element: kisi_elementi, 
#         yil_element: yil_elementi,
#         element_skorlari: element_puanlari # Artık skorları da gönderebiliriz
#     )
    
#     # 4. Sonuç
#     return {
#         "tam_isim": tam_isim,
#         "ebced_degeri": ebced_degeri,
#         "kisi_elementi": kisi_elementi,
#         "yil_elementi": yil_elementi,
#         "element_puanlari": element_puanlari,
#         "yorumlar": yorumlar
#     }

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)


# # backend/main.py
# from fastapi import FastAPI
# from schemas.analysis import AnalizIstegi, AnalizSonucu
# from services.calculator import EbcedCalculator
# from services.interpreter import Interpreter

# app = FastAPI(title="İnsan Ekspertizi - Ebced Pro")

# @app.post("/analiz-yap", response_model=AnalizSonucu)
# def analiz_endpoint(istek: AnalizIstegi):
#     # 1. Hazırlık
#     tam_isim = f"{istek.isim} {istek.soyisim}"
    
#     # 2. Hesaplamalar (Sırasıyla)
#     # A. Ebced Hesabı
#     ebced_degeri = EbcedCalculator.calculate_ebced(tam_isim)
    
#     # B. Pin Kodu Hesabı
#     pin_kodu = EbcedCalculator.calculate_pin_code(ebced_degeri, istek.dogum_yili)
    
#     # C. Element Puanlama (Karmaşık Mantık)
#     element_puanlari = EbcedCalculator.calculate_element_distribution(ebced_degeri, pin_kodu)
    
#     # D. Baskın Element ve Yıl Elementi
#     kisi_elementi = EbcedCalculator.get_dominant_element(element_puanlari)
#     yil_elementi = EbcedCalculator.calculate_year_element(istek.mevcut_yil)
    
#     # 3. Yorumlama (DÜZELTME BURADA: : yerine = kullandık)
#     yorumlar = Interpreter.generate_comments(
#         kisi_element=kisi_elementi, 
#         yil_element=yil_elementi,
#         element_skorlari=element_puanlari
#     )
    
#     # 4. Sonuç
#     return {
#         "tam_isim": tam_isim,
#         "ebced_degeri": ebced_degeri,
#         "kisi_elementi": kisi_elementi,
#         "yil_elementi": yil_elementi,
#         "element_puanlari": element_puanlari,
#         "yorumlar": yorumlar
#     }

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

# from fastapi import FastAPI
# from schemas.analysis import AnalizIstegi, AnalizSonucu, IliskiAnaliziIstegi, IliskiAnaliziSonucu, KisiBilgisi
# from services.calculator import EbcedCalculator
# from services.interpreter import Interpreter
# from core.constants import YASAM_YOLU_ANALIZLERI, KISISEL_YIL_ANALIZLERI, BEREKET_SAYISI_OZET
# from datetime import datetime

# app = FastAPI(title="İnsan Ekspertizi - Full Sistem (Ders 18 Final)")

# def analyze_person_data(kisi_adi, kisi_soyadi, kisi_anne, gun, ay, yil, mevcut_yil):
#     tam_isim = f"{kisi_adi} {kisi_soyadi}"
#     analiz_metni = f"{kisi_adi} {kisi_soyadi} {kisi_anne}"
    
#     pin = EbcedCalculator.calculate_pin_code(kisi_adi, kisi_soyadi, kisi_anne)
#     cakra = EbcedCalculator.analyze_chakras(analiz_metni)
#     lp = EbcedCalculator.calculate_life_path(gun, ay, yil)
#     py = EbcedCalculator.calculate_personal_year(gun, ay, mevcut_yil)
    
#     baskin_cakra_val = max(cakra["raw_counts"], key=cakra["raw_counts"].get)
#     donusum_katmanlari = EbcedCalculator.calculate_transformation_layers(py, pin, baskin_cakra_val)
#     element_skorlari = EbcedCalculator.analyze_elements(tam_isim)
#     isim_esma_idx = EbcedCalculator.calculate_name_esma_index(kisi_adi)
#     harf_ozellikleri = EbcedCalculator.analyze_letter_attributes(tam_isim)
#     element_dengesizligi = EbcedCalculator.detect_element_imbalance(element_skorlari)
    
#     name_pin = EbcedCalculator.calculate_name_only_pin(kisi_adi)
#     surname_pin = EbcedCalculator.calculate_surname_only_pin(kisi_soyadi)
#     birth_year_pin = EbcedCalculator.calculate_birth_year_pin(yil)
#     year_element = EbcedCalculator.calculate_year_element_pin(mevcut_yil)
    
#     bereket_iliski = EbcedCalculator.calculate_abundance_number_for_relationship(kisi_adi, kisi_soyadi, kisi_anne)
#     esas_bereket = EbcedCalculator.calculate_esas_bereket(kisi_adi, kisi_soyadi)
#     dongu_bereket = EbcedCalculator.calculate_dongu_bereket(gun, ay)
    
#     return {
#         "pin": pin, "cakra": cakra, "life_path": lp, "personal_year": py, 
#         "donusum_katmanlari": donusum_katmanlari,
#         "element_skorlari": element_skorlari,
#         "element_dengesizligi": element_dengesizligi,
#         "isim_esma_idx": isim_esma_idx,
#         "harf_ozellikleri": harf_ozellikleri,
#         "baskin_cakra_val": baskin_cakra_val,
#         "bereket": bereket_iliski, "esas_bereket": esas_bereket, "dongu_bereket": dongu_bereket,
#         "tam_isim": tam_isim,
#         "name_pin": name_pin, "surname_pin": surname_pin, "birth_year_pin": birth_year_pin,
#         "year_element": year_element
#     }

# @app.post("/analiz-yap", response_model=AnalizSonucu)
# def tekil_analiz(istek: AnalizIstegi):
#     data = analyze_person_data(istek.isim, istek.soyisim, istek.anne_adi, 
#                                istek.dogum_gunu, istek.dogum_ayi, istek.dogum_yili, istek.mevcut_yil)
    
#     pin_detay = Interpreter.generate_pin_report(data["pin"])
#     cakra_rapor = Interpreter.generate_full_chakra_report(data["cakra"])
#     lp_data = YASAM_YOLU_ANALIZLERI.get(data["life_path"], {})
#     py_yorum = KISISEL_YIL_ANALIZLERI.get(data["personal_year"], "-")
#     ozel_kombinasyon = Interpreter.analyze_combination(data["pin"], data["life_path"])
#     bereket_raporu = Interpreter.generate_abundance_report(data["esas_bereket"], data["dongu_bereket"])
    
#     donusum_raporu = Interpreter.generate_transformation_report(
#         istek.mevcut_yil,
#         data["personal_year"],
#         data["donusum_katmanlari"]["pin_multiplier"],
#         data["donusum_katmanlari"]["chakra_multiplier"]
#     )
    
#     element_raporu = Interpreter.generate_element_report(data["element_skorlari"])
    
#     esma_raporu = Interpreter.generate_esma_sure_report(
#         data["life_path"],
#         data["isim_esma_idx"],
#         cakra_rapor["zayif_cakra_val"]
#     )
    
#     enerji_mimarisi = Interpreter.generate_energy_architecture(
#         data["pin"], 
#         data["baskin_cakra_val"], 
#         element_raporu["baskin_element"]
#     )
    
#     mizac_yasam_tarzi = Interpreter.generate_lifestyle_advice(element_raporu["baskin_element"])
#     operasyonel_analiz = Interpreter.generate_operational_analysis(data["pin"])
#     harf_analiz_raporu = Interpreter.generate_letter_analysis_report(data["harf_ozellikleri"])
#     frekans_raporu = Interpreter.generate_frequency_adjustment_report(data["element_dengesizligi"])
    
#     eksik_elementler = [el for el, skor in data["element_skorlari"].items() if skor == 0]
    
#     alan_aktivasyon_raporu = Interpreter.generate_field_activation_report(
#         data["name_pin"], data["surname_pin"], data["birth_year_pin"],
#         data["year_element"], element_raporu["baskin_element"], eksik_elementler
#     )
    
#     element_alan_raporu = Interpreter.generate_element_field_analysis(
#         element_raporu["baskin_element"],
#         data["year_element"],
#         eksik_elementler
#     )
    
#     now = datetime.now()
#     gun_val = istek.mevcut_gun if istek.mevcut_gun else now.day
#     ay_val = istek.mevcut_ay if istek.mevcut_ay else now.month
#     yil_val = istek.mevcut_yil if istek.mevcut_yil else now.year
#     gun_tarihi_str = f"{gun_val}/{ay_val}/{yil_val}"
    
#     gun_titresimi = EbcedCalculator.calculate_current_day_vibration(gun_val)
#     gun_analiz_raporu = Interpreter.generate_day_analysis(
#         gun_titresimi, 
#         element_raporu["baskin_element"], 
#         gun_tarihi_str
#     )
    
#     refleks_raporu = Interpreter.generate_reflex_report(data["element_skorlari"])
    
#     # DERS 18: Enerji Uygulama Planı
#     enerji_uygulama_raporu = Interpreter.generate_energy_practice_guide(data["element_skorlari"])
    
#     ozet = Interpreter.generate_summary(pin_detay, lp_data, donusum_raporu)
    
#     return {
#         "tam_isim": data["tam_isim"],
#         "pin_kodu": data["pin"],
#         "pin_arketipler": pin_detay,
#         "cakra_tablosu": data["cakra"]["readable_counts"],
#         "cakra_detaylari": cakra_rapor["detayli_rapor"],
#         "baskin_element": cakra_rapor["baskin_element"],
#         "baskin_gezegen": cakra_rapor["baskin_gezegen"],
#         "yasam_yolu_sayisi": data["life_path"],
#         "yasam_yolu_detay": lp_data,
#         "kisisel_yil_sayisi": data["personal_year"],
#         "kisisel_yil_yorumu": py_yorum,
#         "ozel_kombinasyon": ozel_kombinasyon,
#         "bereket_sayisi": data["esas_bereket"],
#         "bereket_yorumu": bereket_raporu["esas_detay"]["baslik"],
#         "para_analizi": {
#             "esas_bereket_sayisi": data["esas_bereket"],
#             "esas_bereket_detay": bereket_raporu["esas_detay"],
#             "dongu_bereket_sayisi": data["dongu_bereket"],
#             "dongu_bereket_detay": bereket_raporu["dongu_detay"],
#             "finansal_yorum": bereket_raporu["finansal_yorum"]
#         },
#         "donusum_yili_analizi": donusum_raporu,
#         "element_mizac_analizi": element_raporu,
#         "esma_sure_analizi": esma_raporu,
#         "enerji_mimarisi": enerji_mimarisi,
#         "mizac_yasam_tarzi": mizac_yasam_tarzi,
#         "operasyonel_analiz": operasyonel_analiz,
#         "harf_analizi": harf_analiz_raporu,
#         "frekans_analizi": frekans_raporu,
#         "alan_aktivasyonu_analizi": alan_aktivasyon_raporu,
#         "element_alan_analizi": element_alan_raporu,
#         "gun_analizi": gun_analiz_raporu,
#         "refleks_analizi": refleks_raporu,
#         "enerji_uygulama_plani": enerji_uygulama_raporu,
        
#         "yorumlar": ozet
#     }

# @app.post("/iliski-analizi", response_model=IliskiAnaliziSonucu)
# def iliski_analizi(istek: IliskiAnaliziIstegi):
#     p1 = analyze_person_data(istek.kisi1.isim, istek.kisi1.soyisim, istek.kisi1.anne_adi, 
#                              istek.kisi1.dogum_gunu, istek.kisi1.dogum_ayi, istek.kisi1.dogum_yili, istek.mevcut_yil)
#     p2 = analyze_person_data(istek.kisi2.isim, istek.kisi2.soyisim, istek.kisi2.anne_adi, 
#                              istek.kisi2.dogum_gunu, istek.kisi2.dogum_ayi, istek.kisi2.dogum_yili, istek.mevcut_yil)
    
#     sonuc = Interpreter.analyze_relationship(p1, p2)
#     detay = sonuc["detaylar"]
    
#     return {
#         "kisi1_ad": p1["tam_isim"],
#         "kisi2_ad": p2["tam_isim"],
#         "genel_uyum_puani": sonuc["puan"],
#         "pin_uyumu": {"kategori": "Pin", "kisi1_deger": str(detay["pin"]["kisi1"]), "kisi2_deger": str(detay["pin"]["kisi2"]), "analiz": detay["pin"]["analiz"], "puan": detay["pin"]["puan"]},
#         "cakra_uyumu": {"kategori": "Çakra", "kisi1_deger": str(detay["cakra"]["kisi1"]), "kisi2_deger": str(detay["cakra"]["kisi2"]), "analiz": detay["cakra"]["analiz"], "puan": detay["cakra"]["puan"]},
#         "element_uyumu": {"kategori": "Element", "kisi1_deger": str(detay["element"]["kisi1"]), "kisi2_deger": str(detay["element"]["kisi2"]), "analiz": detay["element"]["analiz"], "puan": detay["element"]["puan"]},
#         "yasam_yolu_uyumu": {"kategori": "Yaşam Yolu", "kisi1_deger": str(detay["lp"]["kisi1"]), "kisi2_deger": str(detay["lp"]["kisi2"]), "analiz": detay["lp"]["analiz"], "puan": detay["lp"]["puan"]},
#         "bereket_uyumu": {"kategori": "Bereket", "kisi1_deger": str(detay["bereket"]["kisi1"]), "kisi2_deger": str(detay["bereket"]["kisi2"]), "analiz": detay["bereket"]["analiz"], "puan": detay["bereket"]["puan"]},
#         "ozet_yorum": sonuc["ozet"],
#         "tavsiyeler": sonuc["tavsiyeler"]
#     }

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
# --- BU KISIMDAKİ IMPORTLARDA HATA ALIRSAN TERMİNAL SANA SÖYLEYECEK ---
# backend/main.py
from fastapi import FastAPI, Depends, HTTPException, status, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from datetime import timedelta
from pydantic import BaseModel
import uvicorn
import os
import sys

# --- MODÜL YOLLARI ---
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# --- KENDİ MODÜLLERİMİZ ---
from database import engine, get_db
import models
import schemas
from services.auth import AuthService
from services.ai_writer import AIWriter
from services.calculator import EbcedCalculator
# interpreter, visualizer vb. şu an kullanılmıyorsa import etmeye gerek yok, sade tutalım.

# --- VERİTABANI OLUŞTURMA ---
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="İnsan Ekspertizi API", version="2.0")

# --- GÜVENLİK ---
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")

# --- 1. CORS AYARLARI ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 2. DOSYA YOLLARI ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# --- 3. YARDIMCI FONKSİYONLAR ---

# Kullanıcıyı Token'dan Tanıma
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

# Analizi Veritabanına Kaydetme
def analiz_kaydet(db: Session, tip: str, girdi: str, sonuc: str, user_id: int = None):
    try:
        yeni_analiz = models.Analysis(
            user_id=user_id, # Giriş yapmamışsa None olur
            analysis_type=tip,
            input_text=girdi,
            result_text=sonuc
        )
        db.add(yeni_analiz)
        db.commit()
        print(f"✅ Analiz veritabanına kaydedildi: {tip}")
    except Exception as e:
        print(f"❌ Kayıt Hatası: {str(e)}")

# --- 4. AUTH (ÜYELİK) ENDPOINTLERİ ---

@app.post("/api/register", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Bu e-posta zaten kayıtlı.")
    
    hashed_password = AuthService.get_password_hash(user.password)
    new_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/api/token", response_model=schemas.Token)
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

@app.get("/api/users/me", response_model=schemas.User)
def read_users_me(current_user: models.User = Depends(get_current_user)):
    # Bu endpoint çağrıldığında, schemas.User modelindeki 'analyses' alanı sayesinde
    # kullanıcının geçmiş analizleri de otomatik olarak dönecek.
    return current_user

# --- 5. ANALİZ ENDPOINTLERİ (KAYIT ÖZELLİKLİ) ---

@app.post("/api/isim-analizi-yap")
async def isim_analizi_servisi(
    isim: str = Form(...),
    soyisim: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        tam_isim = f"{isim} {soyisim}".upper()
        
        # Yapay Zeka Motorunu Çalıştır (PDF/RAG yok, name_data.py var)
        analiz_metni = AIWriter.generate_name_analysis_rag(tam_isim)
        
        # Veritabanına Kaydet (Şimdilik User ID None - Misafir)
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

        # Yapay Zeka Motoru
        analiz_sonucu = AIWriter.ruya_tabiri_motoru(ruya_metni)
        
        # Veritabanına Kaydet
        analiz_kaydet(db, "RUYA", ruya_metni, analiz_sonucu, user_id=None)
        
        return JSONResponse({"analiz": analiz_sonucu})
    except Exception as e:
        return JSONResponse({"analiz": f"Hata: {str(e)}"}, status_code=500)

# --- 6. DİĞER API'LER (Mobil/Ebced) ---
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

# --- 7. STATİK SAYFALAR ---
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

# --- DEBUG & BAŞLATMA ---
@app.get("/ajan/model-test")
async def model_test():
    import os
    from google import genai
    api_key = os.getenv("GOOGLE_API_KEY")
    try:
        client = genai.Client(api_key=api_key)
        return {"durum": "BAŞARILI", "mesaj": "API Key çalışıyor"}
    except Exception as e:
        return {"durum": "HATA", "mesaj": str(e)}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)