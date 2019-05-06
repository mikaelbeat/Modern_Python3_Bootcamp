
import requests

url = "http://www.google.com"

response = requests.get(url)

print(response)
print(response.status_code)
print(response.text)
