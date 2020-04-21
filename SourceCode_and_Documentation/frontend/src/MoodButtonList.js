import React, { Component } from "react";
import {MoodButton} from "./MoodButton";
import "./App.css";
import "./MoodButtonList.css";

const moods = [
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

class MoodButtonList extends Component {
  constructor(props) {
    super(props);
    this.state = new Map(moods.map(mood => [mood, false]));
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick = mood => {
    this.setState(state => ({
      [mood]: !state[mood]
    }));
  };

  render() {
    const moodButtons = moods.map(mood => (
      <MoodButton
        key={mood}
        mood={mood}
        onClick={this.handleClick}
        value={this.state[mood]}
      />
    ));
    return <div className="button-container">{moodButtons}</div>;
  }
}

export default MoodButtonList;