from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict, Any
from model.model import PokemonModel
from ....core.repositories.irpokemon import IPokemonRepository
from aiocache import cached


class PokemonRepositoryIpml(IPokemonRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    @cached(600)
    async def get_pokemon_by_id(self, id: int) -> Dict[str, Any]:
        async with self.session() as session:
            result = await session.execute(select(PokemonModel).where(PokemonModel.id == id))
            pokemon = result.scalars().first()
            if pokemon:
                return pokemon.__dict__
            return None


    @cached(ttl=3600)
    async def get_pokemons(self, offset: int, limit: int) -> List[Dict[str, Any]]:
        async with self.session() as session:
            result = await session.execute(select(PokemonModel).offset(offset).limit(limit))
            pokemons = result.scalars().all()
            return [pokemon.__dict__ for pokemon in pokemons]
   

    async def update_pokemon_info(self, id: int, pokemon_data: Dict[str, Any]) -> None:
        async with self.session() as session:
            result = await session.execute(select(PokemonModel).where(PokemonModel.id == id))
            pokemon = result.scalars().first()
            if pokemon:
                for key, value in pokemon_data.items():
                    setattr(pokemon, key, value)
                await session.commit()

    async def insert_pokemons(self, pokemons: List[Dict[str, Any]]):
        async with self.session() as session:
            for pokemon_data in pokemons:
                pokemon = PokemonModel(**pokemon_data)
                session.add(pokemon)
            await session.commit()
