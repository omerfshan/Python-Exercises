class newDict(dict):
    def __repr__(self):
        print("repr metodundan mesaj var")
        return super().__repr__()
    def __missing__(self,key):
        print("olmayan key bilgisi")
    def __getitem__(self, key):
        print("bir eleman cağrıyorsunuz")
        return super().__getitem__(key)
    def __setitem__(self,key,value):
        print("listeye eleman ekliyoruz")
        super().__setitem__(key,value)
    def __contains__(self, key):
        print("listeden eleman arayamazsınız")  
        return False

data=newDict({"first":"şenol","last":"güneş"})
print(data["first"])
data["age"]
data["first"]="galip"
print(data)