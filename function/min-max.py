sayilar=[1,5,7,45,25,89]
harfler=["a","v","h","s"]
isimler=["ahmet","ismail","ada","sena",]
sonuc=min(isimler)
sonuc=min(harfler)
sonuc=min(harfler)
sonuc=max(isimler)
sonuc=max(harfler)
sonuc=max(harfler)


sonuc=max(isimler,key=lambda a: len(a))
sonuc=min(isimler,key=lambda a: len(a))

urunler = [
    {"title":"iphone x","price":5000},
    {"title":"iphone xr","price":6000},
    {"title":"iphone 11","price":7000}
]

sonuc=max(urunler,key=lambda a: a["price"])
sonuc=max(urunler,key=lambda a: a["price"])["title"]

print(sonuc)