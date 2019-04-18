
class User:
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    
    def likes(self, thing):
        return f"{self.first} likes {thing}."
    
    def is_senior(self):
        return self.age >= 65
    
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday, {self.first}"
    
    def say_hi(self):
        print("\nHello!")
        
user1 = User("Joe", "Smith", 68)
print(user1.full_name())
print(user1.initials())
print(user1.likes("Candy"))
print(user1.is_senior())
print(user1.birthday())
user1.say_hi()