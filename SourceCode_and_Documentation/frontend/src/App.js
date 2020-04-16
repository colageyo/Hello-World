import React, { Component } from 'react';
import './App.css';
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom';

// components
import HelloWorldToolBar from './HelloWorldToolBar';
import HomePage from './HomePage';

class App extends Component {
  render() {
    return (
      <Router> 
      <div className="App">
      <HelloWorldToolBar />
        <Route exact path='/' component={HomePage} />
      </div>
      </Router>
    );
  }
}

export default App;