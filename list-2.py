diller=["python","c#","java","javaScript"]
sonuc =diller
sonuc=diller[0:2]
sonuc=diller[-4:-2]
diller[0]="html"
sonuc=len(diller)
sonuc=diller+["angular","python"]

if "python" in diller:
    print("python diller listesinde var")
else:
    print("python diller listesinde yok")
for x in diller:
    print(x)
del diller[2]# listeden eleman silme



print(sonuc)
