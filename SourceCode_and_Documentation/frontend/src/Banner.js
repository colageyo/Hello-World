import React, { Component } from 'react';
import ClosingIcon from './assets/closing_icon_black.png';
import "./Banner.css";

class Banner extends Component {
    render() {
        return (
            <div className='banner-main-container' >
                <div id='row'>
                    <div className='covid-text'>
                        Stay safe in these difficult times. <a href="https://www.health.gov.au/news/health-alerts/novel-coronavirus-2019-ncov-health-alert" target="_blank" ><u>Learn More</u></a>
                    </div>
                    <img className='closing-icon' src={ClosingIcon} onClick={collapseBanner} />
                </div>
            </div>

        );
    }
}

function collapseBanner() {
    document.getElementsByClassName("banner-main-container")[0].style.display = "none";
}

export default Banner;  
