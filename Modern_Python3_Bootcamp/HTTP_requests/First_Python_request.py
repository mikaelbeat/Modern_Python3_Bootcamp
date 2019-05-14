
import requests

url = "http://www.google.com"

response = requests.get(url)

print("\n***** Printing response *****\n")
print(response)

print("\n***** Printing response status code *****\n")
print(response.status_code)

print("\n***** Printing response text *****\n")
print(response.text)
