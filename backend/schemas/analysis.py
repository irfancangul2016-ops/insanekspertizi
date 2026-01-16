# from pydantic import BaseModel

# class AnalysisRequest(BaseModel):
#     name: str
#     birth_year: int
#     current_year: int

# class AnalysisResponse(BaseModel):
#     ebced_score: int
#     dominant_element: str
#     year_element: str
#     comments: list[str]


# # backend/schemas/analysis.py
# from pydantic import BaseModel
# from typing import List, Dict

# # Kullanıcıdan ne isteyeceğiz?
# class AnalizIstegi(BaseModel):
#     isim: str
#     soyisim: str
#     dogum_yili: int # Yıl elementini bulmak için gerekli
#     mevcut_yil: int = 2026

# # Kullanıcıya ne vereceğiz?
# class AnalizSonucu(BaseModel):
#     tam_isim: str
#     ebced_degeri: int
#     kisi_elementi: str      # Kişinin baskın elementi
#     yil_elementi: str       # O yılın elementi
#     element_puanlari: Dict[str, int] # Örn: {"Ateş": 2, "Su": 0...}
#     yorumlar: List[str]     # Yapay zeka veya algoritma yorumları
    

# from pydantic import BaseModel
# from typing import List, Dict, Optional, Any

# # --- ALT MODELLER ---
# class CakraDetayModel(BaseModel):
#     cakra: str
#     adet: int
#     durum: str
#     gezegen: str
#     element: str
#     nefes_mertebesi: str
#     analiz: str

# class YasamYoluDetayModel(BaseModel):
#     baslik: str
#     element: str
#     anahtar: str
#     guclu: str
#     zayif: str
#     kader: str

# class PinDetayModel(BaseModel):
#     arketip: str
#     guclu_yon: str
#     golge_yon: str
#     cakra: str

# class IliskiDetayModel(BaseModel):
#     kategori: str
#     kisi1_deger: str
#     kisi2_deger: str
#     analiz: str
#     puan: int

# class BereketDetayModel(BaseModel):
#     baslik: str
#     para_yolu: str
#     risk: str
#     para_dongusu: str

# class BereketSonucModel(BaseModel):
#     esas_bereket_sayisi: int
#     esas_bereket_detay: BereketDetayModel
#     dongu_bereket_sayisi: int
#     dongu_bereket_detay: BereketDetayModel
#     finansal_yorum: str

# class DonusumYiliModel(BaseModel):
#     yil: int
#     ana_ritim_sayisi: int
#     ana_tema: str
#     pin_etkisi_sayisi: int
#     baskin_cakra_etkisi_sayisi: int
#     yil_yorumu: str

# class ElementDetayModel(BaseModel):
#     baskin_element: str
#     mizac_tipi: str
#     element_puanlari: Dict[str, int]
#     mizac_yorumu: str
#     eksik_element_uyarisi: str

# class EsmaSureDetayModel(BaseModel):
#     kader_esmasi: str
#     isim_esmasi: str
#     denge_esmasi: str
#     onerilen_sureler: List[str]
#     alan_koruma_tavsiyesi: str

# class EnerjiMimariModel(BaseModel):
#     yapisal_esma: str
#     dengeleyici_esma: str
#     guc_esmasi: str
#     gunluk_uygulama_rutini: List[str]

# class MizacYasamTarziModel(BaseModel):
#     calisma_tarzi: str
#     beslenme_onerisi: str
#     iliski_tarzi: str
#     para_yonetimi: str
#     spirituel_yol: str

# class OperasyonelAnalizModel(BaseModel):
#     aktivasyon_gunu: str
#     kader_alani: str
#     aktif_cakra: str
#     aciklama: str

# class HarfAnaliziModel(BaseModel):
#     frekans_dagilimi: Dict[str, int]
#     baskin_frekans: str
#     frekans_yorumu: str
#     mahal_dagilimi: Dict[str, int]
#     baskin_mahal: str
#     mahal_yorumu: str

# class FrekansAnaliziModel(BaseModel):
#     tespit_edilen_durum: str
#     dusunce_yapisi_analizi: str
#     frekans_yukseltme_reçetesi: str

# class AlanAktivasyonuModel(BaseModel):
#     aktif_sayilar: List[int]
#     aktif_alanlar: List[str]
#     yil_elementi: str
#     yil_etkisi_yorumu: str
#     aktivasyon_tavsiyesi: str

