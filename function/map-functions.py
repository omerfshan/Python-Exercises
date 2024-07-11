sayilar=[1,2,3,4,5]
isimler=["ali","ayşe","deniz","emel","çınar"]
str_sayilar=["1","2","3","4","7","9"]
users=[
{"ad":"ali","soyad":"yılmaz"},
{"ad":"ahmet","soyad":"yılmaz"}
]
sonuc=list(map(lambda sayi :sayi**2,sayilar))
sonuc=list(map(int,str_sayilar))
sonuc=list(map(str,sayilar))
sonuc=list(map(str.capitalize,isimler))
sonuc=list(map(lambda x:x["ad"],users))

print(sonuc)