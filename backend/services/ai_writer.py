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
import requests
import re

# --- GLOBAL DEĞİŞKENLER VE VERİ YÜKLEME ---
RUYA_SOZLUGU = {}
ANAHTAR_KELIMELER = {}
HARF_DETAYLARI = {}
OZEL_UYARILAR = {}
OZEL_ISIM_ANALIZLERI = {}

# 1. RÜYA VERİLERİNİ YÜKLE
try:
    from services import ruya_data
    RUYA_SOZLUGU = getattr(ruya_data, "RUYA_SOZLUGU", {})
    ANAHTAR_KELIMELER = getattr(ruya_data, "ANAHTAR_KELIMELER", {})
except Exception:
    try:
        import ruya_data
        RUYA_SOZLUGU = getattr(ruya_data, "RUYA_SOZLUGU", {})
        ANAHTAR_KELIMELER = getattr(ruya_data, "ANAHTAR_KELIMELER", {})
    except:
        print("UYARI: ruya_data.py bulunamadı.")

# 2. İSİM VERİLERİNİ YÜKLE
try:
    from services import name_data
    HARF_DETAYLARI = getattr(name_data, "HARF_DETAYLARI", {})
    OZEL_UYARILAR = getattr(name_data, "OZEL_UYARILAR", {})
    OZEL_ISIM_ANALIZLERI = getattr(name_data, "OZEL_ISIM_ANALIZLERI", {})
except Exception:
    try:
        import name_data
        HARF_DETAYLARI = getattr(name_data, "HARF_DETAYLARI", {})
        OZEL_UYARILAR = getattr(name_data, "OZEL_UYARILAR", {})
        OZEL_ISIM_ANALIZLERI = getattr(name_data, "OZEL_ISIM_ANALIZLERI", {})
    except:
        print("UYARI: name_data.py bulunamadı.")

