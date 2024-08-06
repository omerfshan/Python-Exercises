class Person:
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
        print("person nesnesi türetildi")
    def intro(self):
        print(self.name,self.surname,self.age)

class Teacher(Person):
    def __init__(self, name, surname, age,branch):
        super().__init__(name, surname, age)
        self.branch=branch
    def teach(self):
     print(f"{self.name} ogretmen {self.branch} öğretiyor")

    def intro(self):
     print(self.name,self.surname,self.age,self.branch)
class Student(Person):
   def __init__(self, name, surname, age,number):
      super().__init__(name, surname, age)
      self.number=number
   def study(self):
      print(f"{self.number} numaralı {self.name} ogrenci derstte")
   def intro(self):
        print(self.name,self.surname,self.age,self.number) 


p1=Person("aydın","gunes",26)
p1.intro()
t1=Teacher("Ersin","Karcı",30,"ingilizce")
t1.intro()
t1.teach()
s1=Student("azra","bulut",21,278787)
s1.intro()
s1.study()