with open('file-management/new-file.txt',"a",encoding="UTF-8") as file:
    file.write("hello word!\n")
    file.write("merhaba\n")
    file.write("dunya")
    print(file)
    # cursoru değiştirmek append modunda etkilemez


with open('file-management/new-file.txt',"r+",encoding="UTF-8") as file:
    file.read()
    # read metodu  cursoru ensona getirecek
    file.write("yeni satır")
    # r+ en baştan yazar yani cursor 0 dan başlar
