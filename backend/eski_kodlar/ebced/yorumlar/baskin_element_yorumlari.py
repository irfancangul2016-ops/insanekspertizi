def baskin_element_yorumlari(baskin_element: str):
    yorumlar = {
        "Ateş": [
            "Hızlı düşünürsün ama sabırsızlık karar kaliteni düşürür.",
            "Reaksiyonun güçlü, kontrolün zayıf."
        ],
        "Su": [
            "Duyguları derin yaşarsın ama içine atarsın.",
            "Herkesi anlarsın, kendini anlatamazsın."
        ],
        "Hava": [
            "Zihnin çok hızlı ama dağınık.",
            "Başladığın işi bitirmekte zorlanırsın."
        ],
        "Toprak": [
            "Ayakların yere basar ama risk almaktan kaçarsın.",
            "Güven arayışı seni yavaşlatır."
        ]
    }

    return yorumlar.get(baskin_element, [])
