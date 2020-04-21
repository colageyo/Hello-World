import React, { Component } from 'react';

import './HomePage.css';
import Background from './assets/background_day.png';
import { MoodButton } from './MoodButton';

class HomePage extends Component {
  

  render() {
    const { isCovid } = this.props;
    return (
      <div className="home-page small-content">
        <div className="home-container">
          <div className="home-text">
            <div className="text large-text">Hello <u>Sydney !</u> </div>
            <div className="text small-text">I'm in the mood for something... </div>
          </div>
          <div className="button-container">
            <MoodButton mood={"sporty"} />
            <MoodButton mood={"romantic"} />
            <MoodButton mood={"artsy"} />
            <MoodButton mood={"delicious"} />
            <MoodButton mood={"indoors"} />
            <MoodButton isCovid={isCovid} mood={"outdoors"} />
            <MoodButton mood={"historic"} />
            <MoodButton mood={"geeky"} />
            <MoodButton mood={"family-friendly"} />
          </div>
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
