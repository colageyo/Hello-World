import React, { Component } from 'react';

import './HomePage.css';
import DayBackground from './assets/background_day.png';
import SunsetBackground from './assets/background_sunset.png';
import EveningBackground from './assets/background_evening.png';
import SunriseBackground from './assets/background_sunrise.png';
import RainyBackground from './assets/background_rainy.png';
import { MoodButton } from './MoodButton';

class HomePage extends Component {

  render() {
    
    const { isCovid, style } = this.props;
    const background = SunsetBackground;
    const styles = {
      sunset: SunsetBackground,
      day: DayBackground,
      rainy: RainyBackground,
      sunrise: SunriseBackground,
      evening: EveningBackground
    }

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
        </div>

        <div className="home-background">
          <img className="home-image" src={styles[style]} />
        </div>
      </div>
    );
  }
}


export default HomePage;
