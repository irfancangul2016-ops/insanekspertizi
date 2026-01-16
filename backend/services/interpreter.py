# from core.constants import ELEMENT_RELATIONS

# class Analyzer:
#     @staticmethod
#     def generate_comments(user_elements: dict, dominant_element: str, year_element: str) -> list[str]:
#         comments = []
        
#         # 1. Yıl Etkisi Yorumu
#         if dominant_element == year_element:
#             comments.append("Bu yıl senin yılın! İvme kazanırsın.")
#         elif ELEMENT_RELATIONS[dominant_element]["zıt"] == year_element:
#             comments.append(f"Bu yıl zorlayıcı geçecek. {year_element} enerjisi seni frenleyebilir.")
#         else:
#             comments.append("Nötr bir yıl, hazırlık dönemi.")

#         # 2. Eksik Element Yorumu
#         for elem, score in user_elements.items():
#             if score == 0:
#                 comments.append(f"{elem} elementin eksik. Bu alanda denge kurmak için çalışmalısın.")

#         # 3. Mizaç Yorumu (Baskın elemente göre)
#         traits = {
#             "Ateş": "Lider ruhlusun ama öfkeni kontrol etmelisin.",
#             "Toprak": "Sağlamsın ama değişime dirençlisin.",
#             "Hava": "Zekisin ama odaklanma sorunu yaşayabilirsin.",
#             "Su": "Duygusalsın, sezgilerin kuvvetli."
#         }
#         comments.append(traits.get(dominant_element, ""))

#         return comments
    

# # backend/services/interpreter.py
# from core.constants import ELEMENT_RELATIONS

# class Interpreter:
#     @staticmethod
#     def generate_comments(kisi_element: str, yil_element: str, element_skorlari: dict = None) -> list:
#         yorumlar = []
        
#         # 1. Mizaç Yorumu
#         mizac_yorumlari = {
#             "Ateş": "Lider ruhlu, tez canlı ve enerjiksin. Öfke kontrolüne dikkat.",
#             "Toprak": "Sağlamcı, sadık ve düzenlisin. Değişime direnme.",
#             "Hava": "Zeki, iletişimci ve meraklısın. Odaklanma sorunu yaşayabilirsin.",
#             "Su": "Duygusal, sezgisel ve fedakarsın. Sınır çizmeyi öğrenmelisin."
#         }
#         yorumlar.append(mizac_yorumlari.get(kisi_element, ""))

#         # 2. Yıl Etkisi (Senin eski kodundaki mantık)
#         if kisi_element == yil_element:
#             yorumlar.append("Bu yıl senin yılın! İvme yılı, hızlanırsın.")
        
#         elif ELEMENT_RELATIONS[kisi_element]["zıt"] == yil_element:
#             yorumlar.append("Bu yıl zorlayıcı etkiler var. Sabır ve planlama şart.")
        
#         elif ELEMENT_RELATIONS[kisi_element]["destek"] == yil_element:
#             yorumlar.append("Bu yıl çevrenden destek göreceksin, şanslı bir yıl.")
        
#         else:
#             yorumlar.append("Nötr bir yıl. Büyük riskler alma, hazırlık yap.")

#         return yorumlar


# from core.constants import ELEMENT_RELATIONS

# class Interpreter:
#     @staticmethod
#     def generate_comments(kisi_element: str, yil_element: str, element_skorlari: dict = None) -> list:
#         yorumlar = []
        
#         # Mizaç Yorumları
#         mizac_yorumlari = {
#             "Ateş": "Lider ruhlu, tez canlı. Harekete geçme gücün yüksek.",
#             "Toprak": "Sağlamcı ve düzenli. Riske girmeyi sevmezsin.",
#             "Hava": "Zihinsel süreçlerin çok hızlı. Fikirlerin sürekli değişebilir.",
#             "Su": "Duygusal zekan yüksek. Sezgilerinle hareket edersin."
#         }
#         yorumlar.append(mizac_yorumlari.get(kisi_element, ""))

#         # Yıl Etkisi Analizi
#         if kisi_element == yil_element:
#             yorumlar.append(f"Bu yıl {kisi_element} elementinin yılı. Enerjin tavan yapacak, durdurulamazsın.")
        
#         elif ELEMENT_RELATIONS[kisi_element]["zıt"] == yil_element:
#             yorumlar.append(f"Zıtlık yılı ({yil_element}). Engellerle karşılaşabilirsin, sabırlı olmalısın.")
            
#         elif ELEMENT_RELATIONS[kisi_element]["destek"] == yil_element:
#             yorumlar.append("Destekleyici bir yıl. Çevrenden yardım göreceksin.")
        
#         else:
#             yorumlar.append("Nötr bir yıl. Kendi iç dengeni korumalısın.")
            
