from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
import os

class PDFGenerator:
    def __init__(self, filename="analiz_raporu.pdf"):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Static klasörünün içine kaydetsin
        static_dir = os.path.join(base_dir, "static", "reports")
        if not os.path.exists(static_dir):
            os.makedirs(static_dir)
            
        self.filename = os.path.join(static_dir, filename)
        self.logo_path = os.path.join(base_dir, "logo.png")
        self.register_fonts()
        
    def register_fonts(self):
        try:
            # Windows için Arial fontları
            font_path = 'C:\\Windows\\Fonts\\arial.ttf'
            if os.path.exists(font_path):
                pdfmetrics.registerFont(TTFont('Arial', font_path))
                pdfmetrics.registerFont(TTFont('Arial-Bold', 'C:\\Windows\\Fonts\\arialbd.ttf'))
                self.font_regular = 'Arial'
                self.font_bold = 'Arial-Bold'
            else:
                self.font_regular = 'Helvetica'
                self.font_bold = 'Helvetica-Bold'
        except:
            self.font_regular = 'Helvetica'
            self.font_bold = 'Helvetica-Bold'

    def create_report(self, data: dict):
        doc = SimpleDocTemplate(
            self.filename, 
            pagesize=A4,
            rightMargin=2*cm, leftMargin=2*cm, 
            topMargin=2*cm, bottomMargin=2*cm
        )
        
        styles = getSampleStyleSheet()
        story = []

        # --- STİLLER ---
        style_baslik = ParagraphStyle(
            'OzelBaslik', parent=styles['Heading1'], fontName=self.font_bold, 
            fontSize=24, textColor=colors.HexColor("#1e293b"), alignment=TA_CENTER, spaceAfter=20
        )
        style_alt_baslik = ParagraphStyle(
            'AltBaslik', parent=styles['Heading2'], fontName=self.font_bold, 
            fontSize=16, textColor=colors.HexColor("#d4af37"), spaceBefore=15, spaceAfter=10
        )
        style_metin = ParagraphStyle(
            'OzelMetin', parent=styles['Normal'], fontName=self.font_regular, 
            fontSize=11, leading=16, alignment=TA_JUSTIFY, spaceAfter=8
        )
        
        # --- 1. KAPAK SAYFASI ---
        story.append(Spacer(1, 4*cm))
        if os.path.exists(self.logo_path):
            im = Image(self.logo_path, width=4*cm, height=4*cm)
            story.append(im)
        
        story.append(Spacer(1, 2*cm))
        story.append(Paragraph("KOZMİK KİMLİK ANALİZİ", style_baslik))
        story.append(Spacer(1, 1*cm))
        
        danisan = data.get('danisan_bilgisi', 'Sayın Danışan')
        story.append(Paragraph(f"Hazırlanan Kişi: {danisan}", style_metin))
        story.append(PageBreak())

        # --- 2. İÇERİK DÖNGÜSÜ ---
        bolum_sirasi = ["kimlik", "tespit", "gelecek", "recete"]
        
        basliklar = {
            "kimlik": "I. RUHSAL KİMLİK & POTANSİYEL",
            "tespit": "II. TEKNİK TESPİTLER & ENERJİ",
            "gelecek": "III. GELECEK PROJEKSİYONU",
            "recete": "IV. ŞİFA VE DÖNÜŞÜM REÇETESİ"
        }

        for bolum_kodu in bolum_sirasi:
            # Bölüm verisi var mı kontrol et
            if bolum_kodu in data and isinstance(data[bolum_kodu], dict):
                icerik = data[bolum_kodu]
                
                # Bölüm Başlığı
                story.append(Paragraph(basliklar.get(bolum_kodu, "ANALİZ"), style_alt_baslik))
                story.append(Spacer(1, 0.2*cm))

                # Tablo Verisi Hazırla
                table_data = []
                
                # Hicri Bilgi (Sadece Kimlik Bölümünde)
                if bolum_kodu == "kimlik" and 'hicri_bilgi' in data:
                    hicri = data['hicri_bilgi']
                    if isinstance(hicri, dict):
                        # Uzun satırı bölüyoruz
                        satir = [
                            Paragraph("<b>Hicri Doğum:</b>", style_metin), 
                            Paragraph(str(hicri.get('tarih_str', '-')), style_metin)
                        ]
                        table_data.append(satir)

                # Diğer Sözlük Verileri
                for k, v in icerik.items():
                    # Atlanacak anahtarlar
                    skip_keys = ["baslik", "yasakli_davranislar", "element_chart_path", "chakra_chart_path"]
                    if k in skip_keys:
                        continue
                    
                    key_readable = k.replace("_", " ").title()
                    val_readable = str(v).replace("\n", "<br/>")
                    
                    table_data.append([
                        Paragraph(f"<b>{key_readable}:</b>", style_metin), 
                        Paragraph(val_readable, style_metin)
                    ])

                # Tabloyu Sayfaya Ekle
                if table_data:
                    t = Table(table_data, colWidths=[6*cm, 10*cm])
                    t.setStyle(TableStyle([
                        ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#f8fafc")),
                        ('TEXTCOLOR', (0,0), (-1,-1), colors.HexColor("#334155")),
                        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                        ('VALIGN', (0,0), (-1,-1), 'TOP'),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.HexColor("#e2e8f0")),
                        ('BOX', (0,0), (-1,-1), 0.25, colors.HexColor("#cbd5e1")),
                        ('PADDING', (0,0), (-1,-1), 10),
                    ]))
                    story.append(t)
                    story.append(Spacer(1, 0.5*cm))

                # --- GRAFİKLER (TESPİT BÖLÜMÜ) ---
                if bolum_kodu == "tespit":
                    img_element = icerik.get('element_chart_path')
                    img_chakra = icerik.get('chakra_chart_path')
                    
                    chart_row = []
                    
                    if img_element and os.path.exists(img_element):
                        chart_row.append(Image(img_element, width=8*cm, height=4*cm))
                    
                    if img_chakra and os.path.exists(img_chakra):
                        chart_row.append(Image(img_chakra, width=7*cm, height=7*cm))
                        
                    if chart_row:
                        story.append(Spacer(1, 0.5*cm))
                        t_charts = Table([chart_row], colWidths=[9*cm, 8*cm])
                        t_charts.setStyle(TableStyle([
                            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                        ]))
                        story.append(t_charts)

                # --- AI YORUMU (REÇETE BÖLÜMÜ) ---
                if bolum_kodu == "recete" and "yasakli_davranislar" in icerik:
                    
                    # Önce AI yorumu (Varsa)
                    if "yasakli_davranislar" in icerik:
                        story.append(Spacer(1, 0.5*cm))
                        story.append(Paragraph("YAPAY ZEKA ÖZEL REHBERLİĞİ", style_alt_baslik))
                        ai_metni = icerik["yasakli_davranislar"].replace("\n", "<br/>")
                        story.append(Paragraph(ai_metni, style_metin))
                    
                    # --- SONRA QR KOD (TİCARİ FİNAL) ---
                    qr_path = icerik.get("qr_code_path")
                    if qr_path and os.path.exists(qr_path):
                        story.append(Spacer(1, 1*cm))
                        story.append(Paragraph("BU REÇETEYİ UYGULAMAK İÇİN:", style_alt_baslik)) # Aşağıda stil tanımlayacağız veya normal metin kullan
                        
                        im_qr = Image(qr_path, width=4*cm, height=4*cm)
                        story.append(im_qr)
                        story.append(Paragraph("Ürünlere ulaşmak ve randevu almak için okutunuz.", style_metin))

                    story.append(Spacer(1, 0.5*cm))
                    story.append(Paragraph("YAPAY ZEKA ÖZEL REHBERLİĞİ", style_alt_baslik))
                    ai_metni = icerik["yasakli_davranislar"].replace("\n", "<br/>")
                    story.append(Paragraph(ai_metni, style_metin))

                story.append(PageBreak())

        try:
            doc.build(story)
            return self.filename
        except Exception as e:
            print(f"PDF Build Hatası: {e}")
            return None