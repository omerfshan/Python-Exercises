def sum(*args):
    print(type(args))
    print(args)
    sonuc=0
    for i in args:
        sonuc+=i
    return sonuc
print(sum(10,20,40))
print(sum(30,20,30,70))