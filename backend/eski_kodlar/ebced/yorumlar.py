YORUMLAR = [
    {
        "kosul": lambda e: e["Hava"] >= 4 and e["Toprak"] <= 1,
        "metin": "Hızlı düşünürsün ama karar vermekte zorlanırsın."
    },
    {
        "kosul": lambda e: e["Su"] == 0,
        "metin": "Duygusal bağ kurmak senin için doğal değildir, bilinçli olarak öğrenilmelidir."
    },
    {
        "kosul": lambda e: e["Toprak"] <= 1,
        "metin": "Hayatında düzen ve ritim kurulmazsa dağılma yaşarsın."
    }
]
