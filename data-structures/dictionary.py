# key-value sıralanamaz
plakalar= {'kocaeli':41,'istabul':34,'aydın':9}
plakalar["rize"]=53
plakalar["izmir"]=70
plakalar["izmir"]=35 #70 to 35 
ogrenci={100:{
    "ad":"ali",
    "yas":19,
    "notlar":[100,50,60]
    
}}
# print(ogrenci[100]["ad"])
# print(ogrenci[100]["yas"])
# print(ogrenci[100]["notlar"][0])
sonuc=ogrenci.get(100)

# for x in plakalar.values():
#  print(x)

for x,y in plakalar.items():
 print(x,y)
print("eskişekir"in plakalar )
print(len(plakalar))
plakalar.pop("izmir")
del plakalar["aydın"]
# del plakalar
# plakalar.clear()
plakalar2=plakalar #referans
plakalar3=plakalar.copy()
plakalar.update({
 "kocaeli":23,
 "balıkesir":10
})
