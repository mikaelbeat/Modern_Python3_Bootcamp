
class User:
    
    active_users = 0
    
    @classmethod
    def display_active_users(cls):
        return f"\nThere are currently {cls.active_users} active users online."
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
        
        
    def full_name(self):
        return f"{self.first} {self.last}"
    
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    
    
    def logout(self):
        User.active_users -= 1
        return f"\n{self.first} logged out from application"
    
    
print("\nActive users at start: " + str(User.active_users))
    
    
user1 = User("Joe", "Smith", 30)

user2 = User("Matt", "Damon", 34)


print("\nActive users online: " + str(User.active_users))

print(user1.logout())

print("\nActive users online: " + str(User.active_users))


print(User.display_active_users())