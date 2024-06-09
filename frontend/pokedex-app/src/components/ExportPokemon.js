import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { exportPokemonsToXML } from '../features/pokemons/pokemonsSlice';

const ExportPokemons = () => {
    const dispatch = useDispatch();
    const status = useSelector((state) => state.pokemons.status);
    const error = useSelector((state) => state.pokemons.error);

    const handleExport = () => {
        dispatch(exportPokemonsToXML({ offset: 0, limit: 20 }));
    };

    return (
        <div>
            <button onClick={handleExport} disabled={status === 'loading'}>
                Export Pokemons to XML
            </button>
            {status === 'loading' && <p>Exporting...</p>}
            {status === 'failed' && <p>Error: {error}</p>}
            {status === 'succeeded' && <p>Export successful! Check your download folder.</p>}
        </div>
    );
};

export default ExportPokemons;
