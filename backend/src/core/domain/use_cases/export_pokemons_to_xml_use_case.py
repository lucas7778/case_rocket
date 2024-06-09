from typing import Any, Dict
from ...repositories.irpokemon import IRPokemon
from utils.xml_generator import generate_pokemon_xml
from aiocache import cached


class ExportPokemonsToXMLUseCase:

     def __init__(self, pokemon_repository: IRPokemon) -> None:
        self.pokemon_repository = pokemon_repository
    
     @cached(ttl=600)
     async def execute(self, input: Dict[str, str], file_path):
         offset =  input["offset"]
         limit =  input["limit"]

         pokemons_data =  await self.pokemon_repository.get_pokemons_repository(offset, limit)
         generate_pokemon_xml(pokemons_data, file_path)
         return file_path

         
    