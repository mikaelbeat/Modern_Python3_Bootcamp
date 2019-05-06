
from pyfiglet import figlet_format

from termcolor import colored


def print_art(text, color):
    colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
    if color not in colors:
        color = "white"
    result = figlet_format(text)
    colored_result = colored(result, color=color)
    print(colored_result)


text = input("\nWhat would you like to print? ")
color = input("\nWhat color? ")

print_art(text, color)