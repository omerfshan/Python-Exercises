def colorize(text,color):
    colors=("blue","red","white","black","orange")
    if type(text) is not str:
        raise TypeError("text str tipinde olmalılıdır")
    if type(color) is not str:
        raise TypeError("renk str tipinde olmalılıdır")
    if color not in colors:
        raise ValueError("gecersiz renk girildi")
    print(f"{text} {color} rengindedir")

  
try:
  colorize("selam","yellow")
except Exception as ex:
  print(ex)

try:
   colorize("selam","yellow")
except (TypeError,ValueError) as ex:
   print(ex)
   