import React from "react";
import "./MoodButton.css";

const icons = {
  delicious: "🍔",
  artsy: "🎨",
  sporty: "⚽",
  romantic: "💖",
  outdoors: "🌞",
  indoors: "🚪",
  geeky: "🎮",
  historic: "🏛️",
  "family-friendly": "🧒",
};

export const MoodButton = (props) => {
  const { mood, onClick } = props;
  
  return (
    <div className="mood-button" onClick={onClick}>
      <div className="mood-text text">
        {mood} {icons[mood] || ""}
      </div>
    </div>
  )
};
