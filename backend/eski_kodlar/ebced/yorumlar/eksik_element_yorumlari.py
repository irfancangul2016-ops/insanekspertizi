def eksik_element_yorumlari(elementler):
    yorumlar = []

    if elementler.get("Toprak", 0) == 0:
        yorumlar.append(
            "Toprak eksikliği dağılma yaratır. Rutin, beden disiplini ve somut hedef şart."
        )

    if elementler.get("Su", 0) == 0:
        yorumlar.append(
            "Su eksikliği duygusal mesafe oluşturur. Empati ve bağ kurma bilinçli geliştirilmeli."
        )

    return yorumlar

def eksik_element_yorumlari(kisi_element: dict):
    yorumlar = []

    if kisi_element.get("Toprak", 0) == 0:
        yorumlar.append(
            "Toprak eksikliği seni hayattan koparır. Rutin kurmazsan dağınırsın."
        )

    if kisi_element.get("Su", 0) == 0:
        yorumlar.append(
            "Su eksikliği ilişkilerde mesafe yaratır. Duygu göstermek zorundasın."
        )

    if kisi_element.get("Ateş", 0) == 0:
        yorumlar.append(
            "Ateş eksikliği özgüveni düşürür. Kendini geri çekmeye meyillisin."
        )

    if kisi_element.get("Hava", 0) == 0:
        yorumlar.append(
            "Hava eksikliği esnek düşünmeni zorlaştırır. Tek bakış açısına saplanırsın."
        )

    return yorumlar
