import requests
from pprint import pprint
pokemon_number = input("What is the Pokemon's ID? ")
url = f'https://pokeapi.co/api/v2/pokemon/'format(pokemon_number)


response = requests.get(url)
print(response)
pokemon = response.json()
#pprint(pokemon)
print(pokemon.keys())
print(pokemon['name'])
print(pokemon['height'])
print(pokemon['weight'])

print(pokemon['abilities'])
pprint(pokemon['moves'][0]['move']['name'])

moves = pokemon['moves']

for move in moves:
    print(move['move']['name'])