
import sqlite3, requests
from bs4 import BeautifulSoup


response = requests.get("http://books.toscrape.com/catalogue/category/books/history_32/index.html")
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article")


for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.select(".price_color")[0].get_text()
    price = float(price.replace("Â","").replace("£",""))
    