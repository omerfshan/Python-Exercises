class Product:
    def __init__(self,name,price,description):
        self.name=name
        self.description=description
        if  price>=0:
         self._price=price
        else:
           raise ValueError("price negatif deger olamaz")
    @property
    def price(self):
       return self._price
    @price.setter
    def price(self,value):
        if  value>=0:
         self._price=value
        else:
           raise ValueError("price negatif deger olamaz")
    @property
    def short_description(self):
       return f"{self.description[:10]}"
    


p=Product("iphone 12",9000,"iphon 12 apple tarafından üretilmiştir")
print(p.price)
# p.price=-9000
print(p.price)
