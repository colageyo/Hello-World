import React from 'react';
import Axios from 'axios';

import EventList from './EventList';
import Map from './Map';
import './RecommendationPage.css';

const RecommendationPage = () => {

  const [
    events,
    setEvents
  ] = React.useState([]);

  React.useEffect(() => {
    Axios.post(
      'http://localhost:5000/events/recommended',
      {
        tags: []
      },
      {
        headers: {
          'Content-Type': 'application/json'
        }
      }
    ).then(res => {
      setEvents(res.data);
    });
  }, []);

  return (
    <div
      className="recommendation-page"
    >
      <div className='recommendation-panel'>
        <EventList
          events={events}
        />
        <Map/>
      </div>
    </div>
  );
};

export default RecommendationPage;
