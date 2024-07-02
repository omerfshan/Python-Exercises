msg = "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit"

# sonuc = msg.upper()
# sonuc = msg.lower()
# sonuc = msg.title()
# sonuc = msg.capitalize()

# sonuc = "abc".islower()
# sonuc = "    abc ".strip() boşluk karakterleri alır
# sonuc = msg.split() kelimeleri dizi elemanı yapar
# sonuc = msg.split('.') nokta karakterleri ile ayır

# sonuc = "-".join(sonuc) elamanları birleştirir elamanları - ile ayırır

# index = msg.index('Hoş') kacıncı index
# sonuc = msg.startswith('A') a ile mi başlıyor
# sonuc = msg.endswith('n') n ile mi bitiyor
sonuc = msg.replace('porro','lorem') # replace ile porroyu lorem ile değiştir
sonuc = msg.lower().replace(' ','-').replace('ş','s').replace('.','').replace('ı','i')


print(sonuc)