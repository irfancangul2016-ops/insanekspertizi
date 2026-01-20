import unicodedata

# --- 1. EBCED VE SABİT DEĞERLER (ARTIK CORE KLASÖRÜNE GEREK YOK) ---

# Harflerin Ebced Değerleri (Standart Tablo)
EBCED_DEGERLERI = {
    'A': 1, 'B': 2, 'C': 3, 'Ç': 3, 'D': 4, 'E': 5, 'F': 80, 'G': 1000, 'Ğ': 1000,
    'H': 8, 'I': 10, 'İ': 10, 'J': 3, 'K': 20, 'L': 30, 'M': 40, 'N': 50,
    'O': 6, 'Ö': 6, 'P': 2, 'R': 200, 'S': 60, 'Ş': 300, 'T': 400, 'U': 6,
    'Ü': 6, 'V': 6, 'Y': 10, 'Z': 7
}

# Element Grupları (Harflere göre)
ELEMENTLER = {
    "ATES": ["A", "H", "T", "M", "F", "Ş", "Z"], # Öncü, Lider, Enerjik
    "TOPRAK": ["B", "D", "K", "N", "S", "R", "L"], # Sabit, Güvenilir, Pratik
    "HAVA": ["J", "Z", "K", "S", "Q", "P", "G", "Ğ"], # İletişimci, Zeki, Değişken
    "SU": ["D", "H", "L", "E", "I", "İ", "O", "Ö", "U", "Ü", "V"] # Duygusal, Sezgisel
}

# Pin Kodu Analizleri (1-9 Arası)
PIN_ANALIZLERI = {
    1: "Lider ruhlu, girişimci ve özgüven sahibisiniz. Bağımsızlık sizin için çok önemli.",
    2: "İşbirlikçi, diplomatik ve sevgi dolusunuz. Başkalarını anlama yeteneğiniz çok yüksek.",
    3: "İletişim becerileriniz kuvvetli, yaratıcı ve sosyal birisiniz. Kendinizi ifade etmeyi seviyorsunuz.",
    4: "Düzenli, disiplinli ve çalışkansınız. Güvenilirlik ve sağlamlık sizin temel taşınız.",
    5: "Özgürlüğüne düşkün, maceraperest ve değişimi seven bir yapınız var. Rutin sizi sıkar.",
    6: "Sorumluluk sahibi, koruyucu ve ailesine düşkün birisiniz. Hizmet etmek ruhunuzda var.",
    7: "Analitik, araştırmacı ve spiritüel yönü güçlü birisiniz. Yalnız kalıp düşünmeyi sevebilirsiniz.",
    8: "Güçlü, otoriter ve maddi konularda başarılısınız. Yönetim becerileriniz gelişmiştir.",
    9: "Hümanist, şefkatli ve evrensel bir bakış açısına sahipsiniz. İnsanlığa hizmet etmeyi önemsersiniz."
}

BASKIN_ELEMENT_TANIMLARI = {
    "ATES": "Ateş elementi baskınlığı size yüksek enerji, liderlik vasfı ve cesaret verir. Hızlı harekete geçersiniz.",
    "TOPRAK": "Toprak elementi baskınlığı sizi ayakları yere basan, güvenilir ve sabırlı biri yapar. Maddi güvence ararsınız.",
    "HAVA": "Hava elementi baskınlığı zeka, iletişim ve sosyalleşme ihtiyacınızı artırır. Fikirlerinizle öne çıkarsınız.",
    "SU": "Su elementi baskınlığı derin duygular, sezgiler ve empati yeteneği verir. Çevrenize karşı duyarlısınız."
}

class EbcedCalculator:
    
    @staticmethod
    def temizle_ve_buyut(metin: str) -> str:
        """Türkçe karakterleri koruyarak metni büyütür ve temizler."""
        if not metin:
            return ""
        
        # Türkçe karakter düzeltmesi
        ceviri = str.maketrans("iı", "İI")
        metin = metin.translate(ceviri).upper()
        
        # Sadece harfleri al
        temiz_metin = ""
        for harf in metin:
            if harf.isalpha():
                temiz_metin += harf
        return temiz_metin

    @staticmethod
    def calculate_ebced(isim: str) -> int:
        """Verilen ismin Ebced değerini hesaplar."""
        toplam = 0
        temiz_isim = EbcedCalculator.temizle_ve_buyut(isim)
        
        for harf in temiz_isim:
            if harf in EBCED_DEGERLERI:
                toplam += EBCED_DEGERLERI[harf]
        
        return toplam

    @staticmethod
    def calculate_pin_code(isim: str, soyisim: str, anne_adi: str) -> dict:
        """
        Kişinin PIN kodunu hesaplar.
        Formül: İsim + Soyisim + Anne Adı (Mod 9)
        """
        toplam_deger = (
            EbcedCalculator.calculate_ebced(isim) +
            EbcedCalculator.calculate_ebced(soyisim) +
            EbcedCalculator.calculate_ebced(anne_adi)
        )
        
        # Mod 9 işlemi (0 çıkarsa 9 kabul edilir)
        pin = toplam_deger % 9
        if pin == 0:
            pin = 9
            
        return {
            "pin_numarasi": pin,
            "analiz": PIN_ANALIZLERI.get(pin, "Analiz bulunamadı.")
        }

    @staticmethod
    def analyze_elements(tam_isim: str) -> dict:
        """İsimdeki harflere göre element dağılımını analiz eder."""
        temiz_isim = EbcedCalculator.temizle_ve_buyut(tam_isim)
        skorlar = {"ATES": 0, "TOPRAK": 0, "HAVA": 0, "SU": 0}
        toplam_harf = 0

        for harf in temiz_isim:
            bulundu = False
            for element, harfler in ELEMENTLER.items():
                if harf in harfler:
                    skorlar[element] += 1
                    bulundu = True
            if bulundu:
                toplam_harf += 1

        # Yüzdeleri hesapla
        yuzdeler = {}
        baskin_element = "BELIRSIZ"
        en_yuksek_skor = -1

        if toplam_harf > 0:
            for el, skor in skorlar.items():
                yuzde = int((skor / toplam_harf) * 100)
                yuzdeler[el] = yuzde
                if skor > en_yuksek_skor:
                    en_yuksek_skor = skor
                    baskin_element = el
        else:
            yuzdeler = {k: 0 for k in skorlar}

        return {
            "skorlar": skorlar,
            "yuzdeler": yuzdeler,
            "baskin_element": baskin_element,
            "element_yorumu": BASKIN_ELEMENT_TANIMLARI.get(baskin_element, "")
        }