def iliski_uyumu(e1: dict, e2: dict) -> dict:
    skor = 0
    yorumlar = []

    def baskin(e):
        return max(e, key=e.get)

    b1 = baskin(e1)
    b2 = baskin(e2)

    if b1 == b2:
        skor += 2
        yorumlar.append("Benzer mizaçtan geliyorsunuz, bu konfor sağlar.")
    
    destek = {
        "Ateş":"Toprak",
        "Hava":"Toprak",
        "Su":"Toprak",
        "Toprak":"Su"
    }

    if destek.get(b1) == b2 or destek.get(b2) == b1:
        skor += 3
        yorumlar.append("Birbirinizi dengeleyen elementleriniz var.")

    zıt = {
        "Ateş":"Su",
        "Su":"Ateş",
        "Hava":"Su",
        "Su":"Hava"
    }

    if zıt.get(b1) == b2:
        skor -= 3
        yorumlar.append("Elementleriniz çatışıyor, emek şart.")

    return {
        "uyum_puani": skor,
        "yorumlar": yorumlar
    }