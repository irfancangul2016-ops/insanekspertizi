# from core.constants import EBCED_VALUES, LATIN_TO_ARABIC

# class EbcedCalculator:
#     @staticmethod
#     def calculate_name(name: str) -> dict:
#         """
#         İsmi alır, Arapça harflere çevirir, Ebced değerini ve Element puanlarını hesaplar.
#         """
#         cleaned_name = name.upper().strip()
#         arabic_chars = []
#         total_ebced = 0
        
#         # Harf Harf Dönüşüm ve Toplama
#         for char in cleaned_name:
#             if char in LATIN_TO_ARABIC:
#                 arabic_char = LATIN_TO_ARABIC[char]
#                 value = EBCED_VALUES.get(arabic_char, 0)
                
#                 arabic_chars.append(arabic_char)
#                 total_ebced += value

#         # Element Hesaplama (Mod 4 kuralı: 1:Ateş, 2:Toprak, 3:Hava, 0(4):Su gibi - Kendi kuralına göre düzenle)
#         # Senin koddaki mantığı buraya temizleyerek alıyorum:
#         elements = {"Ateş": 0, "Toprak": 0, "Hava": 0, "Su": 0}
        
#         # Basit örnek mantık (Senin mizac.py'deki mantığı buraya taşı):
#         mod = total_ebced % 4
#         if mod == 1: elements["Ateş"] += 2
#         elif mod == 2: elements["Toprak"] += 2
#         elif mod == 3: elements["Hava"] += 2
#         else: elements["Su"] += 2
        
#         # Baskın Elementi Bul
#         dominant = max(elements, key=elements.get)

#         return {
#             "name": name,
#             "arabic_mapping": "".join(arabic_chars),
#             "ebced_score": total_ebced,
#             "elements": elements,
#             "dominant_element": dominant
#         }

#     @staticmethod
#     def calculate_year_element(year: int) -> str:
#         # Yıl elementi hesaplama mantığın (örnek)
#         # Buraya kendi mantığını koy
#         modes = ["Su", "Ateş", "Toprak", "Hava"] 
#         return modes[year % 4]






# # backend/services/calculator.py
# from core.constants import EBCED_VALUES, LATIN_TO_ARABIC

# class EbcedCalculator:
    
#     @staticmethod
#     def calculate_ebced(text: str) -> int:
#         """Metnin Ebced değerini hesaplar."""
#         toplam = 0
#         temiz_metin = text.upper().strip().replace(" ", "")
        
#         for harf in temiz_metin:
#             if harf in LATIN_TO_ARABIC:
#                 arapca_harf = LATIN_TO_ARABIC[harf]
#                 toplam += EBCED_VALUES.get(arapca_harf, 0)
#         return toplam

#     @staticmethod
#     def find_dominant_element(ebced_score: int) -> str:
#         """
#         Ebced değerine göre element belirler.
#         Eski kodundaki mantık: Mod 4.
#         0 -> Su, 1 -> Ateş, 2 -> Toprak, 3 -> Hava (Senin sıralamana göre uyarlandı)
#         """
#         mod = ebced_score % 4
#         # Eski kodundaki analiz.py referansı: ["Ateş","Toprak","Hava","Su"]
#         if mod == 1: return "Ateş"
#         if mod == 2: return "Toprak"
#         if mod == 3: return "Hava"
#         return "Su" # mod 0 ise

#     @staticmethod
#     def calculate_year_element(year: int) -> str:
#         """Yılın elementini hesaplar."""
#         # Basit bir döngü mantığı (Örnek: 4 yılda bir döner)
#         # Bunu kendi sistemine göre sonra detaylandırabiliriz.
#         cycle = ["Ateş", "Toprak", "Hava", "Su"]
#         return cycle[year % 4]



# # backend/services/calculator.py
# from core.constants import EBCED_VALUES, LATIN_TO_ARABIC

# class EbcedCalculator:
    
#     @staticmethod
#     def calculate_ebced(text: str) -> int:
#         """İsmin Ebced değerini hesaplar."""
#         toplam = 0
#         temiz_metin = text.upper().strip().replace(" ", "")
        
#         for harf in temiz_metin:
#             if harf in LATIN_TO_ARABIC:
#                 arapca_harf = LATIN_TO_ARABIC[harf]
#                 toplam += EBCED_VALUES.get(arapca_harf, 0)
#         return toplam

