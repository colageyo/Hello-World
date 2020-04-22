import React, { Component } from "react";
import { Link } from "react-router-dom";


import './HomePage.css';
import DayBackground from './assets/background_day.png';
import SunsetBackground from './assets/background_sunset.png';
import EveningBackground from './assets/background_evening.png';
import SunriseBackground from './assets/background_sunrise.png';
import RainyBackground from './assets/background_rainy.png';
import blackArrow from "./assets/arrow_right_black.png";
import whiteArrow from "./assets/arrow_right_white.png";
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

    let arrowIcon;
    if (style === "evening") {
      arrowIcon = <img id="arrow" src={whiteArrow} />;
    } else {
      arrowIcon = <img id="arrow" src={blackArrow} />;
    }

    return (
      <div className="home-page small-content">
        <div className="home-container">
          <div className="home-text">
            <div className="text large-text">
              Hello <u>Sydney !</u>{" "}
            </div>
            <div className="text small-text">
              I'm in the mood for something...{" "}
            </div>
          </div>
          <div className="button-container">
            <MoodButton
              mood={"sporty"}
              onClick={() => this.props.toggleCategory("sporty")}
              value={this.props.categories["sporty"]}
            />
            <MoodButton
              mood={"romantic"}
              onClick={() => this.props.toggleCategory("romantic")}
              value={this.props.categories["romantic"]}
            />
            <MoodButton
              mood={"artsy"}
              onClick={() => this.props.toggleCategory("artsy")}
              value={this.props.categories["artsy"]}
            />
            <MoodButton
              mood={"hungry"}
              onClick={() => this.props.toggleCategory("hungry")}
              value={this.props.categories["hungry"]}
            />
            <MoodButton
              mood={"indoors"}
              onClick={() => this.props.toggleCategory("indoors")}
              value={this.props.categories["indoors"]}
            />
            <MoodButton
              isCovid={isCovid}
              mood={"outdoors"}
              onClick={() => !isCovid && this.props.toggleCategory("outdoors")}
              value={this.props.categories["outdoors"]}
            />
            <MoodButton
              mood={"historic"}
              onClick={() => this.props.toggleCategory("historic")}
              value={this.props.categories["historic"]}
            />
            <MoodButton
              mood={"geeky"}
              onClick={() => this.props.toggleCategory("geeky")}
              value={this.props.categories["geeky"]}
            />
            <MoodButton
              mood={"family-friendly"}
              onClick={() => this.props.toggleCategory("family-friendly")}
              value={this.props.categories["family-friendly"]}
            />
          </div>
          {Object.keys(this.props.categories).filter(
            tag => this.props.categories[tag]
          ).length > 0 ? (
            <div className="text lets-go">
              <u>
                <Link to="/recommend">Let's go {arrowIcon}</Link>
              </u>
            </div>
          ) : null}
        </div>

        <div className="home-background">
          <img className="home-image" src={styles[style]} />
        </div>
      </div>
    );
  }
}

export default HomePage;
