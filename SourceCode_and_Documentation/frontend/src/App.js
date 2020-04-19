import React, { Component } from 'react';
import './App.css';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import sun_img from './assets/sun_icon.png';
import rain_drop from './assets/rain_drop.png';

// components
import HelloWorldToolBar from './HelloWorldToolBar';
import HomePage from './HomePage';
import RecommendationPage from './RecommendationPage';
import ContactUsPage from './ContactUs';

const styles = {
  sunset: {
    background: "linear-gradient(to bottom, #392033, #fd6051, #fec051)",
    color: "#ffffff"
  },
  day: {
    background: "linear-gradient(to bottom, #c7dff1, #d6dde4)",
    color: "#000000"
  },
  rainy: {
    backgroundImage: `url(${rain_drop}), linear-gradient(to bottom, #cfd8dc, #d6dde4)`,
  },
  sunrise: {
    background: "linear-gradient(to bottom, #f5a57f, #fee4a2, #8a92a5)"
  },
  evening: {
    background: "linear-gradient(to bottom, #131862, #2e4482, #546bab, #bea9de)",
    color: "#ffffff"
  }
}

class App extends Component {
  render() {
    // if true, display gradient background
    const toggleDynamicBackgroundOn = true;
    const style = "rainy";

    return (
      <Router>
        <div className="App" style={toggleDynamicBackgroundOn ? styles[style] : {}}>
          <HelloWorldToolBar/>
          <Route exact path='/' component={HomePage}/>
          {toggleDynamicBackgroundOn && style == 'day' && <img className="sun" src={sun_img} />}
          <Route path='/recommend' component={RecommendationPage}/>
          <Route path='/contact' component={ContactUsPage}/>
        </div>
      </Router>
    );
  }
}

export default App;
