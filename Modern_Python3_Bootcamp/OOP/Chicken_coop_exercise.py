
class Chicken:
    
    total_eggs = 0
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0
        
        
    def lay_egg(self):
        Chicken.total_eggs += 1
        self.eggs += 1
        return f"{self.name} layed egg. Total layed egg count is {self.eggs}"
    
    
chicken1 = Chicken("\nAlice", "Great chicken")
print(chicken1.lay_egg())
print(chicken1.lay_egg())
print(chicken1.lay_egg())


chicken2 = Chicken("\nAmelia", "Red Chicken")
print(chicken2.lay_egg())
print(chicken2.lay_egg())


print(f"\nTotal layed eggs for all chickens are {Chicken.total_eggs}.")
    
    