# # backend/core/constants.py

# # 1. Temel Ebced Değerleri
# EBCED_VALUES = {
#     "ا": 1, "ب": 2, "ج": 3, "د": 4, "ه": 5, "و": 6, "ز": 7, "ح": 8, "ط": 9, "ي": 10,
#     "ك": 20, "ل": 30, "م": 40, "ن": 50, "س": 60, "ع": 70, "ف": 80, "ص": 90, "ق": 100,
#     "ر": 200, "ش": 300, "ت": 400, "ث": 500, "خ": 600, "ذ": 700, "ض": 800, "ظ": 900, "غ": 1000
# }

# # 2. Latin -> Arapça Dönüşüm
# LATIN_TO_ARABIC = {
#     "A": "ا", "B": "ب", "C": "ج", "Ç": "ج", "D": "د", "E": "ه", "F": "ف", 
#     "G": "غ", "Ğ": "غ", "H": "ح", "I": "ي", "İ": "ي", "J": "ج", "K": "ك", 
#     "L": "ل", "M": "م", "N": "ن", "O": "و", "Ö": "و", "P": "ب", "R": "ر", 
#     "S": "س", "Ş": "ش", "T": "ت", "U": "و", "Ü": "و", "V": "و", "Y": "ي", 
#     "Z": "ز", "W": "و", "X": "ك", "Q": "ق"
# }

# # 3. PIN KODU ANALİZLERİ (PDF Sayfa 8-11 Kaynaklı)
# # Kaynak: [cite: 218-334]
PIN_ANALIZLERI = {
    1: {
        "arketip": "Lider / Başlatıcı",
        "guclu_yon": "Kararlılık, özgüven, liderlik, bağımsızlık.",
        "golge_yon": "Sabırsızlık, kibir, yalnız savaşma.",
        "para_temasi": "Tek başına iş yaparak kazanır.",
        "iliski_temasi": "Dominant olur, alan ister.",
        "kader_dersi": "Sabırlı olmak ve işbirliği öğrenmek.",
        "cakra": "Taç Çakra (Birlik Bilinci)"
    },
    2: {
        "arketip": "Diplomat / Sezgisel",
        "guclu_yon": "Uyum, sezgi, ilişki zekâsı.",
        "golge_yon": "Aşırı duygusallık, alınganlık.",
        "para_temasi": "Ortaklık ve hizmet işlerinden gelir.",
        "iliski_temasi": "Duygusal bağa ihtiyaç duyar.",
        "kader_dersi": "Kendine değer vermek.",
        "cakra": "Kalp Çakrası (Sevgi Merkezi)"
    },
    3: {
        "arketip": "Yaratıcı / İfade İnsanı",
        "guclu_yon": "Neşe, yaratıcılık, konuşma ve gösteri enerjisi.",
        "golge_yon": "Dağınıklık, kararsızlık.",
        "para_temasi": "Sanat, medya, içerik üretimi.",
        "iliski_temasi": "Flört enerjisi yüksek.",
        "kader_dersi": "Disiplin öğrenmek.",
        "cakra": "Boğaz Çakrası (İfade)"
    },
    4: {
        "arketip": "Yapı Kurucu / Sistemci",
        "guclu_yon": "Düzen, disiplin, sistem kurma, derinleşme.",
        "golge_yon": "Takıntı, aşırı kontrol, sertlik, detayda boğulma.",
        "para_temasi": "Uzun vadeli, kalıcı işlerden.",
        "iliski_temasi": "Güven ister, kolay açılmaz.",
        "kader_dersi": "Esneklik ve duygusal yumuşama.",
        "cakra": "Solar Pleksus (Güç ve İrade)"
    },
    5: {
        "arketip": "Değişimci / Özgür Ruh",
        "guclu_yon": "Risk alma, özgürlük, yenilik.",
        "golge_yon": "Sıkılma, yüzeysellik, kaçış.",
        "para_temasi": "Seyahat, satış, hız gerektiren işler.",
        "iliski_temasi": "Bağlanmakta zorlanır.",
        "kader_dersi": "Kökleşmek.",
        "cakra": "Sakral Çakra (Yaratıcılık)"
    },
    6: {
        "arketip": "Koruyucu / Öğretici",
        "guclu_yon": "Sorumluluk, aile enerjisi, öğretme kapasitesi.",
        "golge_yon": "Aşırı fedakârlık, kendini unutma.",
        "para_temasi": "Hizmet ve danışmanlık.",
        "iliski_temasi": "Sadakat yüksek ama kontrol eğilimi olabilir.",
        "kader_dersi": "Kendine alan açmak.",
        "cakra": "Üçüncü Göz (Sezgi)"
    },
    7: {
        "arketip": "Bilge / Analist",
        "guclu_yon": "Zihin, analiz, derin bilgi, içe dönüş.",
        "golge_yon": "Mesafe, aşırı eleştiri, yalnızlık isteği.",
        "para_temasi": "Bilgi ve analiz üzerinden.",
        "iliski_temasi": "Soğuk görünür, geç açılır.",
        "kader_dersi": "Duygusal yakınlık.",
        "cakra": "Taç / Üçüncü Göz"
    },
    8: {
        "arketip": "Güç / Yönetici",
        "guclu_yon": "Otorite, para, güç, yönetme.",
        "golge_yon": "Kontrol hırsı, öfke, kibir.",
        "para_temasi": "Her şekilde gelir; para enerjisi en güçlü kod.",
        "iliski_temasi": "Güç dengesine çok dikkat eder.",
        "kader_dersi": "Adalet ve tevazu.",
        "cakra": "Kök Çakra (Aidiyet)"
    },
    9: {
        "arketip": "Şifacı / Ruhsal Yolcu",
        "guclu_yon": "Merhamet, iyileştirme, sanat, sezgi.",
        "golge_yon": "Kurban psikolojisi, kırılganlık.",
        "para_temasi": "Hizmet, sanat, terapi.",
        "iliski_temasi": "Derin bağ ister ama çabuk incinir.",
        "kader_dersi": "Sınır çizmek.",
        "cakra": "Tüm Çakralar (Bütünlük)"
    }
}

# # 1. Temel Ebced Değerleri
# EBCED_VALUES = {
#     "ا": 1, "ب": 2, "ج": 3, "د": 4, "ه": 5, "و": 6, "ز": 7, "ح": 8, "ط": 9, "ي": 10,
#     "ك": 20, "ل": 30, "م": 40, "ن": 50, "س": 60, "ع": 70, "ف": 80, "ص": 90, "ق": 100,
#     "ر": 200, "ش": 300, "ت": 400, "ث": 500, "خ": 600, "ذ": 700, "ض": 800, "ظ": 900, "غ": 1000
# }

# # 2. Latin -> Arapça Dönüşüm
# LATIN_TO_ARABIC = {
#     "A": "ا", "B": "ب", "C": "ج", "Ç": "ج", "D": "د", "E": "ه", "F": "ف", 
#     "G": "غ", "Ğ": "غ", "H": "ح", "I": "ي", "İ": "ي", "J": "ج", "K": "ك", 
#     "L": "ل", "M": "م", "N": "ن", "O": "و", "Ö": "و", "P": "ب", "R": "ر", 
#     "S": "س", "Ş": "ش", "T": "ت", "U": "و", "Ü": "و", "V": "و", "Y": "ي", 
#     "Z": "ز", "W": "و", "X": "ك", "Q": "ق"
# }

# # 3. PIN KODU ANALİZLERİ (Ders 1 Kaynaklı)
# PIN_ANALIZLERI = {
#     1: {"arketip": "Lider", "guclu_yon": "Kararlılık, özgüven", "golge_yon": "Kibir, sabırsızlık", "cakra": "Taç"},
#     2: {"arketip": "Diplomat", "guclu_yon": "Sezgi, uyum", "golge_yon": "Aşırı duygusallık", "cakra": "Kalp"},
#     3: {"arketip": "Yaratıcı", "guclu_yon": "İfade, neşe", "golge_yon": "Dağınıklık", "cakra": "Boğaz"},
#     4: {"arketip": "Sistemci", "guclu_yon": "Disiplin, düzen", "golge_yon": "Takıntı, kontrolcülük", "cakra": "Solar Pleksus"},
#     5: {"arketip": "Özgür Ruh", "guclu_yon": "Değişim, hız", "golge_yon": "Maymun iştahlılık", "cakra": "Sakral"},
#     6: {"arketip": "Koruyucu", "guclu_yon": "Sorumluluk, aile", "golge_yon": "Kendini feda etme", "cakra": "Üçüncü Göz"},
#     7: {"arketip": "Bilge", "guclu_yon": "Analiz, derinlik", "golge_yon": "Soğukluk, mesafe", "cakra": "Taç/3.Göz"},
#     8: {"arketip": "Yönetici", "guclu_yon": "Güç, otorite", "golge_yon": "Hırs, öfke", "cakra": "Kök"},
#     9: {"arketip": "Şifacı", "guclu_yon": "Merhamet, sanat", "golge_yon": "Kurban psikolojisi", "cakra": "Tüm Çakralar"}
# }

# # [cite_start]4. HARF - ÇAKRA EŞLEŞMESİ (Ders 2 Kaynaklı - Sayfa 6-10) [cite: 509-640]
# # Her harfin hangi çakraya ait olduğu
# HARF_CAKRA_MAP = {
#     # 1. Kök Çakra (Toprak, Güven)
#     "ا": 1, "ء": 1, "د": 1, "ذ": 1, "ر": 1, "ز": 1, 
#     # 2. Sakral Çakra (Yaratıcılık, İlişki)
#     "ب": 2, "ف": 2, "م": 2, "و": 2,
#     # 3. Solar Pleksus (İrade, Güç)
#     "ج": 3, "ك": 3, "ق": 3, "ص": 3, "ض": 3,
#     # 4. Kalp Çakrası (Sevgi, Duygu)
#     "ح": 4, "خ": 4, "ع": 4, "غ": 4,
#     # 5. Boğaz Çakrası (İfade)
#     "ط": 5, "ت": 5, "ث": 5, "ظ": 5, 
#     # [cite_start]6. Üçüncü Göz (Zihin, Analiz) [cite: 612-630]
#     "س": 6, "ش": 6, "ي": 6, "ن": 6,
#     # [cite_start]7. Taç Çakra (Ruhsallık) [cite: 631-640]
#     "ل": 7, "ه": 7
# }

# # Çakra İsimleri ve Temaları
# CAKRA_ISIMLERI = {
#     1: "Kök Çakra (Maddi Güven & Aile)",
#     2: "Sakral Çakra (Üretkenlik & İlişki)",
#     3: "Solar Pleksus (İrade & Güç)",
#     4: "Kalp Çakrası (Sevgi & Şefkat)",
#     5: "Boğaz Çakrası (İfade & İletişim)",
#     6: "Üçüncü Göz (Analiz & Sezgi)",
#     7: "Taç Çakra (Maneviyat & Vizyon)"
# }

