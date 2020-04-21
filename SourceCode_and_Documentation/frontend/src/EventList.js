import React from 'react';
import './EventList.css';
import { Event } from './Event';

const EventList = (
  {
    isCovid,
    events,
    setSelectedEvent
  }
) => {
  const shouldShowEvent = (e) => isCovid ? e.is_online : true;
  const filteredEvents = events.filter(shouldShowEvent);
  return (
    <div
      className='event-list text'
    >
      <p>
        {filteredEvents.length} events and activities just for you
      </p>
      {filteredEvents.map((event, i) => (
        <Event event={event} key={i} onClick={() => setSelectedEvent(event)} />
      ))}
    </div>
  )
};

export default EventList;
