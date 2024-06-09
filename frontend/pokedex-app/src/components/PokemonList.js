import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchPokemons } from '../features/pokemons/pokemonsSlice';

const PokemonList = () => {
    const dispatch = useDispatch();
    const pokemons = useSelector((state) => state.pokemons.pokemons);
    const status = useSelector((state) => state.pokemons.status);
    const error = useSelector((state) => state.pokemons.error);

    useEffect(() => {
        dispatch(fetchPokemons({ offset: 0, limit: 20 }));
    }, [dispatch]);

    if (status === 'loading') {
        return <div>Loading...</div>;
    }

    if (status === 'failed') {
        return <div>Error: {error}</div>;
    }

    return (
        <div>
            <h2>Pokemon List</h2>
            <ul>
                {pokemons.map((pokemon) => (
                    <li key={pokemon.id}>{pokemon.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default PokemonList;
