from ...core.services.ipokemon import IPokemon
import httpx
from typing import Any, Dict
import asyncio


class IRPokemon(IPokemon):
    
    BASE_URL = "https://pokeapi.co/api/v2/pokemon"
    semaphore = 10

    async def get_pokemons(self, offset: int, limit: int) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            response = await client.get(self.BASE_URL, params={"offset": offset, "limit": limit})
            response.raise_for_status()
            return response.json()

    async def get_pokemon_by_id(self, id: int) -> Dict[list[Dict], Any]:
        
        async with self.semaphore:

            async with httpx.AsyncClient() as client:
                tasks = []
                response = await client.get(f"{self.BASE_URL}/{id}")
                tasks.append(asyncio.ensure_future(response))
                pokemon = asyncio.gather(*tasks)
                return pokemon
        
     