#     @staticmethod
#     def calculate_pin_code(ebced_score: int, birth_year: int) -> list:
#         """
#         Doğum tarihi ve Ebced toplamından Pin kodu üretir.
#         Eski mantığın: Toplam = İsim Ebced + Tarih Rakamları Toplamı
#         """
#         # Tarihteki rakamları topla (Örn: 1990 -> 1+9+9+0 = 19)
#         date_sum = sum(int(digit) for digit in str(birth_year))
        
#         total_score = ebced_score + date_sum
        
#         # Pin dizilimi (Sayının rakamlarına ayrılmış hali)
#         pin_list = [int(x) for x in str(total_score)]
#         return pin_list

#     @staticmethod
#     def calculate_element_distribution(ebced_score: int, pin_list: list) -> dict:
#         """
#         Gerçek Element Puanlama Mantığı (Senin eski mizac.py mantığın)
#         """
#         scores = {"Ateş": 0, "Toprak": 0, "Hava": 0, "Su": 0}
        
#         # KURAL 1: İsim Ebced Etkisi (+2 Puan)
#         # Mod 4: 1->Ateş, 2->Toprak, 3->Hava, 0->Su
#         mod = ebced_score % 4
#         if mod == 1: scores["Ateş"] += 2
#         elif mod == 2: scores["Toprak"] += 2
#         elif mod == 3: scores["Hava"] += 2
#         else: scores["Su"] += 2 # mod 0 ise

#         # KURAL 2: Pin Kodu Etkisi (+1 Puan)
#         # Eski koduna göre: <=4 Toprak, <=7 Hava, >7 Ateş
#         for digit in pin_list:
#             if digit <= 4:
#                 scores["Toprak"] += 1
#             elif digit <= 7:
#                 scores["Hava"] += 1
#             else:
#                 scores["Ateş"] += 1

#         # KURAL 3: Tekil Değer Etkisi (+1 Puan)
#         # (ebced % 9 or 9) -> <=2 Ateş, <=4 Toprak, <=6 Hava, Diğeri Su
#         tekil = ebced_score % 9 or 9
#         if tekil <= 2:
#             scores["Ateş"] += 1
#         elif tekil <= 4:
#             scores["Toprak"] += 1
#         elif tekil <= 6:
#             scores["Hava"] += 1
#         else:
#             scores["Su"] += 1
            
#         return scores

#     @staticmethod
#     def get_dominant_element(scores: dict) -> str:
#         """En yüksek puana sahip elementi bulur."""
#         return max(scores, key=scores.get)

#     @staticmethod
#     def calculate_year_element(year: int) -> str:
#         """Yıl elementini hesaplar"""
#         cycle = ["Su", "Ateş", "Toprak", "Hava"] 
#         return cycle[year % 4]


# from core.constants import EBCED_VALUES, LATIN_TO_ARABIC

# class EbcedCalculator:
    
#     @staticmethod
#     def calculate_ebced(text: str) -> int:
#         """Metnin Ebced değerini hesaplar."""
#         toplam = 0
#         temiz_metin = text.upper().strip().replace(" ", "")
        
#         for harf in temiz_metin:
#             if harf in LATIN_TO_ARABIC:
#                 arapca_harf = LATIN_TO_ARABIC[harf]
#                 toplam += EBCED_VALUES.get(arapca_harf, 0)
#         return toplam

#     @staticmethod
#     def reduce_to_single_digit(number: int) -> int:
#         """
#         PDF Kuralı: Sayıyı tek haneye (1-9) indir. [cite: 197]
#         Örn: 148 -> 1+4+8=13 -> 1+3=4
#         """
#         while number > 9:
#             number = sum(int(digit) for digit in str(number))
#         return number

#     @staticmethod
#     def calculate_pin_code(isim: str, soyisim: str, anne_adi: str) -> int:
#         """
#         PDF Sayfa 2 ve 6'daki formül:
#         (İsim + Anne adı + Soyad) -> Tek hane [cite: 40, 63]
#         """
#         val_isim = EbcedCalculator.calculate_ebced(isim)
#         val_soyisim = EbcedCalculator.calculate_ebced(soyisim)
#         val_anne = EbcedCalculator.calculate_ebced(anne_adi)
        
#         toplam_ebced = val_isim + val_soyisim + val_anne
#         return EbcedCalculator.reduce_to_single_digit(toplam_ebced)

