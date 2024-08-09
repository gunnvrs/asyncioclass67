from pypokemon.pokemon import Pokemon
import asyncio
import httpx
import time
import random

async def get_pokemon(client, url):
    pass

async def get_pokemons():
    async with httpx.AsyncClient() as client:
        pass

async def index():
    start_time = time.perf_counter()
    pokemons = await get_pokemons()
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous get {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")

if __name__ == '__main__':
   asyncio.run(index())