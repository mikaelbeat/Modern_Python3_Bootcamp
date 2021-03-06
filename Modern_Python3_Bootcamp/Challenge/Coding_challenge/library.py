import sys


# Define library book collection datafile
datafile = sys.argv[1]
        

def show_menu():
    print("\n********** LIBRARY APPLICTION **********\n")
    print("Available actions:")
    print("1 - Add a new book")
    print("2 - Show book collection")
    print("3 - Quit")
    
    selection = int(input("\nWhat do you want to do? "))  
        
    if (selection == 1):
        add_a_new_book()
    elif (selection == 2):
        show_collection()
    elif (selection == 3):
        quit_program()


def add_a_new_book():
    name = input("\nEnter name of the book: ")
    writer = input("\nEnter book writer name: ")
    isbn = input("\nGive book isbn: ")
    
    print("\nBook information " + name + ", " + writer + ", " + isbn)
    saveBook = input("\nDo you want to add new book to collection, yes or no? ")
    
    if(saveBook == "yes"):
        with open(datafile, 'a') as file:
            file.write(name + ", " + writer + ", " + isbn + "\n")
            print("\nBook saved to collection!")
    else:
        print("\nBook not saved to collection, returning to main menu.")
    show_menu()
    
    
def show_collection():
    print("\nLibrary book collection\n")
    with open(datafile, "r") as file:
        print(file.read())
    show_menu()


def quit_program():
    print("\nQuitting library program")
    sys.exit(0)
    
    
# Starting library application    
show_menu()