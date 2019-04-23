
# __repr__ turns created instance as string readable format
# Without using __repr__ printing instance would print something like 
# __main__.User object at 0x102483a>
# which would indicate object location in memory

class User:
    
    active_users = 0
    
    @classmethod
    def display_active_users(cls):
        return f"\nThere are currently {cls.active_users} active users online."
    
    # Class methods are used to do functions which should be run before constructor
    @classmethod
    def from_string(cls, data):
        first, last, age = data.split(",")
        return cls(first, last, int(age))
    
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
        
        
    def __repr__(self):
        return f"{self.first} is {self.age}"
        
        
    def full_name(self):
        return f"{self.first} {self.last}"
    
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    
    
    def logout(self):
        User.active_users -= 1
        return f"\n{self.first} logged out from application"
    
    
user1 = User("Joe", "Smith", 30)
print(user1)

j = User("Judy", "Steele", 18)
print(j)

