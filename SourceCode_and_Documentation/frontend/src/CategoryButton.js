import React, {Component} from "react";
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
  delicious: Delicious,
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
    }

    handleClick= () => {
      this.props.onClick(this.props.category); 
    }

    render() {
        return (
            <div className={this.props.value ? 'category-button click-effect': 'category-button'} onClick={this.handleClick} >
              <div className="category-text text">
                {this.props.category} <img className="category-image" src={icons[this.props.category]}></img>
              </div>
            </div>
          );
    }
}

export default CategoryButton;
