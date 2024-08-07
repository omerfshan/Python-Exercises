class Film:
    def __init__(self,baslik,yonetmen,sure):
        self.baslik=baslik
        self.yonetmen=yonetmen
        self.sure=sure
    def __str__(self):
       return f"{self.baslik}, {self.yonetmen} tarafından yönetildi"
    def __repr__(self):
        return f"{self.baslik}, {self.yonetmen} tarafından yönetildi"
    def __len__(self):
        return self.sure
    def __del__(self):
       print( f"{self.baslik} silindi")

liste=1,2,3
f =Film("film adı","yonetmen",120)
print(str(liste))
print(len(f))
print(str(f))
del f