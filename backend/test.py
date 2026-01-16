from ebced.isim_analizi import isim_toplam, tek_haneye_indir

sonuc = isim_toplam("BUKET")

print("Toplam:", sonuc["toplam"])
print("Detay:", sonuc["detay"])
print("Tek Hane:", tek_haneye_indir(sonuc["toplam"]))