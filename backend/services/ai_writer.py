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

class AIWriter:
    @staticmethod
    def _get_client():
        """
        Google GenAI istemcisini güvenli bir şekilde oluşturur.
        """
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return None
        return genai.Client(api_key=api_key)

    @staticmethod
    def generate_human_report(analysis_data: dict) -> str:
        """
        Eski PDF Raporu için: Kişisel Yıl, Element vb. yorumlayan fonksiyon.
        """
        client = AIWriter._get_client()
        if not client:
            return "HATA: Google API Anahtarı bulunamadı (Render Environment Ayarlarını kontrol edin)."

        try:
            # --- PROMPT HAZIRLIĞI ---
            prompt = f"""
            Sen mistik konularda uzman, bilge bir yaşam koçusun.
            Aşağıdaki teknik analiz verilerini kullanarak, bu kişiye özel, motive edici ve
            edebi bir dille yazılmış DETAYLI BİR MEKTUP (en az 3 paragraf) oluştur.

            KİŞİ BİLGİLERİ:
            - İsim: {analysis_data.get('tam_isim')}
            - Pin Kodu: {analysis_data.get('pin')}
            - Baskın Element: {analysis_data.get('baskin_element')}
            - Eksik Element: {analysis_data.get('eksik_element')}
            - Çakra Durumu: {analysis_data.get('baskin_cakra_val')} aktif, {analysis_data.get('zayif_cakra_val')} blokajlı.

            Lütfen kısa kesme. Ona potansiyelini anlat, zayıf yönlerini nasıl güçlendireceğini söyle.
            """

            # --- YENİ KÜTÜPHANE ÇAĞRISI ---
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt
            )
            return response.text

        except Exception as e:
            return f"Yapay Zeka Hatası: {str(e)}"

    @staticmethod
    def generate_name_analysis_rag(isim: str, pdf_icerigi: str) -> str:
        """
        RAG SİSTEMİ: İsim Analizi PDF'ini okuyup yorumlayan fonksiyon.
        """
        client = AIWriter._get_client()
        if not client:
            return "HATA: Google API Anahtarı bulunamadı."

        try:
            # --- RAG PROMPT ---
            prompt = f"""
            Sen uzman bir İsim Analisti'sin.
            Elimizde şu KİTAP BİLGİSİ (CONTEXT) var:
            
            --- BAŞLANGIÇ ---
            {pdf_icerigi[:40000]} 
            --- BİTİŞ ---
            
            ANALİZ EDİLECEK KİŞİ: {isim}
            
            GÖREV:
            Yukarıdaki KİTAP BİLGİSİNİ temel alarak, bu ismin harf analizini ve genel enerjisini yorumla.
            Kitapta yazmayan bir şeyi uydurma. Çıktıyı başlıklar halinde, profesyonelce ver.
            """

            # --- YENİ KÜTÜPHANE ÇAĞRISI ---
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt
            )
            return response.text

        except Exception as e:
            return f"AI RAG Hatası: {str(e)}"