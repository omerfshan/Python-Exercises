# [expression for item in list]
liste=[10,4,7,9,70]
sayilar=[]
liste2=[]
for i in range(10):
    sayilar.append(i)

sayilar=[i**2 for i in range(10)]
liste2=[i for  i in liste]
isim ="Salih"
sonuc=[c.upper() for c in isim]
# [expression for item in list if koşul]
sonuc=[sayi for sayi in sayilar if sayi%2==0]
sonuc=[sayi if sayi%2==0 else "tek sayi " for sayi in sayilar]
sonuc=[(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(sonuc)
