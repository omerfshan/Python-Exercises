class Products:
    def __init__(self,name,price,isActivate):
        self.name=name
        self.price=price
        self.isActivate=isActivate
        print("ürün oluştu")
p1=Products("samsung S20",12000,True)
p2=Products("Iphone12",25000,False)

print(p1.name,p1.price,p1.isActivate)
print(p2.name,p2.price,p2.isActivate)