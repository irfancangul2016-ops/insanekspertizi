def turkce_to_arapca(isim: str) -> str:
    map = {
        "A":"ا","E":"ا","B":"ب","C":"ج","D":"د","F":"ف",
        "G":"ك","H":"ه","I":"ي","İ":"ي","K":"ك","L":"ل",
        "M":"م","N":"ن","O":"و","U":"و","P":"ب","R":"ر",
        "S":"س","Ş":"ش","T":"ت","V":"و","Y":"ي","Z":"ز"
    }

    sonuc = ""
    for harf in isim.upper():
        sonuc += map.get(harf, "")
    return sonuc