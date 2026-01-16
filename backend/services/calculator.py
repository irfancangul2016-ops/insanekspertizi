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
from hijri_converter import convert
from core.constants import *

class EbcedCalculator:
    @staticmethod
    def calculate_pin_code(isim: str, soyisim: str, anne_adi: str) -> int:
        def get_mod9_value(text):
            """
            Metnin Ebced değerini bulur ve 9'a göre modunu (1-9 arası) döndürür.
            Önce İSTİSNA SÖZLÜĞÜNE bakar.
            """
            if not text: return 0
            
            temiz_isim = text.upper().strip()
            
            # 1. ADIM: SÖZLÜK KONTROLÜ (Gerçek Ebced)
            # İsim sözlükte varsa, direkt oradaki sayıyı al (Örn: MEHMET -> 92)
            if temiz_isim in OZEL_ISIM_DEGERLERI:
                raw_value = OZEL_ISIM_DEGERLERI[temiz_isim]
            
            # 2. ADIM: İKİ İSİMLİLERİ KONTROL ET (Örn: "YAHYA HAMZA")
            # Sözlükte tek parça bulamadıysa, boşluktan bölüp tek tek bak.
            elif " " in temiz_isim:
                parts = temiz_isim.split()
                total_parts = 0
                for part in parts:
                    if part in OZEL_ISIM_DEGERLERI:
                        total_parts += OZEL_ISIM_DEGERLERI[part]
                    else:
                        # Sözlükte yoksa harf harf topla
                        for char in part:
                            total_parts += HARF_DEGERLERI.get(char, 0)
                raw_value = total_parts
            
            # 3. ADIM: HİÇBİR YERDE YOKSA HARF HARF TOPLA (Latin Usulü)
            else:
                raw_value = 0
                for char in temiz_isim:
                    raw_value += HARF_DEGERLERI.get(char, 0)
            
            # 4. ADIM: 9'A İNDİRGEME (Sadeleştirme)
            while raw_value > 9:
                raw_value = sum(int(digit) for digit in str(raw_value))
            
            return raw_value

        # Ana Hesaplama
        isim_val = get_mod9_value(isim)
        soyisim_val = get_mod9_value(soyisim)
        anne_val = get_mod9_value(anne_adi)
        
        # Pin Kodu Haritası (Kozmik Hesaplama)
        hane1 = get_mod9_value(str(isim_val + soyisim_val)) # Kişilik
        hane2 = get_mod9_value(str(anne_val))               # Çocukluk/Duygu
        hane3 = get_mod9_value(str(hane1 + hane2))          # Yaşam Amacı
        hane4 = get_mod9_value(str(hane3 + hane2))          # Bilinçaltı
        hane5 = get_mod9_value(str(hane1 + hane4))          # Orta Yaş
        hane6 = get_mod9_value(str(hane1 + hane2 + hane3))  # Olgunluk
        hane7 = get_mod9_value(str(hane2 + hane5))          # Geçiş Kapısı
        hane8 = get_mod9_value(str(hane6 + hane7))          # Ruhsal Miras
        
        # Sonuç (Genelde 1. Hane "Kişinin Sayısı" kabul edilir ama biz pin haritasını dönmek yerine şimdilik ana kodu dönelim)
        return hane1

    @staticmethod
    def analyze_chakras(full_name: str) -> dict:
        counts = {i: 0 for i in range(1, 10)}
        for char in full_name.upper():
            if char in HARF_DEGERLERI:
                val = HARF_DEGERLERI[char]
                # Numerolojide harf değerleri 1-9 arasıdır, çakra da öyledir
                mod_val = val % 9
                if mod_val == 0: mod_val = 9
                counts[mod_val] += 1
        return {"raw_counts": counts}

    @staticmethod
    def calculate_life_path(gun: int, ay: int, yil: int) -> int:
        def reduce_to_single(n):
            while n > 9 and n not in [11, 22, 33]: # Master sayılar korunur
                n = sum(int(d) for d in str(n))
            return n
        return reduce_to_single(reduce_to_single(gun) + reduce_to_single(ay) + reduce_to_single(yil))

    @staticmethod
    def calculate_personal_year(gun: int, ay: int, mevcut_yil: int) -> int:
        def reduce(n):
            while n > 9: n = sum(int(d) for d in str(n))
            return n
        return reduce(reduce(gun) + reduce(ay) + reduce(mevcut_yil))

    @staticmethod
    def analyze_elements(full_name: str) -> dict:
        scores = {"ATEŞ": 0, "TOPRAK": 0, "HAVA": 0, "SU": 0}
        for char in full_name.upper():
            elem = HARF_ELEMENTLERI.get(char)
            if elem:
                scores[elem] += 1
        return scores

    @staticmethod
    def analyze_letter_attributes(full_name: str) -> dict:
        ozellikler = {"Noktalı": 0, "Nurani": 0, "Zulmani": 0}
        for char in full_name.upper():
            if char in HARF_OZELLIKLERI["NOKTALI"]: ozellikler["Noktalı"] += 1
            if char in HARF_OZELLIKLERI["NURANI"]: ozellikler["Nurani"] += 1
            if char in HARF_OZELLIKLERI["ZULMANI"]: ozellikler["Zulmani"] += 1
        return ozellikler

    @staticmethod
    def calculate_name_esma_index(name: str) -> int:
        total = 0
        for char in name.upper():
            total += HARF_DEGERLERI.get(char, 0)
        return (total % 99) if total % 99 != 0 else 99

    @staticmethod
    def calculate_esas_bereket(isim: str, soyisim: str) -> int:
        # İsim ve Soyisim baş harfleri
        if not isim or not soyisim: return 0
        ilk_harf = isim[0].upper()
        son_harf = soyisim[0].upper()
        val = HARF_DEGERLERI.get(ilk_harf, 0) + HARF_DEGERLERI.get(son_harf, 0)
        while val > 9: val = sum(int(d) for d in str(val))
        return val

    @staticmethod
    def calculate_dongu_bereket(gun: int, ay: int) -> int:
        val = gun + ay
        while val > 9: val = sum(int(d) for d in str(val))
        return val

    @staticmethod
    def calculate_year_element_pin(year: int) -> str:
        # Basit bir element döngüsü (Örnek mantık)
        rem = year % 4
        if rem == 0: return "ATEŞ"
        if rem == 1: return "HAVA"
        if rem == 2: return "SU"
        return "TOPRAK"

    @staticmethod
    def detect_element_imbalance(scores: dict) -> int:
        # Element dengesizliği kodu (Frekans analizi için)
        # Örnek: Eğer ateş çok yüksekse kod 1, su yoksa kod 2 vb.
        # Şimdilik en düşük olanın puanını döndürelim (Basitleştirilmiş)
        return min(scores.values())

    # --- YENİ EKLENEN KISIM: HİCRİ TAKVİM ---
    @staticmethod
    def calculate_hijri_date(gun: int, ay: int, yil: int) -> dict:
        """
        Miladi tarihi Hicri tarihe çevirir ve o ayın manevi temasını bulur.
        """
        try:
            hicri = convert.Gregorian(yil, ay, gun).to_hijri()
            
            # Hicri Ayların Manevi Temaları
            ay_temalari = {
                1: "Muharrem (Başlangıç ve Hürmet)",
                2: "Safer (Korunma ve Tedbir)",
                3: "Rebiülevvel (Nur ve Doğuş)",
                4: "Rebiülahir (Toparlanma)",
                5: "Cemaziyelevvel (Sessizlik)",
                6: "Cemaziyelahir (Hazırlık)",
                7: "Recep (Arınma ve Yükseliş)",
                8: "Şaban (Berat ve Kader)",
                9: "Ramazan (Rahmet ve Oruç)",
                10: "Şevval (Kutlama ve Sevinç)",
                11: "Zilkade (Oturma ve Barış)",
                12: "Zilhicce (Hac ve Teslimiyet)"
            }

            ay_adi = ay_temalari.get(hicri.month, "Bilinmiyor")
            
            # Ayın hangi evresinde doğmuş?
            ay_evresi = ""
            if 1 <= hicri.day <= 5: ay_evresi = "Yeni Ay (Tohum Atma Enerjisi)"
            elif 6 <= hicri.day <= 12: ay_evresi = "İlk Dördün (Büyüme Enerjisi)"
            elif 13 <= hicri.day <= 16: ay_evresi = "Dolunay (Zirve ve Tamamlanma Enerjisi)"
            elif 17 <= hicri.day <= 24: ay_evresi = "Son Dördün (Hasat ve Bırakma Enerjisi)"
            else: ay_evresi = "Kapanan Ay (İçe Dönüş Enerjisi)"

            return {
                "tarih_str": f"{hicri.day} {hicri.month_name()} {hicri.year}",
                "ay_temasi": ay_adi,
                "ay_evresi": ay_evresi
            }
        except Exception as e:
            return {"tarih_str": "Hesaplanamadı", "ay_temasi": "-", "ay_evresi": "-"}