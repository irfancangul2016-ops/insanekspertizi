# from google import genai
# import json
# import random

# # --- DİKKAT: API ANAHTARINI BURAYA TIRNAK İÇİNE YAPIŞTIR ---
# # Örnek: "AIzaSyD.......-...."
# MY_API_KEY = "AIzaSyCk8rnVcQJTvzsISo9Prew5TN7iLUWQkuo" 

# # Client'ı başlat
# try:
#     client = genai.Client(api_key=MY_API_KEY)
# except Exception as e:
#     print(f"API Key Hatası: {e}")

# class AIWriter:
#     @staticmethod
#     def generate_human_report(analiz_verisi: dict) -> str:
        
#         # Eğer anahtar girilmemişse uyarı ver
#         if "BURAYA_" in MY_API_KEY or len(MY_API_KEY) < 10:
#             return "HATA: Lütfen services/ai_writer.py dosyasına Google API Key'inizi yapıştırın."

#         tonlar = ["Bilge bir mentör", "Motive edici bir koç", "Derin bir analiz uzmanı"]
#         secilen_ton = random.choice(tonlar)

#         prompt = f"""
#         GÖREV:
#         Sen {secilen_ton} gibi konuşan, 20 yıllık tecrübeye sahip bir uzmansın.
#         Danışana, aşağıdaki teknik verileri yorumlayarak ona özel bir mektup yaz.

#         VERİLER:
#         {json.dumps(analiz_verisi, indent=2, ensure_ascii=False)}

#         KURALLAR:
#         1. Asla kendini tekrar etme.
#         2. Teknik terimleri (Pin, Çakra) açıkla ama hikayeleştir.
#         3. Metni şu 4 başlık altında topla (Başlıkları **BOLD** yaz):
#            I. RUHSAL KİMLİĞİN
#            II. GİZLİ TUZAKLAR
#            III. 2026 KADER PLANI
#            IV. UYGULAMA REÇETESİ
#         4. Çıktı Türkçe olsun.
#         """

#         try:
#             response = client.models.generate_content(
#                 model="gemini-1.5-flash", # Daha hızlı ve kararlı model
#                 contents=prompt
#             )
#             return response.text
#         except Exception as e:
#             return f"Yapay zeka bağlantı hatası: {str(e)}. Lütfen API Key'inizi kontrol edin."


# from google import genai
# import json
# import random

# # --- DİKKAT: API ANAHTARINI BURAYA TIRNAK İÇİNE YAPIŞTIR ---
# # Örnek: "AIzaSyD.......-...."
# MY_API_KEY = "AIzaSyCk8rnVcQJTvzsISo9Prew5TN7iLUWQkuo" 

# # Client'ı başlat
# try:
#     client = genai.Client(api_key=MY_API_KEY)
# except Exception as e:
#     print(f"API Key Hatası: {e}")

# class AIWriter:
#     @staticmethod
#     def generate_human_report(analiz_verisi: dict) -> str:
        
#         # Eğer anahtar girilmemişse uyarı ver
#         if "BURAYA_" in MY_API_KEY or len(MY_API_KEY) < 10:
#             return "HATA: Lütfen services/ai_writer.py dosyasına Google API Key'inizi yapıştırın."

#         tonlar = ["Bilge bir mentör", "Motive edici bir koç", "Derin bir analiz uzmanı"]
#         secilen_ton = random.choice(tonlar)

#         prompt = f"""
#         GÖREV:
#         Sen {secilen_ton} gibi konuşan, 20 yıllık tecrübeye sahip bir uzmansın.
#         Danışana, aşağıdaki teknik verileri yorumlayarak ona özel bir mektup yaz.

#         VERİLER:
#         {json.dumps(analiz_verisi, indent=2, ensure_ascii=False)}

#         KURALLAR:
#         1. Asla kendini tekrar etme.
#         2. Teknik terimleri (Pin, Çakra) açıkla ama hikayeleştir.
#         3. Metni şu 4 başlık altında topla (Başlıkları **BOLD** yaz):
#            I. RUHSAL KİMLİĞİN
#            II. GİZLİ TUZAKLAR
#            III. 2026 KADER PLANI
#            IV. UYGULAMA REÇETESİ
#         4. Çıktı Türkçe olsun.
#         """

