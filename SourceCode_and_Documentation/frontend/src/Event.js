import React from "react";
import './Event.css';

export const Event = (props) => {
  const {
    event: {
      name,
      url,
      image,
      summary,
      is_online,
    }
  } = props;

  return (
    <div
      className='event-item'
      onClick={() => {
        props.onClick();
      }}
    >
      {is_online && <div className="online-banner">Online Event</div>}
      {image !== "" && <img
        src={image}
        className='event-picture'
        alt='Sydney'
      />}
      <div className='event-text'>
        <p>
          {name}
        </p>
        <p className='event-summary'>
          {summary}
        </p>
        <a href={url} target='_blank' className='event-summary learn-more' onClick={e => {
          e.stopPropagation();
        }}>
          Learn more
        </a>
      </div>
    </div>
  );
};