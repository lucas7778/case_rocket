from core.domain.use_cases.get_pokemons_use_case import GetPokemonsUseCase
from infra.data.repositories.repository_impl import PokemonRepositoryIpml
from infra.data.model.model import SessionLocal

async def insertDataOnDb():
    async with SessionLocal() as session:
        pokemon_repository = PokemonRepositoryIpml(session)
        get_pokemons_use_case = GetPokemonsUseCase(pokemon_repository)
        pokemons = await get_pokemons_use_case.execute({"offset": 1, "limit": 1302})
        await pokemon_repository.insert_pokemons(pokemons)
