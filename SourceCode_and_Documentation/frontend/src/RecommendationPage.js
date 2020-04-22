import React from 'react';
import Axios from 'axios';

import CategoryBar from './CategoryBar';
import EventList from './EventList';
import Map from './Map';
import './RecommendationPage.css';

const RecommendationPage = (props) => {
  const { tags = [], isCovid, toggleCategory, style } = props;
  const [
    events,
    setEvents
  ] = React.useState([]);

  const [
    selectedEvent,
    setSelectedEvent
  ] = React.useState();

  const [temperature, setTemperature] = React.useState();
  const [condition, setCondition] = React.useState();
  const [isLocal, setIsLocal] = React.useState(false);

  React.useEffect(() => {
    Axios.get(
      'http://localhost:5000/conditions'
    ).then(res => {
      const { conditions: { weather, temperature } } = res.data;
      const description = weather.split('-')[1].trim();
      setCondition(description);
      setTemperature(temperature);
    });
  }, []);

  React.useEffect(() => {
    Axios.post(
      'http://localhost:5000/events/recommended',
      {
        tags: Object.keys(tags).filter(tag => tags[tag]),
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

  const handleLocal = () => {
    setIsLocal(!isLocal);
  };

  const turnOffLocal = () => {
    setIsLocal(false);
  };

  return (
    <div
      className="recommendation-page"
    >
      <div style={{ flexGrow: 1 }}>
        <CategoryBar
          categories={tags} 
          toggleCategory={toggleCategory}
          isLocal={isLocal}
          isCovid={isCovid}
          handleLocal={handleLocal}
          turnOffLocal={turnOffLocal}
          style={style}
        />
      </div>
      {condition !== undefined && temperature !== undefined &&
      <div className='weather-forecast text'>
        Today, you can expect <b>{condition}</b>, with a temperature of <b>{temperature} degrees celcius</b>.
        {
          isCovid && ' Remember to stay safe, stay inside ❤'
        }
      </div>
      }
      <div className='recommendation-panel'>
        <EventList
          isLocal={isLocal}
          isCovid={isCovid}
          events={events}
          setSelectedEvent={setSelectedEvent}
        />
        <Map
          selectedEvent={selectedEvent}
        />
      </div>
    </div>
  );
};

export default RecommendationPage;