# class ElementAlanDetayModel(BaseModel):
#     baskin_alan: str
#     yil_mudahalesi: str
#     catisma_durumu: str
#     kilitli_alanlar: List[str]
#     analiz_sonucu: str

# class GunAnaliziModel(BaseModel):
#     gunun_tarihi: str
#     gun_sayisi: int
#     aktif_cakra: str
#     gunun_temasi: str
#     risk_uyarisi: str
#     kisi_gun_uyumu: str

# class RefleksAnaliziModel(BaseModel):
#     ilk_tepki: str
#     bilincalti_sorusu: str
#     sinir_sistemi_merkezi: str
#     kacis_alani: str
#     altin_kural: str

# class EnerjiUygulamaModel(BaseModel):
#     temel_protokol: List[Dict[str, str]]
#     kisisel_odak: str
#     yasaklar: List[str]
#     dogru_uygulama_belirtileri: str

# # --- GİRİŞ MODELLERİ ---
# class KisiBilgisi(BaseModel):
#     isim: str
#     soyisim: str
#     anne_adi: str
#     dogum_gunu: int
#     dogum_ayi: int
#     dogum_yili: int

# class AnalizIstegi(BaseModel):
#     isim: str
#     soyisim: str
#     anne_adi: str
#     dogum_gunu: int
#     dogum_ayi: int
#     dogum_yili: int
#     mevcut_yil: int = 2025
#     mevcut_gun: Optional[int] = None
#     mevcut_ay: Optional[int] = None

# class IliskiAnaliziIstegi(BaseModel):
#     kisi1: KisiBilgisi
#     kisi2: KisiBilgisi
#     mevcut_yil: int = 2025

# # --- SONUÇ MODELLERİ ---

# class AnalizSonucu(BaseModel):
#     tam_isim: str
#     pin_kodu: int
#     pin_arketipler: PinDetayModel
#     cakra_tablosu: Dict[str, int]
#     cakra_detaylari: List[CakraDetayModel]
#     baskin_element: str
#     baskin_gezegen: str
#     yasam_yolu_sayisi: int
#     yasam_yolu_detay: YasamYoluDetayModel
#     ozel_kombinasyon: str
#     para_analizi: BereketSonucModel
#     donusum_yili_analizi: DonusumYiliModel
#     element_mizac_analizi: ElementDetayModel
#     esma_sure_analizi: EsmaSureDetayModel
#     enerji_mimarisi: EnerjiMimariModel
#     mizac_yasam_tarzi: MizacYasamTarziModel
#     operasyonel_analiz: OperasyonelAnalizModel
#     harf_analizi: HarfAnaliziModel
#     frekans_analizi: FrekansAnaliziModel
#     alan_aktivasyonu_analizi: AlanAktivasyonuModel
#     element_alan_analizi: ElementAlanDetayModel
#     gun_analizi: GunAnaliziModel
#     refleks_analizi: RefleksAnaliziModel
#     enerji_uygulama_plani: EnerjiUygulamaModel
    
#     yorumlar: List[str]

