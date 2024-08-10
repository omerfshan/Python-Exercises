def usalma(number):
    def inner(power):
        return number**power
    return inner


two=usalma(2)#  return inner 


print(two(2))# return number**power


def yetki_sorgula(page):
    def inner(role):
        if role=="admin":
            return "{0} rolü {1} sayfasına ulaşılabilir".format(role,page)
        else:
             return "{0} rolü {1} sayfasına ulaşamaz".format(role,page)
    return inner


admin=yetki_sorgula("web")
print(admin("user"))

def islem(islem_adi):
    def toplam(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    
    def carpma(*args):
        carpim=1
        for i in args:
            carpim*=i
        return carpim
    if islem_adi=="toplam":
        return toplam
    else:
        return carpma

toplam=islem("toplam")
carpma=islem("carpma")
print(toplam(2,3,5,78,5))
print(carpma(1,2,5,6,8,34))