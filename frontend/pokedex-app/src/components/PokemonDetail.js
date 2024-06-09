import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchPokemonById } from '../features/pokemons/pokemonsSlice';

const PokemonDetail = ({ match }) => {
    const dispatch = useDispatch();
    const pokemon = useSelector((state) => state.pokemons.pokemon);
    const status = useSelector((state) => state.pokemons.status);
    const error = useSelector((state) => state.pokemons.error);

    useEffect(() => {
        dispatch(fetchPokemonById(match.params.id));
    }, [dispatch, match.params.id]);

    if (status === 'loading') {
        return <div>Loading...</div>;
    }

    if (status === 'failed') {
        return <div>Error: {error}</div>;
    }

    if (!pokemon) {
        return <div>Pokemon not found</div>;
    }

    return (
        <div>
            <h2>{pokemon.name}</h2>
            <p>ID: {pokemon.id}</p>
            <p>Height: {pokemon.height}</p>
            <p>Weight: {pokemon.weight}</p>
            <p>Base Experience: {pokemon.base_experience}</p>
        </div>
    );
};

export default PokemonDetail;
