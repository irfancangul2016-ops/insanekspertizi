
from fastapi import APIRouter
from analiz.yil_etkisi import yil_etkisi

router = APIRouter()


@router.post("/yil-analizi")
def yil_analizi():
    # ŞİMDİLİK SABİT VERİ (sonra kullanıcıdan gelecek)
    kisi_element = {
        "Ateş": 2,
        "Su": 0,
        "Hava": 3,
        "Toprak": 1
    }

    yil_element = "Ateş"

    yorumlar = yil_etkisi(kisi_element, yil_element)

    return {
        "element_dagilimi": kisi_element,
        "yil_yorumlari": yorumlar
    }
