from flask import Flask, render_template
import asyncio
import httpx
import time
import random
from pypokemon.pokemon import Pokemon


app = Flask(__name__)

async def get_pokemon(client, url):
    pass

async def get_pokemons():
    pass

@app.route('/')
async def index():
    pass
if __name__ == '__main__':
    app.run(debug=True, port=50001)