#         # Eksik Element Uyarısı (Yeni Özellik)
#         if element_skorlari:
#             for elem, puan in element_skorlari.items():
#                 if puan == 0:
#                     yorumlar.append(f"DİKKAT: {elem} elementin hiç yok (0 puan). Bu alanda büyük eksiklik yaşayabilirsin.")

#         return yorumlar


# from core.constants import PIN_ANALIZLERI

# class Interpreter:
#     @staticmethod
#     def generate_pin_report(pin_code: int) -> dict:
#         """
#         PDF'ten gelen veriyi rapora dönüştürür.
#         """
#         data = PIN_ANALIZLERI.get(pin_code, {})
        
#         return {
#             "arketip": data.get("arketip", ""),
#             "guclu_yon": data.get("guclu_yon", ""),
#             "golge_yon": data.get("golge_yon", ""),
#             "kader_dersi": data.get("kader_dersi", ""),
#             "para_iliskisi": data.get("para_temasi", ""),
#             "iliski_durumu": data.get("iliski_temasi", ""),
#             "cakra": data.get("cakra", "")
#         }

#     @staticmethod
#     def generate_summary(pin_data: dict) -> list:
#         yorumlar = []
#         yorumlar.append(f"Kader Arketipin: {pin_data['arketip']}")
#         yorumlar.append(f"GÜÇLÜ YÖNLERİN: {pin_data['guclu_yon']}")
#         yorumlar.append(f"DİKKAT ETMEN GEREKEN GÖLGE YÖN: {pin_data['golge_yon']}")
#         yorumlar.append(f"BU HAYATTAKİ SINAVIN: {pin_data['kader_dersi']}")
#         return yorumlar

# from core.constants import PIN_ANALIZLERI, CAKRA_DETAYLARI, YASAM_YOLU_ANALIZLERI, KISISEL_YIL_ANALIZLERI, PIN_UYUMU, ELEMENT_UYUMU, BEREKET_SAYISI_OZET, BEREKET_ANALIZLERI, DONUSUM_YILLARI_TEMALARI, ELEMENT_ANALIZLERI, KADER_ESMALARI, CAKRA_DENGE_ESMALARI, SURE_ANALIZLERI, ESMA_UL_HUSNA_99, PIN_YAPISAL_ESMALARI, BASKIN_CAKRA_DENGE_ESMALARI, MIZAC_GUC_ESMALARI, MIZAC_YASAM_TARZI, SAYI_OLAY_ALANI, SAYI_GUN_AKTIVASYONU, SAYI_CAKRA_ILISKISI, FREKANS_COZUMLERI, ALAN_TURLERI, SAYI_ALAN_HARITASI, ALAN_AKTIVASYON_YORUMLARI, ELEMENT_ALAN_ILISKISI, YIL_ELEMENTI_MUDALELERI, GUN_ANALIZLERI, GUN_ELEMENTI, MIZAC_REFLEKSLERI, ELEMENT_CAKRA_DETAY, ENERJI_UYGULAMA_ADIMLARI, ENERJI_UYGULAMA_YASAKLARI, ENERJI_UYGULAMA_SONUCLARI

# class Interpreter:
#     @staticmethod
#     def generate_pin_report(pin_code: int) -> dict:
#         data = PIN_ANALIZLERI.get(pin_code, {})
#         return {
#             "arketip": data.get("arketip", "-"),
#             "guclu_yon": data.get("guclu_yon", "-"),
#             "golge_yon": data.get("golge_yon", "-"),
#             "cakra": data.get("cakra", "-")
#         }

#     @staticmethod
#     def generate_full_chakra_report(chakra_data: dict) -> dict:
#         raw_counts = chakra_data["raw_counts"]
#         detayli_rapor = []
#         for cakra_no, adet in raw_counts.items():
#             bilgi = CAKRA_DETAYLARI[cakra_no]
#             if adet <= 1: durum, yorum = "ZAYIF", bilgi["eksik_yorum"]
#             elif adet <= 4: durum, yorum = "DENGELİ", "Enerji akışı sağlıklı."
#             else: durum, yorum = "BASKIN", bilgi["fazla_yorum"]
            
#             detayli_rapor.append({
#                 "cakra": bilgi["isim"],
#                 "adet": adet,
#                 "durum": durum,
#                 "gezegen": bilgi["gezegen"],
#                 "element": bilgi["element"],
#                 "nefes_mertebesi": bilgi["nefes"],
#                 "analiz": yorum
#             })
#         baskin_no = max(raw_counts, key=raw_counts.get)
#         baskin_bilgi = CAKRA_DETAYLARI[baskin_no]
#         zayif_no = min(raw_counts, key=raw_counts.get)
        
#         return {
#             "detayli_rapor": detayli_rapor,
#             "baskin_element": baskin_bilgi["element"],
#             "baskin_gezegen": baskin_bilgi["gezegen"],
#             "baskin_cakra_val": baskin_no,
#             "zayif_cakra_val": zayif_no
#         }

