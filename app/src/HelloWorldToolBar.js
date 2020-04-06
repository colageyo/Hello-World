import React, { Component } from 'react';
import './HelloWorldToolBar.css';
import './App.css';
import Logo from './favicon.ico'

class HelloWorldToolBar extends Component {
  render() {
    return (
      <div className="main-container">
        <div className="inner-container">
          <img className="logo" src={Logo}/>
          <div className="text-container">
            <div className="text tool-bar-text button">Activities and Events</div>
            <div className="text tool-bar-text button">Contact Us</div>
          </div>
        </div>
      </div>
    );
  }
}

export default HelloWorldToolBar;
