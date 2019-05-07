
# Adding @be_polite to fuction gives fuction ablity to call given function


def be_polite(func):
    def wrapper():
        print("What a pleasure to meet you!")
        func()
        print("Have a great day!\n")
    return wrapper()

@be_polite
def greet():
    print("My name is Colt.")
    
@be_polite    
def rage():
    print("I hate you!")
    
