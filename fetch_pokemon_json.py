import requests
import json


def fetch_pokemon_data(pokemon_name):
    response1 = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    pokemon = response1.json()
    

    return pokemon

def calculate_average_weight(pokemon_list):
    total_weight = 0
    for weight in pokemon_list:
        total_weight += weight

    average = total_weight/3
    
    return average

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_weights = []

for pokemon in pokemon_names:
    pokemon_data = fetch_pokemon_data(pokemon)
    name = pokemon_data.get("name")
    types = pokemon_data.get("types")

    for type in types:
        type_final = type['type']['name']

    print(f"{name}: {type_final}")
    pokemon_weights.append(pokemon_data["weight"])

average = calculate_average_weight(pokemon_weights)
print(f"average weight of the three pokemon is: {average}")