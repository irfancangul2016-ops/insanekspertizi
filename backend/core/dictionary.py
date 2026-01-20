# backend/core/dictionary.py

# Yaygın isimlerin Osmanlıca harf karşılıkları (Manuel Tanımlama)
# Bu liste zamanla büyüyecek. %100 Doğruluk için burayı besleyeceğiz.

ISIM_SOZLUGU = {
    # İSİM: [Harf Listesi]
    
    # PDF Örneği
    "YAHYA": ["ي", "ح", "ي"], # Sonunda Y var ama A okunur (Elif-i Maksure)
    "HAMZA": ["ح", "م", "ز", "ه"], # Sonu He ile biter
    "SEVİLAY": ["س", "و", "ي", "ل", "ا", "ي"], 
    
    # Yaygın Erkek İsimleri
    "MEHMET": ["م", "ح", "م", "د"], # Mim, Ha, Mim, Dal (Sesliler yok)
    "MUSTAFA": ["م", "ص", "ط", "ف", "ي"], # Sonu Y (Elif-i Maksure)
    "AHMET": ["ا", "ح", "m", "ت"],
    "ALİ": ["ع", "ل", "ي"],
    "ÖMER": ["ع", "م", "r"],
    "İBRAHİM": ["ا", "b", "r", "a", "h", "m"], # (Basitleştirilmiş)
    
    # Yaygın Kadın İsimleri
    "AYŞE": ["ع", "ا", "y", "ş", "e"], # Ayşe genelde Ayın ile başlar
    "FATMA": ["ف", "a", "t", "m", "a"],
    "ELİF": ["ا", "l", "i", "f"],
    "ZEYNEP": ["z", "y", "n", "b"] # Sonu Be ile biter
}

# Not: Buradaki harfler constants.py içindeki LATIN_TO_ARABIC anahtarlarına 
# veya doğrudan Arapça harflere karşılık gelmeli.
# Kolaylık olsun diye şimdilik sistemi karmaşıklaştırmadan 
# manuel müdahale edebileceğimiz bir "override" (ezme) yapısı kuracağız.