# # [cite_start]5. KÖK ÇAKRA ANALİZ KURALLARI (Ders 2 - Sayfa 13-14) [cite: 746-756]
# def get_kok_yorumu(adet):
#     if adet <= 1:
#         return "DÜŞÜK KÖK ENERJİSİ: Hayat zemini zayıf olabilir. Para ve güven konularında dalgalanma yaşanır. Enerji bedene inmekte zorlanır, zihinde kalır."
#     elif adet <= 4:
#         return "DENGELİ KÖK ENERJİSİ: Güven hissi yerinde. Maddi akış stabil. Hayat zemini sağlam."
#     else:
#         return "AŞIRI KÖK ENERJİSİ: Değişime dirençli, sabit ve garantici bir yapı. Esneklik kazanmalı."

# 1. Temel Ebced Değerleri
# backend/core/constants.py

# 1. Temel Ebced Değerleri
# EBCED_VALUES = {
#     "ا": 1, "ب": 2, "ج": 3, "د": 4, "ه": 5, "و": 6, "ز": 7, "ح": 8, "ط": 9, "ي": 10,
#     "ك": 20, "ل": 30, "م": 40, "ن": 50, "س": 60, "ع": 70, "ف": 80, "ص": 90, "ق": 100,
#     "ر": 200, "ش": 300, "ت": 400, "ث": 500, "خ": 600, "ذ": 700, "ض": 800, "ظ": 900, "غ": 1000
# }

# # 2. Latin -> Arapça Dönüşüm
# LATIN_TO_ARABIC = {
#     "A": "ا", "B": "ب", "C": "ج", "Ç": "ج", "D": "د", "E": "ه", "F": "ف", 
#     "G": "غ", "Ğ": "غ", "H": "ح", "I": "ي", "İ": "ي", "J": "ج", "K": "ك", 
#     "L": "ل", "M": "م", "N": "ن", "O": "و", "Ö": "و", "P": "ب", "R": "ر", 
#     "S": "س", "Ş": "ش", "T": "ت", "U": "و", "Ü": "و", "V": "و", "Y": "ي", 
#     "Z": "ز", "W": "و", "X": "ك", "Q": "ق"
# }

# # 3. PIN KODU ANALİZLERİ
# PIN_ANALIZLERI = {
#     1: {"arketip": "Lider", "guclu_yon": "Kararlılık", "golge_yon": "Kibir", "cakra": "Taç"},
#     2: {"arketip": "Diplomat", "guclu_yon": "Sezgi", "golge_yon": "Alınganlık", "cakra": "Kalp"},
#     3: {"arketip": "Yaratıcı", "guclu_yon": "İfade", "golge_yon": "Dağınıklık", "cakra": "Boğaz"},
#     4: {"arketip": "Sistemci", "guclu_yon": "Disiplin", "golge_yon": "Takıntı", "cakra": "Solar Pleksus"},
#     5: {"arketip": "Özgür Ruh", "guclu_yon": "Değişim", "golge_yon": "Maymun iştahlılık", "cakra": "Sakral"},
#     6: {"arketip": "Koruyucu", "guclu_yon": "Sorumluluk", "golge_yon": "Kendini feda", "cakra": "Üçüncü Göz"},
#     7: {"arketip": "Bilge", "guclu_yon": "Analiz", "golge_yon": "Soğukluk", "cakra": "Taç/3.Göz"},
#     8: {"arketip": "Yönetici", "guclu_yon": "Güç", "golge_yon": "Hırs", "cakra": "Kök"},
#     9: {"arketip": "Şifacı", "guclu_yon": "Merhamet", "golge_yon": "Kurban psikolojisi", "cakra": "Tüm Çakralar"}
# }

# # 4. HARF - ÇAKRA EŞLEŞMESİ (Ders 3 Güncellemesi)
# HARF_CAKRA_MAP = {
#     "ا": 1, "ء": 1, "د": 1, "ذ": 1, "ر": 1, "ز": 1, # Kök (Satürn/Toprak)
#     "ب": 2, "ف": 2, "م": 2, "و": 2,                 # Sakral (Venüs/Su)
#     "ج": 3, "ك": 3, "ق": 3, "ص": 3, "ض": 3,         # Solar (Mars/Ateş)
#     "ح": 4, "خ": 4, "ع": 4, "غ": 4,                 # Kalp (Ay/Hava)
#     "ط": 5, "ت": 5, "ث": 5, "ظ": 5,                 # Boğaz (Merkür/Eter)
#     "س": 6, "ش": 6, "ي": 6, "ن": 6,                 # 3.Göz (Jüpiter/Işık)
#     "ل": 7, "ه": 7                                  # Taç (Güneş/Ruh)
# }

# # [cite_start]5. ÇAKRA DETAYLARI (PDF Ders 3 - Sayfa 1-4) [cite: 929-1005]
# # Her çakranın Gezegeni, Elementi, Nefes Mertebesi ve Anlamı
# CAKRA_DETAYLARI = {
#     1: {
#         "isim": "Kök Çakra",
#         "gezegen": "Satürn",
#         "element": "Toprak",
#         "nefes": "Nefs-i Emmare (Beden)",
#         "konu": "Hayat gücü, güven, soy enerjisi",
#         "eksik_yorum": "Güvensizlik hissi, köklerden kopukluk, para akışında dalgalanma.",
#         "fazla_yorum": "Sağlam, dayanıklı ama değişime kapalı, risk almayan yapı."
#     },
#     2: {
#         "isim": "Sakral Çakra",
#         "gezegen": "Venüs",
#         "element": "Su",
#         "nefes": "Nefs-i Levvame (Arzu)",
#         "konu": "Cinsellik, üretim, zevk, bolluk",
#         "eksik_yorum": "Ekonomik akış düzensiz, yaşam enerjisi ve üretim tıkanık.",
#         "fazla_yorum": "Karizma, yaratım gücü yüksek, ilişkilerde etkin."
#     },
#     3: {
#         "isim": "Solar Pleksus",
#         "gezegen": "Mars",
#         "element": "Ateş",
#         "nefes": "Nefs-i Mulhime (Ego/Güç)",
#         "konu": "İrade, ego, güç, savaşma ruhu",
#         "eksik_yorum": "Kararsızlık, çabuk pes etme, kendini savunmada zayıflık.",
#         "fazla_yorum": "Domine eden, yönetici, baskın karakter."
#     },
#     4: {
#         "isim": "Kalp Çakrası",
#         "gezegen": "Ay",
#         "element": "Hava",
#         "nefes": "Nefs-i Mutmainne (Duygu)",
#         "konu": "Duygu, şefkat, bağlanma",
#         "eksik_yorum": "Mesafe, duyguyu geç ifade etme, kırgınlık biriktirme.",
#         "fazla_yorum": "Duygusal yoğunluk, hassasiyet, sevgi gücü yüksek."
#     },
#     5: {
#         "isim": "Boğaz Çakrası",
#         "gezegen": "Merkür",
#         "element": "Eter",
#         "nefes": "Nefs-i Râdiye (İfade)",
#         "konu": "İfade, iletişim, doğruluk",
#         "eksik_yorum": "Konuşma tıkanmaları, ifade kaygısı, kendini anlatamama.",
#         "fazla_yorum": "Hitabet güçlü, ikna kabiliyeti yüksek, öğretici."
#     },
#     6: {
#         "isim": "Üçüncü Göz",
#         "gezegen": "Jüpiter",
#         "element": "Işık",
#         "nefes": "Nefs-i Marziyye (Zihin)",
#         "konu": "Sezgi, analiz, zihin gücü",
#         "eksik_yorum": "Zihinsel karışıklık, karar karmaşası, odak sorunları.",
#         "fazla_yorum": "Zeka yüksekliği, stratejik akıl, sezgi açıklığı."
#     },
#     7: {
#         "isim": "Taç Çakra",
#         "gezegen": "Güneş",
#         "element": "Ruh",
#         "nefes": "Nefs-i Kâmile (İlham)",
#         "konu": "İlahi akış, kader, ilham",
#         "eksik_yorum": "Amaçsızlık, yön kaybı, nasip kapılarında gecikme.",
#         "fazla_yorum": "Sezgi kuvveti, misyon duygusu, ruhsal liderlik."
#     }
# }


# backend/core/constants.py

# 1. Temel Ebced Değerleri
# backend/core/constants.py

# 1. Temel Ebced Değerleri
# backend/core/constants.py

# --- MEVCUT EBCED VERİLERİ (DEĞİŞMEDİ) ---
# EBCED_VALUES = {
#     "ا": 1, "ب": 2, "ج": 3, "د": 4, "ه": 5, "و": 6, "ز": 7, "ح": 8, "ط": 9, "ي": 10,
#     "ك": 20, "ل": 30, "م": 40, "ن": 50, "س": 60, "ع": 70, "ف": 80, "ص": 90, "ق": 100,
#     "ر": 200, "ش": 300, "ت": 400, "ث": 500, "خ": 600, "ذ": 700, "ض": 800, "ظ": 900, "غ": 1000
# }

# LATIN_TO_ARABIC = {
#     "A": "ا", "B": "ب", "C": "ج", "Ç": "ج", "D": "د", "E": "ه", "F": "ف", 
#     "G": "غ", "Ğ": "غ", "H": "ح", "I": "ي", "İ": "ي", "J": "ج", "K": "ك", 
#     "L": "ل", "M": "م", "N": "ن", "O": "و", "Ö": "و", "P": "ب", "R": "ر", 
#     "S": "س", "Ş": "ش", "T": "ت", "U": "و", "Ü": "و", "V": "و", "Y": "ي", 
#     "Z": "ز", "W": "و", "X": "ك", "Q": "ق"
# }

# # --- DERS 5: İLİŞKİ UYUM TABLOSU (PDF Sayfa 1-2 & 14-15) ---
# # Pin kodlarının birbirleriyle etkileşimi
# PIN_UYUMU = {
#     # Genel Kurallar (Özel eşleşme yoksa bunlar çalışır)
#     "ayni": "AYNI FREKANS: Güçlü başlangıç ama zamanla sıkıcılık veya çatışma olabilir. (Ayna etkisi)",
#     "komsu": "DOĞAL ÇEKİM: Birbirini tamamlayan, akışkan enerji (Örn: 3-4, 4-5).",
#     "zit": "YÜKSEK ÇEKİM & ÇATIŞMA: Zıt kutuplar birbirini çeker ama yönetmesi zordur (Örn: 1-8, 2-7).",
    