#     @staticmethod
#     def calculate_element_distribution(ebced_score: int, pin_code: int) -> dict:
#         """
#         Element puanlama (Senin eski mizac.py mantığın)
#         """
#         scores = {"Ateş": 0, "Toprak": 0, "Hava": 0, "Su": 0}
        
#         # Ebced Etkisi
#         mod = ebced_score % 4
#         if mod == 1: scores["Ateş"] += 2
#         elif mod == 2: scores["Toprak"] += 2
#         elif mod == 3: scores["Hava"] += 2
#         else: scores["Su"] += 2 

#         # Pin Kodu Etkisi (PDF'te element geçmiyor ama eski mantığını koruyoruz)
#         if pin_code <= 4:
#             scores["Toprak"] += 1
#         elif pin_code <= 7:
#             scores["Hava"] += 1
#         else:
#             scores["Ateş"] += 1

#         return scores
from core.constants import EBCED_DEGERLERI, BASKIN_ELEMENT_TANIMLARI, PIN_ANALIZLERI

class EbcedCalculator:
    
    @staticmethod
    def calculate_ebced(text: str) -> int:
        total = 0
        text = text.lower()
        # Türkçe karakter düzeltmeleri
        mapping = {'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u'}
        for k, v in mapping.items():
            text = text.replace(k, v)
            
        for char in text:
            if char in EBCED_DEGERLERI:
                total += EBCED_DEGERLERI[char]
        return total

    @staticmethod
    def calculate_pin_code(isim, soyisim, anne_adi):
        def reduce_to_single(num):
            while num > 9 and num != 11 and num != 22:
                num = sum(int(d) for d in str(num))
            return num

        # 1. Hane: İsim (Sesli+Sessiz)
        hane1 = reduce_to_single(EbcedCalculator.calculate_ebced(isim))
        
        # 2. Hane: Soyisim
        hane2 = reduce_to_single(EbcedCalculator.calculate_ebced(soyisim))
        
        # 3. Hane: İsim + Soyisim
        hane3 = reduce_to_single(hane1 + hane2)
        
        # 4. Hane: Anne Adı
        hane4 = reduce_to_single(EbcedCalculator.calculate_ebced(anne_adi))
        
        # 5. Hane: Hane 4 + Hane 1
        hane5 = reduce_to_single(hane4 + hane1)
        
        # 6. Hane (Pin): Hane 1 + Hane 2 + Hane 3 + Hane 4 + Hane 5
        # (Genelde 6. hane PIN kodu olarak kabul edilir)
        toplam = hane1 + hane2 + hane3 + hane4 + hane5
        pin = reduce_to_single(toplam)
        
        return pin

    @staticmethod
    def analyze_chakras(full_name: str):
        # Basit harf sayımı (Çakralar 1-8 arası)
        full_name = full_name.lower().replace(" ", "")
        counts = {i: 0 for i in range(1, 9)}
        
        # Harflerin hangi çakraya denk geldiği (Basitleştirilmiş)
        # 1: a,j,s,ş | 2: b,k,t | 3: c,ç,l,u,ü | 4: d,m,v | 5: e,n,w | 6: f,o,ö,x | 7: g,ğ,p,y | 8: h,q,z
        chakra_map = {
            'a':1, 'j':1, 's':1, 'ş':1, 
            'b':2, 'k':2, 't':2, 
            'c':3, 'ç':3, 'l':3, 'u':3, 'ü':3,
            'd':4, 'm':4, 'v':4, 
            'e':5, 'n':5, 'w':5,
            'f':6, 'o':6, 'ö':6, 'x':6,
            'g':7, 'ğ':7, 'p':7, 'y':7,
            'h':8, 'q':8, 'z':8, 'i':9, 'ı':9, 'r':9 # 9. Çakra (Bütünlük) genelde 8'in üstüdür ama 9'u 9 olarak sayabiliriz.
        }
        
        # Biz 1-8 sistemine göre normalize edelim (9'u 8'e veya 1'e katabiliriz, burada ayrı tutalım ya da yok sayalım)
        # Standart numerolojide 1-9 arasıdır. Kodumuz 1-8 radar çiziyor. 9'ları pas geçebiliriz veya dağıtabiliriz.
        # Basitlik adına:
        for char in full_name:
            val = chakra_map.get(char)
            if val and val <= 8:
                counts[val] += 1
            elif val == 9:
                # 9. çakra evrenseldir, 1 ve 8'i destekler.
                counts[1] += 0.5
                counts[8] += 0.5
                
        return {"raw_counts": counts}

    @staticmethod
    def calculate_life_path(day, month, year):
        def reduce(n):
            while n > 9 and n != 11 and n != 22:
                n = sum(int(d) for d in str(n))
            return n
        return reduce(reduce(day) + reduce(month) + reduce(year))

    @staticmethod
    def calculate_personal_year(day, month, current_year):
        def reduce(n):
            while n > 9:
                n = sum(int(d) for d in str(n))
            return n
        return reduce(reduce(day) + reduce(month) + reduce(current_year))

    @staticmethod
    def analyze_elements(full_name: str):
        # Harf element haritası
        elements = {"ATEŞ": 0, "TOPRAK": 0, "HAVA": 0, "SU": 0}
        
        # ATEŞ: a, h, t, m
        # TOPRAK: b, n, y, s, ş
        # HAVA: c, ç, l, g, ğ, k
        # SU: d, ı, i, z, f, p
        # (Bu harita ekollere göre değişir, standart bir set kullanıyoruz)
        
        mapping = {
            'a': 'ATEŞ', 'h': 'ATEŞ', 't': 'ATEŞ', 'm': 'ATEŞ',
            'b': 'TOPRAK', 'n': 'TOPRAK', 'y': 'TOPRAK', 's': 'TOPRAK', 'ş': 'TOPRAK',
            'c': 'HAVA', 'ç': 'HAVA', 'l': 'HAVA', 'g': 'HAVA', 'ğ': 'HAVA', 'k': 'HAVA',
            'd': 'SU', 'ı': 'SU', 'i': 'SU', 'z': 'SU', 'f': 'SU', 'p': 'SU',
            'e': 'ATEŞ', 'o': 'SU', 'ö': 'SU', 'u': 'HAVA', 'ü': 'HAVA', 'v': 'TOPRAK', 'r': 'SU' # Ek harfler
        }
        
        for char in full_name.lower().replace(" ", ""):
            if char in mapping:
                elements[mapping[char]] += 1
                
        return elements
        
    @staticmethod
    def analyze_letter_attributes(full_name: str):
        # Nurani ve Zulmani harf analizi (Basit Simülasyon)
        nurani_harfler = "almrkheynqs" # Elif, Lam, Mim, Ra, Kaf, Ha, Ya, Ayn, Sad...
        count = sum(1 for c in full_name.lower() if c in nurani_harfler)
        return {"nurani_puan": count, "toplam_harf": len(full_name)}

    @staticmethod
    def calculate_name_esma_index(name: str):
        # İsim ebcedi mod 99
        val = EbcedCalculator.calculate_ebced(name)
        return val

    @staticmethod
    def calculate_esas_bereket(isim, soyisim):
        # Basit bir toplama algoritması
        return EbcedCalculator.calculate_ebced(isim + soyisim)

    @staticmethod
    def calculate_year_element_pin(year: int):
        # Yılın elementini bulma (Modüler)
        rem = year % 4
        el_map = {0: "SU", 1: "ATEŞ", 2: "TOPRAK", 3: "HAVA"}
        return el_map.get(rem, "ATEŞ")

    @staticmethod
    def detect_element_imbalance(scores: dict):
        # En düşük ve en yüksek arasındaki fark
        vals = list(scores.values())
        if not vals: return "Dengeli"
        diff = max(vals) - min(vals)
        if diff > 5: return "Aşırı Dengesiz"
        if diff > 3: return "Hafif Dengesiz"
        return "Dengeli"
        
    # --- GÜNCELLENEN KISIM: KÜTÜPHANESİZ HİCRİ HESAPLAMA ---
    @staticmethod
    def calculate_hijri_date(day, month, year):
        """
        Kütüphane kullanmadan yaklaşık Hicri tarihi verir.
        (Net hesaplama karmaşıktır, bu bir yaklaşımdır ama sunucuyu çökertmez)
        """
        try:
            # Hicri yıl yaklaşık: (Miladi - 622) * 1.03
            hicri_yil = int((year - 622) * 1.030684)
            return {
                "yil": hicri_yil,
                "ay": "-", # Ay hesaplaması kütüphanesiz zor, boş geçiyoruz
                "gun": day,
                "tarih_str": f"{hicri_yil} (Yaklaşık)"
            }
        except:
            return {"tarih_str": "-"}