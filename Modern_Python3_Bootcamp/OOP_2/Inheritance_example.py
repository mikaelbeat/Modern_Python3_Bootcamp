
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
        
        
    def full_name(self):
        return f"{self.first} {self.last}"
    
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    
    
    def logout(self):
        User.active_users -= 1
        return f"\n{self.first} logged out from application"
    
    
class Moderator(User):
    
    total_mods = 0
    
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1
        
        
    @classmethod
    def display_active_moderators(cls):
        return f"\nThere is currently {cls.total_mods} moderators online."
        
    def remove_post(self):
        return f"{self.full_name} removed post from {self.community}."
    
    
print(User.display_active_users())    

jasmine = Moderator("Jasmine", "Connor", 40, "Piano")
jasmine2 = Moderator("Jasmine", "Connor", 40, "Piano")

print(User.display_active_users())

user1 = User("Tom", "Garcia", 35)
user2 = User("Tom", "Garcia", 35)
user3 = User("Tom", "Garcia", 35)
user4 = User("Tom", "Garcia", 35)

print(User.display_active_users())
print(Moderator.display_active_moderators())