#     model_config = {
#         "json_schema_extra": {
#             "example": {
#                 "tam_isim": "YAHYA HAMZA GÜL",
#                 "pin_kodu": 4,
#                 "pin_arketipler": {
#                     "arketip": "Sistemci",
#                     "guclu_yon": "Disiplin, düzen ve inşaa etme",
#                     "golge_yon": "Takıntı, kontrolcülük ve esnememe",
#                     "cakra": "Solar Pleksus"
#                 },
#                 "cakra_tablosu": {
#                     "Kök": 2,
#                     "Sakral": 1,
#                     "Solar": 2,
#                     "Kalp": 4,
#                     "Boğaz": 0,
#                     "3.Göz": 5,
#                     "Taç": 1
#                 },
#                 "cakra_detaylari": [
#                     {
#                         "cakra": "Kök Çakra",
#                         "adet": 2,
#                         "durum": "DENGELİ",
#                         "gezegen": "Satürn",
#                         "element": "Toprak",
#                         "nefes_mertebesi": "Nefs-i Emmare",
#                         "analiz": "Enerji akışı sağlıklı ve dengeli."
#                     }
#                 ],
#                 "baskin_element": "HAVA",
#                 "baskin_gezegen": "Merkür",
#                 "yasam_yolu_sayisi": 3,
#                 "yasam_yolu_detay": {
#                     "baslik": "Yaratıcı",
#                     "element": "Ateş",
#                     "anahtar": "İfade",
#                     "guclu": "Hitabet, sanat ve sahne ışığı.",
#                     "zayif": "Dağınıklık ve yüzeysellik.",
#                     "kader": "Kendini ifade etmezsen enerjin patlar."
#                 },
#                 "ozel_kombinasyon": "Sistem Kuran Yaratıcı: Zihin uçar (3), el yapar (4).",
#                 "para_analizi": {
#                     "esas_bereket_sayisi": 4,
#                     "esas_bereket_detay": {
#                         "baslik": "SİSTEM BEREKETİ",
#                         "para_yolu": "Sabit gelir, gayrimenkul ve kurumsal düzen.",
#                         "risk": "Aşırı kontrol yüzünden fırsat kaçırma.",
#                         "para_dongusu": "Yavaş ama sürekli yükselen."
#                     },
#                     "dongu_bereket_sayisi": 8,
#                     "dongu_bereket_detay": {
#                         "baslik": "GÜÇ BEREKETİ",
#                         "para_yolu": "Yatırım, yönetim, büyük organizasyonlar.",
#                         "risk": "Güç savaşları ve büyük riskler.",
#                         "para_dongusu": "Yüksek gelgitler ama yüksek tavan."
#                     },
#                     "finansal_yorum": "MÜKEMMEL ZENGİNLİK POTANSİYELİ: Para biriktirir (4) ve büyük fırsatları çekersiniz (8)."
#                 },
#                 "donusum_yili_analizi": {
#                     "yil": 2026,
#                     "ana_ritim_sayisi": 9,
#                     "ana_tema": "BİTİŞ / TEMİZLİK",
#                     "pin_etkisi_sayisi": 9,
#                     "baskin_cakra_etkisi_sayisi": 6,
#                     "yil_yorumu": "2026 YILI TEMASI: BİTİŞ / TEMİZLİK (9). Kapanış yılı. İşe yaramayan her şey hayatından çıkar. BU BİR KAPANIŞ VE TEMİZLİK YILIDIR. Yeniye yer açmak için eskiler gider."
#                 },
#                 "element_mizac_analizi": {
#                     "baskin_element": "HAVA",
#                     "mizac_tipi": "AKLİ MİZAÇ (Soğuk-Kuru)",
#                     "element_puanlari": {"HAVA": 5, "ATES": 3, "SU": 2, "TOPRAK": 1},
#                     "mizac_yorumu": "Siz AKLİ MİZAÇ yapısındasınız. Analiz, strateji, sistem kurma özellikleriniz baskın.",
#                     "eksik_element_uyarisi": "TOPRAK elementiniz düşük. Bu durum Para tutamama, dağınıklık, istikrar sorunu yaratabilir."
#                 },
#                 "esma_sure_analizi": {
#                     "kader_esmasi": "El-Melik, El-Adl (Yönetici, Düzen Kuran)",
#                     "isim_esmasi": "El-Latîf (Genel)",
#                     "denge_esmasi": "El-Kuddûs (Topraklanma ve Arınma)",
#                     "onerilen_sureler": ["Fatiha & Nasr (Otorite ve Zafer İçin)", "Vâki'a & Rahmân (Rızık ve Bolluk İçin)"],
#                     "alan_koruma_tavsiyesi": "Enerjinizi korumak için sabahları Felak & Nas okuyun, akşamları 'Ya Hâfız' zikri çekin."
#                 },
#                 "enerji_mimarisi": {
#                     "yapisal_esma": "El-Melik (Mülkün Sahibi, Düzen Kuran)",
#                     "dengeleyici_esma": "El-Latîf (Zihin çoksa incelik için)",
#                     "guc_esmasi": "El-Habîr (Haberdar Olan)",
#                     "gunluk_uygulama_rutini": [
#                         "SABAH: 'El-Melik (Mülkün Sahibi, Düzen Kuran)' (33 Kez) -> Günü planlamak ve köklenmek için.",
#                         "GÜN İÇİ: 'El-Latîf (Zihin çoksa incelik için)' (11-33 Kez) -> Baskın enerjinizi dengelemek ve akışta kalmak için.",
#                         "AKŞAM: 'El-Habîr (Haberdar Olan)' (21 Kez) -> İradenizi güçlendirmek ve günü kapatmak için."
#                     ]
#                 },
#                 "mizac_yasam_tarzi": {
#                     "calisma_tarzi": "40 dk odak / 10 dk mola. Yazmak, anlatmak, analiz etmek. Kaostan uzak dur.",
#                     "beslenme_onerisi": "Sıcak ve ıslak gıdalar (Et, zencefil, bal). Kuru gıdalardan kaçın.",
#                     "iliski_tarzi": "Zihinsel uyum şart. Güven testi yapar. Su ve Ateş ile iyi anlaşır.",
#                     "para_yonetimi": "Analizci. Parayı zihinden kazanır. Düzenli gelir sistemi şart.",
#                     "spirituel_yol": "Bilgi ve derinlik yolu. Yazılı analiz, tefekkür."
#                 },
#                 "operasyonel_analiz": {
#                     "aktivasyon_gunu": "PERŞEMBE (Jüpiter Günü - Karar/Düzen)",
#                     "kader_alani": "Düzen / Sistem / Kontrol",
#                     "aktif_cakra": "Solar Pleksus",
#                     "aciklama": "Sizin Pin Kodunuz 4. Bu sayı 'Düzen / Sistem / Kontrol' konularını yönetir. Önemli kararlarınızı, başlangıçlarınızı ve enerji çalışmalarınızı PERŞEMBE (Jüpiter Günü - Karar/Düzen) günü yapmanız akışı hızlandırır."
#                 },
#                 "harf_analizi": {
#                     "frekans_dagilimi": {"YUKSEK": 5, "ORTA": 3, "DUSUK": 1},
#                     "baskin_frekans": "YUKSEK",
#                     "frekans_yorumu": "Zihin aşırı aktif, sezgi çok yüksek, enerji yukarıda. Kafa çalışıyor ama beden eşlik etmeyebilir (Topraklanma şart).",
#                     "mahal_dagilimi": {"GIRTLAK": 4, "DUDAK": 1},
#                     "baskin_mahal": "GIRTLAK",
#                     "mahal_yorumu": "Kader, ruh ve ilham kanalı çok açık. Sezgisel analiz gücü."
#                 },
#                 "frekans_analizi": {
#                     "tespit_edilen_durum": "HAVA_FAZLA_TOPRAK_EKSIK",
#                     "dusunce_yapisi_analizi": "Düşük Frekans: Zihin kaosu, Başlayıp bitirememe, Kaçış.",
#                     "frekans_yukseltme_reçetesi": "Daha çok düşünme! Toprakla somutlaştır (Yazarak planla, doğaya çık)."
#                 },
#                 "alan_aktivasyonu_analizi": {
#                     "aktif_sayilar": [4],
#                     "aktif_alanlar": ["FIZIKSEL (Düzen/Beden)"],
#                     "yil_elementi": "ATES",
#                     "yil_etkisi_yorumu": "ALAN ÇATIŞMASI: Senin doğan ile yılın elementi zıt. Kriz ve sürtünme ile büyüme yılı.",
#                     "aktivasyon_tavsiyesi": "Sizin doğanız HAVA, bu yıl ATES. Bu bir sürtünme yaratır ama büyüme getirir."
#                 },
#                 "element_alan_analizi": {
#                     "baskin_alan": "ZİHİNSEL / İLETİŞİM (HAVA). Analiz, Öğrenme, Konuşma. Bu alan doğuştan aktiftir.",
#                     "yil_mudahalesi": "SOSYAL / EYLEM (ATES). Bu yıl evren sizi bu alana zorluyor.",
#                     "catisma_durumu": "GENEL_CATISMA",
#                     "kilitli_alanlar": ["FİZİKSEL / KADERSEL (TOPRAK eksikliği)"],
#                     "analiz_sonucu": "Konfor alanınızdan farklı bir enerji çalışıyor. Uyumlanmak için esnek olun."
#                 },
#                 "gun_analizi": {
#                     "gunun_tarihi": "15/01/2026",
#                     "gun_sayisi": 6,
#                     "aktif_cakra": "Üçüncü Göz (6)",
#                     "gunun_temasi": "Algı, Sezgi, Rüya",
#                     "risk_uyarisi": "Kuruntu, Paranoia, Aşırı Anlam Yükleme",
#                     "kisi_gun_uyumu": "HAVA (Siz) + HAVA (Gün) = Enerji akışı mükemmel. Kendi doğanızda hareket edin."
#                 },
#                 "refleks_analizi": {
#                     "ilk_tepki": "Konuşur / Fikir Üretir",
#                     "bilincalti_sorusu": "Ne olabilir?",
#                     "sinir_sistemi_merkezi": "Boğaz + Alın (Zihin - İletişim)",
#                     "kacis_alani": "TOPRAK (Güven - Düzen) - Eksik olan bu alan, kriz anında kaçtığınız yerdir.",
#                     "altin_kural": "Baskın olan (HAVA) seni ileri taşır ama eksik olan (TOPRAK) seni düşürür. Eksik olana odaklan."
#                 },
#                 "enerji_uygulama_plani": {
#                     "temel_protokol": [
#                         {
#                             "adim": 1,
#                             "isim": "BEDENSEL KANAL AÇMA (Topraklanma)",
#                             "nasil": "Ayakta durun, ayak tabanlarınızı yere güçlüce basın. İçinizden 'Buradayım' deyin.",
#                             "etki": "Zihni sakinleştirir, enerjiyi bedene indirir.",
#                             "uygun_element": "TOPRAK"
#                         },
#                         {
#                             "adim": 2,
#                             "isim": "NEFESLE AKIŞ SERBESTLEŞTİRME",
#                             "nasil": "Nefesi yönetmeyin, sadece izleyin. İçinizden 'Kontrol etmiyorum' deyin.",
#                             "etki": "Bastırılmış duyguyu çözer, akışı sağlar.",
#                             "uygun_element": "HAVA"
#                         }
#                     ],
#                     "kisisel_odak": "Toprak elementiniz zayıf olduğu için 1. ADIM (Bedensel Kanal) sizin için hayati önem taşır. Topraklanmadan diğer adımlara geçmeyin.",
#                     "yasaklar": [
#                         "Öfkeliyken (Enerji patlaması yaşatır)",
#                         "Aşıkken / Yoğun Duygudayken (Denge bozulur)",
#                         "Uykusuzken (Sinir sistemi kaldırmaz)"
#                     ],
#                     "dogru_uygulama_belirtileri": "Sakinlik, netlik, bedende ağırlık hissi (Topraklanma) ve huzur."
#                 },
#                 "yorumlar": [
#                     "KİŞİSEL YILIN: BİTİŞ YILI: Temizlik ve sadeleşme zamanı.",
#                     "YAŞAM YOLUN: Yaratıcı (Ateş)",
#                     "KADER DÖNGÜSÜ: İfade etmezsen patlarsın."
#                 ]
#             }
#         }
#     }