#     @staticmethod
#     def analyze_combination(pin: int, life_path: int) -> str:
#         if pin == 4 and life_path == 3:
#             return "ÇOK NADİR KOMBİNASYON (Sistem Kuran Yaratıcı): Zihin uçar (3), el yapar (4)."
#         return f"Pin {pin} (İç Yapı) ve Yaşam Yolu {life_path} (Dış Kader) birlikte çalışıyor."

#     @staticmethod
#     def generate_abundance_report(esas: int, dongu: int) -> dict:
#         esas_bilgi = BEREKET_ANALIZLERI.get(esas, {})
#         dongu_bilgi = BEREKET_ANALIZLERI.get(dongu, {})
#         if esas == 4 and dongu == 8: ozel = "MÜKEMMEL ZENGİNLİK: Birikim (4) ve Fırsat (8)."
#         elif esas == dongu: ozel = "SAF ENERJİ: Para karakteri ve fırsatlar uyumlu."
#         else: ozel = f"İçsel karakter {esas} ve dış fırsatlar {dongu} dengelenmeli."
#         return {
#             "esas_detay": {"baslik": esas_bilgi.get("baslik", "-"), "para_yolu": esas_bilgi.get("para_yolu", "-"), "risk": esas_bilgi.get("risk", "-"), "para_dongusu": esas_bilgi.get("dongu", "-")},
#             "dongu_detay": {"baslik": dongu_bilgi.get("baslik", "-"), "para_yolu": dongu_bilgi.get("para_yolu", "-"), "risk": dongu_bilgi.get("risk", "-"), "para_dongusu": dongu_bilgi.get("dongu", "-")},
#             "finansal_yorum": ozel
#         }

#     @staticmethod
#     def generate_transformation_report(yil: int, ana_ritim: int, pin_etkisi: int, cakra_etkisi: int) -> dict:
#         ana_bilgi = DONUSUM_YILLARI_TEMALARI.get(ana_ritim, {})
#         yorum = f"{yil} YILI TEMASI: {ana_bilgi.get('tema')} ({ana_ritim}). {ana_bilgi.get('aciklama')} "
#         yorum += f"Pin etkiniz yılı {pin_etkisi} enerjisiyle şekillendiriyor. "
#         return {
#             "yil": yil,
#             "ana_ritim_sayisi": ana_ritim,
#             "ana_tema": ana_bilgi.get("tema", "-"),
#             "pin_etkisi_sayisi": pin_etkisi,
#             "baskin_cakra_etkisi_sayisi": cakra_etkisi,
#             "yil_yorumu": yorum
#         }

#     @staticmethod
#     def generate_element_report(element_scores: dict) -> dict:
#         baskin = max(element_scores, key=element_scores.get)
#         eksik = min(element_scores, key=element_scores.get)
#         bilgi = ELEMENT_ANALIZLERI.get(baskin, {})
#         eksik_bilgi = ELEMENT_ANALIZLERI.get(eksik, {})
#         mizac_yorumu = f"Siz {bilgi.get('mizac')} yapısındasınız. {bilgi.get('ozellik')} özellikleriniz baskın."
#         uyari = f"{eksik} elementiniz düşük. Bu durum {eksik_bilgi.get('eksiklik')} yaratabilir."
#         return {
#             "baskin_element": baskin,
#             "mizac_tipi": bilgi.get("mizac", "-"),
#             "element_puanlari": element_scores,
#             "mizac_yorumu": mizac_yorumu,
#             "eksik_element_uyarisi": uyari
#         }

#     @staticmethod
#     def generate_esma_sure_report(life_path: int, name_esma_idx: int, weak_chakra: int) -> dict:
#         kader_esma = KADER_ESMALARI.get(life_path, "El-Bâkî")
#         isim_esma = ESMA_UL_HUSNA_99.get(name_esma_idx, "El-Latîf (Genel)")
#         if name_esma_idx not in ESMA_UL_HUSNA_99:isim_esma = KADER_ESMALARI.get(life_path, "Er-Rahmân")
#         denge_esma = CAKRA_DENGE_ESMALARI.get(weak_chakra, "Ya Şâfi")
#         onerilen_sureler = []
#         if weak_chakra in [1, 2, 3]: 
#             onerilen_sureler.append(SURE_ANALIZLERI["GUC"])
#             onerilen_sureler.append(SURE_ANALIZLERI["BEREKET"])
#         else:
#             onerilen_sureler.append(SURE_ANALIZLERI["ZIHIN"])
#             onerilen_sureler.append(SURE_ANALIZLERI["KORUMA"])
#         return {
#             "kader_esmasi": kader_esma,
#             "isim_esmasi": isim_esma,
#             "denge_esmasi": denge_esma,
#             "onerilen_sureler": onerilen_sureler,
#             "alan_koruma_tavsiyesi": "Enerjinizi korumak için sabahları Felak & Nas okuyun."
#         }

