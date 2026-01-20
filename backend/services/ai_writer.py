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
import traceback

# --- GLOBAL DEĞİŞKENLER ---
RUYA_DATA_HATASI = None
RUYA_SOZLUGU = {}
ANAHTAR_KELIMELER = {}

# --- MODÜL YÜKLEME (HATA GÖSTEREN VERSİYON) ---
try:
    from services import ruya_data
    RUYA_SOZLUGU = getattr(ruya_data, "RUYA_SOZLUGU", {})
    ANAHTAR_KELIMELER = getattr(ruya_data, "ANAHTAR_KELIMELER", {})
except Exception as e1:
    try:
        import ruya_data
        RUYA_SOZLUGU = getattr(ruya_data, "RUYA_SOZLUGU", {})
        ANAHTAR_KELIMELER = getattr(ruya_data, "ANAHTAR_KELIMELER", {})
    except Exception as e2:
        RUYA_DATA_HATASI = f"Veritabanı Yükleme Hatası:\n1. {str(e1)}\n2. {str(e2)}"
        print(f"KRİTİK HATA: {RUYA_DATA_HATASI}")

try:
    from services import name_data
    HARF_DETAYLARI = getattr(name_data, "HARF_DETAYLARI", {})
    OZEL_UYARILAR = getattr(name_data, "OZEL_UYARILAR", {})
    OZEL_ISIM_ANALIZLERI = getattr(name_data, "OZEL_ISIM_ANALIZLERI", {})
except:
    try:
        import name_data
        HARF_DETAYLARI = getattr(name_data, "HARF_DETAYLARI", {})
        OZEL_UYARILAR = getattr(name_data, "OZEL_UYARILAR", {})
        OZEL_ISIM_ANALIZLERI = getattr(name_data, "OZEL_ISIM_ANALIZLERI", {})
    except:
        HARF_DETAYLARI = {}

class AIWriter:
    @staticmethod
    def _find_active_model(api_key):
        """
        Aktif modelleri bulur ve KALİTE öncelikli sıralama yapar.
        Önce PRO, sonra FLASH arar.
        """
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
            response = requests.get(url)
            if response.status_code != 200: return None
            data = response.json()
            
            if 'models' in data:
                # Sadece metin üretebilen modelleri al
                valid_models = [m for m in data['models'] if 'generateContent' in m.get('supportedGenerationMethods', [])]
                
                # --- MODEL SEÇİM MANTIĞI (GÜNCELLENDİ) ---
                
                # 1. TERCİH: Gemini 1.5 Pro (En güncel ve zeki olan)
                for model in valid_models:
                    if "gemini-1.5-pro" in model['name']:
                        return model['name']
                
                # 2. TERCİH: Gemini 1.0 Pro (Eski ama sağlam Pro)
                for model in valid_models:
                    if "gemini-pro" in model['name']:
                        return model['name']
                        
                # 3. TERCİH: Gemini 1.5 Flash (Hızlı ama daha basit - Yedek)
                for model in valid_models:
                    if "gemini-1.5-flash" in model['name']:
                        return model['name']
                
                # 4. SON ÇARE: Listede ne varsa ilkini al
                if valid_models:
                    return valid_models[0]['name']
                    
            return None
        except:
            return None

    @staticmethod
    def _send_request(prompt_text):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key: return "HATA: API Key yok. Lütfen .env dosyasını kontrol et."
        
        active_model = AIWriter._find_active_model(api_key)
        if not active_model: return "HATA: Google API aktif model bulamadı."

        # Seçilen modeli log'a bas (Render loglarından görmek için)
        print(f"KULLANILAN YAPAY ZEKA MODELİ: {active_model}")

        url = f"https://generativelanguage.googleapis.com/v1beta/{active_model}:generateContent?key={api_key}"
        headers = {'Content-Type': 'application/json'}
        payload = {"contents": [{"parts": [{"text": prompt_text}]}]}

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=60) # Timeout'u 60 saniyeye çıkardık, Pro bazen düşünebilir.
            if response.status_code == 200:
                return response.json()['candidates'][0]['content']['parts'][0]['text']
            else:
                return f"Google API Hatası: {response.text}"
        except Exception as e:
            return f"Bağlantı Hatası: {str(e)}"

    # --- İSİM ANALİZİ MOTORU ---
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

    # --- RÜYA ANALİZİ MOTORU ---
    @staticmethod
    def ruya_tabiri_motoru(ruya_metni: str):
        if RUYA_DATA_HATASI:
            return f"SİSTEM HATASI: `ruya_data.py` dosyasında kod hatası var.\n\nDetay: {RUYA_DATA_HATASI}"

        if not RUYA_SOZLUGU:
            return "UYARI: `ruya_data.py` yüklendi ama içi boş görünüyor."

        ruya_temiz = re.sub(r'[^\w\s]', '', ruya_metni).upper()
        ruya_kelimeler = ruya_temiz.split()
        
        bulunan_bilgiler = []
        bulunan_anahtarlar = set()

        for anahtar, bilgi in RUYA_SOZLUGU.items():
            if anahtar in ruya_temiz and anahtar not in bulunan_anahtarlar:
                bulunan_anahtarlar.add(anahtar)
                detay_str = "\n".join([f"- {d}" for d in bilgi.get('detaylar', [])])
                uyari_str = f"⚠️ UYARI: {bilgi.get('uyari')}" if bilgi.get('uyari') else ""
                bulunan_bilgiler.append(f"📖 SEMBOL: {anahtar}\nGenel: {bilgi.get('genel')}\n{detay_str}\n{uyari_str}")

        for kelime in ruya_kelimeler:
            if kelime in ANAHTAR_KELIMELER:
                asil_anahtar = ANAHTAR_KELIMELER[kelime]
                if asil_anahtar in RUYA_SOZLUGU and asil_anahtar not in bulunan_anahtarlar:
                    bulunan_anahtarlar.add(asil_anahtar)
                    bilgi = RUYA_SOZLUGU[asil_anahtar]
                    detay_str = "\n".join([f"- {d}" for d in bilgi.get('detaylar', [])])
                    bulunan_bilgiler.append(f"📖 SEMBOL: {asil_anahtar}\nGenel: {bilgi.get('genel')}\n{detay_str}")

        kaynak_metni = "\n".join(bulunan_bilgiler) if bulunan_bilgiler else "Veritabanında eşleşme yok. Genel rüya tabiri yap."

        prompt = f"""
        Sen "İnsan Ekspertizi" projesinin Rüya Alimisin.
        
        RÜYA: "{ruya_metni}"
        
        ARŞİV BİLGİLERİ (KESİN GERÇEKLER):
        {kaynak_metni}
        
        GÖREV:
        1. Öncelikle yukarıdaki ARŞİV BİLGİLERİ'ni kullan. Arşivde ne yazıyorsa o esastır.
        2. Arşivde eksik kalan kısımları kendi derin sembolizm bilginle tamamla.
        3. Mistik, uyarıcı ve "Mentör" tonunda konuş. "Hayırdır inşallah" gibi basit laflar etme, bilinçaltını deşifre et.
        """
        
        return AIWriter._send_request(prompt)