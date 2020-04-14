import React, { Component } from 'react';
import { Home } from "./pages/Home";
import { Activities } from "./pages/Activities";
import { Contact } from "./pages/Contact";
import { Switch, Route, BrowserRouter } from "react-router-dom";
import './App.css';
import HelloWorldToolBar from './components/HelloWorldToolBar';

class App extends Component {
  render() {
    return (
      <>
        <HelloWorldToolBar />
        <BrowserRouter>
          <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/activities" component={Activities} />
            <Route path="/contact" component={Contact} />
          </Switch>
        </BrowserRouter>
      </>
    );
  }
}

export default App;
