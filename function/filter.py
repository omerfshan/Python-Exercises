yaslar=[5,12,18,24,45]
sonuc=list(filter(lambda x:x>=18,yaslar))
sonuc=list(filter(lambda x: x%2!=0,yaslar))

users=[
    {"username":"user1","tweets":["tweet 1","tweet 2"]},
    {"username":"user2","tweets":[]},
    {"username":"user3","tweets":["twet1"]}
]
sonuc=list(filter(lambda a:len(a["tweets"])>0,users))
sonuc=list(map(lambda u: u["username"].upper(),filter(lambda a:len(a["tweets"])>0,users) ))
sonuc=[user["username"].upper() for user in users if len(user["tweets"])>0]
print(sonuc)
