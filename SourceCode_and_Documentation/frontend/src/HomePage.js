import React, { Component } from 'react';
import Banner from './Banner';
import './Banner.css'
import {MoodButton} from './MoodButton';
import './HomePage.css';
import Background from './background_image.png';
import ClosingIcon from './closing-icon.png';



class HomePage extends Component {
  
    render() {
    return (

    <div className="body-main-container">
        
        <Banner/>

        <div className="body-inner-container">
          <div className="left-container">
            <div className="body-text-container">
              <div className="text large-text">Hello Sydney!</div>
              <div className="text small-text">I'm feeling for something...</div>
            </div>
            <div className="button-container">
              <div className='top-button-container'>
                <MoodButton mood={'sporty'}/>
                <MoodButton mood={'romantic'}/>
                <MoodButton mood={'artsy'}/>
                <MoodButton mood={'delicious'}/>
              </div>
              <div className='middle-button-container'>
                <MoodButton mood={'indoors'}/>
                <MoodButton mood={'outdoors'}/>
                          <MoodButton mood={'historic'}/>
                          <MoodButton mood={'geeky'}/>
                      </div>
                      <div className='bottom-button-container'>
                          <MoodButton mood={'family-friendly'}/>
                      </div>
                  </div>
              </div>

              <div className="body-image-container">
                  <img className="background" src={Background}/>
              </div>

          </div>

      </div>

    );
  }
}


export default HomePage;
