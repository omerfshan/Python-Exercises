while True:
    try:
        x= int(input('x: '))
        y=int(input('y: '))
        print(x/y)
    except (ZeroDivisionError,ValueError) as e:
        print(e)
        print("hata oluştu")
       
    except Exception as e:
        print(e)
        print("bilinmemyen hata oluştu")
    else:
        break