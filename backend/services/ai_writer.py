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
    def _send_request(prompt_text):
        """
        Google Kütüphanesini BYPASS eder.
        Doğrudan Google sunucusuna HTTP isteği atar.
        Kütüphane hatası verme ihtimali %0'dır.
        """
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return "HATA: API Key bulunamadı."

        # 1. HEDEF ADRES (Doğrudan Google'ın REST API adresi)
        # Burası değişmez, sabittir. Kütüphane sürümü vs. etkilemez.
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

        # 2. PAKETİ HAZIRLA
        headers = {'Content-Type': 'application/json'}
        payload = {
            "contents": [{
                "parts": [{"text": prompt_text}]
            }]
        }

        try:
            # 3. İSTEĞİ GÖNDER (requests kütüphanesi ile)
            response = requests.post(url, headers=headers, json=payload)
            
            # 4. CEVABI KONTROL ET
            if response.status_code == 200:
                # Başarılı! İçinden metni cımbızla al.
                data = response.json()
                try:
                    return data['candidates'][0]['content']['parts'][0]['text']
                except:
                    return "Cevap geldi ama metin bulunamadı. Ham cevap: " + str(data)
            else:
                # Google hata verdi (Açıkça ne olduğunu yazar)
                return f"Google Hata Verdi (Kod {response.status_code}): {response.text}"

        except Exception as e:
            return f"Bağlantı Hatası: {str(e)}"

    @staticmethod
    def generate_human_report(analysis_data: dict) -> str:
        prompt = f"""
        Sen mistik bir yaşam koçusun. Şu verilere göre kişiye özel motive edici bir mektup yaz:
        İsim: {analysis_data.get('tam_isim')}
        Pin: {analysis_data.get('pin')}
        Element: {analysis_data.get('baskin_element')}
        """
        return AIWriter._send_request(prompt)

    @staticmethod
    def generate_name_analysis_rag(isim: str, pdf_icerigi: str) -> str:
        prompt = f"""
        Sen bir İsim Analistisin. Aşağıdaki KİTAP BİLGİSİNE dayanarak yorum yap.
        Kafandan uydurma, sadece kitaba bak.
        
        KİTAP BİLGİSİ:
        {pdf_icerigi[:30000]}
        
        ANALİZ EDİLECEK KİŞİ: {isim}
        
        Yorumun profesyonel ve başlıklar halinde olsun.
        """
        return AIWriter._send_request(prompt)