#         try:
#             response = client.models.generate_content(
#                 model="gemini-1.5-flash", # Daha hızlı ve kararlı model
#                 contents=prompt
#             )
#             return response.text
#         except Exception as e:
#             return f"Yapay zeka bağlantı hatası: {str(e)}. Lütfen API Key'inizi kontrol edin."













# import os
# import sys
# import requests
# import json
# import importlib.util

# # --- GARANTİLİ MODÜL YÜKLEME ---
# # Bu yöntem, dosya yolunu bulur ve modülü doğrudan kaynağından yükler.
# # ImportError hatasını bypass eder.

# def load_name_data():
#     """name_data.py dosyasını dinamik olarak yükler."""
#     try:
#         # 1. Önce standart yolu dene
#         from services import name_data
#         return name_data
#     except ImportError:
#         try:
#             # 2. Aynı klasörde mi diye bak (Local/Render farkı için)
#             import name_data
#             return name_data
#         except ImportError:
#             # 3. Manuel dosya yolu ile yükle (En garantisi)
#             current_dir = os.path.dirname(os.path.abspath(__file__))
#             file_path = os.path.join(current_dir, "name_data.py")
            
#             spec = importlib.util.spec_from_file_location("name_data", file_path)
#             foo = importlib.util.module_from_spec(spec)
#             sys.modules["name_data"] = foo
#             spec.loader.exec_module(foo)
#             return foo

# # Veri tabanını yükle
# ND = load_name_data()

# # Değişkenleri güvenli bir şekilde çek (Hata verirse boş sözlük ata)
# HARF_DETAYLARI = getattr(ND, "HARF_DETAYLARI", {})
# OZEL_UYARILAR = getattr(ND, "OZEL_UYARILAR", {})
# OZEL_ISIM_ANALIZLERI = getattr(ND, "OZEL_ISIM_ANALIZLERI", {})
# ISIM_VERME_KURALLARI = getattr(ND, "ISIM_VERME_KURALLARI", {})

# class AIWriter:
#     @staticmethod
#     def _find_active_model(api_key):
#         """Google'ın aktif modellerini bulur"""
#         try:
#             url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
#             response = requests.get(url)
#             if response.status_code != 200: return None
#             data = response.json()
#             if 'models' in data:
#                 for model in data['models']:
#                     methods = model.get('supportedGenerationMethods', [])
#                     if 'generateContent' in methods:
#                         return model['name']
#             return None
#         except:
#             return None

#     @staticmethod
#     def _send_request(prompt_text):
#         """Yapay Zekaya istek atar"""
#         api_key = os.getenv("GOOGLE_API_KEY")
#         if not api_key: return "HATA: API Key yok."
        
#         active_model = AIWriter._find_active_model(api_key)
#         if not active_model: return "HATA: Google API aktif model bulamadı."

#         url = f"https://generativelanguage.googleapis.com/v1beta/{active_model}:generateContent?key={api_key}"
#         headers = {'Content-Type': 'application/json'}
#         payload = {"contents": [{"parts": [{"text": prompt_text}]}]}

#         try:
#             response = requests.post(url, headers=headers, json=payload, timeout=40)
#             if response.status_code == 200:
#                 return response.json()['candidates'][0]['content']['parts'][0]['text']
#             else:
#                 return f"Hata: {response.text}"
#         except Exception as e:
#             return f"Bağlantı Hatası: {str(e)}"

#     @staticmethod
#     def veri_madenciligi(isim: str):
#         """
#         name_data.py verisini işler.
#         """
#         isim = isim.upper().strip()
#         ham_veri = []
        
#         # Veritabanı boş geldiyse uyarı ver (Debug için)
#         if not HARF_DETAYLARI:
#             return "SİSTEM UYARISI: Veritabanı dosyası yüklendi ancak içi boş görünüyor. Lütfen name_data.py dosyasını kontrol edin."