#     # Özel Kombinasyonlar (PDF'ten)
#     "4-2": "GÜVEN VE DENGE: Pin 2, Pin 4'ü yumuşatır. En iyi eşleşmelerden biri.",
#     "4-6": "AİLE KURMA: Uzun ömürlü, sadakat ve sorumluluk temelli ilişki.",
#     "4-8": "GÜÇ VE PARA: Maddi başarı ve verimli ortaklık. İmparatorluk kurar.",
#     "4-4": "STABİL AMA SIKICI: Güven tamdır ama heyecan eksik kalabilir.",
#     "4-5": "SÜREKLİ ÇATIŞMA: Düzen (4) ile Kaos (5) savaşı. Yorucu olabilir.",
#     "4-7": "DUYGUSAL MESAFE: İki taraf da zihinde yaşar. Kalp bağı zayıf kalabilir.",
#     "4-9": "YOĞUN AMA YIPRATICI: Geçici tutku, uzun vadede anlaşmazlık.",
    
#     # Diğer Örnekler
#     "3-7": "ZIT KUTUP: İletişim (3) ve Gizem (7). İlk başta çeker, sonra kopukluk olabilir.",
#     "1-1": "LİDERLER SAVAŞI: İki taraf da yönetmek ister.",
#     "2-6": "İDEAL EVLİLİK: Sevgi, uyum ve aile odaklı.",
#     "5-7": "ZİHİNSEL MACERA: Özgürlük ve derinlik. Bağlanma sorunu olabilir."
# }

# # --- DERS 5: BEREKET SAYISI (PDF Sayfa 4) ---
# # Ebced Toplamı -> Tek Hane
# BEREKET_SAYISI = {
#     1: "Liderlik ve girişimden gelen kazanç.",
#     2: "Ortaklık ve destekle büyüyen bereket.",
#     3: "Sanat, iletişim ve sahne işlerinden gelen para.",
#     4: "Sabit, düzenli ve garantili gelir.",
#     5: "HAREKET BEREKETİ: Ticaret, seyahat ve değişimden gelen fırsatlar.",
#     6: "Aile işi, hizmet sektörü ve gayrimenkul kazancı.",
#     7: "Bilgi, uzmanlık ve analizden gelen kazanç.",
#     8: "BÜYÜK PARA: Yatırım, yönetim ve güçten gelen servet.",
#     9: "Hizmet, yardım ve uluslararası işlerden gelen nasip."
# }

# # --- ELEMENT UYUMU (PDF Sayfa 3-4) ---
# ELEMENT_UYUMU = {
#     ("Ateş", "Hava"): "YÜKSEK UYUM: Hava ateşi besler. (Tutku + İletişim)",
#     ("Toprak", "Su"): "DENGELİ UYUM: Su toprağı besler. (Güven + Duygu)",
#     ("Ateş", "Su"): "ZORLAYICI: Su ateşi söndürür veya ateş suyu buharlaştırır. (Çatışma)",
#     ("Hava", "Toprak"): "YAVAŞ GELİŞEN: Biri uçar, biri tutar. Anlaşmak zaman alır.",
#     ("Ateş", "Ateş"): "EGO SAVAŞI: Yüksek enerji ama çabuk tükenme.",
#     ("Su", "Su"): "AŞIRI DUYGUSAL: Mantık devre dışı kalabilir.",
#     ("Hava", "Hava"): "ZİHİNSEL AKIŞ: Çok konuşulur ama icraat az olabilir.",
#     ("Toprak", "Toprak"): "GARANTİCİ: Çok sağlam ama durağan."
# }

# # --- ESKİ VERİLER (AYNEN KORUNDU) ---
# PIN_ANALIZLERI = {
#     1: {"arketip": "Lider", "guclu_yon": "Kararlılık", "cakra": "Taç"},
#     2: {"arketip": "Diplomat", "guclu_yon": "Sezgi", "cakra": "Kalp"},
#     3: {"arketip": "Yaratıcı", "guclu_yon": "İfade", "cakra": "Boğaz"},
#     4: {"arketip": "Sistemci", "guclu_yon": "Disiplin", "cakra": "Solar Pleksus"},
#     5: {"arketip": "Özgür Ruh", "guclu_yon": "Değişim", "cakra": "Sakral"},
#     6: {"arketip": "Koruyucu", "guclu_yon": "Sorumluluk", "cakra": "Üçüncü Göz"},
#     7: {"arketip": "Bilge", "guclu_yon": "Analiz", "cakra": "Taç/3.Göz"},
#     8: {"arketip": "Yönetici", "guclu_yon": "Güç", "cakra": "Kök"},
#     9: {"arketip": "Şifacı", "guclu_yon": "Merhamet", "cakra": "Tüm Çakralar"}
# }

# HARF_CAKRA_MAP = {
#     "ا": 1, "ء": 1, "د": 1, "ذ": 1, "ر": 1, "ز": 1,
#     "ب": 2, "ف": 2, "م": 2, "و": 2,
#     "ج": 3, "ك": 3, "ق": 3, "ص": 3, "ض": 3,
#     "ح": 4, "خ": 4, "ع": 4, "غ": 4,
#     "ط": 5, "ت": 5, "ث": 5, "ظ": 5,
#     "س": 6, "ش": 6, "ي": 6, "ن": 6,
#     "ل": 7, "ه": 7
# }

# CAKRA_DETAYLARI = {
#     1: {"isim": "Kök Çakra", "gezegen": "Satürn", "element": "Toprak"},
#     2: {"isim": "Sakral Çakra", "gezegen": "Venüs", "element": "Su"},
#     3: {"isim": "Solar Pleksus", "gezegen": "Mars", "element": "Ateş"},
#     4: {"isim": "Kalp Çakrası", "gezegen": "Ay", "element": "Hava"},
#     5: {"isim": "Boğaz Çakrası", "gezegen": "Merkür", "element": "Eter"},
#     6: {"isim": "Üçüncü Göz", "gezegen": "Jüpiter", "element": "Işık"},
#     7: {"isim": "Taç Çakra", "gezegen": "Güneş", "element": "Ruh"}
# }

# YASAM_YOLU_ANALIZLERI = {
#     1: {"element": "Ateş", "anahtar": "Liderlik"},
#     2: {"element": "Su", "anahtar": "Denge"},
#     3: {"element": "Ateş", "anahtar": "İfade"},
#     4: {"element": "Toprak", "anahtar": "Düzen"},
#     5: {"element": "Hava", "anahtar": "Özgürlük"},
#     6: {"element": "Toprak", "anahtar": "Sorumluluk"},
#     7: {"element": "Su", "anahtar": "Bilgelik"},
#     8: {"element": "Ateş/Toprak", "anahtar": "Güç"},
#     9: {"element": "Ateş/Su", "anahtar": "Evrensel"}
# }

# KISISEL_YIL_ANALIZLERI = {
#     1: "BAŞLANGIÇ YILI", 2: "İŞBİRLİĞİ YILI", 3: "SOSYAL YIL",
#     4: "ÇALIŞMA YILI", 5: "DEĞİŞİM YILI", 6: "AİLE YILI",
#     7: "İÇE DÖNÜŞ YILI", 8: "GÜÇ VE PARA YILI", 9: "BİTİŞ YILI"
# }


# 1. TEMEL EBCED DEĞERLERİ (Ders 1)
# backend/core/constants.py

# --- DERS 1 & 2: EBCED VE HARFLER ---
# backend/core/constants.py

# --- DERS 1 & 2: EBCED VE HARFLER ---
# backend/core/constants.py

# backend/core/constants.py

# --- DERS 1 & 2: EBCED VE HARFLER ---
# backend/core/constants.py

# --- DERS 1 & 2: EBCED VE HARFLER ---
# backend/core/constants.py

# --- DERS 1 & 2: EBCED VE HARFLER ---
# backend/core/constants.py

# --- DERS 1 & 2: EBCED VE HARFLER ---
# backend/core/constants.py

# --- DERS 1 & 2: EBCED VE HARFLER ---
# backend/core/constants.py

# --- DERS 1 & 2: EBCED VE HARFLER ---
# backend/core/constants.py

# --- DERS 1 & 2: EBCED VE HARFLER ---
EBCED_VALUES = {
    "ا": 1, "ب": 2, "ج": 3, "د": 4, "ه": 5, "و": 6, "ز": 7, "ح": 8, "ط": 9, "ي": 10,
    "ك": 20, "ل": 30, "م": 40, "ن": 50, "س": 60, "ع": 70, "ف": 80, "ص": 90, "ق": 100,
    "ر": 200, "ش": 300, "ت": 400, "ث": 500, "خ": 600, "ذ": 700, "ض": 800, "ظ": 900, "غ": 1000,
    "گ": 20, "پ": 2, "ç": 3
}

LATIN_TO_ARABIC = {
    "A": "ا", "B": "ب", "C": "ج", "Ç": "ç", "D": "د", "E": "ه", "F": "ف", 
    "G": "گ", "Ğ": "غ", "H": "ح", "I": "ي", "İ": "ي", "J": "ج", "K": "ك", 
    "L": "ل", "M": "م", "N": "ن", "O": "و", "Ö": "و", "P": "پ", "R": "ر", 
    "S": "س", "Ş": "ش", "T": "ت", "U": "و", "Ü": "و", "V": "و", "Y": "ي", 
    "Z": "ز", "W": "و", "X": "ك", "Q": "ق"
}

# --- DERS 1: PIN KODU ANALİZLERİ ---
PIN_ANALIZLERI = {
    1: {"arketip": "Lider", "guclu_yon": "Kararlılık, özgüven ve başlatma enerjisi", "golge_yon": "Kibir, sabırsızlık ve bencillik", "cakra": "Taç Çakra"},
    2: {"arketip": "Diplomat", "guclu_yon": "Sezgi, uyum ve arabuluculuk", "golge_yon": "Alınganlık, aşırı duygu ve bağımlılık", "cakra": "Kalp Çakrası"},
    3: {"arketip": "Yaratıcı", "guclu_yon": "İfade, neşe ve sahne ışığı", "golge_yon": "Dağınıklık, yüzeysellik ve dedikodu", "cakra": "Boğaz Çakrası"},
    4: {"arketip": "Sistemci", "guclu_yon": "Disiplin, düzen ve inşaa etme", "golge_yon": "Takıntı, kontrolcülük ve esnememe", "cakra": "Solar Pleksus"},
    5: {"arketip": "Özgür Ruh", "guclu_yon": "Değişim, hız ve adaptasyon", "golge_yon": "Maymun iştahlılık, kaçış ve sorumsuzluk", "cakra": "Sakral Çakra"},
    6: {"arketip": "Koruyucu", "guclu_yon": "Sorumluluk, aile ve hizmet", "golge_yon": "Kendini feda etme ve mükemmeliyetçilik", "cakra": "Üçüncü Göz"},
    7: {"arketip": "Bilge", "guclu_yon": "Analiz, derinlik ve ruhsallık", "golge_yon": "Soğukluk, mesafe ve şüphecilik", "cakra": "Taç/3.Göz"},
    8: {"arketip": "Yönetici", "guclu_yon": "Güç, otorite ve finansal zeka", "golge_yon": "Hırs, öfke, baskı ve materyalizm", "cakra": "Kök Çakra"},
    9: {"arketip": "Şifacı", "guclu_yon": "Merhamet, sanat ve evrensellik", "golge_yon": "Kurban psikolojisi ve hayalperestlik", "cakra": "Tüm Çakralar"}
}

