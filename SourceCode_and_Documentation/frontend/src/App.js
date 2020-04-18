import React, { Component } from 'react';
import './App.css';
import { BrowserRouter as Router, Route } from 'react-router-dom';
// components
import HelloWorldToolBar from './HelloWorldToolBar';
import HomePage from './HomePage';
import RecommendationPage from './RecommendationPage';

class App extends Component {
  render() {
    return (
      <Router>
        <div className="App">
          <HelloWorldToolBar/>
          <Route exact path='/' component={HomePage}/>
          <Route path='/recommend' component={RecommendationPage}/>
        </div>
      </Router>
    );
  }
}

export default App;