#     @staticmethod
#     def generate_energy_architecture(pin_code: int, dominant_chakra: int, dominant_element: str) -> dict:
#         yapisal = PIN_YAPISAL_ESMALARI.get(pin_code, "El-Bâkî")
#         dengeleyici = BASKIN_CAKRA_DENGE_ESMALARI.get(dominant_chakra, "El-Muksit")
#         guc = MIZAC_GUC_ESMALARI.get(dominant_element, "El-Kaviyy")
#         rutin = [
#             f"SABAH: '{yapisal}' (33 Kez) -> Günü planlamak ve köklenmek için.",
#             f"GÜN İÇİ: '{dengeleyici}' (11-33 Kez) -> Baskın enerjinizi dengelemek ve akışta kalmak için.",
#             f"AKŞAM: '{guc}' (21 Kez) -> İradenizi güçlendirmek ve günü kapatmak için."
#         ]
#         return {
#             "yapisal_esma": yapisal,
#             "dengeleyici_esma": dengeleyici,
#             "guc_esmasi": guc,
#             "gunluk_uygulama_rutini": rutin
#         }

#     @staticmethod
#     def generate_lifestyle_advice(dominant_element: str) -> dict:
#         advice = MIZAC_YASAM_TARZI.get(dominant_element, MIZAC_YASAM_TARZI["HAVA"])
#         return {
#             "calisma_tarzi": advice["calisma"],
#             "beslenme_onerisi": advice["beslenme"],
#             "iliski_tarzi": advice["iliski"],
#             "para_yonetimi": advice["para"],
#             "spirituel_yol": advice["spirituel"]
#         }

#     @staticmethod
#     def generate_operational_analysis(pin_code: int) -> dict:
#         gun = SAYI_GUN_AKTIVASYONU.get(pin_code, "Bilinmiyor")
#         alan = SAYI_OLAY_ALANI.get(pin_code, "Genel Yaşam")
#         cakra = SAYI_CAKRA_ILISKISI.get(pin_code, "Tüm Çakralar")
#         aciklama = f"Sizin Pin Kodunuz {pin_code}. Bu sayı '{alan}' konularını yönetir. "
#         aciklama += f"Önemli kararlarınızı, başlangıçlarınızı ve enerji çalışmalarınızı {gun} günü yapmanız akışı hızlandırır."
#         return {
#             "aktivasyon_gunu": gun,
#             "kader_alani": alan,
#             "aktif_cakra": cakra,
#             "aciklama": aciklama
#         }

#     @staticmethod
#     def generate_letter_analysis_report(attr_data: dict) -> dict:
#         frekans = attr_data["frekans"]
#         mahal = attr_data["mahal"]
#         baskin_frekans = max(frekans, key=frekans.get)
#         if baskin_frekans == "YUKSEK": f_yorum = "Zihin aşırı aktif, sezgi çok yüksek."
#         elif baskin_frekans == "DUSUK": f_yorum = "Kök ve fiziksel alan güçlü."
#         else: f_yorum = "Kalp ve iletişim odaklı."
#         baskin_mahal = max(mahal, key=mahal.get)
#         if baskin_mahal == "GIRTLAK": m_yorum = "Kader, ruh ve ilham kanalı çok açık."
#         elif baskin_mahal == "DUDAK": m_yorum = "Madde, para ve fiziksel dünya ile bağ güçlü."
#         elif baskin_mahal == "DIL_ORTASI": m_yorum = "Analiz, düşünce ve mantık merkezi baskın."
#         elif baskin_mahal == "BOGAZ_ACIKLIGI": m_yorum = "Vizyon, özgürlük ve yükselme enerjisi."
#         else: m_yorum = "İletişim, ifade ve sosyallik ön planda."
#         return {
#             "frekans_dagilimi": frekans, "baskin_frekans": baskin_frekans, "frekans_yorumu": f_yorum,
#             "mahal_dagilimi": mahal, "baskin_mahal": baskin_mahal, "mahal_yorumu": m_yorum
#         }

#     @staticmethod
#     def generate_frequency_adjustment_report(imbalance_key: str) -> dict:
#         result = FREKANS_COZUMLERI.get(imbalance_key, FREKANS_COZUMLERI["DENGELI"])
#         return {
#             "tespit_edilen_durum": imbalance_key,
#             "dusunce_yapisi_analizi": result["tespit"],
#             "frekans_yukseltme_reçetesi": result["cozum"]
#         }

#     @staticmethod
#     def generate_field_activation_report(
#         name_pin: int, surname_pin: int, birth_pin: int,
#         year_element: str, dominant_element: str, missing_elements: list
#     ) -> dict:
#         active_numbers = []
#         if name_pin == surname_pin: active_numbers.append(name_pin)
#         if name_pin == birth_pin: active_numbers.append(name_pin)
#         if surname_pin == birth_pin: active_numbers.append(surname_pin)
#         active_numbers = list(set(active_numbers))
        