# --- DERS 2 & 3: ÇAKRA VE HARF İLİŞKİSİ ---
HARF_CAKRA_MAP = {
    "ا": 1, "ء": 1, "د": 1, "ذ": 1, "ر": 1, "ز": 1, 
    "ب": 2, "ف": 2, "م": 2, "و": 2, "پ": 2,         
    "ج": 3, "ك": 3, "ق": 3, "ص": 3, "ض": 3, "گ": 3, 
    "ح": 4, "خ": 4, "ع": 4, "غ": 4,                 
    "ط": 5, "ت": 5, "ث": 5, "ظ": 5,                 
    "س": 6, "ش": 6, "ي": 6, "ن": 6,                 
    "ل": 7, "ه": 7                                  
}

CAKRA_DETAYLARI = {
    1: {"isim": "Kök Çakra", "gezegen": "Satürn", "element": "Toprak", "nefes": "Nefs-i Emmare", "eksik_yorum": "Güvensizlik hissi, köklerden kopukluk ve maddi kaygılar.", "fazla_yorum": "Sağlam ama değişime kapalı, inatçı yapı."},
    2: {"isim": "Sakral Çakra", "gezegen": "Venüs", "element": "Su", "nefes": "Nefs-i Levvame", "eksik_yorum": "Üretim tıkanıklığı, yaşam enerjisi düşüklüğü.", "fazla_yorum": "Yaratım gücü yüksek, çekici ve haz odaklı."},
    3: {"isim": "Solar Pleksus", "gezegen": "Mars", "element": "Ateş", "nefes": "Nefs-i Mulhime", "eksik_yorum": "Kararsızlık, kendini savunamama ve özgüven eksikliği.", "fazla_yorum": "Baskın, yönetici karakter ve kontrol tutkusu."},
    4: {"isim": "Kalp Çakrası", "gezegen": "Ay", "element": "Hava", "nefes": "Nefs-i Mutmainne", "eksik_yorum": "Duygusal mesafe, kırgınlık ve affedememe.", "fazla_yorum": "Empati ve sevgi gücü yüksek, şifacı yapı."},
    5: {"isim": "Boğaz Çakrası", "gezegen": "Merkür", "element": "Eter", "nefes": "Nefs-i Râdiye", "eksik_yorum": "Kendini anlatamama, tıkanıklık ve içe atma.", "fazla_yorum": "İkna kabiliyeti yüksek, hatip ve etkileyici."},
    6: {"isim": "Üçüncü Göz", "gezegen": "Jüpiter", "element": "Işık", "nefes": "Nefs-i Marziyye", "eksik_yorum": "Zihinsel karışıklık, odaksızlık ve vizyon eksikliği.", "fazla_yorum": "Stratejik zeka, yüksek sezgi ve analiz yeteneği."},
    7: {"isim": "Taç Çakra", "gezegen": "Güneş", "element": "Ruh", "nefes": "Nefs-i Kâmile", "eksik_yorum": "Amaçsızlık, yön kaybı ve manevi boşluk.", "fazla_yorum": "Misyon duygusu, ruhsal liderlik ve bütünlük hissi."}
}

# --- DERS 4: YAŞAM YOLU VE ZAMANLAMA ---
YASAM_YOLU_ANALIZLERI = {
    1: {"baslik": "Lider", "element": "Ateş", "anahtar": "Başlatma", "guclu": "Yönetme, risk alma", "zayif": "Bencillik", "kader": "Yalnız savaşma hissi ile sınanır."},
    2: {"baslik": "Diplomat", "element": "Su", "anahtar": "Denge", "guclu": "Empati, diplomasi", "zayif": "Alınganlık", "kader": "İlişkiler ve hayır diyebilme sınavı."},
    3: {"baslik": "Yaratıcı", "element": "Ateş", "anahtar": "İfade", "guclu": "Hitabet, sanat", "zayif": "Dağınıklık", "kader": "İfade etmezsen patlarsın."},
    4: {"baslik": "Sistemci", "element": "Toprak", "anahtar": "Düzen", "guclu": "Planlama, sabır", "zayif": "Katılık", "kader": "Temel atmayan ilerleyemez."},
    5: {"baslik": "Özgür Ruh", "element": "Hava", "anahtar": "Değişim", "guclu": "Esneklik, keşif", "zayif": "Sıkılma", "kader": "Ani değişimler ve seyahatler."},
    6: {"baslik": "Sorumlu", "element": "Toprak", "anahtar": "Hizmet", "guclu": "Koruma, aile", "zayif": "Fedakarlık", "kader": "Aile karması ve sınır koyma."},
    7: {"baslik": "Bilge", "element": "Su", "anahtar": "Analiz", "guclu": "Sezgi, detay", "zayif": "Şüphecilik", "kader": "Dışarıya değil, içeri bak."},
    8: {"baslik": "Güçlü", "element": "Ateş/Toprak", "anahtar": "Otorite", "guclu": "Para, yönetim", "zayif": "Baskı", "kader": "Ektiğini biçersin, güç sınavı."},
    9: {"baslik": "Hümanist", "element": "Ateş/Su", "anahtar": "Evrensel", "guclu": "Şifa, sanat", "zayif": "Dram", "kader": "Bırakmayı öğrenmek, tamamlanma."}
}

KISISEL_YIL_ANALIZLERI = {
    1: "BAŞLANGIÇ YILI: Tohum atma zamanı.",
    2: "İŞBİRLİĞİ YILI: Sabır ve ortaklık zamanı.",
    3: "SOSYAL YIL: Eğlence ve ifade zamanı.",
    4: "ÇALIŞMA YILI: Temel atma ve disiplin zamanı.",
    5: "DEĞİŞİM YILI: Sürprizler ve özgürleşme zamanı.",
    6: "AİLE YILI: Yuva ve sorumluluk zamanı.",
    7: "İÇE DÖNÜŞ YILI: Analiz ve ruhsal gelişim zamanı.",
    8: "GÜÇ VE PARA YILI: Kariyer ve maddi hasat zamanı.",
    9: "BİTİŞ YILI: Temizlik ve sadeleşme zamanı."
}

# --- DERS 5: İLİŞKİ UYUMU ---
PIN_UYUMU = {
    "ayni": "AYNI FREKANS: Güçlü başlangıç ama zamanla rekabet olabilir.",
    "komsu": "DOĞAL ÇEKİM: Enerjiler birbirini tamamlar.",
    "zit": "YÜKSEK TUTKU VE ÇATIŞMA: Zıt kutupların çekimi.",
    "4-2": "GÜVEN VE DENGE (Mükemmel)",
    "4-6": "AİLE KURMA (Uzun vadeli)",
    "4-8": "GÜÇ VE PARA (İmparatorluk)"
}

BEREKET_SAYISI_OZET = {
    1: "Liderlik Kazancı", 2: "Ortaklık Kazancı", 3: "Sanat/İletişim Kazancı",
    4: "Sabit Gelir", 5: "Ticaret/Fırsat Kazancı", 6: "Hizmet/Aile Kazancı",
    7: "Uzmanlık Kazancı", 8: "Büyük Yatırım Kazancı", 9: "Evrensel Hizmet Kazancı"
}

ELEMENT_UYUMU = {
    ("Ateş", "Hava"): "YÜKSEK UYUM (Besleyici)",
    ("Toprak", "Su"): "DENGELİ UYUM (Verimli)",
    ("Ateş", "Su"): "ZORLAYICI (Çatışmalı)",
    ("Hava", "Toprak"): "YAVAŞ GELİŞEN (Ağır)"
}

# --- DERS 6: BEREKET DETAYLARI ---
BEREKET_ANALIZLERI = {
    1: {"baslik": "KÖK BEREKETİ (Girişimci)", "para_yolu": "Girişimcilik, risk alma.", "risk": "Disiplin yoksa para uçar.", "dongu": "Dalgalı ama hızlı."},
    2: {"baslik": "AKIŞ BEREKETİ (Ortaklık)", "para_yolu": "Ortak işler, diplomasi.", "risk": "Duygusal kararlar.", "dongu": "Yavaş ama stabil."},
    3: {"baslik": "İFADE BEREKETİ (Sosyal)", "para_yolu": "İletişim, eğitim.", "risk": "Dağınıklık.", "dongu": "Dönemsel patlamalar."},
    4: {"baslik": "SİSTEM BEREKETİ (Birikim)", "para_yolu": "Sabit gelir, gayrimenkul.", "risk": "Aşırı kontrol.", "dongu": "Yavaş ama sürekli yükselen."},
    5: {"baslik": "DEĞİŞİM BEREKETİ (Ticaret)", "para_yolu": "Satış, ticaret.", "risk": "Plansızlık.", "dongu": "Hızlı kazanma - hızlı tüketme."},
    6: {"baslik": "HİZMET BEREKETİ (Estetik)", "para_yolu": "Güzellik, danışmanlık.", "risk": "Başkaları için harcama.", "dongu": "Duygusal duruma bağlı."},
    7: {"baslik": "SPİRİTÜEL BEREKET (Analiz)", "para_yolu": "Uzmanlık, analiz.", "risk": "Maddiyattan kopukluk.", "dongu": "Yavaş ama derin."},
    8: {"baslik": "GÜÇ BEREKETİ (Yönetim)", "para_yolu": "Yatırım, yönetim.", "risk": "Güç savaşları.", "dongu": "Yüksek gelgitler ama yüksek tavan."},
    9: {"baslik": "EVRENSEL BEREKET (Tamamlama)", "para_yolu": "Uluslararası işler.", "risk": "Dağıtma isteği.", "dongu": "Döngüsel."}
}

