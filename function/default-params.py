def greeting(name="user",greet="hello"):
    print(greet+" "+name)

greeting("ali","merhaba")
greeting()

def sum(a,b):
    return a+b
def sub(a,b):
    return a-b

def operation(a,b,fn=sum):
    return fn(a,b)

print(operation(12,3))
print(operation(12,3,sub))