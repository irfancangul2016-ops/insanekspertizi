def yil_etkisi(kisi_element: dict, yil_element: str):
    baskin = max(kisi_element, key=kisi_element.get)
    yorumlar = []

    if baskin == yil_element:
        yorumlar.append("Bu yıl ivme yılı. Hızlanırsın.")

    zıt = {
        "Ateş": "Su",
        "Su": "Ateş",
        "Hava": "Toprak",
        "Toprak": "Hava"
    }

    if zıt.get(baskin) == yil_element:
        yorumlar.append("Bu yıl zorlayıcı. Sabır şart.")

    eksik = [e for e, v in kisi_element.items() if v == 0]
    if eksik:
        yorumlar.append(
            f"Eksik elementler ({', '.join(eksik)}) bilinçli desteklenmeli."
        )

    return yorumlar

def yil_detayli_etkisi(kisi_element: dict, yil_element: str):
    yorumlar = []

    baskin = max(kisi_element, key=kisi_element.get)
    oran = kisi_element[baskin]

    if baskin == yil_element:
        if oran >= 3:
            yorumlar.append("Bu yıl güçlü destek var. Hızlanma ve görünürlük artar.")
        else:
            yorumlar.append("Bu yıl destek var ama kararsızlık ivmeyi kesebilir.")

    zıt = {
        "Ateş": "Su",
        "Su": "Ateş",
        "Hava": "Toprak",
        "Toprak": "Hava"
    }

    if zıt.get(baskin) == yil_element:
        if oran >= 3:
            yorumlar.append("Bu yıl sert sınavlar getirir. Direnç kazanırsın.")
        else:
            yorumlar.append("Bu yıl yorar. Acele karar kaybettirir.")

    if not yorumlar:
        yorumlar.append("Bu yıl nötr. Büyük kırılma yok, hazırlık yılı.")

    return yorumlar