#         # 1. ÖZEL İSİM ANALİZİ
#         if isim in OZEL_ISIM_ANALIZLERI:
#             bilgi = OZEL_ISIM_ANALIZLERI[isim]
#             ham_veri.append(f"⚠️ ÖZEL İSİM ANALİZİ TESPİT EDİLDİ: {isim}")
#             ham_veri.append(f"Derece: {bilgi.get('derece')}")
#             ham_veri.append(f"Açıklama: {bilgi.get('aciklama')}")
#             ham_veri.append("-" * 30)

#         # 2. TEHLİKELİ EK VE İSİM KONTROLÜ
#         if isim.endswith("NUR"):
#             ham_veri.append(f"⚠️ RİSKLİ EK TESPİTİ (NUR): {OZEL_UYARILAR.get('NUR_EKI', {}).get('aciklama', 'Nur eki uyarısı')}")
        
#         if isim.endswith("CAN"):
#             ham_veri.append(f"⚠️ RİSKLİ EK TESPİTİ (CAN): {OZEL_UYARILAR.get('CAN_EKI', {}).get('aciklama', 'Can eki uyarısı')}")
            
#         if isim.endswith("LA"):
#             ham_veri.append(f"⚠️ RİSKLİ EK TESPİTİ (LA): {OZEL_UYARILAR.get('LA_EKI', {}).get('aciklama', 'La eki uyarısı')}")

#         # Özel Yasaklı İsimler
#         yasakli_map = {
#             "ELİF": "ELIF_ISMI", "ELIF": "ELIF_ISMI",
#             "İREM": "IREM_ISMI", "IREM": "IREM_ISMI",
#             "ESRA": "ESRA_ISMI",
#             "ALEYNA": "ALEYNA_ISMI",
#             "KÜBRA": "KUBRA_ISMI", "KUBRA": "KUBRA_ISMI",
#             "SÜMEYYE": "SUMEYYE_ISMI", "SUMEYYE": "SUMEYYE_ISMI",
#             "MERVE": "MERVE_ISMI",
#             "KEZBAN": "KEZBAN",
#             "GÜL": "GUL", "GUL": "GUL"
#         }
        
#         if isim in yasakli_map:
#             key = yasakli_map[isim]
#             # Key veritabanında var mı kontrol et
#             if key in OZEL_UYARILAR:
#                 ham_veri.append(f"🛑 KRİTİK İSİM UYARISI ({isim}): {OZEL_UYARILAR[key]['aciklama']}")

#         # 3. HARF HARF ANALİZ
#         ham_veri.append(f"\n--- HARF ENERJİLERİ ({isim}) ---")
#         harf_sayilari = {h: isim.count(h) for h in isim}
        
#         for index, harf in enumerate(isim):
#             if harf == " ": continue
            
#             if harf in HARF_DETAYLARI:
#                 detay = HARF_DETAYLARI[harf]
#                 ham_veri.append(f"► {harf} HARFİ (Genel): {detay['genel']}")
                
#                 if index == 0:
#                     ham_veri.append(f"   ➥ İLK HARF ETKİSİ: {detay.get('ilk_harf', 'Belirtilmemiş')}")
#                 elif index == len(isim) - 1:
#                     son_analiz = detay.get('sonda', 'Belirtilmemiş')
#                     if son_analiz == "Belirtilmemiş":
#                         ham_veri.append(f"   ➥ İÇ HARF ETKİSİ: {detay.get('icinde_veya_coklu', 'Belirtilmemiş')}")
#                     else:
#                         ham_veri.append(f"   ➥ SON HARF ETKİSİ: {son_analiz}")
#                 else:
#                     ham_veri.append(f"   ➥ İÇ HARF ETKİSİ: {detay.get('icinde_veya_coklu', 'Belirtilmemiş')}")
                
#                 if harf_sayilari[harf] > 1:
#                     ham_veri.append(f"   🔥 DİKKAT: Bu harften isimde {harf_sayilari[harf]} tane var! Etkisi katlanarak artar.")

#         return "\n".join(ham_veri)

#     @staticmethod
#     def generate_name_analysis_rag(isim: str, pdf_icerigi=None):
#         teknik_veri = AIWriter.veri_madenciligi(isim)
        
#         prompt = f"""
#         Sen "İnsan Ekspertizi" projesinin baş analistisin.
#         Aşağıda "{isim}" ismi için veritabanımızdan çekilen KESİN ve DEĞİŞMEZ teknik veriler bulunmaktadır.
        
