from typing import Dict, Any
from ...repositories.irpokemon import IRPokemon

class GetPokemonsUseCase:
    
    def __init__(self, pokemon_repository: IRPokemon) -> None:
        self.pokemon_repository = pokemon_repository

    async def execute(self, input: Dict[str, Any]) -> Dict[str, Any]: 
        offset: int = int(input["offset"])  
        limit: int = int(input["limit"])    
        
        pokemons_from_repository: Dict[str, Any] = await self.pokemon_repository.get_pokemons(offset, limit)

        return pokemons_from_repository
        

