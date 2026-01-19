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
import os
import sys
import requests
import json

# --- IMPORT HATASI ÇÖZÜCÜ (YENİ ADRES) ---
# Şu anki dosyanın (ai_writer.py) olduğu klasörü bulur: .../backend/services
current_dir = os.path.dirname(os.path.abspath(__file__))
# Bir üst klasöre (Root) çıkar: .../backend
backend_root = os.path.dirname(current_dir)

# Python'un arama yollarına 'backend' ana klasörünü ekleriz.
# Böylece 'knowledge_base' klasörünü görebilir.
if backend_root not in sys.path:
    sys.path.append(backend_root)

try:
    # ARTIK YENİ ADRESTEN VERİ ÇEKİYORUZ:
    # Klasör: knowledge_base -> isim_analizi
    # Dosya: isim_analizi.py
    from knowledge_base.isim_analizi.isim_analizi import (
        HARF_DETAYLARI,
        OZEL_UYARILAR,
        OZEL_ISIM_ANALIZLERI,
        ISIM_VERME_KURALLARI
    )
except ImportError as e:
    print(f"KRİTİK HATA: Veritabanı dosyası yeni yerinde bulunamadı! Hata: {e}")
    # Kodun tamamen çökmemesi için boş sözlükler tanımlıyoruz (Geçici önlem)
    HARF_DETAYLARI = {}
    OZEL_UYARILAR = {}
    OZEL_ISIM_ANALIZLERI = {}
    ISIM_VERME_KURALLARI = {}

class AIWriter:
    @staticmethod
    def _find_active_model(api_key):
        """Google'ın aktif modellerini bulur"""
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
        """Yapay Zekaya istek atar"""
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

    @staticmethod
    def veri_madenciligi(isim: str):
        """
        knowledge_base/isim_analizi/isim_analizi.py dosyasını tarar.
        """
        isim = isim.upper().strip()
        ham_veri = []
        
        # 1. ÖZEL İSİM ANALİZİ
        if isim in OZEL_ISIM_ANALIZLERI:
            bilgi = OZEL_ISIM_ANALIZLERI[isim]
            ham_veri.append(f"⚠️ ÖZEL İSİM ANALİZİ TESPİT EDİLDİ: {isim}")
            ham_veri.append(f"Derece: {bilgi.get('derece')}")
            ham_veri.append(f"Açıklama: {bilgi.get('aciklama')}")
            ham_veri.append("-" * 30)

        # 2. TEHLİKELİ EK VE İSİM KONTROLÜ
        if isim.endswith("NUR"):
            ham_veri.append(f"⚠️ RİSKLİ EK TESPİTİ (NUR): {OZEL_UYARILAR.get('NUR_EKI', {}).get('aciklama', 'Nur eki uyarısı')}")
        
        if isim.endswith("CAN"):
            ham_veri.append(f"⚠️ RİSKLİ EK TESPİTİ (CAN): {OZEL_UYARILAR.get('CAN_EKI', {}).get('aciklama', 'Can eki uyarısı')}")
            
        if isim.endswith("LA"):
            ham_veri.append(f"⚠️ RİSKLİ EK TESPİTİ (LA): {OZEL_UYARILAR.get('LA_EKI', {}).get('aciklama', 'La eki uyarısı')}")

        # Özel Yasaklı İsimler
        yasakli_map = {
            "ELİF": "ELIF_ISMI", "ELIF": "ELIF_ISMI",
            "İREM": "IREM_ISMI", "IREM": "IREM_ISMI",
            "ESRA": "ESRA_ISMI",
            "ALEYNA": "ALEYNA_ISMI",
            "KÜBRA": "KUBRA_ISMI", "KUBRA": "KUBRA_ISMI",
            "SÜMEYYE": "SUMEYYE_ISMI", "SUMEYYE": "SUMEYYE_ISMI",
            "MERVE": "MERVE_ISMI",
            "KEZBAN": "KEZBAN",
            "GÜL": "GUL", "GUL": "GUL"
        }
        
        if isim in yasakli_map:
            key = yasakli_map[isim]
            if key in OZEL_UYARILAR:
                ham_veri.append(f"🛑 KRİTİK İSİM UYARISI ({isim}): {OZEL_UYARILAR[key]['aciklama']}")

        # 3. HARF HARF ANALİZ
        ham_veri.append(f"\n--- HARF ENERJİLERİ ({isim}) ---")
        harf_sayilari = {h: isim.count(h) for h in isim}
        
        for index, harf in enumerate(isim):
            if harf == " ": continue
            
            if harf in HARF_DETAYLARI:
                detay = HARF_DETAYLARI[harf]
                ham_veri.append(f"► {harf} HARFİ (Genel): {detay['genel']}")
                
                if index == 0:
                    ham_veri.append(f"   ➥ İLK HARF ETKİSİ: {detay.get('ilk_harf', 'Belirtilmemiş')}")
                elif index == len(isim) - 1:
                    son_analiz = detay.get('sonda', 'Belirtilmemiş')
                    if son_analiz == "Belirtilmemiş":
                        ham_veri.append(f"   ➥ İÇ HARF ETKİSİ: {detay.get('icinde_veya_coklu', 'Belirtilmemiş')}")
                    else:
                        ham_veri.append(f"   ➥ SON HARF ETKİSİ: {son_analiz}")
                else:
                    ham_veri.append(f"   ➥ İÇ HARF ETKİSİ: {detay.get('icinde_veya_coklu', 'Belirtilmemiş')}")
                
                if harf_sayilari[harf] > 1:
                    ham_veri.append(f"   🔥 DİKKAT: Bu harften isimde {harf_sayilari[harf]} tane var! Etkisi katlanarak artar.")

        return "\n".join(ham_veri)

    @staticmethod
    def generate_name_analysis_rag(isim: str, pdf_icerigi=None):
        teknik_veri = AIWriter.veri_madenciligi(isim)
        
        prompt = f"""
        Sen "İnsan Ekspertizi" projesinin baş analistisin.
        Aşağıda "{isim}" ismi için veritabanımızdan çekilen KESİN ve DEĞİŞMEZ teknik veriler bulunmaktadır.
        
        GÖREVİN:
        Bu teknik verileri alıp, karşındaki insanı etkileyecek, akıcı, mistik ve derinlemesine bir "İsim Enerjisi Raporu" yazmaktır.
        
        KURALLAR:
        1. SADECE aşağıda verdiğim verileri kullan. Dışarıdan bilgi uydurma.
        2. Eğer "TEHLİKELİ" veya "RİSKLİ" bir uyarı varsa, bunu yumuşatma. Açıkça ve ciddiyetle uyar.
        3. Harfleri tek tek saymak yerine bütünlüklü bir paragraf akışı oluştur.
        
        --- TEKNİK ANALİZ VERİLERİ ---
        {teknik_veri}
        """
        return AIWriter._send_request(prompt)

    @staticmethod
    def generate_human_report(analysis_data: dict) -> str:
        return "Bu özellik şu an bakımda."