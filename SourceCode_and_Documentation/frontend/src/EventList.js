import React from 'react';
import './EventList.css';

const EventList = (
  {
    events
  }
) => (
  <div
    className='event-list text'
  >
    <p>
      {events.length} events and activities just for you
    </p>
    {events.map((event, i) => (
      <div
        className='event-item'
        key={i}
      >
        <img
          src='https://miro.medium.com/max/4250/1*-MklWDSjKS5vWEG5ZYXCww.jpeg'
          className='picture'
          alt='Sydney'
        />
        <p>
          {event.name}
        </p>
        <p>
          bruh
        </p>
      </div>
    ))}
  </div>
);

export default EventList;
