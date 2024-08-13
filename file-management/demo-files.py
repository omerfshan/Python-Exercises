def dosya_kopyala(dosya_ismi,yeni_dosya_ismi):
    with open(dosya_ismi,"r",encoding="utf-8") as file:
        content=file.read()
    with open(yeni_dosya_ismi,"w",encoding="utf-8") as file:
        file.write(content)

# dosya_kopyala("file-management\markalar.txt","file-management\-new-markalar.txt")

def terst_cevir(dosya_ismi,yeni_dosya_ismi):
   with open(dosya_ismi, "r", encoding="utf-8") as file:
    content = file.read()
    content = content[::-1].strip()  # İçeriği ters çevirir ve başındaki/sonundaki boşlukları temizler

   with open(yeni_dosya_ismi, "w", encoding="utf-8") as file:
     file.write(content)
     
# terst_cevir("file-management\markalar.txt","file-management\-new-markalar.txt")

def bilgilendir(dosya_ismi):
   with open(dosya_ismi,"r",encoding="utf-8") as file:
      content=file.readlines()
    #   satir sati ilerletir
      dictContent={
         "satir-sayisi":len(content),
         "kelime-sayisi":sum(len(row.split(' ')) for row in content),
         "karekter-sayisi":sum(len(row) for row in content),

      }
   return dictContent

print(bilgilendir("file-management\markalar.txt"))