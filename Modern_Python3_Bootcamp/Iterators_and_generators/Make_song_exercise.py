
def make_song(verses=99, beverage="soda"):
      
    while verses >= 0:
        if verses >= 2:
            yield f"{verses} bottles of {beverage} on the wall."
        elif verses == 1:
            yield f"Only one bottle of {beverage} left!"
        else:
            yield f"No more {beverage} left!"
        verses -= 1
           
default_song = make_song(99, "beer")

for value in default_song:
    print(value)