# class IliskiAnaliziSonucu(BaseModel):
#     kisi1_ad: str
#     kisi2_ad: str
#     genel_uyum_puani: int
#     pin_uyumu: IliskiDetayModel
#     cakra_uyumu: IliskiDetayModel
#     element_uyumu: IliskiDetayModel
#     yasam_yolu_uyumu: IliskiDetayModel
#     bereket_uyumu: IliskiDetayModel
#     ozet_yorum: str
#     tavsiyeler: List[str]

#     model_config = {
#         "json_schema_extra": {
#             "example": {
#                 "kisi1_ad": "YAHYA HAMZA",
#                 "kisi2_ad": "ELİF NUR",
#                 "genel_uyum_puani": 75,
#                 "pin_uyumu": {
#                     "kategori": "Pin Uyumu",
#                     "kisi1_deger": "4",
#                     "kisi2_deger": "7",
#                     "analiz": "DUYGUSAL MESAFE: İki taraf da zihinde yaşar. Kalp bağı zayıf kalabilir.",
#                     "puan": 60
#                 },
#                 "cakra_uyumu": {
#                     "kategori": "Çakra Uyumu",
#                     "kisi1_deger": "Kalp: 1",
#                     "kisi2_deger": "Kalp: 3",
#                     "analiz": "TAMAMLAYICI DENGE: Biri diğerini açar.",
#                     "puan": 80
#                 },
#                 "element_uyumu": {
#                     "kategori": "Element Uyumu",
#                     "kisi1_deger": "Hava",
#                     "kisi2_deger": "Ateş",
#                     "analiz": "YÜKSEK UYUM (Besleyici)",
#                     "puan": 90
#                 },
#                 "yasam_yolu_uyumu": {
#                     "kategori": "Yaşam Yolu",
#                     "kisi1_deger": "3",
#                     "kisi2_deger": "7",
#                     "analiz": "Yaşam Yolu 3 ve 7.",
#                     "puan": 70
#                 },
#                 "bereket_uyumu": {
#                     "kategori": "Bereket",
#                     "kisi1_deger": "4",
#                     "kisi2_deger": "8",
#                     "analiz": "Sabit Gelir ve Büyük Yatırım Kazancı.",
#                     "puan": 85
#                 },
#                 "ozet_yorum": "Genel Uyum: %75. DUYGUSAL MESAFE: İki taraf da zihinde yaşar. Kalp bağı zayıf kalabilir. TAMAMLAYICI DENGE: Biri diğerini açar.",
#                 "tavsiyeler": [
#                     "Birbirinizi dinleyin.",
#                     "Farklılıklara saygı duyun."
#                 ]
#             }
#         }
#     }


