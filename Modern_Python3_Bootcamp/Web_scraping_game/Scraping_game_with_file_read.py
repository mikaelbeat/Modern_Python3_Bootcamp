# - coding: utf-8 --
# http://quotes.toscrape.com/

import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

baseURL = "http://quotes.toscrape.com/"


def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)
        




def start_game(quotes):    
    remaining_guesses = 4
    
    quote = choice(quotes)
    print(f"Here is a quote: {quote['text']}")
    print(f"Author is {quote['author']}")
    
    guess = ""
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"\nGuesses remaining: {remaining_guesses}. Who said this quote? ")
        if guess.lower() == quote["author"].lower():
            print("\nCorrect answer!")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            response = requests.get(f"{baseURL}{quote['bio-link']}")
            soup = BeautifulSoup(response.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"\nHere is a hint: The author was born in {birth_date} {birth_place}.")
        elif remaining_guesses == 2:
            print(f"\nHere's a hint, author's first name starts with {quote['author'][0]}.")
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"\nHere's a hint: The author's last name starts with {last_initial}.")
        else:
            print(f"\nSorry you ran out of guesses. The author was {quote['author']}")
        
    again = ""
    
    while again.lower() not in ("y" ,"yes", "n", "no"):
        again = input("\nWould you like to play again? (y/n) ")
    if again.lower() in ("yes", "y"):
        return start_game(quotes)
    else:
        print("\nGame over!")
    

quotes = read_quotes("quotes.csv")
start_game(quotes)
