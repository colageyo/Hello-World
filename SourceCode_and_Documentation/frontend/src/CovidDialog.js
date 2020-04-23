import React from 'react';
import './CovidDialog.css';

export const CovidDialog = (props) => {

  const style = {
    top: props.top,
    left: props.left
  }

  return (
    <div className="covid-dialog text" style={style}>
      Outdoor activities are disabled during COVID-19. Stay safe, stay inside ❤️
    </div>
  );
}