#         active_fields = [SAYI_ALAN_HARITASI.get(num, "GENEL") for num in active_numbers]
        
#         if dominant_element == year_element:
#             year_comment = ALAN_AKTIVASYON_YORUMLARI["ELEMENT_UYUSMASI"]
#             tavsiye = f"Bu yıl {year_element} elementinizin doğasıyla akıyor. Engel yok, tam gaz ilerleyin."
#         elif year_element in missing_elements:
#             year_comment = ALAN_AKTIVASYON_YORUMLARI["EKSIK_ELEMENT"]
#             tavsiye = f"Bu yıl {year_element} enerjisi talep ediyor ama sizde eksik. Bu alanda dışarıdan destek alın."
#         else:
#             year_comment = ALAN_AKTIVASYON_YORUMLARI["ELEMENT_CATISMASI"]
#             tavsiye = f"Sizin doğanız {dominant_element}, bu yıl {year_element}. Bu bir sürtünme yaratır ama büyüme getirir."

#         return {
#             "aktif_sayilar": active_numbers,
#             "aktif_alanlar": active_fields,
#             "yil_elementi": year_element,
#             "yil_etkisi_yorumu": year_comment,
#             "aktivasyon_tavsiyesi": tavsiye
#         }

#     @staticmethod
#     def generate_element_field_analysis(dominant_element: str, year_element: str, missing_elements: list) -> dict:
#         baskin_data = ELEMENT_ALAN_ILISKISI.get(dominant_element, ELEMENT_ALAN_ILISKISI["HAVA"])
#         baskin_alan_yorumu = f"{baskin_data['alan']} ({dominant_element}). {baskin_data['tema']}. Bu alan doğuştan aktiftir."
        
#         yil_data = ELEMENT_ALAN_ILISKISI.get(year_element, ELEMENT_ALAN_ILISKISI["TOPRAK"])
#         yil_yorumu = f"{yil_data['alan']} ({year_element}). Bu yıl evren sizi bu alana zorluyor."
        
#         if dominant_element == year_element:
#             catisma_durumu = YIL_ELEMENTI_MUDALELERI["UYUMLU"]
#             sonuc_yorumu = "Enerjiniz ile zamanın ruhu aynı."
#         elif (dominant_element == "ATES" and year_element == "SU") or (dominant_element == "SU" and year_element == "ATES"):
#             catisma_durumu = YIL_ELEMENTI_MUDALELERI["CATISMA_ATES_SU"]
#             sonuc_yorumu = "Duygularla eylemler savaşıyor."
#         elif (dominant_element == "HAVA" and year_element == "TOPRAK") or (dominant_element == "TOPRAK" and year_element == "HAVA"):
#             catisma_durumu = YIL_ELEMENTI_MUDALELERI["CATISMA_HAVA_TOPRAK"]
#             sonuc_yorumu = "Zihin hızlı, hayat yavaş."
#         else:
#             catisma_durumu = YIL_ELEMENTI_MUDALELERI["GENEL_CATISMA"]
#             sonuc_yorumu = "Konfor alanınızdan farklı bir enerji çalışıyor."
            
#         kilitli_alanlar = []
#         for eksik in missing_elements:
#             data = ELEMENT_ALAN_ILISKISI.get(eksik)
#             if data:
#                 kilitli_alanlar.append(f"{data['alan']} ({eksik} eksikliği)")
                
#         return {
#             "baskin_alan": baskin_alan_yorumu,
#             "yil_mudahalesi": yil_yorumu,
#             "catisma_durumu": catisma_durumu,
#             "kilitli_alanlar": kilitli_alanlar,
#             "analiz_sonucu": sonuc_yorumu
#         }

#     @staticmethod
#     def generate_day_analysis(gun_sayisi: int, kisi_elementi: str, gunun_tarihi: str) -> dict:
#         analiz_data = GUN_ANALIZLERI.get(gun_sayisi, GUN_ANALIZLERI[1])
#         gun_elementi = GUN_ELEMENTI.get(gun_sayisi, "TOPRAK")
        
#         if kisi_elementi == gun_elementi:
#             uyum_mesaji = f"{kisi_elementi} (Siz) + {gun_elementi} (Gün) = Enerji akışı mükemmel."
#         elif (kisi_elementi == "ATES" and gun_elementi == "SU") or (kisi_elementi == "SU" and gun_elementi == "ATES"):
#             uyum_mesaji = f"{kisi_elementi} (Siz) + {gun_elementi} (Gün) = ÇATIŞMA. İçsel baskı."
#         else:
#             uyum_mesaji = f"{kisi_elementi} (Siz) + {gun_elementi} (Gün) = Farklı enerjiler."

#         return {
#             "gunun_tarihi": gunun_tarihi,
#             "gun_sayisi": gun_sayisi,
#             "aktif_cakra": analiz_data["cakra"],
#             "gunun_temasi": analiz_data["tema"],
#             "risk_uyarisi": analiz_data["risk"],
#             "kisi_gun_uyumu": uyum_mesaji
#         }

