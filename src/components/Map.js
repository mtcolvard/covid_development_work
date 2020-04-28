import React from 'react'
import MapGl from 'react-map-gl'
import axios from 'axios'
import 'mapbox-gl/dist/mapbox-gl.css'

import Marker from './Marker'

class Map extends React.Component {
  constructor() {
    super()

    this.state = {
      bikePoints: []
    }
    this.handleMapClick = this.handleMapClick.bind(this)
  }

  componentDidMount() {
    navigator.geolocation.getCurrentPosition(({ coords }) => {
      this.getBikePoints(coords.latitude, coords.longitude)
    })
  }

  handleMapClick({ lngLat }) {
    this.setState({ showPopup: false },
    this.getBikePoints(lngLat[1], lngLat[0]))
  }

  getBikePoints(lat, lon) {
    axios.get(
      'https://api.tfl.gov.uk/bikepoint',
      { params: { lat, lon, radius: 1000 } }
    )
      .then(res => this.setState({ bikePoints: res.data.places }))
      .catch(err => console.log(err))
  }

  render() {
    const { bikePoints } = this.state
    return (
      <MapGl
        height={'100vh'}
        width={'100vw'}
        mapboxApiAccessToken={process.env.MAPBOX_TOKEN}
        latitude={51.515}
        longitude={-0.078}
        zoom={12}
        mapStyle="mapbox://styles/mapbox/streets=v9"
        onClick={this.handleMapClick}
      >
        {bikePoints.map(point => (
          <Marker
            key={point.id}
            onClick={this.handlePinCLick}
            {...point}
          />
        ))}
      </MapGl>
    )
  }
}

export default Map
