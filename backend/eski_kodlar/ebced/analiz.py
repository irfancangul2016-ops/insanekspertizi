
def ebced_analizi(deger: int) -> dict:
    return {
        "ebced": deger,
        "tekil": deger % 9 or 9,
        "element": ["Ateş","Toprak","Hava","Su"][deger % 4],
        "yon": "Yapıcı" if deger % 2 == 0 else "Dönüştürücü"
    }


def pin_kodu_uret(isim_ebced: int, tarih: str) -> dict:
    tarih_sayi = sum(int(x) for x in tarih if x.isdigit())
    toplam = isim_ebced + tarih_sayi
    pin = [int(x) for x in str(toplam)]

    return {
        "pin_ana": toplam,
        "pin_dizilim": pin
    }

from .yorumlar import YORUMLAR

def yorum_uret(element_haritasi: dict) -> list:
    aktif_yorumlar = []

    for y in YORUMLAR:
        if y["kosul"](element_haritasi):
            aktif_yorumlar.append(y["metin"])

    return aktif_yorumlar