#     @staticmethod
#     def generate_reflex_report(element_scores: dict) -> dict:
#         baskin = max(element_scores, key=element_scores.get)
#         eksik_liste = [k for k, v in element_scores.items() if v == 0]
#         eksik = eksik_liste[0] if eksik_liste else min(element_scores, key=element_scores.get)
        
#         refleks_data = MIZAC_REFLEKSLERI.get(baskin, MIZAC_REFLEKSLERI["HAVA"])
#         cakra_data = ELEMENT_CAKRA_DETAY.get(baskin, ELEMENT_CAKRA_DETAY["HAVA"])
#         eksik_data = ELEMENT_CAKRA_DETAY.get(eksik, {"alan": "Bilinmiyor"})
        
#         return {
#             "ilk_tepki": refleks_data["tepki"],
#             "bilincalti_sorusu": refleks_data["soru"],
#             "sinir_sistemi_merkezi": f"{cakra_data['merkez']} ({cakra_data['alan']})",
#             "kacis_alani": f"{eksik} ({eksik_data['alan']}) - Eksik olan bu alan, kriz anında kaçtığınız yerdir.",
#             "altin_kural": f"Baskın olan ({baskin}) seni ileri taşır ama eksik olan ({eksik}) seni düşürür. Eksik olana odaklan."
#         }

#     # --- DERS 18: ENERJİ UYGULAMA PLANI (YENİ) ---
#     @staticmethod
#     def generate_energy_practice_guide(element_scores: dict) -> dict:
#         """Ders 18: Kişiselleştirilmiş Enerji Uygulaması"""
#         eksik_element = min(element_scores, key=element_scores.get)
        
#         if eksik_element == "TOPRAK":
#             odak = "Toprak elementiniz zayıf olduğu için 1. ADIM (Bedensel Kanal) sizin için hayati önem taşır. Topraklanmadan diğer adımlara geçmeyin."
#         elif eksik_element == "HAVA":
#             odak = "Hava elementiniz zayıf olduğu için 2. ADIM (Nefesle Akış) kilit noktanızdır. Zihni serbest bırakmaya odaklanın."
#         elif eksik_element == "SU":
#             odak = "Su elementiniz zayıf olduğu için 3. ADIM (Duygu Kanalı) en çok zorlanacağınız ama en çok şifa bulacağınız yerdir. Duyguyu adlandırın."
#         else: # Ateş
#             odak = "Ateş elementiniz zayıf olduğu için 4. ADIM (Algısal Açılım) vizyonunuzu açacak en kritik adımdır."

#         return {
#             "temel_protokol": ENERJI_UYGULAMA_ADIMLARI,
#             "kisisel_odak": odak,
#             "yasaklar": ENERJI_UYGULAMA_YASAKLARI,
#             "dogru_uygulama_belirtileri": ENERJI_UYGULAMA_SONUCLARI["DOGRU"]
#         }

#     @staticmethod
#     def generate_summary(pin_data: dict, lp_data: dict, transformation_data: dict) -> list:
#         return [
#             f"KİŞİSEL YILIN: {transformation_data['ana_tema']} ({transformation_data['ana_ritim_sayisi']})",
#             f"YAŞAM YOLUN: {lp_data.get('baslik', '-')} ({lp_data.get('element', '-')})",
#             f"KADER DÖNGÜSÜ: {lp_data.get('kader', '-')}"
#         ]

#     @staticmethod
#     def analyze_relationship(kisi1_data: dict, kisi2_data: dict) -> dict:
#         toplam_puan = 0
#         p1, p2 = kisi1_data["pin"], kisi2_data["pin"]
#         key = f"{min(p1, p2)}-{max(p1, p2)}"
#         pin_yorum = PIN_UYUMU.get(key, PIN_UYUMU.get("ayni" if p1 == p2 else "komsu" if abs(p1-p2)==1 else "standart", "Standart Etkileşim"))
#         pin_puan = 90 if key in PIN_UYUMU else 70
#         toplam_puan += pin_puan

#         k1_kalp = kisi1_data["cakra"]["raw_counts"].get(4, 0)
#         k2_kalp = kisi2_data["cakra"]["raw_counts"].get(4, 0)
#         cakra_yorum = "GÜÇLÜ BAĞ" if k1_kalp > 1 and k2_kalp > 1 else "DENGE GEREK"
#         cakra_puan = 90 if k1_kalp > 1 and k2_kalp > 1 else 60
#         toplam_puan += cakra_puan

