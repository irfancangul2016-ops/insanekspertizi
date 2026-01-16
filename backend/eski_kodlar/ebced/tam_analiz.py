from ebced.isim_analizi import isim_soyisim_ebced
from ebced.element import yil_elementi_hesapla, yil_etkisi
from ebced.yorum_motoru import element_yorumlari


def tam_analiz(isim: str, soyisim: str, yil: int):
    # 1. Ebced
    ebced_sonuc = isim_soyisim_ebced(isim, soyisim)

    kisi_element = ebced_sonuc["element_dagilimi"]
    baskin_element = ebced_sonuc["baskin_element"]

    # 2. Yıl elementi
    yil_element = yil_elementi_hesapla(yil)

    # 3. Yorumlar
    yorumlar = []
    yorumlar += element_yorumlari(kisi_element)
    yorumlar += yil_etkisi(kisi_element, yil_element)

    return {
        "isim_ebced": ebced_sonuc["toplam"],
        "baskin_element": baskin_element,
        "eksik_elementler": [e for e, v in kisi_element.items() if v == 0],
        "yil_element": yil_element,
        "yorumlar": yorumlar
    }