from pydantic import BaseModel
from typing import List, Dict, Optional, Any

# --- ALT MODELLER (Tüm Dersler İçin Gerekli Parçalar) ---
class CakraDetayModel(BaseModel):
    cakra: str
    adet: int
    durum: str
    gezegen: str
    element: str
    nefes_mertebesi: str
    analiz: str

class YasamYoluDetayModel(BaseModel):
    baslik: str
    element: str
    anahtar: str
    guclu: str
    zayif: str
    kader: str

class PinDetayModel(BaseModel):
    arketip: str
    guclu_yon: str
    golge_yon: str
    cakra: str

class IliskiDetayModel(BaseModel):
    kategori: str
    kisi1_deger: str
    kisi2_deger: str
    analiz: str
    puan: int

class BereketDetayModel(BaseModel):
    baslik: str
    para_yolu: str
    risk: str
    para_dongusu: str

class BereketSonucModel(BaseModel):
    esas_bereket_sayisi: int
    esas_bereket_detay: BereketDetayModel
    dongu_bereket_sayisi: int
    dongu_bereket_detay: BereketDetayModel
    finansal_yorum: str

class DonusumYiliModel(BaseModel):
    yil: int
    ana_ritim_sayisi: int
    ana_tema: str
    pin_etkisi_sayisi: int
    baskin_cakra_etkisi_sayisi: int
    yil_yorumu: str

