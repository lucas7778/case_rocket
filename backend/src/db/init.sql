CREATE TABLE pokemons (
    id INTEGER NOT NULL, 
    name VARCHAR, 
    base_experience INTEGER, 
    height INTEGER, 
    is_default BOOLEAN, 
    "order" INTEGER, 
    weight INTEGER, 
    abilities JSON, 
    forms JSON, 
    game_indices JSON, 
    held_items JSON, 
    location_area_encounters VARCHAR, 
    moves JSON, 
    species JSON, 
    sprites JSON, 
    stats JSON, 
    types JSON, 
    PRIMARY KEY (id)
);
CREATE INDEX ix_pokemons_id ON pokemons (id);
CREATE INDEX ix_pokemons_name ON pokemons (name);