# - coding: utf-8 --
# http://quotes.toscrape.com/

import requests
from bs4 import BeautifulSoup
from time import sleep

baseURL = "http://quotes.toscrape.com/"
url = "/page/1"

while url:

    response = requests.get(f"{baseURL}{url}")
    print(f"Now scraping {baseURL}{url}...")
    soup = BeautifulSoup(response.text, "html.parser")
    
    all_quotes = []
    
    quotes = soup.find_all(class_="quote")
    for quote in quotes:
        all_quotes.append({
            "text": quote.find(class_="text").get_text(),
            "author": quote.find(class_="author").get_text(),
            "bio-link": quote.find("a")["href"]
            })
        
        
    next_btn = soup.find(class_="next")
    url = next_btn.find("a")["href"] if next_btn else None
    sleep(2)

    
print(all_quotes)
    



# 13:48