#         e1 = YASAM_YOLU_ANALIZLERI[kisi1_data["life_path"]]["element"].split("/")[0]
#         e2 = YASAM_YOLU_ANALIZLERI[kisi2_data["life_path"]]["element"].split("/")[0]
#         elem_key = (e1, e2) if (e1, e2) in ELEMENT_UYUMU else (e2, e1)
#         element_yorum = ELEMENT_UYUMU.get(elem_key, "Nötr Etkileşim")
#         element_puan = 85 if elem_key in ELEMENT_UYUMU else 70
#         toplam_puan += element_puan

#         lp1, lp2 = kisi1_data["life_path"], kisi2_data["life_path"]
#         lp_yorum = f"Yaşam Yolu {lp1} ve {lp2}."
#         lp_puan = 80
#         toplam_puan += lp_puan

#         b1, b2 = kisi1_data["bereket"], kisi2_data["bereket"]
#         bereket_yorum = f"{BEREKET_SAYISI_OZET.get(b1, '-')} ve {BEREKET_SAYISI_OZET.get(b2, '-')}."
#         bereket_puan = 85
#         toplam_puan += bereket_puan

#         final_score = int(toplam_puan / 5)
        
#         return {
#             "puan": final_score,
#             "ozet": f"Genel Uyum: %{final_score}. {pin_yorum}. {cakra_yorum}. {element_yorum}",
#             "tavsiyeler": ["Birbirinizi dinleyin.", "Farklılıklara saygı duyun."],
#             "detaylar": {
#                 "pin": {"kategori": "Pin Uyumu", "kisi1": str(p1), "kisi2": str(p2), "analiz": pin_yorum, "puan": pin_puan},
#                 "cakra": {"kategori": "Çakra Uyumu", "kisi1": f"Kalp: {k1_kalp}", "kisi2": f"Kalp: {k2_kalp}", "analiz": cakra_yorum, "puan": cakra_puan},
#                 "element": {"kategori": "Element Uyumu", "kisi1": e1, "kisi2": e2, "analiz": element_yorum, "puan": element_puan},
#                 "lp": {"kategori": "Yaşam Yolu", "kisi1": str(lp1), "kisi2": str(lp2), "analiz": lp_yorum, "puan": lp_puan},
#                 "bereket": {"kategori": "Bereket", "kisi1": str(b1), "kisi2": str(b2), "analiz": bereket_yorum, "puan": bereket_puan}
#             }
#         }


from core.constants import *

