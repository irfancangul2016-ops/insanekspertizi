# def yil_etkisi(kisi_element: dict, yil_element: str):
#     baskin = max(kisi_element, key=kisi_element.get)
#     yorumlar = []

#     if baskin == yil_element:
#         yorumlar.append("Bu yıl ivme yılı. Hızlanırsın.")

#     zit = {
#         "Ateş": "Su",
#         "Su": "Ateş",
#         "Hava": "Toprak",
#         "Toprak": "Hava"
#     }

#     if zit.get(baskin) == yil_element:
#         yorumlar.append("Bu yıl zorlayıcı. Sabır şart.")

#     eksik = [e for e, v in kisi_element.items() if v == 0]
#     if eksik:
#         yorumlar.append(
#             f"Eksik elementler ({', '.join(eksik)}) bilinçli desteklenmeli."
#         )

#     return yorumlar

def yil_etkisi(kisi_element: dict, yil_element: str):
    baskin = max(kisi_element, key=kisi_element.get)
    yorumlar = []

    if baskin == yil_element:
        yorumlar.append("Bu yıl ivme yılı. Hızlanırsın.")

    zit = {
        "Ateş": "Su",
        "Su": "Ateş",
        "Hava": "Toprak",
        "Toprak": "Hava"
    }

    if zit.get(baskin) == yil_element:
        yorumlar.append("Bu yıl zorlayıcı. Sabır şart.")

    eksik = [e for e, v in kisi_element.items() if v == 0]
    if eksik:
        yorumlar.append(
            f"Eksik elementler ({', '.join(eksik)}) bilinçli desteklenmeli."
        )

    return yorumlar
