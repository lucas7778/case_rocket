from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from core.domain.use_cases.get_pokemon_by_id_use_case import GetPokemonsByIdUseCase
from core.domain.use_cases.get_pokemons_use_case import GetPokemonsUseCase
from core.domain.use_cases.export_pokemons_to_xml_use_case import ExportPokemonsToXMLUseCase
from infra.data.repositories.repository_impl import PokemonRepositoryIpml
from sqlalchemy.ext.asyncio import AsyncSession
from infra.data.model.model import SessionLocal
from aiocache import cached
import os, asyncio

router = APIRouter()
session: AsyncSession = SessionLocal()
pokemon_repository = PokemonRepositoryIpml(session)
queue = asyncio.Queue()
semaphore = asyncio.Semaphore(10)

@router.get("/pokemon/{pokemon_id}")
async def get_pokemon_by_id(pokemon_id: int):
    get_pokemon_by_id_use_case = GetPokemonsByIdUseCase(pokemon_repository)

    result = await get_pokemon_by_id_use_case.execute({"id": pokemon_id})
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@router.get("/pokemons/")
async def get_pokemons(offset: int = 0, limit: int = 20):
    get_pokemons_use_case = GetPokemonsUseCase(pokemon_repository)

    result = await get_pokemons_use_case.execute({"offset": offset, "limit": limit})
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@router.get("/pokemons/xml")
@cached(ttl=600)
async def get_pokemon_xml(offset: int = 0, limit: int = 20):
    export_pokemons_to_xml_use_case = ExportPokemonsToXMLUseCase(pokemon_repository)
    file_path = "pokemon.xml"
    
    await queue.put(file_path)
    while not queue.empty():
        async with semaphore:
            file_path = await queue.get()
            try:
                await export_pokemons_to_xml_use_case.execute({"offset": offset, "limit": limit}, file_path)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
            finally:
                queue.task_done()

    if not os.path.exists(file_path):
        raise HTTPException(status_code=500, detail="Failed to generate XML file")

    return FileResponse(file_path, media_type='application/xml', filename=file_path)
