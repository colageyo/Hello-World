import React from 'react';
import './EventList.css';
import { Event } from './Event';

const EventList = (
  {
    events,
    setSelectedEvent
  }
) => (
  <div
    className='event-list text'
  >
    <p>
      {events.length} events and activities just for you
    </p>
    {events.map((event, i) => (
      <Event event={event} key={i} onClick={() => setSelectedEvent(event)} />
    ))}
  </div>
);

export default EventList;
