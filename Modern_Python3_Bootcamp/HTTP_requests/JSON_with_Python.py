
import requests


url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"})

data = response.json()

print("\n***** Returns dictionary *****\n")
print(data)

print("\n***** How to access specific value in dictionary *****\n")
print(data["joke"])

print(f"\nStatus code for response: {data['status']}")