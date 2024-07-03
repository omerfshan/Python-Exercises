# sets => indekslenemez, sıralanamaz eleman ekleyip çıkarabiliriz

meyveler = { "elma","kiraz","kavun","üzüm" }
sebzeler = { "bezelye","soğan" }

# sonuc = meyveler[0] indekslenemez
sonuc = "elma" in meyveler
meyveler.add("karpuz")
meyveler.update(["vişne","kavun"])
# var olan bilgi eklenmez
sonuc = len(meyveler)
# meyveler.remove("karpuzz") # KeyError
# meyveler.discard("karpuz") siler

# sonuc = meyveler.pop()
# meyveler.clear()

sonuc = meyveler.union(sebzeler)# birleştirir

# for x in meyveler:
#     print(x)

print(sonuc)
