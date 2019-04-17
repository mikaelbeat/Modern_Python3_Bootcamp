
print("\n********** Keyword args return dictionary **********\n")
def fav_colors(**kwargs):
    for person, color in kwargs.items():
      print(f"{person}'s favourite color is {color}")  
    
fav_colors(colt="purple", ruby="red", ethel="teal")


print("\n********** Another kwargs example **********\n")
def special_greeting(**kwargs):
    if "David" in kwargs and kwargs ["David"] == "special":
        return "You get a special greeting!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David! "
    return "Not sure wh this is!"

print(special_greeting(Bob="hello"))