a,b,c=2,5,10

x=int(input("x:"))
y=int(input("y:"))
sonuc=(x*y)-(a+b+c)
sonuc=c//b
sonuc=(a+b+c)%3
sonuc=b**a
sayilar=1,5,7,10,3
a,*b,c=sayilar
sonuc=c**3

for x in b:
    z=0
    z+=x
    
print(z)
print(sonuc)
