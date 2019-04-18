
# Keyword args are given in form
# def kwargs_demo(**kwargs):
#
# print(kwargs_demo(job="instructor"))



print("\n********** Keyword kwargs return dictionary **********\n")
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
    return "Not sure who this is!"

print(special_greeting(David="hello"))