from typing import Dict, Any
from ...services.ipokemon import IPokemon
from ...repositories.irpokemon import IRPokemon
from ..entities import pokemon


class GetPokemonsByIdUseCase: 
    
     def __init__(self, ipokemon: IPokemon, pokemon_repository: IRPokemon ) -> None:
        self._ipokemon = ipokemon
        self._pokemon_repository = pokemon_repository

     async def execute(self, input: Dict[str, Any]) -> Dict[str, Any]:
        pokemon_id =  input["id"]
        
        pokemon_by_id =  await self.pokemon_repository.get_pokemon_by_id(pokemon_id)

        if pokemon_by_id["stats"] is None: 
            pokemon_by_id = await self.ipokemon.get_pokemon_by_id(pokemon_id)
            pokemon_entity = pokemon.PokemonEntity(**pokemon_by_id)
            
            await self.pokemon_repository.update_pokemon_info(pokemon_entity)

            return pokemon_entity
        
        return pokemon_by_id
            