class ElementDetayModel(BaseModel):
    baskin_element: str
    mizac_tipi: str
    element_puanlari: Dict[str, int]
    mizac_yorumu: str
    eksik_element_uyarisi: str

class EsmaSureDetayModel(BaseModel):
    kader_esmasi: str
    isim_esmasi: str
    denge_esmasi: str
    onerilen_sureler: List[str]
    alan_koruma_tavsiyesi: str

class EnerjiMimariModel(BaseModel):
    yapisal_esma: str
    dengeleyici_esma: str
    guc_esmasi: str
    gunluk_uygulama_rutini: List[str]

class MizacYasamTarziModel(BaseModel):
    calisma_tarzi: str
    beslenme_onerisi: str
    iliski_tarzi: str
    para_yonetimi: str
    spirituel_yol: str

class OperasyonelAnalizModel(BaseModel):
    aktivasyon_gunu: str
    kader_alani: str
    aktif_cakra: str
    aciklama: str

class HarfAnaliziModel(BaseModel):
    frekans_dagilimi: Dict[str, int]
    baskin_frekans: str
    frekans_yorumu: str
    mahal_dagilimi: Dict[str, int]
    baskin_mahal: str
    mahal_yorumu: str

class FrekansAnaliziModel(BaseModel):
    tespit_edilen_durum: str
    dusunce_yapisi_analizi: str
    frekans_yukseltme_reçetesi: str

class AlanAktivasyonuModel(BaseModel):
    aktif_sayilar: List[int]
    aktif_alanlar: List[str]
    yil_elementi: str
    yil_etkisi_yorumu: str
    aktivasyon_tavsiyesi: str

class ElementAlanDetayModel(BaseModel):
    baskin_alan: str
    yil_mudahalesi: str
    catisma_durumu: str
    kilitli_alanlar: List[str]
    analiz_sonucu: str

class GunAnaliziModel(BaseModel):
    gunun_tarihi: str
    gun_sayisi: int
    aktif_cakra: str
    gunun_temasi: str
    risk_uyarisi: str
    kisi_gun_uyumu: str

class RefleksAnaliziModel(BaseModel):
    ilk_tepki: str
    bilincalti_sorusu: str
    sinir_sistemi_merkezi: str
    kacis_alani: str
    altin_kural: str

class EnerjiUygulamaModel(BaseModel):
    temel_protokol: List[Dict[str, str]]
    kisisel_odak: str
    yasaklar: List[str]
    dogru_uygulama_belirtileri: str

# --- GİRİŞ MODELLERİ ---
class KisiBilgisi(BaseModel):
    isim: str
    soyisim: str
    anne_adi: str
    dogum_gunu: int
    dogum_ayi: int
    dogum_yili: int

