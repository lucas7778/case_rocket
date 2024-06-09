from pydantic import BaseModel
from typing import List, Optional

class Pokemon(BaseModel):
    id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    abilities: List[dict]
    forms: List[dict]
    game_indices: List[dict]
    held_items: List[dict]
    location_area_encounters: str
    moves: List[dict]
    species: dict
    sprites: dict
    stats: List[dict]
    types: List[dict]
