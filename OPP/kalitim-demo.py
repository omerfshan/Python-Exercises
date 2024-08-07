class User:
    active_users=0
    @classmethod
    def Display_Active_Users(cls):
      return f"{cls.active_users} aktif users var"  
    
   
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
        User.active_users+=1

class Moderator(User):
   active_moderator=0
   
   @classmethod
   def Display_Active_modaretor(cls):
      return f"{cls.active_moderator}  aktif moderator var"
   
   def __init__(self, firstName, lastName,community):
      super().__init__(firstName, lastName)
      self.community=community
      Moderator.active_moderator+=1
   def remove_post(self):
      return f"{self.firstName} {self.community} post sildi"
   def update_post(self):
      return f"{self.firstName} {self.community} post guncellendi"
   
print(User.Display_Active_Users())
print(Moderator.Display_Active_modaretor())    
u1=User("Ali","korkmaz")
m1=Moderator("yağmur","korkmaz","yazılım")
m2=Moderator("yağmur","korkmaz","yazılım")
print(User.Display_Active_Users())
print(Moderator.Display_Active_modaretor())  