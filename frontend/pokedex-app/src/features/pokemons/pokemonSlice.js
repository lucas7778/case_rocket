import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

const initialState = {
    pokemons: [],
    pokemon: null,
    status: 'idle',
    error: null,
};

export const fetchPokemons = createAsyncThunk('pokemons/fetchPokemons', async ({ offset, limit }) => {
    const response = await axios.get(`/api/pokemons?offset=${offset}&limit=${limit}`);
    return response.data;
});

export const fetchPokemonById = createAsyncThunk('pokemons/fetchPokemonById', async (id) => {
    const response = await axios.get(`/api/pokemon/${id}`);
    return response.data;
});

export const exportPokemonsToXML = createAsyncThunk('pokemons/exportPokemonsToXML', async ({ offset, limit }) => {
    const response = await axios.get(`/api/pokemons/xml?offset=${offset}&limit=${limit}`);
    return response.data;
});

const pokemonsSlice = createSlice({
    name: 'pokemons',
    initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(fetchPokemons.pending, (state) => {
                state.status = 'loading';
            })
            .addCase(fetchPokemons.fulfilled, (state, action) => {
                state.status = 'succeeded';
                state.pokemons = action.payload;
            })
            .addCase(fetchPokemons.rejected, (state, action) => {
                state.status = 'failed';
                state.error = action.error.message;
            })
            .addCase(fetchPokemonById.pending, (state) => {
                state.status = 'loading';
            })
            .addCase(fetchPokemonById.fulfilled, (state, action) => {
                state.status = 'succeeded';
                state.pokemon = action.payload;
            })
            .addCase(fetchPokemonById.rejected, (state, action) => {
                state.status = 'failed';
                state.error = action.error.message;
            })
            .addCase(exportPokemonsToXML.pending, (state) => {
                state.status = 'loading';
            })
            .addCase(exportPokemonsToXML.fulfilled, (state) => {
                state.status = 'succeeded';
            })
            .addCase(exportPokemonsToXML.rejected, (state, action) => {
                state.status = 'failed';
                state.error = action.error.message;
            });
    },
});

export default pokemonsSlice.reducer;
