import React, { Component } from 'react';
import ClosingIcon from './assets/closing_icon_black.png';


class Banner extends Component {
    render() {
        return (
        
        <div className='banner-main-container' > 
            <div className='row'>
                <div className='text'>
                    Stay safe in these difficult times. Learn More
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
