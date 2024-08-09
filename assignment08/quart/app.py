from quart import Quart
from quart import render_template

from pypokemon.pokemon import Pokemon
import asyncio
import httpx
import time
import random

app = Quart(__name__)

async def get_pokemon(client, url):
    print(f"{time.ctime()} - get {url}")
    resp = await client.get(url)
    pokemon = resp.json()

    return Pokemon(pokemon)



async def get_pokemons():
    async with httpx.AsyncClient() as client:
        tasks = []
        rand_list= []
        for i in range(20):
            rand_list.append(random.randint(1, 151))

        for number in rand_list:
            url = f"https://pokeapi.co/api/v2/pokemon/{number}"
            tasks.append(asyncio.create_task(get_pokemon(client, url)))

        pokemons = await asyncio.gather(*tasks)
        return pokemons




@app.route('/')
async def index():
    start_time = time.perf_counter()
    pokemons = await get_pokemons()
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous get {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")
    return await render_template('index.html', pokemons=pokemons, end_time=end_time, start_time=start_time)

if __name__ == '__main__':
    app.run(debug=True, port=50002)