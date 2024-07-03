x=15
sonuc=(x>5) and (x<15)
sonuc=(x>5) or (x<15)
sonuc=not(x>5)
print(sonuc)

# identity operator:is referans karşılaştırması
z=y=[1,2,3]
r=[1,2,3]
print(z==y)
print(r==z)
print(z is y)
print(r is z)
print(r is not z)
# membership operator: in eleman liste içersinde varmı
a=["apple","banana"]
print("orange" in a)
print("a" not in a)