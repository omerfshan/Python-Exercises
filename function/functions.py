# def greeting():
#     print("hello")
def phrases():
    print("lorem ipsum.")

phrases()

def sum(a,b):
    return a+b

print(sum(12,34))


def year():
    import datetime
    return datetime.datetime.now().year

def clock():
    import datetime
    return datetime.datetime.now().hour

def greeting():
    if(clock()<12):
        print("good morning")
    elif(clock()==12):
        print("good afternoon")
    else:
        print("good night")

def yasHesapla():
    return year()-1999

greeting()
print(yasHesapla())