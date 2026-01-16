# isim_analizi.py
# İnsanekspertizi – İsim Analizi Motoru

# from ebced.harf_degerleri import EBCED, LATIN_MAP

# def latin_to_arabic(isim):
#     sonuc = []
#     for harf in isim.upper():
#         if harf in LATIN_MAP:
#             sonuc.append(LATIN_MAP[harf])
#     return sonuc


# def isim_toplam(isim):
#     arapca_harfler = latin_to_arabic(isim)
#     toplam = 0
#     detay = []

#     for harf in arapca_harfler:
#         deger = EBCED.get(harf, 0)
#         toplam += deger
#         detay.append((harf, deger))

#     return {
#         "toplam": toplam,
#         "detay": detay,
#         "harf_sayisi": len(arapca_harfler)
#     }




# def tek_haneye_indir(sayi):
#     while sayi > 9:
#         sayi = sum(int(x) for x in str(sayi))
#     return sayi

# def ebced_hesapla(metin):
#     harf_map = {
#         "A": 1, "B": 2, "C": 3, "D": 4, "E": 5,
#         "F": 80, "G": 3, "H": 5, "I": 10, "J": 10,
#         "K": 20, "L": 30, "M": 40, "N": 50,
#         "O": 70, "P": 80, "Q": 100, "R": 200,
#         "S": 300, "T": 400, "U": 6, "V": 6,
#         "W": 6, "X": 60, "Y": 10, "Z": 7
#     }

#     toplam = 0
#     for harf in metin.upper():
#         if harf in harf_map:
#             toplam += harf_map[harf]

#     return toplam


# isim = input("İsim: ")
# soyisim = input("Soyisim: ")

# isim_ebced = ebced_hesapla(isim)
# soyisim_ebced = ebced_hesapla(soyisim)

# toplam_ebced = isim_ebced + soyisim_ebced

# print(f"İsim Ebced: {isim_ebced}")
# print(f"Soyisim Ebced: {soyisim_ebced}")
# print(f"Toplam Ebced: {toplam_ebced}")


def ebced_hesapla(metin: str) -> int:
    harf_map = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5,
        "F": 80, "G": 3, "H": 5, "I": 10, "J": 10,
        "K": 20, "L": 30, "M": 40, "N": 50,
        "O": 70, "P": 80, "Q": 100, "R": 200,
        "S": 300, "T": 400, "U": 6, "V": 6,
        "W": 6, "X": 60, "Y": 10, "Z": 7
    }

    toplam = 0
    for harf in metin.upper():
        if harf in harf_map:
            toplam += harf_map[harf]

    return toplam


def isim_soyisim_ebced(isim: str, soyisim: str) -> dict:
    isim_deger = ebced_hesapla(isim)
    soyisim_deger = ebced_hesapla(soyisim)

    return {
        "isim": isim,
        "soyisim": soyisim,
        "isim_ebced": isim_deger,
        "soyisim_ebced": soyisim_deger,
        "toplam_ebced": isim_deger + soyisim_deger
    }