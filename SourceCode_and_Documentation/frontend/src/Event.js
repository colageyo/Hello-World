import React from "react";
import DayLogo from './assets/logo_day.png';
import './Event.css';

export const Event = (props) => {
  const {
    event: {
      event_id,
      name,
      url,
      image,
      summary,
      is_online,
      tags,
    }
  } = props;

  return (
    <div
      className='event-item'
      onClick={() => {
        props.onClick();
      }}
    >
      <div className="tag-banners">
        {event_id.includes('FOURSQUARE') && tags.includes('hungry') && <div className="tag-banner restaurant-banner">Local Eatery</div>}
        {tags.includes('indoors') && !tags.includes('hungry') && <div className="tag-banner indoors-banner">Indoor</div>}
        {is_online && <div className="tag-banner online-banner">Online</div>}
      </div>
      <img
        src={image === '' ? DayLogo : image}
        className='event-picture'
        alt='Sydney'
      />
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