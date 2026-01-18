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
from google import genai
from google.genai import types

class AIWriter:
    @staticmethod
    def _get_client():
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return None
        return genai.Client(api_key=api_key)

    @staticmethod
    def _generate(prompt_text: str):
        """
        Modelleri sırayla deneyen akıllı fonksiyon.
        """
        client = AIWriter._get_client()
        if not client:
            return "HATA: Google API Anahtarı bulunamadı."

        # Denenecek Modeller Listesi (Sırayla)
        models_to_try = [
            'gemini-1.5-flash-001',  # En hızlı ve stabil
            'gemini-1.5-flash',      # Kısa isim
            'gemini-1.5-pro-001',    # Daha zeki (Yedek)
            'gemini-1.0-pro'         # Eski toprak (Son çare)
        ]

        last_error = ""

        for model_name in models_to_try:
            try:
                # Modeli dene
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt_text
                )
                # Cevap geldiyse hemen döndür
                if response.text:
                    return response.text
            except Exception as e:
                # Hata aldıysan not et ve bir sonraki modeli dene
                last_error = str(e)
                print(f"Model {model_name} başarısız oldu: {e}")
                continue
        
        # Hiçbiri çalışmadıysa hatayı ver
        return f"Yapay Zeka Hatası (Tüm modeller denendi): {last_error}"

    @staticmethod
    def generate_human_report(analysis_data: dict) -> str:
        prompt = f"""
        Sen mistik konularda uzman, bilge bir yaşam koçusun.
        Aşağıdaki verilere göre motive edici, edebi bir mektup yaz (En az 3 paragraf).

        KİŞİ: {analysis_data.get('tam_isim')}
        PIN: {analysis_data.get('pin')}
        ELEMENT: {analysis_data.get('baskin_element')}
        ÇAKRA: {analysis_data.get('baskin_cakra_val')} aktif.
        """
        return AIWriter._generate(prompt)

    @staticmethod
    def generate_name_analysis_rag(isim: str, pdf_icerigi: str) -> str:
        prompt = f"""
        Sen uzman bir İsim Analisti'sin.
        Şu KİTAP BİLGİSİNİ (CONTEXT) kullanarak "{isim}" ismini analiz et:
        
        --- KİTAP ---
        {pdf_icerigi[:40000]}
        --- SON ---
        
        GÖREV: Sadece kitaptaki bilgilere dayanarak profesyonel bir yorum yap.
        """
        return AIWriter._generate(prompt)