def urun_ekle(ad,fiyat):
    with open("file-management/urunler.txt","a",encoding="utf-8") as file:
        file.write(f"ad:{ad} fiyat:{fiyat} \n")
# urun_ekle("samsung s20",6000)
# urun_ekle("Iphone 13",9000)

def bul_ve_degistir(dosya_ismi,eski_kelime,yeni_kelime):
    with open(dosya_ismi,"r+") as file:
        text=file.read()
        yeni_text=text.replace(eski_kelime,yeni_kelime)
        file.seek(0)
        file.write(yeni_text)
        file.truncate()
bul_ve_degistir("file-management/urunler.txt","6000","0")