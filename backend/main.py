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
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel
import uvicorn
import os

# Servislerimizi çağırıyoruz
from services.calculator import EbcedCalculator
from services.interpreter import Interpreter
from services.visualizer import Visualizer
from services.pdf_generator import PDFGenerator
from services.ai_writer import AIWriter
from services.database import Database # <--- Veritabanı modülü

app = FastAPI()

# Statik dosyalar (CSS, Resimler, PDF'ler) için yol tanımı
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

class AnalizIstegi(BaseModel):
    isim: str
    soyisim: str
    dogum_gun: int
    dogum_ay: int
    dogum_yil: int
    anne_adi: str

@app.get("/", response_class=HTMLResponse)
async def ana_sayfa():
    with open("backend/static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/rapor-olustur")
async def rapor_olustur(
    isim: str = Form(...),
    soyisim: str = Form(...),
    dogum_gun: int = Form(...),
    dogum_ay: int = Form(...),
    dogum_yil: int = Form(...),
    anne_adi: str = Form(...)
):
    print(f"--> Analiz İsteği Geldi: {isim} {soyisim}")
    
    # Verileri bir sınıf yapısında toplayalım (Kolaylık olsun diye)
    istek = AnalizIstegi(
        isim=isim, soyisim=soyisim, 
        dogum_gun=dogum_gun, dogum_ay=dogum_ay, dogum_yil=dogum_yil, 
        anne_adi=anne_adi
    )

    try:
        # 1. HESAPLAMALAR (Calculator)
        pin = EbcedCalculator.calculate_pin_code(istek.isim, istek.soyisim, istek.anne_adi)
        life_path = EbcedCalculator.calculate_life_path(istek.dogum_gun, istek.dogum_ay, istek.dogum_yil)
        personal_year = EbcedCalculator.calculate_personal_year(istek.dogum_gun, istek.dogum_ay, 2026) # 2026 varsayılan
        element_skorlari = EbcedCalculator.analyze_elements(istek.isim + istek.soyisim)
        cakra = EbcedCalculator.analyze_chakras(istek.isim + istek.soyisim)
        esma_idx = EbcedCalculator.calculate_name_esma_index(istek.isim)
        
        # 2. YORUMLAMA (Interpreter)
        # Ham verileri yorumlanmış metinlere çeviriyoruz
        analiz_sonucu = {
            "isim": istek.isim,
            "soyisim": istek.soyisim,
            "pin": pin,
            "life_path": life_path,
            "personal_year": personal_year,
            "element_skorlari": element_skorlari,
            "cakra_analizi": cakra,
            "mevcut_yil": 2026,
            "isim_esma_idx": esma_idx,
            # Element ve Çakra Dengesi Tespiti
            "baskin_element": max(element_skorlari, key=element_skorlari.get),
            "eksik_element": min(element_skorlari, key=element_skorlari.get),
            "frekans_durumu": EbcedCalculator.detect_element_imbalance(element_skorlari),
            "zayif_cakra_val": sorted(cakra["raw_counts"].items(), key=lambda x: x[1])[0][0], # En az puanlı çakra
            "baskin_cakra_val": sorted(cakra["raw_counts"].items(), key=lambda x: x[1], reverse=True)[0][0]
        }
        
        tam_isim = f"{istek.isim} {istek.soyisim}"

        # 3. GRAFİKLER VE QR KOD (Visualizer)
        viz = Visualizer()
        dosya_eki = f"{istek.isim}_{istek.soyisim}".replace(" ", "_")
        
        # --- BURAYA KENDİ LİNKİNİ YAZ ---
        SENIN_LINKIN = "https://www.instagram.com/insanekspertizi/"  # Müşteri buna gidecek
        
        try:
            c1 = viz.create_element_chart(element_skorlari, filename_prefix=dosya_eki)
            c2 = viz.create_chakra_radar(cakra["raw_counts"], filename_prefix=dosya_eki)
            qr_kod = viz.create_qr(SENIN_LINKIN, filename_prefix=dosya_eki)
        except Exception as viz_err:
            print(f"Grafik Hatası: {viz_err}")
            c1, c2, qr_kod = None, None, None

        # 4. AI RAPORU (Yapay Zeka)
        analiz_sonucu["tam_isim"] = tam_isim
        ai_raporu = AIWriter.generate_human_report(analiz_sonucu)

        # 5. PDF HAZIRLIĞI VE OLUŞTURMA (PDFGenerator)
        pdf_verisi = Interpreter.generate_full_report_text(analiz_sonucu)
        
        # Ekstraları PDF verisine gömüyoruz
        pdf_verisi["recete"]["yasakli_davranislar"] = ai_raporu
        pdf_verisi["danisan_bilgisi"] = tam_isim
        
        if c1: pdf_verisi["tespit"]["element_chart_path"] = c1
        if c2: pdf_verisi["tespit"]["chakra_chart_path"] = c2
        if qr_kod: pdf_verisi["recete"]["qr_code_path"] = qr_kod

        # PDF OLUŞTURUYORUZ (Bu satır 'pdf_yolu' değişkenini yaratır!)
        generator = PDFGenerator(filename=f"Analiz_{dosya_eki}.pdf")
        pdf_yolu = generator.create_report(pdf_verisi)

        # 6. VERİTABANINA KAYIT (KARA KUTU)
        # Bu işlem PDF oluşturulduktan sonra yapılmalı
        try:
            db = Database()
            kayit_verisi = {
                "isim": istek.isim,
                "soyisim": istek.soyisim,
                "gun": istek.dogum_gun,
                "ay": istek.dogum_ay,
                "yil": istek.dogum_yil,
                "pin": analiz_sonucu.get("pin"),
                "baskin_element": analiz_sonucu.get("baskin_element"),
                "eksik_element": analiz_sonucu.get("eksik_element")
            }
            db.kayit_ekle(kayit_verisi)
        except Exception as e:
            print(f"Veritabanı Kayıt Hatası: {e}")

        # 7. DOSYAYI İNDİRTME
        if pdf_yolu and os.path.exists(pdf_yolu):
            print(f"--> Başarılı! PDF: {pdf_yolu}")
            return FileResponse(pdf_yolu, media_type='application/pdf', filename=f"Analiz_{dosya_eki}.pdf")
        else:
            return {"hata": "PDF oluşturulamadı."}

    except Exception as e:
        print(f"Genel Hata: {str(e)}")
        import traceback
        traceback.print_exc()
        return {"hata": f"Bir şeyler ters gitti: {str(e)}"}

