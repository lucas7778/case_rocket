import { configureStore } from '@reduxjs/toolkit';
import pokemonsReducer from './features/pokemons/pokemonsSlice';

const store = configureStore({
    reducer: {
        pokemons: pokemonsReducer,
    },
});

export default store;