#         GÖREVİN:
#         Bu teknik verileri alıp, karşındaki insanı etkileyecek, akıcı, mistik ve derinlemesine bir "İsim Enerjisi Raporu" yazmaktır.
        
#         KURALLAR:
#         1. SADECE aşağıda verdiğim verileri kullan. Dışarıdan bilgi uydurma.
#         2. Eğer "TEHLİKELİ" veya "RİSKLİ" bir uyarı varsa, bunu yumuşatma. Açıkça ve ciddiyetle uyar.
#         3. Harfleri tek tek saymak yerine bütünlüklü bir paragraf akışı oluştur.
        
#         --- TEKNİK ANALİZ VERİLERİ ---
#         {teknik_veri}
#         """
#         return AIWriter._send_request(prompt)

#     @staticmethod
#     def generate_human_report(analysis_data: dict) -> str:
#         return "Bu özellik şu an bakımda."





import os
import sys
import requests
import json
import importlib.util
import re

# --- MODÜL YÜKLEME SİSTEMİ (Standart) ---
def load_module(module_name):
    try:
        # 1. Standart yol
        return importlib.import_module(f"services.{module_name}")
    except ImportError:
        try:
            # 2. Aynı dizin
            return importlib.import_module(module_name)
        except ImportError:
            # 3. Manuel yol
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, f"{module_name}.py")
            if os.path.exists(file_path):
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                foo = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = foo
                spec.loader.exec_module(foo)
                return foo
            return None

# Veritabanlarını Yükle
ND = load_module("name_data")
RD = load_module("ruya_data")

# İsim Verileri
HARF_DETAYLARI = getattr(ND, "HARF_DETAYLARI", {})
OZEL_UYARILAR = getattr(ND, "OZEL_UYARILAR", {})
OZEL_ISIM_ANALIZLERI = getattr(ND, "OZEL_ISIM_ANALIZLERI", {})

# Rüya Verileri (Devasa Sözlük)
RUYA_SOZLUGU = getattr(RD, "RUYA_SOZLUGU", {})

