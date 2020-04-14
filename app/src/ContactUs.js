import React, { Component } from 'react';
import './ContactUs.css';
import './App.css';

class ContactUsPage extends Component {
    constructor() {
        super();
        this.state = {
          width: window.innerWidth,
        };
    }
      
    componentWillMount() {
        window.addEventListener('resize', this.handleWindowSizeChange);
    }
    
    componentWillUnmount() {
        window.removeEventListener('resize', this.handleWindowSizeChange);
    }
    
    handleWindowSizeChange = () => {
        this.setState({ width: window.innerWidth });
    };

    render() {
        const { width } = this.state;
        const isMobile = width <= 500;
        if (isMobile) {
            return (
                <div>

                </div>
            );
        } else {
            return (
                <div className="contact-us-outer-container">
                    <div className="contact-us-inner-container">
                       <span id="title" className="text"> Get in Touch</span> 

                    </div>
                </div>
            );
        }
    }
}


export default ContactUsPage;
