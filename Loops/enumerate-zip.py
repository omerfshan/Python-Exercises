markalalar=["opel","bmw","mercedes"]
obj1=enumerate(markalalar)
print(list(obj1))
for index,value in enumerate(markalalar,1):
    print(f"{index}-{value}")

liste1=[1,2,3,4,5]
liste2=['a','b','c','d','e','f']
liste3=[100,200,300,400,500,700]
# zip farklı liste elamanları birleştirmeye yarar birleşmeyen elemanlar göz ardı edilir
print(list(zip(liste1,liste2,liste3)))