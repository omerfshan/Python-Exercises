class User:
    activate_users=0
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

print(User.activate_users)
userA=User("anil","vural",30)
print(userA.full_name())
print(User.activate_users)
print(userA.logout())
print(User.activate_users)