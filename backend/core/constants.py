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
# --- SABİT VERİLER VE SÖZLÜKLER ---

# 1. EBCED DEĞERLERİ (HESAPLAMA MOTORU İÇİN KRİTİK)
EBCED_DEGERLERI = {
    'a': 1, 'b': 2, 'c': 3, 'ç': 3, 'd': 4, 'e': 5, 'f': 8, 'g': 8, 'ğ': 8, 'h': 8, 
    'ı': 10, 'i': 10, 'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 7, 'ö': 7, 'p': 8, 
    'r': 2, 's': 6, 'ş': 6, 't': 4, 'u': 7, 'ü': 7, 'v': 6, 'y': 1, 'z': 7,
    'q': 4, 'w': 6, 'x': 6
}

# 2. PIN KODU ANALİZLERİ
PIN_ANALIZLERI = {
    1: {"arketip": "Lider & Öncü", "guclu_yon": "Yaratıcılık, Bağımsızlık", "golge_yon": "Egosantrizm", "cakra": "Kök Çakra"},
    2: {"arketip": "Besleyici & Diplomat", "guclu_yon": "Sezgi, İşbirliği", "golge_yon": "Aşırı Duyarlılık", "cakra": "Sakral Çakra"},
    3: {"arketip": "İfadeci & Sanatçı", "guclu_yon": "İletişim, Neşe", "golge_yon": "Dağınıklık", "cakra": "Solar Pleksus"},
    4: {"arketip": "İnşa Edici & Öğretmen", "guclu_yon": "Düzen, Sabır", "golge_yon": "Katılık", "cakra": "Kalp Çakrası"},
    5: {"arketip": "Gezgin & Özgür Ruh", "guclu_yon": "Değişim, Macera", "golge_yon": "Odaklanma Sorunu", "cakra": "Boğaz Çakrası"},
    6: {"arketip": "Şifacı & Ebeveyn", "guclu_yon": "Sorumluluk, Sevgi", "golge_yon": "Müdahalecilik", "cakra": "3. Göz Çakrası"},
    7: {"arketip": "Bilge & Araştırmacı", "guclu_yon": "Analiz, Derinlik", "golge_yon": "Münzevilik", "cakra": "Taç Çakra"},
    8: {"arketip": "Yönetici & Güç Sahibi", "guclu_yon": "Otorite, Bolluk", "golge_yon": "Maddecilik", "cakra": "Aura"},
    9: {"arketip": "Hümanist & Rehber", "guclu_yon": "Merhamet, Bilgelik", "golge_yon": "Kurban Psikolojisi", "cakra": "Evrensel"},
    11: {"arketip": "Aydınlatıcı (Üstat)", "guclu_yon": "İlham, Sezgi", "golge_yon": "Gerginlik", "cakra": "Yüksek Frekans"},
    22: {"arketip": "Büyük Mimar (Üstat)", "guclu_yon": "Büyük Vizyon", "golge_yon": "Yıkıcılık", "cakra": "Kozmik Denge"}
}

# 3. YAŞAM YOLU MİSYONLARI
YASAM_MISYONU = {
    1: "Kendi ayakları üzerinde durmayı ve liderlik etmeyi öğrenmek.",
    2: "Uyum, denge ve işbirliği içinde yaşamayı öğrenmek.",
    3: "Kendini ifade etmeyi ve başkalarına neşe vermeyi öğrenmek.",
    4: "Sistem kurmayı, sabretmeyi ve köklenmeyi öğrenmek.",
    5: "Özgürlüğü deneyimlemeyi ve değişime adapte olmayı öğrenmek.",
    6: "Sorumluluk almayı ve koşulsuz sevmeyi öğrenmek.",
    7: "İçsel bilgeliği keşfetmeyi ve ruhsal derinleşmeyi öğrenmek.",
    8: "Gücü ve parayı etik bir şekilde yönetmeyi öğrenmek.",
    9: "Bırakmayı, affetmeyi ve evrensel sevgiyi öğrenmek.",
    11: "İnsanlara ruhsal rehberlik ve ilham kaynağı olmak.",
    22: "Büyük projelerle topluma kalıcı eserler bırakmak."
}

