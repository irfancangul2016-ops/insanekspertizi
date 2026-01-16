def yapi_yorumlari(kisi_element: dict):
    yorumlar = []

    if kisi_element.get("Hava", 0) > kisi_element.get("Toprak", 0):
        yorumlar.append(
            "Hızlı düşünürsün ama karar aşamasında gecikme yaşarsın."
        )

    if kisi_element.get("Toprak", 0) == 0:
        yorumlar.append(
            "Toprak enerjisi eklenmezse dağılma ve istikrarsızlık yaşanır."
        )

    if kisi_element.get("Su", 0) == 0:
        yorumlar.append(
            "Su eksikliği duygusal ilişkilerde mesafe ve kopukluk yaratır."
        )

    if kisi_element.get("Ateş", 0) > 3:
        yorumlar.append(
            "Ateş fazlalığı sabırsızlık ve ani tepkilere yol açabilir."
        )

    return yorumlar