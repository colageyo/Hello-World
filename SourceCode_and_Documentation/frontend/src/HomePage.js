import React, { Component } from 'react';
import Banner from './Banner';
import './Banner.css'
import './HomePage.css';
import Background from './assets/background_image.png';
import { MoodButton } from './MoodButton';

class HomePage extends Component {

  render() {
    return (
      <div className="home-page small-content">
        <Banner />
        <div className="home-container">
          <div className="home-text">
            <div className="text large-text">Hello Sydney ! </div>
            <div className="text small-text">I'm in the mood for something... </div>
          </div>
          <div className="button-container" >
            <MoodButton mood={"sporty"} />
            <MoodButton mood={"romantic"} />
            <MoodButton mood={"artsy"} />
            <MoodButton mood={"delicious"} />
            <MoodButton mood={"indoors"} />
            <MoodButton mood={"outdoors"} />
            <MoodButton mood={"historic"} />
            <MoodButton mood={"geeky"} />
            <MoodButton mood={"family-friendly"} />
          </div>
        </div>

        <div className="home-background">
          <img className="home-image" src={Background} />
        </div>
      </div>
    );
  }
}


export default HomePage;