# 4. ELEMENT KARİYERLERİ
ELEMENT_KARIYER = {
    "ATEŞ": {"tarz": "Girişimci", "alanlar": "Yöneticilik, Spor, Sahne Sanatları", "uyari": "Tükenmişlik Sendromuna Dikkat"},
    "TOPRAK": {"tarz": "İstikrarlı", "alanlar": "Finans, Mühendislik, Tarım", "uyari": "Değişime Direnme"},
    "HAVA": {"tarz": "Zihinsel", "alanlar": "Medya, Teknoloji, Yazarlık", "uyari": "Odaklanma Sorunu"},
    "SU": {"tarz": "Duygusal", "alanlar": "Psikoloji, Sağlık, Sanat", "uyari": "Duygusal Yük Alma"}
}

# 5. DÖNÜŞÜM YILLARI TEMALARI (Kişisel Yıl)
DONUSUM_YILLARI_TEMALARI = {
    1: {"tema": "YENİ BAŞLANGIÇLAR", "aciklama": "Tohum ekme zamanı. Yeni iş, yeni ilişki."},
    2: {"tema": "İŞBİRLİĞİ VE BEKLEME", "aciklama": "Sabır yılı. İlişkiler ön planda."},
    3: {"tema": "İFADE VE SOSYALLEŞME", "aciklama": "Eğlence ve yaratıcılık yılı."},
    4: {"tema": "ÇALIŞMA VE DÜZEN", "aciklama": "Temelleri sağlamlaştırma yılı."},
    5: {"tema": "DEĞİŞİM VE ÖZGÜRLÜK", "aciklama": "Sürpriz gelişmeler, seyahatler."},
    6: {"tema": "AİLE VE SORUMLULUK", "aciklama": "Evlilik, yuva kurma veya tadilat."},
    7: {"tema": "İÇE DÖNÜŞ VE ANALİZ", "aciklama": "Ruhsal gelişim, yalnız kalma isteği."},
    8: {"tema": "GÜÇ VE HASAT", "aciklama": "Maddi kazançlar ve kariyer zirvesi."},
    9: {"tema": "BİTİŞ VE ARINMA", "aciklama": "Eskiyi bırakma, sadeleşme yılı."}
}

# 6. ESMA-ÜL HÜSNA (Örnek - 99'u da eklenebilir ama yer kaplamasın diye özet)
ESMA_UL_HUSNA_99 = {
    1: {"ad": "Ya Rahman", "anlam": "Dünyadaki her varlığa merhamet eden", "zikir": 298},
    99: {"ad": "Ya Sabur", "anlam": "Çok sabırlı olan", "zikir": 298},
    # Burası normalde 99 satır olur, kodda .get() ile hata almamak için default değer kullanıyoruz.
}

# 7. ELEMENT ŞİFALARI (AKTAR MODÜLÜ)
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

# 8. MİZAÇ REFLEKSLERİ VE FREKANS ÇÖZÜMLERİ
MIZAC_REFLEKSLERI = {
    "ATEŞ": {"tepki": "Hızlı ve Öfkeli"},
    "TOPRAK": {"tepki": "Sakin ve İnatçı"},
    "HAVA": {"tepki": "Değişken ve Konuşkan"},
    "SU": {"tepki": "Duygusal ve İçe Dönük"}
}

FREKANS_COZUMLERI = {
    "Dengeli": {"tespit": "Enerjiniz uyumlu."},
    "Aşırı Dengesiz": {"tespit": "Acil topraklanma gerekiyor."},
    "Hafif Dengesiz": {"tespit": "Ufak dokunuşlarla düzelir."}
}

# HATA ÖNLEYİCİ TANIMLAR
BASKIN_ELEMENT_TANIMLARI = MIZAC_REFLEKSLERI # Geriye dönük uyumluluk için