# --- DERS 7: DÖNÜŞÜM YILLARI ---
DONUSUM_YILLARI_TEMALARI = {
    1: {"tema": "BAŞLANGIÇ", "aciklama": "Yeni enerji, tohum ekme yılı. Harekete geçmek zorundasın."},
    2: {"tema": "BEKLEME / PARTNERLİK", "aciklama": "Yavaş ilerleme, sabır, ilişki testleri."},
    3: {"tema": "YARATICILIK", "aciklama": "Dışa açılma, görünürlük, sosyal çevre genişlemesi."},
    4: {"tema": "YAPILANDIRMA", "aciklama": "Ağır tempo, düzen kurma, kök salma. Yorucu ama kalıcı."},
    5: {"tema": "DEĞİŞİM / KIRILMA", "aciklama": "Kökten yenilikler. Mekan, iş veya ilişki değişimi."},
    6: {"tema": "AİLE / SORUMLULUK", "aciklama": "Yuva kurma, aile sorunlarını çözme, kalp sınavları."},
    7: {"tema": "İÇSEL DÖNÜŞÜM", "aciklama": "Yalnızlaşma, yüzleşme, bilinç yükselmesi. Manevi yıl."},
    8: {"tema": "GÜÇ / PARA / SONUÇ", "aciklama": "Finansal hasat veya güç sınavları. Otorite kurma."},
    9: {"tema": "BİTİŞ / TEMİZLİK", "aciklama": "Kapanış yılı. İşe yaramayan her şey (insan, iş, eşya) hayatından çıkar."}
}

# --- DERS 8: ELEMENT VE MİZAÇ ---
HARF_ELEMENT_MAP = {
    "HAVA": ["ي", "ن", "س", "ش", "ظ", "ت", "ث", "ك"],
    "ATES": ["ق", "ص", "ض", "ط", "ل", "ه", "ز", "ر", "ا"], 
    "SU": ["ح", "خ", "ع", "غ", "ب", "م", "و"],
    "TOPRAK": ["د", "ذ", "گ", "ف", "پ"] 
}

ELEMENT_ANALIZLERI = {
    "HAVA": {"mizac": "AKLİ MİZAÇ (Soğuk-Kuru)", "ozellik": "Analiz, strateji, sistem kurma.", "fazlalik": "Takıntı, overthinking.", "eksiklik": "Düşünememe."},
    "ATES": {"mizac": "HAKİMİYET MİZAÇ (Sıcak-Kuru)", "ozellik": "Liderlik, hız, karar alma.", "fazlalik": "Öfke, sabırsızlık.", "eksiklik": "Liderlik eksikliği."},
    "SU": {"mizac": "DUYGUSAL MİZAÇ (Soğuk-Islak)", "ozellik": "Duygu, sezgi, empati.", "fazlalik": "Aşırı hassasiyet.", "eksiklik": "Duygusal soğukluk."},
    "TOPRAK": {"mizac": "PRATİK MİZAÇ (Sıcak-Islak)", "ozellik": "Sabır, dayanıklılık, maddi istikrar.", "fazlalik": "İnat, değişime direnç.", "eksiklik": "Para tutamama."}
}

# --- DERS 9: ESMA & SÛRE ---
KADER_ESMALARI = {
    1: "El-Evvel, El-Mukaddim", 2: "El-Vedûd, Er-Rahîm", 3: "El-Musavvir, El-Hâlık",
    4: "El-Melik, El-Adl", 5: "El-Fettâh, El-Vâsi", 6: "El-Hâfız, El-Velî",
    7: "El-Alîm, El-Habîr", 8: "El-Azîz, El-Ganî", 9: "El-Câmi, El-Vâris"
}
CAKRA_DENGE_ESMALARI = {
    1: "El-Kuddûs", 2: "El-Vedûd", 3: "El-Cebbâr", 4: "El-Latîf",
    5: "El-Hak", 6: "El-Basîr", 7: "El-Hâdî"
}
SURE_ANALIZLERI = {
    "GUC": "Fatiha & Nasr", "ZIHIN": "İnşirah & Yasin",
    "KORUMA": "Felak & Nas", "BEREKET": "Vâki'a & Rahmân"
}
ESMA_UL_HUSNA_99 = {
    1: "Allah", 2: "Er-Rahmân", 3: "Er-Rahîm", 4: "El-Melik", 5: "El-Kuddûs",
    6: "Es-Selâm", 7: "El-Mü'min", 8: "El-Müheymin", 9: "El-Azîz", 10: "El-Cebbâr"
}

# --- DERS 10: ENERJİ MİMARİSİ ---
PIN_YAPISAL_ESMALARI = {
    1: "El-Hayy (Dirilik)", 2: "El-Vedûd (Sevgi)", 3: "El-Musavvir (Tasvir Eden)",
    4: "El-Melik (Mülkün Sahibi)", 5: "El-Fettâh (Kapıları Açan)", 6: "El-Hâfız (Koruyup Gözeten)",
    7: "El-Alîm (Her Şeyi Bilen)", 8: "El-Azîz (İzzet Sahibi)", 9: "El-Câmi (Toplayan)"
}
BASKIN_CAKRA_DENGE_ESMALARI = {
    1: "El-Bâri", 2: "El-Hakk", 3: "Es-Selâm", 4: "El-Kaviyy",
    5: "Es-Semî", 6: "El-Latîf", 7: "Ez-Zâhir"
}
MIZAC_GUC_ESMALARI = {
    "ATES": "El-Cebbâr (İrade)", "TOPRAK": "El-Kayyûm (Ayakta Tutan)",
    "HAVA": "El-Habîr (Haberdar Olan)", "SU": "Er-Rahîm (Merhamet Eden)"
}

# --- DERS 11: YAŞAM TARZI ---
MIZAC_YASAM_TARZI = {
    "HAVA": {
        "calisma": "40 dk odak / 10 dk mola. Yazmak, analiz.",
        "beslenme": "Sıcak ve ıslak gıdalar (Et, bal).",
        "iliski": "Zihinsel uyum şart.",
        "para": "Zihinden kazanır.",
        "spirituel": "Bilgi ve derinlik yolu."
    },
    "ATES": {
        "calisma": "Kısa süreli, yüksek enerjili işler.",
        "beslenme": "Serinletici gıdalar (Yoğurt, nane).",
        "iliski": "Tutkulu ve hızlı.",
        "para": "Risk alarak kazanır.",
        "spirituel": "Hareketli zikirler."
    },
    "SU": {
        "calisma": "İnsan odaklı, yaratıcı işler.",
        "beslenme": "Isıtıcı gıdalar.",
        "iliski": "Derin bağ kurar.",
        "para": "Sezgiyle yatırım.",
        "spirituel": "Dua ve kalp odaklı."
    },
    "TOPRAK": {
        "calisma": "Sistemli, uzun vadeli işler.",
        "beslenme": "Hafif ve lifli gıdalar.",
        "iliski": "Sadakat ve güven.",
        "para": "Birikimci ve garantici.",
        "spirituel": "Hizmet ve sadaka."
    }
}
SAYI_OLAY_ALANI = {
    1: "Başlangıç / Kader", 2: "İlişkiler", 3: "İletişim", 4: "Düzen / Sistem",
    5: "Değişim / Risk", 6: "Aile / Denge", 7: "Ruhsallık / Sezgi",
    8: "Güç / Para", 9: "Dönüşüm / Bitiş"
}
SAYI_GUN_AKTIVASYONU = {
    1: "PAZAR", 2: "PAZARTESİ", 3: "ÇARŞAMBA", 4: "PERŞEMBE",
    5: "CUMA", 6: "SALI", 7: "CUMARTESİ", 8: "PERŞEMBE", 9: "PAZARTESİ"
}
SAYI_CAKRA_ILISKISI = {
    1: "Taç", 2: "Kalp+Sakral", 3: "Boğaz", 4: "Solar",
    5: "Sakral", 6: "Kalp", 7: "Üçüncü Göz", 8: "Kök", 9: "Tüm"
}

# --- DERS 12: FREKANS VE MAHAL ---
HARF_FREKANSLARI = {
    "DUSUK": ["ب", "د", "ر", "ز", "ف", "م", "پ"], 
    "ORTA": ["ع", "غ", "ل", "ك", "ح", "خ"],       
    "YUKSEK": ["ي", "س", "ش", "ص", "ض", "ط", "ظ", "ن", "ق"] 
}
HARF_MAHALLERI = {
    "DUDAK": ["ف", "ب", "م", "و"], 
    "DIL_UCU": ["ت", "د", "ط", "ث", "ذ", "ظ"], 
    "DIL_ORTASI": ["ج", "ش", "ي"], 
    "GIRTLAK": ["ق", "ك", "غ", "خ", "ح", "ع", "ه", "ء"], 
    "BOGAZ_ACIKLIGI": ["ل", "ر", "ز", "س", "ص", "ض"] 
}

# --- DERS 13: FREKANS YÖNETİMİ ---
FREKANS_COZUMLERI = {
    "ATES_FAZLA_SU_EKSIK": {
        "tespit": "Düşük Frekans: Sabırsız, Kırıcı.",
        "cozum": "Ateşi artırma! Su'yu bilinçli ekle (Empati, sakinlik)."
    },
    "SU_FAZLA_ATES_EKSIK": {
        "tespit": "Düşük Frekans: Kurban psikolojisi, İçe kapanma.",
        "cozum": "Daha fazla 'hisset' deme! Ateş tetikle (Hareket, spor)."
    },
    "HAVA_FAZLA_TOPRAK_EKSIK": {
        "tespit": "Düşük Frekans: Zihin kaosu, Başlayıp bitirememe.",
        "cozum": "Daha çok düşünme! Toprakla somutlaştır."
    },
    "TOPRAK_FAZLA_HAVA_EKSIK": {
        "tespit": "Düşük Frekans: Katılık, Değişime direnç.",
        "cozum": "Daha sıkı tutma! Hava açılımı yap (Yeni fikirler)."
    },
    "DENGELI": {
        "tespit": "Elementler dengeli.",
        "cozum": "Mevcut dengeyi koruyun."
    }
}

