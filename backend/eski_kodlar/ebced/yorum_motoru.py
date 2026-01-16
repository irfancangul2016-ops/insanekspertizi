import random

def element_yorumlari(kisi_element: dict):
    yorumlar = []

    baskin = max(kisi_element, key=kisi_element.get)

    varyasyonlar = {
        "Hava": [
            "Hızlı düşünürsün ama kararlar gecikebilir.",
            "Zihnin çok hızlı çalışır fakat netleşme zaman alır.",
            "Analitik gücün yüksek, karar anı zorlayabilir."
        ],
        "Ateş": [
            "Harekete geçme gücün yüksek ama sabır zorlanır.",
            "İnisiyatif alırsın fakat acele riski vardır.",
            "Enerjin yüksek, kontrol edilmezse dağılabilir."
        ],
        "Toprak": [
            "Düzen kurarsın ama esneklik düşebilir.",
            "Planlama gücün yüksek, değişime direnç oluşabilir.",
            "Sistemli ilerlersin fakat katılaşma riski vardır."
        ],
        "Su": [
            "Sezgilerin güçlü fakat duygusal yük artabilir.",
            "Hissiyatın derin, sınırlar bulanıklaşabilir.",
            "Empati gücün yüksek ama içe çekilme görülebilir."
        ]
    }

    # Baskın element → 1 kritik yorum
    yorumlar.append((3, random.choice(varyasyonlar[baskin])))

    # Eksik elementler
    if kisi_element.get("Toprak", 0) == 0:
        yorumlar.append((2, random.choice([
            "Toprak enerjisi eklenmezse dağılma yaşarsın.",
            "Düzenleyici etki olmazsa istikrar zorlaşır."
        ])))

    if kisi_element.get("Su", 0) == 0:
        yorumlar.append((2, random.choice([
            "Su eksikliği ilişkilerde mesafe yaratır.",
            "Duygusal bağları sürdürmek zorlaşabilir."
        ])))

    if kisi_element.get("Ateş", 0) == 0:
        yorumlar.append((1, random.choice([
            "Motivasyon düşüklüğü görülebilir.",
            "Harekete geçmek için dış tetik gerekir."
        ])))

    if kisi_element.get("Hava", 0) == 0:
        yorumlar.append((1, random.choice([
            "İfade zorluğu oluşabilir.",
            "Düşünceler içte birikebilir."
        ])))

    return yorumlar