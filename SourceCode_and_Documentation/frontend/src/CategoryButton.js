import React, { Component } from "react";
import { CovidDialog } from "./CovidDialog";

import "./CategoryButton.css";

import Artsy from "./icons/artsy.png";
import Delicious from "./icons/delicious.png";
import Family from "./icons/family.png";
import Geeky from "./icons/geeky.png";
import History from "./icons/history.png";
import Indoor from "./icons/indoor.png";
import Ouside from "./icons/outside.png";
import Romantic from "./icons/romantic.png";
import Sporty from "./icons/sporty.png";

const icons = {
  "family-friendly": Family,
  artsy: Artsy,
  hungry: Delicious,
  geeky: Geeky,
  historic: History,
  indoors: Indoor,
  outdoors: Ouside,
  romantic: Romantic,
  sporty: Sporty
};

class CategoryButton extends Component {
  constructor(props) {
    super(props);
    this.handleClick = this.handleClick.bind(this);
    this.state = {
      x: 0,
      y: 0,
      isDisabled: this.props.category == "outdoors"
    };
  }

  handleClick = () => {
    this.props.onClick(this.props.category);
  };

  onMouseMove = e => {
    this.setState({
      x: e.clientX,
      y: e.clientY
    });
  };

  onMouseLeave = () => {
    this.setState(() => ({
      x: 0,
      y: 0
    }));
  };

  render() {
    const covidLog =
      this.state.isDisabled && this.state.x != 0 && this.state.y != 0 ? (
        <CovidDialog top={this.state.y} left={this.state.x} />
      ) : null;
    return (
      <div
        className={
          this.props.value ? "category-button click-effect" : "category-button"
        }
        onClick={this.handleClick}
        onMouseMove={this.onMouseMove}
        onMouseLeave={this.onMouseLeave}
      >
        {/*{covidLog}*/}
        <div
          className={
            this.props.style === "evening" && this.props.value
              ? "category-text text text-white"
              : "category-text text"
          }
        >
          {this.props.category === 'hungry' ? 'delicious' : this.props.category}{" "}
          <img
            className="category-image"
            src={icons[this.props.category]}
          ></img>
        </div>
      </div>
    );
  }
}

export default CategoryButton;
