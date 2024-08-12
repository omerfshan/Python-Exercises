try:
    with open("file-management\msg.txt","r",encoding="utf-8") as file:
    # print(file.read())
    # print(file.tell())# cursor nerde
    # print(file.read(10))
    # print(file.tell())# cursor nerde
        for i in file:
            print(i,end="")
except FileNotFoundError as e:
    print("dosya okuma hatası: " + e)
finally:
    print("dosya kapandı")