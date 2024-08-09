def sayi_uret():
    sayi=0
    while True:
        yield sayi
        sayi+=1

generator=sayi_uret()

# for i in generator:
    # print(i)

def fib_gen(max):
    a,b=0,1
    count=0
    while count<max:
        a,b=a,a+b
        yield b
        count +=1

# for i in fib_gen(10000000):
#   print(i)

# import sys

# liste = [i*2 for i in range(10000)]
# print(sys.getsizeof(liste))

# gen = (i**2 for i in range(10000))
# print(sys.getsizeof(gen))

import time

list_start_time = time.time()
print([i**2 for i in range(10000)])
list_stop = time.time() - list_start_time

gen_start_time = time.time()
print((i**2 for i in range(10000)))
gen_stop = time.time() - gen_start_time

print(list_stop, gen_stop)