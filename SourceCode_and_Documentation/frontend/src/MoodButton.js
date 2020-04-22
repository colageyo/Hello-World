import React from "react";
import { CovidDialog } from './CovidDialog';
import "./MoodButton.css";

const icons = {
  hungry: '🍔',
  artsy: '🎨',
  sporty: '⚽',
  romantic: '💖',
  outdoors: '🌞',
  indoors: '🚪',
  geeky: '🎮',
  historic: '🏛️',
  'family-friendly': '🧒'
};

export const MoodButton = (props) => {
  const [x, setX] = React.useState();
  const [y, setY] = React.useState();

  const onMouseMove = (e) => {
    setX(e.clientX + 5);
    setY(e.clientY + 5);
  }  

  const onMouseLeave = () => {
    setX(undefined);
    setY(undefined);
  }

  const { mood, onClick, isCovid = false } = props;
  const isDisabled = mood === "outdoors" && isCovid;

  return (
    <div className={`mood-button ${props.value ? 'mood-button-selected' : ''}`} onClick={onClick} onMouseMove={onMouseMove} onMouseLeave={onMouseLeave} >
      {isDisabled && x && y && <CovidDialog top={y} left={x} />}
      <div className="mood-text text" disabled={isDisabled}>
        {mood === 'hungry' ? 'delicious' : mood} {icons[mood] || ""}
      </div>
    </div>
  );
};
