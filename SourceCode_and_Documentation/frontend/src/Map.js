import React from 'react';
import ReactMapGL, { GeolocateControl } from 'react-map-gl';

import './Map.css';

const geolocateStyle = {
  position: 'absolute',
  top: 0,
  left: 0,
  margin: 10
};

const Map = () => {

  const [
    viewport,
    setViewport
  ] = React.useState({
    width: '100%',
    height: '100vh',
    latitude: 0,
    longitude: 0,
    zoom: 10
  });

  React.useEffect(() => {
    navigator.geolocation.getCurrentPosition(pos => {
      setViewport({
        ...viewport,
        latitude: pos.coords.latitude,
        longitude: pos.coords.longitude
      });
    });
  }, [])

  return (
    <div
      className='map'
    >
      <ReactMapGL
        mapStyle='mapbox://styles/mapbox/streets-v10'
        {...viewport}
        onViewportChange={viewport => setViewport(viewport)}
      >
        <GeolocateControl
          style={geolocateStyle}
          positionOptions={{ enableHighAccuracy: true }}
          trackUserLocation={true}
        />
      </ReactMapGL>
    </div>
  );
};

export default Map;
