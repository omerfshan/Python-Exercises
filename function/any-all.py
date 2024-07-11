sonuc=all([True,False,True])
sonuc=all([True,True,True])
sonuc=any([True,False,True])

# And => True and True => True => All()
# Or  => True or False => True => Any()
sayilar=[1,2,3,4,5,6,7,8,9,10]
sonuc=any([bool(sayi) for sayi in sayilar])
sonuc=all([bool(sayi) for sayi in sayilar])
sonuc=all([bool(sayi) for sayi in sayilar if sayi%2==0])
sonuc=all([sayi%2==0 for sayi in sayilar])
sonuc=any([sayi%2==0 for sayi in sayilar])

kisiler=["ali","ahmet","çınar"]
sonuc=any( [kisi[0]=="a" for kisi in kisiler])
sonuc=all( [kisi for kisi in kisiler if kisi[0]=="a"])

print(sonuc)