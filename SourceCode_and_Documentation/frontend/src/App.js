import React, { Component } from "react";
import { BrowserRouter as Router, Route, withRouter } from "react-router-dom";

import "./App.css";
import "./Banner.css";

// components
import Banner from "./Banner";
import HelloWorldToolBar from "./HelloWorldToolBar";
import HomePage from "./HomePage";
import RecommendationPage from "./RecommendationPage";
import ContactUsPage from "./ContactUs";

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
    backgroundImage: `linear-gradient(to bottom, #7e96a1, #a3b4bc, #ffffff)`
  },
  sunrise: {
    background: "linear-gradient(to bottom, #9280ff, #ffbb83, #ffffff)"
  },
  evening: {
    background:
      "linear-gradient(to bottom, #3d3848, #4c4857, #787580, #95939b, #ffffff)",
    color: "#ffffff"
  }
};

export const categories = [
  "family-friendly",
  "artsy",
  "hungry",
  "geeky",
  "historic",
  "indoors",
  "outdoors",
  "romantic",
  "sporty"
];

class App extends Component {
  state = {
    categories: new Map(categories.map(cat => [cat, false]))
  };

  toggleCategory = category => {
    this.setState(state => ({
      categories: {
        ...state.categories,
        [category]: !state["categories"][category]
      }
    }));
  };

  render() {
    // if true, display gradient background
    const toggleDynamicBackgroundOn = true;
    const style = "rainy";
    const isCovid = false;

    return (
      <Router>
        <div
          className="App"
          style={toggleDynamicBackgroundOn ? styles[style] : {}}
        >
          {isCovid && <Banner />}

          <HelloWorldToolBar style={style}/>

          <Route
            exact
            path="/"
            component={() => (
              <HomePage
                isCovid={isCovid}
                categories={this.state.categories}
                toggleCategory={this.toggleCategory}
                style={style}
              />
            )}
          />
          <Route
            path="/recommend"
            component={() => (
              <RecommendationPage
                isCovid={isCovid}
                tags={this.state.categories}
                toggleCategory={this.toggleCategory}
                style={style}
              />
            )}
          />
          <Route
            path="/contact"
            component={() => <ContactUsPage style={style} />}
          />
        </div>
      </Router>
    );
  }
}

export default App;
