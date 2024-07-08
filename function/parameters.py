def selamla(isim):
    return "merhaba" +isim

def  toplam(a,b):
    return a+b

sonuc=toplam(20,30)

def YasHesaplama(dogumYili,isim):
    import datetime
    year= datetime.datetime.now().year
    return isim +" "+f"{year-dogumYili}" +" " +"yaşında"
print(YasHesaplama(1999,"ali"))