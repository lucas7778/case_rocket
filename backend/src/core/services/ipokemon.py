from abc import ABC, abstractmethod

class IPokemon(ABC):

    @abstractmethod
    async def get_pokemons(offset: int, limit: int):
        pass
    
    @abstractmethod
    async def get_pokemon_by_id(id: int):
        pass
        