class User:
    activate_users=0
    @classmethod
    def display_activate_users(cls):
       return f"{cls.activate_users} tane aktif kullanıcı var"

    @classmethod
    def from_string(cls,data_str):
       first,last,age=data_str.split(',')
       return cls(first,last,age)

    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age
        User.activate_users+=1
    
    def full_name(self):
        return f"{self.first} {self.last}"
    
    
    def logout(self):
     User.activate_users-=1
     return f"{self.full_name()} uygulamadan cikis yapti"



ali=User.from_string("ali,korkmaz,23")
UserB=User(ali.first,ali.last,ali.age)
print(type(UserB))
print(ali.first)
print(ali)
print(User.display_activate_users())
userA=User("anil","vural",30)
print(User.display_activate_users())
print(userA.full_name())
print(userA.logout())
print(User.display_activate_users())
