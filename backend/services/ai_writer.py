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
import requests
import json

class AIWriter:
    @staticmethod
    def _find_active_model(api_key):
        """
        Google'a 'Elinizde hangi modeller var?' diye sorar.
        İlk bulduğu çalışan modeli seçer.
        Böylece 404 hatası alma şansı kalmaz.
        """
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
            response = requests.get(url)
            
            if response.status_code != 200:
                print(f"Model Listesi Alınamadı: {response.text}")
                return None

            data = response.json()
            # Listeyi tara ve generateContent (Metin üretme) özelliği olan İLK modeli bul
            if 'models' in data:
                for model in data['models']:
                    # Desteklenen metodlara bak
                    methods = model.get('supportedGenerationMethods', [])
                    if 'generateContent' in methods:
                        print(f"--> BULUNAN ÇALIŞAN MODEL: {model['name']}")
                        return model['name'] # Örn: 'models/gemini-1.5-flash'
            
            return None
        except Exception as e:
            print(f"Model arama hatası: {e}")
            return None

    @staticmethod
    def _send_request(prompt_text):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return "HATA: API Key bulunamadı."

        # ADIM 1: Rastgele isim deneme, git Google'a sor!
        active_model = AIWriter._find_active_model(api_key)
        
        if not active_model:
            # Eğer liste boş dönüyorsa, API Key yetkisizdir.
            return "HATA: API Key geçerli ama Google 'Hiçbir model kullanamazsın' diyor. (Google Cloud Console'dan Generative Language API'nin ENABLE olduğundan emin ol)."

        # ADIM 2: Bulunan modeli kullan
        # active_model zaten 'models/gemini-...' formatında gelir.
        url = f"https://generativelanguage.googleapis.com/v1beta/{active_model}:generateContent?key={api_key}"

        headers = {'Content-Type': 'application/json'}
        payload = {
            "contents": [{
                "parts": [{"text": prompt_text}]
            }]
        }

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                try:
                    return data['candidates'][0]['content']['parts'][0]['text']
                except:
                    return "Model cevap verdi ama metin boş. Ham cevap: " + str(data)
            else:
                return f"Google Hatası ({response.status_code}): {response.text}"

        except Exception as e:
            return f"Bağlantı Hatası: {str(e)}"

    @staticmethod
    def generate_human_report(analysis_data: dict) -> str:
        prompt = f"""
        Sen mistik bir yaşam koçusun. Şu verilere göre kişiye özel motive edici bir mektup yaz:
        İsim: {analysis_data.get('tam_isim')}
        Pin: {analysis_data.get('pin')}
        """
        return AIWriter._send_request(prompt)

    @staticmethod
    def generate_name_analysis_rag(isim: str, pdf_icerigi: str) -> str:
        prompt = f"""
        Sen bir İsim Analistisin. Aşağıdaki KİTAP BİLGİSİNE dayanarak yorum yap.
        
        KİTAP BİLGİSİ:
        {pdf_icerigi[:30000]}
        
        ANALİZ EDİLECEK KİŞİ: {isim}
        
        Lütfen profesyonel bir dille, kitapta yazanlara göre ismin analizini yap.
        """
        return AIWriter._send_request(prompt)