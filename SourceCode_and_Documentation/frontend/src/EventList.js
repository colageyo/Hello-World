import React from 'react';
import './EventList.css';
import { Event } from './Event';

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
      <Event event={event} key={i} onClick={() => console.log('click!')} />
    ))}
  </div>
);

export default EventList;
