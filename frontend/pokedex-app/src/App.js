import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './store';
import PokemonList from './components/PokemonList';
import PokemonDetail from './components/PokemonDetail';
import ExportPokemons from './components/ExportPokemons';

const App = () => {
  return (
    <Provider store={store}>
      <Router>
        <div>
          <h1>Pokédex</h1>
          <Switch>
            <Route exact path="/" component={PokemonList} />
            <Route path="/pokemon/:id" component={PokemonDetail} />
          </Switch>
          <ExportPokemons />
        </div>
      </Router>
    </Provider>
  );
};

export default App;
