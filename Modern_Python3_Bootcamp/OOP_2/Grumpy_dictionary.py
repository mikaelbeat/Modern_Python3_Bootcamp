
class GrumpyDict(dict):
    
    def __repr__(self):
        print("None of your business") 
        return super().__repr__()
    
    def __missing__(self, key):
        print(f"You want {key}? Well it aint here!")
        
    def __setitem__(self, key, value):
        print("You want to change the dictionary?")
        print("Ok, fine!")
        super().__setitem__(key, value)
        
    def __contains__(self, item):
        print("No, it aint in here!")
        return False
        
    
data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
data["city"]   
data["city"] = "Tokyo"    
print(data)