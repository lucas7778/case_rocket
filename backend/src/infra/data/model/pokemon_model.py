from sqlalchemy import Column, Integer, String, JSON
from infra.data.model.model import Base

class PokemonModel(Base):
    __tablename__ = "pokemon"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    base_experience = Column(Integer)
    height = Column(Integer)
    is_default = Column(String)
    order = Column(Integer)
    weight = Column(Integer)
    abilities = Column(JSON)
    forms = Column(JSON)
    game_indices = Column(JSON)
    held_items = Column(JSON)
    location_area_encounters = Column(String)
    moves = Column(JSON)
    species = Column(JSON)
    sprites = Column(JSON)
    stats = Column(JSON)
    types = Column(JSON)
