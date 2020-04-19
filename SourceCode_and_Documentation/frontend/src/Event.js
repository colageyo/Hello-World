import React from "react";
import './Event.css';

export const Event = (props) => {
  const {
    event: {
      name,
      url,
      image,
      summary
    }
  } = props;

  return (
    <a href={url}>
      <div
        className='event-item'
      >
        {image !== "" && <img
          src={image}
          className='event-picture'
          alt='Sydney'
        />}
        <div className='event-text'>
          <p>
            {name}
          </p>
          <p>
            {summary}
          </p>
        </div>
      </div>
    </a>
  );
};