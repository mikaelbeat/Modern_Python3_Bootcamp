
import sqlite3
import requests

from bs4 import BeautifulSoup


# Request URL
response = requests.get("http://books.toscrape.com/catalogue/category/books/history_32/index.html")
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article")
print(books)

# Initialize BS

# Extract data

# Save data to database