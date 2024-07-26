import aiofiles
import asyncio
import json
from pathlib import Path

pokemonapi_directory = './assignment07/pokemon/pokemonapi'
pokemonmove_directory = './assignment07/pokemon/pokemonmove'

async def main():
    pathlist = Path(pokemonapi_directory).glob('*.json')
    
    for path in pathlist:
        # Read the Pokémon data asynchronously
        async with aiofiles.open(path, mode='r') as f:
            pokemon = json.loads(await f.read())
        
        # Extract the Pokémon name and moves
        name = pokemon['name']
        moves = [move['move']['name'] for move in pokemon['moves']]
        
        # Write the moves to a new file asynchronously
        async with aiofiles.open(f'{pokemonmove_directory}/{name}_moves.txt', mode='w') as f:
            await f.write('\n'.join(moves))

if __name__ == "__main__":
    asyncio.run(main())
