def en_onemli_yorumlar(yorumlar, limit=3):
    yorumlar = sorted(yorumlar, key=lambda x: x[0], reverse=True)
    return [y[1] for y in yorumlar[:limit]]
from ebced.yorum_motoru import element_yorumlari
from ebced.yil_etkisi import yil_etkisi

def tam_analiz(kisi_element: dict, yil_element: str):
    sonuc = {}

    # 1️⃣ Kişilik yorumları
    sonuc["kisisel_yorumlar"] = element_yorumlari(kisi_element)

    # 2️⃣ Yıl etkileri
    sonuc["yil_yorumlari"] = yil_etkisi(kisi_element, yil_element)

    # 3️⃣ Birleşik mesaj
    if "Bu yıl ivme yılı. Hızlanırsın." in sonuc["yil_yorumlari"]:
        sonuc["birlesik_mesaj"] = "Doğru hamle yapılırsa bu yıl sıçrama getirir."
    else:
        sonuc["birlesik_mesaj"] = "Bu yıl iç disiplin belirleyici olacak."

    return sonuc
