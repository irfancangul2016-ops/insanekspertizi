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

# Google Kütüphane Kontrolü
try:
    import google.generativeai as genai
    GOOGLE_AVAILABLE = True
except ImportError:
    GOOGLE_AVAILABLE = False

class AIWriter:
    @staticmethod
    def generate_human_report(analysis_data: dict) -> str:
        """
        Gemini AI kullanarak rapor yazar.
        Anahtarı SADECE ortam değişkenlerinden (Environment Variable) okur.
        """
        if not GOOGLE_AVAILABLE:
            return "Yapay Zeka modülü yüklü değil."

        # 1. KASADAN ANAHTARI İSTE (Environment Variable)
        api_key = os.getenv("GOOGLE_API_KEY")

        # 2. Anahtar Yoksa Hata Ver
        if not api_key:
            print("UYARI: GOOGLE_API_KEY ortam değişkeni bulunamadı!")
            return "Sistemde API anahtarı tanımlanmamış. Lütfen yönetici ile iletişime geçin."

        try:
            # 3. Bağlantıyı Kur
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')

            # 4. İsteği Gönder
            prompt = f"""
            Sen mistik, bilge ve derinlemesine analiz yapan bir mentörsün.
            Aşağıdaki verilere göre bu kişiye kısa, vurucu, edebi bir analiz mektubu yaz.
            
            İsim: {analysis_data.get('tam_isim')}
            Baskın Element: {analysis_data.get('baskin_element')}
            Eksik Element: {analysis_data.get('eksik_element')}
            Çakra Durumu: {analysis_data.get('baskin_cakra_val')}. Çakra aktif.
            
            Kurallar:
            - Asla "Merhaba" deme. Direkt derin bir sözle gir.
            - Kısa tut (Maksimum 3 paragraf).
            - Kişiye özel tavsiye ver.
            """
            
            response = model.generate_content(prompt)
            return response.text

        except Exception as e:
            return f"Yapay zeka bağlantısında sorun oluştu. (Hata: {str(e)})"