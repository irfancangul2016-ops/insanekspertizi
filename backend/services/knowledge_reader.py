import os
from pypdf import PdfReader

class KnowledgeReader:
    @staticmethod
    def get_isim_analizi_context():
        """
        knowledge_base/isim_analizi klasöründeki PDF'i okur ve metne çevirir.
        """
        # 1. Dosya Yolunu Bul
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        folder_path = os.path.join(base_dir, "knowledge_base", "isim_analizi")
        
        full_text = ""
        
        # Klasör var mı kontrol et
        if not os.path.exists(folder_path):
            return "UYARI: İsim Analizi klasörü bulunamadı."
            
        # 2. Klasördeki PDF'leri Tara
        files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
        
        if not files:
            return "UYARI: Klasörde PDF dosyası yok."
            
        # 3. İlk PDF'i Oku (Şimdilik tek kitap varsayıyoruz)
        pdf_path = os.path.join(folder_path, files[0])
        print(f"--> OKUNUYOR: {files[0]}")
        
        try:
            reader = PdfReader(pdf_path)
            # Sayfa sayfa oku ve birleştir
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"
            
            return full_text
        except Exception as e:
            return f"PDF Okuma Hatası: {str(e)}"