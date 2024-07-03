a,b,c=5,10,20
a,b=b,a
a+=5
a-=5
a/=5
a%=5
a**=5
a*=5
a//=5

values=(1,2,3)
a,b,c=values
values2=(1,2,3,4,5)
a,b,*c=values2
print(a,b,c)
