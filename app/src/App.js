import React, { Component } from 'react';
import './App.css';
import HelloWorldToolBar from './HelloWorldToolBar';
import ContactUsPage from './ContactUs';

class App extends Component {
  render() {
    return (
      <React.Fragment>
        <HelloWorldToolBar />
        <ContactUsPage />
      </React.Fragment>
    );
  }
}

export default App;
