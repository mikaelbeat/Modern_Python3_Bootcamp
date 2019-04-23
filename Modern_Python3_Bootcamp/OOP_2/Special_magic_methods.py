from copy import copy

class Human:
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        
    def __repr__(self):
        return f"Human named {self.first} {self.last}"
    
    def __len__(self):
        return self.age
    
    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="Newborn", last=self.last, age=0)
        
    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return "Cant multiply"
        
        
        
human1 = Human("Jenny", "Larsen", 47)
print(human1)
print(len(human1))

human2 = Human("Kevin", "Jones", 20)

triplets = human1 * 3
triplets[1].first = "Jessica"
print(triplets)