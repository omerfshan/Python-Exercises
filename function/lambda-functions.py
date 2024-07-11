
multiply=(lambda a,b,c:a*b*c)
print(multiply(1,2,3))
reverse=lambda s:s[::-1]
print(reverse("aliduran"))

def myfunc(n):
    return lambda a: a*n

multiply2=myfunc(4)
print(multiply2(10))
multiply3=myfunc(5)(5)