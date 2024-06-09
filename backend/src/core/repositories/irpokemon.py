from abc import ABC, abstractmethod
from typing import Dict, List, Any

class IRPokemon(ABC):
    
    @abstractmethod
    async def get_pokemon_by_id(self, id: int) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def get_pokemons(self, offset: int, limit: int) -> List[Dict[str, Any]]:
        pass
    
    @abstractmethod
    async def update_pokemon_info(self, id: int, pokemon_data: Dict[str, Any]) -> None:
        pass
    
    @abstractmethod
    async def insert_pokemons(self, pokemons: List[Dict[str, Any]]):
        pass
