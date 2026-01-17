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
import google.generativeai as genai

class AIWriter:
    @staticmethod
    def generate_human_report(analysis_data: dict) -> str:
        """
        Gemini AI kullanarak kişiye özel, derinlemesine ve uzun bir rapor yazar.
        """
        api_key = os.getenv("GOOGLE_API_KEY")
        
        if not api_key:
            return "API Anahtarı bulunamadı. Lütfen sistem yöneticisi ile görüşün."

        try:
            genai.configure(api_key=api_key)
            
            # --- KRİTİK DEĞİŞİKLİK BURADA: Model İsmi Güncellendi ---
            # 'gemini-pro' eskidi. Artık 'gemini-1.5-flash' kullanıyoruz (Hızlı ve Güncel).
            model = genai.GenerativeModel('gemini-1.5-flash')

            # --- PROMPT (YAPAY ZEKA EMRİ) GÜNCELLEMESİ ---
            # Ona uzun yazmasını özellikle tembihliyoruz.
            prompt = f"""
            Sen mistik konularda uzmanlaşmış, derin bilgiye sahip, bilge bir yaşam koçusun.
            Aşağıdaki teknik analiz verilerini kullanarak, danışanına (müşteriye) okuduğunda
            etkileneceği, motive olacağı ve kendini özel hissedeceği DETAYLI BİR MEKTUP yaz.

            KİŞİ BİLGİLERİ:
            - İsim: {analysis_data.get('tam_isim')}
            - Pin Kodu: {analysis_data.get('pin')} (Bu kişinin hayattaki ana arketipi)
            - Baskın Element: {analysis_data.get('baskin_element')} (Güçlü yanı)
            - Eksik Element: {analysis_data.get('eksik_element')} (Geliştirmesi gereken yanı)
            - Çakra Durumu: {analysis_data.get('baskin_cakra_val')}. çakra çok aktif, {analysis_data.get('zayif_cakra_val')}. çakra blokajlı.
            - Bu Yılın Teması (Kişisel Yıl): {analysis_data.get('personal_year')}. yıl döngüsünde.

            KURALLAR:
            1. ASLA kısa kesme. En az 3-4 dolgun paragraf yaz.
            2. "Senin elementin Su" deyip geçme. "Su elementi baskın olduğu için duygusal derinliğin okyanuslar kadar engin..." gibi edebi betimlemeler yap.
            3. Eksik olan elementini nasıl tamamlayacağına dair somut ve uzun tavsiyeler ver.
            4. Pin kodunun (Arketipin) ona kattığı süper güçleri anlat.
            5. Yılın temasına göre onu nelerin beklediğini detaylandır (Aşk, iş, sağlık).
            6. Konuşma dilin samimi, bilge ve akıcı olsun. Robotik olma.

            Lütfen bu kişi için hayat yolculuğuna ışık tutacak o uzun rehberlik yazısını şimdi oluştur:
            """
            
            response = model.generate_content(prompt)
            return response.text

        except Exception as e:
            return f"Yapay zeka servisine ulaşırken bir hata oluştu: {str(e)}. Lütfen internet bağlantınızı veya API kotanızı kontrol edin."