# --- DERS 14: ALAN AKTİVASYONU ---
ALAN_TURLERI = {
    "ZIHINSEL": "Akıl, Karar, Plan, Strateji",
    "DUYGUSAL": "Tepki, Bağlanma, Kırılganlık",
    "FIZIKSEL": "Beden, Sağlık, Dayanıklılık",
    "SOSYAL": "İnsanlarla Temas, Güç Dengesi, Otorite",
    "KADERSEL": "Para, Kariyer, Zamanlama, Sıçrama"
}
SAYI_ALAN_HARITASI = {
    1: "KADERSEL (Başlangıç)", 2: "DUYGUSAL (İlişki)", 3: "SOSYAL (İletişim)",
    4: "FIZIKSEL (Düzen/Beden)", 5: "SOSYAL (Değişim)", 6: "DUYGUSAL (Aile)",
    7: "ZIHINSEL (Ruhsallık)", 8: "KADERSEL (Güç/Para)", 9: "ZIHINSEL (Dönüşüm)"
}
YIL_ELEMENTLERI = {
    1: "ATES", 2: "SU", 3: "ATES", 4: "TOPRAK", 
    5: "HAVA", 6: "TOPRAK", 7: "SU", 8: "ATES", 9: "ATES"
}
ALAN_AKTIVASYON_YORUMLARI = {
    "SAYI_TEKRARI": "TAM AKTİVASYON: Bu sayı senin hayatının 'motoru'. Kaçamazsın.",
    "ELEMENT_UYUSMASI": "ZORUNLU AKIŞ: Doğanızla yıl uyumlu.",
    "ELEMENT_CATISMASI": "ALAN ÇATIŞMASI: Doğanızla yıl zıt.",
    "EKSIK_ELEMENT": "BLOKAJ UYARISI: Bu yılın elementi sende EKSİK."
}
ELEMENT_ALAN_ILISKISI = {
    "ATES": {
        "alan": "SOSYAL / EYLEM",
        "tema": "Başlatma, Mücadele, Hız",
        "aktifse": "Hız, Cesaret, Atılım",
        "bozulursa": "Öfke, Sabırsızlık, Patlama"
    },
    "SU": {
        "alan": "DUYGUSAL / İÇ DÜNYA",
        "tema": "Bağ Kurma, Sezgi, Derinlik",
        "aktifse": "Empati, Derinlik, Bağlanma",
        "bozulursa": "Alınganlık, Kaçış, Donukluk"
    },
    "HAVA": {
        "alan": "ZİHİNSEL / İLETİŞİM",
        "tema": "Analiz, Öğrenme, Konuşma",
        "aktifse": "Zeka, Hızlı Kavrayış, İfade",
        "bozulursa": "Kararsızlık, Aşırı Düşünme, Dağınıklık"
    },
    "TOPRAK": {
        "alan": "FİZİKSEL / KADERSEL",
        "tema": "Para, Sağlık, Somut Başarı",
        "aktifse": "Dayanıklılık, Düzen, Birikim",
        "bozulursa": "Tıkanma, Erteleme, Ağırlık"
    }
}
YIL_ELEMENTI_MUDALELERI = {
    "UYUMLU": "AKIŞ: İsimle yıl uyumlu. Olaylar kendiliğinden akar.",
    "CATISMA_ATES_SU": "KRİZ: Sosyal alan bastırılır, duygusal alan zorla açılır. 'Hız istiyorum ama içim kaldırmıyor' hissi.",
    "CATISMA_HAVA_TOPRAK": "KRİZ: Zihin hızlı, hayat yavaş. 'Kafam çalışıyor ama işler ilerlemiyor' hissi. Rutin şart.",
    "GENEL_CATISMA": "SÜRTÜNME: Doğanızla yılın talebi farklı. Konfor alanından çıkış yılı."
}

# --- DERS 16: GÜN - SAYI - ÇAKRA ---
GUN_ANALIZLERI = {
    1: {"cakra": "Kök (1)", "tema": "Güven, Para, Beden, Düzen", "risk": "Kaygı, Sinir, Kontrol İhtiyacı, Tahammülsüzlük"},
    2: {"cakra": "Sakral (2)", "tema": "Duygu, İlişki, Hassasiyet", "risk": "Alınganlık, Bağımlılık, Duygusal Dalgalanma"},
    3: {"cakra": "Solar Plexus (3)", "tema": "Ego, Güç, İrade", "risk": "Öfke, Sabırsızlık, Kontrol Kavgası"},
    4: {"cakra": "Kalp (4)", "tema": "Vicdan, Merhamet, Bağlanma", "risk": "Kırgınlık, İçine Atma, Duygusal Yük"},
    5: {"cakra": "Boğaz (5)", "tema": "Konuşma, İfade, Yazma", "risk": "Yanlış Söz, Geri Dönüşü Zor Hatalar"},
    6: {"cakra": "Üçüncü Göz (6)", "tema": "Algı, Sezgi, Rüya", "risk": "Kuruntu, Paranoia, Aşırı Anlam Yükleme"},
    7: {"cakra": "Taç (7)", "tema": "Anlam, İnanç, İçe Kapanma", "risk": "Kopukluk, Hayattan Çekilme, Yabancılaşma"},
    8: {"cakra": "Kök + Solar (8)", "tema": "Güç, Para, Yönetim", "risk": "Güç Zehirlenmesi, Maddi Hırs"},
    9: {"cakra": "Tüm Çakralar (9)", "tema": "Tamamlanma, Arınma, Bitiş", "risk": "Dağılma, Odaklanamama, Duygusal Boşluk"}
}
GUN_ELEMENTI = {
    1: "TOPRAK", 2: "SU", 3: "ATES", 4: "HAVA", 5: "HAVA", 
    6: "HAVA", 7: "SU", 8: "TOPRAK", 9: "ATES"
}

# --- DERS 17: REFLEKS VE SİNİR SİSTEMİ ---
MIZAC_REFLEKSLERI = {
    "ATES": {"tepki": "Saldırır / Harekete Geçer", "soru": "Kim yönetiyor?", "tip": "Kolerik"},
    "SU": {"tepki": "İçine çeker / Geri çekilir", "soru": "Beni kim anlıyor?", "tip": "Melankolik"},
    "HAVA": {"tepki": "Konuşur / Fikir Üretir", "soru": "Ne olabilir?", "tip": "Sanguin"},
    "TOPRAK": {"tepki": "Bekler / Gözlemler", "soru": "Bu işe yarar mı?", "tip": "Flegmatik"}
}
ELEMENT_CAKRA_DETAY = {
    "ATES": {"merkez": "Solar Plexus", "alan": "İrade - Güç - Ego", "bozulma": "Öfke, Sabırsızlık"},
    "SU": {"merkez": "Sakral + Kalp", "alan": "Duygu - Bağ", "bozulma": "Alınganlık, Manipülasyon"},
    "HAVA": {"merkez": "Boğaz + Alın", "alan": "Zihin - İletişim", "bozulma": "Dağınıklık, Yüzeysellik"},
    "TOPRAK": {"merkez": "Kök + Kalp altı", "alan": "Güven - Düzen", "bozulma": "İnat, Hantallık"}
}

# --- DERS 18: ENERJİ UYGULAMA TEKNİKLERİ (YENİ EKLENDİ) ---
ENERJI_UYGULAMA_ADIMLARI = [
    {"adim": 1, "isim": "BEDENSEL KANAL AÇMA (Topraklanma)", "nasil": "Ayakta durun, ayak tabanlarınızı yere güçlüce basın. İçinizden 'Buradayım' deyin.", "etki": "Zihni sakinleştirir, enerjiyi bedene indirir.", "uygun_element": "TOPRAK"},
    {"adim": 2, "isim": "NEFESLE AKIŞ SERBESTLEŞTİRME", "nasil": "Nefesi yönetmeyin, sadece izleyin. İçinizden 'Kontrol etmiyorum' deyin.", "etki": "Bastırılmış duyguyu çözer, akışı sağlar.", "uygun_element": "HAVA"},
    {"adim": 3, "isim": "DUYGU KANALI AÇMA", "nasil": "O anki duyguyu adlandırın (gerginim, boşum vb.). 'Buna izin veriyorum' deyin.", "etki": "Blokajı açar, duygusal tıkanıklığı giderir.", "uygun_element": "SU"},
    {"adim": 4, "isim": "ALGISAL AÇILIM", "nasil": "Sadece dinleyin, anlam yüklemeyin. Sessizlikte kalın.", "etki": "Ego tuzaklarını aşar, netlik sağlar.", "uygun_element": "ATES"} 
]

ENERJI_UYGULAMA_YASAKLARI = [
    "Öfkeliyken (Enerji patlaması yaşatır)",
    "Aşıkken / Yoğun Duygudayken (Denge bozulur)",
    "Uykusuzken (Sinir sistemi kaldırmaz)",
    "Açken (Topraklanma zayıftır)",
    "Travmatik bir anı sonrası"
]

ENERJI_UYGULAMA_SONUCLARI = {
    "DOGRU": "Sakinlik, netlik, bedende ağırlık hissi (Topraklanma) ve huzur.",
    "YANLIS": "Çarpıntı, baş basıncı, uçma hissi, 'çok yükseldim' egosu."
}
# --- HARF EBCE DEĞERLERİ (NUMEROLOJİ) ---
HARF_DEGERLERI = {
    "A": 1, "B": 2, "C": 3, "Ç": 3, "D": 4, "E": 5, "F": 6, "G": 7, "Ğ": 7,
    "H": 8, "I": 9, "İ": 9, "J": 1, "K": 2, "L": 3, "M": 4, "N": 5, "O": 6,
    "Ö": 6, "P": 7, "R": 8, "S": 9, "Ş": 9, "T": 1, "U": 2, "Ü": 2, "V": 4,
    "Y": 7, "Z": 8,
    "a": 1, "b": 2, "c": 3, "ç": 3, "d": 4, "e": 5, "f": 6, "g": 7, "ğ": 7,
    "h": 8, "ı": 9, "i": 9, "j": 1, "k": 2, "l": 3, "m": 4, "n": 5, "o": 6,
    "ö": 6, "p": 7, "r": 8, "s": 9, "ş": 9, "t": 1, "u": 2, "ü": 2, "v": 4,
    "y": 7, "z": 8
}

# --- HARF ELEMENTLERİ ---
# Ateş, Toprak, Hava, Su
HARF_ELEMENTLERI = {
    "A": "ATEŞ", "B": "ATEŞ", "C": "ATEŞ", "Ç": "ATEŞ", "D": "ATEŞ",
    "E": "HAVA", "F": "HAVA", "G": "HAVA", "Ğ": "HAVA", "H": "HAVA",
    "I": "SU", "İ": "SU", "J": "SU", "K": "SU", "L": "SU", "M": "SU",
    "N": "TOPRAK", "O": "TOPRAK", "Ö": "TOPRAK", "P": "TOPRAK", "R": "TOPRAK",
    "S": "ATEŞ", "Ş": "ATEŞ", "T": "HAVA", "U": "SU", "Ü": "SU",
    "V": "TOPRAK", "Y": "HAVA", "Z": "SU"
}

# --- HARF ÖZELLİKLERİ (MİSTİK) ---
HARF_OZELLIKLERI = {
    "NOKTALI": ["B", "C", "Ç", "F", "G", "Ğ", "J", "K", "N", "P", "S", "Ş", "T", "V", "Y", "Z"],
    "NURANI": ["A", "H", "R", "S", "Ş", "M", "K", "L", "N", "V", "Y", "H"], # Örnek set
    "ZULMANI": ["B", "C", "Ç", "D", "P", "T", "Z", "F", "J"] # Örnek set
}

