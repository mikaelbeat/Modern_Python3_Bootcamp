
# Raise own error
# raise ValueError("This is custom error!")


def colorize(text, color):
    colors = ("blue", "red", "yellow")
    if type(text) is not str:
        raise TypeError("Text must be a str")
    if color not in colors:
        raise ValueError("Color is invalid color")
    print(f"Printed {text} in {color}.")
    

colorize("Hello", "green")
colorize(12345, "red")