class Interpreter:
    @staticmethod
    def generate_pin_report(pin_code: int) -> dict:
        # PIN_ANALIZLERI sözlüğünden veriyi çeker
        data = PIN_ANALIZLERI.get(pin_code, {})
        return {
            "arketip": data.get("arketip", "Bilinmiyor"),
            "guclu_yon": data.get("guclu_yon", "-"),
            "golge_yon": data.get("golge_yon", "-"),
            "cakra_karsiligi": data.get("cakra", "-")
        }

    @staticmethod
    def generate_transformation_report(mevcut_yil, kisisel_yil, pin, life_path):
        # Yıl temasını çeker
        yil_verisi = DONUSUM_YILLARI_TEMALARI.get(kisisel_yil, {})
        return {
            "ana_tema": yil_verisi.get("tema", "Belirsiz"),
            "odak_noktasi": yil_verisi.get("aciklama", "-"),
            "strateji": "Akışta kal ve işaretleri izle."
        }

    @staticmethod
    def generate_esma_sure_report(life_path, esma_idx, zayif_cakra):
        # 1. Kişiye Özel Esma'yı Bul (Modüler Aritmetik)
        if esma_idx is None: esma_idx = 1
        
        target_index = esma_idx % 99
        if target_index == 0: target_index = 99
        
        # Sözlükten veriyi çek (Hata önleyici varsayılan değerlerle)
        esma_verisi = ESMA_UL_HUSNA_99.get(target_index, 
            {"ad": "Ya Latif", "anlam": "İncelik ve lütuf sahibi", "zikir": 129}
        )
        
        return {
            "yasam_esmasi": f"{esma_verisi['ad']} (Ebced: {esma_verisi['zikir']})",
            "esma_anlami": esma_verisi['anlam'],
            "destek_suresi": "İnşirah Suresi (Ruhsal Genişleme İçin)",
            "cakra_sifasi": "Bilinçaltı Temizliği ve Topraklanma"
        }

    @staticmethod
    def generate_energy_architecture(pin, baskin_cakra, baskin_element):
        return {
            "enerji_tipi": f"{baskin_element} Ağırlıklı",
            "auratik_renk": "Çivit Mavisi (Tahmini)",
            "merkez_cakra": f"{baskin_cakra}. Çakra"
        }

    @staticmethod
    def generate_full_report_text(raw_data: dict) -> dict:
        """
        Tüm verileri alır ve PDF için okunabilir sözlüklere çevirir.
        Kariyer, Misyon, Esma ve Şifa (Aktar) entegrasyonu buradadır.
        """
        
        # 1. Temel Analizleri Çek
        pin_analiz = Interpreter.generate_pin_report(raw_data.get("pin", 1))
        
        yil_analiz = Interpreter.generate_transformation_report(
            raw_data.get("mevcut_yil", 2026), 
            raw_data.get("personal_year", 1), 
            raw_data.get("pin", 1), 
            raw_data.get("life_path", 1)
        )
        
        esma_raporu = Interpreter.generate_esma_sure_report(
            raw_data.get("life_path", 1), 
            raw_data.get("isim_esma_idx", 99), 
            raw_data.get("zayif_cakra_val", 1)
        )

        # 2. Kariyer, Misyon ve ŞİFA Verilerini Çek
        try:
            kariyer_bilgisi = ELEMENT_KARIYER.get(raw_data.get("baskin_element", "TOPRAK"), {})
            misyon_bilgisi = YASAM_MISYONU.get(raw_data.get("life_path", 1), "Özel bir tekamül yolu.")
            
            # --- YENİ EKLENEN KISIM: AKTAR MODÜLÜ ---
            # Eksik elemente göre şifa önerisi alıyoruz
            eksik_el = raw_data.get("eksik_element", "ATEŞ")
            sifa_bilgisi = ELEMENT_SIFALARI.get(eksik_el, {
                "cay": "Karışık Bitki Çayı", "yag": "Lavanta", "aktivite": "Denge çalışmaları"
            })
            
        except NameError:
            kariyer_bilgisi = {"tarz": "-", "alanlar": "-", "uyari": "-"}
            misyon_bilgisi = "-"
            sifa_bilgisi = {"cay": "-", "yag": "-", "aktivite": "-"}

        # 3. Rapor Bölümlerini İnşa Et
        
        # BÖLÜM 1: KİMLİK
        kimlik_bolumu = {
            "baslik": "I. KOZMİK KİMLİK HARİTASI",
            "ruhsal_arketip": f"{raw_data.get('pin', 0)} - {pin_analiz['arketip']}",
            "yasam_yolu_sayisi": f"{raw_data.get('life_path', 0)} (Kader Yolu)",
            "dunyaya_gelis_amaci": misyon_bilgisi,
            "mizac_yapisi": f"{raw_data.get('baskin_element', '-')} Elementi ({raw_data.get('refleks_tipi', '-')})",
            "iletisim_tarzi": pin_analiz['guclu_yon']
        }

        # BÖLÜM 2: TESPİT
        try:
            max_puan = max(raw_data.get('element_skorlari', {'A':0}).values())
        except:
            max_puan = 0

        tespit_bolumu = {
            "baslik": "II. ENERJİ VE DENGE ANALİZİ",
            "baskin_element_gücü": f"{raw_data.get('baskin_element', '-')} (Puan: {max_puan})",
            "zayif_halka": f"{raw_data.get('eksik_element', '-')} Elementi Eksik!",
            "enerji_kacagi_tespiti": f"{raw_data.get('zayif_cakra_val', '-')} . Çakra Blokajı",
            "frekans_durumu": raw_data.get('frekans_durumu', 'Stabil'),
            "isim_titresimi": "Yüksek (Nurali Harfler Mevcut)"
        }

        # BÖLÜM 3: GELECEK & KARİYER
        gelecek_bolumu = {
            "baslik": "III. GELECEK VE KARİYER ROTASI",
            "bu_yilin_temasi": f"{yil_analiz['ana_tema']} ({raw_data.get('mevcut_yil', 2026)})",
            "yil_stratejisi": yil_analiz['odak_noktasi'],
            "uyumlu_yil_mi": raw_data.get('yil_uyumu_yorumu', '-'),
            "calisma_tarziniz": kariyer_bilgisi.get("tarz", "-"),
            "ideal_meslekler": kariyer_bilgisi.get("alanlar", "-"),
            "is_hayatinda_uyari": kariyer_bilgisi.get("uyari", "-")
        }

        # BÖLÜM 4: REÇETE (Güncellendi)
        recete_bolumu = {
            "baslik": "IV. ŞİFA VE DÖNÜŞÜM REÇETESİ",
            "size_ozel_esma": esma_raporu["yasam_esmasi"],
            "esmanin_hikmeti": esma_raporu["esma_anlami"],
            "dogal_tas_onerisi": "Ametist ve Sitrin", # İstersen bunu da dinamikleştirebilirsin
            "ruhsal_odev": esma_raporu["destek_suresi"],
            # --- ŞİFA ÖNERİLERİNİ BURAYA EKLİYORUZ ---
            "sifali_bitki_cayi": sifa_bilgisi["cay"],
            "aromaterapi_yagi": sifa_bilgisi["yag"],
            "dengeleyici_aktivite": sifa_bilgisi["aktivite"],
            "yasakli_davranislar": "..." # AI Dolduracak
        }

        return {
            "kimlik": kimlik_bolumu,
            "tespit": tespit_bolumu,
            "gelecek": gelecek_bolumu,
            "recete": recete_bolumu
        }