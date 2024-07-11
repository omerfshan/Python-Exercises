import random
sayilar = [random.randint(1, 30) for _ in range(40)]
sonuc=sorted(sayilar)
sonuc=sorted(sayilar,reverse=True)
sonuc=sorted((random.randint(1, 30) for _ in range(40)))


users=[
    {"username":"user1","tweets":["tweet 1","tweet 2"]},
    {"username":"user2","tweets":[]},
    {"username":"user3","tweets":["twet1"]}
]

sonuc=sorted(users,key=len)
sonuc=sorted(users,key=lambda a:a["username"])
sonuc=sorted(users,key=lambda a:len(a["tweets"]))










print(sonuc)