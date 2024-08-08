# iterable
# iterator
sayilar=[1,2,3,4,5]
s="hello" 


def my_for(iterable,func):
  Iterator=iter(iterable)
  while True:
    try:
        sayi=next(Iterator)
        func(sayi)
    except StopIteration :
        break

def kareal(x):
   print(x*x)

my_for(sayilar,print)
my_for(s,print)
my_for(sayilar,kareal)