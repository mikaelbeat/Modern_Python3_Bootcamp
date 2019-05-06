
from termcolor import colored

text = colored("Hi there!", color="magenta", on_color="on_yellow", attrs=["blink"])
print(text)