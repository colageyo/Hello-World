import React from 'react';
import './EventList.css';
import { Event } from './Event';

const EventList = (
  {
    isLocal,
    isCovid,
    events,
    setSelectedEvent
  }
) => {
  const shouldShowEvent = (e) => {
    if (isLocal) {
      return e.event_id.includes('FOURSQUARE') && e.tags.includes("hungry");
    } else if (isCovid) {
      return e.event_id.includes('FOURSQUARE') && e.tags.includes("hungry") ? true : e.is_online;
    }
    return true;
  };
  
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
