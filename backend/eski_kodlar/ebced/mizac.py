def element_bul(ebced: int, pin: list) -> dict:
    element_map = {
        "Toprak": 0,
        "Ateş": 0,
        "Su": 0,
        "Hava": 0
    }

    # Ebced etkisi
    mod = ebced % 4
    element_map[["Toprak","Ateş","Su","Hava"][mod]] += 2

    # Pin etkisi
    for s in pin:
        if s <= 4:
            element_map["Toprak"] += 1
        elif s <= 7:
            element_map["Hava"] += 1
        else:
            element_map["Ateş"] += 1

    # Tekil
    tekil = ebced % 9 or 9
    if tekil <= 2:
        element_map["Ateş"] += 1
    elif tekil <= 4:
        element_map["Toprak"] += 1
    elif tekil <= 6:
        element_map["Hava"] += 1
    else:
        element_map["Su"] += 1

    return element_map