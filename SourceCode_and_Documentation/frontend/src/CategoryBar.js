import React, { Component } from "react";
import CategoryButton from "./CategoryButton";
import "./App.css";
import "./CategoryBar.css";

const categories = [
  "family-friendly",
  "artsy",
  "delicious",
  "geeky",
  "historic",
  "indoors",
  "outdoors",
  "romantic",
  "sporty"
];

class CategoryBar extends Component {
  constructor(props) {
    super(props);
    this.state = new Map(categories.map(cat => [cat, false]));
    this.handleClick = this.handleClick.bind(this);
    this.shouldDisplay = this.shouldDisplay.bind(this);
    this.handleLocal = this.handleLocal.bind(this);
  }

  handleLocal() {
    categories.forEach(category => {
      this.setState(state => ({
        [category]: false
      }));
    });
    this.props.handleLocal();
  };

  handleClick = category => {
    this.props.turnOffLocal();
    this.setState(state => ({
      [category]: !state[category]
    }));
  };

  shouldDisplay(c) {
    const { isCovid } = this.props;
    return isCovid && c === 'outdoors' ? false : true;
  }

  render() {
    const { isCovid = false, isLocal } = this.props;
    const categoryButtons = categories.filter(this.shouldDisplay).map(category => (
      <CategoryButton
        key={category}
        category={category}
        onClick={this.handleClick}
        value={this.state[category]}
      />
    ));
    return <div className="category-bar-scroll-filter">
      {
        isCovid ? <CategoryButton
          key='local'
          category='support local 💖'
          onClick={this.handleLocal}
          value={isLocal}
        /> : null
      }
      {categoryButtons}
    </div>;
  }
}

export default CategoryBar;
