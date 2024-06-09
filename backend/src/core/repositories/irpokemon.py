from abc import ABC, abstractmethod
from typing import Dict

class IRPokemon(ABC):

    @abstractmethod
    async def get_pokemons_repository(offset: int, limit: int):
        pass
    
    @abstractmethod
    async def get_pokemon_by_id_repository(id: int):
        pass

    @abstractmethod
    async def insert_pokemons(pokemons: Dict):
        pass

    @abstractmethod
    async def update_pokemon_info(id: int):
        pass

    
