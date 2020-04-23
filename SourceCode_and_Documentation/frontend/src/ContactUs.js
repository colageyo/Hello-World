import React, { Component } from "react";
import "./ContactUs.css";
import "./App.css";

class ContactUsPage extends Component {
  constructor(props) {
    super();
  }

  render() {
    if (this.props.style === "evening") {
      return (
        <div className="contact-us-outer-container">
          <div className="contact-us-inner-container">
            <span id="title" className="text">
              {" "}
              Get in Touch
            </span>
            <input
              className="input-white text"
              type="text"
              id="name"
              name="name"
              placeholder="Name"
            />
            <input
              className="input-white text"
              type="text"
              id="email"
              name="email"
              placeholder="Email"
            />
            <span className="text message-text">Message</span>
            <textarea className="message-white" name="msg"></textarea>
            <div className="send-request text button">Send Request</div>
          </div>
        </div>
      );
    } else {
      return (
        <div className="contact-us-outer-container">
          <div className="contact-us-inner-container">
            <span id="title" className="text">
              {" "}
              Get in Touch
            </span>
            <input
              className="input text"
              type="text"
              id="name"
              name="name"
              placeholder="Name"
            />
            <input
              className="input text"
              type="text"
              id="email"
              name="email"
              placeholder="Email"
            />
            <span className="text message-text">Message</span>
            <textarea className="message" name="msg"></textarea>
            <div className="send-request text button">Send Request</div>
          </div>
        </div>
      );
    }
  }
}

export default ContactUsPage;