class AnalizIstegi(BaseModel):
    isim: str
    soyisim: str
    anne_adi: str
    dogum_gunu: int
    dogum_ayi: int
    dogum_yili: int
    mevcut_yil: int = 2026
    mevcut_gun: Optional[int] = None
    mevcut_ay: Optional[int] = None

class IliskiAnaliziIstegi(BaseModel):
    kisi1: KisiBilgisi
    kisi2: KisiBilgisi
    mevcut_yil: int = 2026

# --- RAPORLAMA BÖLÜMLERİ (YENİ SİSTEM) ---
class Bolum1_Kimlik(BaseModel):
    baslik: str = "KİMLİK ANALİZİ: SEN KİMSİN?"
    ruhsal_arketip: str  
    yasam_amaci: str     
    mizac_yapisi: str    
    iletisim_tarzi: str  

class Bolum2_Tespit(BaseModel):
    baslik: str = "DURUM TESPİTİ: ENERJİN NEREDE TIKANIYOR?"
    baskin_enerji: str   
    zayif_halka: str     
    bilincalti_refleksi: str 
    frekans_durumu: str  

class Bolum3_Gelecek(BaseModel):
    baslik: str = "KADER VE ZAMANLAMA: SENİ NE BEKLİYOR?"
    bu_yilin_temasi: str 
    para_potansiyeli: str 
    operasyonel_gun: str  
    yil_ile_uyum: str    

class Bolum4_Recete(BaseModel):
    baslik: str = "EYLEM PLANI: NE YAPMALISIN?"
    sabah_rutini: str    
    aksam_rutini: str    
    okunacak_sureler: str
    beslenme_tavsiyesi: str
    yasakli_davranislar: str

# --- ANA ÇIKTI MODELLERİ ---

# 1. ESKİ/TEKNİK MODEL (HATA ALMAMAK İÇİN GERİ EKLENDİ)
class AnalizSonucu(BaseModel):
    tam_isim: str
    pin_kodu: int
    pin_arketipler: PinDetayModel
    cakra_tablosu: Dict[str, int]
    cakra_detaylari: List[CakraDetayModel]
    baskin_element: str
    baskin_gezegen: str
    yasam_yolu_sayisi: int
    yasam_yolu_detay: YasamYoluDetayModel
    ozel_kombinasyon: str
    para_analizi: BereketSonucModel
    donusum_yili_analizi: DonusumYiliModel
    element_mizac_analizi: ElementDetayModel
    esma_sure_analizi: EsmaSureDetayModel
    enerji_mimarisi: EnerjiMimariModel
    mizac_yasam_tarzi: MizacYasamTarziModel
    operasyonel_analiz: OperasyonelAnalizModel
    harf_analizi: HarfAnaliziModel
    frekans_analizi: FrekansAnaliziModel
    alan_aktivasyonu_analizi: AlanAktivasyonuModel
    element_alan_analizi: ElementAlanDetayModel
    gun_analizi: GunAnaliziModel
    refleks_analizi: RefleksAnaliziModel
    enerji_uygulama_plani: EnerjiUygulamaModel
    yorumlar: List[str]

class IliskiAnaliziSonucu(BaseModel):
    kisi1_ad: str
    kisi2_ad: str
    genel_uyum_puani: int
    pin_uyumu: IliskiDetayModel
    cakra_uyumu: IliskiDetayModel
    element_uyumu: IliskiDetayModel
    yasam_yolu_uyumu: IliskiDetayModel
    bereket_uyumu: IliskiDetayModel
    ozet_yorum: str
    tavsiyeler: List[str]

    model_config = {
        "json_schema_extra": {
            "example": {
                "kisi1_ad": "KİŞİ 1",
                "kisi2_ad": "KİŞİ 2",
                "genel_uyum_puani": 85,
                "pin_uyumu": {"kategori": "Pin", "kisi1_deger": "4", "kisi2_deger": "2", "analiz": "...", "puan": 90},
                "cakra_uyumu": {"kategori": "Çakra", "kisi1_deger": "...", "kisi2_deger": "...", "analiz": "...", "puan": 90},
                "element_uyumu": {"kategori": "Element", "kisi1_deger": "...", "kisi2_deger": "...", "analiz": "...", "puan": 90},
                "yasam_yolu_uyumu": {"kategori": "Yaşam Yolu", "kisi1_deger": "...", "kisi2_deger": "...", "analiz": "...", "puan": 80},
                "bereket_uyumu": {"kategori": "Bereket", "kisi1_deger": "...", "kisi2_deger": "...", "analiz": "...", "puan": 85},
                "ozet_yorum": "...",
                "tavsiyeler": ["..."]
            }
        }
    }

