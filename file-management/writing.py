with open('file-management/new-file.txt',"w",encoding="UTF-8") as file:
    file.write("hello word!\n")
    file.write("merhaba\n")
    file.write("dunya")
    print(file)
with open("file-management/new-file.txt") as file:
    print(file.read())