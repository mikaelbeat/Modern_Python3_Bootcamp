
class Aquatic:
    
    def __init__(self, name):
        self.name = name
        
    def swm(self):
        return f"\n{self.name} is swimming"
    
    def greet(self):
        return f"\nI am {self.name} of the sea!"
    
    
class Ambulatory:
    
    def __init__(self, name):
        self.name = name
        
    def walk(self):
        return f"\n{self.name} is walking"
    
    def greet(self):
        return f"I am {self.name} of the land!"
    
    
class Penguin(Ambulatory, Aquatic):
    
    def __init__(self, name):
        super().__init__(name=name)
        
jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")