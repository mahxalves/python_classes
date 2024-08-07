import requests
from pprint import pprint

item = input("What is the Item ID? ")
url = f"https://pokeapi.co/api/v2/item/{item}"

response = requests.get(url)
print(response)

items = response.json()
print(items.keys())

print(items['held_by_pokemon'])