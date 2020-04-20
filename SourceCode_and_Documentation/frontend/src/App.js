import React, { Component } from 'react';
import './App.css';
import { BrowserRouter as Router, Route, withRouter } from 'react-router-dom';
import Banner from './Banner';
import './Banner.css'

// components
import HelloWorldToolBar from './HelloWorldToolBar';
import HomePage from './HomePage';
import RecommendationPage from './RecommendationPage';

const styles = {
  sunset: {
    background: "linear-gradient(to bottom, #ff927f, #ff927f, #ffffff)",
    color: "#000000"
  },
  day: {
    background: "linear-gradient(to bottom, #dcf1f9, #d6dde4, #ffffff)",
    color: "#000000"
  },
  rainy: {
    backgroundImage: `linear-gradient(to bottom, #7e96a1, #a3b4bc, #ffffff)`,
  },
  sunrise: {
    background: "linear-gradient(to bottom, #9280ff, #ffbb83, #ffffff)"
  },
  evening: {
    background: "linear-gradient(to bottom, #3d3848, #4c4857, #787580, #95939b, #ffffff)",
    color: "#ffffff"
  }
}


class App extends Component {
  render() {
    // if true, display gradient background
    const toggleDynamicBackgroundOn = true;
    const style = "rainy";
    const isCovid = true;

    return (
      <Router>
        <div className="App" style={toggleDynamicBackgroundOn ? styles[style] : {}}>
          {isCovid && <Banner />}
          <HelloWorldToolBar />
          <Route exact path='/' component={() => <HomePage isCovid={isCovid} />} />
          <Route path='/recommend' component={() => <RecommendationPage isCovid={isCovid} />} />
        </div>
      </Router>
    );
  }
}

export default App;
