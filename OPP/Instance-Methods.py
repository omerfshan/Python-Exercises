class Person:
#    yapıcı metotlar (constructor)
    def __init__(self,name,surname,year):
    #  object attributes,instance attributes
      self.name=name
      self.surname=surname
      self.year=year
#   instance methods
    def intro(self):
     return f"Benim adim {self.name} ve soyadim {self.surname}"
    
    def calculate_age(self):
      return f"{2021-self.year}"
    
# object,Instance
p1=Person("salih","sacit",1988)
p2=Person("aylin","kontante",1944)

print(p1.intro())
print(p2.calculate_age())

        