class AIWriter:
    @staticmethod
    def _find_active_model(api_key):
        """
        Aktif Google modellerini bulur.
        ÖNCELİK: GEMINI FLASH (Hız ve Maliyet İçin)
        """
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
            response = requests.get(url)
            if response.status_code != 200: return None
            data = response.json()
            
            if 'models' in data:
                valid_models = [m for m in data['models'] if 'generateContent' in m.get('supportedGenerationMethods', [])]
                
                # --- MODEL ÖNCELİK SIRALAMASI (DEĞİŞTİ: FLASH İLK SIRADA) ---
                
                # 1. Tercih: Gemini 1.5 Flash (En Hızlı)
                for model in valid_models:
                    if "gemini-1.5-flash" in model['name']: return model['name']
                
                # 2. Tercih: Gemini 1.5 Pro (Yedek - Kalite)
                for model in valid_models:
                    if "gemini-1.5-pro" in model['name']: return model['name']
                
                # 3. Tercih: Eski Pro
                for model in valid_models:
                    if "gemini-pro" in model['name']: return model['name']
                
                # Hiçbiri yoksa ne varsa onu al
                if valid_models: return valid_models[0]['name']
            return None
        except:
            return None

    @staticmethod
    def _send_request(prompt_text):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key: return "HATA: API Key yok. Lütfen .env dosyasını kontrol et."
        
        active_model = AIWriter._find_active_model(api_key)
        if not active_model: return "HATA: Google API aktif model bulamadı."

        url = f"https://generativelanguage.googleapis.com/v1beta/{active_model}:generateContent?key={api_key}"
        headers = {'Content-Type': 'application/json'}
        payload = {"contents": [{"parts": [{"text": prompt_text}]}]}

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=60)
            if response.status_code == 200:
                return response.json()['candidates'][0]['content']['parts'][0]['text']
            else:
                return f"Google API Hatası: {response.text}"
        except Exception as e:
            return f"Bağlantı Hatası: {str(e)}"

    @staticmethod
    def veri_madenciligi(isim: str):
        """İsim hakkında elimizdeki teknik verileri toplar."""
        isim = isim.upper().strip()
        ham_veri = []
        
        # 1. Özel İsim Veritabanı Kontrolü
        if isim in OZEL_ISIM_ANALIZLERI:
            bilgi = OZEL_ISIM_ANALIZLERI[isim]
            ham_veri.append(f"⚠️ KRİTİK VERİTABANI BİLGİSİ: {isim}\nDerece: {bilgi.get('derece')}\nAçıklama: {bilgi.get('aciklama')}\n" + "-"*30)

        # 2. Ek Kontrolleri
        if isim.endswith("NUR"): ham_veri.append(f"⚠️ NUR EKI: {OZEL_UYARILAR.get('NUR_EKI', {}).get('aciklama')}")
        if isim.endswith("CAN"): ham_veri.append(f"⚠️ CAN EKI: {OZEL_UYARILAR.get('CAN_EKI', {}).get('aciklama')}")
        if isim.endswith("HAN"): ham_veri.append("⚠️ HAN EKI: Yönetici ve liderlik vasfı katar ama egoyu yükseltebilir.")

        # 3. Harf Analizi (Daha Detaylı)
        ham_veri.append(f"\n--- HARF FREKANSLARI VE ETKİLERİ ({isim}) ---")
        harf_sayilari = {h: isim.count(h) for h in isim}
        
        for index, harf in enumerate(isim):
            if harf == " ": continue
            if harf in HARF_DETAYLARI:
                detay = HARF_DETAYLARI[harf]
                konum = "BAŞLANGIÇ HARFİ (En güçlü etki)" if index == 0 else ("SON HARF (Kalıcı etki)" if index == len(isim)-1 else "ARA HARF (Destekleyici)")
                
                ham_veri.append(f"► {harf} ({konum}):")
                ham_veri.append(f"   - Anlam: {detay.get('genel')}")
                
                if harf_sayilari[harf] > 1: 
                    ham_veri.append(f"   🔥 UYARI: Bu harften {harf_sayilari[harf]} tane var! Bu özellik kişinin kaderine HAKİM olur.")
        
        return "\n".join(ham_veri)

    @staticmethod
    def generate_name_analysis_rag(isim: str):
        """
        DERİN ANALİZ MOTORU
        """
        teknik_veri = AIWriter.veri_madenciligi(isim)
        
        prompt = f"""
        Rolün: Sen "İnsan Ekspertizi" projesinin ACIMASIZ, DOBRA ve MİSTİK baş analistisin.
        Asla "yapay zeka" gibi konuşma. Kadim bir bilge gibi konuş.
        
        ANALİZ EDİLECEK KİŞİ: "{isim}"

        ELİMİZDEKİ TEKNİK İSTİHBARAT:
        {teknik_veri}

        GÖREVİN:
        Bu teknik verileri al ve birleştirerek kişinin karakter röntgenini çek.
        Sadece verileri listeleme! Onları yorumla. Örneğin "A harfi liderliktir" deme; "Adın A ile başladığı için emir almaktan nefret edersin, kendi kurallarını koymak istersin" de.

        ANALİZ FORMATI (BU BAŞLIKLARI KULLAN):
        
        1. 🎭 GENEL KARAKTER VE AURA
        (Kişinin dışarıdan nasıl göründüğü ve iç dünyası. Maskeleri indir.)

        2. 💼 KARİYER VE PARA POTANSİYELİ
        (Hangi işlere yatkın? Parayı tutar mı saçar mı? Lider mi köle mi?)

        3. ❤️ AŞK VE İLİŞKİ DİNAMİĞİ
        (Kıskanç mı? Sadık mı? Nasıl bir eş arar? "Zor sever" mi?)

        4. ⚠️ KADERSEL UYARILAR VE ZAYIF NOKTALAR
        (Eşya ismiyse -Gül, Deniz vb.- sertçe uyar. "İnsan eşya değildir" de. Ters enerji kuralını uygula: Mutlu ise mutsuz olabilir. Nur/Can ekleri varsa yüklerinden bahset.)

        TONLAMA:
        - Kısa, net ve vurucu cümleler kur.
        - "Olabilir, edebilir" gibi yuvarlak laflar etme. "Böylesin" de.
        - Okuyucuyu sars. Gerçekleri yüzüne vur.
        """
        
        return AIWriter._send_request(prompt)

    # --- RÜYA ANALİZİ MOTORU ---
    @staticmethod
    def ruya_tabiri_motoru(ruya_metni: str):
        ruya_temiz = re.sub(r'[^\w\s]', '', ruya_metni).upper()
        ruya_kelimeler = ruya_temiz.split()
        
        bulunan_bilgiler = []
        bulunan_anahtarlar = set()

        # Veritabanı taraması
        for anahtar, bilgi in RUYA_SOZLUGU.items():
            if anahtar in ruya_temiz and anahtar not in bulunan_anahtarlar:
                bulunan_anahtarlar.add(anahtar)
                detay_str = "\n".join([f"- {d}" for d in bilgi.get('detaylar', [])])
                uyari_str = f"⚠️ DİKKAT: {bilgi.get('uyari')}" if bilgi.get('uyari') else ""
                bulunan_bilgiler.append(f"📖 {anahtar}: {bilgi.get('genel')}\n{detay_str}\n{uyari_str}")

        kaynak_metni = "\n".join(bulunan_bilgiler) if bulunan_bilgiler else "Veritabanında net eşleşme yok. Genel sembolizm kullan."

        prompt = f"""
        Sen Rüya Alimisin. Bilinçaltının şifrelerini çözen bir üst akılsın.
        
        RÜYA: "{ruya_metni}"
        
        ARŞİV KAYITLARI:
        {kaynak_metni}
        
        GÖREV:
        1. Yukarıdaki ARŞİV KAYITLARINI mutlaka analizine yedir.
        2. Mistik, gizemli ve yol gösterici bir dille yorumla.
        3. Rüyanın sahibine bir "Uyarı" veya "Müjde" vererek bitir.
        """
        
        return AIWriter._send_request(prompt)