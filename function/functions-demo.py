# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 
def write(numb,sentences):
    i=0
    while(i<numb):
        print(sentences)
        i+=1

write(10,"aaa")
# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
def rectangle(a,b,selection):
   if(selection=="alan"):
      return a*b
   elif(selection=="cevre"):
     return 2*a+2*b
   else:
      return 0

print(rectangle(20,30,"alan"))
print(rectangle(20,30,"cevre"))
#3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
