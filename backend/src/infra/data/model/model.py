from sqlalchemy import Column, Integer, String, Boolean, JSON, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class PokemonModel(Base):
    __tablename__ = 'pokemons'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    base_experience = Column(Integer)
    height = Column(Integer)
    is_default = Column(Boolean)
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