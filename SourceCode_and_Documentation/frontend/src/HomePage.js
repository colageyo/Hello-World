import React, { Component } from 'react';
import Banner from './Banner';
import './Banner.css'
import './HomePage.css';
import Background from './assets/background_day.png';
import MoodButtonList from './MoodButtonList';

class HomePage extends Component {

  render() {
    const { isCovid } = this.props;
    return (
      <div className="home-page small-content">
        {isCovid && <Banner />}
        <div className="home-container">
          <div className="home-text">
            <div className="text large-text">Hello Sydney ! </div>
            <div className="text small-text">I'm in the mood for something... </div>
          </div>
          <MoodButtonList />
          <div className="text home-text submit-text"><u>Let's go</u></div>
        </div>

        <div className="home-background">
          <img className="home-image" src={Background} />
        </div>
      </div>
    );
  }
}


export default HomePage;
