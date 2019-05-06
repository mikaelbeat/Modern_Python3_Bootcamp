
import requests


url = "https://icanhazdadjoke.com/search"
term = "cat"

response = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term": term, "limit": 1})

data = response.json()

print("\n***** Returns dictionary *****\n")
print(data)

print("\n***** How to access specific value in dictionary *****\n")
print(data["results"])

print(f"\nStatus code for response: {data['status']}")