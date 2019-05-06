
import requests

from pyfiglet import figlet_format
from termcolor import colored
from random import choice


url = "https://icanhazdadjoke.com/search"

header = figlet_format("Joke Generator")

colored_header = colored(header, "red")

print(colored_header)

joke_topic = input("Let me tell you a joke! Give me a topic: ")


response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": joke_topic})

data = response.json()


found_results_amount = data["total_jokes"]

if found_results_amount:
    
    results = data["results"]
    
    print(f"\nFound {found_results_amount} jokes for {joke_topic}.\n")
    print(choice(results)["joke"])
else:
    print(f"\nSorry, i don't have any jokes about {joke_topic}.")



    