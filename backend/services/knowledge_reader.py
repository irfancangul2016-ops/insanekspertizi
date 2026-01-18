import os
import glob
from pypdf import PdfReader

class KnowledgeReader:
    @staticmethod
    def get_isim_analizi_context():
        """
        knowledge_base/isim_analizi klasöründeki PDF'i okur.
        Hata olursa açıkça sebebini söyler.
        """
        try:
            # 1. Klasör Yolunu Bul
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            target_folder = os.path.join(base_dir, "knowledge_base", "isim_analizi")
            
            print(f"--> KONTROL EDİLEN KLASÖR: {target_folder}") # Loglara yaz
            
            # Klasör yoksa oluştur (Hata vermesin)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
                return f"HATA: '{target_folder}' klasörü yoktu, şimdi oluşturdum. Lütfen içine PDF yükleyin."

            # 2. PDF Dosyalarını Ara
            pdf_files = glob.glob(os.path.join(target_folder, "*.pdf"))
            
            if not pdf_files:
                # Klasörde ne var ona bakalım (Belki dosya uzantısı yanlıştır)
                tum_dosyalar = os.listdir(target_folder)
                return f"HATA: Klasörde PDF bulunamadı. Klasördeki dosyalar: {tum_dosyalar}"
            
            # 3. İlk PDF'i Seç ve Oku
            secilen_pdf = pdf_files[0]
            print(f"--> OKUNAN DOSYA: {secilen_pdf}")
            
            text_content = ""
            reader = PdfReader(secilen_pdf)
            
            # Sayfa sayısı kontrolü
            if len(reader.pages) == 0:
                return "HATA: PDF dosyası boş veya okunamıyor."

            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    text_content += text + "\n"
            
            # Eğer metin çok kısaysa (Resim formatındaysa okuyamaz)
            if len(text_content) < 50:
                return "HATA: PDF okundu ama içinden metin çıkmadı. Dosya resim formatında taranmış olabilir. Lütfen metin içeren bir PDF yükleyin."
                
            return text_content

        except Exception as e:
            # Kritik hata durumunda detay ver
            import traceback
            traceback.print_exc()
            return f"KRİTİK HATA (Reader): {str(e)}"