
class Animal:
    
    cool = True
    
    def make_sound(self, sound):
        print(f"This animal says {sound}")
        
        
class Cat(Animal):
    pass


a = Animal()
a.make_sound("Hello")
print(a.cool)

blue = Cat()
blue.make_sound("Meow")
print(blue.cool)