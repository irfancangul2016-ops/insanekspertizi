import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.width, self.height = A4
        
        # --- FONT AYARLARI (TÜRKÇE KARAKTER ÇÖZÜMÜ) ---
        # Statik klasördeki fontu bul ve kaydet
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            font_path = os.path.join(base_dir, "static", "Roboto-Regular.ttf")
            
            if os.path.exists(font_path):
                pdfmetrics.registerFont(TTFont('TurkishFont', font_path))
                self.font_name = 'TurkishFont'
            else:
                # Font yoksa mecburen eskiye dön ama uyar
                print("UYARI: Türkçe font bulunamadı, standart font kullanılıyor.")
                self.font_name = 'Helvetica'
        except Exception as e:
            print(f"Font Hatası: {e}")
            self.font_name = 'Helvetica'

    def create_report(self, data: dict):
        c = canvas.Canvas(self.filename, pagesize=A4)
        
        # BAŞLIK
        c.setFont(self.font_name, 24)
        c.drawCentredString(self.width/2, self.height - 50, "KOZMİK KİMLİK ANALİZİ")
        
        # DANIŞAN BİLGİSİ
        c.setFont(self.font_name, 12)
        c.drawCentredString(self.width/2, self.height - 80, f"Hazırlanan Kişi: {data.get('danisan_bilgisi', 'Bilinmiyor')}")
        
        y_position = self.height - 120
        
        # ANA BÖLÜMLERİ YAZDIR
        bolumler = [
            ("I. RUHSAL KİMLİK", data.get("kisisel_analiz", {})),
            ("II. TEKNİK TESPİTLER", data.get("tespit", {})),
            ("III. GELECEK PROJEKSİYONU", data.get("gelecek", {})),
            ("IV. ŞİFA REÇETESİ", data.get("recete", {}))
        ]

        for baslik, icerik in bolumler:
            # Bölüm Başlığı
            c.setFont(self.font_name, 16)
            c.drawString(50, y_position, baslik)
            y_position -= 25
            
            c.setFont(self.font_name, 10)
            
            # İçerik Döngüsü
            if isinstance(icerik, dict):
                for k, v in icerik.items():
                    # Resim Yolları Hariç (Onları ayrıca çizeceğiz)
                    if "path" in k or "qr" in k: 
                        continue
                        
                    # Uzun metinleri sığdır (Basit Satır Kaydırma)
                    text = f"{k.replace('_', ' ').title()}: {v}"
                    if len(text) > 90:
                        # Çok uzunsa ikiye böl
                        part1 = text[:90]
                        part2 = text[90:]
                        c.drawString(50, y_position, part1)
                        y_position -= 15
                        c.drawString(70, y_position, part2)
                    else:
                        c.drawString(50, y_position, text)
                    
                    y_position -= 20
            
            # Uzun Yapay Zeka Metni (Özel İşlem)
            if baslik == "IV. ŞİFA REÇETESİ" and "yasakli_davranislar" in icerik:
                ai_text = icerik["yasakli_davranislar"]
                c.setFont(self.font_name, 14)
                y_position -= 10
                c.drawString(50, y_position, "ÖZEL YAPAY ZEKA REHBERLİĞİ:")
                y_position -= 20
                c.setFont(self.font_name, 9)
                
                # Metni paragraflara böl ve yazdır
                lines = self.wrap_text(ai_text, 90)
                for line in lines:
                    if y_position < 50: # Sayfa sonu kontrolü
                        c.showPage()
                        c.setFont(self.font_name, 9)
                        y_position = self.height - 50
                    c.drawString(50, y_position, line)
                    y_position -= 12

            y_position -= 20
            
            # GRAFİKLERİ EKLE
            if baslik == "II. TEKNİK TESPİTLER":
                if "element_chart_path" in icerik and icerik["element_chart_path"]:
                    try:
                        c.drawImage(icerik["element_chart_path"], 50, y_position - 150, width=200, height=150)
                    except: pass
                if "chakra_chart_path" in icerik and icerik["chakra_chart_path"]:
                    try:
                        c.drawImage(icerik["chakra_chart_path"], 300, y_position - 150, width=200, height=200)
                    except: pass
                y_position -= 160

            # Sayfa Sonu Kontrolü
            if y_position < 100:
                c.showPage()
                y_position = self.height - 50

        # QR KOD (En Sona)
        if "recete" in data and "qr_code_path" in data["recete"] and data["recete"]["qr_code_path"]:
            try:
                c.drawImage(data["recete"]["qr_code_path"], self.width - 150, 50, width=100, height=100)
                c.setFont(self.font_name, 8)
                c.drawString(self.width - 150, 40, "Detaylar için okutunuz")
            except: pass

        c.save()
        return self.filename

    def wrap_text(self, text, max_chars):
        """Uzun metinleri satırlara böler"""
        words = text.split()
        lines = []
        current_line = []
        current_len = 0
        
        for word in words:
            if current_len + len(word) + 1 > max_chars:
                lines.append(" ".join(current_line))
                current_line = [word]
                current_len = len(word)
            else:
                current_line.append(word)
                current_len += len(word) + 1
        if current_line:
            lines.append(" ".join(current_line))
        return lines