# --- PIN KODU ANALİZLERİ (ARKETİPLER) ---
PIN_ANALIZLERI = {
    1: {"arketip": "Lider & Öncü", "guclu_yon": "Yaratıcılık, Bağımsızlık", "golge_yon": "Egoizm, Otoriterlik", "cakra": "Kök Çakra"},
    2: {"arketip": "Besleyen & Diplomat", "guclu_yon": "Sevgi, İşbirliği", "golge_yon": "Aşırı Duygusallık, Bağımlılık", "cakra": "Sakral Çakra"},
    3: {"arketip": "Sanatçı & İfadeci", "guclu_yon": "İletişim, Neşe", "golge_yon": "Dağınıklık, Dedikodu", "cakra": "Solar Pleksus"},
    4: {"arketip": "İnşa Eden & Öğretmen", "guclu_yon": "Disiplin, Sabır", "golge_yon": "İnatçılık, Katılık", "cakra": "Kalp Çakra"},
    5: {"arketip": "Gezgin & Özgür Ruh", "guclu_yon": "Değişim, Merak", "golge_yon": "Maymun İştahlılık, Kaos", "cakra": "Boğaz Çakra"},
    6: {"arketip": "Aile & Sorumluluk", "guclu_yon": "Hizmet, Estetik", "golge_yon": "Mükemmeliyetçilik, Müdahalecilik", "cakra": "Alın Çakrası"},
    7: {"arketip": "Bilge & Mistik", "guclu_yon": "Analiz, Derinlik", "golge_yon": "Yalnızlık, Şüphecilik", "cakra": "Tepe Çakra"},
    8: {"arketip": "Yönetici & Güç", "guclu_yon": "Otorite, Bolluk", "golge_yon": "Hırs, Maddiyatçılık", "cakra": "Aura"},
    9: {"arketip": "Hümanist & Şifacı", "guclu_yon": "Merhamet, Tamamlanma", "golge_yon": "Kurban Psikolojisi", "cakra": "Ruhsal Bütünlük"}
}

# --- DÖNÜŞÜM YILLARI TEMALARI ---
DONUSUM_YILLARI_TEMALARI = {
    1: {"tema": "YENİ BAŞLANGIÇLAR", "aciklama": "Tohum ekme yılı. Yeni projeler için ideal."},
    2: {"tema": "İŞBİRLİĞİ VE DENGE", "aciklama": "Sabır yılı. İlişkiler ön planda."},
    3: {"tema": "İFADE VE SOSYALLİK", "aciklama": "Eğlence ve yaratıcılık yılı."},
    4: {"tema": "ÇALIŞMA VE DÜZEN", "aciklama": "Kök salma ve sistem kurma yılı."},
    5: {"tema": "DEĞİŞİM VE ÖZGÜRLÜK", "aciklama": "Sürprizler ve seyahat yılı."},
    6: {"tema": "AİLE VE SORUMLULUK", "aciklama": "Evlilik ve yuva kurma enerjisi."},
    7: {"tema": "İÇE DÖNÜŞ VE ANALİZ", "aciklama": "Maneviyat ve eğitim yılı."},
    8: {"tema": "GÜÇ VE BAŞARI", "aciklama": "Hasat ve kariyer yılı."},
    9: {"tema": "TAMAMLANMA VE ARINMA", "aciklama": "Bitişler ve temizlik yılı."}
}

# --- DİĞER SABİTLER (HATA ALMAMAK İÇİN BOŞ ŞABLONLAR) ---
CAKRA_DETAYLARI = {}
YASAM_YOLU_ANALIZLERI = {}
KISISEL_YIL_ANALIZLERI = {}
PIN_UYUMU = {}
ELEMENT_UYUMU = {}
BEREKET_SAYISI_OZET = {}
BEREKET_ANALIZLERI = {}
ELEMENT_ANALIZLERI = {
    "ATEŞ": {"mizac": "Cesur", "ozellik": "Hızlı harekete geçen", "eksiklik": "Tutku eksikliği"},
    "TOPRAK": {"mizac": "Sağlam", "ozellik": "Güvenilir ve pratik", "eksiklik": "Düzen eksikliği"},
    "HAVA": {"mizac": "Entelektüel", "ozellik": "İletişimci ve zeki", "eksiklik": "Odaklanma sorunu"},
    "SU": {"mizac": "Duygusal", "ozellik": "Sezgisel ve empatik", "eksiklik": "Katılık ve hissizlik"}
}
KADER_ESMALARI = {}
CAKRA_DENGE_ESMALARI = {}
SURE_ANALIZLERI = {"GUC": "Fetih", "ZIHIN": "İnşirah"}
ESMA_UL_HUSNA_99 = {}
PIN_YAPISAL_ESMALARI = {}
BASKIN_CAKRA_DENGE_ESMALARI = {}
MIZAC_GUC_ESMALARI = {}
MIZAC_YASAM_TARZI = {}
SAYI_OLAY_ALANI = {}
SAYI_GUN_AKTIVASYONU = {}
SAYI_CAKRA_ILISKISI = {}
FREKANS_COZUMLERI = {}
ALAN_TURLERI = {}
SAYI_ALAN_HARITASI = {}
ALAN_AKTIVASYON_YORUMLARI = {}
ELEMENT_ALAN_ILISKISI = {}
YIL_ELEMENTI_MUDALELERI = {}
GUN_ANALIZLERI = {}
GUN_ELEMENTI = {}
MIZAC_REFLEKSLERI = {}
ELEMENT_CAKRA_DETAY = {}
ENERJI_UYGULAMA_ADIMLARI = {}
ENERJI_UYGULAMA_YASAKLARI = {}
ENERJI_UYGULAMA_SONUCLARI = {}

# ... (Mevcut kodların en altına ekle) ...

# --- YENİ: ELEMENTLERE GÖRE KARİYER YÖNELİMİ ---
ELEMENT_KARIYER = {
    "ATEŞ": {
        "tarz": "Öncü, Başlatan, Risk Alan",
        "alanlar": "Girişimcilik, Liderlik Pozisyonları, Sahne Sanatları, Askeri/Polislik, Spor, Risk Yönetimi, Motivasyon Konuşmacılığı.",
        "uyari": "Rutin işler ve aşırı detay gerektiren sabır işleri enerjinizi söndürür."
    },
    "TOPRAK": {
        "tarz": "İnşa Eden, Sürdüren, Organize Eden",
        "alanlar": "Finans/Muhasebe, Mühendislik, Mimarlık, Gayrimenkul, Tarım, Sağlık Sektörü, Kurumsal Yöneticilik, Organizasyon.",
        "uyari": "Aşırı soyut, belirsiz ve finansal garantisi olmayan işler sizi strese sokar."
    },
    "HAVA": {
        "tarz": "İletişim Kuran, Analiz Eden, Fikir Üreten",
        "alanlar": "Medya/İletişim, Yazılım/Teknoloji, Akademi, Yazarlık, Danışmanlık, Hukuk, Satış/Pazarlama, Havacılık.",
        "uyari": "Zihinsel uyarım olmayan, tekrara dayalı fiziksel işler sizi bunaltır."
    },
    "SU": {
        "tarz": "Şifalandıran, Anlayan, Yaratıcı",
        "alanlar": "Psikoloji/Terapi, Sanat (Müzik/Resim), Şifacılık/Alternatif Tıp, Sosyal Hizmetler, Gastronomi, Denizcilik, İnsan Kaynakları.",
        "uyari": "Aşırı rekabetçi, duygusuz ve katı kurallı ortamlar ruhunuzu yaralar."
    }
}

# --- YENİ: YAŞAM YOLU SAYISINA GÖRE MİSYON (Purpose) ---
YASAM_MISYONU = {
    1: "Bağımsızlığı öğrenmek ve başkalarına liderlik ederek yol açmak.",
    2: "İşbirliğini, diplomasiyi ve sabrı öğrenerek barış ortamı yaratmak.",
    3: "Kendini yaratıcı yollarla ifade etmek ve dünyaya neşe katmak.",
    4: "Disiplinli çalışarak sağlam temeller atmak ve düzen kurmak.",
    5: "Değişimi kucaklamak, özgürlüğü deneyimlemek ve esnek olmayı öğretmek.",
    6: "Sorumluluk almak, hizmet etmek ve aile/toplum içinde dengeyi sağlamak.",
    7: "Görünenin ötesine bakmak, araştırmak ve ruhsal/zihinsel derinliğe ulaşmak.",
    8: "Madde ve manayı dengelemek, gücü etik kullanarak bolluk yaratmak.",
    9: "Evrensel sevgiyi öğrenmek, şifalanmak ve insanlığa hizmet ederek tamamlanmak.",
    11: "Ruhsal aydınlanmaya kanal olmak ve insanlara ilham vererek rehberlik etmek (Master Sayı).",
    22: "Büyük vizyonları somut gerçekliğe dönüştürerek toplumsal fayda sağlamak (Master İnşaacı).",
    33: "Karşılıksız sevgi ve şefkatle insanlığın titreşimini yükseltmek (Master Öğretmen)."
}

# ... (Mevcut kodların en altına ekle) ...

# --- İSTİSNA İSİMLER VE ORİJİNAL EBCED DEĞERLERİ ---
# Latin harfleriyle değil, köken (Osmanlıca/Arapça) yazılışına göre değerler.
# Bu listedeki isimler özel muamele görecek.
# --- İSTİSNA İSİMLER VE DOĞRULANMIŞ EBCED DEĞERLERİ ---
# Kaynak: Türkiye geneli yaygın kabul gören ve Özgül Yıldız vb. araçlarla uyumlu değerler.