# --- PATRON KAPISI (Admin Paneli) ---
@app.get("/patron/musteri-listesi", response_class=HTMLResponse)
async def admin_paneli():
    """
    Sadece senin görebileceğin basit bir admin paneli.
    Veritabanındaki tüm kayıtları tablo olarak basar.
    """
    db = Database()
    kayitlar = db.tum_kayitlari_getir()
    
    html_content = """
    <html>
        <head>
            <title>Kozmik Hafıza - Müşteri Defteri</title>
            <style>
                body { font-family: Arial, sans-serif; padding: 20px; background-color: #f1f5f9; }
                h1 { color: #1e293b; text-align: center; }
                table { width: 100%; border-collapse: collapse; background: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
                th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
                th { background-color: #3b82f6; color: white; }
                tr:hover { background-color: #f8fafc; }
                .badge { padding: 4px 8px; border-radius: 4px; font-size: 0.8em; font-weight: bold; }
                .fire { background: #fee2e2; color: #991b1b; }
                .water { background: #dbeafe; color: #1e40af; }
                .earth { background: #dcfce7; color: #166534; }
                .air { background: #f3f4f6; color: #1f2937; }
            </style>
        </head>
        <body>
            <h1>📁 MÜŞTERİ KAYIT DEFTERİ</h1>
            <p style="text-align:center;">Toplam Analiz: <b>""" + str(len(kayitlar)) + """</b></p>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Tarih</th>
                    <th>İsim Soyisim</th>
                    <th>Doğum Tarihi</th>
                    <th>Pin Kodu</th>
                    <th>Baskın Element</th>
                    <th>Eksik Element</th>
                </tr>
    """
    
    for k in kayitlar:
        baskin = k['baskin_element']
        style_class = "air"
        if baskin == "ATEŞ": style_class = "fire"
        elif baskin == "SU": style_class = "water"
        elif baskin == "TOPRAK": style_class = "earth"
        
        html_content += f"""
                <tr>
                    <td>{k['id']}</td>
                    <td>{k['tarih']}</td>
                    <td><b>{k['isim']} {k['soyisim']}</b></td>
                    <td>{k['dogum_tarihi']}</td>
                    <td>{k['pin_kodu']}</td>
                    <td><span class="badge {style_class}">{k['baskin_element']}</span></td>
                    <td>{k['eksik_element']}</td>
                </tr>
        """
        
    html_content += """
            </table>
        </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)