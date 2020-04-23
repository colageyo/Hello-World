import React from 'react';
import { Link } from 'react-router-dom';
import './HelloWorldToolBar.css';
import './App.css';
import DayLogo from './assets/logo_day.png';
import SunsetLogo from './assets/logo_sunset.png';
import EveningLogo from './assets/logo_evening.png';
import SunriseLogo from './assets/logo_sunrise.png';
import RainyLogo from './assets/logo_rainy.png';
import { render } from '@testing-library/react';


function HelloWorldToolBar(props) {
  
  const styles = {
    sunset: SunsetLogo,
    day: DayLogo,
    rainy: RainyLogo,
    sunrise: SunriseLogo,
    evening: EveningLogo
  }

  return (
    <div className="nav-bar small-content">
      <div className="nav-bar-inner-container">
        <Link
          to='/'
        >
          <img className="logo" src={styles[props.style]} />
        </Link>
        <div className="text-container">
          <div className="text tool-bar-text button">
            <Link
              to='/recommend'
            > 
              Activities and Events
              </Link>
          </div>
          <div className="text tool-bar-text button">
            <Link
              to='/contact'
            >
              Contact Us
              </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default HelloWorldToolBar;