class AIWriter:
    @staticmethod
    def _find_active_model(api_key):
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
            response = requests.get(url)
            if response.status_code != 200: return None
            data = response.json()
            if 'models' in data:
                for model in data['models']:
                    methods = model.get('supportedGenerationMethods', [])
                    if 'generateContent' in methods:
                        return model['name']
            return None
        except:
            return None

    @staticmethod
    def _send_request(prompt_text):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key: return "HATA: API Key yok."
        
        active_model = AIWriter._find_active_model(api_key)
        if not active_model: return "HATA: Google API aktif model bulamadı."

        url = f"https://generativelanguage.googleapis.com/v1beta/{active_model}:generateContent?key={api_key}"
        headers = {'Content-Type': 'application/json'}
        payload = {"contents": [{"parts": [{"text": prompt_text}]}]}

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=40)
            if response.status_code == 200:
                return response.json()['candidates'][0]['content']['parts'][0]['text']
            else:
                return f"Hata: {response.text}"
        except Exception as e:
            return f"Bağlantı Hatası: {str(e)}"

    # --- İSİM ANALİZİ MOTORU (Aynı Kaldı) ---
    @staticmethod
    def veri_madenciligi(isim: str):
        isim = isim.upper().strip()
        ham_veri = []
        
        if not HARF_DETAYLARI: return "SİSTEM UYARISI: İsim veritabanı boş."

        if isim in OZEL_ISIM_ANALIZLERI:
            bilgi = OZEL_ISIM_ANALIZLERI[isim]
            ham_veri.append(f"⚠️ ÖZEL İSİM ANALİZİ: {isim}\nDerece: {bilgi.get('derece')}\nAçıklama: {bilgi.get('aciklama')}\n" + "-"*30)

        if isim.endswith("NUR"): ham_veri.append(f"⚠️ NUR EKI: {OZEL_UYARILAR.get('NUR_EKI', {}).get('aciklama')}")
        if isim.endswith("CAN"): ham_veri.append(f"⚠️ CAN EKI: {OZEL_UYARILAR.get('CAN_EKI', {}).get('aciklama')}")
        if isim.endswith("LA"): ham_veri.append(f"⚠️ LA EKI: {OZEL_UYARILAR.get('LA_EKI', {}).get('aciklama')}")

        yasakli_kelimeler = ["ELİF", "ELIF", "İREM", "IREM", "ESRA", "ALEYNA", "KÜBRA", "KUBRA", "SÜMEYYE", "SUMEYYE", "MERVE", "KEZBAN", "GÜL"]
        for yasak in yasakli_kelimeler:
            if yasak in isim:
                key = f"{yasak}_ISMI" if yasak not in ["GÜL", "KEZBAN"] else ("GUL" if yasak == "GÜL" else "KEZBAN")
                if yasak in ["ELİF", "ELIF"]: key = "ELIF_ISMI"
                if yasak in ["İREM", "IREM"]: key = "IREM_ISMI"
                if yasak in ["KÜBRA", "KUBRA"]: key = "KUBRA_ISMI"
                if yasak in ["SÜMEYYE", "SUMEYYE"]: key = "SUMEYYE_ISMI"
                if key in OZEL_UYARILAR: ham_veri.append(f"🛑 UYARI ({yasak}): {OZEL_UYARILAR[key]['aciklama']}")

        ham_veri.append(f"\n--- HARF ENERJİLERİ ({isim}) ---")
        harf_sayilari = {h: isim.count(h) for h in isim}
        for index, harf in enumerate(isim):
            if harf == " ": continue
            if harf in HARF_DETAYLARI:
                detay = HARF_DETAYLARI[harf]
                ham_veri.append(f"► {harf}: {detay['genel']}")
                if index == 0: ham_veri.append(f"   ➥ BAŞTA: {detay.get('ilk_harf', '')}")
                elif index == len(isim) - 1: ham_veri.append(f"   ➥ SONDA: {detay.get('sonda', detay.get('icinde_veya_coklu'))}")
                else: ham_veri.append(f"   ➥ ORTADA: {detay.get('icinde_veya_coklu', '')}")
                if harf_sayilari[harf] > 1: ham_veri.append(f"   🔥 {harf_sayilari[harf]} tane var! Etki katlanır.")
        return "\n".join(ham_veri)

    @staticmethod
    def generate_name_analysis_rag(isim: str, pdf_icerigi=None):
        teknik_veri = AIWriter.veri_madenciligi(isim)
        if "HARF ENERJİLERİ" not in teknik_veri: return "SİSTEM HATASI."
        prompt = f"""
        Sen "İnsan Ekspertizi" baş analistisin. "{isim}" ismini analiz et.
        AŞAMA 1: İSMİN ANLAMI VE TERS ENERJİ
        - Eşya/Bitki ismiyse (Gül, Kaya, Deniz) sertçe uyar. "İnsan eşya değildir" de.
        - Ters enerji kuralını uygula: "Gül ise gülemez", "Mutlu ise mutsuz olur".
        AŞAMA 2: HARF VE TEKNİK ANALİZ
        - Aşağıdaki verileri kullan ve akıcı bir dille anlat.
        VERİLER: {teknik_veri}
        """
        return AIWriter._send_request(prompt)

    # --- RÜYA ANALİZİ MOTORU (GÜNCELLENDİ) ---
    @staticmethod
    def ruya_tabiri_motoru(ruya_metni: str):
        """
        Rüya metnini tarar ve RUYA_SOZLUGU içindeki eşleşmeleri bulur.
        """
        if not RUYA_SOZLUGU:
            return "SİSTEM UYARISI: Rüya veritabanı bulunamadı veya boş."

        # Rüyayı temizle ve büyük harfe çevir
        ruya_temiz = re.sub(r'[^\w\s]', '', ruya_metni).upper()
        ruya_kelimeler = ruya_temiz.split()
        
        bulunan_bilgiler = []
        bulunan_anahtarlar = set() # Aynı şeyi tekrar eklememek için

        # STRATEJİ 1: Sözlükteki Anahtarları Rüya Metninde Ara (Çok Kelimeli Semboller İçin)
        # Örn: Sözlükte "SİYAH YILAN" varsa ve metinde geçiyorsa yakala.
        for anahtar, bilgi in RUYA_SOZLUGU.items():
            if anahtar in ruya_temiz and anahtar not in bulunan_anahtarlar:
                bulunan_anahtarlar.add(anahtar)
                
                # Bilgiyi formatla
                detay_str = "\n".join([f"- {d}" for d in bilgi.get('detaylar', [])])
                uyari_str = f"⚠️ UYARI: {bilgi.get('uyari')}" if bilgi.get('uyari') else ""
                
                bulunan_bilgiler.append(f"""
                📖 SEMBOL: {anahtar}
                Genel Manası: {bilgi.get('genel', 'Belirtilmemiş')}
                Detaylar:
                {detay_str}
                {uyari_str}
                """)

        # STRATEJİ 2: Rüya Kelimelerini Sözlükte Ara (Tek Kelimelik Semboller İçin)
        # Örn: Metinde "ARABA" geçiyorsa ve yukarıda bulunmadıysa yakala.
        for kelime in ruya_kelimeler:
            # Basit kök bulma (Çoğul eklerini at: ARABALAR -> ARABA)
            kok = kelime[:-3] if kelime.endswith("LAR") or kelime.endswith("LER") else kelime
            
            # Tam eşleşme veya kök eşleşmesi
            hedef_anahtar = None
            if kelime in RUYA_SOZLUGU: hedef_anahtar = kelime
            elif kok in RUYA_SOZLUGU: hedef_anahtar = kok
            
            if hedef_anahtar and hedef_anahtar not in bulunan_anahtarlar:
                bulunan_anahtarlar.add(hedef_anahtar)
                bilgi = RUYA_SOZLUGU[hedef_anahtar]
                
                detay_str = "\n".join([f"- {d}" for d in bilgi.get('detaylar', [])])
                uyari_str = f"⚠️ UYARI: {bilgi.get('uyari')}" if bilgi.get('uyari') else ""
                
                bulunan_bilgiler.append(f"""
                📖 SEMBOL: {hedef_anahtar}
                Genel Manası: {bilgi.get('genel', 'Belirtilmemiş')}
                Detaylar:
                {detay_str}
                {uyari_str}
                """)

        kaynak_metni = "\n".join(bulunan_bilgiler) if bulunan_bilgiler else "Veritabanında doğrudan bir sembol eşleşmesi bulunamadı. Genel İslami rüya tabiri prensiplerini kullan."

        # Prompt Hazırla
        prompt = f"""
        Sen "İnsan Ekspertizi" projesinin Rüya ve Bilinçaltı Alimisin. (İbn-i Sirin ve Nablusi ekolü).
        
        KULLANICININ RÜYASI:
        "{ruya_metni}"

        --- KADİM ARŞİVİMİZDEN BULUNANLAR (BUNLARI TEMEL AL) ---
        {kaynak_metni}
        ----------------------------------------------------------

        ANALİZ KURALLARI:
        1. ÖNCELİK ARŞİVDE: Yukarıdaki "KADİM ARŞİV" bölümünde bilgi varsa, yorumunu %100 ona dayandır. Asla arşivle çelişme. Arşiv "Hayırdır" diyorsa "Şerdir" deme.
        2. BÜTÜNLÜK: Sembolleri tek tek sözlük gibi okuma. Onları birleştirip bir hikaye ve mesaj çıkar.
        3. TONLAMA: Gizemli, net, "Acımasız Mentör" tadında. Uyarı varsa sertçe uyar. "Hayrolsun" deyip geçiştirme.
        4. EKSİKSE TAMAMLA: Arşivde olmayan kısımları kendi geniş rüya tabiri bilginle doldur.

        ÇIKTI FORMATI:
        🌙 RÜYANIN GİZEMİ (Sembollerin analizi ve birleştirilmesi)
        👁️ BİLİNÇALTI MESAJI (Kişinin ruh hali ve korkuları)
        ⚡ İNSAN EKSPERTİZİ HÜKMÜ (Ne yapmalı? Sadaka mı, dikkat mi, müjde mi?)
        """
        
        return AIWriter._send_request(prompt)