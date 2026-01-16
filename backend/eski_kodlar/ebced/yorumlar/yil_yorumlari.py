def yil_yorumlari(baskin, yil):
    yorumlar = []

    if baskin == yil:
        yorumlar.append("Bu yıl ivme yılı. Hızlanırsın, fırsatlar artar.")

    zit = {
        "Ateş": "Su",
        "Su": "Ateş",
        "Hava": "Toprak",
        "Toprak": "Hava"
    }

    if zit.get(baskin) == yil:
        yorumlar.append("Bu yıl zorlayıcı. Sabır, iç denge ve planlama şart.")

    return yorumlar