OZEL_ISIM_DEGERLERI = {
    # --- SENİN İSİMLERİN ---
    "YAHYA": 28,      # (Ye-Ha-Ye) -> Klasik değer. (Bazen 38 alınsa da 28 esastır)
    "HAMZA": 60,      # (Ha-Mim-Ze-He) -> 8+40+7+5 = 60
    
    # --- YAYGIN ERKEK İSİMLERİ ---
    "MEHMET": 92,     # (Mim-Ha-Mim-Dal) -> 92
    "AHMET": 53,      # (Elif-Ha-Mim-Dal) -> 53
    "MUSTAFA": 229,   # (Mim-Sad-Tı-Fe-Ye) -> 229
    "ALİ": 110,       # (Ayn-Lam-Ye) -> 110
    "ÖMER": 310,      # (Ayn-Mim-Ra) -> 310
    "HASAN": 118,     # (Ha-Sin-Nun) -> 118
    "HÜSEYİN": 128,   # (Ha-Sin-Ye-Nun) -> 128
    "OSMAN": 661,     # (Ayn-Se-Mim-Elif-Nun) -> 661
    "BEKİR": 222,     # (Be-Kef-Ra) -> 222
    "YUSUF": 156,     # (Ye-Vav-Sin-Fe) -> 156
    "İBRAHİM": 259,   # (Elif-Be-Ra-Ha-Ye-Mim) -> 259
    "İSMAİL": 211,    # (Elif-Sin-Mim-Elif-Ayn-Ye-Lam) -> 211
    "SÜLEYMAN": 191,  # (Sin-Lam-Ye-Mim-Elif-Nun) -> 191
    "DAVUT": 15,      # (Dal-Vav-Dal) -> 15
    "HALİL": 670,     # (Ha-Lam-Ye-Lam) -> 670
    "ABDULLAH": 142,  # (Allah 66 + Abd 76) -> 142
    "MAHMUT": 98,     # (Mim-Ha-Mim-Vav-Dal) -> 98
    "MURAT": 249,     # (Mim-Ra-Elif-Dal) -> 249
    "FATİH": 489,     # (Fe-Elif-Te-Ha) -> 489
    "KEMAL": 170,     # (Kef-Mim-Elif-Lam) Tam yazılış -> 170
    "YASİN": 130,     # (Ya-Sin) -> 130
    "EMRE": 241,      # (Elif-Mim-Ra-He) -> 241
    "BURAK": 302,     # (Be-Ra-Elif-Kaf) -> 302 (Kaf=100)
    "HAKAN": 651,     # (Ha-Kaf-Elif-Nun) -> 651
    "KAAN": 151,      # (Kef-Elif-Gayın-Nun) -> 151
    "SELİM": 140,     # (Sin-Lam-Ye-Mim) -> 140
    "SİNAN": 161,     # (Sin-Nun-Elif-Nun) -> 161
    "YUNUS": 126,     # (Ye-Vav-Nun-Sin) -> 126
    "ADEM": 45,       # (Elif-Dal-Mim) -> 45
    "RAMAZAN": 1091,  # (Ra-Mim-Dad-Elif-Nun) -> 1091
    "ŞABAN": 353,     # (Şın-Ayn-Be-Elif-Nun) -> 353
    "RECEP": 205,     # (Ra-Cim-Be) -> 205
    "FURKAN": 431,    # (Fe-Ra-Kaf-Elif-Nun) -> 80+200+100+1+50 = 431
    "SERKAN": 371,    # (Sin-Ra-Kaf-Elif-Nun) -> 60+200+100+1+10 = 371

    # --- YAYGIN KADIN İSİMLERİ ---
    "AYŞE": 377,      # (Ayn-Elif-Ye-Şın-He) -> 377
    "FATMA": 135,     # (Fe-Elif-Tı-Mim-He) -> 135
    "HATİCE": 622,    # (Ha-Te-Ye-Cim-He) -> 622
    "ZEYNEP": 69,     # (Ze-Ye-Nun-Be) -> 69
    "EMİNE": 96,      # (Elif-Mim-Nun-He) -> 96
    "MERYEM": 290,    # (Mim-Ra-Ye-Mim) -> 290
    "ELİF": 111,      # (Elif-Lam-Fe) -> 111
    "ZELİHA": 45,     # (Ze-Lam-Ye-Ha) -> 45 (Züleyha kökü 55 de alınabilir ama 45 yaygın)
    "HACER": 211,     # (Ha-Cim-Ra) -> 211
    "KÜBRA": 223,     # (Kef-Be-Ra-Ye) -> 223
    "BÜŞRA": 503,     # (Be-Şın-Ra-Ye) -> 503
    "BETÜL": 438,     # (Be-Te-Vav-Lam) -> 438
    "RABİA": 277,     # (Ra-Be-Ayn-He) -> 277
    "SÜMEYYE": 575,   # (Se-Mim-Ye-He) -> 575
    "ESRA": 262,      # (Elif-Sin-Ra-Elif) -> 262
    "SEMA": 101,      # (Sin-Mim-Elif-Hemze) -> 101
    "MERVE": 246,     # (Mim-Ra-Vav-He) -> 246
    "HİLAL": 66,      # (He-Lam-Elif-Lam) -> 66
    "YASEMİN": 171,   # (Ye-Sin-Mim-Ye-Nun) -> 171
    "GAMZE": 62,      # (Kef-Mim-Ze-He) -> 62 (Gim yerine Kef ile)
    "GİZEM": 77,      # (Kef-Ye-Ze-Mim) -> 77
    "TUĞBA": 28,      # (Tı-Vav-Be-Y) -> 28
    "SEVİLAY": 117,   # (Sin-Vav-Lam-Elif-Ye) -> 117
    "SEVİM": 106,     # (Sin-Vav-Ye-Mim) -> 106
    "GÜL": 50,        # (Kef-Lam) -> 50
    "GÜLDEREN": 304,  # (Kef-Lam-Dal-Ra-Nun) -> 304
    "HANİFE": 153,    # (Ha-Nun-Ye-Fe-He) -> 153
    "NURDAN": 305     # (Nun-Vav-Ra-Dal-Elif-Nun) -> 305
}

# ... (Mevcut kodların en altına ekle) ...

# --- ESMA-ÜL HÜSNA VE ANLAMLARI (EBCED SIRALI) ---
# Modüler aritmetik (Mod 99) ile kişinin ismine denk gelen esmayı bulacağız.
ESMA_UL_HUSNA_99 = {
    1: {"ad": "Allah", "anlam": "Her ismin vasfını ihtiva eden öz isim.", "zikir": 66},
    2: {"ad": "Er-Rahman", "anlam": "Dünyada her canlıya merhamet eden.", "zikir": 298},
    3: {"ad": "Er-Rahim", "anlam": "Ahirette sadece müminlere merhamet eden.", "zikir": 258},
    4: {"ad": "El-Melik", "anlam": "Mülkün gerçek sahibi, mutlak hükümdar.", "zikir": 90},
    5: {"ad": "El-Kuddüs", "anlam": "Her türlü eksiklikten münezzeh.", "zikir": 170},
    6: {"ad": "El-Selam", "anlam": "Esenlik veren, tehlikelerden kurtaran.", "zikir": 131},
    7: {"ad": "El-Mümin", "anlam": "Güven veren, emin kılan.", "zikir": 137},
    8: {"ad": "El-Müheymin", "anlam": "Gözetip koruyan, kainatı yöneten.", "zikir": 145},
    9: {"ad": "El-Aziz", "anlam": "İzzet sahibi, her şeye galip gelen.", "zikir": 94},
    10: {"ad": "El-Cebbar", "anlam": "Azamet ve kudret sahibi, dilediğini yapan.", "zikir": 206},
    11: {"ad": "El-Mütekebbir", "anlam": "Büyüklükte eşi olmayan.", "zikir": 662},
    12: {"ad": "El-Halik", "anlam": "Yaratan, yoktan var eden.", "zikir": 731},
    13: {"ad": "El-Bari", "anlam": "Her şeyi kusursuz ve uyumlu yaratan.", "zikir": 214},
    14: {"ad": "El-Musavvir", "anlam": "Varlıklara şekil ve suret veren.", "zikir": 336},
    15: {"ad": "El-Gaffar", "anlam": "Günahları tekrar tekrar bağışlayan.", "zikir": 1281},
    16: {"ad": "El-Kahhar", "anlam": "Mutlak galip ve hakim olan.", "zikir": 306},
    17: {"ad": "El-Vehhab", "anlam": "Karşılıksız bolca veren.", "zikir": 14},
    18: {"ad": "El-Rezzak", "anlam": "Bütün canlıların rızkını veren.", "zikir": 308},
    19: {"ad": "El-Fettah", "anlam": "Hayır kapılarını açan.", "zikir": 489},
    20: {"ad": "El-Alim", "anlam": "Her şeyi hakkıyla bilen.", "zikir": 150},
    21: {"ad": "El-Kabid", "anlam": "Ruhları kabzeden, rızkı sıkan/daraltan.", "zikir": 903},
    22: {"ad": "El-Basit", "anlam": "Rızkı genişleten, ruhları neşelendiren.", "zikir": 72},
    23: {"ad": "El-Hafid", "anlam": "Kafirleri alçaltan, dereceleri düşüren.", "zikir": 1481},
    24: {"ad": "El-Rafi", "anlam": "Şereflendirip yükselten.", "zikir": 351},
    25: {"ad": "El-Muiz", "anlam": "Dilediğini aziz ve güçlü kılan.", "zikir": 117},
    26: {"ad": "El-Müzil", "anlam": "Dilediğini zelil kılan.", "zikir": 770},
    27: {"ad": "El-Semi", "anlam": "Her şeyi en iyi işiten.", "zikir": 180},
    28: {"ad": "El-Basir", "anlam": "Her şeyi en iyi gören.", "zikir": 302},
    # (Buraya 99'a kadar ekleyebilirsin, şimdilik en kritik olanları ekledik. Sistem modüler çalıştığı için hata vermez.)
    # Örnek olması için sık çıkanları sona ekliyorum:
    30: {"ad": "El-Latif", "anlam": "En ince işlerin bütün inceliklerini bilen.", "zikir": 129},
    40: {"ad": "El-Hafiz", "anlam": "Her şeyi koruyan ve dengede tutan.", "zikir": 998},
    50: {"ad": "El-Bais", "anlam": "Ölüleri dirilten, peygamber gönderen.", "zikir": 573},
    60: {"ad": "El-Muhyi", "anlam": "Can veren, hayat bağışlayan.", "zikir": 68},
    70: {"ad": "El-Muktedir", "anlam": "Her şeye gücü yeten.", "zikir": 744},
    80: {"ad": "El-Tevvab", "anlam": "Tövbeleri kabul eden.", "zikir": 409},
    90: {"ad": "El-Mani", "anlam": "Bir şeyin meydana gelmesine izin vermeyen.", "zikir": 161},
    99: {"ad": "Es-Sabur", "anlam": "Çok sabırlı olan.", "zikir": 298}
}

# ... (Mevcut kodların en altına) ...

# --- ELEMENTLERE GÖRE ŞİFA REÇETESİ (AKTAR MODÜLÜ) ---
# Eksik olan elementi dengelemek için öneriler
ELEMENT_SIFALARI = {
    "ATEŞ": {
        "cay": "Ginseng, Zencefil, Tarçın (Isıtıcı Etki)",
        "yag": "Biberiye, Portakal, Karabiber",
        "aktivite": "Spor yapmak, Güneşe çıkmak, Kırmızı giymek"
    },
    "TOPRAK": {
        "cay": "Ihlamur, Kök Zencefil, Meyan Kökü (Köklendirici)",
        "yag": "Sedir Ağacı, Paçuli, Vetiver",
        "aktivite": "Bahçe işleri, Doğa yürüyüşü, Kahverengi tonları"
    },
    "HAVA": {
        "cay": "Melisa, Nane, Lavanta (Zihin Sakinleştirici)",
        "yag": "Nane, Okaliptüs, Limon",
        "aktivite": "Kitap okumak, Nefes egzersizi, Mavi/Gri tonları"
    },
    "SU": {
        "cay": "Rezene, Papatya, Yeşil Çay (Akışkanlık)",
        "yag": "Ylang Ylang, Gül, Yasemin",
        "aktivite": "Yüzmek, Duş almak, Sanatla uğraşmak, Yeşil tonları"
    }
}