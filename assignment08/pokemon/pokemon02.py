import asyncio
import httpx
import time
import random
from pypokemon.pokemon import Pokemon

async def main():
    async with httpx.AsyncClient() as client:
        rand_list=[]
        pokemon_data = []
        for i in range(5):
            rand_list.append(random.randint(1,151))
        for number in rand_list:
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            print(f"{time.ctime()} - get {pokemon_url}")
            resp = await client.get(pokemon_url)
            pokemon_json = resp.json()
            pokemon_object = Pokemon(pokemon_json)
            pokemon_data.append(pokemon_object)
        return pokemon_data

if __name__ == '__main__':
    start_time = time.perf_counter()
    pokemons = asyncio.run(main())
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous get {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")
