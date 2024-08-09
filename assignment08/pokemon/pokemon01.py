import requests as requests
import time
import random
from pypokemon.pokemon import Pokemon

def get_pokemon(url):
    print(f"{time.ctime()} - get {url}")
    resp = requests.get(url)
    pokemon = resp.json()

    return pokemon

def get_pokemons():
    rand_list=[]
    for i in range(5):
        rand_list.append(random.randint(1,151))

    pokemon_data = []
    for number in rand_list:
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        pokemon_json = get_pokemon(url)
        pokemon_object = Pokemon(pokemon_json)
        pokemon_data.append(pokemon_object)
    return pokemon_data

def main():
    start_time = time.perf_counter()
    pokemons = get_pokemons()
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Synchronous get {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")

if __name__ == '__main__':
    main()