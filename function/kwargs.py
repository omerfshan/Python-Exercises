def displayUser(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    print("\n")

displayUser(username="ardaguler")
displayUser(username="ardaguler",email="info@ardaguler.com")
displayUser(username="ardaguler",email="info@ardaguler.com",country="turkey")

def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,key1="value 1",key2="value 2")
