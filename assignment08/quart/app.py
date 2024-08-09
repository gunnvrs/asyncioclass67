from quart import Quart
from quart import render_template

from pypokemon.pokemon import Pokemon
import asyncio
import httpx
import time
import random

app = Quart(__name__)

async def get_pokemon(client, url):
    pass




async def get_pokemons():
    async with httpx.AsyncClient() as client:
        pass




@app.route('/')
async def index():
    pass

if __name__ == '__main__':
    app.run(debug=True, port=50002)