# 2. YENİ HİKAYELEŞTİRİLMİŞ RAPOR MODELİ
class AnalizRaporu(BaseModel):
    danisan_bilgisi: str
    bolum_1_kimlik: Bolum1_Kimlik
    bolum_2_tespit: Bolum2_Tespit
    bolum_3_gelecek: Bolum3_Gelecek
    bolum_4_recete: Bolum4_Recete

    model_config = {
        "json_schema_extra": {
            "example": {
                "danisan_bilgisi": "YAHYA HAMZA GÜL (09.08.2002) - Analiz Tarihi: 15.01.2026",
                "bolum_1_kimlik": {
                    "baslik": "KİMLİK ANALİZİ: SEN KİMSİN?",
                    "ruhsal_arketip": "Siz bir 'Sistem Kurucususunuz' (Pin 4). Kaos içinde düzen yaratmak ve somut yapılar inşa etmek için buradasınız.",
                    "yasam_amaci": "Hayat yolunuz 'İfade ve Yaratım' (3) üzerine kurulu. Sahne ışığı, konuşma ve insanlara ilham verme potansiyeliniz var.",
                    "mizac_yapisi": "Baskın elementiniz HAVA. Bu sizi 'Aklî Mizaç' yapar. Hızlı düşünen, stratejik ve analitik bir zekaya sahipsiniz.",
                    "iletisim_tarzi": "Harfleriniz çoğunlukla 'Gırtlak ve Dil Ucu' bölgesinden çıkıyor. Bu, sözlerinizin kaderi etkileme gücünün çok yüksek olduğunu gösterir."
                },
                "bolum_2_tespit": {
                    "baslik": "DURUM TESPİTİ: ENERJİN NEREDE TIKANIYOR?",
                    "baskin_enerji": "Zihin ve İletişim (Hava) enerjiniz çok yüksek. Sürekli yeni fikirler üretiyorsunuz.",
                    "zayif_halka": "DİKKAT: TOPRAK elementiniz eksik veya zayıf. Bu durum; fikirlerinizi paraya çevirmekte zorlanmanıza, maymun iştahlılığa ve başladığınız işi bitirememeye sebep olabilir.",
                    "bilincalti_refleksi": "Stres anında 'Konuşarak ve Fikir Üreterek' tepki veriyorsunuz (Sanguin).",
                    "frekans_durumu": "Şu an 'Zihin Kaosu' frekansındasınız. Çok düşünüyorsunuz ama eyleme geçmekte zorlanıyorsunuz."
                },
                "bolum_3_gelecek": {
                    "baslik": "KADER VE ZAMANLAMA: SENİ NE BEKLİYOR?",
                    "bu_yilin_temasi": "2026 sizin için 'BİTİŞ VE TEMİZLİK' (9) yılıdır. Size hizmet etmeyen insanları ve alışkanlıkları hayatınızdan çıkaracağınız bir dönem.",
                    "para_potansiyeli": "Kaderinizde 'Büyük Yatırım ve Güç' (8) bereketi var. Ancak bunu aktif etmek için sabırlı olmalısınız.",
                    "operasyonel_gun": "Haftanın en güçlü günü: PERŞEMBE. Önemli imzaları ve başlangıçları bu gün yapmalısınız.",
                    "yil_ile_uyum": "KRİZ UYARISI: Sizin doğanız (Hava) ile bu yılın enerjisi (Toprak) çatışıyor. Zihniniz hız istiyor ama hayat sizi yavaşlatıyor."
                },
                "bolum_4_recete": {
                    "baslik": "EYLEM PLANI: NE YAPMALISIN?",
                    "sabah_rutini": "Güne 'Ya Melik' esmasıyla (33 kere) ve topraklanma egzersizi (çıplak ayakla yere basma) ile başlayın.",
                    "aksam_rutini": "Günü kapatırken 'Ya Fettah' esması çekin ve zihni boşaltmak için nefes egzersizi yapın.",
                    "okunacak_sureler": "Zihinsel netlik için 'İnşirah', güç ve koruma için 'Fatiha' suresi okuyun.",
                    "beslenme_tavsiyesi": "Hava mizacını dengelemek için sıcak ve ıslak gıdalar (Et suyu, zencefil, bal) tüketin. Kuru gıdalardan kaçının.",
                    "yasakli_davranislar": "Öfkeliyken veya çok açken asla önemli bir karar vermeyin veya enerji çalışması yapmayın."
                }
            }
        }
    }