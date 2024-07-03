sayilar=[1,5,5,9,3,45]
harfler=['a','b','e','s','a','y']
sonuc=min(sayilar)
sonuc=max(harfler)   

sayilar.append(10)# append listeye elaman dizi ekleme
sayilar.insert(3,5)
sayilar.insert(-1,60)# listeye index ile ekleme
sayilar.insert(len(sayilar),12)
sayilar.pop()
sayilar.pop(-1)
sayilar.remove(60)
sayilar.sort() # sırala

harfler.reverse()# tersten sırala
harfler.clear() # listeyi temizler
print(sayilar.count(5))# kac tane 5 var
sayilar.index(5)# 5 kacıncı indexte
print(sonuc)


for x in sayilar:
    print(x)