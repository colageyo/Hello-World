import React, { Component } from 'react';
import ClosingIcon from './assets/closing_icon_black.png';

class Banner extends Component {
    render() {
        return (
            <div className='banner-main-container' >
                <div className='row'>
                    <div className='text' style={{ color: 'black' }}>
                        Stay safe in these difficult times. <a onClick={pageRedirect} ><u>Learn More</u></a>
                    </div>
                    <img className='closing-icon' src={ClosingIcon} onClick={collapseBanner} />
                </div>
            </div>

        );
    }
}

function pageRedirect() {
    window.location.href = "https://www.health.gov.au/news/health-alerts/novel-coronavirus-2019-ncov-health-alert";
}

function collapseBanner() {
    document.getElementsByClassName("banner-main-container")[0].style.display = "none";
}

export default Banner;  
